# Source: https://docs.edgeimpulse.com/studio/projects/post-processing/object-tracking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Object tracking

Object Tracking is a postprocessing layer that allows you to track bounding boxes across inference runs, turning raw bounding boxes into stable “tracked” detections. This can significantly reduce jitter and provide continuity of object labels across frames. Object tracking works both for models trained in Edge Impulse, as well as through [Bring your own model (BYOM)](/studio/projects/dashboard/byom).

<Frame caption="Object tracking">
  <img src="https://mintcdn.com/edgeimpulse/Z1Offd_0m7N7yP2K/.assets/images/object-tracking/object-tracking.png?fit=max&auto=format&n=Z1Offd_0m7N7yP2K&q=85&s=78c9d48ce0e6510d019f3d15ce471ff2" width="1340" height="1000" data-path=".assets/images/object-tracking/object-tracking.png" />
</Frame>

## How object tracking works

Object tracking maintains ongoing traces of detected objects across video frames by aligning new detections with existing traces. Each frame, the system matches detections to traces—if a detection matches a trace, the trace is updated; if not, a new trace is started. If a trace doesn't match any detection, it is closed after a short grace period, allowing for occasional missed detections. This approach enables robust tracking, especially for object counting by monitoring when traces cross defined regions.

To align detections and traces, the system uses a cost function based on the overlap (for Bounding Box models) or distance (for Centroid models) between predicted and detected positions. Trace predictions are made using Kalman filters, which help smooth object movement and handle missing detections for short periods.

**Best for:**

* Linear, predictable motion (e.g., vehicles on a road, products on a conveyor belt)
* Tracking to facilitate counting, where a stable detection of unique objects crossing a line or region is required

**Not ideal for:**

* Objects with sharp, sudden changes in direction
* Highly random or erratic motion with overlapping objects (e.g., bouncing balls, swarming insects)
* Tracking where smoothness of motion around an entire scene is critical

This method provides stable, continuous object identities across frames, but works best when object movement is relatively smooth and predictable.

## Configuring object tracking

### 1. Enabling object tracking

To enable the Object Tracking feature:

1. Open your Edge Impulse project.
2. Go to the **Dashboard**.
3. Scroll down to 'Administrative zone' and enable **Post-processing / object tracking**.
4. Click **Save experiments**.

You'll now have a new entry in the left navigation bar called "Post-processing".

<Frame caption="Post-processing in the navigation bar">
  <img src="https://mintcdn.com/edgeimpulse/Z1Offd_0m7N7yP2K/.assets/images/object-tracking/navbar.png?fit=max&auto=format&n=Z1Offd_0m7N7yP2K&q=85&s=911d5a8882023f180eaa95401a187ab8" width="478" height="814" data-path=".assets/images/object-tracking/navbar.png" />
</Frame>

### 2. Uploading data

To configure object tracking you'll need to upload one or more video files of representable scenes. E.g. a video of your production line if you want to track products on a conveyor belt; or a video of people walking around if you're building intruder detection systems. This data does not need to be labeled.

Frames are squashed before running inference. For the most representative results, use the same aspect ratio as your impulse, for example if your model input is 320x320 with "fit-short" as the resize type you should crop your video to this aspect ratio before uploading.

To upload this data, go to **Data acquisition > Post-processing**; and click the upload icon. We support video files in the most common formats, but there's a 100MB file size limit.

<Frame caption="Post-processing dataset">
  <img src="https://mintcdn.com/edgeimpulse/Z1Offd_0m7N7yP2K/.assets/images/object-tracking/dataset.png?fit=max&auto=format&n=Z1Offd_0m7N7yP2K&q=85&s=80a6ce2f26e41debe9822f78d4378171" width="1028" height="1000" data-path=".assets/images/object-tracking/dataset.png" />
</Frame>

### 3. Tuning object tracking parameters

After you've uploaded your data you can go to **Post-processing** (in the left navigation bar). This UI allows you to quickly iterate over all object tracking parameters to find the perfect configuration for your specific use case. This UI can also be used to see raw bounding box predictions overlaid onto your videos, which is a great way to assert model performance.

<Frame caption="Object tracking Configuration - mobile client">
  <img src="https://mintcdn.com/edgeimpulse/Z1Offd_0m7N7yP2K/.assets/images/object-tracking/ui2.png?fit=max&auto=format&n=Z1Offd_0m7N7yP2K&q=85&s=9f5804acf021f87e473981dfe77665cc" width="1230" height="1000" data-path=".assets/images/object-tracking/ui2.png" />
</Frame>

*Configuring the object tracking parameters to identify people.*

#### Object tracking parameter descriptions

It is important to consider the target framerate of the camera on your deployed device when configuring these parameters. If you're experimenting with a 30fps video here, make sure you're limiting your on-device framerate to 30fps and vice versa.

