import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

# Create database tables if they don't exist
def create_tables(conn):
    cursor = conn.cursor()

    # Create flashcard_sets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flashcard_sets (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL
        )
    ''')

    # Create flashcards table with foreign key reference to flashcard_sets
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            set_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            definition TEXT NOT NULL,
            FOREIGN KEY (set_id) REFERENCES flashcard_sets(id)               
        )
    ''')

# Add a new flashcard set to the database
def add_set(conn, name):
    cursor = conn.cursor()

    # Insert the set name into flashcard_sets table
    cursor.execute('''
        INSERT INTO flashcard_sets (name)
        VALUES (?)
    ''', (name,))

    set_id = cursor.lastrowid
    conn.commit()

    return set_id

# Function to add a flashcard to the database
def add_card(conn, set_id, word, definition):
    cursor = conn.cursor()

    # Execute SQL query to insert a new flashcard into the database
    cursor.execute('''
        INSERT INTO flashcards (set_id, word, definition)
        VALUES (?, ?, ?)
    ''', (set_id, word, definition))

    # Get the ID of the newly inserted card
    card_id = cursor.lastrowid
    conn.commit()

    return card_id

# Function to retrieve all flashcard sets from the database
def get_sets(conn):
    cursor = conn.cursor()

    # Execite SQL query to fetch all flashcard sets
    cursor.execute('''
        SELECT id, name FROM flashcard_sets
    ''')

    rows = cursor.fetchall()
    sets = {row[1]: row[0] for row in rows} # Create a dictionary of sets (name: id)

    return sets

# Function to retrieve all flashcards of a specific set
def get_cards(conn, set_id):
    cursor = conn.cursor()

    cursor.execute('''
        SELECT word, definition FROM flashcards
        WHERE set_id = ?
    ''', (set_id,))

    rows = cursor.fetchall()
    cards = [(row[0], row[1]) for row in rows] # Create a list of cards (word, definition)

    return cards

# Function to delete a flashcard set from the database
def delete_set(conn, set_id):
    cursor = conn.cursor()

    # Execute SQL query to delete a flashcard set
    cursor.execute('''
        DELETE FROM flashcard_sets
        WHERE id = ?
    ''', (set_id,))

    conn.commit()
    sets_combobox.set('')
    clear_flashcard_display()
    populate_sets_combobox()

    # Clear the current_cards list and reset card_index
    global current_cards, card_index
    current_cards = []
    card_index = 0

# Function to create a new flashcard set
def create_set():
    set_name = set_name_var.get()
    if set_name:
        if set_name not in get_sets(conn):
            set_id = add_set(conn, set_name)
            populate_sets_combobox()
            set_name_var.set('')

            # Clear the input fields
            set_name_var.set('')
            word_var.set('')
            definition_var.set('')

def add_word():
    set_name = set_name_var.get()
    word = word_var.get()
    definition = definition_var.get()

    if set_name and word and definition:
        if set_name not in get_sets(conn):
            set_id = add_set(conn, set_name)
        else:
            set_id = get_sets(conn)[set_name]

        add_card(conn, set_id, word, definition)

        word_var.set('')
        definition_var.set('')

        populate_sets_combobox()

def populate_sets_combobox():
    sets_combobox['values'] = tuple(get_sets(conn).keys())

# Function to delete a selected flashcard set
def delete_selected_set():
    set_name = sets_combobox.get()

    if set_name:
        result = messagebox.askyesno(
            'Confirmation', f'Are you sure you want to delete the "{set_name}" set?'
        )

        if result == tk.YES:
            set_id = get_sets(conn)[set_name]
            delete_set(conn, set_id)
            populate_sets_combobox()
            clear_flashcard_display()

def select_set():
    set_name = sets_combobox.get()

    if set_name:
        set_id = get_sets(conn)[set_name]
        cards = get_cards(conn, set_id)

        if cards:
            display_flashcards(cards)
        else:
            word_label.config(text="No cards in this set")
            definition_label.config(text='')
    else:
        # Clear the current cards list and reset card index
        global current_cards, card_index
        current_cards = []
        card_index = 0
        clear_flashcard_display()

