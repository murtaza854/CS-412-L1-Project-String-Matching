def NaiveAlgorithm(pattern, text):
    m = len(pattern)
    n = len(text)
    for i in range(n-m+1):
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
            if j == m - 1:
                pass
            # print("Pattern is found at position: " + str(i))