* **Keep Grace**: The number of frames an object is kept for after it disappears (i.e., is not detected). This allows for brief occlusions or missed detections without immediately ending the object's trace.
* **Max. observations**: The maximum number of observations (detections) to use for matching and maintaining stable tracking of an object. Higher values can help smooth out noise but may increase latency.
* **Threshold**: The matching threshold for associating detections with existing traces:
  * For **centroid-based models** (like FOMO): the Euclidean distance (in pixels) between centroids.
  * For **bounding box models** (like MobileNetV3): the Intersection over Union (IoU) threshold between bounding boxes to decide if objects are the same between frames. Here is a visualisation of the overlap:
  <Frame caption="IoU Threshold Parameter Visualisation">
    <img src="https://mintcdn.com/edgeimpulse/Mti_c8GM-j8PYeEi/.assets/images/object-tracking/iou_comparison.png?fit=max&auto=format&n=Mti_c8GM-j8PYeEi&q=85&s=422accc5f7600a13ffa921159489dea4" width="1500" height="300" data-path=".assets/images/object-tracking/iou_comparison.png" />
  </Frame>

When you're happy with the results, click **Save** to store the configuration then click **Render Preview** to see the changes in action. The first render will take a bit longer, but the results are cached so further updates will be faster.

### 4. Deploying your model

Once you've configured object tracking, all deployments (Linux, Mobile, EON Compiler, C++ library, WebAssembly, etc.) that contain an Object Detection block will automatically include the object tracking postprocessing layer. 🚀

## Re-configuring object tracking thresholds at runtime

<Frame caption="Object tracking Configuration - mobile client">
  <img src="https://mintcdn.com/edgeimpulse/Z1Offd_0m7N7yP2K/.assets/images/object-tracking/object-tracking-config.gif?s=1a89f4cf6cf90a57cbc98ec72deaa7bf" width="2056" height="958" data-path=".assets/images/object-tracking/object-tracking-config.gif" />
</Frame>

When you have built a model that includes Object Tracking postprocessing, you can dynamically configure the tracking thresholds.

### Linux CLI

Use `edge-impulse-linux-runner --model-file <model.eim>`.

* The runner’s interactive console (and web UI via `http://localhost:PORT`) now includes configurable tracking thresholds (click the 'gear' icon).

### Mobile client

If you’re running your impulse in the Edge Impulse mobile client, you can configure thresholds in the UI as well (click the 'gear' icon).

### Node.js SDK

In the Node.js SDK, there is a new function to set these thresholds at runtime:

```javascript  theme={"system"}
// classifier is an instance of EdgeImpulseClassifier
classifier.setLearnBlockThreshold({
  keepGrace: 5,
  maxObservations: 5,
  iouThreshold: 0.5,
});
```

### Code deployments (C++)

For C++ library deployments, you can configure thresholds in `model-parameters/model_variables.h` (name may vary based on your project’s generated files). A typical configuration might look like:

```c  theme={"system"}
const ei_object_tracking_config_t ei_posprocessing_config_9 = {
  1,       /* implementation_version */
  5,       /* keep_grace */
  5,       /* max_observations */
  0.5000f, /* iou_threshold */
  true     /* use_iou */
};
```

You can update the configuration at runtime through `set_threshold_postprocessing`.

## Comparing object tracking vs. standard object detection

A simple way to see the difference between raw bounding boxes and tracked bounding boxes:

<Frame caption="Standard object detection vs object tracking ">
  <img src="https://mintcdn.com/edgeimpulse/Z1Offd_0m7N7yP2K/.assets/images/object-tracking/object-tracking-jitter.gif?s=18e5bc93daa2ebe1ce64318249776d0a" width="1832" height="634" data-path=".assets/images/object-tracking/object-tracking-jitter.gif" />
</Frame>

#### Terminal 1:

```bash  theme={"system"}
PORT=9200 edge-impulse-linux-runner --model-file ./model-with-object-tracking.eim
```

#### Terminal 2:

```bash  theme={"system"}
PORT=9201 edge-impulse-linux-runner --model-file ./model-without-object-tracking.eim
```

Open `http://localhost:9200` and `http://localhost:9201` in two separate browser windows and observe the difference in bounding box stability.
You’ll see smoother, more persistent bounding boxes with object tracking enabled.

## Accessing tracked objects in the inference output

### C++ libraries

```cpp  theme={"system"}
ei_impulse_result_t result;

// ... run inference ...

for (uint32_t i = 0; i < result.postprocessed_output.object_tracking_output.open_traces_count; i++) {
  ei_object_tracking_trace_t trace = result.postprocessed_output.object_tracking_output.open_traces[i];

  // Access tracked object data:
  // trace.id, trace.label, trace.x, trace.y, trace.width, trace.height
}
```

### WebAssembly

```javascript  theme={"system"}
let result = classifier.classify(/* frame or image data */);
console.log(result.object_tracking_results);
```

### EIM files

When reading inference metadata from an EIM file, look under the `object_tracking` field to retrieve tracked objects.

## Advanced usage

Looking for a more complex example? Check out the Model Cascade approach, which chains together an Object Tracking model with an LLM (e.g., GPT-4):

* [example-llm-model-cascade-object-tracking](https://github.com/edgeimpulse/example-llm-model-cascade-object-tracking)

## Troubleshooting

If you encounter any issues with object tracking, please reach out to your solutions engineer for assistance.


Built with [Mintlify](https://mintlify.com).