# Source: https://docs.roboflow.com/roboflow/roboflow-ko/rapid/upload-data-to-rapid.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/rapid/upload-data-to-rapid.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/rapid/upload-data-to-rapid.md

# Source: https://docs.roboflow.com/rapid/upload-data-to-rapid.md

# Upload Data to Rapid

To get started with Roboflow Rapid, you first need to upload either:

* A short video that contains objects you want to identify, or;
* A few images that contain objects you want to identify.

You can upload a data from your desktop, or you can use the mobile upload feature to record a video or take a photo for use with Rapid.

If you upload a video to Rapid, you will be asked to clip its length to 10 seconds.

If you upload images, we recommend uploading at least five, although you can get started and build a prototype Rapid model with as few as one image.

### How to Upload Data to Rapid

To upload data, go to Roboflow Rapid and drag either your video or image into the web interface. Your files will then be processed and uploaded. This may take a few moments depending on the size of the files you upload. All popular image and video formats are supported (i.e. JPEG, PNG, for images, and mp4 and mov for videos).

The data you upload will then be displayed in the Rapid interface:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-373d2a85545a1f1bf549d2bf1d7e61468199dd3b%2FScreenshot%202025-11-10%20at%2010.49.57.png?alt=media" alt=""><figcaption></figcaption></figure>

Once you upload data, you will be asked what objects you are looking for. This is where you should type in labels for objects you want to identify. For example, if you want to find trucks in an image, type "truck". Rapid will also suggest a few classes relevant to the data you upload in the "Try these" section on the page.

To specify multiple classes, separate each class with a comma, like "truck, car".

Once you have set one or more classes to identify, click "Find My Objects" to start building your Rapid model.
