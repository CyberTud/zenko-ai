from googletrans import Translator

# Create a Translator object
translator = Translator()

# Translate text
text = "Hello, how are you?"
translated = translator.translate(text, src='en', dest='fr')

# Print the translation
print(f"Original: {text}")
print(f"Translation: {translated.text}")