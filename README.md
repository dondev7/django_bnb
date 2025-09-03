# 에어비앤비 챌린지

## Users (2025-09-03)

- 오늘의 강의: 에어비앤비 클론코딩: From #12.0 to #12.3
- 제출기간: 익일 오전 6시까지

### Mission:

- Build the following URLs:
- GET /api/v1/users: See all users
- POST /api/v1/users: Create a user account with password
- PUT /api/v1/users/password: Edit logged in user password
- POST /api/v1/users/login: Log a user in
- POST /api/v1/users/logout: Log a user out

## REST Framework (2025-08-28)

- 오늘의 강의: 에어비앤비 클론코딩: From #10.0 to #10.9
- 제출기간: 익일 오전 6시까지

### Mission:

- When the user goes to /api/v1/tweets, show a list of all the Tweets on your database.
- When the user goes to /api/v1/users/<user_id>/tweets show a list of all the Tweets created by a User
- 유저가 /api/v1/tweets 이동하면, 데이터베이스의 모든 Tweets 리스트를 보여줘야 한다.
- 유저가 /api/v1/users/<user_id>/tweets 이동하면, User 가 만든 모든 Tweets 리스트를 보여줘야 한다.

### Requirements:

- DON'T use the ModelSerializer class.
- DON'T use the APIView class.
- Use models.Serializer
- Handle User.DoesNotExists

## Mission

- Create a new Django project and upload it to Github.
- Create and install an app named tweets.
- The tweets app should have the models: Tweet and Like.
- Build the admins for the Tweet and Like models.
- tweets 라는 이름의 앱을 생성하고 설치하세요.
- tweets앱은 Tweet 그리고 Like 라는 models 이 있어야 합니다.
- Tweet 그리고 Like models 을 위한 어드민을 만드세요.

### Tweet Model Fields

- payload: Text(max. lenght 180)
- user: ForeignKey
- created_at: Date
- updated_at: Date

### Like

- user: ForeignKey
- tweet: ForeignKey
- created_at: Date
- updated_at: Date

### Requirements:

- Use abstract classes.
- Customize the **str** method of all classes.

## Urls, Views and Templates (2025-08-27)

- 오늘의 강의: 풀스택 에어비앤비 클론코딩: From #9.0 to #9.6
- 제출기간: 익일 오전 6시까지

### Mission

- Using urls.py, views.py, render() and the Django ORM, write code to show a list of all the Tweets to the user when the user visits the / page.
- urls.py, views.py, render() 그리고 Django ORM 을 활용하여. / 페이지에 유저가 방문하였을때. 모든 Tweets 을 보여주는 리스트 코드를 작성하세요.
