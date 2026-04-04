# Source: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/llms.txt

# Rekognition Custom Labels Guide

> Amazon Rekognition Custom Labels allows you to train a machine learning model that detect objects, scenes and concepts in images.

- [What is Amazon Rekognition Custom Labels?](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html)
- [Understanding Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/understanding-custom-labels.html)
- [Classifying images](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tutorial-classification.html)
- [Analyzing an image with a trained model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/detecting-custom-labels.html)
- [Security](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/sc-introduction.html)
- [Guidelines and quotas](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/limits.html)
- [API reference](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/custom-labels-api-reference.html)
- [Document history](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/document-history.html)

## [Setting up Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/setting-up.html)

- [Step 1: Create an AWS account](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-account.html): In this step, you create an AWS account, create an administrative user, and learn about granting programmatic access to the AWS SDK.
- [Step 2: Set up console permissions](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-console-policy.html): To use the Amazon Rekognition console you need add to have appropriate permissions.
- [Step 3: Create the console bucket](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-create-console-bucket.html): You use an Amazon Rekognition Custom Labels project to create and manage your models.

### [Step 4: Set up the AWS CLI and AWS SDKs](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-awscli-sdk.html)

You can use Amazon Rekognition Custom Labels with the AWS Command Line Interface (AWS CLI) and AWS SDKs.

- [Grant programmatic access](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-sdk-programmatic-access.html): Grant programmatic access to AWS CLI and AWS SDKs.
- [Set up SDK permissions](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-sdk-permissions.html): To use Amazon Rekognition Custom Labels SDK operations, you need access permissions to the Amazon Rekognition Custom Labels API and the Amazon S3 bucket used for model training.
- [Call an operation](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-sdk-list-projects.html): Call an Amazon Rekognition Custom Labels operation.
- [Step 5: (Optional) Encrypt training files](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-encrypt-bucket.html): You can choose one of the following options to encrypt the Amazon Rekognition Custom Labels manifest files and image files that are in a console bucket or an external Amazon S3 bucket.
- [Step 6: (Optional) Associate prior datasets](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-associate-prior-dataset.html): Amazon Rekognition Custom Labels now manages datasets with projects.


## [Getting started](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/getting-started.html)

- [Step 1: Choose an example project](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-step-choose-example-project.html): Use the Amazon Rekognition Custom Labels console to choose and create an example project.
- [Step 2: Train your model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-step-train-model.html): Use the Amazon Rekognition Custom Labels console to train your example model and view evaluation results.
- [Step 3: Start your model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-step-start-model.html): Use the Amazon Rekognition Custom Labels console to start the model for your example project.
- [Step 4: Analyze an image with your model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-step-get-a-prediction.html): Use the detect_custom_labels AWS CLI command to analyze an image with your example model.
- [Step 5: Stop your model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-step-stop-model.html): Use the Amazon Rekognition Custom Labels console to stop your model.
- [Step 6: Next steps](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-step-next.html): Next steps after using an Amazon Rekognition Custom Labels project.


## [Creating a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/creating-model.html)

- [Creating a project](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/mp-create-project.html): A project manages the model versions, training dataset, and test dataset for a model.

### [Creating datasets](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/creating-datasets.html)

- [Purposing datasets](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-dataset-purpose.html): How you label the training and test datasets in your project determines the type of model that you create.
- [Preparing images](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-prepare-images.html): The images in your training and test dataset contain the objects, scenes, or concepts that you want your model to find.

### [Creating datasets with images](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-dataset.html)

You can start with a project that has a single dataset, or a project that has separate training and test datasets.

- [Importing images from an Amazon S3 bucket](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-dataset-s3.html): The images are imported from an Amazon S3 bucket.
- [Importing images from a local computer](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-dataset-computer.html): The images are loaded directly from your computer.

### [Using a manifest file to import images](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-dataset-ground-truth.html)

You can create a dataset using an Amazon SageMaker AI Ground Truth format manifest file.

