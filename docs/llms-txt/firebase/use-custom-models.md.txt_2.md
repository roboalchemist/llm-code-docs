# Source: https://firebase.google.com/docs/ml-kit/use-custom-models.md.txt

# Custom Models

> [!CAUTION]
> This page is about an old version of the
> Custom Models API, which was part of ML Kit for
> Firebase. For the latest docs, see
> [the latest version](https://firebase.google.com/docs/ml/use-custom-models)
> in the
> Firebase ML section.

If you're an experienced ML developer and ML Kit's pre-built models don't
meet your needs, you can use a custom
[TensorFlow Lite](https://www.tensorflow.org/lite/) model with
ML Kit.

Host your TensorFlow Lite models using Firebase or package them with your app.
Then, use the ML Kit SDK to perform inference using the best-available
version of your custom model.
If you host your model with Firebase, ML Kit automatically updates your users
with the latest version.

[iOS](https://firebase.google.com/docs/ml-kit/ios/use-custom-models)
[Android](https://firebase.google.com/docs/ml-kit/android/use-custom-models)
This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|---|---|
| TensorFlow Lite model hosting | Host your models using Firebase to reduce your app's binary size and to make sure your app is always using the most recent version available of your model |
| On-device ML inference | Perform inference in an iOS or Android app by using the ML Kit SDK to run your custom TensorFlow Lite model. The model can be bundled with the app, hosted in the Cloud, or both. |
| Automatic model fallback | Specify multiple model sources; use a locally-stored model when the Cloud-hosted model is unavailable |
| Automatic model updates | Configure the conditions under which your app automatically downloads new versions of your model: when the user's device is idle, is charging, or has a Wi-Fi connection |

## Implementation path

|---|---|---|
|   | **Train your TensorFlow model** | Build and train a custom model using TensorFlow. Or, re-train an existing model that solves a problem similar to what you want to achieve. See the TensorFlow Lite [Developer Guide](https://www.tensorflow.org/mobile/tflite/devguide). |
|   | **Convert the model to TensorFlow Lite** | Convert your model from standard TensorFlow format to TensorFlow Lite by freezing the graph, and then using the TensorFlow Optimizing Converter (TOCO). See the TensorFlow Lite [Developer Guide](https://www.tensorflow.org/mobile/tflite/devguide). |
|   | **Host your TensorFlow Lite model with Firebase** | Optional: When you host your TensorFlow Lite model with Firebase and include the ML Kit SDK in your app, ML Kit keeps your users up to date with the latest version of your model. You can configure ML Kit to automatically download model updates when the user's device is idle or charging, or has a Wi-Fi connection. |
|   | **Use the TensorFlow Lite model for inference** | Use ML Kit's custom model APIs in your iOS or Android app to perform inference with your Firebase-hosted or app-bundled model. |