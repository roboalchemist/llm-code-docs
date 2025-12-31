# Source: https://firebase.google.com/docs/reference/js/ai.hybridparams.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configures hybrid inference.

**Signature:**  

    export interface HybridParams 

## Properties

|                                                   Property                                                    |                                                     Type                                                      |                                           Description                                           |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [inCloudParams](https://firebase.google.com/docs/reference/js/ai.hybridparams.md#hybridparamsincloudparams)   | [ModelParams](https://firebase.google.com/docs/reference/js/ai.modelparams.md#modelparams_interface)          | ***(Public Preview)*** Optional. Specifies advanced params for in-cloud inference.              |
| [mode](https://firebase.google.com/docs/reference/js/ai.hybridparams.md#hybridparamsmode)                     | [InferenceMode](https://firebase.google.com/docs/reference/js/ai.md#inferencemode)                            | ***(Public Preview)*** Specifies on-device or in-cloud inference. Defaults to prefer on-device. |
| [onDeviceParams](https://firebase.google.com/docs/reference/js/ai.hybridparams.md#hybridparamsondeviceparams) | [OnDeviceParams](https://firebase.google.com/docs/reference/js/ai.ondeviceparams.md#ondeviceparams_interface) | ***(Public Preview)*** Optional. Specifies advanced params for on-device inference.             |

## HybridParams.inCloudParams

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Optional. Specifies advanced params for in-cloud inference.

**Signature:**  

    inCloudParams?: ModelParams;

## HybridParams.mode

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Specifies on-device or in-cloud inference. Defaults to prefer on-device.

**Signature:**  

    mode: InferenceMode;

## HybridParams.onDeviceParams

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Optional. Specifies advanced params for on-device inference.

**Signature:**  

    onDeviceParams?: OnDeviceParams;