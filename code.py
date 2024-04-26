import re
from collections import Counter
from nltk.corpus import stopwords

# Download NLTK stopwords if not already downloaded
import nltk
nltk.download('stopwords')

# Get NLTK English stopwords
stop_words = set(stopwords.words('english'))

# Function to clean text and count word frequency
def count_word_frequency(text):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    # Split the text into words
    words = cleaned_text.split()
    # Remove stop words
    words = [word for word in words if word not in stop_words]
    # Count word frequency
    word_freq = Counter(words)
    return word_freq

# Read the contents of the file
with open("paragraphs.txt", "r") as file:
    text = file.read()

# Count word frequency
word_freq = count_word_frequency(text)

# Display word frequency count to the console
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
