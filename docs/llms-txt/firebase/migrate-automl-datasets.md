# Source: https://firebase.google.com/docs/ml/migrate-automl-datasets.md.txt

<br />

Firebase MLstores your AutoML training datasets differently, depending on your project's pricing plan. When your project is on the Blaze pricing plan,Firebase MLcreates a newCloud Storagebucket in your project to store AutoML Vision Edge data. When your project is on the Spark pricing plan,Firebase MLstores your AutoML Vision Edge data internally instead of using your project'sCloud Storage.
| Firebase ML's AutoML Vision Edge features are deprecated. Consider using[Vertex AI](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)to automatically train ML models, which you can either[export as TensorFlow Lite models](https://cloud.google.com/vertex-ai/docs/export/export-edge-model)for on-device use or[deploy for cloud-based inference](https://cloud.google.com/vertex-ai/docs/predictions/overview).

If you create a dataset while on the Spark pricing plan and later upgrade to the Blaze plan, your dataset will be available, but will still be subject to the limitations of the Spark plan (these datasets are labeled**Spark datasets** in theFirebaseconsole). If you want your dataset to take advantage of Blaze features, such as unlimited training examples (billed by storage use), you'll have to migrate the Spark dataset to a new dataset.

To migrate a dataset:

1. Open the[AutoML section](https://console.firebase.google.com/project/_/ml/automl)of theFirebaseconsole. (Select your project when prompted.)

2. On the dataset you want to migrate, click**View** to open the details page, then click**Export dataset**. You will download a zip file containing the dataset's training images and labels.

3. Create a new dataset by uploading the zip file. (See[Train your model](https://firebase.google.com/docs/ml/train-image-labeler#train_the_model).)