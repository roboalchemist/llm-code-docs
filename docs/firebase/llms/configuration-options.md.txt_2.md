# Source: https://firebase.google.com/docs/ai-logic/hybrid/web/configuration-options.md.txt

> [!WARNING]
> **Preview** : Using the Firebase AI Logic SDKs to build hybrid experiences in Web apps is a Preview feature, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.
>
> This initial release only **supports on-device inference for
> web apps running on Chrome on Desktop.**

<br />

This page describes the following configuration options:

- [Set an inference mode](https://firebase.google.com/docs/ai-logic/hybrid/web/configuration-options#inference-modes)

- [Override the default cloud-hosted fallback model](https://firebase.google.com/docs/ai-logic/hybrid/web/configuration-options#override-default-cloud-model)

- [Use model configuration to control responses](https://firebase.google.com/docs/ai-logic/hybrid/web/configuration-options#model-config), like
  temperature

You can also
[generate structured output](https://firebase.google.com/docs/ai-logic/hybrid/web/generate-structured-output),
including JSON and enums.

## Before you begin

Make sure that you've completed the
[getting started guide for building hybrid experiences](https://firebase.google.com/docs/ai-logic/hybrid/web/get-started#get-started).

## Set an inference mode

The examples in the getting started guide use the `PREFER_ON_DEVICE` mode, but
this is only one of the four available
[inference modes](https://firebase.google.com/docs/reference/js/ai.hybridparams#hybridparamsmode).

> [!NOTE]
> **Note:** For requests sent to the on-device model, make sure it's [supported by on-device inference](https://firebase.google.com/docs/ai-logic/hybrid/web/get-started#features-not-yet-available).   
> For requests sent off-device, the device must be online. Also, the **default cloud-hosted model is
> `gemini-2.5-flash-lite`** , but you can [override the default](https://firebase.google.com/docs/ai-logic/hybrid/web/configuration-options#override-default-cloud-model).

- **`PREFER_ON_DEVICE`** : Use the on-device model if it's available;
  otherwise, *fall back to the cloud-hosted model*.

      const model = getGenerativeModel(ai, { mode: InferenceMode.PREFER_ON_DEVICE });

- **`ONLY_ON_DEVICE`** : Use the on-device model if it's available;
  otherwise, *throw an exception*.

      const model = getGenerativeModel(ai, { mode: InferenceMode.ONLY_ON_DEVICE });

- **`PREFER_IN_CLOUD`** : Use the cloud-hosted model if it's available;
  otherwise, *fall back to the on-device model*.

      const model = getGenerativeModel(ai, { mode: InferenceMode.PREFER_IN_CLOUD });

- **`ONLY_IN_CLOUD`** : Use the cloud-hosted model if it's available;
  otherwise, *throw an exception*.

      const model = getGenerativeModel(ai, { mode: InferenceMode.ONLY_IN_CLOUD });

> [!NOTE]
> **Note:** **Downloading the on-device model can take several minutes.**   
> If you haven't yet [downloaded the model before your first request for on-device inference](https://firebase.google.com/docs/ai-logic/hybrid/web/get-started#instructions-to-download-on-device-model), the request will automatically start the model download in the background (which can significantly delay receiving a response to that request).

### Determine whether on-device or in-cloud inference was used

If you use `PREFER_ON_DEVICE` or `PREFER_IN_CLOUD` inference modes, then it
might be helpful to know which mode was used for given requests. This
information is provided by the `inferenceSource` property of each response
(available starting with JS SDK v12.5.0).

When you access this property, the returned value will be either
`ON_DEVICE` or `IN_CLOUD`.

    // ...

    console.log('You used: ' + result.response.inferenceSource);

    console.log(result.response.text());

## Override the default fallback model

**The default cloud-hosted model is
`gemini-2.5-flash-lite`**
(starting with JS SDK v12.8.0).

This model is the fallback cloud-hosted model when you use the
`PREFER_ON_DEVICE` mode. It's also the default model when you use the
`ONLY_IN_CLOUD` mode or the `PREFER_IN_CLOUD` mode.

You can use the
[`inCloudParams`](https://firebase.google.com/docs/reference/js/ai.hybridparams#hybridparamsincloudparams)
configuration option to specify an alternative default cloud-hosted model.

    const model = getGenerativeModel(ai, {
      mode: InferenceMode.INFERENCE_MODE,
      inCloudParams: {
        model: "GEMINI_MODEL_NAME"
      }
    });

Find model names for all
[supported Gemini models](https://firebase.google.com/docs/ai-logic/models).

## Use model configuration to control responses

In each request to a model, you can send along a model configuration to control
how the model generates a response. Cloud-hosted models and on-device models
offer different configuration options.

The configuration is maintained for the lifetime of the instance. If you want to
use a different config, create a new `GenerativeModel` instance with that
config.

> [!NOTE]
> **Note:** You can [generate structured output (like JSON and enums)](https://firebase.google.com/docs/ai-logic/hybrid/web/generate-structured-output) by configuring the model to respond with structured output.

### Configure cloud-hosted model

Use the
[`inCloudParams`](https://firebase.google.com/docs/reference/js/ai.hybridparams#hybridparamsincloudparams)
option to configure a cloud-hosted Gemini model. Learn about
[available parameters](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-gemini).

    const model = getGenerativeModel(ai, {
      mode: InferenceMode.INFERENCE_MODE,
      inCloudParams: {
        model: "GEMINI_MODEL_NAME"
        temperature: 0.8,
        topK: 10
      }
    });

### Configure on-device model

Note that inference using an on-device model uses the
[Prompt API from Chrome](https://developer.chrome.com/docs/extensions/ai/prompt-api).

Use the
[`onDeviceParams`](https://firebase.google.com/docs/reference/js/ai.hybridparams#hybridparamsondeviceparams)
option to configure an on-device model. Learn about
[available parameters](https://github.com/webmachinelearning/prompt-api?tab=readme-ov-file#configuration-of-per-session-parameters).

    const model = getGenerativeModel(ai, {
      mode: InferenceMode.INFERENCE_MODE,
      onDeviceParams: {
        createOptions: {
          temperature: 0.8,
          topK: 8
        }
      }
    });