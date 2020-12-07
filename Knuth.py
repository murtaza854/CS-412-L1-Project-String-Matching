def get_LPS_array(pattern):
    '''
    Computes the LPS Array using the method 
    explained in the report
    '''
    length = 0
    i = 1
    lps = [0] * len(pattern)
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            lps[i] = length+1
            length += 1
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps


def KMP_search(pattern, text):
    '''
    Applies KMP Algorithm to find all instances
    of the string.
    '''
    lps = get_LPS_array(pattern)
    i, j = 0, 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == len(pattern):
            print(i-j)
            j = lps[j-1]
