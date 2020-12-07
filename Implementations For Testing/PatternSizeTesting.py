import random
import numpy as np
import matplotlib.pyplot as plt
import timeit
pattern_lengths = [50]
alphabet_size = [26]



from string import ascii_lowercase



def plotter(r_k_time, b_f_time, kmp_time, time, filename):
    '''
    plots using information based on time
    '''
    plt.title(f'Complexity Analysis when n = 50,000')
    plt.plot(time, b_f_time, label="Brute Force")
    plt.plot(time, r_k_time,
                   'tab:orange', label="Rabin Karp")
    plt.plot(time, kmp_time
                   , 'tab:green', label="KMP")
    plt.xlabel("m")
    plt.ylabel('time in seconds')
    plt.legend()

    plt.plot()
    plt.savefig(f"{filename}.png")
    print("plotted")


def get_random_string(length, letters):
    '''
    Generates random string of length length using letters
    '''
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def insert(source_str, insert_str, pos):
    '''
    Fits a string into another string and results in a new string
    '''
    return source_str[:pos]+insert_str+source_str[pos:]

start_test,end_test,step_test = 100,10001,50
times = list(range(start_test,end_test,step_test))

b_f_temp = list(range(start_test,end_test,step_test))
r_k_temp = list(range(start_test,end_test,step_test))
kmp_temp = list(range(start_test,end_test,step_test))

for i,n in enumerate(range(start_test,end_test,step_test)):
    pattern = get_random_string(n,ascii_lowercase)
    string_to_search = get_random_string(50000-n, ascii_lowercase)
    string_to_search = insert(
        string_to_search, pattern, random.randint(0, len(string_to_search)-1))
    a = timeit.timeit(stmt="NaiveAlgorithm(pattern,text)",
                        setup=f"from BruteForce import NaiveAlgorithm;text='{string_to_search}';pattern='{pattern}';", number=3)
    
    b = timeit.timeit(stmt=f"RabinKarp(pattern,text,524287)",
                        setup=f"from RabinKarp import RabinKarp;text='{string_to_search}';pattern='{pattern}';", number=3)
    
    c = timeit.timeit(stmt="KMP_search(pattern,text)",
                        setup=f"from Knuth import KMP_search;text='{string_to_search}';pattern='{pattern}';", number=3)
    b_f_temp[i] = a/3
    r_k_temp[i] = b/3
    kmp_temp[i] = c/3
    import time
    if n % 100 == 0:
        print(n)
print("done")
plotter(r_k_temp, b_f_temp, kmp_temp, times, "m_analysis")