import requests

download_url = "https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"

output_file = "downloaded_file.txt"

response = requests.get(download_url)

if response.status_code == 200:
    with open(output_file, 'wb') as file:
        file.write(response.content)
    print(f"Файл успішно завантажено та збережено як {output_file}")
else:
    print("Помилка при завантаженні файлу")

import time


# Adjusted Boyer-Moore algorithm for Unicode support
def boyer_moore_search_unicode(pattern, text):
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    # Preprocessing
    skip = {ch: m for ch in set(text)}
    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1

    # Search
    k = m - 1
    while k < n:
        j, i = k, m - 1
        while i >= 0 and text[j] == pattern[i]:
            j -= 1
            i -= 1
        if i == -1:
            return j + 1
        k += skip.get(text[k], m)  # Use m as the default skip value for characters not in the pattern
    return -1


# Knuth-Morris-Pratt algorithm
def kmp_search(pattern, text):
    m, n = len(pattern), len(text)
    lps = [0] * m
    j = 0  # index for pattern[]

    # Preprocess the pattern (calculate lps[] array)
    compute_lps_array(pattern, m, lps)

    i = 0  # index for text[]
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:  # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def compute_lps_array(pattern, m, lps):
    length = 0  # length of the previous longest prefix suffix
    lps[0] = 0  # lps[0] is always 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


# Rabin-Karp algorithm
def rabin_karp_search(pattern, text, d=256, q=101):
    m, n = len(pattern), len(text)
    h = pow(d, m - 1) % q
    p = t = 0

    # Preprocessing
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        if p == t:  # Check character by character
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1


# Direct measurement of execution time
def measure_time_single_run(func, pattern, text):
    start_time = time.time()
    func(pattern, text)
    end_time = time.time()
    return end_time - start_time


# Main execution and timing comparison
if __name__ == "__main__":
    algorithms = [boyer_moore_search_unicode, kmp_search, rabin_karp_search]
    substrings = ["existing_substring", "non_existing_substring"]
    texts = ["article_1_content", "article_2_content"]

    times_direct = {}
    sample_size = 1000
    for alg in algorithms:
        for substring in substrings:
            for i, text in enumerate(texts, 1):
                sample_text = text[:sample_size]
                key = (
                alg.__name__, 'existing' if substring == "existing_substring" else 'non-existing', f'Article {i}')
                times_direct[key] = measure_time_single_run(alg, substring, sample_text)

    print(times_direct)
