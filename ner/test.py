import re
import random
from konlpy.tag import Kkma

kkma = Kkma()
# pos = kkma.pos('☆호♡랑♡이♡파☆,')
# print(pos)

# 전화번호 비식별처리 완료
# 계좌 비식별처리 x (예: 132-063-191529 > 은행마다 다름)
# 이메일 비식별처리 x (정규표현식으로 가능할듯)
# 작성자 아이디 비식별처리 x (이메일 삭제 후 처리해야할 듯)

def phonenumber(text): # 이미 비식별처리된 전화번호 복원
    i = 0 # 전화번호 갯수 셀 counter
    count = text.count('***-****-****')
    while i < count :
        mid = random.randrange(0, 10000) # 전화번호 중간자리
        text = text.replace('-****-', '-' + str(mid).zfill(4) + '-', 1)
        end = random.randrange(0, 10000) # 전화번호 끝자리
        text = text.replace('-****', '-' + str(end).zfill(4), 1)
        beg = random.randrange(0, 100) # 전화번호 첫자리
        text = text.replace('***-', '0' + str(beg).zfill(2) + '-', 1)
        i += 1
    return text

def cleanser(text):
    text = re.sub('(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', '', text) # http 주소 삭제
    text = re.sub('([ㄱ-ㅎㅏ-ㅣ]+)', '', text) # 한글 자음, 모음 삭제
    text = re.sub('[ぁ-ゔ]+|[ァ-ヴー]+[々〆〤]', '', text) # 일본어 삭제
    text = re.sub('一-龥', '', text) # 한자 삭제
    text = re.sub('[-=+,#/\?:^*\"※~ㆍ]', '', text) # 특수문자 삭제
    return text

print(cleanser('#카페일드 #복숭아토스트 #もも'))
