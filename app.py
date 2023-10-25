# EZHIAN WILSON - 22121128
# SANSKAR GAUR - 22121133


import tkinter as tk
from tkinter import scrolledtext, filedialog
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

# Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

def open_file():
    file_path = filedialog.askopenfilename(title='Select File',
                                           filetypes=[('Text Files', '*.txt'),
                                                       ('All Files', '*.*')])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_input.delete("1.0", tk.END)  # Clear existing text
            text_input.insert(tk.END, file.read())  # Insert text from file

def evaluate_text():
    text = text_input.get("1.0", tk.END)  # Get text from text_input widget
    blob = TextBlob(text)
    
    # Basic Text Analysis
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    num_sentences = len(sentences)
    num_words = len(words)
    avg_words_per_sentence = num_words / num_sentences if num_sentences > 0 else 0
    stop_words = set(stopwords.words('english'))
    non_stop_words = [word for word in words if word.lower() not in stop_words]
    non_stop_word_proportion = len(non_stop_words) / num_words if num_words > 0 else 0
    
    # Sentiment Analysis
    sentiment = blob.sentiment
    
    # Spelling Correction (displaying a snippet for brevity)
    corrected_text_snippet = str(blob.correct())[:100]  # Display first 100 characters of corrected text
    
    result.set(f'Basic Text Analysis:\n'
               f'Number of sentences: {num_sentences}\n'
               f'Number of words: {num_words}\n'
               f'Average words per sentence: {avg_words_per_sentence:.2f}\n'
               f'Proportion of non-stop words: {non_stop_word_proportion:.2f}\n\n'
               f'Sentiment Analysis:\n'
               f'Polarity: {sentiment.polarity:.2f} (negative: -1, positive: 1)\n'
               f'Subjectivity: {sentiment.subjectivity:.2f} (objective: 0, subjective: 1)\n\n'
               f'Spelling Correction Suggestion (snippet):\n{corrected_text_snippet}...')

# Create main window
window = tk.Tk() window.title("NLP Evaluation in Basic English Assessment")

# Create a scrolled text widget for text input
text_input = scrolledtext.ScrolledText(window, width=60, height=20)
text_input.pack()

# Create a button to open a file
open_file_button = tk.Button(window, text="Open File", command=open_file)
open_file_button.pack()

# Create a button to trigger evaluation
eval_button = tk.Button(window, text="Evaluate Text", command=evaluate_text)
eval_button.pack()

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
