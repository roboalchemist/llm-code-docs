# Source: https://docs.aws.amazon.com/sagemaker/latest/dg/llms.txt

# Amazon SageMaker AI Developer Guide

> Use SageMaker AI to build, train, and host machine learning models in AWS.

- [Nova Forge](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-forge.html)

## [What is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

- [Recommendations for a first-time user of Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/first-time-user.html): Learn about the recommendations for a first-time user of Amazon SageMaker AI.
- [Overview of machine learning with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-mlconcepts.html): Get an overview of machine learning, including a typical machine learning workflow and how to accomplish workflow tasks.
- [SageMaker AI Features](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis-features.html): List of features offered by Amazon SageMaker AI: new features, machine learning environments, and major features.


## [Setting up SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html)

- [Complete Amazon SageMaker AI prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-set-up.html): Sign up for an AWS account, create an admin user, and set up AWS CLI for administrative tasks.
- [Use quick setup](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-quick-start.html): Instructions and configuration information using quick setup onboarding.
- [Use custom setup](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-custom.html): Instructions on how to onboard to domain with customization

### [Domain overview](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html)

A brief overview of Amazon SageMaker AI domain and what it contains.

### [SageMaker AI domain entities](https://docs.aws.amazon.com/sagemaker/latest/dg/sm-domain.html)

Learn about Amazon SageMaker AI domain entities and status values for shared space, UserProfile, domain, and App.

- [Complete prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-prerequisites.html): Get information about prerequisites for using an Amazon SageMaker AI domain.

### [Hide ML tools and apps in the Studio UI](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-ui-customize-tools-apps.html)

Learn how to hide machine learning tools and applications that are displayed in the Amazon SageMaker Studio UI left navigation pane.

- [Hide machine learning tools and applications on a domain level](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-ui-customize-tools-apps-domain.html): Learn how to hide machine learning tools and applications that are displayed in the Amazon SageMaker Studio UI left navigation pane.
- [Hide machine learning tools and applications on a user level](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-ui-customize-tools-apps-user.html): Learn how to hide machine learning tools and applications that are displayed in the Amazon SageMaker Studio UI left navigation pane.

### [Hide instance types and images in the Studio UI](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-ui-customize-instances-images.html)

Learn how to hide Amazon SageMaker AI instance types and images that are displayed in the Amazon SageMaker Studio UI.

- [Hide instance types and images on a domain level](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-ui-customize-instances-images-domain.html): The following shows how to use the console to set rules to hide Amazon SageMaker AI instance types and images from being displayed in the Amazon SageMaker Studio Classic UI on a domain level.
- [Hide instance types and images on a user level](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-ui-customize-instances-images-user.html)

### [Multiple domains overview](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-multiple.html)

Learn about considerations when using multiple Amazon SageMaker AI domains.

- [Automatic tag propagation](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-multiple-tag.html): Automatically tag and manage Amazon SageMaker AI resources.
- [How domain resource display filtering works](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-multiple-filtering.html): Amazon SageMaker AI automatically filters the resources displayed in Studio or Studio Classic based on the Amazon SageMaker AI domain.
- [Backfill domain tags](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-multiple-backfill.html): Backfill Amazon SageMaker AI resource metadata tags with Amazon SageMaker AI domain tags.
- [Isolate domain resources](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-resource-isolation.html): Learn how to isolate resources in an Amazon SageMaker AI domain.
- [Default settings for domains](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-set-defaults.html): Learn how Amazon SageMaker AI default settings are set and how they interact with each other.

### [Custom tag propagation](https://docs.aws.amazon.com/sagemaker/latest/dg/custom-tags.html)

Learn about how custom tag propagation works to tag resources in Amazon SageMaker AI.

- [Add custom tags to resources](https://docs.aws.amazon.com/sagemaker/latest/dg/custom-tags-add.html): Learn about how to activate custom tag propagation and add custom tags to resources in Amazon SageMaker AI.
- [Opt-out of custom tag propagation](https://docs.aws.amazon.com/sagemaker/latest/dg/custom-tags-opt-out.html): Learn about how to opt-out of custom tag propagation in Amazon SageMaker AI.
- [Adding a custom file system](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-custom-file-system.html): Learn how to add your own custom file system to a domain so that your users can attach the volume to spaces that they create.
- [View domain environment details](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-space-environment.html): Learn how to view information about the environment of an Amazon SageMaker AI domain.
- [View domains](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-view.html): Learn how to view a list of your Amazon SageMaker AI domains.
- [Edit domain settings](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-edit.html): Learn how to edit your Amazon SageMaker AI domain.
- [Delete a domain](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-delete-domain.html): Learn how to delete a Amazon SageMaker AI domain using the Amazon SageMaker AI console and the AWS Command Line Interface.

### [Domain user profiles](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile.html)

Learn about Amazon SageMaker AI user profiles and how to manage them.

- [Add user profiles](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile-add.html): Learn how to add user profiles to a Amazon SageMaker AI domain.
- [Remove user profiles](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile-remove.html): Learn how to remove user profiles from a Amazon SageMaker AI domain.
- [View user profiles in a domain](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile-view.html): Learn how to view a list of user profiles in an Amazon SageMaker AI domain.
- [View user profile details](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile-describe.html): Learn how to view the details of a user profile in an Amazon SageMaker AI domain.

### [IAM Identity Center groups in a domain](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-groups.html)

Brief background on AWS IAM Identity Center users and groups and where to look to view, add, and remove them in a Amazon SageMaker AI domain.

- [View groups and users](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-groups-view.html): Instructions on how to view AWS IAM Identity Center groups and users for your Amazon SageMaker AI domain.
- [Add groups and users](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-groups-add.html): Instructions on how to add AWS IAM Identity Center groups and users for your Amazon SageMaker AI domain.
- [Remove groups](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-groups-remove.html): Instructions on how to remove AWS IAM Identity Center groups and users for your Amazon SageMaker AI domain.
- [Understanding spaces and execution roles](https://docs.aws.amazon.com/sagemaker/latest/dg/execution-roles-and-spaces.html): Provide information on which execution roles are associated with which spaces.
- [View SageMaker AI resources in your domain](https://docs.aws.amazon.com/sagemaker/latest/dg/sm-console-domain-resources-view.html): Learn how to view Amazon SageMaker AI resources within your Amazon SageMaker AI domain.
- [Shut down SageMaker AI resources in your domain](https://docs.aws.amazon.com/sagemaker/latest/dg/sm-console-domain-resources-shut-down.html): Learn how to shut down Amazon SageMaker AI resources within your Amazon SageMaker AI domain.
- [Where to shut down resources per SageMaker AI features](https://docs.aws.amazon.com/sagemaker/latest/dg/sm-shut-down-resources-per-feature.html): Reference page for where to shut down Amazon SageMaker AI resources in their respective SageMaker AI services or features.
- [Choose an Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-vpc.html): Information on an Amazon VPC and how to set it up
- [Supported Regions and Quotas](https://docs.aws.amazon.com/sagemaker/latest/dg/regions-quotas.html): This page gives information about the AWS Regions supported by Amazon SageMaker AI and the Amazon Elastic Compute Cloud (Amazon EC2) instance types, as well as quotas for Amazon SageMaker AI resources.


## [Automated ML, no-code, or low-code](https://docs.aws.amazon.com/sagemaker/latest/dg/use-auto-ml.html)

### [SageMaker Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html)

Automatically build, train, tune, and deploy models using Autopilot.

### [Create Regression or Classification Jobs Using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html)

Create a regression or classification Job to explore, pre-process, and train various model candidates on a tabular dataset using the AutoML API.

- [Datasets Format and Problem Types](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html): Autopilot datasets, data types, and formats for tabular data
- [Training Modes and Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html): Learn about training modes and which algorithms work with Autopilot .
- [Metrics and validation](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html): Learn about which metrics and validation techniques are available to measure machine learning model performance.

### [Model deployment and prediction](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-deploy-models.html)

Learn the steps for model deployment, setting up real-time inference, and running inference with batch jobs using Amazon SageMaker Autopilot.

- [Deploy models for real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-deploy-models-realtime.html): Use real-time inferencing to obtain predictions interactively from your model.
- [Run batch inference jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-deploy-models-batch.html): Learn how to make batch inferences (offline inferences) that generate model predictions on a batch of observations.
- [View model details](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-models-details.html): Learn how to view model details like statistics, importances, and hyperparameters for your Autopilot model.
- [View a model performance report](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-insights.html): Learn how to view an Autopilot performance report graphically through a PDF, or view metrics as raw data in a JSON file.

### [Notebooks generated](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-notebook-output.html)

Learn about Amazon SageMaker Autopilot generated notebooks and how these manage AutoML tasks.

- [Data exploration report](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-data-exploration-report.html): Identify problems in your dataset and get recommendations about how to address them.
- [Find and run the candidate definition notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-candidate-generation-notebook.html): Learn to use the candidate definition notebook to select model preprocessing steps, algorithm, and hyperparameter ranges.
- [Configure inference output](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-container-output.html): Configure inference output in containers that Autopilot generates, and learn inference container definitions for regression and classification problem types.

### [Create an Image Classification Job using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-image-classification.html)

Create an AutoML job for image classification using the AutoML API to analyze data and train model candidates.

- [Datasets Format and Objective Metric](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification-data-format-and-metric.html): Autopilot datasets format and objective metric for image classification.
- [Deploy Autopilot Models](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification-deploy-models.html): Learn the steps for model deployment and setting up real-time inference using Amazon SageMaker Autopilot.
- [Explainability Report](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification-explainability-report.html): Autopilot explainability for image classification
- [Model Performance Report](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification-model-performance-report.html): Learn how to access an Autopilot performance report as raw data in a JSON file.

### [Create a Text Classification job using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-text-classification.html)

Create an AutoML job for text classification using the API.

- [Datasets Format and Objective Metric](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-data-format-and-metric.html): Autopilot datasets format and objective metric for text classification.
- [Deploy Autopilot Models for Prediction](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-deploy-models.html): Learn the steps for model deployment and setting up real-time inference using Amazon SageMaker Autopilot.
- [Explainability Report](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-explainability-report.html): Autopilot explainability for text classification
- [Model Performance Report](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-model-performance-report.html): Learn how to access an Autopilot performance report as raw data in a JSON file.

### [Create a time-series forecasting job using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-timeseries-forecasting.html)

Create an AutoML job for time-series forecasting using the API.

- [Datasets format and missing values filling methods](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-data-format.html): Autopilot dataset format and missing values filling methods.
- [National Holiday Calendars](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-timeseries-forecasting-holiday-calendars.html): Use Autopilot national holiday calendars to incorporate national holiday information for more than 250 countries into your Autopilot forecasting model.
- [Objective metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-objective-metric.html): List the objective metrics for time-series forecasting in Autopilot.
- [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-algorithms.html): Learn about the algorithms supported by Autopilot for time-series forecasting.

### [Model deployment and forecasts](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-deploy-models.html)

Learn the steps for setting up real-time or batch forecasts using an Amazon SageMaker Autopilot model.

- [Real-time forecasting](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-realtime.html): Learn how to use real-time forecasting to obtain predictions interactively from your model.
- [Batch forecasting](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-batch.html): Learn how to make batch inferences (offline inferences) that generate forecasts on a batch of observations.
- [Data exploration notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-data-exploration-notebook.html): Get a detailed report of the analysis and pre-processing of your input dataset.
- [Reports generated](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-reports.html): Learn about reports generated by Amazon SageMaker Autopilot.
- [Time-series forecasting resource limits](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-limits.html): Time-series resource limits

### [Create an LLM fine-tuning job using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html)

Create an AutoML job to fine-tune text generation models using the API

- [Supported models](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-models.html): Learn about the list of large language models supported by Autopilot for fine-tuning.
- [Dataset file types and input data format](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-data-format.html): Learn about the supported dataset file types and input data format for fine-tuning text generation models in Autopilot.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-hyperparameters.html): Optimize the learning process of your text generation models with hyperparameters.
- [Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-metrics.html): Learn about the list of scores to assess the performance of text generation models fine-tuned in Autopilot
- [Model deployment and predictions](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-deploy-models.html): Learn the steps for model deployment and real-time text generation using Amazon SageMaker Autopilot API.

### [Create a Regression or Classification Job Using the Studio Classic UI](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment-ui.html)

Create an Autopilot experiment using Amazon SageMaker Studio Classic to analyze data and train model candidates.

- [Configure the default parameters of an Autopilot experiment (for administrators)](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-set-default-parameters-create-experiment.html): Learn how to configure the default parameters of an Autopilot experiment.
- [Example Notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-example-notebooks.html): Example notebooks for Autopilot
- [Videos](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-videos.html): Video tutorials for Amazon SageMaker Autopilot.
- [Quotas](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-quotas.html): Account quotas for Autopilot
- [API reference](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-reference.html): API Reference guide for Amazon SageMaker Autopilot.

### [SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)

Amazon SageMaker JumpStart provides access to the SageMaker public model hub that contains the latest publicly available and proprietary foundation models.

### [Foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html)

Access and try out public and proprietary foundation models to customize and integrate them into your generative AI applications.

- [Available models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-latest.html): Explore the latest foundation models from Amazon SageMaker JumpStart.

### [Foundation model usage](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use.html)

Use JumpStart foundation models through the Amazon SageMaker AI Console, Amazon SageMaker Studio Classic, or directly through the Amazon SageMaker Python SDK.

### [Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-studio-updated.html)

Get started with JumpStart foundation models in Amazon SageMaker Studio.

- [Fine-tune a model in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-studio-updated-fine-tune.html): Get started with fine-tuning JumpStart foundation models in Amazon SageMaker Studio.
- [Deploy a model in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-studio-updated-deploy.html): Deploy JumpStart foundation models in Amazon SageMaker Studio.
- [Evaluate a model in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-studio-updated-evaluate.html): Evaluate JumpStart foundation models in Amazon SageMaker Studio.
- [Use your SageMaker JumpStart Models in Amazon Bedrock](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-studio-updated-register-bedrock.html): You can register the models that you've deployed from Amazon SageMaker JumpStart to Amazon Bedrock.
- [Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-studio.html): Get started with JumpStart foundation models in Amazon SageMaker Studio Classic.

### [SageMaker Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-python-sdk.html)

Get started with JumpStart foundation models using the SageMaker Python SDK.

- [Fine-tune a public model](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-python-sdk-estimator-class.html): Learn how to fine-tune a JumpStart foundation model with only a few lines of code.
- [Deploy a public model](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-python-sdk-model-class.html): Learn how to deploy a JumpStart foundation model with only a few lines of code.
- [Deploy a proprietary model](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-python-sdk-proprietary.html): Get started with proprietary JumpStart foundation models using the SageMaker Python SDK.
- [SageMaker AI Console](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-console.html): Get started with JumpStart foundation models in the Amazon SageMaker AI Console.
- [Licenses](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html): Learn how to select a JumpStart foundation models based on your use case.

### [Model Customization](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize.html)

Customize a foundation model with prompt engineering, retrieval augmented generation (RAG), fine-tuning, or pre-training.

- [Prompt engineering](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-prompt-engineering.html): Use prompt engineering to customize your foundation model.

### [Fine-tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-fine-tuning.html)

Customize a foundation model with fine-tuning.

- [Fine-tune a model using domain adaptation](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-fine-tuning-domain-adaptation.html): Customize a foundation model with domain adaptation fine-tuning.
- [Fine-tune a model with prompt instructions](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-fine-tuning-instruction-based.html): Customize a foundation model with instruction-based fine-tuning.
- [Retrieval Augmented Generation](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html): Customize a foundation model with Retrieval Augmented Generation.
- [Evaluate a Model](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-evaluate.html): Learn how to evaluate a JumpStart foundation model in Studio.
- [Example notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-example-notebooks.html): Learn about available example notebooks for JumpStart foundation models.

### [Access control](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html)

Manage access control to pretrained JumpStart foundation models for your organization with private hubs.

### [Admin guide](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide.html)

Learn about the actions needed to use curated private hubs to manage access control for pretrained JumpStart foundation models for your organization.

- [Create a private model hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-create.html): Learn about how to create curated private hubs to manage access control for pretrained JumpStart foundation models for your organization.
- [Add models to a private hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-add-models.html): Learn about how to add models to curated private hubs to manage access control for pretrained JumpStart foundation models for your organization.
- [Update resources in a private hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-update.html): Learn how to update the metadata of models, notebooks, and model references in your private hub.

### [Cross-account sharing](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-ram.html)

Share curated private hubs to necessary users within your organization.

- [Set up cross-account hub sharing](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-ram-setup.html): Learn how to set up cross-account sharing for curated private hubs for necessary users within your organization.
- [Delete models from a private hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-delete-models.html): Learn about how to delete models from a curated private hub for your organization.
- [Restrict access to JumpStart gated models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-gated-model-access.html): Amazon SageMaker JumpStart provides access to both publicly available and proprietary foundation models.
- [Remove access to the SageMaker Public models hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-remove-public-hub.html): Learn about how to remove user access to the SageMaker Public models hub for your organization.
- [Delete a private hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-delete.html): Learn about how to delete a curated private hub for your organization.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-troubleshooting.html): Learn about how to troubleshoot using a curated private hub to manage access control for pretrained JumpStart foundation models for your organization.

### [User guide](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-user-guide.html)

Learn how to perform common user tasks for curated model hubs.

- [Access curated hub models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-access-hubs.html): Access curated private hubs so that you only browse and use JumpStart foundation models approved within your organization.
- [Fine-tune curated hub models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-fine-tune.html): Learn how to fine-tune a curated hub model.

### [Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-studio-classic.html)

Use JumpStart features that are only available in Amazon SageMaker Studio Classic.

### [Task-Specific Models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-models.html)

Use SageMaker JumpStart pre-trained models for common problem types.

- [Deploy a Model](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-deploy.html): Deploy a SageMaker JumpStart pre-trained model.
- [Fine-Tune a Model](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-fine-tune.html): Fine-tune a SageMaker JumpStart pre-trained model.
- [Share Models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-share-models.html): Share a SageMaker JumpStart pre-trained model.

### [Shared Models and Notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing.html)

Share models and notebooks with collaborators in your organization using Amazon SageMaker JumpStart.

- [Model and notebook sharing](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing-access.html): To share models and notebooks, navigate to the Shared models section in Amazon SageMaker Studio Classic, choose Shared by my organization, and then select the Add dropdown list.
- [Access shared content](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing-access-filter.html): From the Amazon SageMaker Studio Classic UI, you can access shared content and filter what you see.

### [Add a model](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing-add-model.html)

To add a model, choose Shared by my organization, and then select Add model from the Add dropdown list.

- [Add basic information](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing-info.html): Adding a model in JumpStart involves providing some basic information about the model you want to train.
- [Enable training](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing-training.html): When adding a model to share, you can optionally provide a training environment and allow collaborators in your organization to train the shared model.
- [Enable deployment](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing-deployment.html): When adding a model to share, you can optionally provide an inference environment in which collaborators in your organization can deploy the shared model for inference.
- [Add a notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing-notebooks.html): To add a notebook, choose Shared by my organization, and then select Add notebook from the Add dropdown list.

### [Solution Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-solutions.html)

You can use SageMaker JumpStart to launch solutions that set up the infrastructure for common use cases.

- [Launch a Solution](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-solutions-launch.html): Use SageMaker JumpStart to launch a solution for common use cases.
- [SageMaker JumpStart Industry: Financial](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart-industry.html): Use Amazon SageMaker JumpStart Industry: Financial to learn about SageMaker AI features and capabilities through curated one-step solutions and examples for industry-focused ML problems.


## [Machine learning environments](https://docs.aws.amazon.com/sagemaker/latest/dg/machine-learning-environments.html)

### [Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html)

Learn about Amazon SageMaker Studio, the latest web-based experience for running ML workflows with Amazon SageMaker AI.

- [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html): Learn how to launch Amazon SageMaker Studio from the Amazon SageMaker AI console and the AWS Command Line Interface (AWS CLI).
- [Amazon SageMaker Studio UI overview](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-ui.html): Learn the key components of the Amazon SageMaker Studio user interface.

### [Amazon EFS auto-mounting in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-automount.html)

Learn about how Amazon SageMaker Studio automatically mounts Amazon EFS folders for user profiles.

- [Opt out of Amazon EFS auto-mounting](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-automount-optout.html): Learn about how Amazon SageMaker Studio automatically mounts Amazon EFS folders for user profiles.

### [Idle shutdown](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown.html)

Learn about support for idle shutdown of Studio applications in Amazon SageMaker AI.

- [Set up idle shutdown](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown-setup.html): Learn about setting up idle shutdown of Studio applications in Amazon SageMaker AI for domains and user profiles.
- [Update default idle shutdown settings](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown-update.html): Learn about update the default idle shutdown settings for Studio applications in Amazon SageMaker AI for domains and user profiles.
- [Modify your idle shutdown time limit](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown-modify.html): Learn about how to modify the default idle shutdown settings for your Studio applications in Amazon SageMaker AI.
- [Applications supported in Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-apps.html): Learn about the applications that Amazon SageMaker Studio supports.

### [Remote access](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access.html)

You can remotely connect from Visual Studio Code to Amazon SageMaker Studio spaces.

### [Set up remote access](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access-remote-setup.html)

Before users can connect their local Visual Studio Code to Studio spaces, the administrator must configure permissions.

- [Advanced access control](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access-remote-setup-abac.html): Amazon SageMaker AI supports attribute-based access control (ABAC) to achieve fine-grained access control for remote Visual Studio Code connections using ABAC policies.
- [Set up private subnet with no internet access](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access-remote-setup-vpc-subnets-without-internet-access.html): This guide shows you how to connect to Amazon SageMaker Studio spaces from Visual Studio Code when your Amazon SageMaker AI domain runs in private subnets without internet access.
- [Set up auto space filtering](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access-remote-setup-filter.html): Users can filter spaces in the AWS Toolkit for Visual Studio Code explorer to display only relevant spaces.

### [Set up local Visual Studio Code](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access-local-ide-setup.html)

After administrators complete the instructions in , you can connect your local Visual Studio Code to your remote SageMaker spaces.

- [Connect to private subnet with no internet access](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access-local-ide-setup-vpc-no-internet.html): Before connecting Visual Studio Code to Studio spaces in private subnets without internet access, ensure your administrator has .
- [Filter your Studio spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access-local-ide-setup-filter.html): You can use filtering to display only the relevant Amazon SageMaker AI spaces in the AWS Toolkit for Visual Studio Code explorer.

### [Bring your own image (BYOI)](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi.html)

Learn how to bring your own image to Amazon SageMaker AI.

- [Image specifications](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-specs.html): The Dockerfile specifications for bringing your own image to Amazon SageMaker AI.

### [How to BYOI](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-how-to.html)

Learn how to bring your own image to Amazon SageMaker AI.

- [Create a custom image and push to Amazon ECR](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-how-to-prepare-image.html): This page provides instructions on how to create a local Dockerfile, build the container image, and add it to Amazon Elastic Container Registry (Amazon ECR).
- [Attach your custom image to your domain](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-how-to-attach-to-domain.html): This page provides instructions on how to attach your custom image to your domain.
- [Update container configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-how-to-container-configuration.html): This guide explains how to configure your container configuration, used to run your application image container.
- [Launch a custom image in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-how-to-launch.html): Learn how to launch a custom image in Amazon SageMaker Studio.
- [View your custom image details](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-view-images.html): Learn how to view your custom image details in the SageMaker AI image store.

### [Speed up container startup with SOCI](https://docs.aws.amazon.com/sagemaker/latest/dg/soci-indexing.html)

Learn how SOCI indexing enables lazy loading of container images in Amazon SageMaker Studio or Amazon SageMaker Unified Studio to reduce startup times by 30-70% for custom containers.

- [Permissions for SOCI indexing](https://docs.aws.amazon.com/sagemaker/latest/dg/soci-indexing-setup.html): Configure prerequisites and IAM permissions required to create SOCI indexes for custom container images and store them in Amazon ECR.
- [Create SOCI indexes with nerdctl and SOCI CLI example](https://docs.aws.amazon.com/sagemaker/latest/dg/soci-indexing-example-create-indexes.html): Example for creating SOCI indexes with nerdctl and SOCI CLI.
- [Integrate SOCI-indexed images with Studio example](https://docs.aws.amazon.com/sagemaker/latest/dg/soci-indexing-example-integrate-studio.html): Examples for integrating SOCI-indexed custom images Amazon SageMaker Studio.
- [Detach and clean up custom image resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-how-to-detach-from-domain.html): Learn how to detach your custom images and clean up custom image resources.

### [Lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations.html)

Use lifecycle configurations to automate the customization of your applications within Amazon SageMaker Studio.

- [Create and attach lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations-create.html): You can create and attach lifecycle configurations using either the AWS Management Console or the AWS Command Line Interface.

### [Debug lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations-debug.html)

Troubleshoot your lifecycle configurations.

- [Lifecycle configuration timeout](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations-debug-timeout.html): There is a lifecycle configuration timeout limitation of 5 minutes.

### [Amazon SageMaker Studio spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-spaces.html)

Learn about spaces in Amazon SageMaker Studio and how to manage them.

- [Launch spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-spaces-access.html): Learn about launching spaces in Amazon SageMaker Studio.

### [Collaboration with shared spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-space.html)

Learn how to use shared spaces for collaboration between all users in a SageMaker AI domain.

- [Create a shared space](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-space-create.html): Learn how to create a shared space from the Amazon SageMaker AI console, Amazon SageMaker Studio, or the AWS CLI.
- [Get information about shared spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-space-list.html): Access a list of shared spaces in an Amazon SageMaker AI domain, and view details of a shared space from the AWS CLI.
- [Edit a shared space](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-space-edit.html): Learn how to edit the settings of a shared space.
- [Delete a shared space](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-space-delete.html): Learn how to delete a shared space from the Amazon SageMaker AI console or the AWS CLI.

### [Trusted identity propagation](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation.html)

Learn how AWS IAM Identity Center's trusted identity propagation works with Studio, used to manage and audit service access based on user attributes.

- [Architecture and compatibility](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-compatibility.html): Learn how trusted identity propagation integrates IAM Identity Center with Studio and compatible AWS services for enhanced security and auditing.
- [Set up](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-setup.html): Configure trusted identity propagation for Studio with IAM Identity Center authentication for identity-based access control.
- [Audit with CloudTrail](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-auditing.html): Monitor user activities with CloudTrail logs that include specific user identity information for enhanced compliance and security auditing.
- [User background sessions](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-user-background-sessions.html): Configure user background sessions to enable long-running jobs that continue after user logout with trusted identity propagation.

### [Connect with other AWS services](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-connect-other.html)

Connect Studio to AWS services like Amazon S3 Access Grants, Amazon EMR, Redshift Data API, and Lake Formation with identity propagation enabled.

### [Connect to Amazon S3 Access Grants](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-s3-access-grants.html)

Use Amazon S3 Access Grants with Studio to provide identity-based fine-grained access control to Amazon S3 buckets and data locations.

- [Studio JupyterLab notebooks with Amazon S3 Access Grants](https://docs.aws.amazon.com/sagemaker/latest/dg/s3-access-grants-setup.html): Configure IAM permissions and trust policies to enable Amazon S3 Access Grants integration with Studio JupyterLab notebooks.
- [Training and Processing jobs with Amazon S3 Access Grants](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-s3-access-grants-jobs.html): Enable Amazon S3 Access Grants for SageMaker Training and Processing jobs to provide identity-based data access with automatic fallback.
- [Connect to Amazon EMR](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-emr-ec2.html): Connect Studio notebooks to Amazon EMR clusters for distributed computing with identity propagation and audit trails.
- [Connect to EMR Serverless](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-emr-serverless.html): Use EMR Serverless with Studio for Apache Spark and Hive applications with automatic scaling and identity-based access.
- [Connect to Redshift Data API](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-redshift-data-apis.html): Set up Redshift Data API with identity-based security and full audit trails for data science workflows.
- [Connect to Lake Formation and Athena](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-lake-formation-athena.html): Integrate Lake Formation and Athena with Studio for comprehensive data lake access with centralized permissions management.
- [Perform common UI tasks](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-common.html): Learn how to perform common tasks in Amazon SageMaker Studio.
- [NVMe stores with Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-nvme.html): Learn about NVMe stores and using them with Amazon SageMaker Studio applications.

### [Local mode support in Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-local.html)

Learn how local mode support in Amazon SageMaker Studio can create estimators, processors, and pipelines that you deploy to a local environment.

- [Getting started with local mode](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-local-get-started.html): Learn steps needed to start using local mode in Amazon SageMaker Studio.
- [View your instances, applications, and spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-running.html): Learn how to viewyour running instance and space in Amazon SageMaker Studio.
- [Stop and delete your Studio running applications and spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-running-stop.html): Learn how to stop and delete running applications and spaces in Amazon SageMaker Studio.
- [SageMaker Studio image support policy](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-distribution.html): The following page describes the support policy for Amazon SageMaker Distribution Docker images that are available on SageMaker Studio.
- [Amazon SageMaker Studio pricing](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-cost.html): Learn about pricing considerations for Amazon SageMaker Studio.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-troubleshooting.html): Learn how to troubleshoot common problems in Amazon SageMaker Studio.

### [Migration from Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-migrate.html)

Migrate from Amazon SageMaker Studio Classic to the Amazon SageMaker Studio experience.

- [Complete prerequisites to migrate the Studio experience](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-migrate-prereq.html): Learn about the prerequisites needed to migrate from Amazon SageMaker Studio Classic to the Amazon SageMaker Studio experience.
- [Migrate the UI from Studio Classic to Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-migrate-ui.html): Migrate from the Amazon SageMaker Studio Classic UI to the Amazon SageMaker Studio experience.
- [(Optional) Migrate custom images and lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-migrate-lcc.html): Migrate custom images and lifecycle configuration (LCC) scripts to work with Amazon SageMaker Studio.
- [(Optional) Migrate data from Studio Classic to Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-migrate-data.html): Learn how to migrate your data from the storage volume that Studio Classic uses to the storage volume that Studio uses, including multiple approaches.

### [Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)

Amazon SageMaker Studio Classic is an integrated machine learning environment where you can build, train, deploy, and analyze models in the same application.

- [UI Overview](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-ui.html): Learn how to use the Amazon SageMaker Studio Classic user interface.
- [Launch](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html): Learn how to launch an Amazon SageMaker Studio Classic application from either the SageMaker AI console or the AWS CLI.
- [JupyterLab Versioning](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jl.html): Select the JupyterLab version to use for your Amazon SageMaker Studio Classic instance.
- [Use the Launcher](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launcher.html): Learn how to use the Amazon SageMaker Studio Classic Launcher to create notebooks and text files, and to launch terminals and interactive Python shells.

### [Use Notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks.html)

How to use and share Amazon SageMaker Studio Classic notebooks.

- [Compare with Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-comparison.html)
- [Get Started](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-get-started.html)
- [Studio Classic Tour](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-end-to-end.html): Take a tour of Amazon SageMaker Studio Classic with end-to-end examples that highlights its main features.
- [Create or Open a Notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-create-open.html)
- [Use the Toolbar](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-menu.html): Describes the function of each Amazon SageMaker Studio Classic notebook toolbar tool.
- [Install External Libraries](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-add-external.html)
- [Share and Use a Notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-sharing.html)
- [Get Metadata](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-run-and-manage-metadata.html)
- [Get Notebook Differences](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-diff.html)

### [Manage Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-run-and-manage.html)

- [Change the Instance Type](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-run-and-manage-switch-instance-type.html): When you open a new Studio Classic notebook for the first time, you are assigned a default Amazon Elastic Compute Cloud (Amazon EC2) instance type to run the notebook.
- [Change the Image or Kernel](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-run-and-manage-change-image.html)
- [Shut Down Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-run-and-manage-shut-down.html): Learn how to use Amazon SageMaker Studio Classic to shut down Amazon SageMaker AI resources, including notebooks, terminals, kernels, apps, and instances.
- [Usage Metering](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-usage-metering.html)

### [Available Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-resources.html)

- [Instance Types](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html): Learn about the Amazon Elastic Compute Cloud instance types available to use with Studio Classic, including instances that use CPUs and instances that use GPUs.
- [Amazon SageMaker Images](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-images.html): Learn about the Amazon SageMaker images available to use with Studio Classic, including information about images slated for deprecation and the ARN of images.

### [Customize](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-customize.html)

Customize your Amazon SageMaker Studio Classic environment.

### [Custom Images](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html)

- [Custom Image Specifications](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-specs.html): Describes specifications for bringing your own image to Amazon SageMaker AI.
- [Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-prereq.html): Describes prerequisites for bringing your own image to Amazon SageMaker AI.
- [Add a Studio Classic-Compatible Image to ECR](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-sdk-add-container-image.html): Describes how to add a Docker image compatible with Studio Classic to Amazon ECR.
- [Create a SageMaker Image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-create.html)
- [Attach an Image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-attach.html): Describes how to attach a custom Amazon SageMaker image to your domain.
- [Launch a Custom Image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-launch.html)
- [Clean Up Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-cleanup.html): Describes how to clean up resources after bringing a custom image to Studio Classic.

### [Use LCC with Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc.html)

Use lifecycle configurations to automate customization for your Studio Classic environment.

### [Create and Associate a Lifecycle Configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc-create.html)

Learn how to create and associate a lifecycle configuration with Amazon SageMaker Studio Classic with this tutorial series.

- [Create from the AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc-create-cli.html): Create a lifecycle configuration from the AWS CLI to automate customization for your Studio Classic environment.
- [Create from the SageMaker AI Console](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc-create-console.html): Create a lifecycle configuration from the Amazon SageMaker AI console to automate customization for your Studio Classic environment.

### [Set Defaults](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc-defaults.html)

Set a lifecycle configuration as the default for your domain, user profile, or shared space.

- [Set Defaults from the AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc-defaults-cli.html): Set a lifecycle configuration as the default for your domain, user profile, or space from the AWS CLI.
- [Set Defaults from the SageMaker AI Console](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc-defaults-console.html): Set a lifecycle configuration as the default for your domain or user profile from the SageMaker AI console.
- [Debug Lifecycle Configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc-debug.html): Troubleshoot your lifecycle configurations.
- [Update and Detach Lifecycle Configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc-delete.html): Update and detach your lifecycle configurations.

### [Attach Suggested Git Repos](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-git-attach.html)

Learn how to attach and detach Git repo URLs to Amazon SageMaker Studio Classic with this tutorial series.

- [Attach from the AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-git-attach-cli.html): Attach a Git repository URL from the AWS CLI to an Amazon SageMaker AI domain or user profile for use in Amazon SageMaker Studio Classic.
- [Attach from the SageMaker AI Console](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-git-attach-console.html): Attach a Git repository URL from the Amazon SageMaker AI console to clone it in your Studio Classic environment.
- [Detach Git Repos](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-git-detach.html): Learn how to detach Git repo URLs from an Amazon SageMaker AI domain or user profile.

### [Common Tasks](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks.html)

Describes how to perform common tasks in Amazon SageMaker Studio Classic.

- [Upload Files](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-files.html): Describes how to upload files to Amazon SageMaker Studio Classic.
- [Clone a Git Repository](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-git.html)
- [Stop a Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-stop-training-job.html)
- [Use TensorBoard](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tensorboard.html)
- [Use Amazon Q Developer](https://docs.aws.amazon.com/sagemaker/latest/dg/sm-q.html): Generate code recommendations and suggest improvements related to code issues by Amazon Q Developer with Amazon SageMaker Studio Classic.
- [Manage Your Amazon EFS Volume](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-manage-storage.html)
- [Provide Feedback](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-provide-feedback.html)

### [Shut Down and Update](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-update.html)

- [Shut Down and Update](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-update-studio.html)
- [Shut Down and Update Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-update-apps.html)
- [Pricing](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-pricing.html): Describes how you are billed for using Amazon SageMaker Studio Classic.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-troubleshooting.html): Learn to troubleshoot common Amazon SageMaker Studio Classic issues during setup and use.

### [JupyterLab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl.html)

Select the JupyterLab version to use for an Amazon SageMaker Studio instance.

### [JupyterLab user guide](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-user-guide.html)

Get JupyterLab user guidance for running analytics and machine learning workflows using JupyterLab within SageMaker Studio.

- [Create a space](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-user-guide-create-space.html): To get started using JupyterLab, create a space or choose the space that your administrator created for you and open JupyterLab.
- [Configure a space](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-user-guide-configure-space.html): After you create a JupyterLab space, you can configure it to do the following:
- [Customize your environment using a package manager](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-user-guide-customize-package-manager.html): Use pip or conda to customize your environment.
- [Clean up a conda environment](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-clean-up-conda.html): Cleaning up conda environments that youâre not using can help free up disk space and improve performance.
- [Share conda environments](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-create-conda-share-environment.html): You can share conda environments by saving them to an Amazon EFS directory outside of your Amazon EBS volume.
- [Use Amazon Q to Expedite Your Machine Learning Workflows](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-user-guide-use-amazon-q.html): Amazon Q Developer is your AI-powered companion for machine learning development.

### [JupyterLab administrator guide](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-admin-guide.html)

Use the JupyterLab administrator guide to learn about resources in JupyterLab, how to change storage size, and more.

- [Give your users access to spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-admin-guide-permissions.html): Learn how to give users access to private spaces or shared spaces by attaching a permissions policy to their AWS Identity and Access Management (IAM) roles.
- [Change the default storage size for your JupyterLab users](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-admin-guide-storage-size.html): Learn how to change the storage size for your JupyterLab users.

### [Lifecycle configurations with JupyterLab](https://docs.aws.amazon.com/sagemaker/latest/dg/jl-lcc.html)

Use lifecycle configurations to automate customization for your JupyterLab environment.

- [Lifecycle configuration creation](https://docs.aws.amazon.com/sagemaker/latest/dg/jl-lcc-create.html): Create and associate a lifecycle configuration with the AWS CLI or the AWS Management Console, and learn to automate customization for your JupyterLab environment.
- [Debug lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/jl-lcc-debug.html): Troubleshoot your lifecycle configurations.
- [Detach lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/jl-lcc-delete.html): Detach your lifecycle configurations by using the AWS Command Line Interface (AWS CLI).

### [Git repos](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-admin-guide-git-attach.html)

Attach a Git repository URL to a Amazon SageMaker AI domain (domain) or a user profile.

- [Attach a Git repository (AWS CLI)](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-git-attach-cli.html): This section shows how to attach a Git repository (repo) URL using the AWS CLI.
- [Detach Git repo URLs](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-git-detach.html): This section shows how to detach Git repository URLs from an Amazon SageMaker AI domain (domain) or a user profile.
- [Custom images](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-admin-guide-custom-images.html): If you need functionality that is different than what's provided by SageMaker distribution, you can bring your own image with your custom extensions and packages.
- [Update the SageMaker Distribution Image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-update-distribution-image.html)
- [Delete unused resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-admin-guide-clean-up.html): To avoid incurring additional costs running JupyterLab, we recommend deleting unused resources in the following order:
- [Quotas](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-admin-guide-quotas.html): JupyterLab, has quotas for the following:

### [Notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)

Use Amazon SageMaker notebook instances to prepare and process data and to train and deploy machine learning models.

### [Tutorial for building models with Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-console.html)

Build, train, and deploy your first machine learning model in Amazon SageMaker notebook instances.

- [Create an Amazon SageMaker Notebook Instance for the tutorial](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-setup-working-env.html): Get started by creating an Amazon SageMaker Notebook Instance.
- [Create a Jupyter notebook in the SageMaker notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-prepare.html): Create a Jupyter notebook in the SageMaker notebook instance to start scripting for training and deploying your model.
- [Prepare a dataset](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-preprocess-data.html): In this step, you load the Adult Census dataset to your notebook instance using the SHAP (SHapley Additive exPlanations) Library, review the dataset, transform it, and upload it to Amazon S3.
- [Train a Model](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-train-model.html): Train ML models on Amazon SageMaker notebook instances leveraging generic and framework estimators and SageMaker training features.
- [Deploy the Model](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-model-deployment.html): To get predictions, deploy your model to Amazon EC2 using Amazon SageMaker AI.
- [Evaluate the model](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-test-model.html): Now that you have trained and deployed a model using Amazon SageMaker AI, evaluate the model to ensure that it generates accurate predictions on new data.
- [Clean up Amazon SageMaker notebook instance resources](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-cleanup.html): Learn how to clean up resources associated with a Amazon SageMaker notebook instance from the Amazon SageMaker AI console to avoid incurring unnecessary charges.
- [AL2023 instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-al2023.html): Amazon SageMaker notebook instances currently support AL2023 operating systems.
- [AL2 instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-al2.html)

### [JupyterLab versioning](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-jl.html)

Select the JupyterLab version to use for your Amazon SageMaker notebook instance.

- [Create a notebook with your JupyterLab version](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-jl-create.html): Learn steps needed to create a SageMaker notebook instance with a JupyterLab version.
- [View the JupyterLab version of a notebook from the console](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-jl-view.html): Learn steps needed to view the JupyterLab version of a SageMaker notebook instance.
- [Create an Amazon SageMaker notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-create-ws.html): Learn how to create an Amazon SageMaker notebook instance from the SageMaker AI console.
- [Access Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-access-ws.html)
- [Update a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-update.html): After you create a notebook instance, you can update it using the SageMaker AI console and UpdateNotebookInstance API operation.

### [Customize a Notebook Instance using an LCC](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html)

Learn about customization of an Amazon SageMaker notebook instance using a lifecycle configuration script when creating a new notebook instance or starting up an existing one.

- [Create a lifecycle configuration script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config-create.html): Learn the steps needed to create a lifecycle script for use with an Amazon SageMaker notebook instance.
- [External library and kernel installation](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-add-external.html): How to install external libraries and kernels in Amazon SageMaker notebook instances.
- [Notebook Instance Software Updates](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-software-updates.html): Amazon SageMaker AI periodically tests and releases software that is installed on notebook instances.
- [Control an Amazon EMR Spark Instance Using a Notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-lifecycle-config-emr.html)
- [Set the Notebook Kernel](https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-set-kernel.html): Amazon SageMaker AI provides several kernels for Jupyter that provide support for Python 2 and 3, Apache MXNet, TensorFlow, and PySpark.

### [Git Repos](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html)

Associate Git repositories with your Amazon SageMaker notebook instances to enable you to save notebooks beyond the life of your notebook instance and collaborate on notebooks with peers.

### [Add a Git repository to your Amazon SageMaker AI account](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-resource.html)

- [Add a Git repository to your Amazon SageMaker AI account (CLI)](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-resource-cli.html)

### [Create a Notebook Instance with an Associated Git Repository](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-create.html)

- [Create a Notebook Instance with an Associated Git Repository (CLI)](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-create-cli.html)
- [Associate a CodeCommit Repository in a Different AWS Account with a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-cross.html): To associate a CodeCommit repository in a different AWS account with your notebook instance, set up cross-account access for the CodeCommit repository.
- [Use Git Repositories in a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/git-nbi-use.html): When you open a notebook instance that has Git repositories associated with it, it opens in the default repository, which is installed in your notebook instance directly under /home/ec2-user/SageMaker.
- [Notebook Instance Metadata](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-metadata.html): When you create a notebook instance, Amazon SageMaker AI creates a JSON file on the instance at the location /opt/ml/metadata/resource-metadata.json that contains the ResourceName and ResourceArn of the notebook instance.
- [Monitor Jupyter Logs in Amazon CloudWatch Logs](https://docs.aws.amazon.com/sagemaker/latest/dg/jupyter-logs.html): Jupyter logs include important information such as events, metrics, and health information that provide actionable insights when running Amazon SageMaker notebooks.

### [Studio Lab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab.html)

Describes Amazon SageMaker Studio Lab and how to use it.

- [Studio Lab components overview](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-overview.html): Gives an overview of Amazon SageMaker Studio Lab structure and components.
- [Onboard to Studio Lab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-onboard.html): Describes the steps for onboarding to Amazon SageMaker Studio Lab.
- [Manage your account](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-manage-account.html): Describes how to change your Amazon SageMaker Studio Lab password and delete your account.
- [Launch Studio Lab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-manage-runtime.html): Describes how to launch the Amazon SageMaker Studio Lab project runtime, stop it, and switch your compute type.
- [Use Studio Lab starter assets](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-integrated-resources.html): Describes the starter assets that come with Amazon SageMaker Studio Lab, goes over cloning the notebooks, and shows you how to use them.
- [Studio Lab pre-installed environments](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-environments.html): Describes the Amazon SageMaker Studio Lab provided environments.

### [Use the Studio Lab project runtime](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use.html)

Gives information about how to use the Amazon SageMaker Studio Lab project runtime.

- [Studio Lab UI overview](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-ui.html): Provides an overview of the Amazon SageMaker Studio Lab user interface.
- [Create or open a notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-create.html): Describes how to create and open a notebook in Amazon SageMaker Studio Lab.
- [Use the toolbar](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-menu.html): Describes the function of each Amazon SageMaker Studio Lab notebook toolbar tool.
- [Manage your environment](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-manage.html): Describes the Amazon SageMaker Studio Lab pre-installed environment and how to customize the default environment.
- [Use external resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-external.html): Describes how to integrate external resources in Amazon SageMaker Studio Lab, including GitHub and Amazon S3.
- [Get notebook differences](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-diff.html): Shows how to view the difference between your current Amazon SageMaker Studio Lab notebook and the last checkpoint or Git commit.
- [Export a Studio Lab environment to Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-migrate.html): Learn how to export an Amazon SageMaker Studio Lab environment and files for use with Amazon SageMaker Studio Classic.
- [Shut down Studio Lab resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-shutdown.html): Instructions on how to shut down your Amazon SageMaker Studio Lab resources.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-troubleshooting.html): Describes common errors when using Amazon SageMaker Studio Lab and how to resolve them.

### [Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)

Learn about Amazon SageMaker Canvas, a service that you can use to get machine learning predictions and build models without using any code.

- [Getting started](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-getting-started.html): Get started with using SageMaker Canvas.
- [Tutorial: Build a machine learning workflow in Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-end-to-end-machine-learning-workflow.html): Complete a tutorial that walks you through preparing data, training a model, evaluating the model, and deploying the model in Amazon SageMaker Canvas.

### [Amazon SageMaker Canvas setup and permissions management (for IT administrators)](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-setting-up.html)

Help your users set up SageMaker Canvas and manage updates for that service.

- [Grant Your Users Permissions to Upload Local Files](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-set-up-local-upload.html): Grant your users permissions to upload files from their local machines into SageMaker Canvas.
- [Set Up SageMaker Canvas for Your Users](https://docs.aws.amazon.com/sagemaker/latest/dg/setting-up-canvas-sso.html): Set up Okta SSO for your Amazon SageMaker Canvas users.
- [Configure your Amazon S3 storage](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-storage-configuration.html): Configure the Amazon S3 storage location for your Canvas application data.
- [Grant permissions for cross-account Amazon S3 storage](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-permissions-cross-account.html): Grant your user permissions to use an Amazon S3 bucket in another account for storing Canvas application data.
- [Grant Large Data Permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-large-data-permissions.html): Grant users permissions to process large datasets across the machine learning lifecycle using SageMaker Canvas.
- [Encrypt Your SageMaker Canvas Data with AWS KMS](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-kms.html): Encrypt your data in the SageMaker Canvas application, and grant your users permissions to import encrypted datasets.
- [Store SageMaker Canvas application data in your own SageMaker AI space](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-spaces-setup.html): Use a custom SageMaker AI space location to store your SageMaker Canvas application data.
- [Grant Your Users Permissions to Build Custom Image and Text Prediction Models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-set-up-cv-nlp.html): To grant your users permissions to build the custom image and text prediction model types, you can optionally configure these permissions for your IAM role.
- [Grant Users Permissions to Use Amazon Bedrock and Generative AI Features in Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fine-tuning-permissions.html): Grant your users the permissions necessary to access Amazon Bedrock models, fine tune Amazon Bedrock models, and use generative AI features in SageMaker Canvas.
- [Update SageMaker Canvas for Your Users](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-update.html): Use the Amazon SageMaker AI console to update Amazon SageMaker Canvas for your users.
- [Request a Quota Increase](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-requesting-quota-increases.html): Increase the amount of AWS resources for your Amazon SageMaker Canvas users.
- [Grant Users Permissions to Import Amazon Redshift Data](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-redshift-permissions.html): Grant your users permissions to import datasets from Amazon Redshift.
- [Grant Your Users Permissions to Send Predictions to Quick](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-quicksight-permissions.html): Grant your SageMaker Canvas users permissions to send their batch predictions to Quick to build predictive data dashboards.

### [Applications management](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-apps.html)

Manage your SageMaker Canvas applications.

- [Check for active applications](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-apps-active.html): Learn how to check for active SageMaker Canvas applications.
- [Delete an application](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-apps-delete.html): Learn how to delete active SageMaker Canvas applications.
- [Relaunch an application](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-apps-relaunch.html): Learn how to relaunch for active SageMaker Canvas applications.
- [Configure Amazon SageMaker Canvas in a VPC without internet access](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-vpc.html): Run Amazon SageMaker Canvas in an Amazon Virtual Private Cloud.
- [Set up connections to data sources with OAuth](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-setting-up-oauth.html): Connect to your data stored in Snowflake and Salesforce Data Cloud using OAuth so that you don't have to share passwords.

### [Generative AI assistance using Q Developer](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-q.html)

Use Amazon Q Developer for conversational generative AI assistance while you solve business problems and build machine learning models.

- [Logging Q Developer conversations with AWS CloudTrail](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-q-cloudtrail.html): Learn about how to view AWS CloudTrail logs for your conversations with Q Developer in SageMaker Canvas, which go through the SageMaker AI Data Science Assistant service.

### [Data import](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-importing-data.html)

You can import data from your local machine, various AWS data sources, or an outside data source.

- [Create a dataset](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-import-dataset.html): Learn how to create an Amazon SageMaker Canvas dataset for training models.
- [Update a dataset](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-update-dataset.html): Update your datasets and create new dataset versions in SageMaker Canvas.
- [Configure automatic updates for a dataset](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-update-dataset-auto.html): After importing your initial dataset into Amazon SageMaker Canvas, you might have additional data that you want to add to your dataset.
- [View your automatic dataset update jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-update-dataset-auto-view.html): Learn how to view your automatic dataset update jobs in Amazon SageMaker Canvas.
- [Edit your automatic dataset update configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-update-dataset-auto-edit.html): Learn how to edit your automatic dataset update configurations in Amazon SageMaker Canvas.
- [Connect to data sources](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-connecting-external.html): Connect to data sources and import data into Amazon SageMaker Canvas
- [Sample datasets in Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-sample-datasets.html): Use the sample datasets and their associated tutorials to quickly get started in SageMaker Canvas.
- [Re-import a deleted sample dataset](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-sample-datasets-reimport.html): Learn how to re-import a sample dataset into SageMaker Canvas that you previously deleted.

### [Data preparation](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-prep.html)

Use Amazon SageMaker Data Wrangler in SageMaker Canvas to import, prepare, and analyze your data before training models.

- [Create a data flow](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-flow.html): Use a SageMaker Canvas data flow to connect your datasets, transformations, and analyses into a single pipeline.
- [How the data flow UI works](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-flow-ui.html): Learn how to navigate the data flow UI in Data Wrangler in Amazon SageMaker Canvas.
- [Edit the data flow sampling configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-flow-edit-sampling.html): Learn how to edit your Data Wrangler data flow sample in Amazon SageMaker Canvas.
- [Add a step to your data flow](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-flow-add-step.html): Learn how to add steps to your Data Wrangler data flows in Amazon SageMaker Canvas.
- [Edit data flow steps](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-flow-edit-steps.html): Learn how to edit your Data Wrangler data source and transform steps in Amazon SageMaker Canvas.
- [Reorder steps in your data flow](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-flow-reorder-steps.html): Learn how to reorder steps to your Data Wrangler data flows in Amazon SageMaker Canvas.
- [Delete a step from your data flow](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-flow-delete-step.html): Delete a step in your Data Wrangler flow in SageMaker Canvas.
- [Perform EDA](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-analyses.html): Use Data Wrangler in SageMaker Canvas to create visualizations and analyses for your data.
- [Transform data](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-transform.html): Use Data Wrangler to apply different transformations to your data.
- [Chat for data prep](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-chat-for-data-prep.html)

### [Data processing](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-processing.html)

Learn how to export your data after finishing an Amazon SageMaker Data Wrangler data flow in Amazon SageMaker Canvas.

- [Export to create a model](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-processing-export-model.html): Learn how to export your transformed dataset directly to the model building process in Amazon SageMaker Canvas model.
- [Export data](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-export-data.html): Learn how to export your transformed data from Data Wrangler data flows either to a Canvas dataset or to Amazon S3.
- [Export a data flow](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-export-data-flow.html): Learn how to export your Data Wrangler data flows as Python code.
- [Add destination nodes](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-destination-nodes-add.html): Learn about how to specify a data export location, also known as a destination node, in your Amazon SageMaker Canvas data flows.
- [Edit a destination node](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-destination-nodes-edit.html): Learn how to edit the export location of a destination node in your Amazon SageMaker Canvas data flows.
- [Create a schedule to automatically process new data](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-export-schedule-job.html): Learn how to create an Amazon EventBridge schedule to run SageMaker Processing jobs on your SageMaker Canvas data.
- [Automate data preparation in SageMaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-export.html): After you transform your data in data flow, you can export the transforms to your machine learning workflows.

### [Generative AI foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat.html)

Chat with Amazon SageMaker JumpStart and Amazon Bedrock large language models to answer questions and increase your productivity.

- [Complete prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-prereqs.html): Complete the prerequisites for using generative AI foundation models in SageMaker Canvas.
- [Start a new conversation to generate, extract, or summarize content](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-new.html): Start chat sessions with generative AI foundation models in SageMaker Canvas.
- [Extract information from documents with document querying](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-query.html): Query your documents and retrieve information from them using generative AI foundation models in SageMaker Canvas.
- [Start up models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-manage.html)
- [Shut down models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-shut-down.html): We highly recommend that you shut down models that you arenât using.
- [Compare model outputs](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-compare.html): Compare the outputs of different generative AI foundation models in SageMaker Canvas.
- [Fine-tune foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-fine-tune.html): Fine-tune foundation models on your data to get responses that are customized to your use case.

### [Ready-to-use models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-ready-to-use-models.html)

Get predictions with Ready-to-use models in SageMaker Canvas without having to build a model or write a single of code.

- [Make predictions for text data](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-ready-to-use-predict-text.html): The following procedures describe how to make both single and batch predictions for text datasets.
- [Make predictions for image data](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-ready-to-use-predict-image.html): The following procedures describe how to make both single and batch predictions for image datasets.
- [Make predictions for document data](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-ready-to-use-predict-document.html): The following procedures describe how to make both single and batch predictions for document datasets.

### [Custom models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-custom-models.html)

Build a custom model in Amazon SageMaker Canvas with your data and make predictions specific to your use case.

### [How custom models work](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-build-model.html)

Build a model in Amazon SageMaker Canvas to make predictions on your data.

- [Preview your model](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-preview-model.html): Preview the accuracy of your model in SageMaker Canvas before running a full build.
- [Data validation](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-dataset-validation.html): Learn about how SageMaker Canvas validates your dataset before model building and how to fix some of the common validation errors.
- [Random sample](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-random-sample.html): Learn about the sampling feature in SageMaker Canvas, which randomly samples your data for model building.
- [Build a model](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-build-model-how-to.html): Learn how to build a custom model in SageMaker Canvas.
- [Advanced model building configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-advanced-settings.html): Learn how to configure the advanced settings when building models in Amazon SageMaker Canvas.
- [Edit an image dataset](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-edit-image.html): Edit your image datasets in SageMaker Canvas.

### [Data exploration and analysis](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-explore-data.html)

Explore your dataset and features in SageMaker Canvas with data visualizations and analytics.

- [Explore your data using visualization techniques](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-explore-data-visualization.html): Explore your dataset and features in SageMaker Canvas with data visualizations.
- [Explore your data using analytics](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-explore-data-analytics.html): Explore your dataset and features in SageMaker Canvas with analytics.
- [Prepare data for model building](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-prepare-data.html): Prepare your data in Amazon SageMaker Canvas with basic transformations before building your model.

### [Model evaluation](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-evaluate-model.html)

Use metrics to evaluate your Amazon SageMaker Canvas model.

- [Evaluate your model's performance](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-scoring.html): Use visualizations and metrics to gain insight into the performance of your Amazon SageMaker Canvas model.
- [Use advanced metrics in your analyses](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-advanced-metrics.html): Use advanced metrics in Amazon SageMaker Canvas to gain deeper insights on the performance of your model.
- [View model candidates in the model leaderboard](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-evaluate-model-candidates.html): View and evaluate the multiple model candidates that Amazon SageMaker Canvas trains.
- [Metrics reference](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-metrics.html): Refer to the definitions of metrics for evaluating models built in Amazon SageMaker Canvas.

### [Predictions with custom models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions.html)

Use the models that you've built to make predictions for your data in Amazon SageMaker Canvas

- [Make single predictions](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions-single.html): Make single predictions with a model that you've built in SageMaker Canvas.

### [Batch predictions](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions-batch.html)

Make batch predictions with a model that you've built in SageMaker Canvas.

- [Batch prediction dataset requirements](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions-batch-preqreqs.html): When making batch predictions in Amazon SageMaker Canvas, make sure you read the following prerequisites.
- [Make manual batch predictions](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions-batch-manual.html): Learn how to make manual batch predictions with your models in Amazon SageMaker Canvas.
- [Make automatic batch predictions](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions-batch-auto.html): Learn how to schedule automatic predictions for a dataset in Amazon SageMaker Canvas.
- [Edit your automatic batch prediction configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions-batch-auto-edit.html): Learn how to edit a schedule for automated batch predictions in Amazon SageMaker Canvas.
- [Delete your automatic batch prediction configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions-batch-auto-delete.html): Learn how to delete a schedule for automated batch predictions in Amazon SageMaker Canvas.
- [View your batch prediction jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions-batch-auto-view.html): Learn how to find your manual and automatic batch prediction jobs in the Amazon SageMaker Canvas application.
- [Send predictions to Quick](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-send-predictions.html): Send your predictions from SageMaker Canvas to Quick to build predictive dashboards with your data.
- [Download a model notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-notebook.html): Access a Jupyter notebook of Python code that shows the steps to building your Amazon SageMaker Canvas model.
- [Send your model to Quick](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-send-model-to-quicksight.html): Send your custom model to Quick and generate predictions in Quick.

### [Time Series Forecasts in Amazon SageMaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-time-series.html)

Make time series forecasts in Amazon SageMaker Canvas.

- [Additional options for forecasting insights](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-additional-insights.html): Use optional methods in Amazon SageMaker Canvas to get more insights from your forecast.
- [Adding model versions in Amazon SageMaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-update-model.html): Update a model by adding new model versions.

### [MLOps](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-mlops.html)

Learn how to integrate models built in SageMaker Canvas with the MLOps processes in your organization.

- [Register a model version in the SageMaker AI model registry](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-register-model.html): Register model versions built in SageMaker Canvas to the SageMaker Model Registry to track the status of your versions and deploy them.
- [Deploy your models to an endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-deploy-model.html): Learn how to deploy your models from SageMaker Canvas to an endpoint and get real-time predictions in a production environment.
- [View your deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-deploy-model-view.html): View your model deployments and deployment details in the SageMaker Canvas application.
- [Update a deployment configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-deploy-model-update.html): Update the details of a model deployment in the SageMaker Canvas application.
- [Test your deployment](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-deploy-model-test.html): Make a single invocation request to test your model deployments in the SageMaker Canvas application.
- [Invoke your endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-deploy-model-invoke.html): Get predictions from a SageMaker Canvas model deployed to an endpoint.
- [Delete a model deployment](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-deploy-model-delete.html): Delete a model deployment and its associated endpoint through the SageMaker Canvas application.

### [How to manage automations](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations.html)

Manage your automatic dataset updates and automatic batch predictions in SageMaker Canvas.

- [View your automations](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations-view.html): View your automatics in SageMaker Canvas.

### [Edit your automatic configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations-edit.html)

Edit your automatic configurations in SageMaker Canvas.

- [Edit your automatic dataset update configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations-edit-dataset.html): You might want to make changes to your auto update configuration for a dataset, such as changing the frequency of the updates.
- [Edit your automatic batch prediction configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations-edit-batch.html): When you edit a batch prediction configuration, you can change the target dataset but not the frequency (since automatic batch predictions occur whenever the dataset is updated).
- [Delete an automatic configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations-delete.html): Delete your automatic configuration in SageMaker Canvas.
- [Logging out](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-log-out.html): Log out of SageMaker Canvas to stop your workspace instance.
- [Limitations and troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-limits.html): Review the following SageMaker Canvas limitations, which can help you troubleshoot any issues you have in Canvas.
- [Billing and cost in SageMaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-cost.html): Manage billing and costs for your SageMaker Canvas apps and users.

### [Geospatial capabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial.html)

Learn about Amazon SageMaker AI capabilities to build, train, and deploy geospatial models.

### [Getting started](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-getting-started.html)

Learn how to get started using the capabilities that Amazon SageMaker geospatial provides.

- [Access to SageMaker geospatial](https://docs.aws.amazon.com/sagemaker/latest/dg/access-studio-classic-geospatial.html)
- [Create a SageMaker geospatial notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-launch-notebook.html): Learn about launching a SageMaker Studio Classic notebook instance with the SageMaker geospatial image.
- [Access a raster data collection and start an earth observation job](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-demo.html): Learn how to access an available raster data collection and create an earth observation job.

### [Geospatial processing job](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-custom-operations.html)

Create processing jobs in Amazon SageMaker Processing to process geospatial data using a fully managed cluster.

- [Overview: ScriptProcessor API](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-custom-operations-overview.html): An overview of how to use Amazon SageMaker Processing with a SageMaker geospatial purpose-built container.
- [Using ScriptProcessor](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-custom-operations-procedure.html): See how to use the ScriptProcessor API with the SageMaker geospatial container to calculate the Normalized Difference Vegetation Index (NDVI).

### [Earth Observation Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-eoj.html)

Learn about Earth Observation jobs.

- [Create an Earth Observation Job](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-eoj-ntb.html): Learn how to create Earth Observation jobs using a Amazon SageMaker Studio Classic notebook with SageMaker geospatial image.
- [Types of Operations](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-eoj-models.html): Learn about the different operations you can use to create Earth Observation jobs.
- [Vector Enrichment Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-vej.html): Learn about Vector Enrichment jobs.
- [Visualization Using SageMaker geospatial capabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-visualize.html): Learn about visualizing data using SageMaker geospatial capabilities.
- [Amazon SageMaker geospatial Map SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-notebook-sdk.html): Learn about the SageMaker geospatial map SDK.
- [SageMaker geospatial capabilities FAQ](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-faq.html): Discover frequently asked questions and solutions about SageMaker geospatial capabilities.

### [Security and Permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-security-general.html)

Use the topics on this page to learn how SageMaker geospatial keeps your data secure.

- [Configuration and Vulnerability Analysis in SageMaker geospatial](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-config-vulnerability.html): Use this page to learn about the configuration and analysis in AWS.
- [Security Best Practices for SageMaker geospatial capabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-sec-best-practices.html): Use this page to learn about security best practices for AWS capabilities.
- [Use SageMaker geospatial capabilities in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-notebooks-and-internet-access-vpc-requirements.html): Use this page to get started using Amazon SageMaker geospatial capabilities in an Amazon Virtual Private Cloud.
- [Use AWS KMS Permissions for SageMaker geospatial capabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-kms.html): Use this page to get started using AWS KMS Permissions for Amazon SageMaker geospatial capabilities.
- [Types of compute instances](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-instances.html): Learn about the three types of compute instances that SageMaker geospatial capabilities offer.
- [Data collections](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-data-collections.html): Learn about the different data collections and which ones you can use to create Earth Observation Jobs (EOJs) using the SageMaker SDK.

### [RStudio](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio.html)

RStudio on Amazon SageMaker AI is an integrated development environment for R with a console, syntax-highlighting editor that supports direct code execution, and tools for plotting, history, debugging and workspace management.

### [RStudio on SageMaker AI management](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-manage.html)

Information on managing RStudio on SageMaker AI.

- [Get an RStudio license](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-license.html): How to Activate and accept an RStudio license for use with Amazon SageMaker AI.

### [RStudio Versioning](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-version.html)

Upgrade to the latest RStudio version and get information about how the upgrade works with SageMaker AI, such as how it affects BYOI images and RSessions.

- [Upgrade to the new version](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-version-upgrade.html): Learn how to upgrade your RStudio version to the new version in Amazon SageMaker AI.
- [Downgrade to a previous version](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-version-downgrade.html): Learn how to downgrade your RStudio version to a previous version in Amazon SageMaker AI.
- [Network and Storage](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-network.html): Describes network access and data storage considerations for your RStudio instance.
- [RStudioServerPro instance type](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-select-instance.html): Information about how to select an instance type for your RStudio Server.
- [Add an RStudio Connect URL](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-configure-connect.html): Setting up a RStudio Connect URL on SageMaker AI.
- [Update the RStudio Package Manager URL](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-configure-pm.html): Setting up a RStudio Package Manager URL on SageMaker AI.
- [Create an Amazon SageMaker AI domain with RStudio using the AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-create-cli.html): Describes how to onboard to Amazon SageMaker AI domain with RStudio enabled using the AWS CLI
- [Add RStudio support to an existing domain](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-add-existing.html): Learn how to add RStudio on Amazon SageMaker AI support to your existing Amazon SageMaker AI domain.

### [Bring your own image](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-byoi.html)

Learn how to bring your own image to use with RStudio on SageMaker AI.

- [Complete prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-byoi-prerequisites.html): Learn the prerequisites for bringing your own image to use with RStudio on SageMaker AI.
- [Custom image specifications](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-byoi-specs.html): Learn custom RStudio image specifications to use with SageMaker AI when you bring your own image.
- [Create an image](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-byoi-create.html): Describes how to create a custom RStudio image.
- [Attach an image](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-byoi-attach.html): Learn how to attach a custom RStudio image to your domain using the SageMaker AI console or the AWS Command Line Interface (AWS CLI).
- [Launch a custom image](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-byoi-launch.html): Learn how to launch your custom Amazon SageMaker image in RStudio.
- [Clean up image resources](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-byoi-sdk-cleanup.html): Learn how to clean up RStudio image resources on SageMaker AI.
- [Create a user to use RStudio](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-create-user.html): Describes how to create and add users to your RStudio-enabled Amazon SageMaker AI domain.
- [Log in to RStudio as another user](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-login-another.html): Learn how to log in to RStudio on SageMaker AI as another user.
- [Terminate sessions for another user](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-terminate-another.html): Learn how to terminate sessions for another user in RStudio on SageMaker AI.
- [Use the RStudio administrative dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-admin.html): Describes how to take actions as an admin to manage other users and access the RStudio administrative dashboard.
- [Shut down RStudio](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-shutdown.html): Information on shutting down and restarting RStudio on SageMaker AI.
- [Billing and cost](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-billing.html): Track the costs associated with your RStudio environment.
- [Diagnose issues and get support](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-troubleshooting.html): Describes how to diagnose issues and get support when using RStudio on Amazon SageMaker AI.

### [RStudio on Amazon SageMaker AI user guide](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-use.html)

Procedures to use RStudio on Amazon SageMaker AI.

- [Launch RSessions from the RStudio Launcher](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-launcher.html): Describes how to open the RStudio Launcher from within SageMaker AI and launch RSessions.
- [Suspend your RSessions](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-launcher-suspend.html): Learn about how to suspend RSessions from the RStudio Launcher when using RStudio on Amazon SageMaker AI.
- [Delete your RSessions](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-launcher-delete.html): Learn about how to delete RSessions from the RStudio Launcher when using RStudio on Amazon SageMaker AI.
- [RStudio Connect](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-connect.html): Describes how to publish your projects to RStudio Connect.
- [Amazon SageMaker AI feature integration with RStudio on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-sm-features.html): Describes how to use Amazon SageMaker AI features using RStudio on Amazon SageMaker AI.

### [Code Editor](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor.html)

Learn how Code Editor, based on Code-OSS, Visual Studio Code - Open Source supports writing, testing, debugging, and running your analytics and machine learning code.

### [Using the Code Editor](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use.html)

Learn how to launch Code Editor, add connections to AWS services, shut down resources, and more.

- [Check version](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-version.html): Learn how to check your Code Editor version.
- [Instances and images](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-instances.html): Look up the Code Editor images for each AWS Region.
- [Launch in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-studio.html): To configure and access your Code Editor integrated development environment through Studio, you must create a Code Editor space.
- [Launch using the AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-launch-cli.html): Learn how to launch a Code Editor application using the AWS CLI
- [Clone a repository](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-clone-a-repository.html): Learn how to clone a repository in Code Editor within Amazon SageMaker Studio.
- [Connections and extensions](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-connections-and-extensions.html): Code Editor supports IDE connections to AWS services as well as extensions available in the Open VSX Registry.
- [Shut down Code Editor resources](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-log-out.html): Shut down resources for Code Editor.

### [Code Editor administrator guide](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-admin.html)

Learn about Code Editor, based on Code-OSS, Visual Studio Code - Open Source workflows specific to administrators.

- [Complete prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-admin-prerequisites.html): Learn about the prerequisites needed to use Code Editor, based on Code-OSS, Visual Studio Code - Open Source on Amazon SageMaker Studio.
- [Give your users access to private spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-admin-user-access.html): Learn how administrators can give users access to private Code Editor spaces.
- [Change the default storage size](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-admin-storage-size.html): Learn how to change the default storage size of a Code Editor space.

### [Code Editor lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-lifecycle-configurations.html)

Learn about using Code Editor lifecycle configurations to automate customization for your Studio environment.

- [Create and attach lifecycle configurations in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-lifecycle-configurations-studio-create.html): Learn about creating and attaching Code Editor lifecycle configurations to automate customization for your Studio environment.
- [Debug lifecycle configurations in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-lifecycle-configurations-studio-debug.html): Learn about debugging Code Editor lifecycle configurations to automate customization for your Studio environment.
- [Detach lifecycle configurations in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-lifecycle-configurations-studio-detach.html): Learn about detaching Code Editor lifecycle configurations from your Studio environment.
- [Clone repositories](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-lifecycle-configurations-repositories.html): Learn how to o clone a repository and create a Code Editor application with the lifecycle configuration attached.
- [Configure extensions](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-lifecycle-configurations-extensions.html): Learn how to create a lifecycle configuration to install Code Editor extensions.
- [Custom images](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-custom-images.html): If you need functionality that is different than what's provided by SageMaker distribution, you can bring your own image with your custom extensions and packages.

### [HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)

SageMaker HyperPod is a capability of SageMaker AI that provides an always-on machine learning environment on resilient clusters.

- [Quickstart](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-quickstart.html): Learn how to set up and manage SageMaker HyperPod clusters using SageMaker HyperPod quickstart guides.
- [Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html): Learn about prerequisites before you get started with SageMaker HyperPod.
- [IAM for HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites-iam.html): Learn about setting up IAM for SageMaker HyperPod.
- [Customer managed key encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-cmk.html): Learn how to use customer managed AWS KMS keys to encrypt volumes in SageMaker HyperPod clusters.

### [HyperPod recipes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipes.html)

Use Amazon SageMaker HyperPod recipes to get started with training and fine-tuning publicly available foundation models.

### [Tutorials](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipes-tutorials.html)

The following quick-start tutorials help you get started with using the recipes for training:

- [GPU pre-training with Slurm clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-gpu-slurm-pretrain-tutorial.html): The following tutorial sets up Slurm environment and starts a training job on a Llama 8 billion parameter model.
- [Trainium pre-training with Slurm clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-trainium-slurm-cluster-pretrain-tutorial.html): The following tutorial sets up a Trainium environment on a Slurm cluster and starts a training job on a Llama 8 billion parameter model.
- [DPO training with Slurm clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-gpu-slurm-dpo-tutorial.html): The following tutorial sets up a Slurm environment and starts a direct preference optimization (DPO) job on a Llama 8 billion parameter model.
- [PEFT-Lora training with Slurm clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-gpu-slurm-peft-lora-tutorial.html): The following tutorial sets up Slurm environment and starts a parameter-efficient fine-tuning (PEFT) job on a Llama 8 billion parameter model.
- [GPU pre-training with Kubernetes clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-gpu-kubernetes-cluster-pretrain-tutorial.html): There are two ways to launch a training job in a GPU Kubernetes cluster:
- [Trainium pre-training with Kubernetes clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-trainium-kubernetes-cluster-pretrain-tutorial.html): You can use one of the following methods to start a training job in a Trainium Kubernetes cluster.
- [GPU pre-training with SageMaker jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-gpu-sagemaker-training-jobs-pretrain-tutorial.html): This tutorial guides you through the process of setting up and running a pre-training job using SageMaker training jobs with GPU instances.
- [Trainium pre-training with SageMaker jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-trainium-sagemaker-training-jobs-pretrain-tutorial.html): This tutorial guides you through the process of setting up and running a pre-training job using SageMaker training jobs with AWS Trainium instances.

### [Default configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/default-configurations.html)

This section outlines the essential components and settings required to initiate and customize your Large Language Model (LLM) training processes using SageMaker HyperPod.

- [GitHub repositories](https://docs.aws.amazon.com/sagemaker/latest/dg/github-repositories.html): To launch a training job, you utilize files from two distinct GitHub repositories:
- [General configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipes-general-configuration.html): The config.yaml file specifies the training recipe and the cluster.

### [Cluster-specific configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations.html)

SageMaker HyperPod offers flexibility in running training jobs across different cluster environments.

- [Running a training job on HyperPod Slurm](https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations-run-training-job-hyperpod-slurm.html): SageMaker HyperPod Recipes supports submitting a training job to a GPU/Trainium slurm cluster.
- [Running a training job on HyperPod k8s](https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations-run-training-job-hyperpod-k8s.html): SageMaker HyperPod Recipes supports submitting a training job to a GPU/Trainium Kubernetes cluster.
- [Running a SageMaker training job](https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations-run-sagemaker-training-job.html): SageMaker HyperPod Recipes supports submitting a SageMaker training job.
- [Considerations](https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations-special-considerations.html): When you're using a Amazon SageMaker HyperPod recipes, there are some factors that can impact the process of model training.
- [Advanced settings](https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations-advanced-settings.html): The SageMaker HyperPod recipe adapter is built on top of the Nvidia Nemo and Pytorch-lightning frameworks.
- [Appendix](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix.html): Use the following information to get information about monitoring and analyzing training results.

### [Slurm orchestration](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-slurm.html)

Orchestrate SageMaker HyperPod clusters using the Slurm open-source software.

### [Getting started](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-slurm.html)

Create your first SageMaker HyperPod cluster and learn the cluster operation functionalities of SageMaker HyperPod.

- [Console](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-slurm-console.html): Create your first SageMaker HyperPod cluster using the SageMaker HyperPod console UI, and delete the cluster and clean resources.
- [CloudFormation](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-slurm-console-create-cluster-cfn.html): Create your SageMaker HyperPod clusters using the CloudFormation templates for HyperPod.
- [AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-slurm-cli.html): Create your first SageMaker HyperPod cluster using the AWS CLI commands for HyperPod.

### [Managing Slurm clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate-slurm.html)

Learn how to manage SageMaker HyperPod clusters orchestrated by Slurm through the console UI or AWS CLI.

- [Using the SageMaker console](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate-slurm-console-ui.html): The following topics provide guidance on how to manage SageMaker HyperPod through the console UI.
- [Using the AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate-slurm-cli-command.html): The following topics provide guidance on writing SageMaker HyperPod API request files in JSON format and run them using the AWS CLI commands.

### [Lifecycle scripts](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-lifecycle-best-practices-slurm.html)

Best practices for preparing lifecycle scripts to set up SageMaker HyperPod with open source workload manager tools.

- [Base lifecycle scripts](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.html): Best practices for setting up base lifecycle scripts provided by HyperPod.
- [Slurm configuration files](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-lifecycle-best-practices-slurm-what-hyperpod-overrides-in-slurm-conf.html): Best practices for managing configurations excluding those that HyperPod manages in Slurm configuration files.
- [Slurm log rotations](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-slurm-log-rotation.html): Learn about enabling log rotation for Slurm to manage disk space usage and system performance.
- [Mounting FSx for Lustre and Amazon FSx for OpenZFS to a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-setup-with-fsx.html): Best practices for mounting Amazon FSx for Lustre and Amazon FSx for OpenZFS to a HyperPod cluster.
- [Validating configuration files](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-validate-json-files.html): Best practices for validating the JSON configuration files before creating a Slurm cluster on HyperPod.
- [Validating runtime](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-validate-runtime.html): Best practices for validating runtime before running production workloads on a Slurm cluster on HyperPod
- [Developing interactive lifecycle scripts](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-develop-lifecycle-scripts.html): Best practices for developing lifecycle scripts interactively on a cluster node

### [Multi-head node support](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-multihead-slurm.html)

Learn about how SageMaker HyperPod supports multiple controller (head) nodes and how to set up multiple controller nodes in a Slurm cluster.

### [Setting up multiple controller nodes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-multihead-slurm-setup.html)

This topic explains how to configure multiple controller (head) nodes in a SageMaker HyperPod Slurm cluster using lifecycle scripts.

- [Provisioning resources](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-multihead-slurm-cfn.html): To set up multiple controller nodes in a HyperPod Slurm cluster, provision AWS resources through two CloudFormation stacks: and .
- [Creating and attaching an IAM policy](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-multihead-slurm-iam.html): This section explains how to create an IAM policy and attach it to the execution role you created in .
- [Preparing and uploading lifecycle scripts](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-multihead-slurm-scripts.html): After creating all the required resources, you'll need to set up lifecycle scripts for your SageMaker HyperPod cluster.
- [Creating a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-multihead-slurm-create.html): After setting up all the required resources and uploading the scripts to the Amazon S3 bucket, you can create a cluster.
- [Considerations](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-multihead-slurm-notes.html): This section provides several important notes which you might find helpful.
- [Environment variables reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-multihead-slurm-variables-reference.html): The following environment variables are defined and used in the tutorial of .

### [Jobs on HyperPod clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-run-jobs-slurm.html)

Learn how to run machine learning workloads on SageMaker HyperPod clusters.

- [Accessing cluster nodes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-run-jobs-slurm-access-nodes.html): Learn how to access SageMaker HyperPod cluster nodes to run distributed jobs.
- [Scheduling Slurm jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-run-jobs-slurm-schedule-slurm-job.html): Learn how to schedule a Slurm job on a SageMaker HyperPod cluster to launch training jobs.
- [Running Docker containers](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-run-jobs-slurm-docker.html): Learn how to run docker containers with a Slurm node on SageMaker HyperPod to run distributed training jobs.
- [Running distributed training workloads](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload.html): Learn how to use Slurm on HyperPod to run distributed training.

### [Cluster resources monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-observability-slurm.html)

To achieve comprehensive observability into your SageMaker HyperPod cluster resources and software components, integrate the cluster with Amazon Managed Service for Prometheus and Amazon Managed Grafana.

- [Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-observability-slurm-prerequisites.html): Before proceeding with the steps to , ensure that the following prerequisites are met.
- [Installing metrics exporter packages](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-observability-slurm-install-exporters.html): In the base configuration lifecycle scripts that the SageMaker HyperPod team provides also includes installation of various metric exporter packages.
- [Validating Prometheus setup](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-observability-slurm-validate-prometheus-setup.html): After you have successfully set up your HyperPod cluster installed with the exporter packages, check if Prometheus is properly set up on the head node of your HyperPod cluster.
- [Setting up a Grafana workspace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws.html): Create a new Amazon Managed Grafana workspace or update an existing Amazon Managed Grafana workspace with Amazon Managed Service for Prometheus as the data source.
- [Exported metrics reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-observability-slurm-exported-metrics-reference.html): The following sections present comprehensive lists of metrics exported from SageMaker HyperPod to Amazon Managed Service for Prometheus upon the successful configuration of the CloudFormation stack for SageMaker HyperPod observability.
- [Slurm metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-slurm-metrics.html): Learn about the Amazon CloudWatch metrics you can use to monitor yourSageMaker HyperPod clusters.

### [Cluster resiliency](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-resiliency-slurm.html)

Learn about the SageMaker HyperPod cluster resiliency features.

- [Health monitoring agent](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-resiliency-slurm-cluster-health-check.html): This section describes the set of health checks that SageMaker HyperPod uses to regularly monitor cluster instance health for issues with devices such as accelerators (GPU and Trainium cores) and networking (EFA).
- [Automatic node recovery and auto-resume](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-resiliency-slurm-auto-resume.html)
- [Manually replace or reboot a node using Slurm](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-resiliency-slurm-replace-faulty-instance.html): This section talks about when you should manually reboot or replace a node, with instructions on how to do both.
- [Cluster management](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-management-slurm.html): Learn about logging and managing SageMaker HyperPod clusters.
- [HyperPod FAQs](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-faq-slurm.html): Frequently asked questions to troubleshoot problems with using SageMaker HyperPod.

### [Amazon EKS orchestration](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks.html)

Orchestrate SageMaker HyperPod compute resources with Amazon EKS.

### [Managing EKS clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate.html)

Learn how to manage SageMaker HyperPod clusters orchestrated by Amazon EKS through the console UI or AWS CLI.

- [Getting started](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-prerequisites.html): Learn about prerequisites before you get started with SageMaker HyperPod cluster orchestration with Amazon EKS.
- [Installing packages](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-install-packages-using-helm-chart.html): Install packages on the Amazon EKS cluster using Helm.
- [Setting up role-based access control](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-setup-rbac.html): Set up Kubernetes role-based access control (RBAC) for data scientist users to run workloads on SageMaker HyperPod clusters orchestrated with Amazon EKS.

### [Custom AMIs](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-custom-ami-support.html)

Learn how to use custom Amazon Machine Images (AMIs) with SageMaker HyperPod clusters to standardize environments and maintain control over your AI infrastructure.

- [Build a custom AMI](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-custom-ami-how-to.html): Learn the process for selecting base AMIs and building custom AMIs for SageMaker HyperPod clusters.
- [Custom AMI cluster management](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-custom-ami-cluster-management.html): Learn how to use custom AMIs when creating and updating SageMaker HyperPod clusters.

### [Console](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui.html)

Learn how to manage SageMaker HyperPod clusters orchestrated by Amazon EKS in the SageMaker AI console.

- [Creating a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-create-cluster.html): Learn how to create SageMaker HyperPod clusters orchestrated by Amazon EKS in the SageMaker AI console.
- [Browsing, viewing, and editing clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-browse-view-edit.html): Learn how to browse, view, and edit SageMaker HyperPod clusters orchestrated by Amazon EKS in the SageMaker AI console.
- [Deleting a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-delete-cluster.html): Learn how to delete SageMaker HyperPod clusters orchestrated by Amazon EKS in the SageMaker AI console.
- [CloudFormation](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-eks-console-create-cluster-cfn.html): Create your SageMaker HyperPod cluster using the CloudFormation templates for HyperPod.

### [AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-cli-command.html)

Learn how to manage SageMaker HyperPod clusters orchestrated by Amazon EKS using the AWS CLI.

- [Creating a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-cli-command-create-cluster.html): Learn how to create a SageMaker HyperPod cluster using the AWS CLI.
- [Retrieving cluster details](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-cli-command-cluster-details.html): Learn how to retrieve SageMaker HyperPod cluster details using the AWS CLI.
- [Updating cluster configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-cli-command-update-cluster.html): Learn how to update the configuration of an existing HyperPod cluster using the AWS CLI.
- [Updating platform software](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-cli-command-update-cluster-software.html): Learn how to update SageMaker HyperPod cluster software using the AWS CLI.
- [Accessing cluster nodes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-access-through-terminal.html): Learn how to access SageMaker HyperPod cluster nodes.
- [Scaling down a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-scale-down.html): Learn how to scale down the instances in your Amazon SageMaker HyperPod cluster either by choosing instances to terminate or randomly terminating instances.
- [Deleting a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-cli-command-delete-cluster.html): Learn how to delete SageMaker HyperPod clusters using the AWS CLI.

### [Managed tiered checkpointing](https://docs.aws.amazon.com/sagemaker/latest/dg/managed-tier-checkpointing.html)

Describes the managed tiered checkpointing for Amazon SageMaker HyperPod.

- [Set up](https://docs.aws.amazon.com/sagemaker/latest/dg/managed-tier-checkpointing-setup.html): Learn how to set up managed tiered checkpointing for Amazon SageMaker HyperPod.
- [Remove](https://docs.aws.amazon.com/sagemaker/latest/dg/managed-tier-checkpointing-remove.html): Learn how to remove managed tiered checkpointing for Amazon SageMaker HyperPod.
- [Security considerations](https://docs.aws.amazon.com/sagemaker/latest/dg/managed-tier-security-considerations.html): Learn about security considerations for managed tiered checkpointing in Amazon SageMaker HyperPod.

### [Task governance](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance.html)

Learn about HyperPod task governance for Amazon EKS clusters, a feature that helps you optimize your HyperPod cluster utilization.

### [Setup](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-setup.html)

Set up SageMaker HyperPod task governance for HyperPod EKS clusters.

- [Dashboard setup](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-setup-dashboard.html): Learn about the dashboard setup, Amazon CloudWatch Observability Amazon EKS add-on, for HyperPod task governance for Amazon EKS clusters.
- [Task governance setup](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-setup-task-governance.html): Learn about the setup for HyperPod task governance for your EKS clusters.
- [Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-metrics.html): Learn about SageMaker HyperPod task governance dashboard metrics.

### [Tasks](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-tasks.html)

Learn about SageMaker HyperPod task governance tasks.

- [Scheduling](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-tasks-scheduling.html): Topology-aware scheduling in Amazon SageMaker HyperPod task governance optimizes the training efficiency of distributed machine learning workloads by placing pods based on the physical network topology of your Amazon EC2 instances.

### [Policies](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-policies.html)

Learn about SageMaker HyperPod task governance policies.

- [Create policies](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-policies-create.html): Learn how to create SageMaker HyperPod task governance policies and how the updates impacts your clusters.
- [Edit policies](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-policies-edit.html): Learn how to edit SageMaker HyperPod task governance policies and how the updates impacts your clusters.
- [Delete policies](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-policies-delete.html): Learn how to delete SageMaker HyperPod task governance policies.

### [Compute allocation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-policies-compute-allocation.html)

Cluster administrators can decide how the organization uses purchased compute.

- [GPU partition quota](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-policies-compute-allocation-gpu-partitions.html): You can extend compute quota allocation to support GPU partitioning, enabling fine-grained resource sharing at the GPU partition level.
- [Example commands](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-cli.html): Examples on how to use the HyperPod task governance AWS CLI commands.
- [Troubleshoot](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-troubleshoot.html): Learn about known solutions for troubleshooting your EKS clusters.
- [Attribution](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-attributions.html): Learn about attributions and third-party licenses for material used in Amazon SageMaker HyperPod task governance.

### [Reporting compute usage](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-usage-reporting.html)

Learn how to implement usage reporting for cost attribution in SageMaker HyperPod EKS-orchestrated clusters.

- [Reports details and data breakdown](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-usage-reporting-content.html): Learn about the content and structure of SageMaker HyperPod usage reports.
- [Generate a report](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-usage-reporting-generate.html): Learn how to generate usage reports for SageMaker HyperPod clusters.
- [Configuring storage for clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-setup-storage.html): Configure storage for data scientist users to manage input and output data and storing checkpoints during training on SageMaker HyperPod clusters orchestrated by Amazon EKS.
- [Using the Amazon EBS CSI driver](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-ebs.html): Learn how to set up the Amazon EBS CSI driver on SageMaker HyperPod EKS clusters.
- [Custom Kubernetes labels and taints](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-custom-labels-and-taints.html): Learn how to configure custom Kubernetes labels and taints on SageMaker HyperPod clusters.

### [Checkpointless training](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless.html)

Checkpointless training on Amazon SageMaker HyperPod enables faster recovery from training infrastructure faults.

### [Training tutorials](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-recipes.html)

HyperPod checkpointless training recipes are predefined job configurations with checkpointless training features enabled.

- [Full Finetuning GPT OSS 120b](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-recipes-finetune.html): The following sequence of steps is required to run checkpointless training recipes on HyperPod.
- [PEFT-LoRA GPT OSS 120b](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-recipes-peft.html): The following sequence of steps is required to run checkpointless training recipes on HyperPod.
- [Pretraining Llama 3 70b](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-recipes-pretraining-llama3.html): The following sequence of steps is required to run checkpointless training recipes on HyperPod.
- [PEFT-LoRA Llama 3 70b](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-recipes-peft-llama.html): The following sequence of steps is required to run checkpointless training recipes on HyperPod.
- [Pretraining or finetuning custom models](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-recipes-custom.html): The following sequence of steps is required to run checkpointless training with your custom model on HyperPod.

### [Training features](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-features.html)

See the following pages to learn about the training features in checkpointless training.

- [Collective communication initialization improvements](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-features-communication.html): NCCL and Gloo are fundamental communication libraries that enable collective operations (such as all-reduce and broadcast) across distributed training processes.
- [Memory Mapped DataLoader](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-features-mmap.html): Another restart overhead stems from data loading: the training cluster remains idle while the dataloader initializes, downloads data from remote file systems, and processes it into batches.
- [In-process recovery and checkpointless training](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-in-process-recovery.html): HyperPod checkpointless training uses model redundancy to enable fault-tolerant training.
- [Special considerations](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-considerations.html): We collect certain routine aggregated and anonymized operational metrics to provide essential service availability.
- [Appendix](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-appendix.html): Monitor training results via HyperPod recipes
- [Release notes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-checkpointless-release-notes.html): See the following release notes to track the latest updates for the SageMaker HyperPod checkpointless training.

### [GPU partitioning](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-gpu-partitioning.html)

Learn how to maximize GPU utilization with GPU partitioning using NVIDIA Multi-Instance GPU (MIG) technology on SageMaker HyperPod clusters.

- [Setting up GPU partitions](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-gpu-partitioning-setup.html): Learn how to configure GPU partitioning with MIG on SageMaker HyperPod clusters.
- [Node lifecycle](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-gpu-partitioning-labels.html): Learn about node lifecycle states and labels for GPU partitioning with MIG on SageMaker HyperPod clusters.
- [Task submission](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-gpu-partitioning-task-submission.html): Learn how to submit tasks and deploy models using GPU partitions on SageMaker HyperPod clusters.

### [Cluster resiliency](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency.html)

Learn about the cluster resiliency features for SageMaker HyperPod cluster orchestration with Amazon EKS.

- [Health Monitoring System](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-health-monitoring-agent.html): SageMaker HyperPod health monitoring system includes Health Monitoring Agent (HMA) as an on-host health monitor and a set of out-of-node health monitors.
- [Basic health checks](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-basic-health-check.html): SageMaker HyperPod performs a set of basic health checks on cluster instances during the creation and update of HyperPod clusters.
- [Deep health checks](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-deep-health-checks.html): SageMaker HyperPod performs deep health checks on cluster instances during the creation and update of HyperPod clusters.
- [Automatic node recovery](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-node-recovery.html): Use the automatic node recovery feature of SageMaker HyperPod to achieve cluster resiliency.
- [Resilience-related Kubernetes labels](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-node-labels.html): Learn about the labels that SageMaker HyperPod creates for marking cluster nodes.
- [Manually quarantine, replace, or reboot a node](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-manual.html): Learn how to manually quarantine, replace, and reboot a faulty node in SageMaker HyperPod clusters orchestrated with Amazon EKS.
- [Suggested resilience configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-config-tips.html): Additional suggestions for configuring the SageMaker HyperPod resiliency features.
- [Spot instances](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-spot.html): Amazon SageMaker HyperPod supports Amazon EC2 Spot Instances, enabling significant cost savings for fault-tolerant and stateless AI/ML workloads.
- [UltraServers](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ultraserver.html): SageMaker HyperPod support for Ultraservers provides high-performance GPU computing capabilities for AI and machine learning workloads.

### [IDEs and Notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-ide.html)

Amazon SageMaker is introducing a new capability for SageMaker HyperPod EKS clusters, which allows AI developers to run their interactive machine learning workloads directly on the HyperPod EKS cluster.

- [Set up permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/permission-setup.html)
- [Install SageMaker AI Spaces Add-on](https://docs.aws.amazon.com/sagemaker/latest/dg/operator-install.html)
- [Customize add-on](https://docs.aws.amazon.com/sagemaker/latest/dg/customization.html)
- [Add users and set up service accounts](https://docs.aws.amazon.com/sagemaker/latest/dg/add-user.html)
- [Limits](https://docs.aws.amazon.com/sagemaker/latest/dg/ds-limits.html): Spaces run as pods on HyperPod EKS nodes with attached EBS volumes.
- [Task governance for Interactive Spaces on HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/task-governance.html): This section covers how to optimize your shared Amazon SageMaker HyperPod EKS clusters for Interactive Spaces workloads.
- [Observability](https://docs.aws.amazon.com/sagemaker/latest/dg/observability.html)
- [Create and manage spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/create-manage-spaces.html): Data scientists can list to view all the spaces they have access to, create a space using one of the templates, update space to update the image, file system, and other attributes of space configuration, and delete a space.
- [Web browser access](https://docs.aws.amazon.com/sagemaker/latest/dg/browser-access.html): Web UI access allows you to connect directly to development spaces running on your SageMaker HyperPod cluster through a secure web browser interface.
- [Remote access to SageMaker Spaces](https://docs.aws.amazon.com/sagemaker/latest/dg/vscode-access.html): Remote access allows you to connect your local Visual Studio Code directly to development spaces running on your SageMaker HyperPod cluster.

### [Train and deploy models](https://docs.aws.amazon.com/sagemaker/latest/dg/getting-started-hyperpod-training-deploying-models.html)

Amazon SageMaker AI HyperPod simplifies large-scale machine learning by providing a robust platform for training and deploying models.

- [Train a PyTorch model](https://docs.aws.amazon.com/sagemaker/latest/dg/train-models-with-hyperpod.html): This topic walks you through the process of training a PyTorch model using HyperPod.
- [Deploy a custom model](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-trained-model.html): After training completes, deploy your model for inference.
- [Deploy a JumpStart model](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-jumpstart-model.html): You can deploy a pre-trained JumpStart model for inference using either the CLI or the SDK.

### [Running jobs on clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-run-jobs.html)

Learn how to run machine learning workloads on SageMaker HyperPod clusters.

- [Installing the HyperPod CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-run-jobs-access-nodes.html): Learn how to install the SageMaker HyperPod CLI.
- [HyperPod CLI commands](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-hyperpod-cli-reference.html): Summary of the SageMaker HyperPod CLI commands.
- [Running jobs using the HyperPod CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-run-jobs-hyperpod-cli.html): Run training jobs on SageMaker HyperPod clusters orchestrated by Amazon EKS using the SageMaker HyperPod CLI.
- [Running jobs using kubectl](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-run-jobs-kubectl.html): Run training jobs on SageMaker HyperPod clusters orchestrated by Amazon EKS using the Kubernetes command line tool (kubectl).

### [Training operator](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-operator.html)

The Amazon SageMaker HyperPod training operator helps you accelerate generative AI model development by efficiently managing distributed training across large GPU clusters.

- [Installation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-operator-install.html): See the following sections to learn about how to install the training operator.
- [Usage](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-operator-usage.html): To use kubectl to run the job, you must create a job.yaml to specify the job specifications and run kubectl apply -f job.yaml to submit the job.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-operator-troubleshooting.html): See the following sections to learn how to troubleshoot error when using the training operator.
- [Elastic training](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-elastic-training.html): Elastic training is a new Amazon SageMaker HyperPod capability that automatically scales training jobs based on compute resource availability and workload priority.

### [Observability](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability.html)

Achieve comprehensive observability into your SageMaker HyperPod cluster resources and software components.

- [Model observability](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability-model.html): Integrate SageMaker HyperPod clusters orchestrated with Amazon EKS with the MLflow application on Amazon SageMaker Studio.

### [Cluster and task observability](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability-cluster.html)

Set up Amazon CloudWatch Container Insights and Amazon Managed Grafana to extract cluster resource utilization metrics and visualize them on various dashboards.

### [Observability with Grafana and Prometheus](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-observability-addon.html)

Learn how to collect and view SageMaker HyperPod metrics by using Amazon Managed Service for Prometheus and Amazon Managed Grafana.

- [Setup](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-addon-setup.html): Learn how to set up the SageMaker HyperPod observability add-on.
- [Dashboards](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-addon-viewing-dashboards.html): Learn how to set up the SageMaker HyperPod observability add-on.
- [Exploring metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-addon-exploring-metrics.html): Learn how to explore SageMaker HyperPod metrics in Amazon Managed Grafana.
- [Customizing dashboards](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-addon-customizing.html): Learn how to customize SageMaker HyperPod cluster metrics and dashboards.
- [Custom metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-addon-custom-metrics.html): Learn how to create custom SageMaker HyperPod cluster metrics.
- [Cluster metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-cluster-metrics.html): Learn about the SageMaker HyperPod metrics categories in Amazon Managed Grafana.
- [Preconfigured alerts](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-addon-alerts.html): Learn about default SageMaker HyperPod metrics alerts.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-addon-troubleshooting.html): Use the following guidance to resolve common issues with the Amazon SageMaker HyperPod (SageMaker HyperPod) observability add-on.

### [Observability with Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci.html)

Use Amazon CloudWatch Container Insights to collect, aggregate, and summarize metrics and logs from the containerized applications and micro-services on the EKS cluster associated with a HyperPod cluster.

- [Access CloudWatch container insights dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci-access-dashboard.html)
- [Continuous provisioning](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-scaling-eks.html): Amazon SageMaker HyperPod clusters created with Amazon EKS orchestration now supports continuous provisioning, a new capability that enables greater flexibility and efficiency running large-scale AI/ML workloads.

### [Autoscaling on HyperPod EKS](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling.html)

Amazon SageMaker HyperPod provides a managed Karpenter based node autoscaling solution for clusters created with EKS orchestration.

- [Create an IAM role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling-iam.html): In the following steps, you'll create an IAM role that allows SageMaker HyperPod to manage Kubernetes nodes in your cluster through Karpenter-based autoscaling.
- [Create a HyperPod cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling-cluster.html): In the following steps, you'll create a SageMaker HyperPod cluster with continuous provisioning enabled and configure it to use Karpenter-based autoscaling.
- [Create a NodeClass](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling-nodeclass.html)
- [Create a NodePool](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling-nodepool.html): The NodePool sets constraints on the nodes that can be created by Karpenter and the pods that can run on those nodes.
- [Deploy a workload](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling-workload.html): The following examples demonstrate how HyperPod autoscaling with Karpenter automatically provisions nodes in response to workload demands.
- [Topology-aware scheduling](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-topology.html): Data transfer efficiency is a critical factor in high-performance computing (HPC) and machine learning workloads.

### [Deploy models on HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment.html)

Learn how to deploy and scale machine learning models on Amazon SageMaker HyperPod, which extends beyond training to provide a comprehensive inference platform that combines Kubernetes flexibility with AWS managed services.

- [Setting up your HyperPod clusters for model deployment](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-setup.html): Learn how to configure and enable Amazon SageMaker HyperPod clusters for machine learning inference by setting up the necessary infrastructure, IAM permissions, and Kubernetes operators.

### [Deploy foundation models and custom fine-tuned models](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy.html)

Learn how to deploy open-weights foundation models from Amazon SageMaker JumpStart and your own fine-tuned models from Amazon S3 and Feature Store using Amazon SageMaker HyperPod's flexible, scalable infrastructure for production inference workloads.

- [Deploy models from JumpStart using Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy-js-ui.html): The following steps show you through how to deploy models from JumpStart using Amazon SageMaker Studio.
- [Deploy models from JumpStart using kubectl](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy-js-kubectl.html): The following steps show you how to deploy a JumpStart model to a HyperPod cluster using kubectl.
- [Deploy custom fine-tuned models from Amazon S3 and Amazon FSx using kubectl](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy-ftm.html): The following steps show you how to deploy models stored on Amazon S3 or Amazon FSx to a Amazon SageMaker HyperPod cluster using kubectl.
- [Autoscaling](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-autoscaling.html): Learn how to configure automatic scaling for your Amazon SageMaker HyperPod inference model deployments to handle varying workload demands efficiently.
- [Monitoring and observability](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-observability.html): Learn how to implement comprehensive inference observability on your Amazon SageMaker HyperPod clusters to monitor and optimize deployed machine learning models through integrated Prometheus and Grafana dashboards.
- [Task governance](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-task-gov.html): Learn how to configure task governance features in Amazon SageMaker HyperPod EKS clusters to optimize shared GPU resources for real-time inference workloads during traffic spikes.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-ts.html): This troubleshooting guide addresses common issues that can occur during Amazon SageMaker HyperPod inference deployment and operation.
- [HyperPod Inference release notes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-inference-release-notes.html): Track the latest updates for Amazon SageMaker HyperPod Inference capabilities.

### [HyperPod in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio.html)

Learn about using Amazon SageMaker HyperPod in Amazon SageMaker Studio.

### [Setting up HyperPod in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-setup.html)

Set up Amazon SageMaker HyperPod in Amazon SageMaker Studio.

- [Setting up a Slurm cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-setup-slurm.html): Set up Amazon SageMaker HyperPod Slurm cluster in Amazon SageMaker Studio.
- [Setting up an Amazon EKS cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-setup-eks.html): Set up your Amazon SageMaker HyperPod EKS cluster in Amazon SageMaker Studio
- [HyperPod tabs in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-tabs.html): Learn about the HyperPod tabs in Studio.
- [Cluster connection and task submission](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-open.html): Learn how to launch Amazon SageMaker Studio IDEs with Amazon SageMaker HyperPod clusters.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-troubleshoot.html): Learn known troubleshoot issues for Amazon SageMaker HyperPod in Amazon SageMaker Studio.
- [References](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ref.html): Use this reference page to find more detailed information and references for SageMaker HyperPod.
- [HyperPod release notes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-notes.html): Track the latest updates for Amazon SageMaker HyperPod.

### [HyperPod AMI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-ami.html)

Track the latest updates for Amazon SageMaker HyperPod AMI releases for Slurm and Amazon EKS orchestrations.

- [AMI updates](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-ami-update.html): Update the AMI version in your SageMaker HyperPod cluster to use the latest versions of the included components and packages for your training jobs and workflows
- [AMI releases for Slurm](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-ami-slurm.html): Track the latest updates for Amazon SageMaker HyperPod AMI releases for Slurm orchestration.
- [AMI releases for Amazon EKS](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-ami-eks.html): Track the latest updates for Amazon SageMaker HyperPod AMI releases for Amazon EKS orchestration.
- [Public AMI releases](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-public-ami.html): Release notes for SageMaker HyperPod public Amazon Machine Images (AMI).

### [Jupyter AI](https://docs.aws.amazon.com/sagemaker/latest/dg/jupyterai.html)

Learn how to use Jupyter AI in SageMaker AI.

- [Installation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-jupyterai-installation.html): Learn how to install the Jupyter AI package.
- [Access features](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-jupyterai-overview.html): Learn about Jupyter AI main capabilities.
- [Model configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-jupyterai-model-configuration.html): Learn how to configure a model provider.
- [Use Jupyter AI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-jupyterai-use.html): Learn how to use Jupyter AI in JupyterLab or Studio Classic.

### [Amazon Q Developer](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-amazon-q.html)

Amazon Q Developer is a generative AI conversational assistant that helps you write better code.

- [Set up](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-amazon-q-admin-guide-set-up.html): Amazon Q Developer is a generative AI conversational assistant.
- [Use](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-user-guide-use-amazon-q.html): Amazon Q Developer is your AI-powered companion for machine learning development.
- [Customize](https://docs.aws.amazon.com/sagemaker/latest/dg/q-customizations.html): Customize Amazon Q Developer in JupyterLab or Code Editor to get code suggestions that are based on examples that you provide.

### [Partner AI Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps.html)

Learn about Amazon SageMaker Partner AI Apps, the types of applications supported, how they work, and integration with AWS services.

- [Set up Partner AI Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-app-onboard.html): Learn about how to set up an Amazon SageMaker Partner AI App, including the permissions needed for administrators and users.
- [Partner AI App provisioning](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps-provision.html): Learn about how to provision a Amazon SageMaker Partner AI App so that users can access it.
- [Set up the Amazon SageMaker Partner AI Apps SDKs](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps-sdk.html): Use this page to learn about the process needed to install and use application-specific SDKs with Amazon SageMaker Partner AI Apps.
- [Partner AI Apps in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps-studio.html): Learn about how to launch Amazon SageMaker Partner AI App from Studio.
- [Use AWS KMS Permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps-kms.html): Use this page to get started using AWS KMS Permissions for Amazon SageMaker Partner AI App capabilities.
- [Cross-account sharing](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-app-resource-sharing-ram.html): Learn how to use AWS Resource Access Manager to set up cross-account sharing for you partner AI app.


## [Data labeling with a human-in-the-loop](https://docs.aws.amazon.com/sagemaker/latest/dg/data-label.html)

### [Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html)

Learn more about creating labeling jobs that use human workers to label your training data

### [Getting started: Create a labeling job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-getting-started.html)

To get started using Amazon SageMaker Ground Truth, follow the instructions in the following sections.

- [Monitoring Your Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-getting-started-step5.html): After you create your labeling job, you see a list of all the jobs that you have created.

### [Label Images](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-label-images.html)

Use Ground Truth to label images.

- [Classify image objects using a bounding box](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-bounding-box.html): The images used to train a machine learning model often contain more than one object.
- [Identify image contents using semantic segmentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-semantic-segmentation.html): To identify the contents of an image at the pixel level, use an Amazon SageMaker Ground Truth semantic segmentation labeling task.
- [Auto-Segmentation Tool](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-auto-segmentation.html): Image segmentation is the process of dividing an image into multiple segments, or sets of labeled pixels.
- [Create an image classification job (Single Label)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-image-classification.html): Use an Amazon SageMaker Ground Truth image classification labeling task when you need workers to classify images using predefined labels that you specify.
- [Create an image classification job (Multi-label)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-image-classification-multilabel.html): Use an Amazon SageMaker Ground Truth multi-label image classification labeling task when you need workers to classify multiple objects in an image.
- [Image Label Verification](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-label-verification.html): Building a highly accurate training dataset for your machine learning (ML) algorithm is an iterative process.

### [Label Text](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-label-text.html)

Use Ground Truth to label text.

- [Extract text information using named entity recognition](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-named-entity-recg.html): To extract information from unstructured text and classify it into predefined categories, use an Amazon SageMaker Ground Truth named entity recognition (NER) labeling task.
- [Categorize text with text classification (Single Label)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-text-classification.html): To categorize articles and text into predefined categories, use text classification.
- [Categorize text with text classification (Multi-label)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-text-classification-multilabel.html): To categorize articles and text into multiple predefined categories, use the multi-label text classification task type.

### [Videos and video frame labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video.html)

You can use Ground Truth to classify videos and annotate video frames (still images extracted from videos) using one of the three built-in video task types.

- [Classify videos](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-classification.html): Use an Amazon SageMaker Ground Truth video classification labeling task when you need workers to classify videos using predefined labels that you specify.

### [Video frames](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-task-types.html)

You can use Ground Truth built-in video frame task types to have workers annotate video frames using bounding boxes, polylines, polygons or keypoints.

- [Identify objects using video frame object detection](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-object-detection.html): You can use the video frame object detection task type to have workers identify and locate objects in a sequence of video frames (images extracted from a video) using bounding boxes, polylines, polygons or keypoint annotation tools.
- [Track objects in video frames using video frame object tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-object-tracking.html): You can use the video frame object tracking task type to have workers track the movement of objects in a sequence of video frames (images extracted from a video) using bounding boxes, polylines, polygons or keypoint annotation tools.
- [Video frame labeling job reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-overview.html): Provides a detailed reference for video frame labeling jobs, including information on input data, task types, workforces, worker user interface, and permission requirements.

### [Worker Instructions](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-worker-instructions.html)

This topic provides an overview of the Ground Truth worker portal and the tools available to complete your video frame labeling task.

- [Navigate the UI](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-worker-instructions-worker-ui-ot.html): You can navigate between video frames using the navigation bar in the bottom-left corner of your UI.
- [Bulk Edit Label and Frame Attributes](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-frame-worker-instructions-ot-bulk-edit.html): You can bulk edit label attributes and frame attributes (attributes).
- [Tool Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-worker-instructions-tool-guide.html): Your task will include one or more tools.
- [Icons Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-worker-instructions-ot-icons.html): Use this table to learn about the icons you see in your UI.
- [Shortcuts](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-worker-instructions-ot-hot-keys.html): The keyboard shortcuts listed in the Shortcuts menu can help you quickly select icons, undo and redo annotations, and use tools to add and edit annotations.
- [Understand Release, Stop and Resume, and Decline Task Options](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-worker-instructions-skip-reject-ot.html): When you open the labeling task, three buttons on the top right allow you to decline the task (Decline task), release it (Release task), and stop and resume it at a later time (Stop and resume later).
- [Saving Your Work and Submitting](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-worker-instructions-saving-work-ot.html): You should periodically save your work using the Save button.

### [Video Frame Object Tracking Tasks](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-ot-worker-instructions.html)

Video frame object tracking tasks require you to track the movement of objects across video frames.

- [Your Task](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-worker-instructions-ot-task.html): When you work on a video frame object tracking task, you need to select a category from the Label category menu on the right side of your worker portal to start annotating.

### [Video Frame Object Detection Tasks](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-od-worker-instructions.html)

Video frame object detection tasks required you to classify and identify the location of objects in video frames using annotations.

- [Your Task](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-worker-instructions-od-task.html): When you work on a video frame object detection task, you need to select a category from the Label category menu on the right side of your worker portal to start annotating.

### [Label 3D Point Clouds](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud.html)

Create a 3D point cloud labeling job to have workers label objects in 3D point clouds generated from 3D sensors like Light Detection and Ranging (LiDAR) sensors and depth cameras, or generated from 3D reconstruction by stitching images captured by an agent like a drone.

### [Built-In Task Types](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-task-types.html)

You can use Ground Truth 3D point cloud labeling modality for a variety of use cases.

- [Classify objects in a 3D point cloud with object detection](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-object-detection.html): Use this task type when you want workers to classify objects in a 3D point cloud by drawing 3D cuboids around objects.

### [3D point cloud object tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-object-tracking.html)

Describes the 3D point cloud object tracking task type in SageMaker AI Ground Truth, including how workers annotate object movement across point cloud frames and the data and tools provided to them.

- [Create a 3D point cloud object tracking labeling job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-object-tracking-create-labeling-job.html): Create a 3D point cloud object tracking labeling job in SageMaker AI using the console or API, including steps for setting up the input manifest file, work team, IAM permissions, and labeling job configuration.
- [View the worker task interface](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-object-tracking-worker-ui.html): Discover how Ground Truth provides workers with tools to complete 3D point cloud object tracking annotation tasks, including navigating the point cloud, adjusting cuboids, using assistive labeling tools, and working with sensor fusion data.
- [Output data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-object-tracking-output-data.html): Understand the output data format for a 3D point cloud object tracking labeling job in Ground Truth, including where the annotations are stored and how to view the output data.
- [Information for creating an adjustment or verification job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-object-tracking-adjustment-verification.html): Get the information you need to create an adjustment and verification labeling job using Ground Truth to verify and adjust labels for 3D point cloud object tracking data.

### [3D point cloud semantic segmentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-semantic-segmentation.html)

Discover how to use the Ground Truth 3D point cloud semantic segmentation task type to classify individual points of a 3D point cloud into pre-specified categories like car, pedestrian, and bike.

- [Create a 3D point cloud semantic segmentation labeling job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-semantic-segmentation-create-labeling-job.html): Learn how to create a 3D point cloud semantic segmentation labeling job using the SageMaker AI console or API.
- [View the worker task interface](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-semantic-segmentation-worker-ui.html): Explore the 3D point cloud semantic segmentation worker task interface, which provides tools for navigating, painting, and annotating objects in a 3D point cloud and corresponding 2D images.
- [Output data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-semantic-segmentation-input-data.html): Understand the Ground Truth output data format when your 3D point cloud semantic segmentation labeling job is completed, and learn about the 3D point cloud object detection output data format.

### [3D-2D point cloud object tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-3d-2d-object-tracking.html)

Use this page to get started with 3D-2D object tracking.

- [Create a 3D-2D point cloud object tracking labeling job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-3d-2d-point-cloud-object-tracking-create-labeling-job.html): Use the CreateLabelingJob API to create a 3D-2D point cloud object tracking labeling job.
- [View the worker task interface](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-3d-2d-object-tracking-worker-ui.html): See what the worker task interface looks like for a 3D-2D object tracking labeling job task.
- [Output data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-3d-2d-object-tracking-output-data.html): Read a brief overview of the output data for a 3D-2D object tracking labeling job.

### [3D point cloud labeling job overview](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-general-information.html)

Provides an overview of the unique features of a Ground Truth 3D point cloud labeling job.

- [3D point cloud labeling job permission requirements](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-permission-3d-point-cloud.html): Security and permissions required to create a 3D point cloud labeling job using Ground Truth

### [Worker instructions](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-worker-instructions.html)

This topic provides an overview of the Ground Truth worker portal and the tools available to complete your 3D Point Cloud labeling task.

- [3D point cloud semantic segmentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-worker-instructions-semantic-segmentation.html): Use this page to become familiarize with the user interface and tools available to complete your 3D point cloud semantic segmentation task.
- [3D point cloud object detection](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-worker-instructions-object-detection.html): Use this page to familiarize yourself with the user interface and tools available to complete your 3D point cloud object detection task.
- [3D point cloud object tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-worker-instructions-object-tracking.html): Use this page to become familiarize with the user interface and tools available to complete your 3D point cloud object detection task.

### [Label verification and adjustment](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-verification-data.html)

Learn about how to validate labels on a dataset and how to have workers adjust previous labels with Amazon SageMaker Ground Truth.

- [Requirements to create verification and adjustment labeling jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-verify-adjust-prereq.html): Learn about how to requirements needed to create verification and adjustment jobs with Amazon SageMaker Ground Truth.
- [Create a label verification job (console)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-verify-start-console.html): Learn about how to create label verification jobs with Amazon SageMaker Ground Truth.
- [Create a label adjustment job (console)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-adjust-start-console.html): Learn about how to create label adjustment jobs with Amazon SageMaker Ground Truth.
- [Start a label verification or adjustment job (API)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-verify-start-api.html): Learn about how to start a label verification or adjustment job with Amazon SageMaker Ground Truth.
- [Label verification and adjustment data in the output manifest](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-verify-manifest.html): Learn about how label verification and adjustment data is found in the output manifest with Amazon SageMaker Ground Truth.

### [Custom workflows](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates.html)

Learn more about creating a custom labeling workflow using templates and Lambda functions

- [Set up your workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step1.html): In this step you use the console to establish which worker type to use and make the necessary sub-selections for the worker type.
- [Worker templates](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step2.html): Learn more about creating a custom worker task template using HTML, CSS, JavaScript, Liquid template language, and Crowd HTML elements.
- [Liquid automation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step2-automate.html): Our custom template system uses Liquid for automation.

### [Processing with Lambda](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step3.html)

Learn more about the optional lambda functions you can specify when creating a custom labeling workflow

- [Using Lambda functions](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step3-lambda-requirements.html): Learn more about the required syntax of Lambda functions used in Ground Truth
- [Add required permissions to use AWS Lambda with Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step3-lambda-permissions.html): You may need to configure some or all the following to create and use AWS Lambda with Ground Truth.
- [Create Lambda functions using Ground Truth templates](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step3-lambda-create.html): You can create a Lambda function using the Lambda console, the AWS CLI, or an AWS SDK in a supported programming language of your choice.
- [Test pre-annotation and post-annotation Lambda functions](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step3-lambda-test.html): You can test your pre-annotation and post annotation Lambda functions in the Lambda console.
- [Demo: Image Annotation with crowd-bounding-box](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step2-demo1.html): When you chose to use a custom template as your task type in the Amazon SageMaker Ground Truth console, you reach the Custom labeling task panel.
- [Demo: Text Intent with crowd-classifier](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step2-demo2.html): If you choose a custom template, you'll reach the Custom labeling task panel.
- [Create a custom workflow using the API](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step4.html): When you have created your custom UI template (Step 2) and processing Lambda functions (Step 3), you should place the template in an Amazon S3 bucket with a file name format of: <FileName>.liquid.html.

### [Create a Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-create-labeling-job.html)

You can create a labeling job in the Amazon SageMaker AI console and by using an AWS SDK in your preferred language to run CreateLabelingJob.

- [Built-in Task Types](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html): Amazon SageMaker Ground Truth has several built-in task types.
- [Create instruction pages](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-creating-instruction-pages.html): Create custom instructions for labeling jobs to improve your worker's accuracy in completing their task.
- [Create a Labeling Job (Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-create-labeling-job-console.html): You can use the Amazon SageMaker AI console to create a labeling job for all of the Ground Truth built-in task types and custom labeling workflows.
- [Create a Labeling Job (API)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-create-labeling-job-api.html): To create a labeling job using the Amazon SageMaker API, you use the CreateLabelingJob operation.

### [Create a streaming labeling job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-create-job.html)

Streaming labeling jobs enable you to send individual data objects in real time to a perpetually running, streaming labeling job.

- [Use Amazon SNS Topics for Data Labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-create-sns-input-topic.html): You need to create an Amazon SNS input to create a streaming labeling job.
- [Labeling job bucket based notifications](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-s3-setup.html): Learn more about connect a Amazon SNS input topic to updates in your Amazon S3 bucket when creating a labeling job in Ground Truth.
- [Create a Manifest File (Optional)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-manifest.html): When you create a streaming labeling job, you have the one time option to add objects (such as images or text) to an input manifest file that you specify in ManifestS3Uri of CreateLabelingJob.
- [Create a Streaming Labeling Job with the SageMaker API](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-create-labeling-job-api.html): The following is an example of an AWS Python SDK (Boto3) request that you can use to start a streaming labeling job for a built-in task type in the US East (N.
- [Stop a Streaming Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-stop-labeling-job.html): You can manually stop your streaming labeling job using the operation StopLabelingJob.
- [Label category and frame attributes reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-label-cat-config-attributes.html): When you create a 3D point cloud or video frame labeling job using the Amazon SageMaker API operation CreateLabelingJob, you use a label category configuration file to specify your labels and worker instructions.

### [Use input and output data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data.html)

The input data that you provide to Amazon SageMaker Ground Truth is sent to your workers for labeling.

### [Input data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-input.html)

The input data are the data objects that you send to your workforce to be labeled.

- [Input manifest files](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-input-data-input-manifest.html): Each line in an input manifest file is an entry containing an object, or a reference to an object, to label.
- [Automate data setup for labeling jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-console-create-manifest-file.html): You can use the automated data setup to create manifest files for your labeling jobs in the Ground Truth console using images, videos, video frames, text (.txt) files, and comma-separated value (.csv) files stored in Amazon S3.
- [Supported data formats](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-supported-data-formats.html): When you create an input manifest file for a built-in task types manually, your input data must be in one of the following support file formats for the respective input data type.

### [Streaming labeling jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html)

If you want to perpetually send new data objects to Amazon SageMaker Ground Truth to be labeled, use a streaming labeling job.

- [Send data to a streaming labeling job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-how-it-works-send-data.html): Learn about how to send data to a Ground Truth streaming labeling job in Amazon SageMaker AI.
- [Manage labeling requests with an Amazon SQS queue](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-how-it-works-sqs.html): Learn about how to manage labeling requests with an Amazon SQS queue in Amazon SageMaker AI.
- [Receive output data from a streaming labeling job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-how-it-works-output-data.html): Learn about how to receive output data from a Ground Truth streaming labeling job in Amazon SageMaker AI.

### [Duplicate message handling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-impotency.html)

Learn about how Ground Truth handles duplicate messages in Amazon SageMaker AI.

- [Specify a deduplication key and ID in an Amazon SNS message](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-impotency-create.html): Learn about how to specify a deduplication key and ID in an Amazon SNS message in Amazon SageMaker AI.
- [Find deduplication key and ID in your output data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-impotency-output.html): Learn about how to find a deduplication key and ID in your output data in Amazon SageMaker AI.
- [Input Data Quotas](https://docs.aws.amazon.com/sagemaker/latest/dg/input-data-limits.html): Input datasets used in semantic segmentation labeling jobs have a quota of 20,000 items.
- [Select Data for Labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-filtering.html): You can use the Amazon SageMaker AI console to select a portion of your dataset for labeling.

### [3D Point Cloud Input Data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-input-data.html)

Use this topic to learn about the input data format requirements when using Ground Truth 3D point cloud labeling modality to label LiDAR and sensor fusion data.

- [Accepted Raw 3D Data Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-raw-data-types.html): Ground Truth uses your 3D point cloud data to render a 3D scenes that workers annotate.

### [Input Manifest Files for 3D Point Cloud Labeling Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-input-manifest.html)

When you create a labeling job, you provide an input manifest file where each line of the manifest describes a unit of task to be completed by annotators.

- [Create a Point Cloud Frame Input Manifest File](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-single-frame-input-data.html): The manifest is a UTF-8 encoded file in which each line is a complete and valid JSON object.
- [Create a Point Cloud Sequence Input Manifest](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-multi-frame-input-data.html): The manifest is a UTF-8 encoded file in which each line is a complete and valid JSON object.
- [LiDAR Coordinate System and Sensor Fusion](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-sensor-fusion-details.html): Point cloud data is always located in a coordinate system.

### [Video Frame Input Data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-frame-input-data-overview.html)

Use this page to learn about the input data requirements and setup options when creating video frame object detection and object tracking labeling jobs.

- [Choose Video Files or Video Frames for Input Data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-video-input-data.html): When you create a video frame object detection or object tracking labeling job, you can provide a sequence of video frames (images) or you can use the Amazon SageMaker AI console to have Ground Truth automatically extract video frames from your video files.

### [Input Data Setup](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-data-setup.html)

When you create a video frame labeling job, you need to let Ground Truth know where to look for your input data.

- [Set up Automated Video Frame Input Data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-automated-data-setup.html): You can use the Ground Truth automated data setup to automatically detect video files in your Amazon S3 bucket and extract video frames from those files.
- [Set up Video Frame Input Data Manually](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-manual-data-setup.html): Choose the manual data setup option if you have created sequence files for each of your video frame sequences, and a manifest file listing references to those sequences files.
- [Output data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-output.html): The output from a labeling job is placed in the Amazon S3 location that you specified in the console or in the call to the CreateLabelingJob operation.

### [Enhanced data labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-labeling.html)

This guide explains different ways to specify how data is labeled when using Amazon SageMaker Ground Truth.

- [Control the flow of data objects sent to workers](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-batching.html): Learn more about managing how jobs are sent to workers in a labeling job.

### [Annotation consolidation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html)

Learn about annotation consolidation in Amazon SageMaker Ground Truth, which combines multiple workers' annotations into a single label.

- [Annotation consolidation function creation](https://docs.aws.amazon.com/sagemaker/latest/dg/consolidation-lambda.html): Learn how to create your own annotation consolidation function in Amazon SageMaker Ground Truth.
- [Automate data labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html): If you choose, Amazon SageMaker Ground Truth can use active learning to automate the labeling of your input data for certain built-in task types.
- [Chaining labeling jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-reusing-data.html): Amazon SageMaker Ground Truth can reuse datasets from prior jobs in two ways: cloning and chaining.

### [Security and Permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-general.html)

Use the topics on this page to learn how Ground Truth keeps your data secure and how to configure IAM permissions to create a labeling job.

- [CORS Requirement for Input Image Data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-cors-update.html): Earlier in 2020, widely used browsers like Chrome and Firefox changed their default behavior for rotating images based on image metadata, referred to as EXIF data.

### [IAM Permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-permission.html)

Security and permissions required to create a labeling job using Ground Truth

- [Use IAM Managed Policies](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-permissions-get-started.html): SageMaker AI and Ground Truth provide AWS managed policies that you can use to create a labeling job.
- [IAM Permissions To Use the Ground Truth Console](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-permission-console-access.html): To use the Ground Truth area of the SageMaker AI console, you need to grant permission to an entity to access SageMaker AI and other AWS services that Ground Truth interacts with.
- [Create an SageMaker AI Execution Role](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-permission-execution-role.html): When you configure your labeling job, you need to provide an execution role, which is a role that SageMaker AI has permission to assume to start and run your labeling job.
- [Encrypt Output Data and Storage Volume with AWS KMS](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-kms-permissions.html): You can use AWS Key Management Service (AWS KMS) to encrypt output data from a labeling job by specifying a customer managed key when you create the labeling job.

### [Use Ground Truth in an Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-vpc.html)

Use this page to get started using Amazon SageMaker Ground Truth in an Amazon Virtual Private Cloud.

- [Run an Amazon SageMaker Ground Truth Labeling Job in an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/samurai-vpc-labeling-job.html): Use this page to run a Ground Truth labeling job in Amazon VPC.

### [Use Amazon VPC Mode from a Private Worker Portal](https://docs.aws.amazon.com/sagemaker/latest/dg/samurai-vpc-worker-portal.html)

Use this page to run a Ground Truth labeling job in Amazon VPC.

- [Using the SageMaker AI console to manage a VPC config](https://docs.aws.amazon.com/sagemaker/latest/dg/samurai-vpc-workforce-console.html): Use this page to configure a workforce using the Amazon SageMaker Runtime console
- [Using the SageMaker AI AWS API to manage a VPC config](https://docs.aws.amazon.com/sagemaker/latest/dg/samurai-vpc-workforce-cli.html): Use this page to configure a workforce using the Amazon SageMaker Runtime API.
- [Data Encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security.html): An overview data encryption used and supported by Amazon SageMaker Ground Truth.
- [Workforce Authentication and Restrictions](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-workforce-authentication.html): Ground Truth enables you to use your own private workforce to work on labeling jobs.
- [Monitor Labeling Job Status](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-monitor-cloud-watch.html): To monitor a Amazon SageMaker Ground Truth (Ground Truth) labeling job and receive a notification when its status changes, create an Amazon CloudWatch Events rule.

### [Ground Truth Plus](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp.html)

Learn about Amazon SageMaker Ground Truth Plus, a turnkey data labeling service that helps you create high-quality labeled datasets.

### [Getting Started with Amazon SageMaker Ground Truth Plus.](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-getting-started.html)

Use this page to get started with Amazon SageMaker Ground Truth Plus.

- [Set up Amazon SageMaker Ground Truth Plus Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-getting-started-prerequisites.html): Use this page to get started with the prerequisites to set up Amazon SageMaker Ground Truth Plus.
- [Core Components of Amazon SageMaker Ground Truth Plus](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-getting-started-core-components.html): Use this page to get started with the core components for Amazon SageMaker Ground Truth Plus.
- [Request a Project](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-request-project.html): Use this page to learn more about creating an Amazon SageMaker Ground Truth Plus project.
- [Create a Project Team](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-project-team.html): Use this page to learn more about creating a project team for Amazon SageMaker Ground Truth Plus
- [Project Portal](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-project-portal.html): Use this page to learn more about the project portal for Amazon SageMaker Ground Truth Plus.
- [Create a Batch](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-create-batches.html): Use this page to learn more about creating a batch for Amazon SageMaker Ground Truth Plus.
- [Batch Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-review-metrics.html): Use this page to learn more about reviewing your project metrics for Amazon SageMaker Ground Truth Plus.
- [Batch Details](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-review-batches.html): Use this page to learn more about reviewing your batches for Amazon SageMaker Ground Truth Plus.
- [Accept or Reject Batches](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-accept-reject-batch.html): Use this page to learn more about accepting or rejecting batches with Amazon SageMaker Ground Truth Plus.

### [Workforces](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html)

A workforce is the group of workers that you have selected to label your dataset.

- [Using the Amazon Mechanical Turk Workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-public.html): The Amazon Mechanical Turk (Mechanical Turk) workforce provides the most workers for your Amazon SageMaker Ground Truth labeling job and Amazon Augmented AI human review task.
- [Subscribe to vendor workforces](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-vendor.html): You can use a vendor-managed workforce to label your data using Amazon SageMaker Ground Truth (Ground Truth) and Amazon Augmented AI (Amazon A2I).

### [Private workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-private.html)

AÂ private workforceÂ is a group of workers thatÂ youÂ choose.

### [Amazon Cognito Workforces](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-private-use-cognito.html)

Create and manage your private workforce using Amazon Cognito when you want to create your workforce using the Amazon SageMaker AI console or you don't want the overhead of managing worker credentials and authentication.

### [Create a Private Workforce (Amazon Cognito)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html)

When you use Amazon Cognito, you can create a private workforce in one of the following ways:

- [Create a Private Workforce (Amazon SageMaker AI Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private-console.html): You can create a private workforce in the Amazon SageMaker AI console in one of two ways:
- [Create a Private Workforce (Amazon Cognito Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private-cognito.html): Amazon Cognito is used to define and manage your private workforce and your work teams.

### [Manage a Private Workforce (Amazon Cognito)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private.html)

After you have created a private workforce using Amazon Cognito, you can create and manage work teams using the Amazon SageMaker AI console and API operations.

- [Manage a Workforce (Amazon SageMaker AI Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-console.html): You can use the Amazon SageMaker AI console to create and manage the work teams and individual workers that make up a private workforce.
- [Manage a Private Workforce (Amazon Cognito Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-cognito.html): A private workforce corresponds to a singleÂ Amazon Cognito user pool.

### [OIDC IdP Workforces](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-private-use-oidc.html)

Create a private workforce using an OpenID Connect (OIDC) Identity Provider (IdP) when you want to manage and authenticate your workers using your own OIDC IdP.

- [Create a Private Workforce (OIDC IdP)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private-oidc.html): Create a private workforce using an OpenID Connect (OIDC) Identity Provider (IdP) when you want to authenticate and manage workers using your own identity provider.
- [Manage a Private Workforce (OIDC IdP)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-manage-private-oidc.html): Once you've created a private workforce using your OpenID Connect (OIDC) Identity Provider (IdP), you can manage your workers using your IdP.

### [Private workforce management using the Amazon SageMaker API](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api.html)

Learn about private workforce management in Amazon SageMaker AI using the Amazon SageMaker API.

- [Find your workforce name](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api-name.html): Learn about the steps to find your workforce name in Amazon SageMaker AI using the Amazon SageMaker API.
- [Restrict worker access to tasks to allowable IP addresses](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api-cidr.html): Learn about the steps to restrict worker access to tasks in Amazon SageMaker AI using the Amazon SageMaker API.
- [Enable a dual-stack workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api-dualstack.html): Learn about the steps to enable a dual-stack workforce in Amazon SageMaker AI using the Amazon SageMaker API.
- [Update OIDC Identity Provider workforce configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api-update.html): Learn about how to update the OIDC Identity Provider workforce configuration in Amazon SageMaker AI using the Amazon SageMaker API.
- [Delete a private workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api-delete.html): Learn about how to delete a private workforce in Amazon SageMaker AI using the Amazon SageMaker API.
- [Track Worker Performance Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/workteam-private-tracking.html): Amazon SageMaker Ground Truth logs worker events to Amazon CloudWatch, such as when a worker starts or submits a task.

### [Create the Amazon SNS topic](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-sns.html)

Learn about the requirements and steps needed to create an Amazon SNS topic in Amazon SageMaker AI.

- [Manage worker subscriptions](https://docs.aws.amazon.com/sagemaker/latest/dg/workteam-private-sns-manage-topic.html): Learn about the requirements and steps needed to manage worker subscriptions in Amazon SageMaker AI.

### [Crowd HTML Elements Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html)

Crowd HTML Elements are web components, a web standard that abstracts HTML markup, CSS, and JavaScript functionality into an HTML tag or set of tags.

- [SageMaker AI Crowd HTML Elements](https://docs.aws.amazon.com/sagemaker/latest/dg/general-topiclist.html): The following is a list of Crowd HTML Elements that make building a custom template easier and provide a familiar UI for workers.
- [Augmented AI Crowd HTML Elements](https://docs.aws.amazon.com/sagemaker/latest/dg/crowd-elements-a2i-list.html): The following Crowd HTML Elements are only available for Amazon Augmented AI human workflow tasks.

### [Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html)

Learn about Amazon Augmented AI (A2I), a service for augmenting AI application labeling with human review loops to boost confidence in datasets.

### [Get Started with Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-getting-started.html)

Get started with Amazon Augmented AI and learn the core components, prerequisites, and how to use the Amazon A2I console and API.

- [Core Components of Amazon A2I](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-getting-started-core-components.html): Learn the core components of Amazon Augmented AI.
- [Prerequisites to Using Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-getting-started-prerequisites.html): Prerequisites to use Augmented AI.
- [Tutorial: Get Started in the Amazon A2I Console](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-get-started-console.html): Tutorial on using the Amazon A2I console to leverage Augmented AI for document review using Amazon Textract or image moderation using Amazon Rekognition.
- [Tutorial: Get Started Using the Amazon A2I API](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-get-started-api.html): Tutorial on using the Amazon A2I API to create a private work team and a human review workflow for content moderation using Amazon Textract or Amazon Rekognition.

### [Use Cases and Examples](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-task-types-general.html)

You can use Amazon Augmented AI to incorporate a human review into your workflow for built-in task types, Amazon Textract and Amazon Rekognition, or your own custom tasks using a custom task type.

- [Use with Amazon Textract](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-textract-task-type.html): Amazon Textract enables you to add document text detection and analysis to your applications.
- [Use with Amazon Rekognition](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-rekognition-task-type.html): Amazon Rekognition makes it easy to add image analysis to your applications.
- [Use With Custom Task Types](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-task-types-custom.html): This topic covers how to integrate Amazon Augmented AI (Amazon A2I) into a custom machine learning workflow.

### [Create a Human Review Workflow](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-create-flow-definition.html)

Learn how to create a flow definition to configure your Amazon A2I human review loop.

### [JSON Schema for Human Loop Activation Conditions in Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-human-fallback-conditions-json-schema.html)

The HumanLoopActivationConditions is an input parameter of the CreateFlowDefinition API.

- [Use Human Loop Activation Conditions JSON Schema with Amazon Textract](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-json-humantaskactivationconditions-textract-example.html): When used with Amazon A2I, the AnalyzeDocument operation supports the following inputs in the ConditionType parameter:
- [Use Human Loop Activation Conditions JSON Schema with Amazon Rekognition](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-json-humantaskactivationconditions-rekognition-example.html): When used with Amazon A2I, the Amazon Rekognition DetectModerationLabels operation supports the following inputs in the ConditionType parameters:
- [Delete a Human Review Workflow](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-delete-flow-definition.html): Use this page to learn how to delete your human review workflows (flow definitions), and how the status of human loops associated with your flow definition impacts the deletion process.
- [Create and Start a Human Loop](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-start-human-loop.html): Use this guide to learn how to create a start a human loop when using Amazon Augmented AI.
- [Delete a Human Loop](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-delete-human-loop.html): Use this page to learn how to delete your human loops, and the impact of deleting a human loop.

### [Create and Manage Worker Task Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-instructions-overview.html)

You can create a task user interface for your workers by creating a worker task template.

- [Create and Delete Worker Task Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-worker-template-console.html): You can use a worker template to customize the interface and instructions that your workers see when working on your tasks.
- [Create Custom Worker Task Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-custom-templates.html): Customize the Amazon Augmented AI worker console and instructions by creating a custom worker template and integrating it with an Amazon A2I human review workflow.
- [Creating Good Worker Instructions](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-creating-good-instructions-guide.html): Creating good instructions for your human review jobs improves your worker's accuracy in completing their task.
- [Monitor and Manage Your Human Loop](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-monitor-humanloop-results.html): Once you've started a human review loop, you can check the results of tasks sent to the loop and manage it using the Amazon Augmented AI Runtime API.
- [Output Data](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-output-data.html): Explains the Amazon A2I output data format for built-in and custom task types.
- [Permissions and Security](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-permissions-security.html): Learn about permissions required for creating human review workflows (flow definitions), starting human loops, and previewing worker task templates for Amazon Augmented AI.
- [CloudWatch Events](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-cloudwatch-events.html): Learn about how to use Amazon CloudWatch Events (also known as Amazon EventBridge) in Amazon Augmented AI to listen for human review results.
- [API References](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-api-references.html): Learn how to use the different APIs in Amazon Augmented AI, including the control plane and data plane, and the direct integrations with Amazon Rekognition and Amazon Textract.


## [Prepare data](https://docs.aws.amazon.com/sagemaker/latest/dg/data-prep.html)

### [Data preparation with SQL in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension.html)

Learn about the SQL extension in Amazon SageMaker Studio.

- [Quickstart: Query data in Amazon S3](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-sqlexplorer-athena-s3-quickstart.html): Learn how to analyze data in Amazon S3 using the SQL extension in JupyterLab notebooks within Studio.

### [Features overview and usage](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features.html)

Learn about the JupyterLab SQL extension in Studio, its data exploration, SQL editing, and query execution features.

- [Browse data](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-data-discovery.html): Learn about the capabilities of the SQL extension data browser.
- [SQL editor](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-editor.html): Learn about the capabilities of the SQL extension SQL editor.

### [SQL execution](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-sql-execution.html)

Learn about the SQL execution capabilities of the SQL extension.

- [Create a simple connection](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-sql-execution-create-connection.html): Learn how to create a simple connection.
- [Save results in a DataFrame](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-sql-execution-save-dataframe.html): Learn how to save the results of an SQL query in a pandas DataFrame.
- [Override connection properties](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-sql-execution-override-connection.html): Learn how to override default connection properties.
- [Provide dynamic values in SQL queries](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-sql-execution-query-parameters.html): Learn how to use query parameters to provide dynamic values in SQL queries.

### [Connection caching](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-connection-caching.html)

Learn about the connection caching capabilities of the SQL extension.

- [Create cached connections](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-create-cached-connection.html): Learn how to create cached connection.
- [List cached connections](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-list-cached-connection.html): Learn how to list cached connections.
- [Clear cached connections](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-clear-cached-connection.html): Learn how to clear cached connections.
- [Disable cached connections](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-disable-cached-connection.html): Learn how to disable cached connections.
- [Configure network access (for administrators)](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-networking.html): Learn how to configure your network to allow communication between Studio and your data source.

### [Data source connections](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-datasources-connection.html)

Learn how administrators can configure the SQL extension connection to data sources.

- [Create secrets for database access credentials](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-glue-connection-secrets.html): Learn how to create secrets for database access credentials in Secrets Manager.
- [Create admin connections](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-datasources-glue-connection.html): Learn how administrators can create AWS Glue connections to configure the SQL extension access to data sources.
- [Create user-defined connections](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-datasources-glue-connection-user-defined.html): Learn how users can create their own AWS Glue connections to configure the SQL extension access to data sources.
- [Required IAM permissions (for administrators)](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-datasources-connection-permissions.html): Learn about the required IAM permissions that the JupyterLab application needs to access the data through the configured AWS Glue connections using the SQL extension.
- [FAQs](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-faqs.html): FAQs about using the SQL extension, covering logs, errors, and Snowflake issues such as warehouse selection and object access in JupyterLab.
- [Connection parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-connection-properties.html): Details of the supported Python properties for AWS Glue connections per data source.

### [Data preparation at scale using Amazon EMR](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-emr-data-preparation.html)

Learn how to prepare data at scale using Amazon EMR clusters, or EMR Serverless applications from Studio.

- [Configure network access](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-networking.html): Learn how to configure your network to allow communication between Studio or Studio Classic and Amazon EMR.

### [Prepare data using EMR Serverless](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-serverless.html)

Learn about creating and managing Amazon EMR clusters from Amazon SageMaker Studio Classic to process large-scale data for machine learning workloads.

- [Set up permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-emr-serverless-permissions.html): Learn about how to enable listing and self-provisioning Amazon EMR applications from Studio.
- [Create EMR Serverless applications](https://docs.aws.amazon.com/sagemaker/latest/dg/create-emr-serverless-application.html): Learn how to create EMR Serverless applications from Studio.
- [Connect to an EMR Serverless application](https://docs.aws.amazon.com/sagemaker/latest/dg/connect-emr-serverless-application.html): Learn how to connect to an EMR Serverless application from Studio UI or a JupyterLab notebook.
- [Stop an EMR Serverless application](https://docs.aws.amazon.com/sagemaker/latest/dg/terminate-emr-serverless-application.html): Learn how to stop or delete an EMR Serverless application from the Studio UI.

### [Data preparation using Amazon EMR](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-cluster.html)

Learn about creating and managing Amazon EMR clusters from Amazon SageMaker Studio Classic to process large-scale data for machine learning workloads.

- [Quickstart: Launch Amazon EMR clusters in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-cluster-quickstart.html): Quickly set up a test domain that lets data scientists launch Amazon EMR clusters from Amazon SageMaker Studio.

### [Admin guide](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-emr-admin-guide.html)

Learn how administrators can configure networking for Studio to integrate with Amazon EMR clusters across Amazon VPCs and accounts, and enable data scientists to discover and self-provision Amazon EMR clusters using CloudFormation templates.

- [Configure launching an Amazon EMR cluster from Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-set-up-emr-templates.html): Learn how administrators can configure AWS Service Catalog products so data scientists can discover CloudFormation templates and self-provision Amazon EMR clusters from Studio or Studio Classic.
- [Configure listing Amazon EMR clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-configure-discoverability-emr-cluster.html): Instructions on how to set up the discoverability of Amazon EMR clusters in single account or across accounts use cases.
- [Configure IAM runtime roles for Amazon EMR cluster access](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-cluster-rbac.html): Configure IAM runtime roles for Amazon EMR cluster access in Studio.
- [Reference policies](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-set-up-emr-permissions-reference.html): Learn about the JSON documents of the permissions allowing the discovery and launching of Amazon EMR clusters in Studio.

### [User guide](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-emr-user-guide.html)

Learn how to launch, discover, connect to, or terminate an Amazon EMR cluster from Studio or Studio Classic.

- [Launch an Amazon EMR cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-launch-emr-cluster-from-template.html): Learn how to launch an Amazon EMR cluster from Studio or Studio Classic using the CloudFormation templates setup by your administrator.
- [List Amazon EMR clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/discover-emr-clusters.html): Learn how to discover existing Amazon EMR clusters from Studio or Studio Classic.
- [Connect to an Amazon EMR cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/connect-emr-clusters.html): Learn how to connect to an Amazon EMR cluster from Studio or Studio Classic .
- [Terminate an Amazon EMR cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/terminate-emr-clusters.html): Learn how to terminate an Amazon EMR cluster from Studio or Studio Classic.
- [Monitor Spark workloads in Spark UI from Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-access-spark-ui.html): This guide explains how to monitor workloads in Amazon EMR clusters from within Studio or Studio Classic using Spark UI.
- [Blogs and whitepapers](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-resources.html): The following blogs use a case study of sentiment prediction for a movie review to illustrate the process of executing a complete machine learning workflow.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-troubleshooting.html): Learn to troubleshoot common errors that might occur while connecting or using Amazon EMR clusters from Studio or Studio Classic notebooks.

### [Data preparation using AWS Glue interactive sessions](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-glue.html)

Intro to using AWS Glue interactive sessions inside Studio.

- [Get started with AWS Glue interactive sessions](https://docs.aws.amazon.com/sagemaker/latest/dg/getting-started-glue-sm.html): How to set IAM permissions, launch, and use magics for interactive AWS Glue sessions in SageMaker AI.
- [AWS Glue interactive session pricing](https://docs.aws.amazon.com/sagemaker/latest/dg/glue-sm-pricing.html): Pricing information for interactive AWS Glue sessions in Studio or Studio Classic.

### [Prepare Data with Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)

Use Data Wrangler to import your data, run transformations on it, analyze it, and export the results.

- [Get Started with Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-getting-started.html): Get started with Data Wrangler and follow a walkthrough to apply your knowledge.
- [Import](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-import.html): Import your data into Data Wrangler to run transformations and analyses.
- [Create and Use a Data Wrangler Flow](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-data-flow.html): Use a Data Wrangler data flow to connect your datasets, transformations, and analyses into a single pipeline.
- [Get Insights On Data and Data Quality](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-data-insights.html): Use Data Wrangler to get insights about the data and its quality.
- [Automatically Train Models on Your Data Flow](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-autopilot.html): Use Amazon SageMaker Autopilot integration with Data Wrangler to automatically train, tune, and deploy models on your data.
- [Transform Data](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html): Use Data Wrangler to apply different transformations to your data.
- [Analyze and Visualize](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-analyses.html): Use Data Wrangler to create visualizations and analyses for your data.
- [Reusing Data Flows for Different Datasets](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-parameterize.html): Create reusable or rewritable parameters to help automate your data flows.
- [Export](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-data-export.html): You can export some or all of the transformations that you've made in Data Wrangler.
- [Use Data Preparation in a Studio Classic Notebook to Get Data Insights](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-interactively-prepare-data-notebook.html): Use the Data Wrangler data preparation widget within an Amazon SageMaker Studio Classic to get actionable insights and fix data quality issues.
- [Security and Permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-security.html): Understand the permissions needed to use Data Wrangler.
- [Release Notes](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-release-notes.html): See the release notes for information about new Data Wrangler features and documentation updates.
- [Troubleshoot](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-trouble-shooting.html): Use the information on the page for troubleshooting information.
- [Increase Amazon EC2 Instance Limit](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-increase-instance-limit.html): You might see the following error message when you're using Data Wrangler: The following instance type is not available: ml.m5.4xlarge.
- [Update Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-update.html): To update Data Wrangler to the latest release, first shut down the corresponding KernelGateway app from the Amazon SageMaker Studio Classic control panel.
- [Shut Down Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-shut-down.html): When you are not using Data Wrangler, it is important to shut down the instance on which it runs to avoid incurring additional fees.


## [Processing jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)

- [Run a Processing Job with Apache Spark](https://docs.aws.amazon.com/sagemaker/latest/dg/use-spark-processing-container.html): Use Amazon SageMaker Processing to process data and evaluate models with Apache Spark scripts in a Docker image provided by Amazon SageMaker AI.
- [Run a Processing Job with scikit-learn](https://docs.aws.amazon.com/sagemaker/latest/dg/use-scikit-learn-processing-container.html): Use Amazon SageMaker Processing to process data and evaluate models with scikit-learn scripts in a Docker image provided by Amazon SageMaker AI.

### [Data Processing with Framework Processors](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job-frameworks.html)

Use Amazon SageMaker Processing to process data and evaluate models with scripts in premade Docker images for various popular machine learning frameworks.

- [Hugging Face Framework Processor](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job-frameworks-hugging-face.html): Use Amazon SageMaker Processing to process data and evaluate models with scripts in a premade Hugging Face Docker image.
- [MXNet Framework Processor](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job-frameworks-mxnet.html): Use Amazon SageMaker Processing to process data and evaluate models with scripts in a premade MXNet Docker image.
- [PyTorch Framework Processor](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job-frameworks-pytorch.html): Use Amazon SageMaker Processing to process data and evaluate models with scripts in a premade PyTorch Docker image.
- [TensorFlow Framework Processor](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job-frameworks-tensorflow.html): Use Amazon SageMaker Processing to process data and evaluate models with scripts in a premade TensorFlow Docker image.
- [XGBoost Framework Processor](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job-frameworks-xgboost.html): Use Amazon SageMaker Processing to process data and evaluate models with scripts in a premade XGBoost Docker image.

### [Use Your Own Processing Code](https://docs.aws.amazon.com/sagemaker/latest/dg/use-your-own-processing-code.html)

Use your own processing container or build a container to run your Python scripts with Amazon SageMaker Processing.

- [Run Scripts with a Processing Container](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-container-run-scripts.html): Use Amazon SageMaker Processing to perform text processing with your own processing container.

### [How to Build Your Own Processing Container](https://docs.aws.amazon.com/sagemaker/latest/dg/build-your-own-processing-container.html)

This page contains information on how to build your own processing container for Amazon SageMaker Processing from scratch.

- [How Amazon SageMaker Processing Runs Your Processing Container Image](https://docs.aws.amazon.com/sagemaker/latest/dg/byoc-run-image.html): Amazon SageMaker Processing runs your processing container image in a similar way as the following command, where AppSpecification.ImageUri is the Amazon ECR image URI that you specify in a CreateProcessingJob operation.
- [How Amazon SageMaker Processing Configures Input and Output For Your Processing Container](https://docs.aws.amazon.com/sagemaker/latest/dg/byoc-input-and-output.html): When you create a processing job using the CreateProcessingJob operation, you can specify multiple ProcessingInput and ProcessingOutput. values.
- [How Amazon SageMaker Processing Provides Logs and Metrics for Your Processing Container](https://docs.aws.amazon.com/sagemaker/latest/dg/byoc-logs-and-metrics.html): When your processing container writes to stdout or stderr, Amazon SageMaker Processing saves the output from each processing container and puts it in Amazon CloudWatch logs.
- [Save and Access Metadata Information About Your Processing Job](https://docs.aws.amazon.com/sagemaker/latest/dg/byoc-metadata.html): To save metadata from the processing container after exiting it, containers can write UTF-8 encoded text to the /opt/ml/output/message file.
- [Run Your Processing Container Using the SageMaker AI Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/byoc-run.html): You can use the SageMaker Python SDK to run your own processing image by using the Processor class.


## [Create, store, and share features](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)

### [Get started with Amazon SageMaker Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-getting-started.html)

Learn basic Feature Store concepts, learn how to ingest data for your feature store, and then walk through a Feature Store example.

- [Feature Store concepts](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-concepts.html): Learn basic Feature Store concepts.
- [Adding policies to your IAM role](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-adding-policies.html): Amazon SageMaker Feature Store How to add policies to your role?

### [Use Feature Store with SDK for Python (Boto3)](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-create-feature-group.html)

This topic explains how to use Feature Store and create feature groups in Amazon SageMaker Feature Store.

- [Introduction to Feature Store example notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html): This topic introduces Feature Store by providing example code for an example notebook.
- [Fraud detection with Feature Store example notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-fraud-detection-notebook.html): Learn about a fraud detection use case by using an example notebook in Feature Store.
- [Using Amazon SageMaker Feature Store in the console](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-use-with-studio.html): Create, view, and update feature groups, and view pipeline executions and lineage using Amazon SageMaker Feature Store on the console.
- [Delete a feature group](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-delete-feature-group.html): Learn how to delete a feature group using Studio Classic and Studio and to give example code.
- [Add features and records to a feature group](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-update-feature-group.html): Use the UpdateFeatureGroup operation or the console to add features to a feature group.
- [Delete records from your feature groups](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-delete-records.html): How to delete records from online and offline stores.
- [Collection types](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-collection-types.html): Learn about collection types.
- [Time to live (TTL) duration for records](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-time-to-live.html): Amazon SageMaker Feature Store provides function to let records expire after a duration, time to live duration (TTL duration).

### [Feature Store storage configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-storage-configurations.html)

This topic explains the different Feature Store storage configurations and a few major contents.

- [Online store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-storage-configurations-online-store.html): This topic explains the online store storage configuration and storage types.
- [Offline store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-storage-configurations-offline-store.html): This topic explains the offline store storage configuration and table formats.
- [Throughput modes](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-throughput-mode.html): This topic explains the different Feature Store throughput modes.

### [Data sources and ingestion](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-ingest-data.html)

Discuss Amazon SageMaker Feature Store ingestion concepts (online vs offline stores) and then integrations with Data Wrangler, Athena, and AWS Glue.

- [Feature Store Spark](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-ingestion-spark-connector-setup.html): Learn how to set up Spark on Amazon SageMaker AI with Amazon EMR.

### [Feature Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processing.html)

Amazon SageMaker Feature Store Feature Processing is a tool with which you can transform and ingest raw data into your feature groups.

- [Feature Store Feature Processor SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-sdk.html): Amazon SageMaker Feature Store Feature Processor SDK is a toolbox with which you can transform and ingest raw data into your feature groups.
- [Running Feature Store Feature Processor remotely](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-execute-remotely.html): Learn how to run the Amazon SageMaker Feature Store Feature Processor SDK remotely.
- [Creating and running Feature Store Feature Processor pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-create-execute-pipeline.html): Learn how to create and run Amazon SageMaker Feature Store Feature Processor SDK pipelines.
- [Scheduled and event based executions for Feature Processor pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-schedule-pipeline.html): Learn how to schedule an Amazon SageMaker Feature Store Feature Processor SDK Pipeline.
- [Monitor Amazon SageMaker Feature Store Feature Processor pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-monitor-pipeline.html): Learn how to monitor Amazon SageMaker Feature Store Feature Processor SDK pipelines.
- [IAM permissions and execution roles](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-iam-permissions.html): Learn how to use Amazon SageMaker Feature Store Feature Processor SDK IAM permissions.
- [Feature Processor restrictions, limits, and quotas](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-quotas.html): Learn about Amazon SageMaker Feature Store Feature Processor restrictions, limits, and quotas.

### [Data sources](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-data-sources.html)

Learn how to use data sources with feature processor.

- [Feature Processor SDK data sources](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-data-sources-sdk.html): Provide links to Feature Processor SDK data sources, already made by Feature Store, and include examples.
- [Custom data sources](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-data-sources-custom.html): Give instructions on how to create custom data sources for Feature Processor
- [Custom data source examples](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-data-sources-custom-examples.html): Custom data source examples for Feature Processor
- [Example Feature Processing code for common use cases](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-examples.html): Learn about Amazon SageMaker Feature Store Feature Processor SDK examples.
- [Find features in your feature groups](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-search-metadata.html): Find features in your feature groups by using the console or SDK for Python (Boto3).
- [Find feature groups in your Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-search-feature-group-metadata.html): Instructions on finding feature groups in your Feature Store.
- [Adding searchable metadata to your features](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-add-metadata.html): Learn how to add searchable metadata to features in Amazon SageMaker Feature Store.
- [Create a dataset from your feature groups](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-create-a-dataset.html): After a Feature Store feature group has been created in an offline store, you can choose to use the following methods to get your data:

### [Cross account feature group discoverability and access](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account.html)

Learn how to share resources in Amazon SageMaker Feature Store with discoverability and access permissions.

### [Enabling cross account discoverability](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-discoverability.html)

Learn how to share resources in Amazon SageMaker Feature Store with the discoverability permission.

- [Share your feature group catalog](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-discoverability-share-feature-group-catalog.html): Learn how to share the feature group catalog in Amazon SageMaker Feature Store with the discoverability permission.
- [Search discoverable resources](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-discoverability-use.html): Learn how to search for discoverable resources within the feature group catalog.

### [Enabling cross account access](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-access.html)

Learn how to share resources in Amazon SageMaker Feature Store with access permissions.

### [Share online feature groups with AWS Resource Access Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-access-online-store.html)

Learn how to share online store resources in Amazon SageMaker Feature Store with access permissions using AWS RAM.

- [Share your feature group entities](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-access-online-store-share-feature-group.html): Learn how to share the feature group resource type and feature group entities in Amazon SageMaker Feature Store.
- [Use online store shared resources with access permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-access-online-store-use.html): Learn how to use shared online store resources in Amazon SageMaker Feature Store given one of the access permissions.
- [Cross account offline store access](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-access-offline-store.html): Share offline store resources
- [Security and access control](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-security.html): Feature Store Security
- [Logging Feature Store operations by using AWS CloudTrail](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-logging-using-cloudtrail.html): CloudTrail logs Feature Store management and data events
- [Quotas, naming rules and data types](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-quotas.html): Amazon SageMaker Feature Store Quotas, naming rules and data types.
- [Amazon SageMaker Feature Store offline store data format](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-offline.html): Feature Store offline data formats.
- [Amazon SageMaker Feature Store resources](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-resources.html): List of Amazon SageMaker Feature Store resources


## [Reserve capacity with SageMaker training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html)

- [IAM for SageMaker training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-iam-permissions.html): Learn about the IAM permissions required for SageMaker training plans.

### [Training plans creation](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-creation.html)

Learn about creating SageMaker training plans, including searching for offerings, reserving capacity, and managing plans through both the SageMaker AI console and programmatic methods.

### [Create a training plan using the console UI](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-creation-using-console.html)

Learn about creating SageMaker training plans through the SageMaker AI console UI, covering the process of searching for offerings, reviewing options, and purchasing plans for SageMaker AI training jobs and SageMaker HyperPod clusters.

- [Search training plan offerings](https://docs.aws.amazon.com/sagemaker/latest/dg/search-training-plan-offerings.html): After you choose Training Plans in the left pane of the SageMaker AI console, and then Create training plan, a Find training plan form opens up.
- [Reserve the best training plan](https://docs.aws.amazon.com/sagemaker/latest/dg/choose-best-training-plan.html): The search of a training plan has returned offerings that fit your capacity needs and budget.
- [List training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/list-training-plans.html): To view your training plans:
- [View training plan details](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-details.html): From the training plans list, follow a plan's name to view its details.

### [Create a training plan programmatically](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-creation-using-api-cli-sdk.html)

Learn about the programmatic creation of SageMaker training plans using the SageMaker API or AWS CLI.

- [Search training plan offerings](https://docs.aws.amazon.com/sagemaker/latest/dg/search-training-plan-offerings-api-cli-sdk.html): To create a training plan, start by calling the SearchTrainingPlanOfferings API operation, passing your plan requirements (such as instance type, count, and desired time window) as input parameters.
- [Reserve the best training plan](https://docs.aws.amazon.com/sagemaker/latest/dg/choose-best-training-plan-using-api-cli-sdk.html): After reviewing the available training plan offerings that best match your requirements, you can reserve a specific plan by calling the CreateTrainingPlan API operation.
- [List training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/list-training-plans-using-api-cli-sdk.html): You can list all the training plans that have been created in your AWS account and Region by calling the ListTrainingPlans API.
- [View training plan details](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-details-using-api-cli-sdk.html): To monitor the status or retrieve details of a training plan, you can use the DescribeTrainingPlan API.

### [Training plans utilization for SageMaker training jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-utilization-for-training-jobs.html)

You can use a SageMaker training plans for your training jobs by specifying the plan of your choice when creating a training job.

- [Create a training job using the console UI](https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-training-jobs-using-console.html): You can use a SageMaker training plans for your training jobs using the SageMaker AI UI.
- [Create a training job programmatically](https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-training-jobs-using-api-cli-sdk.html): To use SageMaker training plans for your SageMaker training job, specify the TrainingPlanArn parameter of the desired plan in the ResourceConfig when calling the CreateTrainingJob API operation.

### [Training plans utilization for SageMaker HyperPod clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-utilization-for-hyperpod.html)

To use SageMaker training plans for your Amazon SageMaker HyperPod cluster, you specify the training plan you want to use at the cluster instance level when creating or updating your cluster.

- [Create an HyperPod cluster on a training plan using the console UI](https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-hyperpod-creation-using-console.html): To create an SageMaker HyperPod cluster using training plans from the SageMaker AI console UI, follow these steps:
- [Update an HyperPod cluster on a training plan using the console UI](https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-hyperpod-update-using-console.html): You can update, remove, or add a training plan to an existing SageMaker HyperPod cluster using the SageMaker AI console UI.
- [Create an HyperPod cluster on a training plan programmatically](https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-hyperpod-creation-using-api-cli-sdk.html): To use SageMaker training plans for your Amazon SageMaker HyperPod cluster, specify the ARN of the training plan you want to use in the TrainingPlanArn parameter of the ClusterInstanceGroupSpecification when calling the CreateCluster API operation.
- [Update an HyperPod cluster on a training plan programmatically](https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-hyperpod-update-using-api-cli-sdk.html): You can add, update, or remove a training plan by updating the instance group of an existing cluster using the update-cluster AWS CLI command.
- [Quotas and pricing](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-quotas.html): This section provides information on the quotas and limits for SageMaker training plans.
- [Release notes](https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-release-notes.html): See the following release notes to track the latest updates for SageMaker training plans.


## [Model training](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html)

- [Model Training](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html): Review the options for training models with Amazon SageMaker, including built-in algorithms, custom algorithms, libraries, and models from the AWS Marketplace.

### [Types of Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-choose.html)

Learn about the different types of algorithms and machine learning problems that Amazon SageMaker AI supports.

### [Built-in algorithms and pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)

Use Amazon SageMaker built-in algorithms or pretrained models to quickly get started with fine-tuning or deploying models for specific tasks.

### [Common Information](https://docs.aws.amazon.com/sagemaker/latest/dg/common-info-all-im-models.html)

Information common to all of the Amazon SageMaker AI algorithms.

- [Common Data Formats for Training](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-training.html): Data formats commonly accepted by Amazon SageMaker AI for training.
- [Common data formats for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html): Lists the media types that models accept as input for inference.
- [Suggested instance types](https://docs.aws.amazon.com/sagemaker/latest/dg/cmn-info-instance-types.html): Suggested instance types for Amazon SageMaker AI algorithms.
- [Logs](https://docs.aws.amazon.com/sagemaker/latest/dg/common-info-all-sagemaker-models-logs.html): Amazon CloudWatch logs provide detailed information on the Amazon SageMaker training process.

### [Tabular](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-tabular.html)

Learn more about built-in SageMaker AI algorithms for tabular data.

### [AutoGluon-Tabular Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/autogluon-tabular.html)

AutoGluon-Tabular is a novel deep tabular data modeling architecture for supervised learning.

- [How to use AutoGluon-Tabular](https://docs.aws.amazon.com/sagemaker/latest/dg/autogluon-tabular-modes.html): Learn how to use AutoGluon-Tabular as an Amazon SageMaker AI built-in algorithm.
- [Input and Output interface for the AutoGluon-Tabular algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/InputOutput-AutoGluon-Tabular.html): Learn how to use AutoGluon-Tabular as an Amazon SageMaker AI built-in algorithm and about the input and output interface.
- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/autogluon-tabular-HowItWorks.html): How the SageMaker AI AutoGluon-Tabular algorithm works.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/autogluon-tabular-hyperparameters.html): Commonly used hyperparameters for the Amazon SageMaker AI AutoGluon-Tabular algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/autogluon-tabular-tuning.html): Model tuning is not needed for the open-source AutoGluon-Tabular algorithm in Amazon SageMaker AI.

### [CatBoost Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/catboost.html)

CatBoost is a supervised learning algorithm that is an open-source implementation of the gradient boosted decision tree algorithm.

- [How to use CatBoost](https://docs.aws.amazon.com/sagemaker/latest/dg/catboost-modes.html): Learn how to use CatBoost as an Amazon SageMaker AI built-in algorithm.
- [Input and Output interface for the CatBoost algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/InputOutput-CatBoost.html): Learn how to use CatBoost as an Amazon SageMaker AI built-in algorithm and about the input and output interface.
- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/catboost-HowItWorks.html): How the Amazon SageMaker AI CatBoost algorithm works.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/catboost-hyperparameters.html): Commonly used hyperparameters for the Amazon SageMaker AI CatBoost algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/catboost-tuning.html): Metrics and tunable hyperparameters for the open-source CatBoost algorithm in Amazon SageMaker AI.

### [Factorization Machines](https://docs.aws.amazon.com/sagemaker/latest/dg/fact-machines.html)

The Factorization Machines algorithm is a general-purpose supervised learning algorithm that you can use for both classification and regression tasks.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/fact-machines-howitworks.html): The prediction task for a Factorization Machines model is to estimate a function Å· from a feature set xi to a target domain.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/fact-machines-hyperparameters.html): The following table contains the hyperparameters for the Factorization Machines algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/fm-tuning.html): Metrics and tunable hyperparameters for the Factorization Machines algorithm in Amazon SageMaker AI.
- [Inference Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/fm-in-formats.html): Reference of the different inference response formats for the Amazon SageMaker AI Factorization Machines model.

### [K-Nearest Neighbors (k-NN) Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/k-nearest-neighbors.html)

Amazon SageMaker AI k-nearest neighbors (k-NN) algorithm is an index-based algorithm.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/kNN_how-it-works.html): The Amazon SageMaker AI k-nearest neighbors (k-NN) algorithm follows a multi-step training process which includes sampling the input data, performing dimension reduction, and building an index.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/kNN_hyperparameters.html): The following table lists the hyperparameters that you can set for the Amazon SageMaker AI k-nearest neighbors (k-NN) algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/kNN-tuning.html): Metrics and tunable hyperparameters for the Amazon SageMaker AI k-nearest neighbor.
- [Training Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/kNN-in-formats.html): All Amazon SageMaker AI built-in algorithms adhere to the common input training formats described in Common Data Formats - Training.
- [Inference Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/kNN-inference-formats.html): All Amazon SageMaker AI built-in algorithms adhere to the common input inference format described in Common Data Formats - Inference.

### [LightGBM Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/lightgbm.html)

LightGBM is a supervised learning algorithm that is an open-source implementation of the gradient boosted decision tree algorithm.

- [How to use LightGBM](https://docs.aws.amazon.com/sagemaker/latest/dg/lightgbm-modes.html): Learn how to use LightGBM as an Amazon SageMaker AI built-in algorithm.
- [Input and Output interface for the LightGBM algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/InputOutput-LightGBM.html): Learn how to use LightGBM as an Amazon SageMaker AI built-in algorithm and about the input and output interface.
- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/lightgbm-HowItWorks.html): How the SageMaker AI LightGBM algorithm works.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/lightgbm-hyperparameters.html): Commonly used hyperparameters for the Amazon SageMaker AI LightGBM algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/lightgbm-tuning.html): Metrics and tunable hyperparameters for the open-source LightGBM algorithm in Amazon SageMaker AI.

### [Linear Learner Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html)

Linear models are supervised learning algorithms used for solving either classification or regression problems.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/ll_how-it-works.html): There are three steps involved in the implementation of the linear learner algorithm: preprocess, train, and validate.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/ll_hyperparameters.html): The following table contains the hyperparameters for the linear learner algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner-tuning.html): Metrics and tunable hyperparameters for the linear learner algorithm in Amazon SageMaker AI.
- [Inference Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/LL-in-formats.html)

### [TabTransformer Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/tabtransformer.html)

TabTransformer is a supervised learning algorithm that is an open-source implementation of the gradient boosted decision tree algorithm.

- [How to use TabTransformer](https://docs.aws.amazon.com/sagemaker/latest/dg/tabtransformer-modes.html): Learn how to use TabTransformer as an Amazon SageMaker AI built-in algorithm.
- [Input and Output interface for the TabTransformer algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/InputOutput-TabTransformer.html): Learn how to use TabTransformer as an Amazon SageMaker AI built-in algorithm and about the input and output interface.
- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/tabtransformer-HowItWorks.html): How the SageMaker AI TabTransformer algorithm works.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/tabtransformer-hyperparameters.html): Commonly used hyperparameters for the Amazon SageMaker AI TabTransformer algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/tabtransformer-tuning.html): Metrics and tunable hyperparameters for the open-source TabTransformer algorithm in Amazon SageMaker AI.

### [XGBoost Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html)

Learn about XGBoost, which is a supervised learning algorithm that is an open-source implementation of the gradient boosted trees algorithm.

- [How to Use XGBoost](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-how-to-use.html): Learn how to use the XGBoost algorithm with Amazon SageMaker AI.
- [Sample Notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-sample-notebooks.html): The following list contains a variety of sample Jupyter notebooks that address different use cases of Amazon SageMaker AI XGBoost algorithm.
- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-HowItWorks.html): Learn how the SageMaker AI built-in XGBoost algorithm works and explore key concepts related to gradient tree boosting and target variable prediction.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost_hyperparameters.html): Learn about how the hyperparameters used to facilitate the estimation of model parameters from data with the Amazon SageMaker AI XGBoost algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-tuning.html): Metrics and tunable hyperparameters for the Open-Source XGBoost algorithm in Amazon SageMaker AI.

### [Deprecated Versions of XGBoost](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-previous-versions.html)

Deprecated Versions of XGBoost and how to Upgrade to Current Versions.

- [XGBoost Release 0.90](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-version-0.90.html): If you are using the SageMaker Python SDK, to upgrade existing XGBoost 0.90 jobs to version 1.5, you must have version 2.x of the SDK installed and change the XGBoost version and framework_version parameters to 1.5-1.
- [XGBoost Release 0.72](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-72.html): XGBoost is a supervised learning algorithm that is an open-source implementation of the gradient boosted trees algorithm.

### [Text](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-text.html)

Learn more about built-in SageMaker AI algorithms for text data.

### [BlazingText](https://docs.aws.amazon.com/sagemaker/latest/dg/blazingtext.html)

The Amazon SageMaker AI BlazingText algorithm provides implementations of the Word2vec and text classification algorithms.

- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/blazingtext_hyperparameters.html): When you start a training job with a CreateTrainingJob request, you specify a training algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/blazingtext-tuning.html): Metrics and tunable hyperparameters for the Amazon SageMaker AI BlazingText algorithm.

### [Latent Dirichlet Allocation (LDA)](https://docs.aws.amazon.com/sagemaker/latest/dg/lda.html)

The Amazon SageMaker AI Latent Dirichlet Allocation (LDA) algorithm is an unsupervised learning algorithm that attempts to describe a set of observations as a mixture of distinct categories.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/lda-how-it-works.html): Amazon SageMaker AI LDA is an unsupervised learning algorithm that attempts to describe a set of observations as a mixture of different categories.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/lda_hyperparameters.html): In the CreateTrainingJob request, you specify the training algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/lda-tuning.html): Metrics and tunable hyperparameters for the Latent Dirichlet Allocation (LDA) algorithm in Amazon SageMaker AI.

### [Neural Topic Model (NTM) Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/ntm.html)

Amazon SageMaker AI NTM is an unsupervised learning algorithm that is used to organize a corpus of documents into topics that contain word groupings based on their statistical distribution.

- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/ntm_hyperparameters.html): The following table lists the hyperparameters that you can set for the Amazon SageMaker AI Neural Topic Model (NTM) algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/ntm-tuning.html): Metrics and tunable hyperparameters for the Neural Topic Model (NTM) algorithm in Amazon SageMaker AI.
- [Inference Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/ntm-in-formats.html): All Amazon SageMaker AI built-in algorithms adhere to the common input inference format described in Common Data Formats - Inference.

### [Object2Vec](https://docs.aws.amazon.com/sagemaker/latest/dg/object2vec.html)

The Amazon SageMaker AI Object2Vec algorithm is a general-purpose neural embedding algorithm.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/object2vec-howitworks.html): When using the Amazon SageMaker AI Object2Vec algorithm, you follow the standard workflow: process the data, train the model, and produce inferences.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/object2vec-hyperparameters.html): In the CreateTrainingJob request, you specify the training algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/object2vec-tuning.html): Metrics and tunable hyperparameters for the Object2Vec algorithm in Amazon SageMaker AI.
- [Training Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/object2vec-training-formats.html): When training with the Object2Vec algorithm, make sure that the input data in your request is in JSON Lines format, where each line represents a single data point.
- [Inference Formats: Scoring](https://docs.aws.amazon.com/sagemaker/latest/dg/object2vec-inference-formats.html): The following page describes the input request and output response formats for getting scoring inference from the Amazon SageMaker AI Object2Vec model.
- [Inference Formats: Embeddings](https://docs.aws.amazon.com/sagemaker/latest/dg/object2vec-encoder-embeddings.html): The following page lists the input request and output response formats for getting encoder embedding inference from the Amazon SageMaker AI Object2Vec model.

### [Sequence to Sequence (seq2seq)](https://docs.aws.amazon.com/sagemaker/latest/dg/seq-2-seq.html)

Sequence to Sequence (seq2seq) is a supervised learning algorithm that uses Recurrent Neural Networks (RNNs) and Convolutional Neural Networks (CNNs) to map a sequence in one doamin to a sequence in another domain.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/seq-2-seq-howitworks.html): Typically, a neural network for sequence-to-sequence modeling consists of a few layers, including:
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/seq-2-seq-hyperparameters.html): The following table lists the hyperparameters that you can set when training with the Amazon SageMaker AI Sequence-to-Sequence (seq2seq) algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/seq-2-seq-tuning.html): Metrics and tunable hyperparameters for the sequence to sequence algorithm.

### [Text Classification - TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-tensorflow.html)

Use the built-in Amazon SageMaker AI Text Classification - TensorFlow algorithm.

- [How to use Text Classification - TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-tensorflow-how-to-use.html): Learn how to use Text Classification - TensorFlow as an Amazon SageMaker AI built-in algorithm.
- [Input and output interface for the Text Classification - TensorFlow algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-tensorflow-inputoutput.html): Learn how to use Text Classification - TensorFlow as an Amazon SageMaker AI built-in algorithm and about the input and output interface.
- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-tensorflow-HowItWorks.html): The Text Classification - TensorFlow algorithm takes text as classifies it into one of the output class labels.
- [TensorFlow Models](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-tensorflow-Models.html): The following pretrained models are available to use for transfer learning with the Text Classification - TensorFlow algorithm.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-tensorflow-Hyperparameter.html): Hyperparameters for the Amazon SageMaker AI Text Classification - TensorFlow algorithm
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-tensorflow-tuning.html): Metrics and tunable hyperparameters for the Amazon SageMaker AI Text Classification - TensorFlow algorithm.

### [Time-Series](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-time-series.html)

Learn more about built-in SageMaker AI algorithms for time-series data.

### [DeepAR Forecasting](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar.html)

Learn about DeepAR, which is a supervised learning algorithm for forecasting scalar (one-dimensional) time series using recurrent neural networks (RNN).

- [How DeepAR Works](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar_how-it-works.html): During training, DeepAR accepts a training dataset and an optional test dataset.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar_hyperparameters.html): The following table lists the hyperparameters that you can set when training with the Amazon SageMaker AI DeepAR forecasting algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar-tuning.html): Metrics and tunable hyperparameters for the DeepAR algorithm in Amazon SageMaker AI.
- [Inference Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar-in-formats.html): The following page describes the request and response formats for inference with the Amazon SageMaker AI DeepAR model.

### [Unsupervised](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-unsupervised.html)

Learn more about unsupervised built-in SageMaker AI algorithms.

### [IP Insights](https://docs.aws.amazon.com/sagemaker/latest/dg/ip-insights.html)

Amazon SageMaker AI IP Insights is an unsupervised learning algorithm that learns the usage patterns for IPv4 addresses.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/ip-insights-howitworks.html): Amazon SageMaker AI IP Insights is an unsupervised algorithm that consumes observed data in the form of (entity, IPv4 address) pairs that associates entities with IP addresses.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/ip-insights-hyperparameters.html): In the CreateTransformJob request, you specify the training algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/ip-insights-tuning.html): Metrics and tunable hyperparameters for the Amazon SageMaker AI IP Insights algorithm.

### [Data Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/ip-insights-data-formats.html)

This section provides examples of the available input and output data formats used by the IP Insights algorithm during training and inference.

- [Training](https://docs.aws.amazon.com/sagemaker/latest/dg/ip-insights-training-data-formats.html): The following are the available data input formats for the IP Insights algorithm.
- [Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/ip-insights-inference-data-formats.html): The following are the available input and output formats for the IP Insights algorithm.

### [K-Means Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/k-means.html)

K-means is an unsupervised learning algorithm.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/algo-kmeans-tech-notes.html): K-means is an algorithm that trains a model that groups similar objects together.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/k-means-api-config.html): In the CreateTrainingJob request, you specify the training algorithm that you want to use.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/k-means-tuning.html): Metrics and tunable hyperparameters for the SageMaker AI k-means algorithm.
- [Inference Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/km-in-formats.html): All SageMaker AI built-in algorithms adhere to the common input inference format described in Common Data Formats - Inference.

### [Principal Component Analysis (PCA) Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/pca.html)

PCA is an unsupervised machine learning algorithm that attempts to reduce the dimensionality (number of features) within a dataset while still retaining as much information as possible.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/how-pca-works.html): Principal Component Analysis (PCA) is a learning algorithm that reduces the dimensionality (number of features) within a dataset while still retaining as much information as possible.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/PCA-reference.html): In the CreateTrainingJob request, you specify the training algorithm.
- [Inference Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/PCA-in-formats.html): All Amazon SageMaker AI built-in algorithms adhere to the common input inference format described in Common Data Formats - Inference.

### [Random Cut Forest (RCF) Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/randomcutforest.html)

Amazon SageMaker AI Random Cut Forest (RCF) is an unsupervised algorithm for detecting anomalous data points within a data set.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/rcf_how-it-works.html): Amazon SageMaker AI Random Cut Forest (RCF) is an unsupervised algorithm for detecting anomalous data points within a dataset.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/rcf_hyperparameters.html): In the CreateTrainingJob request, you specify the training algorithm.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/random-cut-forest-tuning.html): Metrics and tunable hyperparameters for the random cut forest (RCF) algorithm in Amazon SageMaker AI.
- [Inference Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/rcf-in-formats.html): All Amazon SageMaker AI built-in algorithms adhere to the common input inference format described in Common Data Formats - Inference.

### [Vision](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-vision.html)

Learn more about built-in SageMaker AI algorithms for computer vision.

### [Image Classification - MXNet](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification.html)

The Amazon SageMaker image classification algorithm is a supervised learning algorithm that supports multi-label classification.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/IC-HowItWorks.html): The image classification algorithm takes an image as input and classifies it into one of the output categories.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/IC-Hyperparameter.html): Hyperparameters are parameters that are set before a machine learning model begins learning.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/IC-tuning.html): Metrics and tunable hyperparameters for the Amazon SageMaker image classification algorithm.

### [Image Classification - TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification-tensorflow.html)

The Amazon SageMaker Image Classification - TensorFlow algorithm is a supervised learning algorithm that supports transfer learning with many pretrained models from the TensorFlow Hub.

- [How to use Image Classification - TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/IC-TF-how-to-use.html): Learn how to use Image Classification - TensorFlow as an Amazon SageMaker AI built-in algorithm.
- [Input and output interface for the Image Classification - TensorFlow algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/IC-TF-inputoutput.html): Learn how to use Image Classification - TensorFlow as an Amazon SageMaker AI built-in algorithm and about the input and output interface.
- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/IC-TF-HowItWorks.html): The Image Classification - TensorFlow algorithm takes an image as input and classifies it into one of the output class labels.
- [TensorFlow Hub Models](https://docs.aws.amazon.com/sagemaker/latest/dg/IC-TF-Models.html): The following pretrained models are available to use for transfer learning with the Image Classification - TensorFlow algorithm.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/IC-TF-Hyperparameter.html): Hyperparameters for the Amazon SageMaker Image Classification - TensorFlow algorithm
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/IC-TF-tuning.html): Metrics and tunable hyperparameters for the Amazon SageMaker Image Classification - TensorFlow algorithm.

### [Object Detection - MXNet](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection.html)

The Amazon SageMaker AI Object Detection - MXNet algorithm identifies object instances in an image.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/algo-object-detection-tech-notes.html): The object detection algorithm identifies and locates all instances of objects in an image from a known collection of object categories.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-api-config.html): Hyperparameters used to help estimate the parameters of the Object Detection model during training.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tuning.html): Metrics and tunable hyperparameters for the Amazon SageMaker AI Object Detection algorithm.
- [Inference Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-in-formats.html): The following page describes the inference request and response formats for the Amazon SageMaker AI Object Detection - MXNet model.

### [Object Detection - TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tensorflow.html)

Use the built-in Amazon SageMaker AI Object Detection - TensorFlow algorithm.

- [How to use Object Detection - TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tensorflow-how-to-use.html): Learn how to use Object Detection - TensorFlow as an Amazon SageMaker AI built-in algorithm.
- [Input and output interface for the Object Detection - TensorFlow algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tensorflow-inputoutput.html): Learn how to use Object Detection - TensorFlow as an Amazon SageMaker AI built-in algorithm and about the input and output interface.
- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tensorflow-HowItWorks.html): The Object Detection - TensorFlow algorithm takes an image as input and predicts bounding boxes and object labels.
- [TensorFlow Models](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tensorflow-Models.html): The following pretrained models are available to use for transfer learning with the Object Detection - TensorFlow algorithm.
- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tensorflow-Hyperparameter.html): Hyperparameters for the Amazon SageMaker AI Object Detection - TensorFlow algorithm
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tensorflow-tuning.html): Metrics and tunable hyperparameters for the Amazon SageMaker AI Object Detection - TensorFlow algorithm.

### [Semantic Segmentation](https://docs.aws.amazon.com/sagemaker/latest/dg/semantic-segmentation.html)

The Amazon SageMaker AI semantic segmentation algorithm identifies and locates objects in an image by tagging every pixel with a class label. .

- [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/segmentation-hyperparameters.html): The following tables list the hyperparameters supported by the Amazon SageMaker AI semantic segmentation algorithm for network architecture, data inputs, and training.
- [Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/semantic-segmentation-tuning.html): Tunable hyperparameters for the semantic segmentation algorithm in SageMaker AI.

### [Use Reinforcement Learning](https://docs.aws.amazon.com/sagemaker/latest/dg/reinforcement-learning.html)

Use reinforcement learning in Amazon SageMaker AI to solve complex machine learning problems that optimize objectives in interactive environments.

- [Sample RL Workflow Using Amazon SageMaker AI RL](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-rl-workflow.html): The following example describes the steps for developing RL models using Amazon SageMaker AI RL.
- [RL Environments in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-rl-environments.html): Amazon SageMaker AI RL uses environments to mimic real-world scenarios.
- [Distributed Training with Amazon SageMaker AI RL](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-rl-distributed.html): Amazon SageMaker AI RL supports multi-core and multi-instance distributed training.
- [Hyperparameter Tuning with Amazon SageMaker AI RL](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-rl-tuning.html): You can run a hyperparameter tuning job to optimize hyperparameters for Amazon SageMaker AI RL.

### [Run local code as a remote job](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator.html)

Learn how to run your local Python code as an Amazon SageMaker training job by annotating your training code with the @remote decorator.

- [Invoke a remote function](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-invocation.html): Learn how to invoke a function inside an @remote decorator.
- [Configuration file](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-config.html): Get code examples for various configurations using the @remote decorator or the RemoteExecutor API.
- [Customize your runtime environment](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-customize.html): Learn how to customize your runtime environment for your use case.
- [Container image compatibility](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-container.html): Learn how to check if your image is compatible with an @remote decorator function.
- [Logging parameters and metrics with Amazon SageMaker Experiments](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-experiments.html): Learn how to log parameters and metrics with Amazon SageMaker Experiments.
- [Using modular code with the @remote decorator](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-modular.html): Organize your code into modules for ease of workspace management during development and still use the @remote function to invoke a function.
- [Private repository for runtime dependencies](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-private.html): Learn how to use an @remote function with a private repository.
- [Example notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-examples.html): Use example notebooks to customize your environment, job settings, and more for an image classification problem.

### [Accelerate generative AI development with MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)

Use Amazon SageMaker AI with MLflow to create, manage, analyze, and compare your machine learning experiments.

### [MLflow App Setup](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-app-setup.html)

Create an MLflow App to get started with MLflow and Amazon SageMaker AI

### [MLflow App Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-app-setup-prerequisites.html)

Create an MLflow App to get started with MLflow and Amazon SageMaker AI

- [IAM permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-app-setup-prerequisites-iam.html): Set up IAM permissions to use MLflow Apps with Amazon SageMaker AI

### [Create MLflow App](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-app-setup-create-app.html)

Create an MLflow App to get started with MLflow and Amazon SageMaker AI

- [AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-app-create-app-cli.html): Create an MLflow App using the AWS CLI

### [Tracking servers](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html)

Create an MLflow Tracking Server to get started with MLflow and Amazon SageMaker AI

- [IAM permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server-iam.html): Set up IAM permissions to use MLflow with Amazon SageMaker AI
- [Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server-studio.html): Create an MLflow Tracking Server using Studio
- [AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server-cli.html): Create an MLflow Tracking Server using the AWS CLI
- [Launch MLflow UI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-launch-ui.html): Launch the MLflow UI using a presigned URL and Amazon SageMaker Studio or the AWS CLI

### [Integrate MLflow with your environment](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-track-experiments.html)

Track experiments with MLflow using the MLflow SDK and the AWS MLflow plugin.

- [Log metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-track-experiments-log-metrics.html): Log metrics, parameters, and MLflow models during training using the MLflow SDK and the AWS MLflow plugin.
- [Register models](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-track-experiments-model-registration.html): Automatically register MLflow models using the SageMaker Model Registry.
- [Deploy models](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-track-experiments-model-deployment.html): Deploy MLflow models for inference using Amazon SageMaker AI Model Builder
- [Tutorials](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-tutorials.html): Explore example notebooks to use MLflow with SageMaker AI for various training workflows
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-troubleshooting.html): Troubleshoot common setup issues for Amazon SageMaker AI with MLflow
- [Cleanup](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-cleanup.html): Clean up MLflow resources after training an MLflow model with Amazon SageMaker AI

### [Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments.html)

Experiment tracking using the SageMaker Experiments Python SDK is only available in Studio Classic.

- [Example notebooks for Experiments Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments-examples.html): Learn about the options for example notebooks for Experiments Classic in Studio Classic.
- [View experiments and runs](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments-view-compare.html): Learn how to view expirements and runs for Experiments Classic in Studio Classic.

### [Automatic Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)

Tune machine learning models by finding the best hyperparameter values automatically.

- [Hyperparameter tuning strategies](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html): Amazon SageMaker AI hyperparameter tuning uses either a Bayesian or a random search strategy to find the best values for hyperparameters.
- [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html): Learn to define metrics and environment variables so you can use a custom algorithm or use a built-in algorithm from Amazon SageMaker AI.
- [Define Hyperparameter Ranges](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html): Learn to use SageMaker APIs to define hyperparameter ranges, and discover which hyperparameter scaling types that you can use.
- [Track and set completion criteria](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-progress.html): Learn how to track the progress of your tuning job and set completion criteria to stop tuning when they are met.

### [Tune Multiple Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/multiple-algorithm-hpo.html)

Learn how to automatically tune multiple algorithms.

- [Create an HPO Tuning Job (Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/multiple-algorithm-hpo-create-tuning-jobs.html): Configure and create an HPO tuning job for single or multiple algorithms.
- [Manage Jobs for HPO](https://docs.aws.amazon.com/sagemaker/latest/dg/multiple-algorithm-hpo-manage-tuning-jobs.html): Tools for managing hyperparameter tuning and training jobs.

### [Example: Hyperparameter Tuning Job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex.html)

Example of a hyperparameter tuning job.

- [Create a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-notebook.html)
- [Get the Amazon SageMaker AI Boto 3 Client](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-client.html): Learn how to get the SageMaker AI Boto 3 client.
- [Get the SageMaker AI Execution Role](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-role.html): Get the execution role for the notebook instance.
- [Use an Amazon S3 bucket for input and output](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-bucket.html): Set up a S3 bucket to upload training datasets and save training output data for your hyperparameter tuning job.
- [Download, Prepare, and Upload Training Data](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-data.html): For this example, you use a training dataset of information about bank customers that includes the customer's job, marital status, and how they were contacted during the bank's direct marketing campaign.

### [Configure and Launch a Hyperparameter Tuning Job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-tuning-job.html)

Learn how to configure and launch a tuning job for hyperparameter optimization.

- [Monitor the Progress of a Hyperparameter Tuning Job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-monitor.html): Learn how to monitor the progress of your hyperparameter tuning job.
- [Clean up](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-cleanup.html): To avoid incurring unnecessary charges, when you are done with the example, use the AWS Management Console to delete the resources that you created for it.
- [Stop Training Jobs Early](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html): Learn how to stop a hyperparameter tuning job early.
- [Run a Warm Start Hyperparameter Tuning Job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html): Use warm start to start a Amazon SageMaker AI hyperparameter tuning job that uses information learned from a previous hyperparameter tuning job.
- [Resource Limits for Automatic Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-limits.html): Default resource limits for automatic model tuning and what you can change the values to.
- [Best Practices for Hyperparameter Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-considerations.html): Learn best practices for hyperparameter tuning, such as choosing hyperparameter ranges and scales, and reproducing consistent hyperparameter configurations.

### [Data refining during training](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting.html)

Amazon SageMaker smart sifting is a capability of SageMaker Training that helps improve the efficiency of training datasets and reduce total training time and cost.

- [How SageMaker smart sifting works](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-how-it-works.html): Learn how Amazon SageMaker smart sifting works.
- [Supported frameworks and AWS Regions](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-what-is-supported.html): Find out what machine learning frameworks and AWS Regions Amazon SageMaker smart sifting supports.

### [SageMaker smart sifting within your training script](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-apply-to-script.html)

Learn how to apply SageMaker smart sifting to your training script.

- [Apply SageMaker smart sifting to your PyTorch script](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-apply-to-pytorch-script.html): Learn how to enable SageMaker smart sifting with your training script.
- [Apply SageMaker smart sifting to your Hugging Face Transformers script](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-apply-to-hugging-face-transformers-script.html): Learn how to enable SageMaker smart sifting with your training script.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-best-prac-considerations-troubleshoot.html): Learn about troubleshooting problems while using SageMaker smart sifting.
- [Security in SageMaker smart sifting](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-security.html): Learn about security in SageMaker smart sifting.
- [SageMaker smart sifting Python SDK reference](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-pysdk-reference.html): Learn about the SageMaker smart sifting Python SDK modules.
- [Release notes](https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-release-notes.html): Follow up with release notes to track the latest updates for the SageMaker smart sifting capability.

### [Debugging and improving model performance](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debug-and-improve-model-performance.html)

Debug and improve the performance of deep learning models while training in Amazon SageMaker AI.

### [TensorBoard in SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/tensorboard-on-sagemaker.html)

Use TensorBoard within Amazon SageMaker AI to debug and analyze your machine learning model and the training job of the model.

- [Prepare a training job to collect TensorBoard output data](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-htb-prepare-training-job.html): Prepare a training job to collect TensorBoard output data by preparing a training script and configuring a SageMaker AI estimator object of the SageMaker AI Python SDK.

### [Accessing the TensorBoard application on SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-htb-access-tb.html)

TensorBoard can be accessed in SageMaker AI either programmatically through the sagemaker.interactive_apps.tensorboard module or through the TensorBoard landing page in the SageMaker console, and it automatically finds and displays all training job output data in a compatible format.

- [Open TensorBoard using the sagemaker.interactive_apps.tensorboard module](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-htb-access-tb-url.html): Learn how to open TensorBoard SageMaker AI using the sagemaker.interactive_apps.tensorboard module.
- [Open TensorBoard using the get_app_url function as an estimator class method](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-htb-access-tb-get-app-url-estimator-method.html): Learn how to open TensorBoard in SageMaker AI using the get_app_url function as an estimator class method
- [Open TensorBoard through the SageMaker AI console](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-htb-access-tb-console.html): Learn how to open TensorBoard in the SageMaker AI console
- [Load and visualize output tensors using the TensorBoard application](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-htb-access-tb-data.html): Learn how to load and visualize output tensors using the TensorBoard application in SageMaker AI.
- [Delete unused TensorBoard applications](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-htb-delete-app.html): After you are done with monitoring and experimenting with jobs in TensorBoard, shut the TensorBoard application down.

### [SageMaker Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html)

Debug training jobs in real time, detect non-converging conditions, improve model performance using Amazon SageMaker Debugger.

- [Supported frameworks and algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-supported-frameworks.html): The following table shows SageMaker AI machine learning frameworks and algorithms supported by Debugger.
- [Debugger architecture](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-how-it-works.html): A high-level overview of the Amazon SageMaker Debugger workflow.

### [Tutorials](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-tutorial.html)

Amazon SageMaker Debugger tutorials

- [Tutorial videos](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-videos.html): The following videos provide a tour of Amazon SageMaker Debugger capabilities using SageMaker Studio and SageMaker AI notebook instances.
- [Example notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-notebooks.html): SageMaker Debugger example notebooks are provided in the aws/amazon-sagemaker-examples repository.
- [Advanced demos and visualization](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-visualization.html): The following demos walk you through advanced use cases and visualization scripts using Debugger.

### [Debugging training jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-debug-training-jobs.html)

To prepare your training script and run training jobs with SageMaker Debugger to debug model training progress, you follow the typical two-step process: modify your training script using the sagemaker-debugger Python SDK, and construct a SageMaker AI estimator using the SageMaker Python SDK.

### [Adapting your training script to register a hook](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-modify-script.html)

Amazon SageMaker Debugger comes with a client library called the sagemaker-debugger Python SDK.

- [PyTorch](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-modify-script-pytorch.html): To start collecting model output tensors and debug training issues, make the following modifications to your PyTorch training script.
- [TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-modify-script-tensorflow.html): To start collecting model output tensors and debug training issues, make the following modifications to your TensorFlow training script.

### [Launch training jobs with Debugger using the SageMaker Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configuration-for-debugging.html)

Configure Amazon SageMaker Debugger using Amazon SageMaker Python SDK.

### [Configuring SageMaker Debugger to save tensors](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configure-hook.html)

Tensors are data collections of updated parameters from the backward and forward pass of each training iteration.

- [Configure Tensor Collections](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configure-tensor-collections.html): Use the CollectionConfig API operation to configure tensor collections.
- [Configure the DebuggerHookConfig API to save tensors](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configure-tensor-hook.html): Use the DebuggerHookConfig API to create a debugger_hook_config object using the collection_configs object you created in the previous step.
- [Example notebooks and code samples to configure Debugger hook](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-save-tensors.html): Example Notebooks and Code Samples to Configure Debugger Hook

### [How to configure Debugger Built-in Rules](https://docs.aws.amazon.com/sagemaker/latest/dg/use-debugger-built-in-rules.html)

In the following topics, you'll learn how to use the SageMaker Debugger built-in rules.

- [Configure Debugger Built-in Rules with the Default Parameter Settings](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules-configuration.html): To specify Debugger built-in rules in an estimator, you need to configure a list object.
- [Configure Debugger Built-in Rules with Custom Parameter Values](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules-configuration-param-change.html): If you want to adjust the built-in rule parameter values and customize tensor collection regex, configure the base_config and rule_parameters parameters for the ProfilerRule.sagemaker and Rule.sagemaker classmethods.
- [Example notebooks and code samples to configure Debugger rules](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules-example.html): In the following sections, notebooks and code samples of how to use Debugger rules to monitor SageMaker training jobs are provided.
- [Turn off Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-turn-off.html): If you want to completely turn off Debugger, do one of the following:
- [Useful SageMaker AI estimator class methods for Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-estimator-classmethods.html): The following estimator class methods are useful for accessing your SageMaker training job information and retrieving output paths of training data collected by Debugger.

### [Debugger interactive report for XGBoost](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-report-xgboost.html)

Receive training and profiling reports autogenerated by Amazon SageMaker Debugger.

- [Construct a SageMaker AI XGBoost estimator with the Debugger XGBoost Report rule](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-training-xgboost-report-estimator.html): The rule collects the following output tensors from your training job:
- [Download the Debugger XGBoost training report](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-training-xgboost-report-download.html): Download the Debugger XGBoost training report while your training job is running or after the job has finished using the Amazon SageMaker Python SDK and AWS Command Line Interface (CLI).
- [Debugger XGBoost training report walkthrough](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-training-xgboost-report-walkthrough.html): This section walks you through the Debugger XGBoost training report.

### [Action on Debugger rules](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-action-on-rules.html)

Based on the Debugger rule evaluation status, you can set up automated actions such as stopping a training job and sending notifications using Amazon Simple Notification Service (Amazon SNS).

- [Use Debugger built-in actions for rules](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-actions.html): Use Debugger built-in actions to respond to issues found by .

### [Actions on rules using Amazon CloudWatch and AWS Lambda](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-cloudwatch-lambda.html)

Learn how to use actions on Debugger's built-in rules using Amazon CloudWatch and AWS Lambda.

- [CloudWatch logs for Debugger rules and training jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-cloudwatch-metric.html): Learn how to access CloudWatch logs for Debugger's built-in rules and training jobs.
- [Set up Debugger automated training job termination](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-stop-training.html): Learn how to set up Debugger's to automate training job termination using Amazon CloudWatch and AWS Lambda.
- [Disable the CloudWatch Events rule](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-disable-cw.html): Learn how to disable the CloudWatch Events rule to stop using automated training job termination with Debugger.
- [Visualize Debugger Output Tensors in TensorBoard](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-enable-tensorboard-summaries.html): Use SageMaker Debugger to create output tensor files that are compatible with TensorBoard.
- [List of built-in rules](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules.html): Analyze tensors emitted during the training of machine learning models with Amazon SageMaker Debugger built-in rules.

### [Creating custom rules](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-custom-rules.html)

Use custom rules with the Amazon SageMaker API or with the Amazon SageMaker Python SDK.

- [Use the smdebug client library to create a custom rule as a Python script](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-custom-rules-python-script.html): Use the smdebug library to create a Custom Rule.
- [Use the Debugger APIs to run your own custom rules](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-custom-rules-python-sdk.html): Use the SageMaker Debugger APIs to use a Custom Rule.
- [Use Debugger with custom training containers](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-bring-your-own-container.html): Amazon SageMaker Debugger is available for any deep learning models that you bring to Amazon SageMaker AI.

### [Configure Debugger using SageMaker API](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html)

The preceding topics focus on using Debugger through Amazon SageMaker Python SDK, which is a wrapper around AWS SDK for Python (Boto3) and SageMaker API operations.

- [JSON (AWS CLI)](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules-api.CLI.html): Amazon SageMaker Debugger built-in rules can be configured for a training job using the DebugHookConfig, DebugRuleConfiguration, ProfilerConfig, and ProfilerRuleConfiguration objects through the SageMaker AI CreateTrainingJob API operation.
- [SDK for Python (Boto3)](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules-api.Boto3.html): Amazon SageMaker Debugger built-in rules can be configured for a training job using the create_training_job() function of the AWS Boto3 SageMaker AI client.
- [](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-reference.html): References for Amazon SageMaker Debugger.
- [Access a training container through SSM for remote debugging](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html): You can securely connect to SageMaker training containers through AWS Systems Manager (SSM).
- [Release notes](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-release-notes.html): Track the latest updates for debugging capabilities of Amazon SageMaker AI.

### [Profile and optimize computational performance](https://docs.aws.amazon.com/sagemaker/latest/dg/train-profile-computational-performance.html)

Profile training jobs at scale, use profiler visualization tools provided by SageMaker AI to gain insights at the level of operations, and identify and resolve computational performance issues.

### [SageMaker Profiler](https://docs.aws.amazon.com/sagemaker/latest/dg/train-use-sagemaker-profiler.html)

Profile training jobs in real time, optimize resource utilization by eliminating bottlenecks, improve training speed, and reduce costs using SageMaker Profiler.

- [Supported framework images, AWS Regions, and instance types](https://docs.aws.amazon.com/sagemaker/latest/dg/profiler-support.html): Find out what machine learning frameworks and AWS Regions SageMaker Profiler supports.
- [Prerequisites for SageMaker Profiler](https://docs.aws.amazon.com/sagemaker/latest/dg/profiler-prereq.html): Check prerequisites for using SageMaker Profiler
- [Prepare and run a training job with SageMaker Profiler](https://docs.aws.amazon.com/sagemaker/latest/dg/profiler-prepare.html): Learn how to prepare and run a training job with SageMaker Profiler.
- [Open the SageMaker Profiler UI application](https://docs.aws.amazon.com/sagemaker/latest/dg/profiler-access-smprofiler-ui.html): Learn how to access the SageMaker Profiler UI application.
- [Explore the profile output data visualized in the SageMaker Profiler UI](https://docs.aws.amazon.com/sagemaker/latest/dg/profiler-explore-viz.html): Learn how to interact with the SageMaker Profiler UI and gain insights into the utilization of compute resource.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/profiler-faq.html): Troubleshoot problems while using SageMaker Profiler

### [Monitor AWS compute resource utilization in SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-profile-training-jobs.html)

Monitor AWS compute resource utilization while running training jobs in real time, optimize resource utilization by eliminating bottlenecks, and improve training time and reduce costs of your machine learning models using Amazon SageMaker Debugger.

### [Configure an estimator with parameters for basic profiling using the SageMaker Debugger Python modules](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configuration-for-profiling.html)

Configure Amazon SageMaker Debugger using Amazon SageMaker Python SDK.

- [Configure settings for basic profiling of system resource utilization](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configure-system-monitoring.html): Learn how to configure an estimator for profiling resource utilization using Amazon SageMaker Debugger.

### [Configuration for framework profiling](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configure-framework-profiling.html)

Learn how to create an estimator for detailed profiling using Debugger.

- [Default profiling](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configure-framework-profiling-basic.html): Learn how to create an estimator for default framework profiling using Debugger.
- [Profiling for a target range](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configure-framework-profiling-range.html): Learn how to create an estimator for default system monitoring and customized framework profiling for target steps or a target time range using Debugger.
- [Profiling with different profiling options](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-configure-framework-profiling-options.html): Learn how to create an estimator for default system monitoring and customized framework profiling with different profiling options using Debugger.
- [Update monitoring and profiling configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-update-monitoring-profiling.html): To activate or update the Debugger monitoring configuration for a training job that is currently running, use the SageMaker AI estimator extension methods.
- [Turn off Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-turn-off-profiling.html): Learn how to use the Python methods to stop profiling and debugging.
- [Use built-in profiler rules](https://docs.aws.amazon.com/sagemaker/latest/dg/use-debugger-built-in-profiler-rules.html): Use the Amazon SageMaker Debugger built-in profiling rules to analyze computational performance issues during training on the Amazon EC2 ML instances.
- [List of Built-in Profiler Rules](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-profiler-rules.html): Analyze tensors emitted during the training of machine learning models with Amazon SageMaker Debugger built-in rules.

### [SageMaker Debugger UI in SageMaker Studio Classic Experiments](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-on-studio.html)

Use the Amazon SageMaker Debugger dashboard in Amazon SageMaker Studio Classic to analyze computational performance of your training job on Amazon EC2 instances.

- [Open the SageMaker Debugger Insights dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-on-studio-insights.html): Open the Debugger dashboard in Studio Classic to analyze your model training and on Amazon EC2 instances.
- [SageMaker Debugger Insights dashboard controller](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-on-studio-insights-controllers.html): Learn about the Amazon SageMaker Debugger controller components.
- [Explore the SageMaker Debugger Insights dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-on-studio-insights-walkthrough.html): This guide walks through the content of the Amazon SageMaker Debugger Insights dashboard tabs.
- [Shut Down SageMaker Debugger Insights](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-on-studio-insights-close.html): When you are not using the SageMaker Debugger Insights dashboard, shut down the app instance to avoid incurring additional fees.

### [Debugger interactive report](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-profiling-report.html)

Receive training and profiling reports autogenerated by Amazon SageMaker Debugger.

- [Download a SageMaker Debugger Profiling Report](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-profiling-report-download.html): Download the SageMaker Debugger profiling report while your training job is running or after the job has finished using the Amazon SageMaker Python SDK and AWS Command Line Interface (CLI).
- [Debugger profiling report walkthrough](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-profiling-report-walkthrough.html): This section walks you through the Debugger profiling report section by section.
- [Opt out of the collection of Debugger usage statistics](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-telemetry.html): For all SageMaker training jobs, Amazon SageMaker Debugger runs the rule and autogenerates a .

### [Analyze data using the Debugger Python client library](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-analyze-data.html)

While your training job is running or after it has completed, you can access the training data collected by Debugger using the Amazon SageMaker Python SDK and the SMDebug client library.

- [Access the profile data](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-analyze-data-profiling.html): The SMDebug TrainingJob class reads data from the S3 bucket where the system and framework metrics are saved.
- [Plot the system metrics and framework metrics data](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-access-data-profiling-default-plot.html): You can use the system and algorithm metrics objects for the following visualization classes to plot timeline graphs and histograms.
- [Access the profiling data using the pandas data parsing tool](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-access-data-profiling-pandas-frame.html): The following PandasFrame class provides tools to convert the collected profiling data to Pandas data frame.
- [Access the Python profiling stats data](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-access-data-python-profiling.html): The Python profiling provides framework metrics related to Python functions and operators in your training scripts and the SageMaker AI deep learning frameworks.
- [Merge timelines of multiple profile trace files](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-merge-timeline.html): The SMDebug client library provide profiling analysis and visualization tools for merging timelines of system metrics, framework metrics, and Python profiling data collected by Debugger.
- [Profiling data loaders](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-data-loading-time.html): In PyTorch, data loader iterators, such as SingleProcessingDataLoaderIter and MultiProcessingDataLoaderIter, are initiated at the beginning of every iteration over a dataset.
- [Release notes](https://docs.aws.amazon.com/sagemaker/latest/dg/profiler-release-notes.html): Track the latest updates for profiling capabilities of Amazon SageMaker AI.

### [Distributed training](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html)

Learn about distributed training in Amazon SageMaker AI.

- [Get started with distributed training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-get-started.html): Learn about how to get started with distributed training in Amazon SageMaker AI.
- [Strategies for distributed training](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-strategies.html): Learn about strategies for distributed training in Amazon SageMaker AI.
- [Distributed training optimization](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-optimize.html): Learn about how to optimize distributed training in Amazon SageMaker AI.
- [Scaling training](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-scenarios.html): Learn about to scale distributed training in Amazon SageMaker AI.

### [SageMaker AI distributed data parallelism library](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel.html)

Learn how to run distributed data parallel training in Amazon SageMaker AI.

- [Introduction to the SMDDP library](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-intro.html): The SageMaker AI distributed data parallelism (SMDDP) library is a collective communication library and improves compute performance of distributed data parallel training.
- [Supported frameworks, AWS Regions, and instances types](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-data-parallel-support.html): Check supported frameworks, AWS Regions, instances, and models by the SageMaker AI distributed data parallelism (SMDDP) library.

### [Distributed training with the SMDDP library](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-modify-sdp.html)

Learn how to adapt your training script to use the SageMaker AI distributed data parallelism (SMDDP) library and run distributed training.

### [Adapting your training script to use the SMDDP collective operations](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-modify-sdp-select-framework.html)

Learn what to adapt in your training script for using the SMDDP collective operations.

- [PyTorch](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-modify-sdp-pt.html): Learn how to adapt your PyTorch training script to use the SageMaker AI distributed data parallel library.
- [PyTorch Lightning](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-modify-sdp-pt-lightning.html): Learn how to modify a PyTorch Lightning training script to adapt the SageMaker AI distributed data parallel library.
- [TensorFlow (deprecated)](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-modify-sdp-tf2.html): Learn how to modify a TensorFlow training script to adapt the SageMaker AI distributed data parallel library.

### [Launching distributed training jobs with SMDDP](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html)

Learn how to run a distributed data parallel training job using the SageMaker Python SDK and your adapted training script with SageMaker AI's distributed data parallel library.

- [Use the PyTorch framework estimators in the SageMaker Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-framework-estimator.html): Learn how to launch a distributed training on SageMaker AI using the SageMaker Python SDK.
- [Use the SageMaker AI generic estimator to extend pre-built DLC containers](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-python-skd-api.html): Learn how to extend pre-built DLC containers to handle additional functional requirements for your algorithm or model.
- [Create your own docker container with the library](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-bring-your-own-container.html): Learn how to create your own Docker container and run distributed training on SageMaker AI using SMDDP.
- [Examples](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-data-parallel-v2-examples.html): Find examples of distributed training with Amazon SageMaker AI distributed data parallelism (SMDDP) librar.
- [Configuration tips](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-config.html): Configuration tips for the Amazon SageMaker AI distributed data parallel library.
- [FAQ](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-faq.html): Find answers to commonly asked questions about using the SageMaker AI distributed data parallelism (SMDDP) library.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-troubleshooting-data-parallel.html): Troubleshooting info for distributed training in Amazon SageMaker AI.
- [SMDDP release notes](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-release-notes.html): Release notes to track the latest updates for the SageMaker AI distributed data parallelism (SMDDP) library.

### [SageMaker model parallelism library v2](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-v2.html)

Run model-parallel distributed training jobs on Amazon SageMaker AI using the SageMaker model parallelism library v2.

- [Model parallelism concepts](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-intro-v2.html): Model parallelism is a distributed training method in which the deep learning model is partitioned across multiple devices, within or across instances.
- [Supported frameworks and AWS Regions](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-model-parallel-support-v2.html): Check supported frameworks and AWS Regions by the SageMaker model parallelism library v2.
- [Use the SMP v2](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-use-api-v2.html): Learn how to run a model-parallel training job of your PyTorch training script using the SageMaker Python SDK with the SageMaker model parallelism library.

### [Core features of SMP v2](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2.html)

Learn about the core features of Amazon SageMaker AI's model parallelism library that offer distribution strategies and memory-saving techniques, such as sharded data parallelism, tensor parallelism, and checkpointing.

- [Hybrid sharded data parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-sharded-data-parallelism.html): Use the SageMaker model parallelism library's sharded data parallelism to shard the training state of a model and reduce the per-GPU memory footprint of the model.
- [Expert parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-expert-parallelism.html): Use the SageMaker model parallelism library's expert parallelism to split the experts of a mixture-of-experts (MoE) model into GPU devices and reduce compute cost.
- [Context parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-context-parallelism.html): Train Hugging Face Transformer models with context parallelism in the SageMaker model parallelism library.
- [Compatibility with the SMDDP library](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-smddp-allgather.html): You can use the SageMaker model parallelism library v2 (SMP v2) in conjunction with the SageMaker distributed data parallelism (SMDDP) library that offers the AllGather collective communication operation optimized for AWS infrastructure.
- [Mixed precision training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-mixed-precision.html): The SageMaker model parallelism (SMP) library v2 supports mixed precision training out of the box by integrating with open source frameworks such as PyTorch FSDP and Transformer Engine.
- [Delayed parameter initialization](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-delayed-param-init.html): Initialization of a large model for training is not always possible with the limited GPU memory.
- [Activation checkpointing](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-pytorch-activation-checkpointing.html): Activation checkpointing is a technique to reduce memory usage by clearing activations of certain layers and recomputing them during the backward pass.
- [Activation offloading](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-pytorch-activation-offloading.html): Use activation offloading with activation checkpointing when the number of micro-batches is greater than one, and to further reduce memory usage.
- [Tensor parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-tensor-parallelism.html): Tensor parallelism is a type of model parallelism in which specific model weights, gradients, and optimizer states are split across devices.
- [Fine-tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-fine-tuning.html): Fine-tuning is a process of continuously training pre-trained models to improve performance for specific use cases.
- [FlashAttention](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-flashattention.html): SMP v2 supports FlashAttention kernels and makes it easy to apply them to various scenarios for Hugging Face Transformer models.
- [Checkpointing using SMP](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-checkpoints.html): The SageMaker model parallelism (SMP) library supports PyTorch APIs for checkpoints, and provides APIs that help checkpoint properly while using the SMP library.
- [Examples](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-model-parallel-v2-examples.html): Find examples of distributed training with Amazon SageMaker AI model parallelism (SMP) library v2.
- [Best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-best-practices-v2.html): Learn best practices for using the SageMaker model parallelism library in Amazon SageMaker AI.
- [SMP v2 reference](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-model-parallel-v2-reference.html): API reference for the SageMaker model parallel library v2
- [SMP release notes](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-release-notes.html): Track the latest updates for the SageMaker model parallelism library.

### [(Archived) SageMaker model parallelism library v1.x](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel.html)

Learn about how to use model parallel distributed training in Amazon SageMaker AI.

- [Introduction to Model Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-intro.html): Model parallelism is a distributed training method in which the deep learning model is partitioned across multiple devices, within or across instances.
- [Supported Frameworks and AWS Regions](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-model-parallel-support.html): Check supported frameworks and AWS Regions by the SageMaker model parallelism library.

### [Core Features](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features.html)

Learn about the core features of Amazon SageMaker AI's model parallelism library that offer distribution strategies and memory-saving techniques, such as sharded data parallelism, tensor parallelism, model partitioning by layers for pipeline scheduling, and checkpointing.

- [Sharded Data Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-sharded-data-parallelism.html): Use the SageMaker model parallelism library's sharded data parallelism to shard the training state of a model and reduce the per-GPU memory footprint of the model.
- [Pipelining a Model](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-pipieline-parallelism.html): Use pipeline parallelism to run training jobs in a pipelined fashion over microbatches and maximize GPU usage

### [Tensor Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-tensor-parallelism.html)

Tensor parallelism is a type of model parallelism in which specific model weights, gradients, and optimizer states are split across devices.

- [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-tensor-parallelism-how-it-works.html): Learn how tensor parallelism takes place at the level of nn.Modules.
- [Run a Training Job with Tensor Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-tensor-parallelism-examples.html): Learn how to run a SageMaker distributed training job using tensor parallelism.
- [Support for Hugging Face Transformer Models](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-hugging-face.html): Use the SageMaker model parallelism library's tensor parallelism for training the Hugging Face Transformer models: GPT-2, GPT-J, BERT, and RoBERTa.
- [Ranking Mechanism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-ranking-mechanism.html): With tensor parallelism, the library introduces three types of ranking and process group APIs: tensor parallel rank, pipeline parallel rank, and reduced-data parallel rank.
- [Optimizer State Sharding](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-optimizer-state-sharding.html): Optimizer state sharding is a useful memory-saving technique that shards the optimizer state across data parallel device groups.
- [Activation Checkpointing](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-activation-checkpointing.html): Activation checkpointing (or gradient checkpointing) is a technique to reduce memory usage by clearing activations of certain layers and recomputing them during a backward pass.
- [Activation Offloading](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-activation-offloading.html): Use activation offloading with activation checkpointing when the number of microbatches is greater than one, and to further reduce memory usage.
- [FP16 Training with Model Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-extended-features-pytorch-fp16.html): For FP16 training with model parallelism, make modifications in your training script and estimator.
- [Support for FlashAttention](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-attention-head-size-for-flash-attention.html): When distributing a Transformer model for model parallelism, adjust the attention head size to enable FlashAttention.

### [Run a SageMaker Distributed Training Job with Model Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-use-api.html)

Learn how to run a model-parallel training job of your own training script using the SageMaker Python SDK with the SageMaker model parallelism library.

### [Step 1: Modify Your Own Training Script](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-customize-training-script.html)

Learn how to customize your training script with Amazon SageMaker AI's model parallelism library-specific API functions and parameters.

- [TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-customize-training-script-tf.html): Modify your own TensorFlow training script to enable SageMaker distributed model parallelism.
- [PyTorch](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-customize-training-script-pt.html): Modify your own PyTorch training script to enable the SageMaker model parallelism library.
- [Step 2: Launch a Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-sm-sdk.html): Learn how to configure distribution options for the SageMaker model parallel library using the SageMaker Python SDK.
- [Checkpointing and Fine-Tuning a Model with Model Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-model-parallel-checkpointing-and-finetuning.html): Checkpoint models distributed by model parallelism techniques using the checkpoint APIs offered by the SageMaker model parallelism library.
- [Examples](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-model-parallel-examples.html): Find examples of distributed training with Amazon SageMaker AI model parallelism (SMP) library v1.
- [Best Practices](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-best-practices.html): Learn how to use model parallel distributed training in Amazon SageMaker AI.
- [Configuration Tips and Pitfalls](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-customize-tips-pitfalls.html): Review the following tips and pitfalls before using Amazon SageMaker AI's model parallelism library.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-troubleshooting-model-parallel.html): Troubleshooting information for distributed training in AWS Server Migration Service.
- [Distributed computing with SageMaker AI best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-options.html): Learn best practices for distributed training jobs and parallel processing jobs at scale with Amazon SageMaker AI.

### [Training Compiler](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler.html)

Compile deep learning (DL) models to achieve an improved training efficiency by using Amazon SageMaker Training Compiler.

- [Supported Frameworks, AWS Regions, Instance Types, and Tested Models](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-support.html): Check supported frameworks, AWS Regions, instances, and models by SageMaker Training Compiler.

### [Bring Your Own Deep Learning Model](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-modify-scripts.html)

Bring your own deep learning model to train with Amazon SageMaker Training Compiler.

- [PyTorch](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-pytorch-models.html): Use Amazon SageMaker Training Compiler to compile PyTorch models.
- [TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-tensorflow.html): Use Amazon SageMaker Training Compiler to compile TensorFlow models.

### [Enable Training Compiler](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-enable.html)

Use SageMaker Python SDK or API to enable SageMaker Training Compiler.

- [Run PyTorch Training Jobs with Training Compiler](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-enable-pytorch.html): Use SageMaker Python SDK or API to enable SageMaker Training Compiler.
- [Run TensorFlow Training Jobs with Training Compiler](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-enable-tensorflow.html): Use SageMaker Python SDK or API to enable SageMaker Training Compiler.
- [Example Notebooks and Blogs](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-examples-and-blogs.html): Use provided examples and reference blogs to learn how to use SageMaker Training Compiler.
- [Best Practices and Considerations](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-tips-pitfalls.html): Review tips and considerations when using SageMaker Training Compiler.
- [Training Compiler FAQ](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-faq.html): Use the FAQ items to find answers to commonly asked questions about SageMaker Training Compiler.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-troubleshooting.html): List to try to troubleshoot your training job.
- [Release Notes](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-release-notes.html): Track the latest updates for Amazon SageMaker Training Compiler.

### [Setting up training jobs to access datasets](https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data.html)

Learn about the different file input modes and AWS cloud storage options for your training dataset.

- [Configure data input mode using the SageMaker Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data-using-pysdk.html): Learn how to choose the data input mode using the SageMaker Python SDK.
- [Configure data input channel to use Amazon FSx for Lustre](https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data-fsx.html): Learn how to use Amazon FSx for Lustre as your data source for higher throughput and faster training by reducing the time for data loading.
- [Choosing an input mode and a storage unit](https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data-best-practices.html): Learn how to choose the optimal data input mode and storage for your use case.
- [Use attribute-based access control (ABAC) for multi-tenancy training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data-abac.html): Learn how SageMaker AI supports attribute-based access control (ABAC) to isolate each tenant's data and ensure accessibility only to authorized entities.

### [Mapping of training storage paths](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html)

Learn how the SageMaker training platform manages storage paths for training datasets, checkpoints, outputs, and model artifacts.

- [Uncompressed model output](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage-uncompressed.html): Leanr how to upload model and data outputs to your S3 bucket as uncompressed files.
- [Managing storage paths for different types of instance local storage](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage-tips-considerations.html): Learm more tips about setting up storage paths.
- [SageMaker AI environment variables and the default paths for training storage locations](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage-env-var-summary.html): Learn about the input and output paths for training datasets, checkpoints, model artifacts, and outputs, managed by the SageMaker training platform.

### [Heterogeneous clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/train-heterogeneous-cluster.html)

Learn how to train machine learning models on heterogeneous clusters in Amazon SageMaker AI.

- [Configure a training job with a heterogeneous cluster in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/train-heterogeneous-cluster-configure.html): Learn how to configure a heterogeneous cluster in Amazon SageMaker AI for training machine learning models.
- [Run distributed training on a heterogeneous cluster in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/train-heterogeneous-cluster-configure-distributed.html): Run distributed training on a heterogeneous cluster in Amazon SageMaker AI.
- [Modify your training script to assign instance groups](https://docs.aws.amazon.com/sagemaker/latest/dg/train-heterogeneous-cluster-modify-training-script.html): Learn how to modify your training script to assign instance groups of the heterogeneous cluster in Amazon SageMaker AI.
- [Use Incremental Training](https://docs.aws.amazon.com/sagemaker/latest/dg/incremental-training.html): Use incremental training in Amazon SageMaker AI to train variants of a model, resume a stopped model, or retrain a mode to improve its ability to generate inferences.

### [Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)

Use managed spot training to lower model training costs.

- [Managed Spot Training Lifecycle](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training-status.html): Monitoring the lifecycle of a managed spot training job.

### [Managed Warm Pools](https://docs.aws.amazon.com/sagemaker/latest/dg/train-warm-pools.html)

Reduce startup latency by retaining infrastructure for consecutive training jobs with SageMaker AI managed warm pools.

- [Request a warm pool quota increase](https://docs.aws.amazon.com/sagemaker/latest/dg/train-warm-pools-resource-limits.html): Request a service limit increase to start using SageMaker AI managed warm pools.
- [Use SageMaker AI managed warm pools](https://docs.aws.amazon.com/sagemaker/latest/dg/train-warm-pools-how-to-use.html): Learn how to set up Amazon SageMaker AI managed warm pools programmatically or through the SageMaker AI console.

### [CloudWatch Metrics for Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/training-metrics.html)

Use Amazon CloudWatch metrics to monitor and analyze Amazon SageMaker training jobs.

- [Define Training Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/define-train-metrics.html): Define the Amazon CloudWatch metrics that you want to monitor for your SageMaker training job.
- [View training job metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/view-train-metrics.html): View the metrics collected from your training job in the CloudWatch or SageMaker AI console.
- [Example: Viewing a Training and Validation Curve](https://docs.aws.amazon.com/sagemaker/latest/dg/train-valid-curve.html): Follow an example for viewing training and validation curves to analyze your model's performance after a Amazon SageMaker training job.

### [Augmented Manifest Files](https://docs.aws.amazon.com/sagemaker/latest/dg/augmented-manifest.html)

To include metadata with your dataset in a training job, use an augmented manifest file.

- [Augmented Manifest File Format for Pipe Mode Training](https://docs.aws.amazon.com/sagemaker/latest/dg/augmented-manifest-stream.html): Learn about how you can stream data with augmented manifest files.

### [Checkpoints in SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints.html)

Use checkpoints in Amazon SageMaker AI to save the state of models.

- [Enable checkpointing](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints-enable.html): Enable checkpointing using the SageMaker Python SDK.
- [Browse checkpoint files](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints-saved-file.html): Locate checkpoint files using the SageMaker Python SDK and the Amazon S3 console.
- [Resume training from a checkpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints-resume.html): Resume training from a checkpoint using the SageMaker Python SDK.
- [Cluster repairs for GPU errors](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints-cluster-repair.html): Learn about how Amazon SageMaker AI performs health checks and cluster repair for errors during training jobs.


## [Customizing models](https://docs.aws.amazon.com/sagemaker/latest/dg/customize-model.html)

### [Amazon Nova model customization](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model.html)

This topic has moved.

- [Amazon Nova recipes](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model-recipes.html): This topic has moved.

### [On SageMaker training jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model-training-job.html)

This topic has moved.

- [Distillation](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-distillation.html): This topic has moved.
- [Nova Customization SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-customization-sdk.html): The Amazon Nova Customization SDK is a comprehensive Python SDK for customizing Amazon Nova models across their entire lifecycleâfrom training and evaluation to deployment and inference.
- [Fine-tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-fine-tuning-training-job.html): This topic has moved.
- [Monitoring Progress Across Iterations](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model-monitor.html): This topic has moved.
- [Evaluation](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model-evaluation.html): This topic has moved.

### [On SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-hp.html)

This topic has moved.

- [Nova Customization SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-hp-customization-sdk.html): This topic has moved.
- [Essential Commands Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-hp-essential-commands-guide.html): This topic has moved.
- [HP cluster setup](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-hp-cluster.html): This topic has moved.
- [Nova Forge access and setup for SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-forge-hp-access.html): This topic has moved.
- [Training](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-hp-training.html): This topic has moved.
- [Fine-tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-hp-fine-tune.html): This topic has moved.
- [Evaluation](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-hp-evaluate.html): This topic has moved.
- [Iterative Training](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-iterative-training.html): Iterative training allows you to improve model performance through multiple training cycles, building on previous checkpoints to systematically address failure modes and adapt to changing requirements.
- [Amazon Bedrock inference](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model-bedrock-inference.html): This topic has moved.
- [Limitations](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model-limitations.html): This topic has moved.

### [Open weight model customization](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-open-weight.html)

This section walks you through the process to get started with open weight model customization.

- [Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-open-weight-prereq.html): Before you begin, complete the following prerequisites:
- [Creating assets for model customization in the UI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-open-weight-create-assets-ui.html): You can create and manage the dataset and evaluator assets that you can use for model customization in the UI.
- [AI model customization job submission](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-open-weight-job.html): The SageMaker AI model customization capability can be accessed from Amazon SageMaker Studioâs Models page in the left hand panel.

### [Model evaluation job submission](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-open-weight-evaluation.html)

This section describes open-weight custom model evaluation.

- [Getting Started](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-evaluation-getting-started.html)
- [Evaluation types and Job Submission](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-evaluation-types.html)
- [Evaluation Metrics Formats](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-evaluation-metrics-formats.html): Evaluating the quality of your model across these metric formats:
- [Supported Dataset Formats for Bring-Your-Own-Dataset (BYOD) Tasks](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-evaluation-dataset-formats.html): The Custom Scorer and LLM-as-judge evaluation types require a custom dataset JSONL file located in AWS S3.
- [Evaluate with Preset and Custom Scorers](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-evaluation-preset-custom-scorers.html): When using the Custom Scorer evaluation type, SageMaker Evaluation supports two built-in scorers (also referred to as "reward functions") Prime Math and Prime Code taken from the volcengine/verl RL training library, or your own custom scorer implemented as a Lambda Function.
- [Model deployment](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-open-weight-deployment.html): From the custom models details page you can also deploy your custom model using either SageMaker AI Inference endpoints or Amazon Bedrock.
- [Sample datasets and evaluators](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-open-weight-samples.html)
- [Release note](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-release-note.html): The SageMaker AI model customization images


## [Deploy models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)

- [Model Deployment](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html): Learn more about how to deploy a model in Amazon SageMaker AI and get predictions after training your model.

### [Options for deploying models and getting inferences](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-get-started.html)

Learn more about the various options for deploying models and getting inference in SageMaker AI.

- [Inference options](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html): Choose the inference option that best suits your workload.
- [Advanced endpoint options](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-advanced.html): Use advanced endpoint options to optimize inference performance and cost.
- [Next steps](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-next-steps.html): Use features in SageMaker AI to improve your inference workflow.
- [Model creation with ModelBuilder](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-modelbuilder-creation.html): Learn how to use the SageMaker AI ModelBuilder to prepare your model for deployment.

### [Inference optimization](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html)

Run optimization jobs in SageMaker AI to improve the performance of your models.

- [Deploy a pre-optimized model](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-preoptimized.html): Learn how to deploy pre-optimized version of SageMaker JumpStart models.
- [Create an optimization job](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-create-job.html): Use inference optimization jobs to optimize the performance of your generative AI models.
- [View the optimization job results](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-view-results.html): View the results of your inference optimization jobs in Amazon SageMaker Studio.
- [Evaluate performance](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-evaluate.html): Evaluate your model's performance after running an inference optimization job.
- [Supported models reference](https://docs.aws.amazon.com/sagemaker/latest/dg/optimization-supported-models.html): Look up the models that you can optimize in SageMaker AI, and look up the supported optimization techniques.
- [Options for evaluating your model](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-model-validation.html): After training a model, evaluate it to determine whether its performance and accuracy enable you to achieve your business goals.

### [Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)

Inference recommendation and load balancing testing with Amazon SageMaker Inference Recommender.

- [Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-prerequisites.html): Describes the prerequisites you must satisfy before you can use Amazon SageMaker Inference Recommender and provides instructions on how to satisfy the requirements.

### [Recommendation jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-recommendation-jobs.html)

High-level description of the two types of recommendation jobs Amazon SageMaker Inference Recommender can make.

- [Get instant prospective instances](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-prospective.html): Learn how to view prospective instances for your Amazon SageMaker AI model.

### [Inference recommendations](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-instance-recommendation.html)

Describes how to create, get results, and stop inference recommendation jobs with AWS SDK for Python (Boto3), AWS CLI, and Amazon SageMaker Studio Classic.

- [Create an inference recommendation](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-recommendation-create.html): Instructions on how to create your inference recommendation job.
- [Get your inference recommendation job results](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-recommendation-results.html): Instructions on how to get your inference recommendation job results.
- [Get an inference recommendation for an existing endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-existing-endpoint.html): Describes how to run an inference recommendation job for an existing SageMaker AI Inference endpoint.
- [Stop your inference recommendation](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-recommendation-stop.html): Stop an inference recommendation that is currently running.
- [Compiled recommendations with Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-neo-compilation.html): Describes how to get endpoint recommendations that include Neo compilation, which can help optimize your model.
- [Recommendation results](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-interpret-results.html): Describes how to interpret the results of your Inference Recommender job.
- [Get autoscaling policy recommendations](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-autoscaling.html): With Amazon SageMaker Inference Recommender, you can get recommendations for autoscaling policies for your SageMaker AI endpoint based on your anticipated traffic pattern.
- [Run a custom load test](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-load-test.html): Learn how to create custom load test jobs, get results, and stop custom load test jobs with AWS SDK for Python (Boto3), AWS CLI, Amazon SageMaker Studio Classic, and the SageMaker AI console.
- [Stop your load test](https://docs.aws.amazon.com/sagemaker/latest/dg/load-test-stop.html): Stop a load test that is currently running.
- [Troubleshoot Inference Recommender errors](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-troubleshooting.html): This section contains information about how to understand and prevent common errors, the error messages they generate, and guidance on how to resolve these errors.

### [Real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)

Real-time inference is ideal for inference workloads where you have real-time, interactive, low latency requirements.

- [Deploy models](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-deploy-models.html): Learn how to deploy your machine learning models for real-time inference using SageMaker AI hosting services.
- [Invoke models](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-test-endpoints.html): Learn about how to invoke models for real-time inference and how to test your endpoints using Amazon SageMaker Studio, the AWS SDKs, or the AWS CLI.

### [Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-manage.html)

Learn how to view, monitor, and manage your SageMaker AI endpoints.

### [View endpoint details in SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-studio.html)

In Amazon SageMaker Studio, you can view and manage your SageMaker AI Hosting endpoints.

- [View Variants (or Models)](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-studio-variants.html): The Variants tab (also called the Models tab if your endpoint has multiple models deployed) shows you the list of model variants or models currently deployed to your endpoint.
- [View settings](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-studio-settings.html): On the Settings tab, you can view the endpointâs associated AWS IAM role, the AWS KMS key used for encryption (if applicable), the name of your VPC, and the network isolation settings.
- [Test inference](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-studio-test.html): On the Test inference tab, you can send a test inference request to a deployed model.
- [Auto-scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-studio-autoscaling.html): On the Auto-scaling tab, you can view any auto-scaling policies configured for the models hosted on your endpoint.

### [View endpoint details in the SageMaker AI console](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-console.html)

To view your endpoints in the SageMaker AI console, do the following:

- [Endpoints monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-console-monitoring.html): After creating a SageMaker AI Hosting endpoint, you can monitor your endpoint using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Settings](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-console-settings.html): You can choose the Settings tab to view additional information about your endpoint, such as the data capture settings, the endpoint configuration, and tags.
- [Create and view alarms](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-console-alarms.html): From the Alarms tab on your endpoint details page, you can view and create simple static threshold metric alarms, where you specify a threshold value for a metric.

### [Hosting options](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-options.html)

The following topics describe available SageMaker AI realtime hosting options along with how to set up, invoke, and delete each hosting option.

- [Single-model endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-single-model.html): You can create, update, and delete real-time inference endpoints that host a single model with Amazon SageMaker Studio, the AWS SDK for Python (Boto3), the SageMaker Python SDK, or the AWS CLI.

### [Multi-model endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)

Create an endpoint that can host multiple Amazon SageMaker AI models to help reduce cost.

- [Supported algorithms, frameworks, and instances for multi-model endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-support.html): For information about the algorithms, frameworks, and instance types that you can use with multi-model endpoints, see the following sections.
- [Instance recommendations for multi-model endpoint deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoint-instance.html): Learn about the considerations for choosing an instance type for your Amazon SageMaker AI multi-model endpoint.
- [Create a Multi-Model Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/create-multi-model-endpoint.html): Create and deploy a Amazon SageMaker AI multi-model endpoint.
- [Invoke a Multi-Model Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/invoke-multi-model-endpoint.html): Invoke an Amazon SageMaker AI multi-model endpoint with the TargetModel parameter.
- [Add or Remove Models](https://docs.aws.amazon.com/sagemaker/latest/dg/add-models-to-endpoint.html): Dynamically deploy an Amazon SageMaker AI model to a multi-model endpoint or remove a model from the endpoint.

### [Bring Your Own Container](https://docs.aws.amazon.com/sagemaker/latest/dg/build-multi-model-build-container.html)

Build Your Own Container and use it to deploy models with SageMaker AI multi-model endpoints.

- [API Container Contract](https://docs.aws.amazon.com/sagemaker/latest/dg/mms-container-apis.html): APIs and error behaviors needed to handle multiple models at an endpoint.
- [Security](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoint-security.html): Using IAM roles to manage access to Amazon SageMaker AI multi-model endpoint resources.
- [CloudWatch Metrics for Multi-Model Endpoint Deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoint-cloudwatch-metrics.html): Amazon SageMaker AI provides metrics for endpoints so you can monitor the cache hit rate, the number of models loaded and the model wait times for loading, downloading, and uploading at a multi-model endpoint.
- [Set SageMaker AI multi-model endpoint model caching behavior](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-caching.html): Learn about Amazon SageMaker AI multi-model endpoints caching behavior and how to modify it.
- [Set Auto Scaling Policies for Multi-Model Endpoint Deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints-autoscaling.html): SageMaker AI multi-model endpoints fully support automatic scaling, which manages replicas of models to ensure models scale based on traffic patterns.

### [Multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html)

Learn about Amazon SageMaker AI multi-container endpoints.

- [Create a multi-container endpoint (Boto 3)](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-create.html): Learn how to create an Amazon SageMaker AI multi-container endpoint.
- [Update a multi-container endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-update.html): Learn how to update your models and endpoint configuration on an Amazon SageMaker AI multi-container endpoint.
- [Invoke a multi-container endpoint with direct invocation](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-direct.html): Learn how to invoke multiple models hosted on an Amazon SageMaker AI multi-container endpoint.
- [Security with multi-container endpoints with direct invocation](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-security.html): Learn about how to secure your containers for multi-container endpoints on Amazon SageMaker AI.
- [Metrics for multi-container endpoints with direct invocation](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-metrics.html): Learn about the Amazon CloudWatch metrics you can use to monitor your Amazon SageMaker AI multi-container endpoints.
- [Autoscale multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-auto-scaling.html): Configure autoscaling for your Amazon SageMaker AI multi-container endpoint.
- [Troubleshoot multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-troubleshooting.html): Learn about how to deal with common errors you might encounter with Amazon SageMaker AI multi-container endpoints.

### [Inference pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html)

Use inference pipelines in Amazon SageMaker AI for real-time and batch transform requests.

- [Process Features with Spark ML and Scikit-learn](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-mleap-scikit-learn-containers.html): Build Apache Spark ML and scikit-learn containers for feature engineering in Amazon SageMaker AI.
- [Create a Pipeline Model](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-create-console.html): Create an inference pipeline model with the Amazon SageMaker AI console.
- [Real-time Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-real-time.html): Use an Amazon SageMaker AI endpoint for real-time inference with an inference pipeline.
- [Batch transforms](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-batch.html): Use the Amazon SageMaker SDK to perform batch transforms with Inference Pipelines in SageMaker AI.
- [Logs and Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-logs-metrics.html): Learn how to use logs and metrics for Inference Pipelines in Amazon SageMaker AI.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-troubleshoot.html): Troubleshoot Pipelines
- [Delete Endpoints and Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-delete-resources.html): Delete endpoints to stop incurring charges.

### [Automatic scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)

Automatically scale Amazon SageMaker AI models in response to changes in workload.

- [Auto scaling policy overview](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-policy.html): Learn about auto scaling policies for Amazon SageMaker AI inference endpoints.
- [Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-prerequisites.html): Before you can use auto scaling, you must have already created an Amazon SageMaker AI model endpoint.
- [Configure model auto scaling with the console](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-add-console.html): Learn how to configure your deployed model for auto scaling using the AWS Management Console.
- [Register a model](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-add-policy.html): Learn how to register your model for auto scaling using the AWS Command Line Interface or Application Auto Scaling API.
- [Define a scaling policy](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-add-code-define.html): Learn how to configure metrics for a target tracking scaling policy using the AWS Command Line Interface or Application Auto Scaling API.
- [Apply a scaling policy](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-add-code-apply.html): Learn how to apply a scaling policy using the AWS Command Line Interface or Application Auto Scaling API.
- [Instructions for editing a scaling policy](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-edit.html): Learn how to edit a scaling policy using the AWS Management Console, AWS Command Line Interface, or Application Auto Scaling API.
- [Temporarily turn off scaling policies](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-suspend-scaling-activities.html): Learn how to temporarily turn off scaling policies.
- [Delete a scaling policy](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-delete.html): Learn how to delete a scaling policy with the AWS Management Console, AWS Command Line Interface, or Application Auto Scaling API.
- [Check the status of a scaling activity](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-query-history.html): Learn how to check the status of a scaling activity for your auto scaled endpoint by describing scaling activities.
- [Scale an endpoint to zero instances](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-zero-instances.html): Save costs by automatically scaling your SageMaker AI endpoint to zero instances during periods with no incoming inference requests.
- [Load testing](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html): Test your auto scaled endpoint with load testing.
- [Use CloudFormation to create a scaling policy](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-cloudformation.html): Code example for auto scaling an endpoint using Application Auto Scaling.
- [Update endpoints that use auto scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-update.html): Learn how to update endpoints with Application Auto Scaling.
- [Delete endpoints configured for auto scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-delete-with-scaling.html): Learn how to delete endpoints with Application Auto Scaling.
- [Instance storage volumes](https://docs.aws.amazon.com/sagemaker/latest/dg/host-instance-storage.html): This table shows the size of storage volumes attached to each instance type.

### [Validation of models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/model-validation.html)

Validate models in production with production and shadow variants.

- [Testing models with production variants](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html): In production ML workflows, data scientists and engineers frequently try to improve performance using various methods, such as , training on additional or more-recent data, improving feature selection, using better updated instances and serving containers.
- [Testing models with shadow variants](https://docs.aws.amazon.com/sagemaker/latest/dg/model-shadow-deployment.html): You can use SageMaker AI Model Shadow Deployments to create long running shadow variants to validate any new candidate component of your model serving stack before promoting it to production.

### [Online explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability.html)

Learn how to configure online explainability with SageMaker Clarify to analyze explainability in a deployed model.

- [Pre-check the model container](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-precheck.html): Learn how to pre-check the model container inputs and outputs for compatibility before you configure an endpoint.

### [Configure and create an endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html)

Learn how to configure and create an endpoint to fit your model.

- [The EnableExplanations expression](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint-enable.html): The EnableExplanations parameter is a JMESPath Boolean expression string.
- [Synthetic dataset](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint-synthetic.html): SageMaker Clarify uses the Kernel SHAP algorithm.
- [Invoke the endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html): Use API in the SageMaker Clarify explainer to send requests to, or invoke, the endpoint.
- [Code examples: SDK for Python](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-examples.html): Code examples to create and invoke the endpoint using the Python SDK.
- [Troubleshooting guide](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-troubleshooting.html): Troubleshooting guide for errors and unsupported endpoint functionalities when using SageMaker Clarify for online explainability.
- [Fine-tune with adapters](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-adapt.html): Apply LoRA adapters to your SageMaker AI models to fine-tune them for your unique customers, tasks, or domains.

### [Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)

Deploy and scale ML models without configuring or managing any of the underlying infrastructure with Amazon SageMaker Serverless Inference.

### [Serverless endpoint operations](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create-invoke-update-delete.html)

The following guide shows you the key capabilities of serverless endpoints.

- [Complete the prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-prerequisites.html): Before creating a serverless endpoint, you must complete the following prerequisites.

### [Serverless endpoint creation](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create.html)

To create a serverless endpoint, create a model, an endpoint configuration, and finally the endpoint.

- [Create a model](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create-model.html): To create your model, you must provide the location of your model artifacts and container image.
- [Create an endpoint configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create-config.html): After you create a model, create an endpoint configuration.
- [Create an endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create-endpoint.html): To create a serverless endpoint, you can use the Amazon SageMaker AI console, the CreateEndpoint API, or the AWS CLI.
- [Invoke a serverless endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-invoke.html): To invoke a serverless endpoint, you must make an HTTP request to the endpoint.
- [Update a serverless endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-update.html): To update a serverless endpoint, create a new endpoint configuration and then update the endpoint using either the console or the APIs.
- [Describe a serverless endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-describe.html): To see information about your serverless endpoint, you can use the APIs or the console.
- [Delete a serverless endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-delete.html): You can delete your serverless endpoint using the APIs or the console.
- [Alarms and logs](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-monitoring.html): You can configure Amazon CloudWatch alarms and logs to collect metrics from and monitor your serverless endpoint.

### [Automatically scale Provisioned Concurrency for a serverless endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-autoscale.html)

Learn how to autoscale the Provisioned Concurrency for a serverless endpoint based on either a target metric or a schedule.

- [Clean up](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-autoscale-cleanup.html): After you have finished using autoscaling for your serverless endpoint with Provisioned Concurrency, you should clean up the resources you created.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-troubleshooting.html): Troubleshooting help for Serverless Inference

### [Asynchronous inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)

Use Asynchronous Inference to queue incoming inference requests and process them asynchronously.

### [Asynchronous endpoint operations](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-create-invoke-update-delete.html)

Use this page to learn how to create, invoke, and update an asynchronous endpoint.

- [Complete the prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-create-endpoint-prerequisites.html): The following topic describes the prerequisites that you must complete before creating an asyncrhonous endpoint.

### [Create](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-create-endpoint.html)

Learn how to create an Asynchronous Inference Endpoint.

- [Create a Model](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-create-endpoint-create-model.html): Learn how to create a model for the Asynchronous Inference Endpoint.
- [Create an Endpoint Configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-create-endpoint-create-endpoint-config.html): Learn how to configure the Asynchronous Inference Endpoint.
- [Create Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-create-endpoint-create-endpoint.html): Learn how to create the Asynchronous Inference Endpoint.
- [Invoke](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-invoke-endpoint.html): Get inferences from the model hosted at your asynchronous endpoint with InvokeEndpointAsync.
- [Update](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-update-endpoint.html): Update an asynchronous endpoint with the UpdateEndpoint API.
- [Delete](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-delete-endpoint.html): Delete an asynchronous endpoint in a similar manner to how you would delete a SageMaker AI hosted endpoint with the DeleteEndpoint API.
- [Alarms and logs](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-monitor.html): Use this page to learn what metrics are applicable to SageMaker AI Asynchronous Endpoints.
- [Check prediction results](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-check-predictions.html): Use this page to learn how to check the output of your predictions from your asynchronous endpoints.
- [Autoscale an asynchronous endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-autoscale.html): Use this page to get a high-level overview of how autoscaling works.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-troubleshooting.html): Troubleshoot your Asynchronous Inference endpoints with the following information.

### [Batch transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html)

Use a batch transform job to get inferences for an entire dataset, when you don't need a persistent endpoint, or to preprocess datasets to remove noise or bias.

- [Associate Prediction Results with Input](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html): Use Amazon SageMaker AI batch transform to associate inputs with prediction results.
- [Storage in Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-storage.html): Amazon SageMaker AI batch transform attaches a storage volume to the instances that run your job.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-errors.html): Learn how to troubleshoot issues with Amazon SageMaker AI Batch Transform jobs.

### [Model parallelism and large model inference](https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference.html)

Using SageMaker AI for large model inference.

- [The LMI container documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference-container-docs.html): Learn how to deploy and optimize large language models on Amazon SageMaker AI using Large Model Inference (LMI) containers.
- [SageMaker AI endpoint parameters for LMI](https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference-hosting.html): Customize SageMaker AI endpoint parameters for large model inference to reduce latency.
- [Deploying uncompressed models](https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference-uncompressed.html): Deploying uncompressed models with SageMaker AI Hosting for faster large model inference
- [Deploy large models for inference with TorchServe](https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference-tutorials-torchserve.html): Learn how to deploy large models to a SageMaker AI Hosting endpoint with TorchServe.

### [Deployment guardrails](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html)

If you want to update a model that you've deployed to production, you can use deployment guardrails.

- [Auto-Rollback Configuration and Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-configuration.html): You can use Amazon CloudWatch alarms to monitor your fleets while using deployment guardrails.

### [Blue/Green Deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green.html)

Blue/green deployments provide you with the ability to roll out an update to a new fleet (green fleet) while your old fleet (blue fleet) is still active.

- [Use all at once traffic shifting](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green-all-at-once.html): All at once traffic shifting mode enables you to roll out a blue/green update to your endpoint while taking advantage of safety guardrails, such as auto-rollbacks, to protect your endpoint.
- [Use canary traffic shifting](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green-canary.html): Canary traffic shifting mode enables you to roll out a blue/green update to your endpoint while taking advantage of safety guardrails, such as auto-rollbacks, to protect your endpoint.
- [Use linear traffic shifting](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green-linear.html): Linear traffic shifting mode enables you to roll out a blue/green update to your endpoint while taking advantage of safety guardrails, such as auto-rollbacks, to protect your endpoint.
- [Use rolling deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-rolling.html): Rolling deployments provide you with the ability to incrementally roll out an update to a new fleet.
- [Exclusions](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-exclusions.html): Deployment guardrails do not support all endpoint features.

### [Shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html)

Learn about shadow tests and when to use them.

- [Create a shadow test](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-create.html): Create a Amazon SageMaker AI shadow test to compare operational metrics on your variants.

### [How to view, monitor, and edit shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit.html)

View, monitor and edit shadow tests through the SageMaker AI console.

- [View shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit-list.html): View all shadow tests on the SageMaker AI console.
- [Monitor a shadow test](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit-dashboard.html): Monitor a shadow test on the dashboard.
- [Start a shadow test early](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit-start.html): You can start your test before its scheduled start time.
- [Delete a shadow test](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit-delete.html): You can delete a test that you no longer need.
- [Edit a shadow test](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit-individual.html): You can modify both scheduled and in-progress tests.
- [Complete a shadow test](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-complete.html): Complete a shadow test early.
- [Best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-best-practices.html): Best practices for running shadow tests with Amazon SageMaker AI inference experiments.
- [Access containers through SSM](https://docs.aws.amazon.com/sagemaker/latest/dg/ssm-access.html): Shows how to access Docker containers with AWS Systems Manager (SSM).

### [Model servers](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-frameworks.html)

Learn how to deploy your ML models on SageMaker AI with popular model servers, such as TorchServe, DJL Serving, and Triton Inference Server.

- [Deploy models with TorchServe](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-models-frameworks-torchserve.html): Deploy your model with the TorchServe model server on SageMaker AI.
- [Deploy models with DJL Serving](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-models-frameworks-djl-serving.html): Deploy your model with the DJL Serving model server on SageMaker AI.
- [Model deployment with Triton Inference Server](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-models-frameworks-triton.html): Deploy your model with the Triton Inference Server on SageMaker AI.

### [Model deployment at the edge](https://docs.aws.amazon.com/sagemaker/latest/dg/edge.html)

### [First Steps](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-manager-getting-started.html)

This guide demonstrates how to complete the necessary steps to register, deploy, and manage a fleet of devices, and how to satisfy Amazon SageMaker AI Edge Manager prerequisites.

- [Setting Up](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-getting-started-step1.html): Before you begin using SageMaker Edge Manager to manage models on your device fleets, you must first create IAM Roles for both SageMaker AI and AWS IoT.
- [Prepare Your Model for Deployment](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-getting-started-step2.html): In this section you will create SageMaker AI and AWS IoT client objects, download a pre-trained machine learning model, upload your model to your Amazon S3 bucket, compile your model for your target device with SageMaker Neo, and package your model so that it can be deployed with the Edge Manager agent.
- [Register and Authenticate Your Device Fleet](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-getting-started-step3.html): In this section you will create your AWS IoT thing object, create a device fleet, register your device fleet so it can interact with the cloud, create X.509 certificates to authenticate your devices to AWS IoT Core, associate the role alias with AWS IoT that was generated when you created your fleet, get your AWS account-specific endpoint for the credentials provider, get an official Amazon Root CA file, and upload the Amazon CA file to Amazon S3.
- [Download and Set Up Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-getting-started-step4.html): The Edge Manager agent is an inference engine for your edge devices.
- [Run Agent](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-getting-started-step5.html): In this section you will run the agent as a binary using gRPC, and check that both your device and fleet are working and collecting sample data.

### [Setup for Devices and Fleets](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet.html)

Fleets are collections of logically grouped devices you can use to collect and analyze data.

- [Create a Fleet](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet-create.html): You can create a fleet programmatically with the AWS SDK for Python (Boto3) or through the SageMaker AI console https://console.aws.amazon.com/sagemaker.
- [Register a Device](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet-register.html)
- [Check Status](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet-check-status.html): Check that your device or fleet is connected and sampling data.

### [How to Package Model](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-packaging-job.html)

How to package a model.

- [Complete prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-packaging-job-prerequisites.html): Prerequisites to package a model.
- [Package a Model (Amazon SageMaker AI Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-packaging-job-console.html): Learn how to package a model in the Amazon SageMaker AI console.
- [Package a Model (Boto3)](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-packaging-job-boto3.html): Learn how to package a model using AWS SDK for Python (Boto3).

### [The Edge Manager Agent](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet-about.html)

Describes how to do deploy jobs to edge devices.

- [Download and Set Up the Edge Manager Agent Manually](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet-manual.html): Download the Edge Manager agent based on your operating system, architecture, and AWS Region.

### [Model Package and Edge Manager Agent Deployment with AWS IoT Greengrass](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-greengrass.html)

SageMaker Edge Manager integrates AWS IoT Greengrass version 2 to simplify accessing, maintaining, and deploying the Edge Manager agent and model to your devices.

- [Complete prerequisites to deploy the Edge Manager agent](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-greengrass-prerequisites.html): Learn about the prerequisites needed to deploy the Edge Manager agent using AWS IoT Greengrass V2, as well as the steps needed to complete the prerequisites.
- [Create the AWS IoT Greengrass V2 Components](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-greengrass-custom-component.html): AWS IoT Greengrass uses components, a software module that is deployed to and runs on a AWS IoT Greengrass core device.
- [Deploy the components to your device](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-greengrass-deploy-components.html): Deploy your components with the AWS IoT console or with the AWS CLI.
- [Deploy the Model Package Directly with SageMaker Edge Manager Deployment API](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-deployment-plan-api.html): SageMaker Edge Manager provides a deployment API that you can use to deploy models to device targets without AWS IoT Greengrass.
- [Manage Model](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-manage-model.html): The Edge Manager agent can load multiple models at a time and make inference with loaded models on edge devices.
- [SageMaker Edge Manager end of life](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html): End-of-life documentation for Amazon SageMaker Edge Manager.

### [Model optimization with Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)

Neo is a capability of Amazon SageMaker AI that enables machine learning models to train once and run anywhere in the cloud and at the edge.

### [Compile Models](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-job-compilation.html)

Compile Models

- [Prepare Model for Compilation](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-compilation-preparing-model.html): SageMaker Neo requires machine learning models to satisfy specific input data shapes.
- [Compile Models: CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-job-compilation-cli.html): How to manage compilation jobs with the CLI.
- [Compile Models: Console](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-job-compilation-console.html): You can create an Amazon SageMaker Neo compilation job in the Amazon SageMaker AI console.
- [Compile Models: SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-job-compilation-sagemaker-sdk.html): You can use the compile_model API in the Amazon SageMaker AI SDK for Python to compile a trained model and optimize it for specific target hardware.

### [Cloud Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-cloud-instances.html)

Amazon SageMaker Neo provides compilation support for popular machine learning frameworks such as TensorFlow, PyTorch, MXNet, and more.

- [Supported Instance Types and Frameworks](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-supported-cloud.html): Amazon SageMaker Neo supports popular deep learning frameworks for both compilation and deployment.

### [Deploy a Model](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-deployment-hosting-services.html)

To deploy an Amazon SageMaker Neo-compiled model to an HTTPS endpoint, you must configure and create the endpoint for the model using Amazon SageMaker AI hosting services.

- [Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-deployment-hosting-services-prerequisites.html)
- [Deploy a Compiled Model Using SageMaker SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-deployment-hosting-services-sdk.html): You must satisfy the prerequisites section if the model was compiled using AWS SDK for Python (Boto3), AWS CLI, or the Amazon SageMaker AI console.
- [Deploy a Compiled Model Using Boto3](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-deployment-hosting-services-boto3.html): You must satisfy the prerequisites section if the model was compiled using AWS SDK for Python (Boto3), AWS CLI, or the Amazon SageMaker AI console.
- [Deploy a Compiled Model Using the AWS CLI](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-deployment-hosting-services-cli.html): You must satisfy the prerequisites section if the model was compiled using AWS SDK for Python (Boto3), AWS CLI, or the Amazon SageMaker AI console.
- [Deploy a Compiled Model Using the Console](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-deployment-hosting-services-console.html): You must satisfy the prerequisites section if the model was compiled using AWS SDK for Python (Boto3), the AWS CLI, or the Amazon SageMaker AI console.

### [Request Inferences](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-requests.html)

If you have followed instructions in , you should have a SageMaker AI endpoint set up and running.

- [Request Inferences from a Deployed Service (Amazon SageMaker SDK)](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-requests-sdk.html): Use the following the code examples to request inferences from your deployed service based on the framework you used to train your model.
- [Request Inferences from a Deployed Service (Boto3)](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-requests-boto3.html): You can submit inference requests using SageMaker AI SDK for Python (Boto3) client and invoke_endpoint() API once you have an SageMaker AI endpoint InService.
- [Request Inferences from a Deployed Service (AWS CLI)](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-requests-cli.html): Inference requests can be made with the sagemaker-runtime invoke-endpoint once you have an Amazon SageMaker AI endpoint InService.
- [Inference Container Images](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-deployment-hosting-services-container-images.html): SageMaker Neo now provides inference image URI information for ml_* targets.

### [Edge Devices](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-edge-devices.html)

Amazon SageMaker Neo provides compilation support for popular machine learning frameworks.

### [Supported Frameworks, Devices, Systems, and Architectures](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-supported-devices-edge.html)

Amazon SageMaker Neo supports common machine learning frameworks, edge devices, operating systems, and chip architectures.

- [Supported Frameworks](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-supported-devices-edge-frameworks.html): Amazon SageMaker Neo supports the following frameworks.
- [Supported Devices, Chip Architectures, and Systems](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-supported-devices-edge-devices.html): Amazon SageMaker Neo supports the following devices, chip architectures, and operating systems.
- [Tested Models](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-supported-edge-tested-models.html): The following collapsible sections provide information about machine learning models that were tested by the Amazon SageMaker Neo team.
- [Deploy Models](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-deployment-edge.html): You can deploy the compute module to resource-constrained edge devices by: downloading the compiled model from Amazon S3 to your device and using DLR, or you can use AWS IoT Greengrass.

### [Set up Neo on Edge Devices](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-getting-started-edge.html)

This guide to getting started with Amazon SageMaker Neo shows you how to compile a model, set up your device, and make inferences on your device.

- [Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-getting-started-edge-step0.html): SageMaker Neo is a capability that allows you to train machine learning models once and run them anywhere in the cloud and at the edge.
- [Compile the Model](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-getting-started-edge-step1.html): Once you have satisfied the Prerequisites, you can compile your model with Amazon SageMaker AI Neo.
- [Set Up Your Device](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-getting-started-edge-step2.html): You will need to install packages on your edge device so that your device can make inferences.
- [Make Inferences on Your Device](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-getting-started-edge-step3.html): In this example, you will use Boto3 to download the output of your compilation job onto your edge device.

### [Troubleshoot Errors](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-troubleshooting.html)

Troubleshoot Neo compilation errors in Amazon SageMaker AI.

- [Troubleshoot Neo Compilation Errors](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-troubleshooting-compilation.html): This section contains information about how to understand and prevent common compilation errors, the error messages they generate, and guidance on how to resolve these errors.
- [Troubleshoot Neo Inference Errors](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-troubleshooting-inference.html): This section contains information about how to prevent and resolve some of the common errors you might encounter upon deploying and/or invoking the endpoint.
- [Troubleshoot Ambarella Errors](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-troubleshooting-target-devices-ambarella.html): SageMaker Neo requires models to be packaged in a compressed TAR file (*.tar.gz).
- [Stateful sessions](https://docs.aws.amazon.com/sagemaker/latest/dg/stateful-sessions.html): Learn how you can use Amazon SageMaker AI to send your inference requests to a session with a stateful model.

### [Best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practices.html)

Best practices for deploying Amazon SageMaker AI machine learning models.

- [Best practices for deploying models on SageMaker AI Hosting Services](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html): When hosting models using SageMaker AI hosting services, consider the following:
- [Monitor Security Best Practices](https://docs.aws.amazon.com/sagemaker/latest/dg/monitor-sec-best-practices.html): Learn about how you can monitor the securirty best practices for deploying Amazon SageMaker AI machine learning models.
- [Low latency real-time inference with AWS PrivateLink](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-privatelink.html): Deploy AWS PrivateLink.
- [Migrate inference workload from x86 to AWS Graviton](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-graviton.html): Provide ARM compatible model image.
- [Troubleshoot deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-troubleshoot.html): Learn how to troubleshoot Amazon SageMaker AI machine learning models deployments.
- [Inference cost optimization best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-cost-optimization.html): The following content provides techniques and considerations for optimizing the cost of endpoints.
- [Best practices to minimize interruptions during GPU driver upgrades](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-gpu-drivers.html): SageMaker AI Model Deployment upgrades GPU drivers on the ML instances for Real-time, Batch, and Asynchronous Inference options over time to provide customers access to improvements from the driver providers.
- [Best practices for endpoint security](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practice-endpoint-security.html): To address the latest security issues, Amazon SageMaker AI automatically patches endpoints to the latest and most secure software.
- [Updating containers for the NVIDIA Container Toolkit](https://docs.aws.amazon.com/sagemaker/latest/dg/container-nvidia-compliance.html): As of versions 1.17.4 and higher, the NVIDIA Container Toolkit no longer mounts CUDA compatibility libraries automatically.
- [Supported features](https://docs.aws.amazon.com/sagemaker/latest/dg/model-deploy-feature-matrix.html): Learn about the core platform features supported by each inference option.

### [Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-resources.html)

Use the following resources for troubleshooting and reference, answerings FAQS, and learning more about Amazon SageMaker AI Inference.

- [Blogs, example notebooks, and additional resources](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-blogs.html): The following sections contain examples and additional resources for you to learn more about Amazon SageMaker AI.
- [Troubleshooting and reference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-reference.html): You can use the following resources and reference documentation to understand best practices when using SageMaker AI Inference and to troubleshoot issues with model deployments:
- [Model Hosting FAQs](https://docs.aws.amazon.com/sagemaker/latest/dg/hosting-faqs.html): FAQs for SageMaker Inference Hosting, including all of the inference options.


## [Implement MLOps](https://docs.aws.amazon.com/sagemaker/latest/dg/mlops.html)

- [Why MLOps?](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-why.html): MLOps is the discipline of integrating ML workloads into release management, CI/CD, and operations.
- [Experiments](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments-mlops.html): Learn about Amazon SageMaker Experiments in MLOps.

### [Workflows](https://docs.aws.amazon.com/sagemaker/latest/dg/workflows.html)

Learn about Amazon SageMaker AI Workflows services.

### [ML Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)

Learn more about Amazon SageMaker Pipelines.

### [Pipelines overview](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-overview.html)

An Amazon SageMaker Pipelines pipeline is a series of interconnected steps that is defined by a JSON pipeline definition.

- [Structure and Execution](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-pipeline.html): Amazon SageMaker Pipelines structure and execution
- [Access Management](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-access.html): AWS Identity and Access Management (IAM) requirements for Amazon SageMaker Pipelines
- [Set up cross-account support](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-xaccount.html): Access pipeline entities from another AWS account.
- [Pipeline parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-parameters.html): How to reference parameters that you define throughout your pipeline definition.

### [Pipelines Steps](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html)

Describes the step types in Amazon SageMaker Pipelines.

- [Add a step](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps-types.html): Describes the step types in Amazon SageMaker Pipelines, as well as how to add the step type to a pipeline.
- [Add integration](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps-integration.html): Describes the step types in Amazon SageMaker Pipelines, as well as how to add the integration type to a pipeline.

### [Lift-and-shift Python code with the @step decorator](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-step-decorator.html)

Learn how to use the @step decorator to convert local code to pipeline steps.

- [Create a pipeline with @step-decorated functions](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-step-decorator-create-pipeline.html): Learn how to create a pipeline with @step-decorated functions.
- [Run a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-step-decorator-run-pipeline.html): Learn how to run a pipeline with @step-decorated functions.
- [Configure your pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-step-decorator-cfg-pipeline.html): Learn how to configure a pipeline with @step-decorated functions.
- [Best Practices](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-step-decorator-best.html): Learn best practices for working with the @step decorator.
- [Limitations](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-step-decorator-limit.html): Learn about limitations when working with the @step decorator.
- [Pass Data Between Steps](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-propertyfile.html): Learn how to get the results of a pipeline step to decide how a conditional step should be run.

### [Caching pipeline steps](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-caching.html)

Use step signature caching to find a previous run of a Amazon SageMaker Pipelines step that was called with the same attributes.

- [Turn on step caching](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-caching-enabling.html): Turn on step signature caching to find a previous run of a Amazon SageMaker Pipelines step that was called with the same attributes.
- [Turn off step caching](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-caching-disabling.html): Turn off step signature caching to stop finding a previous run of a Amazon SageMaker Pipelines step that was called with the same attributes.
- [Default cache key attributes by pipeline step type](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-default-keys.html): Learn about the default cache key attributes based on the type of a Amazon SageMaker Pipelines step.
- [Cached data access control](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-access-control.html): Learn about the cached data access control for Amazon SageMaker Pipelines.

### [Retry Policy](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-retry-policy.html)

This is a retry policy to help retry Pipelines steps after an error occurs.

- [Retry policy example](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-configuring-retry-policy.html): Example of a training step with a retry policy.
- [Selective Execution](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-selective-ex.html): Learn how to create a selective Pipelines execution with selected pipeline steps.
- [ClarifyCheck QualityCheck Baselines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-quality-clarify-baseline-lifecycle.html): Working with baselines in ClarifyCheck and QualityCheck steps in Pipelines
- [Schedule Pipeline Runs](https://docs.aws.amazon.com/sagemaker/latest/dg/pipeline-eventbridge.html): Schedule your Amazon SageMaker Pipelines executions using Amazon EventBridge.

### [Experiments Integration](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-experiments.html)

Amazon SageMaker Pipelines is closely integrated with Amazon SageMaker Experiments.

- [Default Behavior](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-experiments-default.html): Create a pipeline
- [Disable Experiments Integration](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-experiments-none.html): Create a pipeline
- [Specify a Custom Experiment Name](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-experiments-custom-experiment.html): While the default behavior is to use the pipeline name as the experiment name in SageMaker Experiments, you can override this and specify a custom experiment name instead.
- [Specify a Custom Run Group Name](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-experiments-custom-trial.html): In addition to setting a custom experiment name, you can also specify a custom name for the run groups created by SageMaker Experiments during pipeline executions.
- [Run pipelines using local mode](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-local-mode.html): Information about Pipelines Local Mode.
- [Troubleshooting Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-troubleshooting.html): Information about common errors and how to resolve them when using Amazon SageMaker Pipelines.

### [Pipelines actions](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-build.html)

You can use either the Amazon SageMaker Pipelines Python SDK or the drag-and-drop visual designer in Amazon SageMaker Studio to author, view, edit, execute, and monitor your ML workflows.

- [Define a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/define-pipeline.html): Learn how to use Amazon SageMaker Pipelines to orchestrate workflows by generating a directed acyclic graph as a JSON pipeline definition.
- [Edit a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/edit-pipeline-before-execution.html): To make changes to a pipeline before running it, do the following:
- [Run a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/run-pipeline.html): After defining the steps of your pipeline as a directed acyclic graph (DAG), you can run your pipeline, which executes the steps defined in your DAG.
- [Stop a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-studio-stop.html): Learn how to stop a pipeline run.
- [View the details of a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-studio-list.html): Learn how to view the details of a SageMaker AI pipeline.
- [View the details of a pipeline run](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-studio-view-execution.html): Learn how to view the details of a pipeline run.
- [Download a pipeline definition file](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-studio-download.html): Learn how to download a pipeline definition file.
- [Access experiment data from a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-studio-experiments.html): How to view Amazon SageMaker Experiments, run groups, and runs created by Amazon SageMaker Pipelines.
- [Track the lineage of a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-lineage-tracking.html): How to track the lineage of an Amazon SageMaker AI ML Pipeline.

### [Kubernetes Orchestration](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-workflows.html)

Use Kubernetes to orchestrate SageMaker training and inference jobs.

### [SageMaker AI Operators for Kubernetes](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-operators.html)

Set up and use SageMaker AI Operators for Kubernetes.

- [Latest SageMaker AI Operators for Kubernetes](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-operators-ack.html): SageMaker AI Operators for Kubernetes based on AWS Controllers for Kubernetes

### [Old SageMaker AI Operators for Kubernetes](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-operators-end-of-support.html)

Learn about the end of support for the original version of SageMaker AI Operators for Kubernetes.

- [Use SageMaker AI Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-jobs.html): Run training jobs and more with SageMaker AI Operators for Kubernetes.
- [Migrate to Latest Operator](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-operators-migrate.html): Migrate existing resources to the new ACK-based SageMaker AI Operators for Kubernetes.
- [End of support FAQ](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-operators-eos-announcement.html): Learn about the end of support for the original version of SageMaker AI Operators for Kubernetes.

### [SageMaker AI Components for Kubeflow Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-components-for-kubeflow-pipelines.html)

Manage data processing and training jobs with SageMaker AI Components for Kubeflow Pipelines.

- [Install Kubeflow Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-components-install.html): Instructions to install Kubeflow Pipelines with Kubeflow on AWS or standalone.
- [Use SageMaker AI components](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-components-tutorials.html): Run Kubeflow Pipelines on SageMaker AI using SageMaker AI components.

### [Notebook Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-auto-run.html)

Learn about notebook-based noninteractive workflows.

### [Installation guide](https://docs.aws.amazon.com/sagemaker/latest/dg/scheduled-notebook-installation.html)

Learn about how to install the notebook scheduling feature.

- [Set up policies and permissions for Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/scheduled-notebook-policies-studio.html): Learn how to set up the permissions and policies needed to schedule notebook jobs in Studio.
- [Install policies and permissions for local Jupyter environments](https://docs.aws.amazon.com/sagemaker/latest/dg/scheduled-notebook-policies-other.html): Learn about the permissions and policies needed to schedule notebook jobs in local Jupyter environments.

### [Where you can create a notebook job](https://docs.aws.amazon.com/sagemaker/latest/dg/create-notebook-auto-run.html)

Where you can create a noninteractive notebook job.

- [Create notebook job with SageMaker AI Python SDK example](https://docs.aws.amazon.com/sagemaker/latest/dg/create-notebook-auto-run-sdk.html): Learn how to schedule a non-interactive notebook job with the SageMaker AI Python SDK.

### [Create a notebook job in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/create-notebook-auto-run-studio.html)

Schedule a noninteractive notebook job in Studio.

- [Set up default options for local notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/create-notebook-auto-execution-advanced-default.html): Learn how to set up default options when you create a notebook job.

### [Notebook job workflows](https://docs.aws.amazon.com/sagemaker/latest/dg/create-notebook-auto-run-dag.html)

Create a noninteractive notebook job workflow.

- [Pass information to and from your notebook step](https://docs.aws.amazon.com/sagemaker/latest/dg/create-notebook-auto-run-dag-seq.html): Learn how to pass dependencies between notebook jobs.
- [Invoke another notebook in your notebook job](https://docs.aws.amazon.com/sagemaker/latest/dg/create-notebook-auto-run-dag-call.html): Learn how to set up a pipeline in which one notebook job calls another notebook.
- [Available options](https://docs.aws.amazon.com/sagemaker/latest/dg/create-notebook-auto-execution-advanced.html): Advanced settings
- [Parameterize your notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-auto-run-troubleshoot-override.html): Learn how to parameterize your Jupyter notebook.
- [Connect to an Amazon EMR cluster from your notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/scheduled-notebook-connect-emr.html): Learn how to connect to Amazon EMR in your Jupyter notebook.

### [Notebook jobs details in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/track-jobs-jobdefs.html)

View your list of job runs.

- [View notebook jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/view-notebook-jobs.html): View your list of job runs.
- [View notebook job definitions](https://docs.aws.amazon.com/sagemaker/latest/dg/view-def-detail-notebook-auto-run.html): View your list of job definitions.
- [Troubleshooting guide](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-auto-run-troubleshoot.html): Troubleshoot issues you might see when you run a notebook job.
- [Constraints and considerations](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-auto-run-constraints.html): Learn about constraints and considerations on scheduling notebook jobs.
- [Pricing for SageMaker Notebook Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-auto-run-pricing.html): Learn about the cost to schedule notebook jobs.
- [Schedule your ML workflows](https://docs.aws.amazon.com/sagemaker/latest/dg/workflow-scheduling.html): Learn how to schedule your ML workflow steps.
- [AWS Batch support for training jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/training-job-queues.html): Learn how to use AWS Batch job queues with SageMaker AI training jobs.

### [ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html)

Describes how you can track the lineage of machine learning workflows.

- [Tracking Entities](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-entities.html): Tracking entities maintain a representation of all the elements of your end-to-end machine learning workflow.
- [SageMaker AI-Created Entities](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-auto-creation.html): Amazon SageMaker AI creates tracking entities for SageMaker AI jobs, models, model packages, and endpoints.
- [Manually Create Entities](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-manual-creation.html): Manually create tracking entities using the SDK.
- [Querying Lineage Entities](https://docs.aws.amazon.com/sagemaker/latest/dg/querying-lineage-entities.html): Amazon SageMaker AI automatically generates graphs of lineage entities as you use them.
- [Tracking Cross-Account Lineage](https://docs.aws.amazon.com/sagemaker/latest/dg/xaccount-lineage-tracking.html): Accessing lineage entities from another account

### [Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)

With the Amazon SageMaker Model Registry you can catalog models for production, manage model versions, associate metadata, and manage the approval status of a model

### [Models, Model Versions, and Model Groups](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-models.html)

With the SageMaker Model Registry you can catalog models for production, manage model versions, associate metadata, and manage the approval status of a model

- [Create a Model Group](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-model-group.html): A Model Group contains different versions of a model.
- [Delete a Model Group](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-delete-model-group.html): You can delete an Amazon SageMaker AI Model Group in your account in Studio Classic.
- [Register Version](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-version.html): You can register an Amazon SageMaker AI model in your account or in a different account.
- [View Model Groups and Versions](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-view.html): Model Groups and versions help you organize your models.

### [Update Model Version Details](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html)

View and update details of a specific model version by using either the AWS SDK for Python (Boto3) or by using Amazon SageMaker Studio.

- [Add a training job (Studio)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details-studio-training.html): Learn about how to add a training job to a model in Amazon SageMaker AI.
- [Remove a training job (Studio)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details-studio-training-remove.html): Learn about how to remove a training job from a model in Amazon SageMaker AI.
- [Update training job details (Studio)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details-studio-training-update.html): Learn about how to update the details of a training job for a model in Amazon SageMaker AI.
- [Add an evaluation job (Studio)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details-studio-evaluate.html): Learn about how to add an evaluation job to a model in Amazon SageMaker AI.
- [Remove an evaluation job (Studio)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details-studio-evaluate-remove.html): Learn about how to remove an evaluation job from a model in Amazon SageMaker AI.
- [Update an evaluation job (Studio)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details-studio-evaluate-update.html): Learn about how to update an evaluation job from a model in Amazon SageMaker AI.
- [Update audit (governance) information (Studio)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details-studio-audit.html): Learn about how to update the audit information for a model to document important model details in Amazon SageMaker AI.
- [Update deployment information (Studio)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details-studio-deploy.html): Learn about how to update the deployment information for a model to initiate CI/CD deployment in Amazon SageMaker AI.
- [Compare Model Versions](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-version-compare.html): Compare model versions using Amazon SageMaker Studio Classic.
- [View and Manage Tags](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-tags.html): View, add, edit, or delete model group and model version tags.
- [Delete a Model Version](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-delete-model-version.html): You can delete an Amazon SageMaker AI model version in your account in Studio.

### [Staging Construct](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-staging-construct.html)

Learn about constructing staging for your models in Amazon SageMaker Model Registry.

- [Set up Staging Construct Examples](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-staging-construct-set-up.html): Learn how to set up a staging construct for your models in Amazon SageMaker Model Registry.
- [Update a model package stage and status in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-staging-construct-update-studio.html): Learn how to update a status for a staging construct for your models in Amazon SageMaker Studio.
- [Update a model package stage and status example (boto3)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-staging-construct-update-boto3.html): Learn how to update a status for a staging construct for your models in Amazon SageMaker Model Registry using AWS SDK for Python (Boto3).
- [Invoke ModelLifeCycle using the AWS CLI examples](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-staging-construct-cli.html): Learn how to invoke a staging construct using AWS CLI commands.
- [Get event notifications for ModelLifeCycle](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-staging-construct-event-bridge.html): Learn how to set up an Amazon EventBridge rule for ModelLifeCycle updates.
- [Update Model Approval Status](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-approve.html): Evaluate a model's performance before you deploy it to a production endpoint.
- [Deploy Model with Python](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-deploy.html): Deploy a registered model to a SageMaker AI endpoint for real-time inference with Python.
- [Deploy Model in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-deploy-studio.html): Instructions on how to deploy a model in Studio.

### [Cross-account discoverability](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-ram.html)

Learn about concepts related to cross-account model package sharing.

- [Share model group in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-ram-studio-share.html): Instructions on how to share model groups in Studio.
- [View shared model groups in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-ram-studio-view.html): Instructions on how to view shared model groups in Studio.
- [Accessibility](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-ram-accessibility.html): Learn how to set up cross-account model package accessibility.
- [Set up discoverability](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-ram-discover.html): Learn how to set up cross-account model package discoverability.
- [View shared model package groups](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-ram-view-shared.html): Learn how to view shared model package groups.
- [Dissociate principals from a resource share and remove a resource share](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-ram-dissociate.html): Learn how to dissociate principals from a resource shared or delete a resource share.
- [Promote the permission and resource share](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-ram-promote.html): Learn how to promote the permission and model package resource share.
- [Deployment History](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-deploy-history.html): View the deployments for a model version Amazon SageMaker Studio.
- [View model lineage details in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-lineage-view-studio.html): Instructions on how to view the lineage details for your registered model in Amazon SageMaker Studio.

### [Collections](https://docs.aws.amazon.com/sagemaker/latest/dg/modelcollections.html)

Learn about SageMaker Model Registry Collections.

- [Set up prerequisite permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/modelcollections-permissions.html): Learn about permissions you need to set to use Collections.
- [Create a Collection](https://docs.aws.amazon.com/sagemaker/latest/dg/modelcollections-create.html): Learn how to create a Collection.
- [Add Model Groups to a Collection](https://docs.aws.amazon.com/sagemaker/latest/dg/modelcollections-add-models.html): Learn how to add Model Groups to a Collection.
- [Remove Model Groups or Collections from a Collection](https://docs.aws.amazon.com/sagemaker/latest/dg/modelcollections-remove-models.html): Learn how to remove Model Groups or Collections from a Collection.
- [Move a Model Group Between Collections](https://docs.aws.amazon.com/sagemaker/latest/dg/modelcollections-move-models.html): Learn how to move a Model Group to another Collection.
- [View a Model Group's Parent Collection](https://docs.aws.amazon.com/sagemaker/latest/dg/modelcollections-view-parent.html): Learn how to view a Model Group's parent Collection.
- [Constraints](https://docs.aws.amazon.com/sagemaker/latest/dg/modelcollections-limitations.html): Learn about Collection constraints.
- [Model Deployment](https://docs.aws.amazon.com/sagemaker/latest/dg/model-deploy-mlops.html): Learn about Amazon SageMaker AI Model Deploy in MLOps.
- [Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-mlops.html): Learn about Amazon SageMaker Model Monitor in MLOps.

### [Projects](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects.html)

Describes Amazon SageMaker Projects.

- [SageMaker Projects](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-whatis.html): With SageMaker Projects, you can create a MLOps solution to orchestrate and manage building custom images for processing, training, inference, data preparation, and feature engineering for training, evaluating, deploying, monitoring, and updating models.
- [Granting SageMaker Studio Permissions Required to Use Projects](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-studio-updates.html): The Amazon SageMaker Studio (or Studio Classic) administrator and Studio (or Studio Classic) users that you add to your domain can view project templates provided by SageMaker AI and create projects with those templates.
- [Create a MLOps Project](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-create.html): Demonstrates how to create a MLOps project using Amazon SageMaker Studio Classic.

### [Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates.html)

Describes the templates in Amazon SageMaker Projects.

- [Use Provided Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates-sm.html): Amazon SageMaker AI provides project templates that create the infrastructure you need to create an MLOps solution of ML models.
- [Custom Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates-custom.html): For custom and more complex orchestration in the CodePipeline with multiple stages or custom approval steps), create your own templates.
- [View Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-resources.html): View the resources associated with a project in Amazon SageMaker Studio Classic.
- [Update a MLOps Project](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-update.html): Demonstrates how to update a MLOps project in Amazon SageMaker Studio or Studio Classic.
- [Delete a MLOps Project](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-delete.html): Demonstrates how to delete a MLOps project using Amazon SageMaker Studio or Studio Classic.
- [Walk Through a Project Using Third-party Git Repos](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-walkthrough-3rdgit.html): This walkthrough uses the template to demonstrate using MLOps projects to create a CI/CD system to build, train, and deploy models.
- [MLOps troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/mlopsfaq.html): Common questions about SageMaker AI MLOps.


## [Data and model quality monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)

- [Model Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-model-monitor.html): After you deploy a model into your production environment, use Amazon SageMaker Model Monitor to continuously monitor the quality of your machine learning models in real time.

### [Data capture](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html)

How to capture data with Amazon SageMaker Model Monitor.

- [Capture data from real-time endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture-endpoint.html): How to capture data with Amazon SageMaker Model Monitor.
- [Capture data from batch transform job](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture-batch.html): How to capture data with Amazon SageMaker Model Monitor.

### [Data quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html)

Data quality monitoring automatically monitors machine learning (ML) models in production and notifies you when data quality issues arise.

- [Create a Baseline](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-create-baseline.html): How to create baseline statistics.
- [Schedule data quality monitoring jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-schedule-data-monitor.html): Schedule data quality monitoring jobs.
- [Statistics](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-interpreting-statistics.html): Schema file for the statistics are to be computed for the data monitored.
- [CloudWatch Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-interpreting-cloudwatch.html): The schema for the CloudWatch metrics file.
- [Violations](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-interpreting-violations.html): The schema for the violations.json file.

### [Model quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality.html)

Model quality monitoring jobs monitor the performance of a model by comparing the predictions that the model makes with the actual Ground Truth labels that the model attempts to predict.

- [Create a model quality baseline](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-baseline.html): Create a baseline job that compares your model predictions with ground truth labels in a baseline dataset that you have stored in Amazon S3.
- [Schedule model quality monitoring jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html): After you create your baseline, you can call the create_monitoring_schedule() method of your ModelQualityMonitor class instance to schedule an hourly model quality monitor.
- [Ingest Ground Truth labels and merge them with predictions](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-merge.html): Model quality monitoring compares the predictions your model makes with ground truth labels to measure the quality of the model.
- [Model quality metrics and Amazon CloudWatch monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-metrics.html): Model quality monitoring jobs compute different metrics to evaluate the quality and performance of your machine learning models.

### [Bias drift](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift.html)

Monitor bias drift for models in production,using Amazon SageMaker Clarify.

- [Create a Bias Drift Baseline](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift-baseline.html): Create a bias drift baseline for Machine Learning (ML) models.
- [Bias Drift Violations](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift-violations.html): Detecting bias drift in production with SageMaker Clarify.
- [Parameters to Monitor Bias Drift](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-config-json-monitor-bias-parameters.html): How to configure parameters for monitoring bias drift in Amazon SageMaker Clarify.
- [Schedule Bias Drift Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift-schedule.html): Schedule bias drift monitoring jobs.
- [Inspect Reports for Data Bias Drift](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift-report.html): Inspect a data bias drift report in SageMaker Studio.
- [CloudWatch Metrics for Bias Drift Analysis](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift-cw.html): Learn which CloudWatch metrics to use for bias drift analysis in SageMaker Clarify.

### [Feature attribution drift](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-feature-attribution-drift.html)

Monitor feature attribution drift for models in production, using Amazon SageMaker Clarify.

- [Create a SHAP Baseline](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-shap-baseline.html): Explanations are typically contrastive, that is, they account for deviations from a baseline.
- [Feature Attribution Drift Violations](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-model-attribution-drift-violations.html): Detecting model feature attribution drift in production with SageMaker Clarify.
- [Parameters to Monitor Attribution Drift](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-config-json-monitor-model-explainability-parameters.html): How to configure parameters for monitoring attribution drift in Amazon SageMaker Clarify.
- [Schedule Feature Attribute Drift Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-feature-attribute-drift-schedule.html): Schedule feature attribute drift monitoring jobs using Amazon SageMaker AI.
- [Inspect Reports for Feature Attribute Drift](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-drift-report.html): Inspect a feature attribute drift report in production models.
- [CloudWatch Metrics for Feature Drift Analysis](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-drift-cw.html): Learn which CloudWatch metrics to use for feature attribution drift analysis in SageMaker Clarify

### [Schedule monitoring jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-scheduling.html)

How to schedule monitoring jobs.

- [cron scheduling](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-schedule-expression.html): How to create a monitoring schedule.
- [Configuring SCPs for monitoring schedules](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-scp-rules.html): Learn how to configure service control policies (SCPs) for monitoring schedules.
- [Prebuilt container](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-pre-built-container.html): Prebuilt container.
- [Interpret results](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-interpreting-results.html): Interpret results.
- [Visualize results for real-time endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-interpreting-visualize-results.html): Visualize results in Amazon SageMaker Studio.

### [Advanced topics](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-advanced-topics.html)

More advanced, customized procedures.

### [Custom monitoring schedules](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-custom-monitoring-schedules.html)

Custom monitoring with pre and post processing.

- [](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-pre-and-post-processing.html): Extend the code with the preprocessing and postprocessing scripts.

### [Support for Your Own Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-byoc-containers.html)

Contract for building your own container.

- [Inputs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-byoc-contract-inputs.html): Amazon SageMaker Model Monitor container inputs.

### [Outputs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-byoc-contract-outputs.html)

Amazon SageMaker Model Monitor container outputs.

- [Statistics](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-byoc-statistics.html): Which statistics are to be computed for the data monitored.
- [Constraints](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-byoc-constraints.html): Which constraints are to be computed for the data monitored.
- [CloudWatch Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-byoc-cloudwatch.html): The schema for the CloudWatch metrics file.
- [CloudFormation Custom Resource for Real-time Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-cloudformation-monitoring-schedules.html): Monitoring schedules with CloudFormation custom resource.
- [Model Monitor FAQs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-faqs.html): Use the following FAQs to learn more about Model Monitor.


## [Evaluate, explain, and detect bias in models](https://docs.aws.amazon.com/sagemaker/latest/dg/model-explainability.html)

### [Evaluate foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate.html)

Learn how to evaluate a text-based foundation model by using SageMaker Clarify

- [Model evaluations](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-whatis.html): Learn more about what features are available to evaluate foundation models in SageMaker AI.
- [Get started](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-get-started.html): A large language model (LLM) is a machine learning model that can analyze and generate natural language text.

### [Prompt datasets and evaluation dimensions](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-overview.html)

Learn about foundation model evaluation, including evaluation tasks, metrics, and built-in datasets for both human and automatic evaluations.

- [Accuracy](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-accuracy-evaluation.html): Learn about how Amazon SageMaker AI evaluates accuracy for models.
- [Factual Knowledge](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-factual-knowledge-evaluation.html): Learn about how Amazon SageMaker AI runs factual knowledge evaluations for models.
- [Prompt stereotyping](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-prompt-stereotyping-evaluation.html): Learn about how Amazon SageMaker AI runs prompt stereotyping evaluations for models.
- [Semantic Robustness](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-semantic-robustness-evaluation.html): Learn about how Amazon SageMaker AI runs semantic robustness evaluations for models.
- [Toxicity](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-toxicity-evaluation.html): Learn about how Amazon SageMaker AI runs toxicity evaluations for models.
- [Create a model evaluation job that uses human workers](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-human.html): Learn how to ask a human work team to evaluate your foundation model.

### [Automatic model evaluation](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto.html)

Use an automatic evaluation by running it in a UI or by using the fmeval library inside your own code.

- [Create an automatic model evaluation job in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-ui.html): Learn how to create an automatic model evaluation job in Studio.
- [Use the fmeval library to run an automatic evaluation](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-lib.html): Learn how to use the fmeval library for more flexibility over your workflow when creating automatic model evaluation jobs.
- [Model evaluation results](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-reports.html): Learn how to interpret the results of your model evaluation job results

### [Job results](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-results.html)

Learn how to interpret and understand the results of your model evaluation job

- [Understand the results of a human evaluation job](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-results-human.html): Understand how to interpret the JSON results of a human evaluation job.
- [Understand the results of an automatic evaluation job](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-ui-results.html): Learn how to interpret automatic model evaluation results.
- [Using the fmeval library](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-lib-custom.html): Learn how to evaluate a custom foundation model.

### [Model evaluation notebook tutorials](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-tutorial.html)

Learn how to use the fmeval library inside a notebook to evaluate your model.

- [Evaluate a JumpStart model for prompt stereotyping](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-tutorial-one.html): Follow a tutorial for how to evaluate an Amazon SageMaker JumpStart model for prompt stereotyping.
- [Evaluate an Amazon Bedrock model for text summarization accuracy](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-tutorial-two.html): Learn how to evaluate an Amazon Bedrock model for text summarization accuracy.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-troubleshooting.html): Learn about common errors using FMEval and how to mitigate them.

### [Evaluate JumpStart text models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-text-classification-evaluation.html)

Evaluate and compare Amazon SageMaker AI JumpStart text classification models using comprehensive metrics and datasets.

- [Set up your evaluation environment](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-text-classification-setup.html): Set up Amazon SageMaker AI Amazon SageMaker Studio to access Amazon SageMaker JumpStart models for text classification evaluation and understand associated costs.
- [Select and deploy text classification models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-text-classification-deploy.html): Deploy DistilBERT and BERT text classification models from Amazon SageMaker JumpStart for comparison and evaluation.
- [Evaluate and compare model performance](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-text-classification-evaluate.html): Evaluate your deployed text classification models using a notebook-based approach to test performance across multiple datasets and metrics.
- [Interpret your results](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-text-classification-interpret.html): Understand evaluation metrics to help you choose the right model for your needs and avoid common interpretation mistakes.
- [Deploy your model at scale](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-text-classification-scale.html): Set up auto-scaling and Amazon CloudWatch monitoring for your Amazon SageMaker AI endpoint to make it production-ready.

### [Fairness and explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)

Learn how to explain and detect bias with Amazon SageMaker Clarify.

### [Configure a SageMaker Clarify Processing Job](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-configure-parameters.html)

Learn to specify the input dataset name, analysis configuration file name, and output location for a processing job.

- [SageMaker Clarify Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-configure-container.html): The container contains pre-built images and dependencies needed to compute bias metrics and feature attributions.
- [Analysis Configuration Files](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-configure-analysis.html): Learn how to specify the inputs to configure the analysis for explainability and bias.

### [Data Format Compatibility Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format.html)

Learn what types of data formats are compatible with SageMaker Clarify processing jobs.

### [Tabular data](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-tabular.html)

Learn about data format requirements for tabular data when using SageMaker Clarify processing job.

- [Endpoint requests for tabular data](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-tabular-request.html): Learn about endpoint requests for tabular data in JSON Lines and CSV formats with SageMaker Clarify processing jobs.
- [Endpoint response for tabular data](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-tabular-response.html): Learn about endpoint responses for tabular data for CSV and JSON Lines formats.

### [Pre-check endpoint request and response for tabular data](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-tabular-precheck.html)

Learn how to check the format of your endpoint request and response.

- [AWS CLI v1 examples](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-tabular-precheck-cli-v1-examples.html): The example in the preceding section was for AWS CLI v2.
- [Image data requirements](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-image.html): Learn about data format requirements for image data when using SageMaker Clarify processing job.

### [Time series data](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-time-series.html)

Learn about data format requirements for time series data when using SageMaker Clarify processing job.

- [Endpoint requests for time series data](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-time-series-request-jsonlines.html): A SageMaker Clarify processing job serializes data into arbitrary JSON structures (with MIME type: application/json).
- [Endpoint response for time series data](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-time-series-response-json.html): Learn about endpoint responses for time series data for JSON format.
- [Pre-check endpoint request and response for time series data](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-data-format-time-series-precheck.html): Learn about endpoint responses for time series data for JSON format.
- [Run SageMaker Clarify Processing Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-run.html): Run SageMaker Clarify processing jobs for bias and explainability.
- [Analysis Results](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-analysis-results.html): Learn how to find and interpret analysis results that SageMaker Clarify generates.
- [Troubleshoot Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-run-troubleshooting.html): Common troubleshooting scenarios.

### [Pre-training Data Bias](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-data-bias.html)

Learn how to detect bias in your machine learning models.

### [Pre-training Bias Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-data-bias.html)

Measuring bias in ML models is a first step to mitigating bias.

- [Class Imbalance (CI)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-bias-metric-class-imbalance.html): Amazon SageMaker Clarify facet imbalance bias metric.
- [Label Imbalance (DPL)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-true-label-imbalance.html): Amazon SageMaker Clarify observed label imbalance data bias metric.
- [Kullback-Leibler Divergence (KL)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-kl-divergence.html): Amazon SageMaker Clarify KL divergence data bias metric.
- [Jensen-Shannon Divergence (JS)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-jensen-shannon-divergence.html): Amazon SageMaker Clarify Jensen-Shannon divergence data bias metric.
- [Lp-norm (LP)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-lp-norm.html): Amazon SageMaker Clarify Lp-norm data bias metric
- [Total Variation Distance (TVD)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-total-variation-distance.html): Amazon SageMaker Clarify total variation distance data bias metric.
- [Kolmogorov-Smirnov (KS)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-kolmogorov-smirnov.html): Amazon SageMaker Clarify Kolmogorov-Smirnov metric.
- [Conditional Demographic Disparity (CDD)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-cddl.html): Amazon SageMaker Clarify conditional demographic disparity data bias metric.
- [Generate Reports for Bias in Pre-training Data in SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-reports-ui.html): Generate reports for bias in pretraining data.

### [Post-training Data and Model Bias](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-post-training-bias.html)

Compare predictions against groups with different attributes to reveal bias in the data.

### [Post-training Data and Model Bias Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-post-training-bias.html)

Post-training data and model bias metrics compute different measures of fairness.

- [Difference in Positive Proportions in Predicted Labels (DPPL)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-dppl.html): Amazon SageMaker Clarify difference in positive proportions in predicted labels model bias metric.
- [Disparate Impact (DI)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-di.html): Amazon SageMaker Clarify disparate adverse impact model bias metric (DI).
- [Difference in Conditional Acceptance (DCAcc)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-dcacc.html): Amazon SageMaker Clarify post-training model bias metric for difference in conditional acceptance.
- [Difference in Conditional Rejection (DCR)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-dcr.html): Amazon SageMaker Clarify post-training model bias metric for difference in conditional rejection.
- [Specificity difference (SD)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-sd.html): Learn formulas for specificity difference (SD) model bias metric with Amazon SageMaker Clarify.
- [Recall Difference (RD)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-rd.html): Amazon SageMaker Clarify recall difference model bias metric.
- [Difference in Acceptance Rates (DAR)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-dar.html): Amazon SageMaker Clarify difference in acceptance rates model bias metric.
- [Difference in Rejection Rates (DRR)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-drr.html): Amazon SageMaker Clarify difference in rejection rates model bias metric
- [Accuracy Difference (AD)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-ad.html): Amazon SageMaker Clarify accuracy difference model bias metric.
- [Treatment Equality (TE)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-te.html): Amazon SageMaker Clarify treatment equality model bias metric.
- [Conditional Demographic Disparity in Predicted Labels (CDDPL)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-cddpl.html): Amazon SageMaker Clarify conditional demographic disparity in predicted labels model bias metric
- [Counterfactual Fliptest (FT)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-ft.html): Amazon SageMaker Clarify counterfactual fliptest model bias metric.
- [Generalized entropy (GE)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-post-training-bias-metric-ge.html): Use Amazon SageMaker Clarify generalized entropy index model bias metric to measure inequality in benefits (GE).

### [Model Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html)

Amazon SageMaker Clarify provides tools to explain how machine learning (ML) models make predictions.

- [Shapley Values](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-shapley-values.html): SageMaker Clarify provides feature attributions based on the concept of Shapley value.
- [Asymmetric Shapley Values](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-shap-asymm.html): The SageMaker Clarify time series forecasting model explanation solution is a feature attribution method rooted in cooperative game theory, similar in spirit to SHAP.
- [SHAP Baselines for Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.html): Explanations are typically contrastive (that is, they account for deviations from a baseline).
- [Explainability with Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-explainability.html): Use Autopilot and SageMaker Clarify together to get insights into the explainability of your models.


## [Model governance](https://docs.aws.amazon.com/sagemaker/latest/dg/governance.html)

### [Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)

Use Amazon SageMaker Model Card to document critical details about your machine learning (ML) models for governance and reporting.

- [Create a model card](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-create.html): Create an Amazon SageMaker Model Card.

### [Model cards actions](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-manage.html)

After you've created a model card, you can manage them.

- [Edit a model card](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-console-edit.html): To edit a model card, navigate to the model card of your choice by selecting its name in the Amazon SageMaker Model Card console and choose Edit.
- [Export a model card](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-console-export.html): Follow these steps to export a model card.
- [Delete a model card](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-console-delete.html): Follow these steps to permanently delete one or more model cards.
- [Set up cross-account support](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-xaccount.html): Access pipeline entities from another AWS account.
- [Model card APIs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-apis.html): Create an Amazon SageMaker Model Card using the SageMaker API or the AWS CLI.
- [Model card FAQs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-faqs.html): Find answers to commonly asked questions about Amazon SageMaker Model Card.

### [Controlled access to assets](https://docs.aws.amazon.com/sagemaker/latest/dg/sm-assets.html)

Learn about using Amazon SageMaker Assets to manage permissions and access to your models and data tables with minimal administrator overhead.

- [Set up SageMaker Assets (administrator guide)](https://docs.aws.amazon.com/sagemaker/latest/dg/sm-assets-set-up.html)
- [Work with assets (user guide)](https://docs.aws.amazon.com/sagemaker/latest/dg/sm-assets-user-guide.html): Use SageMaker Assets to seamlessly collaborate on machine learning projects with other individuals in your organization.

### [Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html)

Introduction to the Model Dashboard.

### [Model Monitor schedules and alerts](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-schedule.html)

How to view information about Model Monitor scheduling and Alerts.

- [View scheduled monitors](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-schedule-view.html): View a list of your scheduled model monitors in the Model Dashboard.
- [Activate or deactivate a model monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-schedule-activate.html): How to activate or deactivate a Model Monitor in the Model Dashboard.

### [View and edit alerts](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-alerts.html)

View or edit alert information in the Model Dashboard.

- [View alert history or job reports](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-alerts-view.html): View alert history or job reports in the Model Dashboard.
- [Edit alert criteria](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-alerts-edit.html): Edit alert information in the Model Dashboard

### [View a model lineage graph](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-lineage.html)

Introduction to Model Dashboard lineage graphs.

- [Introduction to entities](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-lineage-intro-entities.html): Introduction to entities used in Model Dashboard lineage graphs.
- [View Endpoint Status](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-endpoints.html): View information about a model's endpoints in the Model Dashboard.
- [Model Dashboard FAQ](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-faqs.html): FAQ about Model Dashboard features


## [Docker containers for training and deploying models](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html)

- [Docker container basics](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-basics.html): The following page outlines the most significant aspects of using Docker containers with Amazon SageMaker AI.

### [Pre-built SageMaker AI Docker images](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-prebuilt.html)

Learn about the pre-built container images that SageMaker AI provides.

- [Support Policy](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-support-policy.html): Learn about the support policy for SageMaker AI pre-built images in relation to associated framework releases.
- [Prebuilt Deep Learning Images](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html): Learn how to use prebuilt SageMaker AI Docker images for deep learning, including using the SageMaker Python SDK and extending prebuilt Docker images.
- [Prebuilt Scikit-learn and Spark ML Images](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-docker-containers-scikit-learn-spark.html): SageMaker AI provides prebuilt Docker images that install the scikit-learn and Spark ML libraries.

### [Deep Graph Networks](https://docs.aws.amazon.com/sagemaker/latest/dg/deep-graph-library.html)

How to train a deep graph network with Deep Graph Library (DGL).

- [Getting started with training a deep graph network](https://docs.aws.amazon.com/sagemaker/latest/dg/deep-graph-library-get-started.html): DGL is available as a deep learning container in Amazon ECR.
- [Extend a Pre-built Container](https://docs.aws.amazon.com/sagemaker/latest/dg/prebuilt-containers-extend.html): If a pre-built SageMaker AI container doesn't fulfill all of your requirements, you can extend the existing image to accommodate your needs.

### [Custom Docker containers with SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-adapt-your-own.html)

Leverage the Amazon SageMaker Training and Inference Toolkits to adapt existing Docker images for use with SageMaker AI.

- [SageMaker Training and Inference Toolkits](https://docs.aws.amazon.com/sagemaker/latest/dg/amazon-sagemaker-toolkits.html): How to use the SageMaker Training and Inference Toolkits with your own Docker containers.

### [Adapting your own training container](https://docs.aws.amazon.com/sagemaker/latest/dg/adapt-training-container.html)

To run your own training model, build a Docker container using the Amazon SageMaker Training Toolkit through an Amazon SageMaker notebook instance.

### [Adapt your training job to access images in a private Docker registry](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-adapt-your-own-private-registry.html)

Learn how to use a private Docker registry to host images for your training job.

- [Use a SageMaker AI estimator to run a training job](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-adapt-your-own-private-registry-estimator.html): Use a SageMaker AI estimator to run a training job using a private Docker registry.
- [Use a Docker registry that requires authentication for training](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-adapt-your-own-private-registry-authentication.html): Learn how to use a Docker container that requires authentication to access images for training.
- [Adapt your own inference container for Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/adapt-inference-container.html): Learn how to adapt your own Docker container to work with SageMaker AI hosting.

### [Container creation with your own algorithms and models](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-create.html)

Learn how to create your own Docker container.

### [Containers with custom training algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo.html)

Create a Docker container to run your custom training algorithm.

- [Run Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html): Learn how Amazon SageMaker AI runs your training image in the backend, and how to specify a custom entrypoint script for your Docker container.
- [Provide Training Information](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-running-container.html): How Amazon SageMaker AI makes training information available to your Docker container.
- [Run Training with EFA](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-efa.html): SageMaker AI provides integration with EFA devicesÂ to accelerate High Performance Computing (HPC) and machine learning applications.
- [Signal Success or Failure](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-signal-success-failure.html): How a training algorithm indicates whether it succeeded or failed using the exit code of its process.
- [Training Output](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-output.html): As your algorithm runs in a container, it generates output including the status of the training job and model and output artifacts.

### [Containers with custom inference code](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-main.html)

Use your own inference code with Amazon SageMaker AI hosting services or with batch transform.

### [Custom Inference Code with Hosting Services](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html)

How Amazon SageMaker AI interacts with a Docker container that runs your own inference code for hosting services.

- [Private Docker Registry for Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-containers-inference-private.html): Amazon SageMaker AI hosting enables you to use images stored in Amazon ECR to build your containers for real-time inference by default.
- [Custom Inference Code with Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-batch-code.html): Learn to write your own inference code and deploy it to a Docker container to use with Amazon SageMaker AI batch transform.
- [Examples and more info](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-notebooks.html): The following Jupyter notebooks and added information show how to use your own algorithms or pretrained models from an Amazon SageMaker notebook instance.


## [Configure security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security.html)

- [Data Privacy](https://docs.aws.amazon.com/sagemaker/latest/dg/data-privacy.html): Learn how AWS uses metadata and how to opt out.

### [Data Protection](https://docs.aws.amazon.com/sagemaker/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon SageMaker AI.

### [Protect Data at Rest Using Encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest.html)

Amazon SageMaker AI automatically encrypts your data using an AWS managed key for Amazon S3 (SSE-S3) by default for the following features: Studio notebooks, notebook instances, model-building data, model artifacts, and output from Training, Batch Transform, and Processing jobs.

- [Studio notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest-studio.html): In Amazon SageMaker Studio, your SageMaker Studio notebooks and data can be stored in the following locations:
- [Notebook instances, SageMaker AI jobs, and Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest-nbi.html): To encrypt the machine learning (ML) storage volume that is attached to notebooks, processing jobs, training jobs, hyperparameter tuning jobs, batch transform jobs, and endpoints, you can pass a AWS KMS key to SageMaker AI.
- [SageMaker geospatial capabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-encryption-at-rest.html): Learn how Amazon SageMaker geospatial protect and encrypt your data at rest.

### [Protecting Data in Transit with Encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-in-transit.html)

Protect machine learning and model artifacts data in transit.

- [Protect Communications Between ML Compute Instances in a Distributed Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/train-encrypt.html): Protect communications between ML compute instances in an Amazon SageMaker training job.
- [Key Management](https://docs.aws.amazon.com/sagemaker/latest/dg/key-management.html): Customers can specify AWS KMS keys, including bring your own keys (BYOK), to use for envelope encryption with Amazon S3 input/output buckets and machine learning (ML) Amazon EBS volumes.
- [Internetwork Traffic Privacy](https://docs.aws.amazon.com/sagemaker/latest/dg/inter-network-privacy.html): This topic describes how Amazon SageMaker AI secures connections from the service to other locations.

### [Identity and Access Management](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam.html)

How to authenticate requests and manage access your SageMaker AI resources.

- [How Amazon SageMaker AI works with IAM](https://docs.aws.amazon.com/sagemaker/latest/dg/security_iam_service-with-iam.html)
- [Identity-based policy examples](https://docs.aws.amazon.com/sagemaker/latest/dg/security_iam_id-based-policy-examples.html): Learn how to use Amazon SageMaker AI Identity-Based Policy Examples to give users and roles permission to create or modify Amazon SageMaker AI resources.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/sagemaker/latest/dg/security-confused-deputy-prevention.html): Prevent the cross-service confused deputy problem for Amazon SageMaker AI resources.

### [How to use SageMaker AI execution roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html)

Learn what Amazon SageMaker AI execution roles are and how to use them.

### [SageMaker geospatial capabilities roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-geospatial-roles.html)

As a managed service, Amazon SageMaker geospatial capabilities performs operations on your behalf on the AWS hardware that is managed by SageMaker AI.

- [Creating an new SageMaker AI execution role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-geospatial-roles-create-execution-role.html): To work with SageMaker geospatial capabilities, you must set up a user, group, or role, and an execution role.
- [Adding the SageMaker geospatial service principal to an existing SageMaker AI execution role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-geospatial-roles-pass-role.html): To use the SageMaker geospatial specific API operations your SageMaker AI execution role must include the SageMaker geospatial service principal, sagemaker-geospatial.amazonaws.com in the execution role's trust policy.
- [StartEarthObservationJob API: Execution role permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles-start-eoj-perms.html): For an execution role that you can pass in a StartEarthObservationJob API request, you can attach the following minimum permissions policy to the role:
- [StartVectorEnrichmentJob API: Execution role permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles-start-vej-perms.html): For an execution role that you can pass in a StartVectorEnrichmentJob API request, you can attach the following minimum permissions policy to the role:
- [ExportEarthObservationJob API: Execution role permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles-export-eoj-perms.html): For an execution role that you can pass in a ExportEarthObservationJob API request, you can attach the following minimum permissions policy to the role:
- [ExportVectorEnrichmentJob API: Execution Role Permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles-export-vej-perms.html): For an execution role that you can pass in a ExportVectorEnrichmentJob API request, you can attach the following minimum permissions policy to the role:

### [Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html)

Define least-privilege user permissions for machine learning personas with Amazon SageMaker Role Manager.

- [Using the role manager (console)](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager-tutorial.html): Learn how to use Amazon SageMaker Role Manager.
- [Using the role manager (AWS CDK)](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager-tutorial-cdk.html): Learn how to use Amazon SageMaker Role Manager.
- [Persona reference](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager-personas.html): Learn how Amazon SageMaker Role Manager provides suggested permissions for a number of machine learning personas.
- [ML activity reference](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager-ml-activities.html): Learn about ML activities, common AWS tasks related to machine learning with SageMaker AI that require specific IAM permissions.
- [Launch Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager-launch-notebook.html): Launch Studio Classic using a role created with Amazon SageMaker Role Manager.
- [Role Manager FAQs](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager-faqs.html): Find answers to commonly asked questions about Amazon SageMaker Role Manager.

### [Access Control](https://docs.aws.amazon.com/sagemaker/latest/dg/security-access-control.html)

How to control root access to Amazon SageMaker Studio Classic notebooks and SageMaker notebook instances.

- [Access control and Studio notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/security-access-control-studio-nb.html): Information about access control and Amazon SageMaker Studio notebooks.
- [Control root access to a Notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-root-access.html): How to control root access to a Amazon SageMaker notebook instance.
- [Amazon SageMaker AI API Permissions Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/api-permissions-reference.html): Provides a complete list of the required API permissions you can use to control access to your Amazon SageMaker AI resources.

### [AWS managed policies for SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol.html)

Learn about AWS managed policies for SageMaker AI and recent changes to those policies.

- [SageMaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-canvas.html): Learn about AWS managed policies for SageMaker Canvas and recent changes to those policies.
- [SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-feature-store.html): Learn about AWS managed policies for Amazon SageMaker Feature Store and recent changes to those policies.
- [SageMaker geospatial](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-geospatial.html): Learn about AWS managed policies for SageMaker geospatial and recent changes to those policies.
- [SageMaker AI Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-ground-truth.html): Learn about AWS managed policies for SageMaker AI Ground Truth and recent changes to those policies.

### [SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-hyperpod.html)

Learn about AWS managed policies for Amazon SageMaker HyperPod and recent changes to those policies.

- [AmazonSageMakerHyperPodTrainingOperatorAccess](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-AmazonSageMakerHyperPodTrainingOperatorAccess.html): AmazonSageMakerHyperPodTrainingOperatorAccess grants permissions needed to retrieve information for the Amazon SageMaker HyperPod training operator.
- [AmazonSageMakerHyperPodObservabilityAdminAccess](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.html): AmazonSageMakerHyperPodObservabilityAdminAccess grants permissions needed to set up observability for Amazon SageMaker HyperPod.
- [AmazonSageMakerHyperPodServiceRolePolicy](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.html): How to use service-linked roles to give SageMaker HyperPod access to resources in your AWS account.
- [AmazonSageMakerClusterInstanceRolePolicy](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy.html): AmazonSageMakerClusterInstanceRolePolicy grants permissions commonly needed to use Amazon SageMaker HyperPod.
- [SageMaker AI Model Governance](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-governance.html): Learn about AWS managed policies for SageMaker AI Model Governance and recent changes to those policies.
- [Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-model-registry.html): Learn about AWS managed policies for Model Registry and recent changes to those policies.
- [SageMaker Notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-notebooks.html): Learn about AWS managed policies for SageMaker Notebooks and recent changes to those policies.
- [Amazon SageMaker Partner AI Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-partner-apps.html): Learn about AWS managed policies for Amazon SageMaker Partner AI Apps and recent changes to those policies.
- [SageMaker Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-pipelines.html): Learn about AWS managed policies for SageMaker Pipelines and recent changes to those policies.
- [SageMaker training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-training-plan.html): Learn about the AWS managed policy for SageMaker training plans and recent changes to those policies.
- [SageMaker Projects and JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-sc.html): Learn about AWS managed policies for SageMaker Projects and JumpStart, and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with SageMaker AI and IAM.
- [Logging and Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-incident-response.html): You can monitor Amazon SageMaker AI using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Compliance validation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/sagemaker/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon SageMaker AI features for data resiliency.

### [Infrastructure Security](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-security.html)

Learn how Amazon SageMaker AI isolates service traffic.

### [Connect to Amazon SageMaker AI resources from within a VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-connect-to-resources.html)

- [Connect Studio in a VPC to External Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-and-internet-access.html)
- [Connect Studio Notebooks in a VPC to External Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html): The following topic gives information about how to connect Studio Notebooks in a VPC to external resources.
- [Connect a Notebook Instance in a VPC to External Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-notebook-and-internet-access.html): The following topic gives information on how to connect your notebook instance in a VPC to external resources.
- [Run Training and Inference Containers in Internet-Free Mode](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html): SageMaker AI training and deployed inference containers are internet-enabled by default.

### [Connect to SageMaker AI Within your VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html)

Access the SageMaker API or SageMaker AI Runtime using a VPC.

- [Connect Studio and Studio Classic Through a VPC Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-interface-endpoint.html): Connect to Amazon SageMaker Studio and Studio Classic through an interface VPC endpoint.

### [Connecting to MLflow through a VPC Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-interface-endpoint.html)

Connect to SageMaker AI MLflow through an interface VPC endpoint.

- [Create a VPC Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-interface-endpoint-create.html): You can create an interface endpoint to connect to SageMaker AI MLflow.
- [Create a VPC Endpoint Policy for SageMaker AI MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-private-link-policy.html): You can attach an Amazon VPC endpoint policy to the interface VPC endpoints that you use to connect to SageMaker AI MLflow.
- [Allow Access only from within your VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-private-link-restrict.html): Users outside your VPC can connect to SageMaker AI MLflow or over the internet even if you set up an interface endpoint in your VPC.
- [Connect to a Notebook Instance Through a VPC Interface Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-interface-endpoint.html): Connect to a SageMaker notebook instance by using a VPC interface endpoint.

### [Give SageMaker AI Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html)

SageMaker AI runs the following job types in an Amazon Virtual Private Cloud by default.

- [Give SageMaker AI Processing Jobs Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/process-vpc.html): Give SageMaker Processing jobs access to resources in your VPC.
- [Give SageMaker AI Training Jobs Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html): Give SageMaker training jobs access to resources in your VPC.
- [Give SageMaker AI Hosted Endpoints Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html): Protect SageMaker AI models by using a VPC to limit access to resources over the internet.
- [Give Batch Transform Jobs Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-vpc.html): Protect SageMaker AI batch transform jobs by using a VPC to limit access to resources over the internet.
- [Give Amazon SageMaker Clarify Jobs Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-vpc.html): Protect Amazon SageMaker Clarify jobs by using an Amazon VPC to limit access to resources over the public internet.
- [Give SageMaker AI Compilation Jobs Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-vpc.html)
- [Give Inference Recommender Jobs Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-vpc-access.html): Learn more about how to give Inference Recommender jobs access to resources in your Amazon VPC.


## [Algorithms and packages in the AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace.html)

### [Custom algorithms and models with the AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-marketplace.html)

The following sections show how to create algorithm and model package resources that you can use locally and publish to the AWS Marketplace.

### [Creation of Algorithm and Model Package Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-create.html)

Create algorithms and model packages that you can use as resources in Amazon SageMaker AI and sell on AWS Marketplace.

- [Create an Algorithm Resource](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-create-algo.html): You can create an algorithm resource to use with training jobs in Amazon SageMaker AI, and you can publish it on AWS Marketplace.
- [Create a Model Package Resource](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-create-model-package.html): To create a model package resource that you can use to create deployable models in Amazon SageMaker AI and publish on AWS Marketplace specify the following information:

### [Usage of Algorithm and Model Package Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-buy.html)

Use algorithms and model packages that you create or subscribe to on AWS Marketplace to train models and get inferences in Amazon SageMaker AI.

- [Use an Algorithm to Run a Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-algo-train.html): You can create use an algorithm resource to create a training job by using the Amazon SageMaker AI console, the low-level Amazon SageMaker API, or the Amazon SageMaker Python SDK.
- [Use an Algorithm to Run a Hyperparameter Tuning Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-algo-tune.html): The following section explains how to use an algorithm resource to run a hyperparameter tuning job in Amazon SageMaker AI.
- [Use a Model Package to Create a Model](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-model-pkg-model.html): Use a model package to create a deployable model that you can use to get real-time inferences by creating a hosted endpoint or to run batch transform jobs.

### [Listings for your own algorithms and models with the AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace-sell.html)

Selling Amazon SageMaker AI algorithms and model packages is a three-step process:

- [Develop Algorithms and Models in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace-develop.html): Develop algorithms and models in Amazon SageMaker AI before you create algorithm and model package resources to use in SageMaker AI and sell on AWS Marketplace.
- [List Your Algorithm or Model Package on AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-list.html): After creating and validating your algorithm or model in Amazon SageMaker AI, list your product on AWS Marketplace.
- [Find and Subscribe to Algorithms and Model Packages on AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-find-subscribe.html): With AWS Marketplace, you can browse and search for hundreds of machine learning algorithms and models in a broad range of categories, such as computer vision, natural language processing, speech recognition, text, data, voice, image, video analysis, fraud detection, predictive analysis, and more.


## [Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-overview.html)

- [Metrics in CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html): Learn about how to monitor Amazon SageMaker AI metrics using Amazon CloudWatch to get a better perspective on how your web application or service is performing.
- [CloudWatch logs](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html): Learn about the log groups and log streams that Amazon SageMaker AI sends to Amazon CloudWatch Logs.
- [CloudTrail logs](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-using-cloudtrail.html): Learn about logging Amazon SageMaker AI with AWS CloudTrail.

### [Monitoring individual user access](https://docs.aws.amazon.com/sagemaker/latest/dg/monitor-user-access.html)

Monitor how your Amazon SageMaker Studio Classic users access AWS resources.

- [Turn on sourceIdentity for Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/monitor-user-access-how-to.html): Learn how to turn on sourceIdentity to monitor individual user resource access from Amazon SageMaker Studio Classic.
- [SageMaker AI events with EventBridge](https://docs.aws.amazon.com/sagemaker/latest/dg/automating-sagemaker-with-eventbridge.html): Automate Amazon SageMaker AI with other AWS services by using EventBridge.


## [Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/reference.html)

### [ML Frameworks and Languages](https://docs.aws.amazon.com/sagemaker/latest/dg/frameworks.html)

Amazon SageMaker AI provides native support for popular programming languages and machine learning frameworks, empowering developers and data scientists to leverage their preferred tools and technologies.

- [Apache MXNet](https://docs.aws.amazon.com/sagemaker/latest/dg/mxnet.html): The Amazon SageMaker Python SDK MXNet estimators and models and the Amazon SageMaker AI open-source MXNet container support using the MXNet deep learning framework for training and deploying models in SageMaker AI.

### [Apache Spark](https://docs.aws.amazon.com/sagemaker/latest/dg/apache-spark.html)

Learn how to setup and use Apache Spark with Amazon SageMaker AI to construct machine learning pipelines.

### [SageMaker AI Spark for Scala examples](https://docs.aws.amazon.com/sagemaker/latest/dg/apache-spark-example1.html)

SageMaker AI Spark with Scala examples.

- [Use Custom Algorithms for Model Training and Hosting on Amazon SageMaker AI with Apache Spark](https://docs.aws.amazon.com/sagemaker/latest/dg/apache-spark-example1-cust-algo.html): In , you use the kMeansSageMakerEstimator because the example uses the k-means algorithm provided by Amazon SageMaker AI for model training.
- [Use the SageMakerEstimator in a Spark Pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/apache-spark-example1-extend-pipeline.html): You can use org.apache.spark.ml.Estimator estimators and org.apache.spark.ml.Model models, and SageMakerEstimator estimators and SageMakerModel models in org.apache.spark.ml.Pipeline pipelines, as shown in the following example:
- [SageMaker AI Spark for Python (PySpark) examples](https://docs.aws.amazon.com/sagemaker/latest/dg/apache-spark-additional-examples.html): Amazon SageMaker AI provides an Apache Spark Python library (SageMaker AI PySpark) that you can use to integrate your Apache Spark applications with SageMaker AI.
- [Chainer](https://docs.aws.amazon.com/sagemaker/latest/dg/chainer.html): The Amazon SageMaker Python SDK Chainer estimators and models and the Amazon SageMaker AI open-source Chainer container support using the Chainer machine learning framework for training and deploying models in SageMaker AI.
- [Hugging Face](https://docs.aws.amazon.com/sagemaker/latest/dg/hugging-face.html): Learn how to use Hugging Face models for Natural Language Processing (NLP) with Amazon SageMaker AI.
- [PyTorch](https://docs.aws.amazon.com/sagemaker/latest/dg/pytorch.html): The Amazon SageMaker Python SDK PyTorch estimators and models and the Amazon SageMaker AI open-source PyTorch container support using the PyTorch machine learning framework for training and deploying models in SageMaker AI.

### [R](https://docs.aws.amazon.com/sagemaker/latest/dg/r-guide.html)

How to get started with R on Amazon SageMaker AI.

- [Get started with R in SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/r-sagemaker-get-started.html): Learn how to get started with R in Amazon SageMaker AI.
- [Scikit-learn](https://docs.aws.amazon.com/sagemaker/latest/dg/sklearn.html): The Amazon SageMaker Python SDK Scikit-learn estimators and models and the Amazon SageMaker AI open-source Scikit-learn container support using the Scikit-learn machine learning framework for training and deploying models in SageMaker AI.
- [SparkML Serving](https://docs.aws.amazon.com/sagemaker/latest/dg/sparkml-serving.html): The Amazon SageMaker Python SDK SparkML Serving model and predictor and the Amazon SageMaker AI open-source SparkML Serving container support deploying Apache Spark ML pipelines serialized with MLeap in SageMaker AI to get inferences.
- [TensorFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/tf.html): The Amazon SageMaker Python SDK TensorFlow estimators and models and the Amazon SageMaker AI open-source TensorFlow container support using the TensorFlow deep learning framework for training and deploying models in SageMaker AI.
- [Triton Inference Server](https://docs.aws.amazon.com/sagemaker/latest/dg/triton.html): SageMaker AI enables customers to deploy a model using custom code with NVIDIA Triton Inference Server.

### [API Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/api-and-sdk-reference.html)

Making API calls directly from code is cumbersome, and requires you to write code to authenticate your requests.

- [Programming Model for Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-prog-model.html): Making API calls directly from code is cumbersome, and requires you to write code to authenticate your requests.
- [APIs, CLI, and SDKs](https://docs.aws.amazon.com/sagemaker/latest/dg/api-and-sdk-reference-overview.html): Amazon SageMaker AI provides APIs, SDKs, and a command line interface that you can use to create and manage notebook instances and train and deploy models.
- [SageMaker AI Document History](https://docs.aws.amazon.com/sagemaker/latest/dg/doc-history.html): API version: 2017-07-24
- [Python SDK Troubleshooting](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-python-sdk-troubleshooting.html): You can use the SageMaker Python SDK to interact with Amazon SageMaker AI within your Python scripts or Jupyter notebooks.
