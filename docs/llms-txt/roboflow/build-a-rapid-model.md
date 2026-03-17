# Source: https://docs.roboflow.com/roboflow/roboflow-ko/rapid/build-a-rapid-model.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/rapid/build-a-rapid-model.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/rapid/build-a-rapid-model.md

# Source: https://docs.roboflow.com/rapid/build-a-rapid-model.md

# Build a Rapid Model

Once you have uploaded data to Rapid, you will be taken to the interface where you build a Rapid model. This interface lets you label images and videos. The labeled data will then be used to train a Rapid model.

There are three parts to the Rapid model builder:

1. Your Files list, which lists all the videos and images you uploaded for use in building your model;
2. The preview interface, which lets you see the labels calculated by Rapid, and;
3. The labeling tool (the "What object are you looking for?" panel) which lets you type text prompts and send them to Roboflow Rapid to label data.

Rapid has a text prompt-driven interface. This means you can type in the name of what you want to find and ask Rapid to find it for you.

Here is an example showing the Rapid interface:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-5b553c25b531aeed841e2817719fcd3d7566df14%2FScreenshot%202025-11-10%20at%2010.53.13.png?alt=media" alt=""><figcaption></figcaption></figure>

### Find an Object

To find an object, type in a label that corresponds to the type of object you want to identify in the "What object are you looking for?" input field. For example, if you are looking for a truck, you can type in the prompt "truck".

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-428ed30f738b3b0b26dadf4364747cb7e3d1c8b3%2FScreenshot%202025-11-10%20at%2011.00.31.png?alt=media" alt=""><figcaption></figcaption></figure>

Click "Find Objects" to ask Rapid to find all instances of the object you want to find.

Rapid will then show labels corresponding with your text prompt in the preview interface.

You can prompt Rapid as many times as you would like to find different kinds of objects.

If you are labeling a video, Rapid will by default label the frame you are viewing (which is the first frame in the video by default). Once you go to the "Review Model" stage of the Rapid model builder, Rapid will be run on your full video for you.

### Adjust Rapid's Sensitivity

Rapid may identify too many or too few instances of the object you want to identify. If this happens, you can adjust the "Objects" slider on the right side of the Rapid interface. Keep moving the slider until the preview interface shows all the objects you want to label and shows few or no false positives.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-42e8d940aa349a74795f1144951dfcfd85aab806%2FScreenshot%202025-11-10%20at%2011.00.34.png?alt=media" alt=""><figcaption></figcaption></figure>

### Navigate Between Files

To see how your Rapid prompts do on different images or videos you uploaded, click on the file you want to preview in your Files list:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3126d24db345ecc783e1b9593522ac89bf7d8f35%2FScreenshot%202025-11-10%20at%2011.02.17.png?alt=media" alt=""><figcaption></figcaption></figure>

### Review Your Model

Once you have set your text prompts, click the "Review Model" button:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cd4414dc53a12abb0da0e5ea39f02234076a5c7f%2FScreenshot%202025-11-10%20at%2011.03.55.png?alt=media" alt=""><figcaption></figcaption></figure>

When clicked, the "Review Model" button will take you to a web page where you can preview Rapid on all of your input images and videos.
