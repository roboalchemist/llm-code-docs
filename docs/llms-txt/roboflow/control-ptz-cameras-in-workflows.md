# Source: https://docs.roboflow.com/changelog/explore-by-month/june-2025/control-ptz-cameras-in-workflows.md

# Control PTZ Cameras in Workflows

<figure><img src="https://2667452268-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMR3m936tBXGm5QsAcPwe%2Fuploads%2FbQ6sDtKr03VD5RFMin2w%2F455510727-7c4cd4e6-8271-459e-9e6d-c990ed4ecd12.png?alt=media&#x26;token=96e9443f-5ca3-4e6a-a371-61bece88cbda" alt=""><figcaption></figcaption></figure>

You can now control any PTZ camera that supports the ONVIF protocol using Roboflow Workflows.

Two options are available:

* **Follow:** The object it follows is the maximum confidence prediction out of all predictions passed into it. To follow a specific object, use the appropriate filters on the predictiion object to specify the object you want to follow. Additionally if a tracker is used, the camera will follow the tracked object until it disappears.
* **Move to Preset:** The camera can also move to a defined preset position. The camera must support the GotoPreset service.

[ You can read the full release notes on GitHub.](https://github.com/roboflow/inference/releases/tag/v0.50.5)
