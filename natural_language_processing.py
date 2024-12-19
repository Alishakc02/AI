import nltk  # Import NLTK module

# Download the necessary resources for NLTK (book includes word tokenizers, POS taggers, etc.)
nltk.download("book")

# Sentence to be tokenized
sentence = """Tokenization is the process of breaking text into smaller units called tokens."""

# Tokenize the sentence into words
tokens = nltk.word_tokenize(sentence)
print("Tokens:", tokens)

# Apply POS tagging
tagged = nltk.pos_tag(tokens)
print("POS Tagged:", tagged)
