def remove_duplicate_words(s):
    no_space_str = s.replace(' ', ',').split(',')
    word_container = {}
    for wrd in no_space_str:
        if wrd not in word_container:
            word_container[wrd] = 1
        else:
            word_container[wrd] == 1
    single_word_list = list(word_container.keys())
    return ' '.join(single_word_list)






print(remove_duplicate_words("my cat is my cat fat"))
print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
print(remove_duplicate_words("alpha beta beta gamma gamma gamma"))
