# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/experiments.md

# Experiments

Track your machine learning experiments with detailed logging and comparison tools.

![Experiments View](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-4ce087d91471886f1be85b6abd1dbb8835fc23a2%2Fsection_experiments_1764148174995.png?alt=media)

## Creating an Experiment

Navigate to **Deep Learning Platform** → **Experiments** → Click **Create**

![Create Experiment Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-ffd63a9210658c92f41ab435e5367d37853633a5%2Fcreate_experiment_form.png?alt=media)

### Basic Information

**Experiment Name**\* (Required)

* Enter a descriptive name for the experiment
* Example: `image-classification-resnet`, `nlp-sentiment-bert`

**Description** (Optional)

* Detailed description of experiment purpose and goals

**Framework**\* (Required)

* Select your ML framework from dropdown:
  * PyTorch
  * TensorFlow
  * Scikit-learn
  * Keras
  * Others
* Default: `pytorch`

**Task Type**\* (Required)

* Select the ML task type:
  * Classification
  * Regression
  * Detection
  * Segmentation
  * Others
* Default: `classification`

**Model Type**\* (Required)

* Specify the model architecture
* Examples: ResNet, BERT, YOLO, Custom

**Project ID** (Optional)

* Link experiment to a specific project

### Training Configuration

**Epochs**\* (Required)

* Number of training epochs
* Example: `100`

**Number of training epochs** (Helper text)

* Additional context for epochs setting

**Staging batch size** (Optional)

* Batch size for staging/validation

**Learning Rate**\* (Required)

* Initial learning rate for training
* Example: `0.001`
* Helper text: "Valid learning rate"

**Loss Function**\* (Required)

* Select optimizer from dropdown:
  * Adam
  * SGD
  * RMSprop
  * Others
* Default: `adam`

**Loss Function**\* (Required)

* Select loss function:
  * Categorical Crossentropy
  * Binary Crossentropy
  * MSE
  * Others
* Default: `categorical_crossentropy`

### Environment & Resources

**Python Version**\* (Required)

* Select Python version:
  * Python 3.9
  * Python 3.10
  * Python 3.11
* Default: `python`

**GPU Required** (Checkbox)

* Check if GPU is required for training

**Memory Requirement (GB)**\* (Required)

* Required memory in GB
* Example: `8`, `16`, `32`

**Required memory in GB** (Helper text)

**CPU Cores**\* (Required)

* Number of CPU cores needed
* Example: `4`, `8`, `16`

**Number of CPU cores** (Helper text)

### Metadata

**Tags** (Optional)

* Comma-separated tags for organizing experiments
* Example: `computer-vision, production, baseline`

**Notes** (Optional)

* Additional notes or comments about the experiment

**Public Experiment** (Checkbox)

* Make experiment visible to all organization members

### Actions

* **Cancel**: Discard and close the form
* **Create Experiment**: Submit and create the experiment

## Example Configuration

```yaml
Experiment Name: resnet50-imagenet-baseline
Description: Baseline training of ResNet50 on ImageNet dataset
Framework: PyTorch
Task Type: Classification
Model Type: ResNet50
Epochs: 90
Learning Rate: 0.1
Loss Function: Adam
Loss Function: Categorical Crossentropy
Python Version: Python 3.9
GPU Required: ✓
Memory Requirement: 32 GB
CPU Cores: 16
Tags: computer-vision, classification, baseline
Public Experiment: ✓
```

## Viewing Experiment Details

To view detailed information about an experiment:

1. Navigate to **Deep Learning Platform** → **Experiments**
2. Click on an experiment from the list
3. View comprehensive details in the modal dialog

![View Experiment Details](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-4a706c615173433146d8a6bdf0c330e96c66507e%2Fexperiment_details_view.png?alt=media)

**Details Panel Sections**:

* **Basic Information**:
  * Experiment Name: e.g., "Image Classification CNN"
  * Description: Full description of the experiment
  * Framework: TensorFlow, PyTorch, etc.
  * Task Type: Classification, Regression, etc.
  * Model Type: CNN, ResNet, Custom, etc.
  * Project ID: Associated project
