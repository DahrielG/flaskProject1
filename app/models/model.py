sentence = "Hello"
def count(sentence):
     sentence = sentence.replace(" ", "")
     sentence = sentence.replace(".", "")
     sentence = sentence.replace(",", "")
     sentence = sentence.replace("!", "")
     sentence = sentence.replace("?", "")
     sentence = sentence.replace("'", "")
     sentence = sentence.replace('"', "")
     length = len(sentence)
     return length

def nums(sentence):
    if sentence%2==0:
        return "even"
    else:
        return "odd"
