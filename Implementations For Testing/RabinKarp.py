def hash_(word, m, quotient):
    result = 0
    for i in range(m):
        result = (result + ord(word[i])*2**(m-(1+i))) % quotient 
    return result

def rehash(a, b, hash_value, m, quotient):
    '''
    a : character leaving window.
    b: character entering the window 
    hash_value : Previous Hash value
    m : length of window
    quotient: odd number to take mod by.
    Finds the new hash using old hash
    '''
    return (2*hash_value- ord(a)*2**(m) + ord(b))%quotient

def RabinKarp(word, text, quotient):
    '''
    Applies Rabin-Karp Algorithm to find all instances
    of the string.
    '''
    m = len(word)
    # print("m = ", m)
    n = len(text)
    # print("n = ", n)
    hash_word = hash_(word, m, quotient)
    hash_text = hash_(text, m, quotient)
    for j in range(n-m+1):
        # print("text =", text[j:j+m], ", hash_text =", hash_text, ", hash_word =", hash_word)
        if(hash_word == hash_text and text[j:j+m] == word):
            pass
            # print("Pattern is found at position: " + str(j))
        if (j+m < n):
            hash_text = rehash(text[j], text[j+m], hash_text, m, quotient)
