# Source: https://firebase.google.com/docs/ml/use-custom-models.md.txt

# Custom Models

If you use custom
[TensorFlow Lite](https://www.tensorflow.org/lite/) models,
Firebase ML can help you ensure your users are always using the
best-available version of your custom model. When you deploy your model with
Firebase, Firebase ML only downloads the model when it's needed and
automatically updates your users with the latest version.

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/ml/ios/use-custom-models)
[Android](https://firebase.google.com/docs/ml/android/use-custom-models)

<br />

This is a beta release of Firebase ML. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|---|---|
| TensorFlow Lite model deployment | Deploy your models using Firebase to reduce your app's binary size and to make sure your app is always using the most recent version available of your model |
| On-device ML inference | Perform inference in an Apple or Android app using the TensorFlow Lite interpreter with your model. |
| Automatic model updates | Configure the conditions under which your app automatically downloads new versions of your model: when the user's device is idle, is charging, or has a Wi-Fi connection |

## Implementation path

|---|---|---|
|   | **Train your TensorFlow model** | Build and train a custom model using TensorFlow. Or, re-train an existing model that solves a problem similar to what you want to achieve. |
|   | **Convert the model to TensorFlow Lite** | Convert your model from HDF5 or frozen graph format to TensorFlow Lite using the [TensorFlow Lite converter](https://www.tensorflow.org/lite/convert). |
|   | **Deploy your TensorFlow Lite model to Firebase** | Optional: When you deploy your TensorFlow Lite model to Firebase and include the Firebase ML SDK in your app, Firebase ML keeps your users up to date with the latest version of your model. You can configure it to automatically download model updates when the user's device is idle or charging, or has a Wi-Fi connection. |
|   | **Use the TensorFlow Lite model for inference** | Use the TensorFlow Lite interpreter in your Apple or Android app to perform inference with models deployed using Firebase. |

## Codelabs

Try some [codelabs](https://firebase.google.com/docs/ml/codelabs) to learn hands-on how Firebase can help you use
TensorFlow Lite models more easily and effectively.