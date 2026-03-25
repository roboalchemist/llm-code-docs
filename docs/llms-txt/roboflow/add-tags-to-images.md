# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/manage-datasets/add-tags-to-images.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/manage-datasets/add-tags-to-images.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/manage-datasets/add-tags-to-images.md

# Source: https://docs.roboflow.com/datasets/manage-datasets/add-tags-to-images.md

# Add Tags to Images

Roboflow provides an image tagging feature. This feature allows you to assign tags to images during upload. You can use these tags for batch assignment for labeling, enabling greater precision when assigning images for labeling. Furthermore, you can use image tags as a parameter in the Roboflow dataset search associated with your dataset.

### Assigning a Tag During Upload

You can assign tags during data upload both in the web interface and using the [REST API and Python SDK](https://docs.roboflow.com/api-reference/images/upload-api). The image below shows how to specify tags to associate with images uploaded using the web interface:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-569d72ae83ced7c04f9d632d087ae34f52a0b2f5%2FScreenshot%202024-09-19%20at%204.27.28%E2%80%AFPM.png?alt=media" alt="Opening the Tag menu prior to image Upload"><figcaption><p>Opening the Tag menu prior to image Upload</p></figcaption></figure>

### Apply Tags in the Images Tab

To apply tags in the Image tab, click on the images to which you want to apply tags, click the "Images Selected" button in the top right corner of the page, and then click "Apply tags". This will allow you to add an arbitrary number of tags to the selected images.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-56853073d5dd3135ffbabdd3e6750c1ddfed6c17%2FScreenshot%202024-09-19%20at%204.28.11%E2%80%AFPM.png?alt=media" alt=""><figcaption><p>Applying Tags to selected images</p></figcaption></figure>

### Quickly Rename or Delete Tags Across a Project

To rename a tag or delete a tag across all of the images in a project, click the "Tags" tab in the "Settings" page for your project. Then, click the "Modify Tags" button in the top right of the page to open a dialog that allows you to make changes in bulk.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-e3ab0500df6ee3530539baa2617f448eafa57e1b%2FScreenshot%202024-09-19%20at%204.32.25%E2%80%AFPM.png?alt=media" alt=""><figcaption><p>The tag management dialog that appears when you click "Modify Tags"</p></figcaption></figure>

### Filter Images by Tag

You can filter images using tags in the Assign page on the Roboflow dashboard:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-24be10a04767b10547c866e39c611fa2b372e6f7%2FScreenshot%202024-09-19%20at%204.30.30%E2%80%AFPM.png?alt=media" alt="Filtering by Existing dataset Tags from within the Assign tool"><figcaption><p>Filtering by Existing dataset Tags from within the Assign tool</p></figcaption></figure>

### Use Tags to Curate Data in Versions

The [Filter by Tag](https://docs.roboflow.com/datasets/image-preprocessing#filter-by-tag) preprocessing step allows you to create Versions of your dataset that include or exclude specific data. Use this preprocessing step to train or export only a curated slice of your data.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-25a8907806389c72b595b3dede145d1840cd6825%2FCleanShot%202024-12-20%20at%2009.48.12%402x.png?alt=media" alt=""><figcaption><p>Use the "Filter by Tag" preprocessing step to require or block certain tags from entering a dataset version.</p></figcaption></figure>
