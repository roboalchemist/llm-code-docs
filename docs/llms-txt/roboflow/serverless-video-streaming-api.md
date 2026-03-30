# Source: https://docs.roboflow.com/changelog/explore-by-month/december-2025/serverless-video-streaming-api.md

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/serverless-video-streaming-api.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/serverless-video-streaming-api.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/serverless-video-streaming-api.md

# Source: https://docs.roboflow.com/deploy/serverless-video-streaming-api.md

# Serverless Video Streaming API

### Overview

The Serverless Streaming API uses WebRTC to stream video from webcams, RTSP cameras, or video files to the Roboflow Cloud. Your [Workflow](https://docs.roboflow.com/workflows/what-is-workflows) processes each frame and streams results back to your application.

You can run any Workflow with this API. For single model inference, create a Workflow that wraps your model.

**Supported input sources:**

* **Webcam**: Browser or device camera via MediaStream API
* **RTSP**: IP cameras or any RTSP-compatible source. The URL must be publicly accessible from the internet so the cloud function can connect to it. Authentication via username/password in the URL is supported (e.g., `rtsp://user:pass@host/stream`).
* **Video Files**: Pre-recorded video uploaded via the Data Channel

### How It Works

When you start a streaming session, the SDK calls Roboflow's API to initialize a WebRTC connection. The API spawns a serverless function that runs your Workflow. Once connected, data flows through two WebRTC channels:

#### Video Track

Streams video frames bidirectionally. You send frames from your webcam or video file, and receive annotated/processed frames back. The Video Track is optimized for real-time display: it adjusts resolution and may drop frames based on available bandwidth. Quality ramps up as the connection stabilizes.

Due to WebRTC congestion control, it can take up to a minute for quality and FPS to ramp up to full capacity, especially at higher resolutions like 1920×1080 at 30 FPS.

#### Data Channel

Sends structured inference results as JSON messages. This includes all Workflow output data like predictions, coordinates, and classifications. Unlike the Video Track, the Data Channel provides reliable, ordered delivery without any optimizations to keep up with the live camera feed. To process video files, you can upload the file via the Data Channel and consume results the same way to fully process the video.

You can use both channels simultaneously, for example displaying annotated video while also processing the structured prediction data in your application.

### Regions and GPU Plans

Specify `requested_region` and `requested_plan` in your configuration to control where and how your stream is processed.

**Regions:** `us` (United States), `eu` (Europe), `ap` (Asia Pacific)

Choose the region closest to your users or video source to minimize latency.

**GPU Plans:**

* `webrtc-gpu-medium`: Default and recommended for most workflows
* `webrtc-gpu-small`: Lower cost. Try this after confirming Medium works well for your use case.
* `webrtc-gpu-large`: Required for SAM3 and Rapid Models that use SAM3 (expect \~5 FPS)

### Pricing

Billed per hour based on your selected GPU plan. Billing starts once the serverless function spawns and the WebRTC connection is established. See [roboflow.com/credits](https://roboflow.com/credits) for current rates.

### SDKs

#### JavaScript

For web browsers and React Native applications.

```bash
npm install @roboflow/inference-sdk
```

Do not expose your API key in frontend code. Use a backend proxy endpoint to keep it secure.

* [NPM package](https://www.npmjs.com/package/@roboflow/inference-sdk)
* [Sample application](https://github.com/roboflow/inferenceSampleApp)
* [Documentation](https://docs.roboflow.com/deploy/sdks/web-browser/web-inference-sdk)

#### Python

For backend applications, RTSP streams, and video file processing.

```bash
pip install inference-sdk[webrtc]
```

* [PyPI package](https://pypi.org/project/inference-sdk/)
* [Example scripts](https://github.com/roboflow/inference/tree/main/examples/webrtc_sdk) (webcam, RTSP, video file)

### Configuration

When creating a streaming session, pass a `StreamConfig` object to control behavior:

* `stream_output`: List of Workflow output names to stream via Video Track
* `data_output`: List of Workflow output names to send via Data Channel
* `requested_plan`: GPU plan (see above)
* `requested_region`: Region code (`us`, `eu`, or `ap`)
* `realtime_processing`: If `True` (default), drop frames when processing can't keep up
* `workflow_parameters`: Dictionary of parameters to pass to the Workflow

### Testing Without Code

You can test streaming directly in the Roboflow web interface:

1. Go to [app.roboflow.com](https://app.roboflow.com)
2. Open the **Workflows** tab
3. Select a Workflow and click **Test Workflow**
4. Choose your source (Webcam, RTSP, or Video File) and configure GPU/region settings
5. Click **Run**
