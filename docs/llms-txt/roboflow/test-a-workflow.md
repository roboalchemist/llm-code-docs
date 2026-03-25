# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workflows/test-a-workflow.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workflows/test-a-workflow.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workflows/test-a-workflow.md

# Source: https://docs.roboflow.com/workflows/test-a-workflow.md

# Test a Workflow

To test a workflow, click the "Test Workflow" button at the top of the Workflow editor.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-88217dc32bae909f7b759f0efa7ecf18fd8d1fac%2FScreenshot%202025-05-20%20at%2014.25.39.png?alt=media" alt=""><figcaption></figcaption></figure>

A pane will open from which you can test your Workflow:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-8d9071161a3822b88e27d7945d8f0f6dd60140fc%2FScreenshot%202025-05-20%20at%2014.26.09.png?alt=media" alt=""><figcaption></figcaption></figure>

You can test Workflows on images and video streams.

1. Images are supported on the Hosted API, Dedicated Deployments, and self-hosted servers.
2. Video streams require a Dedicated Deployment or self-hosted server to test in the UI and deploy on.

You cannot test on video files in the browser.

#### Test on an Image

To test on an image, select the Image input tab then drag and drop an image into the "Drop files here" section of the page:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-458f8f3fb9a39261d02580552e2907439b95e023%2FScreenshot%202025-05-20%20at%2014.28.02.png?alt=media" alt=""><figcaption></figcaption></figure>

Then, click "Run" to run your Workflow.

You will see the result of your Workflow on the right side of the testing interface.

By default, the Workflow will show JSON. This JSON contains all the values configured in the "Output" section of your Workflow.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-1ad72c94688bea10d497c2fae0000faf34283757%2FScreenshot%202025-05-20%20at%2014.29.25.png?alt=media" alt=""><figcaption></figcaption></figure>

If your Workflow contains an image output (i.e. a Workflow that uses a Visualization block to show the results from a model), you can preview the images by selecting the “Visual” tab in the top left corner of the testing interface.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-415d8fa95c6fd4edc40cfda166186cd66439f5f9%2FScreenshot%202025-05-20%20at%2014.29.33.png?alt=media" alt=""><figcaption></figcaption></figure>
