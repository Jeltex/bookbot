def get_words_count(text):
    words = text.split()
    return (len(words))

def get_char_count(text):
    charcount = {}
    text = text.lower()
    for char in text:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1
            

    return(charcount)

def get_char_list(chars):
    charlist = []
    for char in chars:
        chardict = {"name": char, "num": chars[char]}
        charlist.append(chardict)
    charlist.sort(reverse=True, key=sort_on)
    
    return charlist
    
def sort_on(dict):
    return dict["num"]