def display_flashcards(cards):
    global card_index
    global current_cards

    card_index = 0
    current_cards = cards
    
    # Clear the display
    if not cards:
        clear_flashcard_display()
    else:
        show_card()
    
    show_card()

def clear_flashcard_display():
    word_label.config(text='')
    definition_label.config(text='')

# Function to display the current flashcards word
def show_card():
    global card_index
    global current_cards

    if current_cards:
        if 0 <= card_index < len(current_cards):
            word, _ = current_cards[card_index]
            word_label.config(text=word)
            definition_label.config(text='')
        else:
            clear_flashcard_display()
    else:
        clear_flashcard_display()

# Function to flip the current card and display its definition
def flip_card():
    global card_index
    global current_cards

    if current_cards:
        _, definition = current_cards[card_index]
        definition_label.config(text=definition)

# Function to move to the next card
def next_card():
    global card_index
    global current_cards

    if current_cards:
        card_index = min(card_index + 1, len(current_cards) -1)
        show_card()

# Function to move to the previous card
def prev_card():
    global card_index
    global current_cards

    if current_cards:
        card_index = max(card_index - 1, 0)
        show_card()

if __name__ == '__main__':
    # Connect to the SQLite database and create tables
    conn = sqlite3.connect('flashcards.db')
    create_tables(conn)

    # Create the main GUI window
    root = tk.Tk()
    root.title('Flashcards App')
    root.geometry('500x400')

    # Apply styling to the GUI elements
    style = Style(theme='superhero')
    style.configure('TLabel', font=('TkDefaultFont', 18))
    style.configure('TButton', font=('TkDefaultFont', 16))

    # Set up variables for storing user input
    set_name_var = tk.StringVar()
    word_var = tk.StringVar()
    definition_var = tk.StringVar()

    # Create a notebook widget to manage tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create the "Create Set" tab and its content
    create_set_frame = ttk.Frame(notebook)
    notebook.add(create_set_frame, text='Create Set')

    # Label and Entry widgets for entering set name, word and definition
    ttk.Label(create_set_frame, text='Set Name:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Word:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=word_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Definition:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=definition_var, width=30).pack(padx=5, pady=5)

    # Button to add a word to the set 
    ttk.Button(create_set_frame, text='Add Word', command=add_word).pack(padx=5, pady=10)
    
    # Button to save the set 
    ttk.Button(create_set_frame, text='Save Set', command=create_set).pack(padx=5, pady=10)

    # Create the "Select Set" tab and its content
    select_set_frame = ttk.Frame(notebook)
    notebook.add(select_set_frame, text="Select Set")

    # Combobox widget for selecting existing flashcard sets
    sets_combobox = ttk.Combobox(select_set_frame, state='readonly')
    sets_combobox.pack(padx=5, pady=40)

    # Button to select a set 
    ttk.Button(select_set_frame, text='Select Set', command=select_set).pack(padx=5, pady=5)

    # Button to delete a set 
    ttk.Button(select_set_frame, text='Delete Set', command=delete_selected_set).pack(padx=5, pady=5)

    # Create the "Learn mode" tab and its content
    flashcards_frame = ttk.Frame(notebook)
    notebook.add(flashcards_frame, text='Learn Mode')

    # Initialize variables for tracking card index and current cards
    card_index = 0
    current_tabs = []

    # Label to display the word on flashcards
    word_label = ttk.Label(flashcards_frame, text='', font=('TkDefaultFont', 24))
    word_label.pack(padx=5, pady=40)

    # Label to display the definition on flashcards
    definition_label = ttk.Label(flashcards_frame, text='')
    definition_label.pack(padx=5, pady=5)

    # Button to flip the flashcard 
    ttk.Button(flashcards_frame, text='Flip', command=flip_card).pack(side='left', padx=5, pady=5)

    # Button to view the next flashcard 
    ttk.Button(flashcards_frame, text='Next', command=next_card).pack(side='right', padx=5, pady=5)

    # Button to view the previous flashcard 
    ttk.Button(flashcards_frame, text='Previous', command=prev_card).pack(side='right', padx=5, pady=5)

    populate_sets_combobox()

    root.mainloop()