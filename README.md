# Django

## 1. 시작하기

```bash
$ pip install django
```

- 현재 활용하고 있는 버전은 다음과 같다.

  - python 3.7.4

  - django 2.2.4

### 1. Django 프로젝트 시작

```bash
$ mkdir __프로젝트 이름/폴더 이름__
$ cd __프로젝트 이름/폴더 이름__
```



```bash
$ django-admin startpoject __프로젝트이름__ .
```

- 프로젝트 이름으로 구성된 폴더와, `manage.py`가 생성된다.
  - `__inti__.py` : 해당 폴더가 패키지로 인식될 수 있게끔 작성
  - `setting.py` :  django 설정과 관련된 파일
  - `url.py` : url 관리
  - `wsgi.py` : 배포시 사용(web server gateway interface : 파이썬에서 사용되는 웹 서버)
  - `manage.py` : django 프로젝트와 관련된 커맨드 라인(명령어) 유틸리티



### 2. 서버 실행

```bash
$ pyhton manage.py runserver
```

- `localhost:8000` 으로 들어가서 로켓 확인!



### 3. App 생성

```bash
$ python manage.py startapp __app이름__
```

- `app이름` 인 폴더가 생성되며, 구성하고 있는 파일은 다음과 같다.

  - `admin.py` : 관리자 페이지 설정

  - `app.py` : app의 정보 설정, 직접 수정하는 경우 별로 없음.

  - `models.py` : **MTV-model을 정의하는 곳**

  - `tests.py` : 테스트 코드를 작성하는 곳.

  - `views.py` : **MTV-VIew를 정의 하는 곳**

    - 사용자에게 요청이 왔을 때, 처리되는 함수

      ```python
      def index(request):
          return render(request, index.html
      ```

**app을 만들고 나서 반드시 `settings.py` 에서 `INSTALLED_APPS` 에 app을 등록한다.**

```python
# first_django/settings.py
#..
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin',
    # ...
]
#..
```

## 2. 작성 흐름

### 1. url 정의

```python
# first_django/urls.py
from pages import views
urlpatterns = [
    path('', views.index),
]
```

- `urls.py`는 우리의 웹 어플리케이션 경로들을 모두 관리한다.
- 요청이 들어오면 `urls.py`의 `urlpatterns`에 정의된 경로로 매핑한다.
- path(`경로`, `views 에 정의된 함수`)



### 2. View 정의

```python
# pages/views.py

def index(request):
    return render(request, 'index.html')
```

- views.py 는 MTV에서 View에 해당한다.
- 일종의 중간관리자로 Model, Template 등의 처리를 담당한다.



### 3. Template 정의

- 기본적으로 app을 생성하면, `templates` 폴더가 없으므로 직접 생성해야 한다.

```html
<!-- pages/gemplates/index.html-->
<h1>
    장고 안녕!
</h1>
```

### 4. 서버 실행 및 확인

```bash
$ python manage.py runserver
```

`localhost:8000` 에서 확인해보자

\







1. 폴더만들고

   mkdir __

2. 가상환경 만들고

   2-1.  .gitignore에 venv/ 추가

   python -m venv venv

3. 가상환경 실행후

   source venv/Scripts/activate

4. 원하는 django 버전 설치

   pip install django

5. 프로젝트 생성

   django-admin startproject ___

6. app 생성 및 등록
7. url 설정

8. views.py 설정
9. templates 설정
10. 서버실행