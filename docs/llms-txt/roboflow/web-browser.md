# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/web-browser.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/sdks/web-browser.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/sdks/web-browser.md

# Source: https://docs.roboflow.com/deploy/sdks/web-browser.md

# Web Browser

Roboflow provides JavaScript packages for deploying computer vision models in web browsers.&#x20;

### inference-sdk

Uses WebRTC to run inference on your video streams with the Roboflow Cloud and return live results with minimal latency.

* For live video streams
* When running Roboflow Workflows, or a model not supported on `inferencejs`
* On latency-sensitive use cases with **compute-heavy models**

<a href="web-browser/web-inference-sdk" class="button primary">Learn more about inference-sdk</a>

### inferencejs

Uses Tensorflow\.js to run inference on your images and video streams on-device.

* For images and live video streams
* On latency-sensitive use cases with **light,** [**supported models**](https://docs.roboflow.com/deploy/sdks/web-inference.js#supported-models)
* When internet access isn't continuously available (still required for initial load)

<a href="web-browser/web-inference.js" class="button primary">Learn more about inferencejs</a>

## Comparison

<table><thead><tr><th width="187.88671875">Feature</th><th>inference-sdk</th><th>inferencejs</th></tr></thead><tbody><tr><td>Processing Location</td><td>Roboflow Cloud</td><td>Browser (On Device)</td></tr><tr><td>Processing Latency</td><td>Consistent (GPU accelerated)</td><td>Dependent on user's device</td></tr><tr><td>Model Support</td><td>All Roboflow models &#x26; Roboflow Workflows</td><td><a href="web-inference.js#supported-models">Supported Models</a></td></tr><tr><td>Device Support</td><td>Wide (WebRTC is widely supported)</td><td>Wide (Tensorflow.js is widely supported)</td></tr><tr><td>Internet Required</td><td>Yes, continuously</td><td>Yes, for initial model load only</td></tr><tr><td>Network Latency</td><td>Minimal</td><td>No network latency</td></tr></tbody></table>
