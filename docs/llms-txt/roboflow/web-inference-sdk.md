# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/sdks/web-browser/web-inference-sdk.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/sdks/web-browser/web-inference-sdk.md

# Source: https://docs.roboflow.com/deploy/sdks/web-browser/web-inference-sdk.md

# Web inference-sdk

### What is WebRTC Streaming?

`@roboflow/inference-sdk` enables real-time video streaming from your browser to Roboflow's inference servers using WebRTC. This allows you to:

* **Execute Workflows** - Run complex multi-step computer vision pipelines
* **Access All Models** - Use any Roboflow model type
* **Server-Side Processing** - Leverage powerful GPUs
* **Low Latency** - WebRTC provides near-real-time results
* **Bidirectional Communication** - Send and receive data during streaming

### Installation

```bash
npm install @roboflow/inference-sdk
```

### Quick Start

Take a look at the video/sample code below to get started:

{% embed url="<https://www.loom.com/share/48b7c442a69c49e081d0dbec49e1ab57>" %}

```typescript
import { connectors, webrtc, streams } from '@roboflow/inference-sdk';

// ⚠️ Use withApiKey for development only
// ⚠️ Do not use this in production, because it will expose your API key
// For production, use a backend proxy (see next section)
const connector = connectors.withApiKey("your-api-key");

// Get camera stream
const stream = await streams.useCamera({
  video: {
    facingMode: { ideal: "environment" },
    width: { ideal: 640 },
    height: { ideal: 480 }
  }
});

// Start WebRTC connection
const connection = await webrtc.useStream({
  source: stream,
  connector,
  wrtcParams: {
    workspaceName: "your-workspace",
    workflowId: "your-workflow",
    imageInputName: "image",
    streamOutputNames: ["output"],
    dataOutputNames: ["predictions"]
  },
  onData: (data) => {
    console.log("Inference results:", data);
  }
});

// Display processed video
const videoElement = document.getElementById('video');
videoElement.srcObject = await connection.remoteStream();

// Clean up when done
await connection.cleanup();
```

### 🔐 Security Best Practices

**NEVER expose your API key in frontend code for production applications.**

The `connectors.withApiKey()` method is convenient for demos but exposes your API key in the browser. **For production, always use a backend proxy:**

#### Secure Production Pattern

**Frontend:**

```typescript
import { connectors, webrtc, streams } from '@roboflow/inference-sdk';

// Use proxy endpoint instead of direct API key
const connector = connectors.withProxyUrl('/api/init-webrtc');

const stream = await streams.useCamera({ video: true });
const connection = await webrtc.useStream({
  source: stream,
  connector,
  wrtcParams: { /* ... */ }
});
```

**Backend (Express):**

```typescript
import { InferenceHTTPClient } from '@roboflow/inference-sdk/api';

app.post('/api/init-webrtc', async (req, res) => {
  const { offer, wrtcparams } = req.body;

  // API key stays secure on the server
  const client = InferenceHTTPClient.init({
    apiKey: process.env.ROBOFLOW_API_KEY
  });

  const answer = await client.initializeWebrtcWorker({
    offer,
    workspaceName: wrtcparams.workspaceName,
    workflowId: wrtcparams.workflowId,
    config: {
      imageInputName: wrtcparams.imageInputName,
      streamOutputNames: wrtcparams.streamOutputNames,
      dataOutputNames: wrtcparams.dataOutputNames
    }
  });

  res.json(answer);
});
```

### Key Features

#### Dynamic Output Reconfiguration

Change stream and data outputs at runtime without restarting:

```typescript
// Switch to different visualization
connection.reconfigureOutputs({
  streamOutput: ["blur_visualization"]
});

// Enable all data outputs
connection.reconfigureOutputs({
  dataOutput: ["*"]
});

// Change both at once
connection.reconfigureOutputs({
  streamOutput: ["annotated_image"],
  dataOutput: ["predictions", "counts"]
});
```

### Complete Working Example

For a full working example with both frontend and backend code, see the [sample application repository](https://github.com/roboflow/inferenceSampleApp). The sample app demonstrates:

* Proper backend proxy setup for API key security
* Camera streaming integration
* Error handling and connection management
* Production-ready patterns

### Resources

* [Example Application](https://github.com/roboflow/inferenceSampleApp)
* [Package on NPM](https://www.npmjs.com/package/@roboflow/inference-sdk)
