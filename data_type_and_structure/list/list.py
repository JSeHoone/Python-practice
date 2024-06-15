"""list"""

import copy

# 리스트 정의하기
LIST1 = []
LIST2 = list()

# 리스트에 data 값 하나 넣기
LIST1.append(1)
LIST2.insert(0, 1)
print("LIST1 :", LIST1)
print("LIST2 :", LIST2)
print("=" * 10)

# 리스트에 data 값 여러개 넣기
LIST1.extend([2, 3, 4])
print("LIST1 :", LIST1)
print("=" * 10)

# 리스트에 여러 형태의 데이터 타입, 구조넣기 - Nested Data Structure
LIST2.append(("Tuple1", "Tuple2"))  # Tuple
LIST2.append("String")  # Stirng
LIST2.append(100)  # Integer
LIST2.append(3.141592)  # Float
LIST2.append({"Key": "value"})  # Dictionary
LIST2.append([2, 3, 4, 5, 6, 7])
print("LIST2 :", LIST2)
print("=" * 10)

# 리스트에서 값 변경하기
LIST1[1] = "Change Value"
print("LIST1 :", LIST1)
print("=" * 10)

# 리스트에 원하는 Index(Offset)위치에 값 추가하기
LIST1.insert(1, "Insert Value")
print("LIST1 :", LIST1)
print("=" * 10)

# 리스트에서 원하는 Index(Offset)위치에 값 삭제하기
LIST1.pop(1)
print("LIST1 :", LIST1)
print("=" * 10)


# 리스트로 구현하는 Stack & Queue
def stack():
    values = [1, 2, 3, 4, 5]
    for _ in range(len(values)):
        print(values.pop(-1))


def queue():
    values = [1, 2, 3, 4, 5]
    for _ in range(len(values)):
        print(values.pop(0))


print("Stack start")
stack()
print("-" * 10)
print("Queue Start")
queue()
print("=" * 10)

# 리스트 복사하기 (얕은 복사)
# 리스트 안에 있는 자료구조들 까지는 복사가 되지 않음
LIST3 = LIST1.copy()
LIST4 = LIST2[:]
print("LIST3 :", LIST3)
print("LIST4 :", LIST4)
print("-" * 10)

LIST4[-1][0] = "Shallow Copy"
print("LIST2 :", LIST2)
print("LIST4 :", LIST4)
print("=" * 10)

# 리스트 복사하기 (깊은 복사)
LIST5 = copy.deepcopy(LIST2)

LIST5[-1][0] = "Deep Copy"

print("LIST2 :", LIST2)
print("LIST5 :", LIST5)

# 리스트의 비교 연산
# 리스트의 비교 연산은 두 리스트의 같은 위치의 Index(Offset) 항목을 비교한다.
A = [1, 2, 3]
B = [1, 2, 3]
C = [1, 2, 4]

print(A > B)  # False
print(A > C)  # False
print(C > A)  # True
print("=" * 10)
