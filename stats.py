def sort_on(items):
    return items["num"]

def get_num_words(word_string):
    list_of_words = word_string.split()
    num_words = len(list_of_words)
    return num_words

def character_count(word_string):
    char_counts = {}
    for c in word_string:
        c = c.lower()
        #print(c.lower())
        if c in char_counts:
            char_counts[c] += 1 
        else:
            char_counts[c] = 1

    return char_counts

def sorted_character_count(char_counts):
    sorted_list = []
    for k, v in char_counts.items():
        sorted_list.append({"char": k, "num": v})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
#    print(sorted_list)

