# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/web-browser/inference.js/inferencejs-requirements.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/sdks/web-browser/web-inference.js/inferencejs-requirements.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/sdks/web-browser/web-inference.js/inferencejs-requirements.md

# Source: https://docs.roboflow.com/deploy/sdks/web-browser/web-inference.js/inferencejs-requirements.md

# inferencejs Requirements

{% hint style="info" %}
Learn more about `inferencejs` [here](https://docs.roboflow.com/deploy/sdks/web-browser) and see the [`inferencejs` reference](https://docs.roboflow.com/deploy/sdks/web-browser/web-inference.js/inferencejs-reference)
{% endhint %}

**Minimum Browser Versions**

* **Chrome**: 61+
* **Firefox**: 60+
* **Safari**: 15.4+
* **Edge (Chromium-based)**: 79+
* **Opera**: 48+

{% hint style="info" %}
These are minimum browser versions based on available MDN feature-support information of browser features `inferencejs` uses and is meant for basic guidance.\
\
Not all of these browsers have been tested on, and there may be instances where a higher version than what is listed is required for use. These minimums are subject to change
{% endhint %}

**Required Browser Features**

* Web Workers (`Worker` API)
* `navigator.hardwareConcurrency`
* `navigator.mediaDevices.getUserMedia`
* `createImageBitmap`
* ES6+
* ESM
* Promises & Fetch API
