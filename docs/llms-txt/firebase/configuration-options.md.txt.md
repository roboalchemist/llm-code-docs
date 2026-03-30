# Source: https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options.md.txt

> [!WARNING]
> **Experimental:** Using the Firebase AI Logic SDK to build hybrid experiences is an Experimental feature (and ML Kit's Prompt API is in beta), which means that this feature isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

This page describes the following configuration options for hybrid experiences:

- [Set an inference mode.](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#inference-modes)

- [Determine whether on-device or in-cloud inference was used.](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#determine-inference-mode)

- [Specify a cloud-hosted model to use.](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#specify-cloud-model)

- [Use model configuration to control responses (like temperature).](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#model-config)

**Make sure that you've completed the
[getting started guide for building hybrid experiences](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#get-started).**

## Set an inference mode

The examples in the getting started guide use the `PREFER_ON_DEVICE` mode, but
this is only one of the four available
[inference modes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/InferenceMode).

> [!NOTE]
> **Note** : Keep the following in mind:
>
> - To use an on-device model, make sure to review the list of [not-yet-available
>   features for on-device inference](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#features-not-yet-available) on the get started page.
> - To use a cloud-hosted model, the device must be online and you must explicitly [specify
>   a cloud-hosted model to use](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#specify-cloud-model).
> - As part of the response, the SDK tells you [whether
>   on-device or in-cloud inference was used](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#determine-inference-mode).

Here are the available inference modes:

- **`PREFER_ON_DEVICE`** : Attempt to use the on-device model if it's available
  and supports the type of request. Otherwise, log an error on the device and
  then automatically *fall back to the cloud-hosted model*.

  ### Kotlin

      val config = OnDeviceConfig(mode = InferenceMode.PREFER_ON_DEVICE)

  ### Java

      InferenceMode mode = InferenceMode.PREFER_ON_DEVICE;
      OnDeviceConfig config = new OnDeviceConfig(mode);

- **`ONLY_ON_DEVICE`** : Attempt to use the on-device model if it's available
  and supports the type of request. Otherwise, *throw an exception*.

  ### Kotlin

      val config = OnDeviceConfig(mode = InferenceMode.ONLY_ON_DEVICE)

  ### Java

      InferenceMode mode = InferenceMode.ONLY_ON_DEVICE;
      OnDeviceConfig config = new OnDeviceConfig(mode);

- **`PREFER_IN_CLOUD`** : Attempt to use the cloud-hosted model if the device is
  online and if the model is available. If the device is offline,
  *fall back to the on-device model* . In all other failure cases,
  *throw an exception*.

  ### Kotlin

      val config = OnDeviceConfig(mode = InferenceMode.PREFER_IN_CLOUD)

  ### Java

      InferenceMode mode = InferenceMode.PREFER_IN_CLOUD;
      OnDeviceConfig config = new OnDeviceConfig(mode);

- **`ONLY_IN_CLOUD`** : Attempt to use the cloud-hosted model if the device is
  online and if the model is available. Otherwise, *throw an exception*.

  ### Kotlin

      val config = OnDeviceConfig(mode = InferenceMode.ONLY_IN_CLOUD)

  ### Java

      InferenceMode mode = InferenceMode.ONLY_IN_CLOUD;
      OnDeviceConfig config = new OnDeviceConfig(mode);

## Determine whether on-device or in-cloud inference was used

If you use `PREFER_ON_DEVICE` or `PREFER_IN_CLOUD` inference modes, then it
might be helpful to know which mode was used for given requests. This
information is provided by the `inferenceSource` property of each response.

When you access this property, the returned value will be either `ON_DEVICE` or
`IN_CLOUD`.

### Kotlin

    // ...

    print("You used: ${result.response.inferenceSource}")

    print(result.response.text)

### Java

    // ...

    System.out.println("You used: " + result.getResponse().getInferenceSource());

    System.out.println(result.getResponse().getText());

## Specify a cloud-hosted model to use

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

If your primary or fallback inference might be performed by a cloud-hosted
model, then you need to explicitly specify a cloud model to use when you create
the
[`generativeModel`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel)
instance.

### Kotlin

    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
        .generativeModel(
            modelName = "MODEL_NAME",
            onDeviceConfig = OnDeviceConfig(mode = InferenceMode.PREFER_ON_DEVICE)
        )

### Java

    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
        .generativeModel(
            "MODEL_NAME",
            new OnDeviceConfig(InferenceMode.PREFER_ON_DEVICE)
        );

    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

Find model names for all
[supported Gemini models](https://firebase.google.com/docs/ai-logic/models).

## Use model configuration to control responses

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

In each request to a model, you can send along a model configuration to control
how the model generates a response. Cloud-hosted models and on-device models
offer different configuration options
([cloud](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-gemini)
vs
[on-device](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig)
parameters).

For cloud-hosted models, set their configuration directly in the model's
configuration. However, for the on-device models, set their configuration within
an
[`onDeviceConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig).

The configuration is maintained for the lifetime of the instance. If you want to
use a different config, create a new `GenerativeModel` instance with that
config.

Here's an example that sets the configurations for the cloud-hosted and
on-device models that could be used if `PREFER_ON_DEVICE` inference mode is
set:

### Kotlin

    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
        .generativeModel("MODEL_NAME",
            // Config for cloud-hosted model
            generationConfig = generationConfig {
              temperature = 0.8f,
              topK = 10
            },
            // Config for on-device model
            onDeviceConfig = onDeviceConfig {
              mode = InferenceMode.PREFER_ON_DEVICE,
              temperature = 0.8f,
              topK = 5
            })

### Java

    // Config for cloud-hosted model
    GenerationConfig generationConfig = new GenerationConfig.Builder()
        .setTemperature(0.8f)
        .setTopK(10)
        .build();

    // Config for on-device model
    OnDeviceConfig onDeviceConfig = new OnDeviceConfig.Builder()
        .setMode(InferenceMode.PREFER_ON_DEVICE)
        .setTemperature(0.8f)
        .setTopK(5)
        .build();

    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
        .generativeModel(
            "MODEL_NAME",
            generationConfig,
            onDeviceConfig
        );

    GenerativeModelFutures model = GenerativeModelFutures.from(ai);