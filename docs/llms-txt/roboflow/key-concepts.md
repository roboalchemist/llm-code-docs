# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workspaces/key-concepts.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workspaces/key-concepts.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workspaces/key-concepts.md

# Source: https://docs.roboflow.com/workspaces/key-concepts.md

# Workspaces, Projects, and Models

Everything in Roboflow follows this structure:

Workspace → Projects → Dataset Versions → Models

### **Workspaces**

A [Workspace](https://docs.roboflow.com/workspaces/roboflow-workspaces) is the top-level container.

* It's where you and your team collaborate.
* All Projects live inside a Workspace
* Billing and [subscription plans](https://roboflow.com/pricing) are managed at the Workspace level

Think of it like a company folder that holds all your computer vision work.

### Projects

A [Project](https://docs.roboflow.com/datasets/create-a-project) lives inside a Workspace. Each Project is built around a computer vision dataset. This is where you manage:

* Images
* Annotations
* Dataset updates over time

When you create a Project, you have to choose the Project type - one of the computer vision task type:

* Object detection
* Classification
* Instance segmentation
* Keypoint detection
* Semantic segmentation
* Multimodal

This determines how your data is structured and which model architectures you can train.

### **Dataset Versions**

A [Dataset Version](https://docs.roboflow.com/datasets/dataset-versions) is a snapshot of your dataset at a specific moment in time.

* You create a Version from the current state of your Project
* Once created, it does not change
* Any future edits to images or annotations will not affect existing Versions

Which ensures reproducibility, clear tracking, and helps with model comparison.

### Models

[Models](https://docs.roboflow.com/train) are trained using Dataset Versions.

* You select a specific Dataset Version which will be used to train a model
* That model is permanently linked to that version
* Available model architectures for training will depend on your Project type

You can also [upload trained models to Roboflow](https://docs.roboflow.com/deploy/upload-custom-weights).
