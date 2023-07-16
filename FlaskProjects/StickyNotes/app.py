from flask import Flask, render_template, request
import json

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    load_notes() # Load notes from file
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    # Get the note text and color from the form submission
    note_text = request.form['note_text']
    note_color = request.form['note_color']
    # Add the note to the list of notes
    notes.append({'text': note_text, 'color': note_color})
    save_notes() # Save notes to file
    return index()

@app.route('/delete_note/<int:note_id>', methods=['GET', 'POST'])
def delete_note(note_id):
    if request.method == 'POST':
        # Delete the note with the given ID from the list of notes
        del notes[note_id]
        save_notes() # Save notes to file
    # Return the updated index page
    return index()

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)