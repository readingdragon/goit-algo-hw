import timeit

# ---------------------------Алгоритм Кнута-Морріса-Пратта------------------------------
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
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

    return lps

def kmp_search(some_text, pattern):
    M = len(pattern)
    N = len(some_text)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == some_text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            print(f"K-M-P alg: Substring found - [{i - j}]")
            return i - j
    print("Substring not found")
    return -1  # якщо підрядок не знайдено

# ---------------------------Алгоритм Боєра-Мура------------------------------
def build_shift_table(pattern):
  table = {}
  length = len(pattern)
  
  for index, char in enumerate(pattern[:-1]):
    table[char] = length - index - 1
  
  table.setdefault(pattern[-1], length)
  return table

def boyer_moore_search(some_text, pattern):

  shift_table = build_shift_table(pattern)
  i = 0
  
  while i <= len(some_text) - len(pattern):
    j = len(pattern) - 1
    while j >= 0 and some_text[i + j] == pattern[j]:
      j -= 1
    if j < 0:
      print(f"B-M alg: Substring found - [{i}]")
      return i
    i += shift_table.get(some_text[i + len(pattern) - 1], len(pattern))
  print("Substring not found")
  return -1

# ---------------------------Алгоритм Рабіна-Карпа------------------------------
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(some_text, substring):
    substring_length = len(substring)
    main_string_length = len(some_text)
    
    base = 256 
    modulus = 101  
    
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(some_text[:substring_length], base, modulus)
    
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if some_text[i:i+substring_length] == substring:
                print(f"R-K alg: Substring found - [{i}]")
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(some_text[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(some_text[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    print("Substring not found")
    return -1

def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

path2file1 = 'стаття_1.txt'
path2file2 = 'стаття_2.txt'

test_text1 = read_file(path2file1)
test_text2 = read_file(path2file2)

substring = "хеш-таблиці"
substring_fake = "навіки вся москва гори й не гасни"

def measure_search_time(text, substring, search_func): 
    start_time = timeit.default_timer()
    search_func(text, substring)

    measured_time = timeit.default_timer() - start_time

    # print(f'Spent time: {round(measured_time, 6)}')
    return round(measured_time, 6)


print("Тест алгоритмів на першому тексті:")
print('+'*70)
print(f"Алгоритм Боєра-Мура: {measure_search_time(test_text1, substring, boyer_moore_search)} секунд")
print(f"Алгоритм Боєра-Мура з бажаним підрядком: {measure_search_time(test_text1, substring_fake, boyer_moore_search)} секунд")
print('-'*70)
print(f"Алгоритм Кнута-Морріса-Пратта: {measure_search_time(test_text1, substring, kmp_search)} секунд")
print(f"Алгоритм Кнута-Морріса-Пратта з бажаним підрядком: {measure_search_time(test_text1, substring_fake, kmp_search)} секунд")
print('-'*70)
print(f"Алгоритм Рабіна-Карпа: {measure_search_time(test_text1, substring, rabin_karp_search)} секунд")
print(f"Алгоритм Рабіна-Карпа з бажаним підрядком: {measure_search_time(test_text1, substring_fake, rabin_karp_search)} секунд")
print('-'*70)

print("Тест алгоритмів на другому тексті:")
print('+'*70)
print(f"Алгоритм Боєра-Мура: {measure_search_time(test_text2, substring, boyer_moore_search)} секунд")
print(f"Алгоритм Боєра-Мура з бажаним підрядком: {measure_search_time(test_text2, substring_fake, boyer_moore_search)} секунд")
print('-'*70)
print(f"Алгоритм Кнута-Морріса-Пратта: {measure_search_time(test_text2, substring, kmp_search)} секунд")
print(f"Алгоритм Кнута-Морріса-Пратта з бажаним підрядком: {measure_search_time(test_text2, substring_fake, kmp_search)} секунд")
print('-'*70)
print(f"Алгоритм Рабіна-Карпа: {measure_search_time(test_text2, substring, rabin_karp_search)} секунд")
print(f"Алгоритм Рабіна-Карпа з бажаним підрядком: {measure_search_time(test_text2, substring_fake, rabin_karp_search)} секунд")
print('-'*70)