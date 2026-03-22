# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/web-browser/inference-sdk.md

# 웹 inference-sdk

### WebRTC 스트리밍이란 무엇인가요?

`@roboflow/inference-sdk` 브라우저에서 WebRTC를 사용해 실시간 비디오를 Roboflow의 inference 서버로 스트리밍할 수 있게 해줍니다. 이를 통해 다음을 할 수 있습니다:

* **워크플로 실행** - 복잡한 다단계 컴퓨터 비전 파이프라인 실행
* **모든 모델 접근** - 모든 Roboflow 모델 유형 사용
* **서버 측 처리** - 강력한 GPU 활용
* **낮은 지연** - WebRTC는 거의 실시간에 가까운 결과를 제공합니다
* **양방향 통신** - 스트리밍 중 데이터 전송 및 수신

### 설치

```bash
npm install @roboflow/inference-sdk
```

### 빠른 시작

시작하려면 아래 동영상/샘플 코드를 참조하세요:

{% embed url="<https://www.loom.com/share/48b7c442a69c49e081d0dbec49e1ab57>" %}

```typescript
import { connectors, webrtc, streams } from '@roboflow/inference-sdk';

// ⚠️ 개발 환경에서만 withApiKey 사용
// ⚠️ 프로덕션에서는 사용하지 마세요. API 키가 노출됩니다
// 프로덕션의 경우 백엔드 프록시 사용 (다음 섹션 참조)
const connector = connectors.withApiKey("your-api-key");

// 카메라 스트림 가져오기
const stream = await streams.useCamera({
  video: {
    facingMode: { ideal: "environment" },
    width: { ideal: 640 },
    height: { ideal: 480 }
  }
});

// WebRTC 연결 시작
const connection = await webrtc.useStream({
  source: stream,
  connector,
  wrtcParams: {
    workspaceName: "your-workspace",
    workflowId: "your-workflow",
    imageInputName: "image",
    streamOutputNames: ["output"],
    dataOutputNames: ["predictions"]
  },
  onData: (data) => {
    console.log("Inference results:", data);
  }
});

// 처리된 비디오 표시
const videoElement = document.getElementById('video');
videoElement.srcObject = await connection.remoteStream();

// 완료 시 정리
await connection.cleanup();
```

### 🔐 보안 권장사항

**프로덕션 앱에서는 절대 프런트엔드 코드에 API 키를 노출하지 마세요.**

The `connectors.withApiKey()` 메서드는 데모에 편리하지만 브라우저에 API 키를 노출합니다. **프로덕션에서는 항상 백엔드 프록시를 사용하세요:**

#### 보안된 프로덕션 패턴

**프런트엔드:**

```typescript
import { connectors, webrtc, streams } from '@roboflow/inference-sdk';

// 직접 API 키 대신 프록시 엔드포인트 사용
const connector = connectors.withProxyUrl('/api/init-webrtc');

const stream = await streams.useCamera({ video: true });
const connection = await webrtc.useStream({
  source: stream,
  connector,
  wrtcParams: { /* ... */ }
});
```

**백엔드 (Express):**

```typescript
import { InferenceHTTPClient } from '@roboflow/inference-sdk/api';

app.post('/api/init-webrtc', async (req, res) => {
  const { offer, wrtcparams } = req.body;

  // API 키는 서버에 안전하게 보관됩니다
  const client = InferenceHTTPClient.init({
    apiKey: process.env.ROBOFLOW_API_KEY
  });

  const answer = await client.initializeWebrtcWorker({
    offer,
    workspaceName: wrtcparams.workspaceName,
    workflowId: wrtcparams.workflowId,
    config: {
      imageInputName: wrtcparams.imageInputName,
      streamOutputNames: wrtcparams.streamOutputNames,
      dataOutputNames: wrtcparams.dataOutputNames
    }
  });

  res.json(answer);
});
```

### 핵심 기능

#### 동적 출력 재구성

재시작 없이 실행 중에 스트림 및 데이터 출력을 변경:

```typescript
// 다른 시각화로 전환
connection.reconfigureOutputs({
  streamOutput: ["blur_visualization"]
});

// 모든 데이터 출력 활성화
connection.reconfigureOutputs({
  dataOutput: ["*"]
});

// 둘 다 동시에 변경
connection.reconfigureOutputs({
  streamOutput: ["annotated_image"],
  dataOutput: ["predictions", "counts"]
});
```

### 완전한 작동 예제

프런트엔드와 백엔드 코드가 모두 포함된 전체 작동 예제는 [샘플 애플리케이션 리포지토리](https://github.com/roboflow/inferenceSampleApp). 샘플 앱은 다음을 보여줍니다:

* API 키 보안을 위한 적절한 백엔드 프록시 설정
* 카메라 스트리밍 통합
* 오류 처리 및 연결 관리
* 프로덕션 준비 패턴

### 리소스

* [예제 애플리케이션](https://github.com/roboflow/inferenceSampleApp)
* [NPM 패키지](https://www.npmjs.com/package/@roboflow/inference-sdk)
