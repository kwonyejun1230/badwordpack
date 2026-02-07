# 비속어와 욕설들을 검열하는 파이썬 팩입니다
## pip install badwordpack을 할경우 다른 패키지가 나오거나 패키지가 존재하지 않습니다.
## 이 팩은 이 깃허브에서만 설치 할수 있습니다.

# 사용방법
## 2 - 1 (import)
팩이 코드와 같은 디렉토리에 있는 경우:
``import badwordmain``
그 외의 경우:
``import (상대경로).badwordmain``
입니다

## 2 - 2 (funcion)
함수종류는
``badwordmain.is_badword()``
와
``badwordmain.add_badword()``
가 있습니다

## 2 - 3 (예시 코드)
import badwordmain

w = input("단어 입력")
print(badwordmain.is_badword(w))
