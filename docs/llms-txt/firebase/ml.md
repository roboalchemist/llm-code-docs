# Source: https://firebase.google.com/docs/ml.md.txt

# Firebase Machine Learning

plat_iosplat_androidplat_flutter  
Use machine learning in your apps to solve real-world problems.  

Firebase Machine Learningis a mobile SDK that brings Google's machine learning expertise to Android and Apple apps in a powerful yet easy-to-use package. Whether you're new or experienced in machine learning, you can implement the functionality you need in just a few lines of code. There's no need to have deep knowledge of neural networks or model optimization to get started. On the other hand, if you are an experienced ML developer,Firebase MLprovides convenient APIs that help you use your custom TensorFlow Lite models in your mobile apps.
| This is a beta release ofFirebase ML. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host and deploy custom models         | Use your own TensorFlow Lite models for on-device inference. Just deploy your model to Firebase, and we'll take care of hosting and serving it to your app. Firebase will dynamically serve the latest version of the model to your users, allowing you to regularly update them without having to push a new version of your app to users. When you useFirebase MLwith[Remote Config](https://firebase.google.com/docs/remote-config), you can serve different models to different user segments, and with[A/B Testing](https://firebase.google.com/docs/ab-testing), you can run experiments to find the best performing model (see the[Apple](https://firebase.google.com/docs/ml/ios/ab-test-models)and[Android](https://firebase.google.com/docs/ml/android/ab-test-models)guides). |
| Production-ready for common use cases | Firebase MLcomes with a set of ready-to-use APIs for common mobile use cases: recognizing text, labeling images, and identifying landmarks. Simply pass in data to theFirebase MLlibrary and it gives you the information you need. These APIs leverage the power ofGoogle Cloud's machine learning technology to give you the highest level of accuracy.                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Cloud vs. on-device

Firebase MLhas APIs that work either in the cloud or on the device. When we describe an ML API as being a cloud API or on-device API, we are describing*which machine performs inference* : that is, which machine uses the ML model to discover insights about the data you provide it. InFirebase ML, this happens either onGoogle Cloud, or on your users' mobile devices.

The text recognition, image labeling, and landmark recognition APIs perform inference in the cloud. These models have more computational power and memory available to them than a comparable on-device model, and as a result, can perform inference with greater accuracy and precision than an on-device model. On the other hand, every request to these APIs requires a network round-trip, which makes them unsuitable for real-time and low-latency applications such as video processing.

The custom model APIs deal with ML models that run on the device. The models used and produced by these features are[TensorFlow Lite](https://tensorflow.org/lite)models, which are optimized to run on mobile devices. The biggest advantage to these models is that they don't require a network connection and can run very quickly---fast enough, for example, to process frames of video in real time.

Firebase MLprovides the ability to deploy custom models to your users' devices by uploading them to our servers. Your Firebase-enabled app will download the model to the device on demand. This allows you to keep your app's initial install size small, and you can swap the ML model without having to republish your app.

## ML Kit: Ready-to-use on-device models

| On June 3, 2020, we started offering ML Kit's on-device APIs through a[new standalone SDK](https://developers.google.com/ml-kit).Google CloudAPIs and custom model deployment will continue to be available through Firebase Machine Learning.

If you're looking for pre-trained models that run on the device, check out[ML Kit](https://developers.google.com/ml-kit). ML Kit is available for iOS and Android, and has APIs for many use cases:

- Text recognition
- Image labeling
- Object detection and tracking
- Face detection and contour tracing
- Barcode scanning
- Language identification
- Translation
- Smart Reply

## Next steps

- Explore the ready-to-use APIs:[text recognition](https://firebase.google.com/docs/ml/recognize-text),[image labeling](https://firebase.google.com/docs/ml/label-images), and[landmark recognition](https://firebase.google.com/docs/ml/recognize-landmarks).
- Learn about using mobile-optimized[custom models](https://firebase.google.com/docs/ml/use-custom-models)in your app.