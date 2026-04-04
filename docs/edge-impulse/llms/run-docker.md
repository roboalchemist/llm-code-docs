# Source: https://docs.edgeimpulse.com/hardware/deployments/run-docker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Docker container

Impulses can be deployed as a Docker container. This packages all your signal processing blocks, configuration and learning blocks up into a container; and then exposes an HTTP inference server. This works great if you have a gateway or cloud runtime that supports containerized workloads. The Docker container is built on top of the [Linux EIM executable](/hardware/deployments/run-linux-eim) deployment option, and supports full hardware acceleration on most Linux targets.

### Deploying your impulse as a Docker container (HTTP interface)

To deploy your impulse, head over to your trained Edge Impulse project, and go to **Deployment**. Here find "Docker container":

<Frame caption="Docker container deployment">
  <img src="https://mintcdn.com/edgeimpulse/x9Ga-7v4NxdQ7jXX/.assets/images/image%20(17).png?fit=max&auto=format&n=x9Ga-7v4NxdQ7jXX&q=85&s=b06c3fcf5b02c75aa351c7756c76b4ec" alt="" width="912" height="1000" data-path=".assets/images/image (17).png" />
</Frame>

It depends on your gateway provider or cloud vendor how you'd run this container, but typically the `container`, `arguments` and `ports to expose` should be enough. If you have questions, contact your solutions engineer (Enterprise plan) or drop a question on the forum (Developer plan).

To test this out locally on macOS or Linux, copy the text under "in a one-liner locally", open a terminal, and paste the command in:

```
$ docker run --rm -it \
>     -p 1337:1337 \
>     public.ecr.aws/g7a8t7v6/inference-container:c94e7ccaca5d3e76e7ed6b046d7a5108b8762707 \
>         --api-key ei_0d... \
>         --run-http-server 1337
Unable to find image 'public.ecr.aws/g7a8t7v6/inference-container:c94e7ccaca5d3e76e7ed6b046d7a5108b8762707' locally
c94e7ccaca5d3e76e7ed6b046d7a5108b8762707: Pulling from g7a8t7v6/inference-container
82d728d38b98: Already exists
59f33b6794af: Pull complete
...

Edge Impulse Linux runner v1.5.1

[RUN] Downloading model...
[BLD] Created build job with ID 15195010
...
[BLD] Building binary OK
[RUN] Downloading model OK
[RUN] Stored model version in /root/.ei-linux-runner/models/1/v231/model.eim
[RUN] Starting HTTP server for Edge Impulse Inc. / Continuous gestures demo (v231) on port 1337
[RUN] Parameters freq 62.5Hz window length 2000ms. classes [ 'drink', 'fistbump', 'idle', 'snake', 'updown', 'wave' ]
[RUN]
[RUN] HTTP Server now running at http://localhost:1337
```

