시작하기 앞서...

    python 홈페이지에 들어가서 3.7.3 Download
    cmd에 들어가서 pip install pipenv
    Visual Studio Code Download ** -> python만을 사용하지 않기 때문에 불가피하게 Visual Studio Code가 있어야 한다.

이 세개가 해결이 된 상태로 가정하고 시작합니다. 0. clone Cheating_Detection
본인 Documents 혹은 본인이 원하는 자리에 CMD나 PowerShell을 킨다.

        git clone https://github.com/okok0415/Cheating_Detection.git

1.        cd Cheating_Detection
        pipenv --three          -> 가상환경 생성
        code .                  -> 현재 폴더로 VSCode 실행

        VSCode가 켜진 상황.

2.  python interpreter을 반드시 설정해주어야 한다.

        F1 -> python select interpreter로 들어가서
        Python 3.7.3 64-bit ('Cheating_Detection':pipenv) -> 이걸로 설정

        혹은 좌측 하단에 Python설정하는 키가 있음
        혹은 Python interpreter을 설정하지 않았습니다! 이럼서 경고창이 뜸

3.  pipfile에 들어가서 Package에 있는 것들을 Install 한다.

        (현재 readme작성 기준)

        pipenv shell            -> 가상환경 킴
            (Cheating_Detection) PS C:\Users\... -> 이러면 정상
        pipenv install Django==3.0
        pipenv install django-rest-framework
        pipenv install django-cors-headers
        pipenv install pillow
        pipenv install flake8
        pipenv install black
        pipenv install django-seed

4.  Backend(Django) 서버를 실행합시다.

        python manage.py runserver  -> 현재는 오류가 뜨지만 /admin으로 일단 들어갑시다.

5.  DataBase 오류. migrate가 하나도 되어있지 않기 때문에 동기화 시켜줘야할 필요가 있음

        python manage.py makemigrations
        python manage.py migrate

        ..... OK가 나오면 정상

6.  Login창이 뜨는데 super계정을 만들어서 접근해봅시다

        python manage.py createsuperuser
        Username: lim
        Email address: (can skip)
        Password: 123
        Password (again):

7.  성공!

8.  frontend 서버를 실행해 봅시다.(node.js, npm, npx, git이 모두 있어야 함)

        node -v
        npm -v
        npx -v
        git --version //깔려있는 지 확인하는 용도 까는건 직접 사이트 들어가서 깔아야함

        cd cheating_detection_react

9.  frontend 설치 준비물 참고영상 -> 로그인해야될걸....?

https://nomadcoders.co/react-fundamentals/lectures/1541

10. package.json에 들어가서 설치해야할 것들을 살펴보자.

        npm install react
        npm install react-dom
        npm install react-router-dom
        npm install react-scripts
        npm install web-vitals

11. frontend 서버 실행

        npm start

12. 성공!!

---

자동 DB 생성기 -> faker를 이용한 Seed방식

1.  Users생성기

        python manage.py seed_users --number (원하는 숫자)

2.  Boards 생성기

        python manage.py seed_boards --number (원하는 숫자)
