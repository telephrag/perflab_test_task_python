#!/usr/bin/python3


star = '*'


def is_star_at_beginning(word) :
    if word[0] == '*' :
        return True
    else :
        return False


def get_first_symbol_index(word) :
    for i in range( len(word) ) :
        if word[i] != '*' :
            return i
    return None


def delete_left(word, index) :
    return word[index:]


def swap(word1, word2) :
    temp = word1
    word1 = word2
    word2 = temp
    return word1, word2


def consist_of_stars(word) :
    for i in range( len(word) ) :
        if word[i] != star :
            return False
    return True


def reset(word1, word2) :
    s1 = is_star_at_beginning(word1)
    s2 = is_star_at_beginning(word2)

    if s1:
        word1, word2 = swap(word1, word2)

    return word1, word2, get_first_symbol_index(word1)


def compare(word1, word2) :

    word1, word2, f_index = reset(word1, word2)
    i = 0

    while not consist_of_stars(word1) or not consist_of_stars(word2) :

        if word1[f_index] == word2[i] :
            word1 = delete_left(word1, f_index + 1)
            word2 = delete_left(word2, i + 1)
            word1, word2, f_index = reset(word1, word2)
            i = 0
            continue

        elif word2[i] != '*' :

            if is_star_at_beginning(word2) :
                word1 = delete_left(word1, f_index + 1)
                word1, word2, f_index = reset(word1, word2)
                i = 0
                continue

            else :
                print('KO')
                return

        elif consist_of_stars(word2) :
            print('OK')
            return

        i += 1

    return
