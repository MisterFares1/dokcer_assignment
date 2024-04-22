import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
import os

# Download NLTK resources (run only once) remove the  #if you haven't downloaded these 2 packages yet
nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords_from_file(input_file, output_file):
    # Read text from input file
    with open(input_file, 'r') as file:
        text = file.read()

    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Get the list of English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Reconstruct the text without stopwords
    filtered_text = ' '.join(filtered_tokens)
    
    # Write filtered text to output file
    with open(output_file, 'w') as file:
        file.write(filtered_text)


def count_word_frequency(input_file):
    # Read text from input file
    with open(input_file, 'r') as file:
        text = file.read()

    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()

    # Tokenize the text
    words = text.split()

    # Count word frequency
    word_frequency = Counter(words)
    
    return word_frequency

# Construct file paths using the relative path to 'paragraphs.txt' within the container
input_file_path = 'paragraphs.txt'
output_file_path = 'paragraphs2.txt'

# Get the absolute paths to 'input_file_path' and 'output_file_path' within the container
input_file_path_absolute = os.path.abspath(input_file_path)
output_file_path_absolute = os.path.abspath(output_file_path)

# Let's run the code
remove_stopwords_from_file(input_file_path_absolute, output_file_path_absolute)
print("Stop words removed from the text in", input_file_path, "and saved to", output_file_path)
word_frequency = count_word_frequency(input_file_path_absolute)

# Print word frequency
for word, frequency in word_frequency.items():
    print(word, ":", frequency)
