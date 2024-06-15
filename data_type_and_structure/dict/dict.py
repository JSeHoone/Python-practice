"""Dictionary
다른 언어에서는 assosicative array, hash, hash map이라고 불린다."""

# 딕셔너리로 변환하기
# 2개의 값으로 이루어진 Sequence를 dict로 변환할 수 있다.
A = [(1, 2), (2, 3), ("key", "value")]
DICT_A = dict(A)
print(DICT_A)
print("=" * 10)

# value 값 얻기
print(DICT_A["key"])
print(DICT_A.get("key"))
print(DICT_A.get("key2", "If dosen't exist key, show this message"))
print("=" * 10)

# 모든 Key 값 얻기
# 해당 메서드는 아주 큰 dict에 유용하다
# 사용되지 않을 리스트를 생성하지 않기에, 메모리와 시간을 절약해준다.
print(DICT_A.keys())
print("=" * 10)

# 결합하기(1) - update 메서드
B = {"new_key": "new_value", "another_key": "another_value"}
print(id(DICT_A))
DICT_A.update(B)
print(id(DICT_A))
print(DICT_A)
print("=" * 10)

# 결합하기(2) - **(Unpacking)를 이용한 방법
# 해당 방법은 얕은 복사이므로 주의하자 !
C = {"test_key": [1, 2, 3, 4]}
NEW_DICT = {**DICT_A, **C}
NEW_DICT["test_key"][0] = "Shallow Value"
print("C :", C["test_key"])
print("NEW_DICT :", NEW_DICT["test_key"])
print("=" * 10)

# 삭제하기
# .pop() 메서드는 get과 del이 동시에 일어난다.
del NEW_DICT["test_key"]
print(NEW_DICT.pop("new_key"))  # new_value
print(NEW_DICT.pop("test_key", "If dosen't exist key, show this message"))  # message

# 비교하기 ( == , != 만 가능)
A = {"1": 1, "2": 2, "3": 3}
B = {"1": 1, "2": 2, "3": 3}
C = {"1": 1, "2": 2, "4": 4}

print(A == B)  # Ture
print(B != C)  # True
print(C == B)  # False
