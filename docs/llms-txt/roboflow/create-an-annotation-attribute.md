# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/manage-datasets/create-an-annotation-attribute.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/manage-datasets/create-an-annotation-attribute.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/manage-datasets/create-an-annotation-attribute.md

# Source: https://docs.roboflow.com/datasets/manage-datasets/create-an-annotation-attribute.md

# Create an Annotation Attribute

Annotation attributes (also referred to as "subclasses") can be added to your annotations using class specific attributes. These attributes are included in your dataset exports for object detection and segmentation projects.

{% hint style="info" %}
This feature is exclusively available for Enterprise customers. [See our pricing page](https://roboflow.com/pricing) to learn more about how to access this feature.
{% endhint %}

## Create an Attribute

To create an Annotation Attribute, first click "Classes & Tags" in your Project sidebar:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-7602336f6bd7b796e68178f6373ecc9ce4ebf60a%2FScreenshot%202025-06-09%20at%2011.55.16.png?alt=media" alt=""><figcaption></figcaption></figure>

On the Classes & Tags page you can see all of your dataset classes. You can also add Annotation Attributes to a class that you can use on images in your dataset.

To add an Annotation Attribute, click the plus icon in the "Attributes" column of the class to which you want to add the attribute:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-ac8b867cccf11e21957c84b963085e80044af5df%2FScreenshot%202025-06-09%20at%2011.56.02.png?alt=media" alt=""><figcaption></figcaption></figure>

A window will appear in which you can set a name for the Annotation Attribute:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-03a7da0f5d207c72b9bc0553a5b15b8d86797a61%2FScreenshot%202025-06-09%20at%2011.56.37.png?alt=media" alt=""><figcaption></figcaption></figure>

Click "Save" to save the Annotation Attribute.

Your Attribute will then show up next to the corresponding class:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-409d4c6a39f3dc05321ba7b7f37bfdccf755664b%2FScreenshot%202025-06-09%20at%2011.58.46.png?alt=media" alt=""><figcaption></figcaption></figure>

### Add an Attribute to an Annotation

After creating an annotation you can add attributes to your annotation in the Class Selector.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-5f445d5c5b8465e2e264f13677b22237b22ac942%2Fimage.png?alt=media" alt="" width="240"><figcaption></figcaption></figure>

## Export Annotations with Attributes

To export annotations with attributes from Roboflow, refer to our [Export Data](https://docs.roboflow.com/datasets/dataset-versions/exporting-data) guide.

{% hint style="warning" %}
Annotation attribute information is only included in [COCO and COCO Segmentation formats](https://roboflow.com/formats).
{% endhint %}
