"""문자열 데이터에 있는 Method"""

from time import time

STRING_DATA = "Test_sample.txt"

# 문자열의 시작이 무엇인지 확인하기
print(STRING_DATA.startswith("test"))  # return True
print(STRING_DATA.startswith("sample"))  # return False

# 문자열의 끝이 무엇인지 확인하기
print(STRING_DATA.endswith("txt"))  # return True
print(STRING_DATA.endswith("test"))  # return False

# 문자열의 Offset 찾기 (index 찾기)
print(STRING_DATA.find("s"))  # find method
print(STRING_DATA.index("s"))  # index method

# """에러 발생 시 차이점"""
print(STRING_DATA.find("z"))  # return -1
# print(string_data.index("z")) # return ValueError (에러 발생으로 인한 주석 처리)

# find랑 index 속도 비교 (그닥 차이가 없음 !)
TEST_SENTENCE = "Abstract: Medical image analysis is performed\
    by analyzing images obtained by medical imaging systems\
    to solve clinical problems. The purpose is to extract effective information and\
    improve the level of clinical diagnosis.\
    In recent years, automatic segmentation based on \
    deep learning (DL) methods has been widely used,\
    where a neural network can automatically learn image features,\
    which is in sharp contrast with the traditional manual learning method.\
    U-net is one of the most important semantic segmentation frameworks\
    for a convolutional neural network (CNN).\
    It is widely used in the medical image analysis domain for \
    lesion segmentation, anatomical segmentation, and classification.\
    The advantage of this network framework is that it can not only accurately segment\
    the desired feature target and effectively process and objectively evaluate medical images\
    but also help to improve accuracy in the diagnosis by medical images.\
    Therefore, this article presents a literature review of medical image segmentation based on U-net,\
    focusing on the successful segmentation experience of U-net for \
    different lesion regions in six medical imaging systems.\
    Along with the latest advances in DL, \
    this article introduces the method of combining the original U-net architecture\
    with deep learning and a method for improving the U-net network.\
    Copyright of Journal of Imaging Science & Technology is the property of International Society\
    for Imaging Science & Technology and its content may not be copied or emailed to multiple sites\
    or posted to a listserv without the copyright holder's express written permission.\
    However, users may print, download, or email articles for individual use.\
    This abstract may be abridged. No warranty is given about the accuracy of the copy.\
    Users should refer to the original published version of the material for the full abstract."

start_time = time()
for _ in range(100_000):
    TEST_SENTENCE.find("U-net")
end_time = time()
print(f"find method: {end_time - start_time}")

start_time = time()
for _ in range(100_000):
    TEST_SENTENCE.index("U-net")
end_time = time()
print(f"index method: {end_time - start_time}")

# 문자열의 대소문자 변경
print(STRING_DATA.upper())  # 모든 문자를 대문자로
print(STRING_DATA.lower())  # 모든 문자를 소문자로
print(STRING_DATA.swapcase())  # 대문자는 소문자로, 소문자는 대문자로
print(STRING_DATA.capitalize())  # 첫 단어만 대문자로
print(STRING_DATA.title())  # 각 단어의 첫 알파벳을 대문자로

# 문자열 정렬 - function(공간,빈 공간 채울 문자열)
print(STRING_DATA.center(20, "*"))  # 20자 내로 중앙 정렬
print(STRING_DATA.ljust(20, "*"))  # 20자 내로 좌측 정렬
print(STRING_DATA.rjust(20, "*"))  # 20자 내로 우측 정렬
