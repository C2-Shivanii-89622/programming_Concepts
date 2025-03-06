text = """Python is a high-level, general-purpose programming language. Its 
design philosophy emphasizes code readability with the use of significant 
indentation. Python is dynamically typed and garbage-collected. It supports 
multiple programming paradigms, including structured, object-oriented and 
functional programming."""

new_text = text.lower()
def Text_count():
    text_count = {}
    print("-" * 80)

    for alphabet in new_text:
        count = text_count.get(alphabet)
        if count == None:
            text_count[alphabet] = 1
        else:
            text_count[alphabet] +=1
    
    print(text_count)

Text_count()