"""string module 사용
* PyLint에서는 string을 import 해서 사용하지 않는다고 합니다."""

import string
from time import time

# ascii_letter : 모든 ASCII 문자
print(string.ascii_letters)

# ascii_lowercase : 모든 소문자 ASCII 문자
print(string.ascii_lowercase)

# ascii_uppercase : 모든 대문자 ASCII 문자
print(string.ascii_uppercase)

# digits : 모든 10진수 문자
print(string.digits)

# hexdigits : 모든 16진수 문자
print(string.hexdigits)

# octdigits : 모든 8진수 문자
print(string.octdigits)

# punctuation : 모든 구두점 문자
print(string.punctuation)

# whitespace : 모든 공백 문자
whitespace = string.whitespace
print(repr(whitespace), "\n")

# capwords : 문자열의 각 단어의 첫 글자를 대문자로 변환
SENTENCE = "hello, world"
print(string.capwords(SENTENCE))

# capitalize와 capwords의 속도 비교 (capitalize > capwords)
start_time = time()
for _ in range(100_000):
    SENTENCE.capitalize()
end_time = time()
print(f"capitalize : {end_time - start_time}")

start_time = time()
for _ in range(100_000):
    string.capwords(SENTENCE)
end_time = time()
print(f"capwords : {end_time - start_time}")
