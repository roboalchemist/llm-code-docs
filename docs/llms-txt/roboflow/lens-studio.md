# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/lens-studio.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/sdks/lens-studio.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/sdks/lens-studio.md

# Source: https://docs.roboflow.com/deploy/sdks/lens-studio.md

# Lens Studio

With a trained model ready in Roboflow, you can deploy your model to SnapML.

## Task Support

The following task types are supported by the hosted API:

| Task Type             | Supported by Lens Studio |
| --------------------- | ------------------------ |
| Object Detection      | ✅                        |
| Classification        |                          |
| Instance Segmentation |                          |
| Semantic Segmentation |                          |

*Note: Only models trained using Roboflow Train 3.0 are supported. You can check if a model is trained on Roboflow Train 3.0 by checking the Versions page associated with your model.*

## Deploy a Model to Lens Studio

Click on “Deploy” in the Roboflow sidebar, then scroll down until you see the “Use with Snap Lens Studio” box. Click “Export to Lens Studio”.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FuDgYj9rvK3qvndktYPVY%2Fimg-1-deploy.png?alt=media&#x26;token=13518512-8709-444b-be19-d5162b7b1dd4" alt=""><figcaption></figcaption></figure>

When you click this button, a pop up will appear showing information about the classes in your model.

These classes are ordered and will be used in the next step for configuring your model in Lens Studio. Take note of the class list for future use.

In addition, two files will be downloaded:

1. The Roboflow Lens Studio template, with which you can use your weights in an application with minimal configuration, and;
2. Your model weights.

The Roboflow Lens Studio template is 100 MB, so downloading the template may take a few moments depending on your internet connection.

With the template ready, we can start setting up our model in Lens Studio.

### Configure Model in Lens Studio

If you haven’t already installed Lens Studio, go to the [Snap AR website](https://ar.snap.com/lens-studio) and download the latest version of Lens Studio. With Lens Studio installed, we are ready to start configuring our model.

For this section, we will use the Roboflow Lens Studio template. But, you can use your model weights in any application with the [MLController component](https://docs.snap.com/lens-studio/references/templates/ml/object-detection).

Unzip the Roboflow Lens Studio template you downloaded earlier, then open up the `Roboflow-Lens-Template.Isproj` file in the unzipped folder.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FWJLG4RXc16RCLnwsmBGU%2Fconfigure-model-1.png?alt=media&#x26;token=ab109009-39f2-422c-9b0b-27f453e86eb7" alt=""><figcaption></figcaption></figure>

When you open the application, you will see something like this:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FO3NYWxWq0zadkD5IyFP3%2Fconfigure-model-2.png?alt=media&#x26;token=73eeb5b9-13c3-4327-938d-5b73ba7cccaf" alt=""><figcaption></figcaption></figure>

By default, the template uses a coin counting model. For this example, we will use the playing cards model we built earlier. This application draws boxes around each prediction, but you can add your own filters and logic using Lens Studio.

Click the “ML Controller” box at the top of the left sidebar in Lens Studio:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FIWbF0ueatm5q6J8tvkMx%2Fconfigure-model-3.png?alt=media&#x26;token=fa8d6f74-5d25-4d4b-bb8f-8995ed1c0f3c" alt=""><figcaption></figcaption></figure>

This will open up a box in which you can configure your model for use in the application next to the preview window:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FGiRIs1hAKAJfJkYNW5VX%2Fconfigure-model-4.png?alt=media&#x26;token=5679992c-7b5a-4324-b373-37189d83c5e8" alt=""><figcaption></figcaption></figure>

Our demo application is configured for the coin counter example. To use your own model, first click the “ML Model” box:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FWPxbUhiIj13OcjlLYIMz%2Fconfigure-model-5.png?alt=media&#x26;token=d61f4ece-38c5-4448-810c-93ff1254d7b6" alt=""><figcaption></figcaption></figure>

Then, drag the weights downloaded from Roboflow into the pop up box:

{% embed url="<https://blog.roboflow.com/content/media/2023/06/Screen-Recording-2023-06-21-at-11.02.58.mp4>" %}

When you drag in the weights, you will be prompted with some configuration options. In the “Inputs” section of the pop up, set each “Scale” value to 0.0039. Leave the bias values as they are by default.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2F8oZGI1XaVRrNQJAqujYz%2Fconfigure-model-6.png?alt=media&#x26;token=b9b89b4d-f148-43dd-b0cb-eef0aef3683c" alt=""><figcaption></figcaption></figure>

Then, click “Import” to import your model.

### Configure Classes in Lens Studio

We now have our model loaded into Lens Studio. There is one more step: tell our model what classes we are using.

In the “Class Settings” tab below the ML Model button that we used earlier, you will see a list of classes. These are configured for a coin counter example in our demo project, but if you are working with your own Lens Studio project these values will be blank.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Feae6lDdvj7kiTo2nkoQG%2Fconfigure-lens-1.png?alt=media&#x26;token=726c62bc-4e51-4faa-a7a7-1198171f9467" alt=""><figcaption></figcaption></figure>

Here, we need to set our class names and labels. The labels must be in the order presented in the Roboflow dashboard. Here is an example of setting one of our values for the playing card application:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fxw0vXAd3xamV51VMdaAt%2Fconfigure-lens-2.png?alt=media&#x26;token=8f1771f2-0847-422e-9538-590d20cabb52" alt=""><figcaption></figcaption></figure>

We need to do this configuration for each class in our model. You must specify all classes in your model so Snap can interpret the information in the model weights.

Now our application is ready to use! You can use the “Preview” box to use your application on your computer, or demo your application on your own device using the [Pairing with Snapchat feature](https://docs.snap.com/lens-studio/references/guides/general/pairing-to-snapchat).
