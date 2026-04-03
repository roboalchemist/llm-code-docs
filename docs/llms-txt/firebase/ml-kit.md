# Source: https://firebase.google.com/docs/ml-kit.md.txt

# ML Kit for Firebase

plat_iosplat_android  
Use machine learning in your apps to solve real-world problems.
| This page describes an old version of this SDK, called ML Kit for Firebase. The functionality of this SDK has been split into:
|
| - [Firebase ML](https://firebase.google.com/docs/ml), which includes all of Firebase's cloud-based ML features.
| - [ML Kit](https://developers.google.com/ml-kit), a standalone library for on-device ML, which you can use with or without Firebase.

ML Kit is a mobile SDK that brings Google's machine learning expertise to Android and iOS apps in a powerful yet easy-to-use package. Whether you're new or experienced in machine learning, you can implement the functionality you need in just a few lines of code. There's no need to have deep knowledge of neural networks or model optimization to get started. On the other hand, if you are an experienced ML developer, ML Kit provides convenient APIs that help you use your custom TensorFlow Lite models in your mobile apps.
| This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Production-ready for common use cases | ML Kit comes with a set of ready-to-use APIs for common mobile use cases: recognizing text, detecting faces, identifying landmarks, scanning barcodes, labeling images, and identifying the language of text. Simply pass in data to the ML Kit library and it gives you the information you need.                  |
| On-device or in the cloud             | ML Kit's selection of APIs run on-device or in the cloud. Our on-device APIs can process your data quickly and work even when there's no network connection. Our cloud-based APIs, on the other hand, leverage the power ofGoogle Cloud's machine learning technology to give you an even higher level of accuracy. |
| Deploy custom models                  | If ML Kit's APIs don't cover your use cases, you can always bring your own existing TensorFlow Lite models. Just upload your model to Firebase, and we'll take care of hosting and serving it to your app. ML Kit acts as an API layer to your custom model, making it simpler to run and use.                      |

## How does it work?

ML Kit makes it easy to apply ML techniques in your apps by bringing Google's ML technologies, such as the[Google Cloud Vision API](https://cloud.google.com/vision/),[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/), and the[Android Neural Networks API](https://developer.android.com/ndk/guides/neuralnetworks/)together in a single SDK. Whether you need the power of cloud-based processing, the real-time capabilities of mobile-optimized on-device models, or the flexibility of custom TensorFlow Lite models, ML Kit makes it possible with just a few lines of code.

### What features are available on device or in the cloud?

|                                         Feature                                          | On-device | Cloud |
|------------------------------------------------------------------------------------------|-----------|-------|
| [Text recognition](https://firebase.google.com/docs/ml-kit/recognize-text)               |           |       |
| [Face detection](https://firebase.google.com/docs/ml-kit/detect-faces)                   |           |       |
| [Barcode scanning](https://firebase.google.com/docs/ml-kit/read-barcodes)                |           |       |
| [Image labeling](https://firebase.google.com/docs/ml-kit/label-images)                   |           |       |
| [Object detection \& tracking](https://firebase.google.com/docs/ml-kit/object-detection) |           |       |
| [Landmark recognition](https://firebase.google.com/docs/ml-kit/recognize-landmarks)      |           |       |
| [Language identification](https://firebase.google.com/docs/ml-kit/identify-languages)    |           |       |
| [Translation](https://firebase.google.com/docs/ml-kit/translation)                       |           |       |
| [Smart Reply](https://firebase.google.com/docs/ml-kit/generate-smart-replies)            |           |       |
| [AutoML model inference](https://firebase.google.com/docs/ml-kit/automl-image-labeling)  |           |       |
| [Custom model inference](https://firebase.google.com/docs/ml-kit/use-custom-models)      |           |       |

| Use of ML Kit to access Cloud ML functionality is subject to the[Google Cloud Platform License Agreement](https://cloud.google.com/terms/)and[Service Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the Firebase[Pricing](https://firebase.google.com/pricing)page.

## Implementation path

|---|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Integrate the SDK               | Quickly include the SDK using Gradle or CocoaPods.                                                                                                                                                                                                                                                                                                       |
|   | Prepare input data              | For example, if you're using a vision feature, capture an image from the camera and generate the necessary metadata such as image rotation, or prompt the user to select a photo from their gallery.                                                                                                                                                     |
|   | Apply the ML model to your data | By applying the ML model to your data, you generate insights such as the emotional state of detected faces or the objects and concepts that were recognized in the image, depending on the feature you used. Use these insights to power features in your app like photo embellishment, automatic metadata generation, or whatever else you can imagine. |

## Next steps

- Explore the ready-to-use APIs:[text recognition](https://firebase.google.com/docs/ml-kit/recognize-text),[face detection](https://firebase.google.com/docs/ml-kit/detect-faces),[barcode scanning](https://firebase.google.com/docs/ml-kit/read-barcodes),[image labeling](https://firebase.google.com/docs/ml-kit/label-images),[object detection \& tracking](https://firebase.google.com/docs/ml-kit/object-detection),[landmark recognition](https://firebase.google.com/docs/ml-kit/recognize-landmarks),[Smart Reply](https://firebase.google.com/docs/ml-kit/generate-smart-replies),[translation](https://firebase.google.com/docs/ml-kit/translation), and[language identification](https://firebase.google.com/docs/ml-kit/identify-languages).
- Train your own image labeling model with[AutoML Vision Edge](https://firebase.google.com/docs/ml-kit/automl-image-labeling).
- Learn about using mobile-optimized[custom models](https://firebase.google.com/docs/ml-kit/use-custom-models)in your app.