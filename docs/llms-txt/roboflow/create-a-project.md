# Source: https://docs.roboflow.com/developer/python-sdk/create-a-project.md

# Source: https://docs.roboflow.com/developer/rest-api/create-a-project.md

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/create-a-project.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/create-a-project.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/create-a-project.md

# Source: https://docs.roboflow.com/datasets/create-a-project.md

# Create a Project

Before you train a model, you need to create a Project.

A Project contains images and annotations. This data can then be turned into a dataset version, a snapshot of your data frozen in time. Versions can then be used to train models.

### Create a Project

First, go to the Roboflow dashboard. Then, click "Create New Project":

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-7186a9c38343d572b4bece7298847e488f123a21%2FScreenshot%202024-07-10%20at%2009.58.35.png?alt=media" alt=""><figcaption></figcaption></figure>

You will be taken to a page where you can create a new project:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-16c3ec9c741c6ab1995575a3bbda8cb292c33fcc%2FScreenshot%202024-07-10%20at%2009.59.17.png?alt=media" alt=""><figcaption></figcaption></figure>

On this page, you will need to fill out:

1. **A project type**.
   1. ***Object Detection***: Find the location of objects in an image.
   2. ***Single-Label Classification***: Given a limited set of categories, assign a label to an image.
   3. ***Multi-Label Classification***: Given a limited set of categories, assign an arbitrary number of labels that are relevant to the image.
   4. ***Instance Segmentation***: To the pixel level, find the location of objects in an image.
   5. ***Semantic Segmentation***: To the pixel level, find the location of objects in an image and create unique references for each object found.
   6. ***Keypoint Detection***: Find the location of objects and their keypoints in an image. Commonly used for determining the pose of an object.
2. **A project name:** The name of your project.
3. **What you are detecting**: A label that summarizes what you are detecting.

When you have specified these values, submit the form to create the project.

*If you would like to see another type of project supported you can select the option from the dropdown of project types to indicate your interest.*

{% hint style="info" %}
If you are on a free plan, your datasets and models will be [available on Roboflow Universe](https://docs.roboflow.com/universe/what-is-roboflow-universe). If you are on a paid plan, you can create private projects. Private projects are only accessible to your Workspace and are never public.
{% endhint %}
