import os
import shutil

# Define the directory path
ddir = "/Users/alinachudnova/Downloads"

# Create subdirectories if they don't exist
if not os.path.exists(ddir + "/Images"):
    os.makedirs(ddir + "/Images")
if not os.path.exists(ddir + "/Music"):
    os.makedirs(ddir + "/Music")
if not os.path.exists(ddir + "/Videos"):
    os.makedirs(ddir + "/Videos")
if not os.path.exists(ddir + "/Documents"):
    os.makedirs(ddir + "/Documents")
if not os.path.exists(ddir + "/Code"):
    os.makedirs(ddir + "/Code")
if not os.path.exists(ddir + "/Other"):
    os.makedirs(ddir + "/Other")

# Lists of file extensions for different categories
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
music_extensions = [".mp3", ".wav", ".aiff"]
video_extensions = [".mp4"]
doc_extensions = [".txt", ".pdf", ".docx", ".doc"]
code_extensions = [".py", ".html", ".css", ".js", ".md"]

# Iterate through files in the directory
for file in os.listdir(ddir):
    # Skip processing if the item is a subdirectory
    if os.path.isdir(ddir + "/" + file):
        continue

    # Skip processing of .DS_Store files
    if file == ".DS_Store":
        continue

    # Get the file extension in lowercase
    extension = os.path.splitext(file)[1].lower()

    # Move the file to appropriate subdirectories based on the extension
    if extension in image_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Images")
    elif extension in music_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Music")
    elif extension in video_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Videos")
    elif extension in doc_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Documents")
    elif extension in code_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Code")
    else:
        shutil.move(ddir + "/" + file, ddir + "/Other")