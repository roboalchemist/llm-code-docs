# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/manage-datasets/manage-classes.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/manage-datasets/manage-classes.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/manage-datasets/manage-classes.md

# Source: https://docs.roboflow.com/datasets/manage-datasets/manage-classes.md

# Set Dataset Classes

You can view, modify, and manage your annotation classes from within the project "Settings" page. These changes impact all images in your project (unlike some of our [preprocessing steps](https://docs.roboflow.com/datasets/image-preprocessing#modify-classes), which only impact a version). As a result, these actions are best taken when you are certain you want to make changes to all of your images.

## How to access Classes

You can access Classes by clicking "Settings" in the project sidebar.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-d89a7cddbccb396b896f6369e1bb96d96d16d017%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

## Remapping Classes

Clicking on the `Modify Classes` button to see the class remapping options available. We recommend using alphanumeric class names to maximize compatibility across computer vision tools. Roboflow does not support annotation classes with special characters aside from `-` .

From this menu, you can:

* Rename a class (by typing the new name in the `Override` column).
* Merge classes (by overriding multiple classes to the same name).
* Delete a class (by clicking the `Delete` checkbox).

**WARNING: these actions are non-reversible and potentially destructive. Ensure you are comfortable with a change before proceeding.**

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-d631f70d9cc491c30508096715bda496bff60772%2FCleanShot%202023-10-25%20at%2012.24.41.png?alt=media" alt=""><figcaption><p>Menu to remap, delete, or merge annotation classes.</p></figcaption></figure>

## Locking Classes

You can check the `Lock Annotation Classes` checkbox to prevent the creation of new classes. This is useful for ensuring annotators do not accidentally add new classes during the labeling process.
