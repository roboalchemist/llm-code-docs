# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/sdks/web-browser/web-inference.js.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/sdks/web-browser/web-inference.js.md

# Source: https://docs.roboflow.com/deploy/sdks/web-browser/web-inference.js.md

# Web inference.js

`inferencejs` is a JavaScript package that enables real-time inference via the browser using models trained on Roboflow.

{% hint style="info" %}
See the `inferencejs` reference [here](https://docs.roboflow.com/deploy/sdks/web-browser/web-inference.js/inferencejs-reference)
{% endhint %}

For most business applications, the [Hosted API](https://docs.roboflow.com/deploy/serverless) is suitable. But for many consumer applications and some enterprise use cases, having a server-hosted model is not workable (for example, if your users are bandwidth constrained or need lower latency than you can achieve using a remote API).

### Learning Resources

* **Try Your Model With a Webcam**: You can try out a webcam demo of a [hand-detector model here](https://demo.roboflow.com/egohands-public/9?publishable_key=rf_5w20VzQObTXjJhTjq6kad9ubrm33) (it is trained on the public [EgoHands dataset](https://universe.roboflow.com/brad-dwyer/egohands-public/)).
* **Interactive Replit Environment**: We have published a "[Getting Started](https://replit.com/@roboflow/Roboflow-Getting-Started#style.css)" project on Repl.it with an accompanying tutorial showing [how to deploy YOLOv8 models using our Repl.it template](https://blog.roboflow.com/deploy-yolov8-models-to-replit/).
* **GitHub Template**: [The Roboflow homepage](https://github.com/roboflow/homepage-demo) uses `inferencejs` to power the COCO inference widget. The README contains instructions on how to use the repository template to deploy a model to the web using GitHub Pages.
* **Documentation**: If you would like more details regarding specific functions in `inferencejs`, check out our [documentation page](https://docs.roboflow.com/deploy/sdks/web-browser/web-inference.js/inferencejs-reference) or click on any mention of a `inferencejs` method in our guide below to be taken to the respective documentation.

### Supported Models

`inferencejs` currently supports these model architectures:

* [RF-DETR](https://roboflow.com/model/rf-detr)
* Roboflow 3.0 (YOLOv8-compatible)
* YOLOv5
* [Gaze Detection](https://docs.roboflow.com/deploy/sdks/web-browser/inferencejs-reference#gazedetections)

### Installation

To add `inference` to your project, simply install using npm or add the script tag reference to your page's `<head>` tag.

```bash
npm install inferencejs
```

```html
<script src="https://cdn.jsdelivr.net/npm/inferencejs"></script>
```

## Initalizing `inferencejs`

### Authenticating

You can obtain your `publishable_key` from the Roboflow workspace settings.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-eba9dfc2cdada466d26a35f6bbb98ef8c1c972e8%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
**Note:** your `publishable_key` is used with `inferencejs`, **not** your **private** API key (which should remain secret).
{% endhint %}

Start by importing `InferenceEngine` and creating a new inference engine object

{% hint style="info" %}
`inferencejs` uses webworkers so that multiple models can be used without blocking the main UI thread. Each model is loaded through the `InferenceEngine` our webworker manager that abstracts the necessary thread management for you.
{% endhint %}

```typescript
import { InferenceEngine } from "inferencejs";
const inferEngine = new InferenceEngine();
```

Now we can load models from roboflow using your `publishable_key` and the model metadata (model name and version) along with configuration parameters like confidence threshold and overlap threshold.

```typescript
const workerId = await inferEngine.startWorker("[model name]", "[version]", "[publishable key]");
```

`inferencejs` will now start a worker that runs the chosen model. The returned worker id corresponds with the worker id in `InferenceEngine` that we will use for inference. To infer on the model we can invoke the `infer` method on the `InferenceEngine`.

Let's load an image and infer on our worker.

```typescript
const image = document.getElementById("image"); // get image element with id `image`
const predictions = await inferEngine.infer(workerId, image); // infer on image
```

{% hint style="info" %}
This can take in a variety of image formats (`HTMLImageElement`, `HTMLVideoElement`, `ImageBitmap`, or `TFJS Tensor`).
{% endhint %}

This returns an array of predictions (as a class, in this case `RFObjectDetectionPrediction` )

### Configuration

If you would like to customize and configure the way `inferencejs` filters its predictions, you can pass parameters to the worker on creation.

```typescript
const configuration = {scoreThreshold: 0.5, iouThreshold: 0.5, maxNumBoxes: 20};
const workerId = await inferEngine.startWorker("[model name]", "[version]", "[publishable key]", configuration);
```

Or you can pass configuration options on inference

```javascript
const configuration = {
    scoreThreshold: 0.5,
    iouThreshold: 0.5,
    maxNumBoxes: 20
};
const predictions = await inferEngine.infer(workerId, image, configuration);
```
