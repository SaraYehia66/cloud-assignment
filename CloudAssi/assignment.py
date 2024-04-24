from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Read the contents of the "paragraphs.txt" file
with open("paragraphs.txt", "r",encoding="utf-8") as file:
        text = file.read()
        
# Remove punctuation 
text = re.sub(r'[^\w\s]', '', text)

# Tokenize the text
text_words = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words("english"))
filtered_words = [word.lower() for word in text_words if word.lower() not in stop_words]

# Remove 'also' as it's stopword
filtered_words = [word for word in filtered_words if word != 'also']

# Join filtered words back into a sentence
filtered_text = " ".join(filtered_words)

print("\nFiltered text (after removing stop words):\n", filtered_text)

# Count word frequency
word_freq = Counter(filtered_words)

# Display word frequency count
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")

# Find word with maximum frequency
max_word, max_freq = word_freq.most_common(1)[0]
print(f"\nWord with maximum frequency: '{max_word}' (Frequency: {max_freq})")