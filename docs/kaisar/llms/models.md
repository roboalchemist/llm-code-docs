# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/models.md

# Models

Manage your trained models with versioning and metadata.

![Models View](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-af01ec57317f84a9468adf2d3d47fd475a3088cb%2Fsection_models_1764148186732.png?alt=media)

## Registering a Model

Navigate to **Deep Learning Platform** → **Models** → Click **Create**

![Create Model Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-ff260cc30187e48676b271d5ccd07387cd263288%2Fcreate_model_form.png?alt=media)

### Basic Information

**Model Name**\* (Required)

* Enter a descriptive name for the model
* Example: `resnet50-imagenet`, `bert-sentiment`

**Version**\* (Required)

* Semantic version (major.minor.patch)
* Default: `1.0.0`
* Helper text: "Semantic version (major.minor.patch)"

**Description** (Optional)

* Detailed description of the model

### Model Configuration

**Framework**\* (Required)

* Select framework from dropdown:
  * PyTorch
  * TensorFlow
  * ONNX
  * Scikit-learn
  * Others

**Task Type**\* (Required)

* Select task type:
  * Classification
  * Regression
  * Detection
  * Segmentation
  * Others
* Default: `classification`

**Model Type**\* (Required)

* Select model architecture:
  * Custom
  * ResNet
  * BERT
  * YOLO
  * Others
* Default: `custom`

**Status**\* (Required)

* Select model status:
  * Draft
  * Training
  * Completed
  * Deployed
  * Archived
* Default: `draft`

### Metadata

**Tags** (Optional)

* Comma-separated tags for organization
* Example: `production, v1, optimized`

**Author** (Optional)

* Model creator or team name

**License** (Optional)

* Select license from dropdown:
  * MIT
  * Apache 2.0
  * GPL
  * Proprietary
  * Others

**Public Access** (Checkbox)

* Make model accessible to all organization members

### Actions

* **Cancel**: Discard and close
* **Create Model**: Submit and register the model

## Example Configuration

```yaml
Model Name: resnet50-imagenet-v1
Version: 1.0.0
Description: ResNet50 trained on ImageNet-1K, 76.5% top-1 accuracy
Framework: PyTorch
Task Type: Classification
Model Type: Custom
Status: Draft
Tags: computer-vision, production
Author: ML Team
License: MIT
Public Access: ✓
```

## Viewing Model Details

To view detailed information about a model:

1. Navigate to **Deep Learning Platform** → **Models**
2. Click on a model from the list
3. View comprehensive details in the modal dialog

![View Model Details](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-168d7d8cb797261acfaed323e347d5cfb595d739%2Fmodel_details_view.png?alt=media)

**Details Panel Sections**:

**Basic Information**:

* **Model Name**: e.g., "XGBoost House Prices"
* **Version**: Semantic version (e.g., 1.0.3)
* **Description**: Full description of the model and its purpose

**Model Configuration** (First Section):

* **Model Name**: Display name
* **Version**: Current version number
* **Description**: Detailed model description

**Model Configuration** (Second Section):

* **Framework**: XGBoost, PyTorch, TensorFlow, etc.
* **Task Type**: Regression, Classification, etc.
* **Model Type**: Custom, ResNet, BERT, etc.
* **Status**: Training, Draft, Completed, Deployed

**Metadata**:

* **Tags**: Comma-separated tags for organization
* **Author**: Model creator or team name
* **License**: Model license information

## Editing a Model

To update model information:

1. Open model details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Model modal

![Edit Model Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-afba7be39b38d31db193e62de66b7ee09ab66e7e%2Fmodel_edit_form.png?alt=media)

4. Click **Update Model** to save changes

> \[!NOTE] The Edit form is identical to the View form, but with editable fields and an "Update Model" button.

**Editable Fields**:

* ✅ Description
* ✅ Tags
* ✅ Status (Draft, Training, Completed, Deployed, Archived)
* ✅ Author
* ✅ License
* ✅ Public Access
* ❌ Model Name (cannot edit)
* ❌ Version (create new version instead)
* ❌ Framework (cannot edit)

## Creating a New Version

To create a new version of an existing model:

1. Open model details
2. Click **New Version** button
3. Enter new version number (e.g., 1.1.0 → 1.2.0)
4. Upload new model artifacts
5. Update description and metrics
6. Click **Create**

**Version Guidelines**:

* **Major** (2.0.0): Breaking changes, new architecture
* **Minor** (1.1.0): Improvements, new features
* **Patch** (1.0.1): Bug fixes, minor updates

## Downloading Model Artifacts

To download model files:

1. Open model details
2. Navigate to **Artifacts** section
3. Click **Download** on desired files:
   * Model weights (.pt, .h5, .onnx)
   * Configuration files
   * Tokenizers/preprocessors
   * README and documentation
4. Files will be downloaded to your local machine

## Deleting a Model

To remove a model:

1. Navigate to model details
2. Click **Delete** button
3. Confirm deletion

> \[!WARNING] You cannot delete a model that is currently deployed. Stop all deployments first.

**Before Deleting**:

* Check for active deployments
* Download artifacts if needed
* Update dependent systems
* Archive instead of delete if uncertain

## Model Lifecycle Management

**Model Stages**:

1. **Development**: Under active development
2. **Staging**: Ready for testing
3. **Production**: Deployed to production
4. **Archived**: No longer in use

## Model Versioning Best Practices

**Version Numbering**:

* `1.0.0`: Initial production release
* `1.1.0`: New features, improved accuracy
* `1.1.1`: Bug fix, no architecture change
* `2.0.0`: New architecture, breaking changes

## Next Steps

* Deploy your model via [Deployments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/deployments)
* Link to training [Experiments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/experiments)
* Monitor in [Analytics](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/analytics)
