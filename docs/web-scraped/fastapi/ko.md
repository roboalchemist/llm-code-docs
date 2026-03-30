# Source: https://fastapi.tiangolo.com/ko/

Title: FastAPI

URL Source: https://fastapi.tiangolo.com/ko/

Markdown Content:
🌐 AI와 사람이 함께한 번역
이 번역은 사람의 안내를 받아 AI가 만들었습니다. 🤝

원문의 의미를 오해하거나 부자연스러워 보이는 등 오류가 있을 수 있습니다. 🤖

[AI LLM을 더 잘 안내하는 데 도움을 주세요](https://fastapi.tiangolo.com/ko/contributing/#translations).

[영문 버전](https://fastapi.tiangolo.com/)

[![Image 1: FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/ko)

_FastAPI 프레임워크, 고성능, 간편한 학습, 빠른 코드 작성, 준비된 프로덕션_

[![Image 2: Test](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)[![Image 3: Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi)[![Image 4: Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)[![Image 5: Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)](https://pypi.org/project/fastapi)

* * *

**문서**: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/ko)

**소스 코드**: [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

* * *

FastAPI는 현대적이고, 빠르며(고성능), 파이썬 표준 타입 힌트에 기초한 Python의 API를 빌드하기 위한 웹 프레임워크입니다.

주요 특징으로:

*   **빠름**: (Starlette과 Pydantic 덕분에) **NodeJS** 및 **Go**와 대등할 정도로 매우 높은 성능. [사용 가능한 가장 빠른 파이썬 프레임워크 중 하나](https://fastapi.tiangolo.com/ko/#performance).
*   **빠른 코드 작성**: 약 200%에서 300%까지 기능 개발 속도 증가. *
*   **적은 버그**: 사람(개발자)에 의한 에러 약 40% 감소. *
*   **직관적**: 훌륭한 편집기 지원. 자동완성 이 모든 곳에서 동작. 적은 디버깅 시간.
*   **쉬움**: 쉽게 사용하고 배우도록 설계. 적은 문서 읽기 시간.
*   **짧음**: 코드 중복 최소화. 각 매개변수 선언의 여러 기능. 적은 버그.
*   **견고함**: 준비된 프로덕션 용 코드를 얻으십시오. 자동 대화형 문서와 함께.
*   **표준 기반**: API에 대한 (완전히 호환되는) 개방형 표준 기반: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (이전에 Swagger로 알려졌던) 및 [JSON Schema](https://json-schema.org/).

* 내부 개발팀의 프로덕션 애플리케이션을 빌드한 테스트에 근거한 측정

[![Image 6](https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png)](https://fastapicloud.com/ "FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud.")

### 골드 및 실버 스폰서[¶](https://fastapi.tiangolo.com/ko/#gold-and-silver-sponsors)

[![Image 7](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")[![Image 8](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")[![Image 9](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product")[![Image 10](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-gh "Zuplo: Deploy, Secure, Document, and Monetize your FastAPI")[![Image 11](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")[![Image 12](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")[![Image 13](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")[![Image 14](https://fastapi.tiangolo.com/img/sponsors/subtotal.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "The Gold Standard in Retail Account Linking")[![Image 15](https://fastapi.tiangolo.com/img/sponsors/railway.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")[![Image 16](https://fastapi.tiangolo.com/img/sponsors/serpapi.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")[![Image 17](https://fastapi.tiangolo.com/img/sponsors/greptile.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")[![Image 18](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display "Pay as you go for market data")[![Image 19](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship "SDKs for your API | Speakeasy")[![Image 20](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service")[![Image 21](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs")[![Image 22](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI")[![Image 23](https://fastapi.tiangolo.com/img/sponsors/interviewpal.png)](https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring "InterviewPal - AI Interview Coach for Engineers and Devs")[![Image 24](https://fastapi.tiangolo.com/img/sponsors/dribia.png)](https://dribia.com/en/ "Dribia - Data Science within your reach")

[다른 스폰서](https://fastapi.tiangolo.com/ko/fastapi-people/#sponsors)

의견들[¶](https://fastapi.tiangolo.com/ko/#opinions)
-------------------------------------------------

"_[...] 저는 요즘 **FastAPI**를 많이 사용하고 있습니다. [...] 사실 우리 팀의 **마이크로소프트 ML 서비스** 전부를 바꿀 계획입니다. 그중 일부는 핵심 **Windows**와 몇몇의 **Office** 제품들이 통합되고 있습니다._"

Kabir Khan - **마이크로소프트**[(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

"_**FastAPI** 라이브러리를 채택하여 **예측**을 얻기 위해 쿼리를 실행 할 수 있는 **REST** 서버를 생성했습니다. [Ludwig을 위해]_"

Piero Molino, Yaroslav Dudin 그리고 Sai Sumanth Miryala - **우버**[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

"_**Netflix**는 우리의 오픈 소스 배포판인 **위기 관리** 오케스트레이션 프레임워크를 발표할 수 있어 기쁩니다: 바로 **Dispatch**입니다! [**FastAPI**로 빌드]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **넷플릭스**[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

"_**FastAPI**가 너무 좋아서 구름 위를 걷는듯 합니다. 정말 즐겁습니다!_"

* * *

"_솔직히, 당신이 만든 것은 매우 견고하고 세련되어 보입니다. 여러 면에서 **Hug**가 이렇게 되었으면 합니다 - 그걸 만든 누군가를 보는 것은 많은 영감을 줍니다._"

* * *

"_REST API를 만들기 위해 **현대적인 프레임워크**를 찾고 있다면 **FastAPI**를 확인해 보십시오. [...] 빠르고, 쓰기 쉽고, 배우기도 쉽습니다 [...]_"

"_우리 **API**를 **FastAPI**로 바꿨습니다 [...] 아마 여러분도 좋아하실 것입니다 [...]_"

* * *

"_프로덕션 Python API를 만들고자 한다면, 저는 **FastAPI**를 강력히 추천합니다. **아름답게 설계**되었고, **사용이 간단**하며, **확장성이 매우 뛰어나**고, 우리의 API 우선 개발 전략에서 **핵심 구성 요소**가 되었으며 Virtual TAC Engineer 같은 많은 자동화와 서비스를 이끌고 있습니다._"

Deon Pillsbury - **Cisco**[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

FastAPI 미니 다큐멘터리[¶](https://fastapi.tiangolo.com/ko/#fastapi-mini-documentary)
------------------------------------------------------------------------------

2025년 말에 공개된 [FastAPI 미니 다큐멘터리](https://www.youtube.com/watch?v=mpR8ngthqiE)가 있습니다. 온라인에서 시청할 수 있습니다:

[![Image 25: FastAPI Mini Documentary](https://fastapi.tiangolo.com/img/fastapi-documentary.jpg)](https://www.youtube.com/watch?v=mpR8ngthqiE)

**Typer**, CLI를 위한 FastAPI[¶](https://fastapi.tiangolo.com/ko/#typer-the-fastapi-of-clis)
-----------------------------------------------------------------------------------------

[![Image 26](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com/)

웹 API 대신 터미널에서 사용할 CLI 앱을 만들고 있다면, [**Typer**](https://typer.tiangolo.com/)를 확인해 보십시오.

**Typer**는 FastAPI의 동생입니다. 그리고 **CLI를 위한 FastAPI**가 되기 위해 생겼습니다. ⌨️ 🚀

요구사항[¶](https://fastapi.tiangolo.com/ko/#requirements)
------------------------------------------------------

FastAPI는 거인들의 어깨 위에 서 있습니다:

*   웹 부분을 위한 [Starlette](https://www.starlette.dev/).
*   데이터 부분을 위한 [Pydantic](https://docs.pydantic.dev/).

설치[¶](https://fastapi.tiangolo.com/ko/#installation)
----------------------------------------------------

[가상 환경](https://fastapi.tiangolo.com/ko/virtual-environments/)을 생성하고 활성화한 다음 FastAPI를 설치하세요:

**Note**: 모든 터미널에서 동작하도록 `"fastapi[standard]"`를 따옴표로 감싸 넣었는지 확인하세요.

예제[¶](https://fastapi.tiangolo.com/ko/#example)
-----------------------------------------------

### 만들기[¶](https://fastapi.tiangolo.com/ko/#create-it)

다음 내용으로 `main.py` 파일을 만드십시오:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

또는 `async def` 사용하기...
여러분의 코드가 `async` / `await`을 사용한다면, `async def`를 사용하십시오:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

**Note**:

잘 모르겠다면, [문서에서 `async`와 `await`](https://fastapi.tiangolo.com/ko/async/#in-a-hurry)에 관한 _"급하세요?"_ 섹션을 확인해 보십시오.

### 실행하기[¶](https://fastapi.tiangolo.com/ko/#run-it)

다음 명령으로 서버를 실행하십시오:

`fastapi dev main.py` 명령에 관하여...
`fastapi dev` 명령은 `main.py` 파일을 읽고, 그 안의 **FastAPI** 앱을 감지한 다음, [Uvicorn](https://www.uvicorn.dev/)을 사용해 서버를 시작합니다.

기본적으로 `fastapi dev`는 로컬 개발을 위해 auto-reload가 활성화된 상태로 시작됩니다.

자세한 내용은 [FastAPI CLI 문서](https://fastapi.tiangolo.com/ko/fastapi-cli/)에서 확인할 수 있습니다.

### 확인하기[¶](https://fastapi.tiangolo.com/ko/#check-it)

브라우저로 [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery)를 열어보십시오.

아래의 JSON 응답을 볼 수 있습니다:

```
{"item_id": 5, "q": "somequery"}
```

여러분은 벌써 API를 만들었습니다:

*   _경로_`/` 및 `/items/{item_id}`에서 HTTP 요청 받기.
*   두 _경로_ 모두 `GET`_연산_(HTTP _메소드_ 로 알려진)을 받습니다.
*   _경로_`/items/{item_id}`는 `int`형 이어야 하는 _경로 매개변수_`item_id`를 가지고 있습니다.
*   _경로_`/items/{item_id}`는 선택적인 `str`형 _쿼리 매개변수_`q`를 가지고 있습니다.

### 대화형 API 문서[¶](https://fastapi.tiangolo.com/ko/#interactive-api-docs)

이제 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)로 가보십시오.

자동 대화형 API 문서를 볼 수 있습니다 ([Swagger UI](https://github.com/swagger-api/swagger-ui) 제공):

![Image 27: Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### 대안 API 문서[¶](https://fastapi.tiangolo.com/ko/#alternative-api-docs)

그리고 이제 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)로 가봅시다.

다른 자동 문서를 볼 수 있습니다([ReDoc](https://github.com/Rebilly/ReDoc) 제공):

![Image 28: ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

예제 업그레이드[¶](https://fastapi.tiangolo.com/ko/#example-upgrade)
-------------------------------------------------------------

이제 `PUT` 요청에서 본문을 받기 위해 `main.py` 파일을 수정해봅시다.

Pydantic 덕분에 표준 Python 타입을 사용해 본문을 선언합니다.

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

`fastapi dev` 서버는 자동으로 리로딩되어야 합니다.

### 대화형 API 문서 업그레이드[¶](https://fastapi.tiangolo.com/ko/#interactive-api-docs-upgrade)

이제 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)로 이동합니다.

*   대화형 API 문서는 새 본문을 포함해 자동으로 업데이트됩니다:

![Image 29: Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

*   "Try it out" 버튼을 클릭하면, 매개변수를 채우고 API와 직접 상호작용할 수 있습니다:

![Image 30: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

*   그런 다음 "Execute" 버튼을 클릭하면, 사용자 인터페이스가 API와 통신하고 매개변수를 전송한 뒤 결과를 받아 화면에 표시합니다:

![Image 31: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### 대안 API 문서 업그레이드[¶](https://fastapi.tiangolo.com/ko/#alternative-api-docs-upgrade)

그리고 이제, [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)로 이동합니다.

*   대안 문서 역시 새 쿼리 매개변수와 본문을 반영합니다:

![Image 32: ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### 요약[¶](https://fastapi.tiangolo.com/ko/#recap)

요약하면, 여러분은 매개변수의 타입, 본문 등을 함수 매개변수로서 **한번에** 선언했습니다.

여러분은 현대 표준 파이썬 타입으로 이를 행했습니다.

새로운 문법, 특정 라이브러리의 메소드나 클래스 등을 배울 필요가 없습니다.

그저 표준 **Python** 입니다.

예를 들어, `int`에 대해선:

```
item_id: int
```

또는 좀 더 복잡한 `Item` 모델에 대해선:

```
item: Item
```

...그리고 단 하나의 선언으로 여러분이 얻는 것은:

*   다음을 포함한 편집기 지원:
    *   자동완성.
    *   타입 검사.

*   데이터 검증:
    *   데이터가 유효하지 않을 때 자동으로 생성하는 명확한 에러.
    *   깊이 중첩된 JSON 객체에 대한 유효성 검사.

*   입력 데이터 변환: 네트워크에서 파이썬 데이터 및 타입으로 전송. 읽을 수 있는 것들:
    *   JSON.
    *   경로 매개변수.
    *   쿼리 매개변수.
    *   쿠키.
    *   헤더.
    *   폼(Forms).
    *   파일.

*   출력 데이터 변환: 파이썬 데이터 및 타입을 네트워크 데이터로 전환(JSON 형식으로):
    *   파이썬 타입 변환 (`str`, `int`, `float`, `bool`, `list`, 등).
    *   `datetime` 객체.
    *   `UUID` 객체.
    *   데이터베이스 모델.
    *   ...더 많은 것들.

*   대안가능한 사용자 인터페이스를 2개 포함한 자동 대화형 API 문서:
    *   Swagger UI.
    *   ReDoc.

* * *

이전 코드 예제로 돌아가서, **FastAPI**는 다음처럼 처리합니다:

*   `GET` 및 `PUT` 요청에 `item_id`가 경로에 있는지 검증.
*   `GET` 및 `PUT` 요청에 `item_id`가 `int` 타입인지 검증.
    *   그렇지 않다면 클라이언트는 유용하고 명확한 에러를 볼 수 있습니다.

*   `GET` 요청에 `q`라는 선택적인 쿼리 매개변수가 있는지 검사(`http://127.0.0.1:8000/items/foo?q=somequery`처럼).
    *   `q` 매개변수는 `= None`으로 선언되었기 때문에 선택사항입니다.
    *   `None`이 없다면 필수사항입니다(`PUT`의 경우와 마찬가지로).

*   `/items/{item_id}`으로의 `PUT` 요청은 본문을 JSON으로 읽음:
    *   `name`을 필수 속성으로 갖고 `str` 형인지 검사.
    *   `price`를 필수 속성으로 갖고 `float` 형이어야 하는지 검사.
    *   만약 주어진다면, `is_offer`를 선택 속성으로 갖고 `bool` 형이어야 하는지 검사.
    *   이 모든 것은 깊이 중첩된 JSON 객체에도 적용됩니다.

*   JSON을 변환하거나 JSON으로 변환하는 것을 자동화.
*   다음에서 사용할 수 있는 모든 것을 OpenAPI로 문서화:
    *   대화형 문서 시스템.
    *   여러 언어들에 대한 자동 클라이언트 코드 생성 시스템.

*   2개의 대화형 문서 웹 인터페이스를 직접 제공.

* * *

우리는 그저 수박 겉 핥기만 했을 뿐인데 여러분은 벌써 어떻게 작동하는지 알고 있습니다.

다음 줄을 바꿔보십시오:

```
return {"item_name": item.name, "item_id": item_id}
```

...에서:

```
... "item_name": item.name ...
```

...으로:

```
... "item_price": item.price ...
```

...그러고 나서 여러분의 편집기가 속성과 타입을 알고 자동 완성하는지 보십시오:

![Image 33: editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

더 많은 기능을 포함한 보다 완전한 예제의 경우, [튜토리얼 - 사용자 가이드](https://fastapi.tiangolo.com/ko/tutorial/)를 보십시오.

**스포일러 주의**: 튜토리얼 - 사용자 가이드는:

*   서로 다른 장소에서 **매개변수** 선언: **헤더**, **쿠키**, **폼 필드** 그리고 **파일**.
*   `maximum_length` 또는 `regex`처럼 **유효성 제약**하는 방법.
*   강력하고 사용하기 쉬운 **의존성 주입** 시스템.
*   **OAuth2** 지원을 포함한 **JWT tokens** 및 **HTTP Basic**을 갖는 보안과 인증.
*   (Pydantic 덕분에) **깊은 중첩 JSON 모델**을 선언하는데 더 진보한 (하지만 마찬가지로 쉬운) 기술.
*   [Strawberry](https://strawberry.rocks/) 및 기타 라이브러리와의 **GraphQL** 통합.
*   (Starlette 덕분에) 많은 추가 기능:
    *   **웹 소켓**
    *   HTTPX 및 `pytest`에 기반한 극히 쉬운 테스트
    *   **CORS**
    *   **쿠키 세션**
    *   ...기타 등등.

### 앱 배포하기(선택 사항)[¶](https://fastapi.tiangolo.com/ko/#deploy-your-app-optional)

선택적으로 FastAPI 앱을 [FastAPI Cloud](https://fastapicloud.com/)에 배포할 수 있습니다. 아직이라면 대기자 명단에 등록해 보세요. 🚀

이미 **FastAPI Cloud** 계정이 있다면(대기자 명단에서 초대해 드렸습니다 😉), 한 번의 명령으로 애플리케이션을 배포할 수 있습니다.

배포하기 전에, 로그인되어 있는지 확인하세요:

그런 다음 앱을 배포하세요:

이게 전부입니다! 이제 해당 URL에서 앱에 접근할 수 있습니다. ✨

#### FastAPI Cloud 소개[¶](https://fastapi.tiangolo.com/ko/#about-fastapi-cloud)

**[FastAPI Cloud](https://fastapicloud.com/)**는 **FastAPI** 뒤에 있는 동일한 작성자와 팀이 만들었습니다.

최소한의 노력으로 API를 **빌드**, **배포**, **접근**하는 과정을 간소화합니다.

FastAPI로 앱을 빌드할 때의 동일한 **개발자 경험**을 클라우드에 **배포**하는 데까지 확장해 줍니다. 🎉

FastAPI Cloud는 _FastAPI and friends_ 오픈 소스 프로젝트의 주요 스폰서이자 자금 제공자입니다. ✨

#### 다른 클라우드 제공자에 배포하기[¶](https://fastapi.tiangolo.com/ko/#deploy-to-other-cloud-providers)

FastAPI는 오픈 소스이며 표준을 기반으로 합니다. 선택한 어떤 클라우드 제공자에도 FastAPI 앱을 배포할 수 있습니다.

클라우드 제공자의 가이드를 따라 FastAPI 앱을 배포하세요. 🤓

성능[¶](https://fastapi.tiangolo.com/ko/#performance)
---------------------------------------------------

독립된 TechEmpower 벤치마크에서 Uvicorn에서 작동하는 FastAPI 애플리케이션이 [사용 가능한 가장 빠른 Python 프레임워크 중 하나](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7)로 Starlette와 Uvicorn(FastAPI에서 내부적으로 사용)에만 밑돌고 있습니다. (*)

자세한 내용은 [벤치마크](https://fastapi.tiangolo.com/ko/benchmarks/) 섹션을 보십시오.

의존성[¶](https://fastapi.tiangolo.com/ko/#dependencies)
-----------------------------------------------------

FastAPI는 Pydantic과 Starlette에 의존합니다.

### `standard` 의존성[¶](https://fastapi.tiangolo.com/ko/#standard-dependencies)

FastAPI를 `pip install "fastapi[standard]"`로 설치하면 `standard` 그룹의 선택적 의존성이 함께 설치됩니다.

Pydantic이 사용하는:

*   [`email-validator`](https://github.com/JoshData/python-email-validator) - 이메일 유효성 검사.

Starlette이 사용하는:

*   [`httpx`](https://www.python-httpx.org/) - `TestClient`를 사용하려면 필요.
*   [`jinja2`](https://jinja.palletsprojects.com/) - 기본 템플릿 설정을 사용하려면 필요.
*   [`python-multipart`](https://github.com/Kludex/python-multipart) - `request.form()`과 함께 form "파싱" 지원을 원하면 필요.

FastAPI가 사용하는:

*   [`uvicorn`](https://www.uvicorn.dev/) - 애플리케이션을 로드하고 제공하는 서버를 위한 것입니다. 여기에는 고성능 서빙에 필요한 일부 의존성(예: `uvloop`)이 포함된 `uvicorn[standard]`가 포함됩니다.
*   `fastapi-cli[standard]` - `fastapi` 명령을 제공하기 위한 것입니다.
    *   여기에는 FastAPI 애플리케이션을 [FastAPI Cloud](https://fastapicloud.com/)에 배포할 수 있게 해주는 `fastapi-cloud-cli`가 포함됩니다.

### `standard` 의존성 없이[¶](https://fastapi.tiangolo.com/ko/#without-standard-dependencies)

`standard` 선택적 의존성을 포함하고 싶지 않다면, `pip install "fastapi[standard]"` 대신 `pip install fastapi`로 설치할 수 있습니다.

### `fastapi-cloud-cli` 없이[¶](https://fastapi.tiangolo.com/ko/#without-fastapi-cloud-cli)

표준 의존성과 함께 FastAPI를 설치하되 `fastapi-cloud-cli` 없이 설치하고 싶다면, `pip install "fastapi[standard-no-fastapi-cloud-cli]"`로 설치할 수 있습니다.

### 추가 선택적 의존성[¶](https://fastapi.tiangolo.com/ko/#additional-optional-dependencies)

추가로 설치하고 싶을 수 있는 의존성도 있습니다.

추가 선택적 Pydantic 의존성:

*   [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) - 설정 관리를 위한 것입니다.
*   [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) - Pydantic에서 사용할 추가 타입을 위한 것입니다.

추가 선택적 FastAPI 의존성:

*   [`orjson`](https://github.com/ijl/orjson) - `ORJSONResponse`를 사용하려면 필요.
*   [`ujson`](https://github.com/esnme/ultrajson) - `UJSONResponse`를 사용하려면 필요.

라이센스[¶](https://fastapi.tiangolo.com/ko/#license)
-------------------------------------------------

이 프로젝트는 MIT 라이센스 조약에 따라 라이센스가 부여됩니다.
