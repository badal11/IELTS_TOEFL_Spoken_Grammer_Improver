import spacy

def grammar_check(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    # Accessing grammar errors (I will customize this later)
    grammar_errors = [error.text for error in doc._.suggestions]

    return doc, grammar_errors


if __name__ == '__main__':
    transcribed_text = "Your transcribed text here"  # I will Replace it with actual transcribed text
    doc, grammar_errors = grammar_check(transcribed_text)
    print("Grammar Errors:", grammar_errors)
