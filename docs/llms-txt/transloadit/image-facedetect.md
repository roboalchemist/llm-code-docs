# Source: https://transloadit.com/docs/robots/image-facedetect.md

You can specify padding around the extracted faces, tailoring the output for your needs.

This Robot works well together with [🤖/image/resize](/docs/robots/image-resize.md) to bring the full power of resized and optimized images to your website or app.

**How to improve the accuracy:**

* Ensure that your pictures have the correct orientation. This Robot achieves the best performance when the faces in the image are oriented upright and not rotated.
* If the Robot detects objects other than a face, you can use `"faces": "max-confidence"` within your Template for selecting only the detection with the highest confidence.
* The number of returned detections can also be controlled using the `min_confidence` parameter. Increasing its value will yield less results but each with a higher confidence. Decreasing the value, on the other hand, will provide more results but may also include objects other than faces.
