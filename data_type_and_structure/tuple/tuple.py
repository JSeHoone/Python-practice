"""Tuple"""

# Assign Tuple
VALUES = (1, 2, 3)
print(VALUES, type(VALUES))
print("=" * 10)

# Unpacking Tuple
A, B, C = (1, 2, 3)
print(A)
print(B)
print(C)
print("=" * 10)


# Tuple의 연산 (더하기와 곱하기만 가능 !)
def add_tuple():
    """
    처음에 할당한 'value1'이랑 더한 뒤 'value1'은 다름
    새로운 튜플을 만들고 'value1'이 해당 메모리를 바라보도록 한 것임
    """
    value1 = (1, 2, 3)
    print("value1 Id:", id(value1))
    value2 = (4, 5)

    value1 = value1 + value2
    print("new value1 Id:", id(value1))


add_tuple()
print("-" * 10)


def multiply_tuple():
    """
    처음에 할당한 'value1'이랑 더한 뒤 'value1'은 다름
    새로운 튜플을 만들고 'value1'이 해당 메모리를 바라보도록 한 것임
    """
    value1 = (1, 2, 3)
    print("value1 Id:", id(value1))

    value1 = value1 * 3
    print("new value1 Id:", id(value1))


multiply_tuple()
