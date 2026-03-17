# Source: https://docs.roboflow.com/developer/authentication/workspace-and-project-ids.md

# Workspace and Project IDs

To run inference on your model, or to query the Roboflow API endpoints associated with your project, you will need three pieces of information:

1. Your project ID
2. Your model version number
3. [Your API key](https://app.roboflow.com/settings/api)

### How to Retrieve a Project ID and Version Number

To get both the project ID and version number, navigate to "Models" page inside your Project. It will list all fine-tuned models, and each one contains the ID that you can easily copy:

<figure><img src="https://1284666567-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fe5GEiPeDoFksvZv1vH3A%2Fuploads%2Fyj9l0QYN2RorQRomA2r4%2Fimage.png?alt=media&#x26;token=c201480d-3f2f-4ed6-b8a9-af78478d5fa8" alt=""><figcaption></figcaption></figure>

In the screenshot above, the `dino-game-rcopt-fjzyh` is the Project Id, and the numbers after the `/` are the model version numbers.
