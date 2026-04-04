# Source: https://docs.roboflow.com/changelog/explore-by-month/november-2025/preview-workflows-on-a-webcam-stream-from-the-web-editor.md

# Preview Workflows on a Webcam Stream from the Web Editor

<figure><img src="https://2667452268-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMR3m936tBXGm5QsAcPwe%2Fuploads%2FVU6Y5YnJ1zzWt8vbyVjd%2FScreenshot%202025-11-24%20at%2015.45.26.png?alt=media&#x26;token=db7973ee-8f5c-4b15-91e2-1ef9a3ecac5e" alt=""><figcaption></figcaption></figure>

You can now run Workflows on a webcam stream from the Roboflow Workflows web editor. This feature is useful for testing Workflows as you develop them. This is available in addition to testing a Workflow on image and video files, RTSP Streams, and USB Devices.

The FPS at which the preview runs will depend on the complexity of your Workflow; smaller object detection models, for example, should run in real time; larger object detection models or foundation models like SAM 3 will be slower and will thus run at a low FPS.

To test your Workflow on a webcam, click "Test Workflow" in the Workflows web interface, then select "Webcam" as your image input. You can then select a webcam to use. Your browser will ask you to give permission to use the webcam. Then, you can run your Workflow.

It will take several seconds for the preview to be available, after which point you will be able to see the results from your Workflow.