- [Labeling images with an Amazon SageMaker AI Ground Truth job](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-dataset-ground-truth-job.html): With Amazon SageMaker AI Ground Truth, you can use workers from either Amazon Mechanical Turk, a vendor company that you choose, or an internal, private workforce along with machine learning that allows you to create a labeled set of images.
- [Creating a manifest file](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-manifest-file.html): You can create a test or training dataset by importing a SageMaker AI Ground Truth format manifest file.
- [Importing image-level labels in manifest files](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-manifest-file-classification.html): To import image-level labels (images labeled with scenes, concepts, or objects that don't require localization information), you add SageMaker AI Ground Truth Classification Job Output format JSON lines to a manifest file.
- [Object localization in manifest files](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-manifest-file-object-detection.html): You can import images labeled with object localization information by adding SageMaker AI Ground Truth Bounding Box Job Output format JSON lines to a manifest file.
- [Validation rules for manifest files](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-manifest-file-validation-rules.html): When you import a manifest file, Amazon Rekognition Custom Labels applies validation rules for limits, syntax, and semantics.

### [Converting other formats to a manifest file](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-converting-to-sm-format.html)

You can use the following information to create Amazon SageMaker AI format manifest files from a variety of source dataset formats.

### [Transforming a COCO dataset into a manifest file format](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-transform-coco.html)

COCO is a format for specifying large-scale object detection, segmentation, and captioning datasets.

- [The COCO dataset format](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-coco-overview.html): A COCO dataset consists of five sections of information that provide information for the entire dataset.
- [Transforming a COCO dataset](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-coco-transform-example.html): Use the following Python example to transform bounding box information from a COCO format dataset into an Amazon Rekognition Custom Labels manifest file.
- [Transforming multi-label Ground Truth manifest files](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-gt-cl-transform.html): This topic shows you how to transform a multi-label Amazon SageMaker AI Ground Truth manifest file to an Amazon Rekognition Custom Labels format manifest file.
- [Creating a manifest file from a CSV file](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/ex-csv-manifest.html): Shows how to create an image classification Amazon Rekognition Custom Labels manifest file from a CSV file.
- [Copying content from an existing dataset](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-dataset-existing-dataset.html): If you've previously created a dataset, you can copy its contents to a new dataset.

### [Labeling images](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-labeling-images.html)

A label identifies an object, scene, concept, or bounding box around an object in an image.

- [Managing labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-labels.html): You can manage labels by using the Amazon Rekognition Custom Labels console.
- [Assigning image-level labels to an image](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-assign-image-level-labels.html): You use image-level labels to train models that classify images into categories.
- [Labeling objects with bounding boxes](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-localize-objects.html): If you want your model to detect the location of objects within an image, you must identify what the object is and where it is in the image.

### [Debugging datasets](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/debugging-datasets.html)

During dataset creation there are two types of error that can occur â terminal errors and non-terminal errors.

- [Debugging terminal dataset errors](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/debugging-datasets-terminal-errors.html): There are two types of terminal errors â file errors that cause dataset creation to fail, and content errors that Amazon Rekognition Custom Labels removes from the dataset.
- [Debugging non-terminal dataset errors](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/debugging-datasets-non-terminal-errors.html): The following are non-terminal errors that can occur during dataset creation or update.
- [Training a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/training-model.html): You can train a model by using the Amazon Rekognition Custom Labels console, or by the Amazon Rekognition Custom Labels API.

### [Debugging model training](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-debugging.html)

You might encounter errors during model training.

- [Understanding the manifest summary](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-debugging-summary.html): The manifest summary contains the following information.
- [Understanding training and testing validation result manifests](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-debugging-scope-json-line.html): During training, Amazon Rekognition Custom Labels creates validation result manifests to hold non-terminal JSON Line errors.
- [Getting the validation results](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-debugging-getting-validation-data.html): The validation results contain error information for and .
- [Fixing training errors](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-debugging-fixing-validation-errors.html): You use the manifest summary to identify and encountered during training.
- [Terminal manifest file errors](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-terminal-errors-reference.html): This topic describes the .
- [Terminal manifest content errors](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-debugging-aggregate-errors.html): This topic describes the reported in the manifest summary.
- [Non-Terminal JSON Line Validation Errors](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-debugging-json-line-errors.html): This topic lists the non-terminal JSON Line validation errors reported by Amazon Rekognition Custom Labels during training.


## [Improving a trained model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/improving-model.html)

- [Metrics for evaluating your model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/im-metrics-use.html): After your model is trained, Amazon Rekognition Custom Labels returns metrics from model testing, which you can use to evaluate the performance of your model.
- [Accessing evaluation metrics (Console)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/im-access-training-results.html): During testing, the model is evaluated for its performance against the test dataset.

### [Accessing evaluation metrics (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/im-metrics-api.html)

The DescribeProjectVersions operation provides access to metrics beyond those provided in the console.

- [Accessing the model summary file](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/im-summary-file-api.html): The summary file contains evaluation results information about the model as a whole and metrics for each label.
- [Interpreting the evaluation manifest snapshot](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/im-evaluation-manifest-snapshot-api.html): The evaluation manifest snapshot contains detailed information about the test results.
- [Accessing the summary file and evaluation manifest snapshot (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/im-access-summary-evaluation-manifest.html): To get training results, you call DescribeProjectVersions.
- [Viewing the confusion matrix for a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/im-confusion-matrix.html): A confusion matrix allows you to see the labels that your model confuses with other labels in your model.
- [Reference: Summary File](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/im-summary-file.html): The training results summary contains metrics you can use to evaluate your model.
- [Improving a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tr-improve-model.html): The performance of machine learning models is largely dependent on factors such as the complexity and variability of your custom labels (the specific objects and scenes that you're interested in), the quality and representative power of the training dataset you provide, and the model frameworks and machine learning methods used to train the model.


## [Running a trained model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/running-model.html)

- [Starting a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/rm-start.html): You can start running an Amazon Rekognition Custom Labels model by using the console or by using the StartProjectVersion operation.
- [Stopping a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/rm-stop.html): You can stop running an Amazon Rekognition Custom Labels model by using the console or by using the StopProjectVersion operation.
- [Reporting duration and inference units](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/rm-model-usage.html): If you trained and started your model after August 2022, you can use the InServiceInferenceUnits Amazon CloudWatch metric to determine how many hours a model has run for and the number of inference units used during those hours.


## [Managing resources](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/managing-resources.html)

### [Managing a project](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/managing-project.html)

Within Amazon Rekognition Custom Labels, you use a project to manage the models that you create for a specific use case.

- [Deleting a project](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/mp-delete-project.html): You can delete a project by using the Amazon Rekognition console or by calling the DeleteProject API.
- [Describing a project (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-describing-project-sdk.html): You can use the DescribeProjects API to get information about your projects.
- [Creating a project with AWS CloudFormation](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/cloudformation.html): Learn about how to create projects for Amazon Rekognition Custom Labels using an AWS CloudFormation template.

### [Managing datasets](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/managing-dataset.html)

A dataset contains the images and assigned labels that you use to train or test a model.

- [Adding a dataset](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-add-dataset.html): You can add a training dataset or a test dataset to an existing project.
- [Adding more images](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-add-images.html): You can add more images to your datasets by using the Amazon Rekognition Custom Labels console or by the calling the UpdateDatasetEntries API.
- [Creating a dataset using an existing dataset (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-dataset-existing-dataset-sdk.html): The following procedure shows you how to create a dataset from an existing dataset by using the CreateDataset operation.
- [Describing a dataset (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-describing-dataset-sdk.html): You can use the DescribeDataset API to get information about a dataset.
- [Listing dataset entries (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-listing-dataset-entries-sdk.html): You can use the ListDatasetEntries API to list the JSON lines for each image in a dataset.
- [Distributing a training dataset (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-distributing-datasets.html): Amazon Rekognition Custom Labels requires a training dataset and a test dataset to train your model.
- [Deleting a dataset](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-delete-dataset.html): You can delete the training and test datasets from a project.

### [Managing a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/managing-model.html)

An Amazon Rekognition Custom Labels model is a mathematical model that predicts the presence of objects, scenes, and concepts in new images.

- [Deleting a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-delete-model.html): You can delete a model by using the Amazon Rekognition Custom Labels console or by using the DeleteProjectVersion API.
- [Tagging a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-tagging-model.html): You can identify, organize, search for, and filter your Amazon Rekognition models by using tags.
- [Describing a model (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-describing-model-sdk.html): You can use the DescribeProjectVersions API to get information about a version of a model.

### [Copying a model (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-copy-model-overview.html)

You can use the CopyProjectVersion operation to copy an Amazon Rekognition Custom Labels model version from a source Amazon Rekognition Custom Labels project to a destination project.

- [Creating a project policy document](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-project-policy-document.html): Rekognition Custom Labels uses a resource-based policy, known as project policy, to manage copy permissions for a model version.
- [Attaching a project policy (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-attach-project-policy.html): You attach a project policy to an Amazon Rekognition Custom Labels project by calling the PutProjectpolicy operation.
- [Copying a model (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-copy-model-sdk.html): You can use the CopyProjectVersion API to copy a model version from a source project to a destination project.
- [Listing project policies (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-list-project-policies.html): You can use the ListProjectPolicies operation to list the project policies that are attached to an Amazon Rekognition Custom Labels project.
- [Deleting a project policy (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-delete-project-policy.title.html): You can use the DeleteProjectPolicy operation to delete a revision of an existing project policy from an Amazon Rekognition Custom Labels project.


## [Custom Labels Examples](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/examples.html)

- [Improving a model with Model feedback](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/ex-feedback.html): Shows how to improve your model's feedback by using human verification.
- [Amazon Rekognition Custom Labels demonstration](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/ex-custom-labels-demo.html): Shows a user interface for Amazon Rekognition Custom Labels that analyzes images from your local computer.
- [Detecting Custom Labels in videos](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/ex-video-extraction.html): Shows how to analyze frames from a video with Amazon Rekognition Custom Labels
- [Analyzing images with an AWS Lambda function](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/ex-lambda.html): Shows how to create an AWS Lambda lambda function that analyzes images with Amazon Rekognition Custom Labels
