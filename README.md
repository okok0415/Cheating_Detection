1. 
cd Cheating_Detection   
pipenv --three          -> 가상환경 생성
code .                  -> 현재 폴더로 VSCode 실행

VSCode가 켜진 상황.

2. python interpreter을 반드시 설정해주어야 한다.

F1 -> python select interpreter로 들어가서
Python 3.7.3 64-bit ('Cheating_Detection':pipenv) -> 이걸로 설정

혹은 좌측 하단에 Python설정하는 키가 있음
혹은 Python interpreter을 설정하지 않았습니다! 이럼서 경고창이 뜸

3. pipfile에 들어가서 Package에 있는 것들을 Install 한다.

(현재 readme작성 기준)

pipenv shell            -> 가상환경 킴
    (Cheating_Detection) PS C:\Users\... -> 이러면 정상
pipenv install Django==3.0
pipenv install django-rest-framework
pipenv install django-cors-headers
pipenv install pillow
pipenv install flake8

