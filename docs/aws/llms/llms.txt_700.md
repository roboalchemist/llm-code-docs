# Source: https://docs.aws.amazon.com/rekognition/latest/dg/llms.txt

# Amazon Rekognition Developer Guide

> Developer Guide

- [What is Amazon Rekognition?](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)
- [People pathing](https://docs.aws.amazon.com/rekognition/latest/dg/persons.html)
- [API Reference](https://docs.aws.amazon.com/rekognition/latest/dg/API_Reference.html)
- [Guidelines and quotas](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html)
- [Document history](https://docs.aws.amazon.com/rekognition/latest/dg/document-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/rekognition/latest/dg/glossary.html)

## [How Rekognition works](https://docs.aws.amazon.com/rekognition/latest/dg/how-it-works.html)

- [Understanding Rekognition's types of analysis](https://docs.aws.amazon.com/rekognition/latest/dg/how-it-works-types.html): Describes the types of analysis Amazon Rekognition can do and the kind of media each operation can use.
- [Understanding Rekognition's image and video operations](https://docs.aws.amazon.com/rekognition/latest/dg/how-it-works-operations-intro.html): Describes the difference between image operations and video operations.
- [Non-storage and storage API operations](https://docs.aws.amazon.com/rekognition/latest/dg/how-it-works-storage-non-storage.html): Describes the differences between operations which store data (storage operations) and those that don't (non-storage operations).
- [Understanding model versioning](https://docs.aws.amazon.com/rekognition/latest/dg/face-detection-model.html): Describes how model versioning works in regards to face detection and face search operations.


## [Getting started](https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html)

- [Step 1: Set up an AWS account and create a User](https://docs.aws.amazon.com/rekognition/latest/dg/setting-up.html): Before you use Amazon Rekognition for the first time, you must complete the following tasks:

### [Step 2: Set up the AWS CLI and AWS SDKs](https://docs.aws.amazon.com/rekognition/latest/dg/setup-awscli-sdk.html)

- [Grant programmatic access](https://docs.aws.amazon.com/rekognition/latest/dg/sdk-programmatic-access.html): Grant programmatic access to AWS CLI and AWS SDKs.
- [Working with AWS SDKs](https://docs.aws.amazon.com/rekognition/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [Step 3: Getting started using the AWS CLI and AWS SDK API](https://docs.aws.amazon.com/rekognition/latest/dg/get-started-exercise.html): Describes how to begin using the AWS CLI and AWS SDK API to analyze images and video.

### [Step 4: Getting started using the console](https://docs.aws.amazon.com/rekognition/latest/dg/getting-started-console.html)

Getting started exercises that use the Amazon Rekognition console.

- [Exercise 1: Detect objects and scenes (console)](https://docs.aws.amazon.com/rekognition/latest/dg/detect-labels-console.html): This section shows how, at a very high level, Amazon Rekognition's objects and scenes detection capability works.
- [Exercise 2: Analyze faces (console)](https://docs.aws.amazon.com/rekognition/latest/dg/detect-faces-console.html): This section shows you how to use the Amazon Rekognition console to detect faces and analyze facial attributes in an image.
- [Exercise 3: Compare faces (console)](https://docs.aws.amazon.com/rekognition/latest/dg/compare-faces-console.html): This section shows you how to use the Amazon Rekognition console to compare faces within a set of images with multiple faces in them.
- [Exercise 4: See aggregated metrics (console)](https://docs.aws.amazon.com/rekognition/latest/dg/aggregated-metrics.html): The Amazon Rekognition metrics pane shows activity graphs for an aggregate of individual Rekognition metrics over a specified period of time.


## [Working with images and videos](https://docs.aws.amazon.com/rekognition/latest/dg/programming.html)

### [Working with images](https://docs.aws.amazon.com/rekognition/latest/dg/images.html)

Overview of Amazon Rekognition Image image analysis.

- [Image specifications](https://docs.aws.amazon.com/rekognition/latest/dg/images-information.html): Amazon Rekognition Image operations can analyze images in .jpg or .png format.
- [Analyzing images in an Amazon S3 bucket](https://docs.aws.amazon.com/rekognition/latest/dg/images-s3.html): Amazon Rekognition Image can analyze images that are stored in an Amazon S3 bucket or images that are supplied as image bytes.

### [Using a local file system](https://docs.aws.amazon.com/rekognition/latest/dg/images-bytes.html)

Amazon Rekognition Image operations can analyze images that are supplied as image bytes or images stored in an Amazon S3 bucket.

- [Using JavaScript](https://docs.aws.amazon.com/rekognition/latest/dg/image-bytes-javascript.html): The following JavaScript webpage example allows a user to choose an image and view the estimated ages of faces that are detected in the image.
- [Displaying bounding boxes](https://docs.aws.amazon.com/rekognition/latest/dg/images-displaying-bounding-boxes.html): Amazon Rekognition Image operations can return bounding boxes coordinates for items that are detected in images.
- [Getting image orientation and bounding box coordinates](https://docs.aws.amazon.com/rekognition/latest/dg/images-orientation.html): Applications that use Amazon Rekognition Image commonly need to display the images that are detected by Amazon Rekognition Image operations and the boxes around detected faces.

### [Working with stored video analysis operations](https://docs.aws.amazon.com/rekognition/latest/dg/video.html)

Overview of Amazon Rekognition Video analysis.

- [Calling Amazon Rekognition Video operations](https://docs.aws.amazon.com/rekognition/latest/dg/api-video.html): Amazon Rekognition Video is an asynchronous API that you can use to analyze videos that are stored in an Amazon Simple Storage Service (Amazon S3) bucket.
- [Configuring Amazon Rekognition Video](https://docs.aws.amazon.com/rekognition/latest/dg/api-video-roles.html): To use the Amazon Rekognition Video API with stored videos, you have to configure the user and an IAM service role to access your Amazon SNS topics.
- [Analyzing a stored video (SDK)](https://docs.aws.amazon.com/rekognition/latest/dg/video-analyzing-with-sqs.html): This procedure shows you how to detect labels in a video by using Amazon Rekognition Video label detection operations, a video stored in an Amazon S3 bucket, and an Amazon SNS topic.
- [Analyzing a video (AWS CLI)](https://docs.aws.amazon.com/rekognition/latest/dg/video-cli-commands.html): You can use the AWS Command Line Interface (AWS CLI) to call Amazon Rekognition Video operations.
- [Reference: Video analysis results notification](https://docs.aws.amazon.com/rekognition/latest/dg/video-notification-payload.html): Amazon Rekognition publishes the results of an Amazon Rekognition Video analysis request, including completion status, to an Amazon Simple Notification Service (Amazon SNS) topic.
- [Troubleshooting Amazon Rekognition Video](https://docs.aws.amazon.com/rekognition/latest/dg/video-troubleshooting.html): The following covers troubleshooting information for working with Amazon Rekognition Video and stored videos.

### [Working with streaming video events](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html)

Overview of Amazon Rekognition streaming video analysis.

- [Add tags to a new stream processor](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video-tagging-stream-processor.html): You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags.
- [Add tags to an existing stream processor](https://docs.aws.amazon.com/rekognition/latest/dg/add-tag-existing-stream-processor.html): You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags.
- [List tags in a stream processor](https://docs.aws.amazon.com/rekognition/latest/dg/list-tags-stream-processor.html): You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags.
- [Delete tags from a stream processor](https://docs.aws.amazon.com/rekognition/latest/dg/delete-tag-stream-processor.html): You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags.
- [Error handling](https://docs.aws.amazon.com/rekognition/latest/dg/error-handling.html): Describes how to handle client and server errors returned by Amazon DynamoDB operations.
- [Using Amazon Rekognition with FedRAMP](https://docs.aws.amazon.com/rekognition/latest/dg/fedramp.html): Describes how to set a FIPS endpoint in Amazon Rekognition.


## [Best practices for sensors, input images, and videos](https://docs.aws.amazon.com/rekognition/latest/dg/best-practices.html)

- [Amazon Rekognition Image operation latency](https://docs.aws.amazon.com/rekognition/latest/dg/operation-latency.html): To ensure the lowest possible latency for Amazon Rekognition Image operations, consider the following:
- [Recommendations for facial comparison input images](https://docs.aws.amazon.com/rekognition/latest/dg/recommendations-facial-input-images.html): The models used for face comparison operations are designed to work for a wide variety of poses, facial expressions, age ranges, rotations, lighting conditions, and sizes.
- [Recomendations for searching faces in a collection](https://docs.aws.amazon.com/rekognition/latest/dg/recommendations-facial-input-images-search.html)
- [Recommendations for camera setup (image and video)](https://docs.aws.amazon.com/rekognition/latest/dg/recommendations-camera-image-video.html): The following recommendations are in addition to .
- [Recommendations for camera setup (stored and streaming video)](https://docs.aws.amazon.com/rekognition/latest/dg/recommendations-camera-stored-streaming-video.html): The following recommendations are in addition to .
- [Recommendations for camera setup (streaming video)](https://docs.aws.amazon.com/rekognition/latest/dg/recommendations-camera-streaming-video.html)
- [Recommendations for Usage of Face Liveness](https://docs.aws.amazon.com/rekognition/latest/dg/recommendations-liveness.html): We recommend the following best practices when using Rekognition Face Liveness:


## [Detecting objects and concepts](https://docs.aws.amazon.com/rekognition/latest/dg/labels.html)

- [Detecting labels in an image](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html): You can use the DetectLabels operation to detect labels (objects and concepts) in an image and retrieve information about an imageâs properties.
- [Detecting labels in a video](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detecting-labels-video.html): Amazon Rekognition Video can detect labels (objects and concepts), and the time a label is detected, in a video.

### [Detecting labels in streaming video events](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video-detect-labels.html)

You can use Amazon Rekognition Video to detect labels in streaming video.

- [Setting up your Amazon Rekognition Video and Amazon Kinesis resources](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-labels-setting-up.html): The following procedures describe the steps that you take to provision the Kinesis video stream and other resources that are used to detect labels in a streaming video.
- [Calling label detection operations for streaming video events](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-labels-detection.html): Explains how to call the label or object detection operations on streaming video media.
- [Detecting custom labels](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detecting-custom-labels.html): Amazon Rekognition Custom Labels can identify the objects and scenes in images that are specific to your business needs, such as logos or engineering machine parts.


## [Detecting and analyzing faces](https://docs.aws.amazon.com/rekognition/latest/dg/faces.html)

- [Overview of face detection and face comparison](https://docs.aws.amazon.com/rekognition/latest/dg/face-feature-differences.html): Amazon Rekognition provides users access to two primary machine learning applications for images containing faces: face detection and face comparison.
- [Guidelines on face attributes](https://docs.aws.amazon.com/rekognition/latest/dg/guidance-face-attributes.html): Here are specifics regarding how Amazon Rekognition processes and returns face attributes.
- [Detecting faces in an image](https://docs.aws.amazon.com/rekognition/latest/dg/faces-detect-images.html): Amazon Rekognition Image provides the DetectFaces operation that looks for key facial features such as eyes, nose, and mouth to detect faces in an input image.
- [Comparing faces in images](https://docs.aws.amazon.com/rekognition/latest/dg/faces-comparefaces.html): With Rekognition you can compare faces between two images using the CompareFaces operation.
- [Detecting faces in a stored video](https://docs.aws.amazon.com/rekognition/latest/dg/faces-sqs-video.html): Amazon Rekognition Video can detect faces in videos that are stored in an Amazon S3 bucket and provide information such as:


## [Searching faces in a collection](https://docs.aws.amazon.com/rekognition/latest/dg/collections.html)

- [Managing face collections, faces, and users](https://docs.aws.amazon.com/rekognition/latest/dg/managing-face-collections.html): Describes how to manage faces, users, and collections.
- [Using similarity thresholds for associating and matching faces](https://docs.aws.amazon.com/rekognition/latest/dg/thresholds-collections.html): Describes how to use and calculate similarity thresholds for collection operations.
- [Guidance for indexing faces in common scenarios](https://docs.aws.amazon.com/rekognition/latest/dg/guidance-index-faces.html): Describes how to use IndexFaces to add faces to a collection in common scenarios
- [Searching for faces and users within a collection](https://docs.aws.amazon.com/rekognition/latest/dg/collections-search-faces.html): Describes how to use IndexFaces to add faces to a collection in common scenarios
- [Use cases that involve public safety](https://docs.aws.amazon.com/rekognition/latest/dg/considerations-public-safety-use-cases.html): In addition to the recommendations listed in and , you should use the following best practices when deploying face detection and comparison systems in use cases that involve public safety.
- [Creating a collection](https://docs.aws.amazon.com/rekognition/latest/dg/create-collection-procedure.html): You can use the CreateCollection operation to create a collection.
- [Tagging collections](https://docs.aws.amazon.com/rekognition/latest/dg/tag-collections.html): You can identify, organize, search for, and filter Amazon Rekognition collections by using tags.
- [Listing collections](https://docs.aws.amazon.com/rekognition/latest/dg/list-collection-procedure.html): You can use the ListCollections operation to list the collections in the region that you are using.
- [Describing a collection](https://docs.aws.amazon.com/rekognition/latest/dg/describe-collection-procedure.html): You can use the DescribeCollection operation to get the following information about a collection:
- [Deleting a collection](https://docs.aws.amazon.com/rekognition/latest/dg/delete-collection-procedure.html): You can use the DeleteCollection operation to delete a collection.
- [Adding faces to a collection](https://docs.aws.amazon.com/rekognition/latest/dg/add-faces-to-collection-procedure.html): You can use the IndexFaces operation to detect faces in an image and add them to a collection.
- [Listing faces and associated users in a collection](https://docs.aws.amazon.com/rekognition/latest/dg/list-faces-in-collection-procedure.html): You can use the ListFaces operation to list faces and their associated users in a collection.
- [Deleting faces from a collection](https://docs.aws.amazon.com/rekognition/latest/dg/delete-faces-procedure.html): You can use the DeleteFaces operation to delete faces from a collection.
- [Creating a user](https://docs.aws.amazon.com/rekognition/latest/dg/create-user.html): You can use the CreateUser operation to create a new user in a collection using a unique user ID you provide.
- [Deleting a user](https://docs.aws.amazon.com/rekognition/latest/dg/delete-user.html): You can use the DeleteUser operation to delete a user from a collection, based on the provided UserID.
- [Associating faces to a user](https://docs.aws.amazon.com/rekognition/latest/dg/associate-faces.html): You can use the AssociateFaces operation to associate multiple individual faces with a single user.
- [Disassociating faces from a user](https://docs.aws.amazon.com/rekognition/latest/dg/disassociate-faces.html): You can use the DisassociateFaces operation to remove the association between a user ID and a face ID.
- [Listing users in a collection](https://docs.aws.amazon.com/rekognition/latest/dg/list-users.html): You can use the ListUsers operation to list UserIds and the UserStatus.
- [Searching for a face (face ID)](https://docs.aws.amazon.com/rekognition/latest/dg/search-face-with-id-procedure.html): You can use the SearchFaces operation to search for users in a collection that match the largest face in a supplied image.
- [Searching for a face (image)](https://docs.aws.amazon.com/rekognition/latest/dg/search-face-with-image-procedure.html): You can use the SearchFacesByImage operation to search for faces in a collection that match the largest face in a supplied image.
- [Searching for users (face ID/ user ID)](https://docs.aws.amazon.com/rekognition/latest/dg/search-users.html): You can use the SearchUsers operation to to search for users in a specified collection that match a supplied face ID or user ID.
- [Searching for users (image)](https://docs.aws.amazon.com/rekognition/latest/dg/search-users-by-image.html): SearchUsersByImagesearches the specified CollectionID for users in a collection that match the largest face detected in a supplied image.
- [Searching stored videos for faces](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-person-search-videos.html): You can search a collection for faces that match faces of people who are detected in a stored video or a streaming video.

### [Searching faces in a collection in streaming video](https://docs.aws.amazon.com/rekognition/latest/dg/collections-streaming.html)

Overview of Amazon Rekognition face search in streaming video.

### [Setting up your Amazon Rekognition Video and Amazon Kinesis resources](https://docs.aws.amazon.com/rekognition/latest/dg/setting-up-your-amazon-rekognition-streaming-video-resources.html)

The following procedures describe the steps you take to provision the Kinesis video stream and other resources that are used to recognize faces in a streaming video.

- [Giving Amazon Rekognition Video access to resources](https://docs.aws.amazon.com/rekognition/latest/dg/api-streaming-video-roles.html): You use an AWS Identity and Access Management (IAM) service role to give Amazon Rekognition Video read access to Kinesis video streams.

### [Searching faces in a streaming video](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-video-stream-processor-search-faces.html)

Amazon Rekognition Video can search faces in a collection that match faces that are detected in a streaming video.

- [Reading analysis results](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video-kinesis-output.html): You can use the Amazon Kinesis Data Streams Client Library to consume analysis results that are sent to the Amazon Kinesis Data Streams output stream.
- [Displaying Rekognition results with Kinesis Video Streams locally](https://docs.aws.amazon.com/rekognition/latest/dg/displaying-rekognition-results-locally.html): You can see the results of Amazon Rekognition Video displayed in your feed from Amazon Kinesis Video Streams using the Amazon Kinesis Video Streams Parser Libraryâs example tests provided at KinesisVideo - Rekognition Examples.

### [Understanding the Kinesis face recognition JSON frame record](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video-kinesis-output-reference.html)

Amazon Rekognition Video can recognize faces in a streaming video.

- [StreamProcessorInformation](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video-kinesis-output-reference-streamprocessorinformation.html): Status information about the stream processor.
- [Streaming using a GStreamer plugin](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-using-gstreamer-plugin.html): Amazon Rekognition Video can analyze a live streaming video from a device camera.
- [Troubleshooting streaming video](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video-troubleshooting.html): This topic provides troubleshooting information for using Amazon Rekognition Video with streaming videos.


## [Detecting personal protective equipment](https://docs.aws.amazon.com/rekognition/latest/dg/ppe-detection.html)

- [Understanding the PPE detection API](https://docs.aws.amazon.com/rekognition/latest/dg/ppe-request-response.html): The following information describes the DetectProtectiveEquipment API.
- [Detecting PPE in an image](https://docs.aws.amazon.com/rekognition/latest/dg/ppe-procedure-image.html): To detect Personal Protective Equipment (PPE) on persons in an image, use the DetectProtectiveEquipment non-storage API operation.
- [Example: bounding boxes and face covers](https://docs.aws.amazon.com/rekognition/latest/dg/ppe-example-image-bounding-box.html): The following examples shows you how to draw bounding boxes around face covers detected on persons.


## [Recognizing celebrities](https://docs.aws.amazon.com/rekognition/latest/dg/celebrities.html)

- [Celebrity recognition compared to face search](https://docs.aws.amazon.com/rekognition/latest/dg/celebrity-recognition-vs-face-search.html): Amazon Rekognition offers both celebrity recognition and face recognition functionality.
- [Recognizing celebrities in an image](https://docs.aws.amazon.com/rekognition/latest/dg/celebrities-procedure-image.html): To recognize celebrities within images and get additional information about recognized celebrities, use the RecognizeCelebrities non-storage API operation.
- [Recognizing celebrities in a stored video](https://docs.aws.amazon.com/rekognition/latest/dg/celebrities-video-sqs.html): Amazon Rekognition Video celebrity recognition in stored videos is an asynchronous operation.
- [Getting celebrity information](https://docs.aws.amazon.com/rekognition/latest/dg/get-celebrity-info-procedure.html): In these procedures, you get celebrity information by using the getCelebrityInfo API operation.


## [Moderating content](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html)

- [Using the image and video moderation APIs](https://docs.aws.amazon.com/rekognition/latest/dg/moderation-api.html): In the Amazon Rekognition Image API, you can detect inappropriate, unwanted, or offensive content synchronously using DetectModerationLabels and asynchronously using StartMediaAnalysisJob and GetMediaAnalysisJob operations.

### [Testing Content Moderation version 7 and transforming the API response](https://docs.aws.amazon.com/rekognition/latest/dg/moderation-response-transform.html)

Rekognition updated the machine learning model for the image video components of Content Moderation label detection feature from version 6.1 to 7.

- [AWS SDK and Usage Guide for Content Moderation version 7](https://docs.aws.amazon.com/rekognition/latest/dg/moderation-labels-update-sdk.html): Download the SDK that corresponds with your chosen development language, and consult the appropriate user guide.
- [Detecting inappropriate images](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-moderate-images.html): You can use the DetectModerationLabels operation to determine if an image contains inappropriate or offensive content.
- [Detecting inappropriate stored videos](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-moderate-videos.html): Amazon Rekognition Video inappropriate or offensive content detection in stored videos is an asynchronous operation.

### [Enhancing accuracy with Custom Moderation](https://docs.aws.amazon.com/rekognition/latest/dg/moderation-custom-moderation.html)

Amazon Rekognitionâs DetectModerationLabels API lets you detect content that is inappropriate, unwanted, or offensive.

### [Creating and using adapters](https://docs.aws.amazon.com/rekognition/latest/dg/creating-and-using-adapters.html)

Adapters are modular components that can be added to the existing Rekognition deep learning model, extending its capabilities for the tasks itâs trained on.

- [Bulk analysis and verification](https://docs.aws.amazon.com/rekognition/latest/dg/adapters-bulk-analysis.html): With this approach, you upload a large number of images you want to use as training data and then use Rekognition to get predictions for these images, which automatically assigns labels to them.
- [Manual annotation](https://docs.aws.amazon.com/rekognition/latest/dg/adapters-manual-annotation.html): With this approach, you create your training data by uploading and annotating images manually.
- [Preparing your datasets](https://docs.aws.amazon.com/rekognition/latest/dg/preparing-datasets-adapters.html): Creating an adapter requires you to provide Rekognition with two datasets, a training dataset and a testing dataset.

### [Managing adapters with the AWS CLI and SDKs](https://docs.aws.amazon.com/rekognition/latest/dg/managing-adapters.html)

Rekognition lets you make use of multiple features that leverage pre-trained computer vision models.

- [Creating a project](https://docs.aws.amazon.com/rekognition/latest/dg/managing-adapters-create-project.html): With the CreateProject operation you can create a project that will hold an adapter for Rekognitionâs label detection operations.
- [Describing projects](https://docs.aws.amazon.com/rekognition/latest/dg/managing-adapters-describe-projects.html): You can use the DescribeProjects API to get information about your projects, including information about all the adapters associated with a project.
- [Deleting a project](https://docs.aws.amazon.com/rekognition/latest/dg/managing-adapters-delete-project.html): You can delete a project by using the Rekognition console or by calling the DeleteProject API.
- [Creating a project version](https://docs.aws.amazon.com/rekognition/latest/dg/managing-adapters-create-project-version.html): You can train an adapter for deployment by using the CreateProjectVersion operation.
- [Describing a project version](https://docs.aws.amazon.com/rekognition/latest/dg/managing-adapters-describe-project.html): You can list and describe adapters associated with a project by using the DescribeProjectVersions operation.
- [Deleting a project version](https://docs.aws.amazon.com/rekognition/latest/dg/managing-adapters-delete-project-version.html): You can delete an Rekognition adapter associated with a project using the DeleteProjectVersion operation.
- [Custom Moderation adapter tutorial](https://docs.aws.amazon.com/rekognition/latest/dg/using-adapters-tutorial.html): This tutorial shows you how to create, train, evaluate, use, and manage adapters using the Rekognition Console.
- [Evaluating and improving your adapter](https://docs.aws.amazon.com/rekognition/latest/dg/using-adapters-evaluating-improving.html): After every round of adapter training, youâll want to review the performance metrics in the Rekognition Console tool to determine how close the adapter is to your desired level of performance.
- [Manifest file formats](https://docs.aws.amazon.com/rekognition/latest/dg/using-adapters-manifest-files.html): The following sections show samples of the manifest file formats for input, output, and evaluation files.
- [Best practices for training adapters](https://docs.aws.amazon.com/rekognition/latest/dg/using-adapters-best-practices.html): It's suggested you abide by the dollowing best practices when creating, training, and using your adapters:
- [Setting up AutoUpdate permissions](https://docs.aws.amazon.com/rekognition/latest/dg/using-adapters-autoupdate.html): Rekognition supports the AutoUpdate feature for custom adapters.
- [AWS Health Dashboard notfication for Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/using-adapters-health-notification.html): Your AWS Health Dashboard provides support for notifications that come from Rekognition.
- [Reviewing inappropriate content with Amazon A2I](https://docs.aws.amazon.com/rekognition/latest/dg/a2i-rekognition.html): Amazon Augmented AI (Amazon A2I) enables you to build the workflows that are required for human review of machine learning predictions.


## [Detecting text](https://docs.aws.amazon.com/rekognition/latest/dg/text-detection.html)

- [Detecting text in an image](https://docs.aws.amazon.com/rekognition/latest/dg/text-detecting-text-procedure.html): You can provide an input image as an image byte array (base64-encoded image bytes), or as an Amazon S3 object.
- [Detecting text in a stored video](https://docs.aws.amazon.com/rekognition/latest/dg/text-detecting-video-procedure.html): Amazon Rekognition Video text detection in stored videos is an asynchronous operation.


## [Detecting video segments](https://docs.aws.amazon.com/rekognition/latest/dg/segments.html)

- [Using the Amazon Rekognition Segment API](https://docs.aws.amazon.com/rekognition/latest/dg/segment-api.html): Amazon Rekognition Video segment detection in stored videos is an Amazon Rekognition Video asynchronous operation.
- [Example: Detecting segments in a stored video](https://docs.aws.amazon.com/rekognition/latest/dg/segment-example.html): The following procedure shows how to detect technical cue segments and shot detection segments in a video stored in an Amazon S3 bucket.


## [Detecting face liveness](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness.html)

- [User-Side Face Liveness Requirements](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-requirements.html): Amazon Rekognition Face Liveness requires the following minimum specifications:
- [Architecture and Sequence Diagrams](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-diagrams.html): The following diagrams detail how Amazon Rekognition Face Liveness operates regarding the feature's architecture and sequence of operations:
- [Prerequisites](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-prerequisites.html): Prerequisites for using Amazon Rekognition Face Liveness include the following:
- [Programming the Amazon Rekognition Face Liveness APIs](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-programming-api.html): To use the Amazon Rekognition Face Liveness API, you must create a backend that carries out the following steps:
- [Calling the Face Liveness APIs](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-calling-apis.html): You can test Amazon Rekognition Face Liveness with any supported AWS SDK , like the AWS Python SDK Boto3 or the AWS SDK for Java.
- [Configuring and Customizing Your Application](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-configure-cutomize-amplify.html)
- [Face Liveness Shared Responsibility Model](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-shared-responsibility-model.html): Information on the Shared Responsibility Model for Amazon Rekognition Face Liveness
- [Face Liveness update guidelines](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-update-guidelines.html): AWS regularly updates Face Liveness AWS SDKs (used in customer backend) and FaceLivenessDetector components of AWS Amplify SDKs (used in client applications) to provide new features, updated APIs, enhanced security, bug fixes, usability improvements, and more.
- [Face Liveness FAQ](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-faq.html): Use the following FAQ items to find answers to commonly asked questions about Rekognition Face Liveness.


## [Bulk analysis](https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis.html)

- [Processing images in bulk](https://docs.aws.amazon.com/rekognition/latest/dg/to-process-images-in-bulk.html): Instructions for starting Amazon Rekognition Bulk Analysis operations.
- [Bulk analysis output manifests](https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis-output-manifests.html): Describes Amazon Rekognition StartMediaAnalysJobs output manifest.
- [Content type](https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis-content-type.html): Describes the content types availabile for use by thhe Amazon Rekognition StartMediaAnalysJobs API.
- [Verifying predictions and training adapters](https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis-pred-verify.html): Describes the prediction verfication and adapter training process.


## [Tutorials](https://docs.aws.amazon.com/rekognition/latest/dg/tutorials.html)

- [Storing Amazon Rekognition Data with Amazon RDS and DynamoDB](https://docs.aws.amazon.com/rekognition/latest/dg/storage-tutorial.html): When using Amazon Rekognitionâs APIs, itâs important to remember that the API operations donât save any of the generated labels.
- [Using Amazon Rekognition and Lambda to tag assets in an Amazon S3 bucket](https://docs.aws.amazon.com/rekognition/latest/dg/images-lambda-s3-tutorial.html): In this tutorial, you create an AWS Lambda function that automatically tags digital assets located in an Amazon S3 bucket.
- [Creating AWS video analyzer applications](https://docs.aws.amazon.com/rekognition/latest/dg/stored-video-tutorial-v2.html): You can create a Java web application that analyzes videos for label detection by using the AWS SDK for Java version 2.
- [Creating an Amazon Rekognition Lambda function](https://docs.aws.amazon.com/rekognition/latest/dg/stored-video-lambda.html): This tutorial shows how to get the results of a video analysis operation for label detection by using a Java Lambda function.
- [Using Amazon Rekognition for Identity Verification](https://docs.aws.amazon.com/rekognition/latest/dg/identity-verification-tutorial.html): Amazon Rekognition provides users with several operations that enable the simple creation of identity verification systems.
- [Using Amazon Rekognition (REK) to detect labels for marketing applications](https://docs.aws.amazon.com/rekognition/latest/dg/label-marketing-tutorial.html): This tutorial guides you through building a sample Python application that could be used to send emails to people, based on on images uploaded to a website.
- [Detecting Labels in an Image Using Lambda and Python](https://docs.aws.amazon.com/rekognition/latest/dg/lambda-s3-tutorial-python.html): AWS Lambda is a compute service that you can use to run code without provisioning or managing servers.


## [Code examples](https://docs.aws.amazon.com/rekognition/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/rekognition/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon Rekognition with AWS SDKs.

- [Hello Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_Hello_section.html): Hello Amazon Rekognition

### [Actions](https://docs.aws.amazon.com/rekognition/latest/dg/service_code_examples_actions.html)

The following code examples show how to use Amazon Rekognition with AWS SDKs.

- [CompareFaces](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_CompareFaces_section.html): Use CompareFaces with an AWS SDK or CLI
- [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_CreateCollection_section.html): Use CreateCollection with an AWS SDK or CLI
- [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_DeleteCollection_section.html): Use DeleteCollection with an AWS SDK or CLI
- [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_DeleteFaces_section.html): Use DeleteFaces with an AWS SDK or CLI
- [DescribeCollection](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_DescribeCollection_section.html): Use DescribeCollection with an AWS SDK or CLI
- [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_DetectFaces_section.html): Use DetectFaces with an AWS SDK or CLI
- [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_DetectLabels_section.html): Use DetectLabels with an AWS SDK or CLI
- [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_DetectModerationLabels_section.html): Use DetectModerationLabels with an AWS SDK or CLI
- [DetectText](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_DetectText_section.html): Use DetectText with an AWS SDK or CLI
- [GetCelebrityInfo](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_GetCelebrityInfo_section.html): Use GetCelebrityInfo with an AWS SDK or CLI
- [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_IndexFaces_section.html): Use IndexFaces with an AWS SDK or CLI
- [ListCollections](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_ListCollections_section.html): Use ListCollections with an AWS SDK or CLI
- [ListFaces](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_ListFaces_section.html): Use ListFaces with an AWS SDK or CLI
- [RecognizeCelebrities](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_RecognizeCelebrities_section.html): Use RecognizeCelebrities with an AWS SDK or CLI
- [SearchFaces](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_SearchFaces_section.html): Use SearchFaces with an AWS SDK or CLI
- [SearchFacesByImage](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_SearchFacesByImage_section.html): Use SearchFacesByImage with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/rekognition/latest/dg/service_code_examples_scenarios.html)

The following code examples show how to use Amazon Rekognition with AWS SDKs.

- [Build a collection and find faces in it](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_Usage_FindFacesInCollection_section.html): Build an Amazon Rekognition collection and find faces in it using an AWS SDK
- [Create a serverless application to manage photos](https://docs.aws.amazon.com/rekognition/latest/dg/example_cross_PAM_section.html): Create a photo asset management application that lets users manage photos using labels
- [Detect PPE in images](https://docs.aws.amazon.com/rekognition/latest/dg/example_cross_RekognitionPhotoAnalyzerPPE_section.html): Detect PPE in images with Amazon Rekognition using an AWS SDK
- [Detect and display elements in images](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_Usage_DetectAndDisplayImage_section.html): Detect and display elements in images with Amazon Rekognition using an AWS SDK
- [Detect faces in an image](https://docs.aws.amazon.com/rekognition/latest/dg/example_cross_DetectFaces_section.html): Detect faces in an image using an AWS SDK
- [Detect information in videos](https://docs.aws.amazon.com/rekognition/latest/dg/example_rekognition_VideoDetection_section.html): Detect information in videos using Amazon Rekognition and the AWS SDK
- [Detect objects in images](https://docs.aws.amazon.com/rekognition/latest/dg/example_cross_RekognitionPhotoAnalyzer_section.html): Detect objects in images with Amazon Rekognition using an AWS SDK
- [Detect people and objects in a video](https://docs.aws.amazon.com/rekognition/latest/dg/example_cross_RekognitionVideoDetection_section.html): Detect people and objects in a video with Amazon Rekognition using an AWS SDK
- [Save EXIF and other image information](https://docs.aws.amazon.com/rekognition/latest/dg/example_cross_DetectLabels_section.html): Save EXIF and other image information using an AWS SDK


## [Security](https://docs.aws.amazon.com/rekognition/latest/dg/security.html)

### [Identity and access management](https://docs.aws.amazon.com/rekognition/latest/dg/security-iam.html)

How to authenticate requests and manage access your Amazon Rekognition resources.

- [How Amazon Rekognition works with IAM](https://docs.aws.amazon.com/rekognition/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Rekognition, you should understand what IAM features are available to use with Amazon Rekognition.
- [AWS managed policies](https://docs.aws.amazon.com/rekognition/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Rekognition and recent changes to those policies.
- [Using the console](https://docs.aws.amazon.com/rekognition/latest/dg/security_iam_id-based-policy-examples-console.html): With the exception of the Amazon Rekognition Custom Labels feature, Amazon Rekognition doesn't require any addition permissions when using the Amazon Rekognition console.
- [Examples of using identity-based policy examples](https://docs.aws.amazon.com/rekognition/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Rekognition resources.
- [Examples of Resource-based policies](https://docs.aws.amazon.com/rekognition/latest/dg/security_iam_resource-based-policy-examples.html): Amazon Rekognition Custom Labels uses resource-based polices, known as project policies, to manage copy permissions for a model version.
- [Troubleshooting](https://docs.aws.amazon.com/rekognition/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Rekognition and IAM.

### [Data protection](https://docs.aws.amazon.com/rekognition/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Rekognition.

- [Data encryption](https://docs.aws.amazon.com/rekognition/latest/dg/security-data-encryption.html): The following information explains where Amazon Rekognition uses data encryption to protect your data.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/rekognition/latest/dg/security-inter-network-privacy.html): An Amazon Virtual Private Cloud (Amazon VPC) endpoint for Amazon Rekognition is a logical entity within a VPC that allows connectivity only to Amazon Rekognition.
- [Using Amazon Rekognition with Amazon VPC endpoints](https://docs.aws.amazon.com/rekognition/latest/dg/vpc.html): If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private connection between your VPC and Amazon Rekognition.
- [Compliance validation](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/rekognition/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Rekognition features for data resiliency.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/rekognition/latest/dg/vulnerability-analysis-and-management.html): Configuration and IT controls are a shared responsibility between AWS and you, our customer.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/rekognition/latest/dg/cross-service-confused-deputy-prevention.html): In AWS, cross-service impersonation can occur when one service (the calling service) calls another service (the called service).
- [Infrastructure security](https://docs.aws.amazon.com/rekognition/latest/dg/infrastructure-security.html): Learn how Amazon Rekognition isolates service traffic.


## [Monitoring](https://docs.aws.amazon.com/rekognition/latest/dg/monitoring-overview.html)

- [Monitoring Rekognition with Amazon CloudWatch](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-monitoring.html): With CloudWatch, you can get metrics for individual Rekognition operations or global Rekognition metrics for your account, You can use metrics to track the health of your Rekognition-based solution and set up alarms to notify you when one or more metrics fall outside a defined threshold.
- [Logging Amazon Rekognition API calls with AWS CloudTrail](https://docs.aws.amazon.com/rekognition/latest/dg/logging-using-cloudtrail.html): Learn about logging Amazon Rekognition with AWS CloudTrail.
