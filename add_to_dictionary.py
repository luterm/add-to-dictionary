
from googletrans import Translator
import sys
import os

# Initialize the translator
translator = Translator()

# Get the selected text from standard input
selected_text = sys.stdin.read().strip()

# Check if text is empty
if not selected_text:
    print("No text selected")
    sys.exit(0)

# Translate the text from English to Polish
try:
    translation = translator.translate(selected_text, src='en', dest='pl').text
    if translation is None:
        raise ValueError("Translation returned None")
except Exception as e:
    print(f"Translation error: {e}")
    sys.exit(1)

# Define the dictionary file path (in iCloud Drive)
dictionary_path = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/personal_dictionary.txt")

# Save the word and its translation to the file
with open(dictionary_path, 'a', encoding='utf-8') as f:
    f.write(f"{selected_text}: {translation}\n")

# Output the translation (for user feedback)
print(translation)