* **Training Configuration**:
  * Epochs: Number of training epochs (e.g., 100)
  * Batch Size: Training batch size (e.g., 32)
  * Learning Rate: Initial learning rate (e.g., 0.001)
  * Optimizer: Adam, SGD, etc.
  * Loss Function: Categorical Crossentropy, MSE, etc.
* **Environment & Resources**:
  * Python Version: e.g., Python 3.9
  * GPU Required: Checkbox status
  * Memory Requirement (GB): e.g., 8 GB
  * CPU Cores: e.g., 4 cores
* **Metadata**:
  * Tags: Comma-separated tags
  * Notes: Additional notes
  * Public Experiment: Visibility status
  * Creator and timestamps

## Editing an Experiment

To modify an experiment configuration:

1. Navigate to the experiment details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Experiment modal

![Edit Experiment Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-55d68b7c74d4f80e8e8dd3a717409298fcfab770%2Fexperiment_edit_form.png?alt=media)

4. Click **Update Experiment** to save changes

> \[!NOTE] The Edit form looks very similar to the View form, but fields become editable and you'll see an "Update Experiment" button instead of just "Cancel".

> \[!NOTE] You cannot edit core configuration (framework, resources, hyperparameters) of a running or completed experiment. To try different settings, clone the experiment instead.

**Editable Fields**:

* ✅ Description
* ✅ Tags
* ✅ Notes
* ✅ Public/Private status
* ❌ Framework (cannot edit)
* ❌ Resources (cannot edit while running)
* ❌ Hyperparameters (cannot edit)

## Cloning an Experiment

To create a copy of an experiment with modified settings:

1. Open experiment details
2. Click **Clone** button
3. Modify configuration as needed
4. Give it a new name
5. Click **Create Experiment**

**Use Cases**:

* Try different hyperparameters
* Run with more/less resources
* Test on different datasets
* Reproduce results

## Deleting an Experiment

To remove an experiment:

1. Navigate to experiment details or list
2. Click **Delete** button (trash icon)
3. Confirm deletion in the dialog
4. Experiment and associated data will be removed

> \[!WARNING] Deleting an experiment will permanently remove:
>
> * Experiment configuration
> * Training logs
> * Metrics and charts
> * Saved checkpoints (unless linked to a registered model)
> * This action cannot be undone!

**Before Deleting**:

* Export important logs or metrics
* Register any valuable models
* Download artifacts if needed
* Verify you have the correct experiment selected

## Monitoring Experiments

Once submitted, track your experiment:

**Real-time Monitoring**

* View live logs
* Monitor resource utilization (CPU, GPU, memory)
* Track metrics as they're logged
* Receive alerts on failures

**Experiment Status**

* **Pending**: Waiting for resources
* **Running**: Currently executing
* **Completed**: Finished successfully
* **Failed**: Encountered an error
* **Stopped**: Manually stopped
* **Cancelled**: Cancelled before starting

**Actions Available**

* **View Logs**: See stdout/stderr
* **View Metrics**: Charts and graphs
* **Stop**: Terminate running experiment
* **Clone**: Create a copy with same config
* **Compare**: Compare with other experiments
* **Export**: Download results and artifacts

## Comparing Experiments

Compare multiple experiments side-by-side:

1. **Select Experiments**: Check boxes for 2+ experiments
2. **Click Compare**: Opens comparison view
3. **View Differences**:
   * Hyperparameters table
   * Metrics charts (overlaid)
   * Resource usage comparison
   * Final results summary

## Best Practices

**Naming Conventions**

```
{model}-{dataset}-{variant}-{version}
Examples:
- resnet50-imagenet-baseline-v1
- bert-squad-finetuned-v2
```

**Tagging Strategy**

* **Domain**: `computer-vision`, `nlp`, `audio`
* **Task**: `classification`, `detection`, `segmentation`
* **Stage**: `exploration`, `tuning`, `production`

**Resource Optimization**

* Start with minimal resources, scale up as needed
* Use GPU only when necessary
* Monitor resource utilization

## Next Steps

* Register your trained model in [Models](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/models)
* Deploy to production via [Deployments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/deployments)
* Monitor performance in [Analytics](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/analytics)
