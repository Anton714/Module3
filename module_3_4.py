def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        lower_other_words = other_words[i]
        if root_word.lower() in lower_other_words.lower() or lower_other_words.lower() in root_word.lower():
            same_words.append(other_words[i])

    print(same_words)


single_root_words('def', 'decimal', 'DEFender', 'luna', 'nudeff', 'dEflect', 'deForm', 'LoCal')

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
