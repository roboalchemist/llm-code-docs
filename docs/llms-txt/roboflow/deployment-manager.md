# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager/making-changes/deployment-manager.md

# Deployment Manager 재배포

어떤 경우에는 Deployment Manager를 기존 장치에 다시 배포(redeploy)해야 합니다. 이는 기존 장치가 손상되었거나 하드웨어 복구가 불가능한 오류가 발생했을 때 가장 흔합니다.&#x20;

수작업을 하지 않고도 장치를 다시 배포하면 한 번의 단계로 모든 Roboflow 구성(Roboflow configurations)을 완전히 복구할 수 있습니다.&#x20;

:warning: 첫 번째 장치가 여전히 작동 중인 동안에는 다른 장치에 manager를 다시 배포하지 않도록 해주십시오.

새 장치에 다시 배포하려면 해당 장치의 Deployment Manager 대시보드를 방문하세요. 그런 다음 오른쪽 상단의 옵션 메뉴를 열고 "Redeploy Device"를 클릭하세요.

<figure><img src="https://3958014485-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fzfc395Dg7MilGGZApAY8%2FScreenshot%202026-01-08%20at%2011.16.35%E2%80%AFAM.png?alt=media&#x26;token=ebbfe3ab-2316-4ab8-a741-4ddfccb588b1" alt="" width="164"><figcaption></figcaption></figure>

그런 다음 설치 스크립트를 받으려면 "Generate Redeploy Command"를 클릭하세요.

<figure><img src="https://3958014485-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FPrfqy0McmWUokdCMy8xo%2FScreenshot%202026-01-08%20at%2011.23.04%E2%80%AFAM.png?alt=media&#x26;token=d68dbabd-9d96-47bf-995c-ce409ea20255" alt="" width="375"><figcaption></figcaption></figure>

설치 스크립트를 복사한 후 권한이 상승된 터미널에서 장치에 실행하세요.&#x20;

<figure><img src="https://3958014485-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FMMEAsk7iDvN9rnPZxXvN%2FScreenshot%202026-01-08%20at%2011.25.29%E2%80%AFAM.png?alt=media&#x26;token=ce900b81-2fb8-442e-98d1-12a240990bd7" alt="" width="375"><figcaption></figcaption></figure>

:warning: 설치 스크립트는 활성화된 상태가 10분으로 제한되며 만료됩니다. 만료된 후에는 설치 스크립트를 다시 생성해야 합니다.
