# 에어비앤비 챌린지

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
