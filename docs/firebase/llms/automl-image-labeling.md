# Source: https://firebase.google.com/docs/ml/automl-image-labeling.md.txt

# AutoML Vision Edge

plat_iosplat_android  
Create custom image classification models from your own training data with AutoML Vision Edge.

![](https://firebase.google.com/static/docs/ml/images/automl.png)

If you want to recognize contents of an image, one option is to use ML Kit's[on-device image labeling API](https://developers.google.com/ml-kit/vision/image-labeling)or[on-device object detection API](https://developers.google.com/ml-kit/vision/object-detection). The models used by these APIs are built for general-purpose use, and are trained to recognize the most commonly-found concepts in photos.

If you need a more specialized image labeling or object detection model, covering a narrower domain of concepts in more detail---for example, a model to distinguish between species of flowers or types of food---you can useFirebase MLand AutoML Vision Edge to train a model with your own images and categories. The custom model is trained inGoogle Cloud, and once the model is ready, it's used fully on the device.
| Firebase ML's AutoML Vision Edge features are deprecated. Consider using[Vertex AI](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)to automatically train ML models, which you can either[export as TensorFlow Lite models](https://cloud.google.com/vertex-ai/docs/export/export-edge-model)for on-device use or[deploy for cloud-based inference](https://cloud.google.com/vertex-ai/docs/predictions/overview).

[Get started with image labeling](https://firebase.google.com/docs/ml/ios/train-image-labeler)[Get started with object detection](https://firebase.google.com/docs/ml/android/train-object-detector)

## Key capabilities

|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Train models based on your data | Automatically train custom image labeling and object detection models to recognize the labels you care about, using your training data.                                                                                                                                                |
| Built-in model hosting          | Host your models with Firebase, and load them at run time. By hosting the model on Firebase, you can make sure users have the latest model without releasing a new app version. And, of course, you can also bundle the model with your app, so it's immediately available on install. |

| **Running AutoML models in the cloud**
|
| These pages only discuss generating mobile-optimized models intended to run on the device. However, for models with many thousands of labels or when significantly higher accuracy is required, you might want to run a server-optimized model in the cloud instead, which you can do by calling the Cloud AutoML Vision APIs directly. See[Making an online prediction](https://cloud.google.com/vision/automl/docs/predict).
|
| Note that unlike running AutoML Vision Edge models on device, running a cloud-based AutoML model is billed per invocation.

## Implementation path

|---|---------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|   | Assemble training data    | Put together a dataset of examples of each label you want your model to recognize.                                               |
|   | Train a new model         | In theGoogle Cloudconsole, import your training data and use it to train a new model.                                            |
|   | Use the model in your app | Bundle the model with your app or download it from Firebase when it's needed. Then, use the model to label images on the device. |

## Pricing \& Limits

To train custom models with AutoML Vision Edge, you must be on the pay-as-you-go (Blaze) plan.
| **Important:** You can no longer train models with AutoML Vision Edge while on the Spark plan. If you previously trained models while on the Spark plan, your training data and trained models are still accessible from theFirebaseconsole in read-only mode. If you want to keep this data download it before March 1, 2021.

|      Datasets      | Billed according to[Cloud Storage rates](https://cloud.google.com/storage/pricing) |
| Images per dataset |                                     1,000,000                                      |
|   Training hours   |                                 No per-model limit                                 |
|--------------------|------------------------------------------------------------------------------------|

## Next steps

- Learn how to[train an image labeling model](https://firebase.google.com/docs/ml/train-image-labeler).
- Learn how to[train an object detection model](https://firebase.google.com/docs/ml/train-object-detector).