This downloads the latest version of the Docker base image, builds your impulse for your current architecture, and then exposes the inference HTTP server. To view the inference server, go to [http://localhost:1337](http://localhost:1337) .

<Frame caption="HTTP Inference server ran from a Docker container">
  <img src="https://mintcdn.com/edgeimpulse/x9Ga-7v4NxdQ7jXX/.assets/images/image%20(18).png?fit=max&auto=format&n=x9Ga-7v4NxdQ7jXX&q=85&s=284b3983d2558c70bd6d1c4007fb6eb1" alt="" width="1124" height="1000" data-path=".assets/images/image (18).png" />
</Frame>

The inference server exposes the following routes:

* `GET` [http://localhost:1337/api/info](http://localhost:1337/api/info) - returns a JSON object with information about the model, and the inputs / outputs it expects.
* `POST` [http://localhost:1337/api/features](http://localhost:1337/api/features) - run inference on raw sensor data. Expects a request with a JSON body containing a `features` array. You can find raw features on **Live classification**. Example call:

```
curl -v -X POST -H "Content-Type: application/json" -d '{"features": [5, 10, 15, 20]}' http://localhost:1337/api/features
```

* `POST` [http://localhost:1337/api/image](http://localhost:1337/api/image) - run inference on an image. Only available for impulses that use an image as input block. Expects a multipart/form-data request with a `file` object that contains a JPG or PNG image. Images that are not in a size matching your impulse are resized using resize mode [contain](https://sharp.pixelplumbing.com/api-resize). Example call:

```
curl -v -X POST -F 'file=@path-to-an-image.jpg' http://localhost:1337/api/image
```

The result of the inference request depends on your model type. You can always see the raw output by using "Try out inferencing" in the inference server UI.

#### Classification / anomaly detection

Both `anomaly` and `classification` are optional, depending on the blocks included in your impulse.

```json  theme={"system"}
{
    "result": {
        "anomaly": -0.18470126390457153,
        "classification": {
            "drink": 0.007849072106182575,
            "fistbump": 0.0008145281462930143,
            "idle": 0.00002064668842649553,
            "snake": 0.0002238723391201347,
            "updown": 0.0015580836916342378,
            "wave": 0.9895338416099548
        }
    },
    "timing": {
        "anomaly": 0,
        "classification": 0,
        "dsp": 0,
        "json": 0,
        "stdin": 0
    }
}
```

#### Object detection

```json  theme={"system"}
{
    "result": {
        "bounding_boxes": [
            {
                "height": 8,
                "label": "face",
                "value": 0.6704540252685547,
                "width": 8,
                "x": 48,
                "y": 40
            }
        ]
    },
    "timing": {
        "anomaly": 0,
        "classification": 1,
        "dsp": 0,
        "json": 1,
        "stdin": 1
    }
}
```

### Deploying your impulse as a Docker container (forwarding hardware, WebSocket interface)

Instead of using an HTTP server you can also forward your physical hardware (like your webcam) to the container; have the container handle inference; and get predictions back over a websocket. To do so, forward your hardware device; forward port 4912; and omit the `--run-http-server` argument.

For example, on an Nvidia Jetson Orin with a USB webcam:

```sh  theme={"system"}
$ docker run --rm -it \
    --privileged \
    -v /dev/video0:/dev/video0 \
    -v /run/udev:/run/udev \
    -v ~/.ei-linux-runner:/root/.ei-linux-runner \
    -p 4912:4912 \
    public.ecr.aws/g7a8t7v6/inference-container:8b150071556d7c409e38414f7de09044dc0d8184 \
        --api-key ei_8f...
```

Then from e.g. a Python script connect to the websocket server:

```py  theme={"system"}
import asyncio
import websockets
import json

async def hello():
    uri = "ws://localhost:4912/socket.io/?EIO=4&transport=websocket"  # Public echo server
    async with websockets.connect(uri) as ws:
        await ws.send('40')

        while True:
            msg = await ws.recv()
            if msg.startswith('42'):
                ev = json.loads(msg[2:])
                if ev[0] == 'classification':
                    print("→", ev[1])
                elif ev[0] == 'hello':
                    print('Hello!', ev[1])

asyncio.run(hello())
```

Example output:

```
Hello! {'projectName': 'Edge Impulse Inc. / Test', 'thresholds': [{'id': 3, 'min_score': 0.20000000298023224, 'type': 'object_detection'}]}
→ {'modelType': 'object_detection', 'result': {'bounding_boxes': [{'height': 99, 'label': 'person', 'value': 0.5918413400650024, 'width': 22, 'x': 297, 'y': 145}, {'height': 30, 'label': 'person', 'value': 0.2651901841163635, 'width': 119, 'x': 1, 'y': 212}, {'height': 197, 'label': 'person', 'value': 0.24501676857471466, 'width': 67, 'x': 252, 'y': 46}]}, 'timeMs': 210}
```

### Caching model files between runs

To not re-download your model files every time you start the container, you can mount in a cache folder to `/root/.ei-linux-runner`. For example:

```
$ docker run --rm -it \
>     -v ~/.ei-linux-runner:/root/.ei-linux-runner \
>     -p 1337:1337 \
>     public.ecr.aws/g7a8t7v6/inference-container:c94e7ccaca5d3e76e7ed6b046d7a5108b8762707 \
>         --api-key ei_0d... \
>         --run-http-server 1337
```

### Running offline

When you run the container it'll use the Edge Impulse API to build and fetch your latest model version. This thus requires internet access. Alternatively you can download the EIM file (containing your complete model) and mount it in the container instead - this will remove the requirement for any internet access.

First, use the container to *download* the EIM file (here to a file called `my-model.eim` in your current working directory):

```
docker run --rm -it \
    -v $PWD:/data \
    public.ecr.aws/g7a8t7v6/inference-container:c94e7ccaca5d3e76e7ed6b046d7a5108b8762707 \
    --api-key ei_0de... \
    --download /data/my-model.eim
```

> Note that the `.eim` file is hardware specific; so if you run the download command on an Arm machine (like your Macbook M1) you cannot run the eim file on an x86 gateway. To build for another architecture, run with `--list-targets` and follow the instructions.

Then, when you run the container next, mount the eim file back in (you can omit the API key now, it's no longer needed):

```
docker run --rm -it \
    -v $PWD:/data \
    -p 1337:1337 \
    public.ecr.aws/g7a8t7v6/inference-container:c94e7ccaca5d3e76e7ed6b046d7a5108b8762707 \
    --model-file /data/my-model.eim \
    --run-http-server 1337
```

### Hardware acceleration

The Docker container is supported on x86 and aarch64 (64-bits Arm). When you run a model we automatically detect your hardware architecture and compile in hardware-specific optimizations so the model runs as fast as possible on the CPU.

If your device has a GPU or NPU we cannot automatically detect that from inside the container, so you'll need to manually override the target. To see a list of all available targets add `--list-targets` when you run the container. It'll return something like:

```
Listing all available targets
-----------------------------
target: runner-linux-aarch64, name: Linux (AARCH64), supported engines: [tflite]
target: runner-linux-armv7, name: Linux (ARMv7), supported engines: [tflite]
target: runner-linux-x86_64, name: Linux (x86), supported engines: [tflite]
target: runner-linux-aarch64-akd1000, name: Linux (AARCH64 with AKD1000 MINI PCIe), supported engines: [akida]
# ...

You can force a target via "edge-impulse-linux-runner --force-target <target> [--force-engine <engine>]"
```

To then override the target, add `--force-target <target>`.

Note that you also need to forward the NPU or GPU to the Docker container to make this work - and this is not always supported. F.e. for GPUs (like on an NVIDIA Jetson Nano development board):

```
docker run --gpus all \
    # rest of the command
```


Built with [Mintlify](https://mintlify.com).