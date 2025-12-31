# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/datasets.md

# Datasets

Organize and version your training data.

![Datasets View](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-67828deab295ac67e068436d89e9815175df2a88%2Fsection_datasets_1764148213987.png?alt=media)

## Creating a Dataset

Navigate to **Deep Learning Platform** → **Datasets** → Click **Create**

![Create Dataset Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-55febeb56bc870c92191dc87ba81eda2bfa53a84%2Fcreate_dataset_form.png?alt=media)

### Basic Information

**Dataset Name**\* (Required)

* Enter a descriptive name for the dataset
* Example: `imagenet-1k`, `coco-2017`, `custom-dataset`

**Version**\* (Required)

* Semantic version (major.minor.patch)
* Default: `1.0.0`
* Helper text: "Semantic version (major.minor.patch)"

**Description**\* (Required)

* Detailed description of dataset contents and purpose

### Dataset Configuration

**Dataset Type**\* (Required)

* Select data type from dropdown:
  * Tabular
  * Image
  * Text
  * Audio
  * Video
  * Others
* Default: `tabular`

**Task Type**\* (Required)

* Select task type:
  * Classification
  * Regression
  * Detection
  * Segmentation
  * Others
* Default: `classification`

**Data Format**\* (Required)

* Select file format:
  * CSV
  * JSON
  * Parquet
  * TFRecord
  * Others
* Default: `csv`

**Status**\* (Required)

* Current dataset status:
  * Uploading
  * Processing
  * Ready
  * Failed
* Default: `uploading`

### Metadata

**Tags** (Optional)

* Comma-separated tags for organization
* Example: `computer-vision, training, augmented`

**License** (Required)

* Select license:
  * MIT
  * CC BY 4.0
  * CC0
  * Apache 2.0
  * Proprietary
* Default: `MIT`

**Public Access** (Checkbox)

* Make dataset accessible to all organization members

### Actions

* **Cancel**: Discard and close
* **Create Dataset**: Submit and create the dataset

## Example Configuration

```yaml
Dataset Name: imagenet-subset-2024
Version: 1.0.0
Description: ImageNet subset with 100 classes for quick experimentation
Dataset Type: Tabular
Task Type: Classification
Data Format: CSV
Status: Uploading
Tags: computer-vision, subset, training
License: MIT
Public Access: ✓
```

## Viewing Dataset Details

To view detailed information about a dataset:

1. Navigate to **Deep Learning Platform** → **Datasets**
2. Click on a dataset from the list
3. View comprehensive details in the modal dialog

![View Dataset Details](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-e0a84a22b6107276f1650d472c08996990e68472%2Fdataset_details_view.png?alt=media)

**Details Panel Sections**:

**Basic Information**:

* **Dataset Name**: e.g., "Time Series Sales Data"
* **Version**: Semantic version (e.g., 1.1.0)
* **Description**: Full description of the dataset

**Dataset Configuration**:

* **Dataset Type**: Time Series, Tabular, Image, Text, Audio, Video
* **Task Type**: Forecasting, Classification, Regression, etc.
* **Data Format**: CSV, JSON, Parquet, TFRecord, etc.
* **Status**: Processing, Uploading, Ready, Failed

**Metadata**:

* **Tags**: Comma-separated tags (e.g., "time-series,forecasting,sales,multivariate,business")
* **License**: Proprietary, MIT, CC BY 4.0, etc.
* **Public Access**: Checkbox for visibility

## Editing a Dataset

To update dataset information:

1. Open dataset details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Dataset modal

![Edit Dataset Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-b54763aed9953abaa8ef2942e75f62934776132e%2Fdataset_edit_form.png?alt=media)

4. Click **Update Dataset** to save changes

> \[!NOTE] The Edit form is identical to the View form, but with editable fields and an "Update Dataset" button.

**Editable Fields**:

* ✅ Description
* ✅ Tags
* ✅ License
* ✅ Public Access
* ❌ Dataset Name (cannot edit)
* ❌ Version (create new version instead)
* ❌ Data Type (cannot edit)
* ❌ Data Format (cannot edit)

## Downloading Dataset

To download dataset files:

1. Open dataset details
2. Click **Download** button
3. Select download format:
   * Original format
   * Compressed archive
   * Specific splits (train/val/test)
4. Download will start

**Download Options**:

* Full dataset
* Specific splits only
* Sample subset
* Metadata only

## Creating a New Version

To create a new version of a dataset:

1. Open dataset details
2. Click **New Version** button
3. Enter new version number
4. Upload updated data
5. Document changes in description
6. Click **Create**

**When to Version**:

* Added new samples
* Fixed data errors
* Changed preprocessing
* Updated annotations
* Removed corrupted files

## Deleting a Dataset

To remove a dataset:

1. Navigate to dataset details
2. Click **Delete** button
3. Confirm deletion

> \[!WARNING] You cannot delete a dataset that is being used by running experiments. Stop experiments first.

**Before Deleting**:

* Check for experiments using this dataset
* Download data if needed
* Update documentation
* Consider archiving instead

## Dataset Versioning

**When to Create New Version**:

* Added new samples
* Fixed annotation errors
* Changed preprocessing
* Updated splits
* Removed corrupted data

## Best Practices

**Organization**:

* Use consistent naming conventions
* Document data collection process
* Include data cards/datasheets
* Provide sample data for preview

**Quality Control**:

* Validate data integrity
* Check for label errors
* Monitor class balance
* Document known issues

## Next Steps

* Use dataset in [Experiments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/experiments)
* Track data lineage
* Monitor usage in [Analytics](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/analytics)
