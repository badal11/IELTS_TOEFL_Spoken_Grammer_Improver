def highlight_errors_and_correct(doc, grammar_errors):
    highlighted_text = doc.text
    for error in grammar_errors:
        highlighted_text = highlighted_text.replace(error, f'***{error}***')

    return highlighted_text
