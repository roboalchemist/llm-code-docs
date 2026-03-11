# Source: https://docs.buildnatively.com/guides/integration/audio-recorder.md

# Audio Recorder

* [Bubble.io Plugin](#element-natively-audio-recorder)
* [JavaScript SDK](#nativelyaudiorecorder)

### 🧋 Bubble.io Plugin

#### \[Element] Natively - Audio Recorder&#x20;

#### Events:

* **Recorder Result Updated** - get called after finished recording
* **Recorder Cancelled** - get called after user close recorder (without recordings)
* **File Uploaded** - get called after the file was successfully uploaded on S3 (You can find a file URL in element's state)
* **File Size over limit** - Triggered when file size is more then File Size Limit param

#### States:

* **Recorder Result (Base64)** - Base64 string representation of a file, can be used for custom uploading
* **Recorder Result (Content Type)** - image/png, image/jpeg or video/mp4
* **Uploaded File URL** - Amazon S3 file URL
* **File Size** - size of latest camera result file in KB

#### Actions:

* **Show Recorder**
  * **Upload File** - checkbox (Upload file to Amazon S3)
  * **File Name** - will be used if **Upload File** is checked
  * **File Size Limit** - (in KB) prevent uploading big files to Bubble's amazon S3
  * **Max Duration (iOS) -** max duration of recording in seconds (v2.8.2)

### 🛠 JavaScript SDK

#### NativelyAudioRecorder

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const recorder = new NativelyAudioRecorder()
const show_recorder_callback = function (resp) {
    console.log(resp.base64); // base64 string of media file
    console.log(resp.content_type); // "audio/m4a" for ios or "audio/wav" for android
    console.log(resp.size); // 1024 <- file size in KB
    console.log(resp.status); // "SUCCESS", "CANCELLED" - finish with recording or just closed (cancelled)
};
recorder.showRecorder(show_recorder_callback);
```

{% endcode %}
