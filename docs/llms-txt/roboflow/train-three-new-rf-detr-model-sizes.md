# Source: https://docs.roboflow.com/changelog/explore-by-month/july-2025/train-three-new-rf-detr-model-sizes.md

# Train Three New RF-DETR Model Sizes

<figure><img src="https://2667452268-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMR3m936tBXGm5QsAcPwe%2Fuploads%2FW3VNLXjy5cPANWXtzV6G%2FScreenshot%202025-07-23%20at%2011.03.21.png?alt=media&#x26;token=12eacda7-0505-4072-a135-e6c26dac5424" alt=""><figcaption></figcaption></figure>

You can now train three new RF-DETR model sizes in the Roboflow platform:

* Nano
* Small
* Medium

These models are available in addition to the Base model size we released earlier this year.

RF-DETR Nano, Small, and Medium are all about as fast as YOLO11 models at the respective size while being significantly more accurate.

To train an RF-DETR model, go to a dataset version in a Roboflow project, click "Custom Train", and select RF-DETR. You will then be able to choose from the new model sizes.

All trained models can be deployed via Roboflow Workflows both in the cloud (with the [Roboflow Serverless V2 API](https://docs.roboflow.com/deploy/serverless-hosted-api-v2) or a [Dedicated Deployment](https://docs.roboflow.com/deploy/dedicated-deployments)), or on your own hardware (with Roboflow Inference).
