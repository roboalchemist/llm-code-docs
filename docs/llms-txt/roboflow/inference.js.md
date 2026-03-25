# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/web-browser/inference.js.md

# 웹 inference.js

`inferencejs` inferencejs는 Roboflow에서 학습된 모델을 사용하여 브라우저를 통해 실시간 추론을 가능하게 하는 JavaScript 패키지입니다.

{% hint style="info" %}
참조는 `inferencejs` 참고문서 [여기](https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/web-browser/inference.js/inferencejs-reference)
{% endhint %}

대부분의 비즈니스 애플리케이션에서는 [Hosted API](https://docs.roboflow.com/roboflow/roboflow-ko/deploy/serverless) 가 적합합니다. 그러나 많은 소비자용 애플리케이션 및 일부 엔터프라이즈 사용 사례에서는 서버에 호스팅된 모델을 사용하는 것이 실용적이지 않을 수 있습니다(예: 사용자가 대역폭 제약이 있거나 원격 API를 사용하여 달성할 수 있는 것보다 더 낮은 지연 시간을 필요로 하는 경우).

### 학습 자료

* **웹캠으로 모델 테스트하기**: 다음에서 웹캠 데모로 [손 감지 모델을 여기에서 시도해볼 수 있습니다](https://demo.roboflow.com/egohands-public/9?publishable_key=rf_5w20VzQObTXjJhTjq6kad9ubrm33) (이 모델은 공개 [EgoHands 데이터셋](https://universe.roboflow.com/brad-dwyer/egohands-public/)).
* **인터랙티브 Replit 환경**: 우리는 "[시작하기](https://replit.com/@roboflow/Roboflow-Getting-Started#style.css)" 프로젝트를 Repl.it에 게시했으며, 함께 제공되는 튜토리얼은 [우리의 Repl.it 템플릿을 사용하여 YOLOv8 모델을 배포하는 방법을 보여줍니다](https://blog.roboflow.com/deploy-yolov8-models-to-replit/).
* **GitHub 템플릿**: [Roboflow 홈페이지는](https://github.com/roboflow/homepage-demo) 를 사용하여 `inferencejs` COCO 추론 위젯을 구동합니다. README에는 리포지토리 템플릿을 사용해 GitHub Pages로 모델을 웹에 배포하는 방법에 대한 지침이 포함되어 있습니다.
* **문서**: 만약 `inferencejs`의 특정 함수들에 대해 더 자세한 정보를 원하시면, [문서 페이지](https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/web-browser/inference.js/inferencejs-reference) 를 확인하세요 또는 아래 가이드에서 `inferencejs` 메서드의 언급을 클릭하면 해당 문서로 이동합니다.

### 지원되는 모델

`inferencejs` 현재 다음 모델 아키텍처를 지원합니다:

* [RF-DETR](https://roboflow.com/model/rf-detr)
* Roboflow 3.0 (YOLOv8 호환)
* YOLOv5
* [시선 감지](https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/web-browser/inferencejs-reference#gazedetections)

### 설치

프로젝트에 `추론을` 추가하려면, npm을 사용해 설치하거나 페이지의 `<head>` 태그에 스크립트 태그 참조를 추가하세요.

```bash
npm install inferencejs
```

```html
<script src="https://cdn.jsdelivr.net/npm/inferencejs"></script>
```

## 초기화 `inferencejs`

### 인증

당신은 Roboflow 워크스페이스 설정에서 `publishable_key` 를 얻을 수 있습니다.

<figure><img src="https://3958014485-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-eba9dfc2cdada466d26a35f6bbb98ef8c1c972e8%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
**참고:** 당신의 `publishable_key` 는 `inferencejs`, **가 아닌** 당신의 **비공개** API 키(이는 비밀로 유지되어야 합니다).
{% endhint %}

시작하려면 `InferenceEngine` 을(를) 가져와 새 inference engine 객체를 생성하세요

{% hint style="info" %}
`inferencejs` 는 메인 UI 스레드를 차단하지 않고 여러 모델을 사용할 수 있도록 webworkers를 사용합니다. 각 모델은 `InferenceEngine` 를 통해 로드되며, 이는 필요한 스레드 관리를 추상화해줍니다.
{% endhint %}

```typescript
import { InferenceEngine } from "inferencejs";
const inferEngine = new InferenceEngine();
```

이제 당신의 `publishable_key` 와 모델 메타데이터(모델 이름 및 버전), 신뢰도 임계값 및 겹침 임계값과 같은 구성 매개변수를 사용하여 roboflow에서 모델을 로드할 수 있습니다.

```typescript
const workerId = await inferEngine.startWorker("[model name]", "[version]", "[publishable key]");
```

`inferencejs` 는 선택한 모델을 실행하는 워커를 시작합니다. 반환된 워커 ID는 우리가 추론에 사용할 `InferenceEngine` 의 워커 ID에 해당합니다. 모델에서 추론하려면 `infer` 메서드를 `InferenceEngine`.

위에서 호출할 수 있습니다. 이미지를 로드하고 우리의 워커에서 추론해봅시다.

```typescript
const image = document.getElementById("image"); // id가 `image`인 이미지 엘리먼트를 가져옵니다
const predictions = await inferEngine.infer(workerId, image); // 이미지에서 추론
```

{% hint style="info" %}
이는 다양한 이미지 형식(`HTMLImageElement`, `HTMLVideoElement`, `ImageBitmap`또는 `TFJS Tensor`).
{% endhint %}

을(를) 받을 수 있습니다. 이것은 예측 배열을 반환합니다(이 경우 클래스 형태로 `RFObjectDetectionPrediction` )

### 설정

만약 `inferencejs` 가 예측을 필터링하는 방식을 사용자화하고 구성하고자 한다면, 생성 시 워커에 매개변수를 전달할 수 있습니다.

```typescript
const configuration = {scoreThreshold: 0.5, iouThreshold: 0.5, maxNumBoxes: 20};
const workerId = await inferEngine.startWorker("[model name]", "[version]", "[publishable key]", configuration);
```

또는 추론 시 구성 옵션을 전달할 수 있습니다

```javascript
const configuration = {
    scoreThreshold: 0.5,
    iouThreshold: 0.5,
    maxNumBoxes: 20
};
const predictions = await inferEngine.infer(workerId, image, configuration);
```
