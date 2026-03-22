# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/enterprise-deployment/offline-mode.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/enterprise-deployment/offline-mode.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/enterprise-deployment/offline-mode.md

# Source: https://docs.roboflow.com/deploy/enterprise-deployment/offline-mode.md

# Offline Mode

{% hint style="info" %}
Offline Mode for Roboflow Enterprise customers requires that you use our Docker container.
{% endhint %}

Roboflow Enterprise customers can configure Roboflow Inference, our on-device inference server, to cache weights for up to 30 days.

This allows your model to run completely air-gapped or in locations where an Internet connection is not readily available.

To run your model offline, you need to:

1. Create and attach a Docker volume to `/tmp/cache` on the your Inference Server.
2. Start a Roboflow Inference server with Docker.
3. Make a request to your model through the server, which will initiate the model weight download and cache process. You will need an internet connection for this step.

Once your weights have been cached, you can use them locally.

Below, we provide instructions for how to run your model offline on various device types, from CPU to GPU.

## CPU

Image: [roboflow / roboflow-inference-server-cpu](https://hub.docker.com/r/roboflow/roboflow-inference-server-cpu)

```bash
sudo docker volume create roboflow
sudo docker run --net=host --env LICENSE_SERVER=10.0.1.1 --mount source=roboflow,target=/tmp/cache roboflow/roboflow-inference-server-cpu
```

## GPU

To use the GPU container, you must first install [nvidia-container-runtime](https://github.com/NVIDIA/nvidia-container-runtime).

Image:[ roboflow / roboflow-inference-server-gpu](https://hub.docker.com/repository/docker/roboflow/roboflow-inference-server-gpu/general)

```bash
sudo docker volume create roboflow
docker run -it --rm -p 9001:9001 --gpus all --mount source=roboflow,target=/tmp/cache roboflow/roboflow-inference-server-gpu
```

## Jetson 4.5

Your Jetson Jetpack 4.5 will already have <https://github.com/NVIDIA/nvidia-container-runtime> installed.

Image:[ roboflow/roboflow-inference-server-jetson-4.5.0](https://hub.docker.com/repository/docker/roboflow/roboflow-inference-server-jetson-4.5.0/general)

<pre class="language-bash"><code class="lang-bash">sudo docker volume create roboflow
<strong>docker run -it --rm -p 9001:9001 --runtime=nvidia --mount source=roboflow,target=/tmp/cache roboflow/roboflow-inference-server-jetson-4.5.0
</strong></code></pre>

## Jetson 4.6

Your Jetson Jetpack 4.6 will already have <https://github.com/NVIDIA/nvidia-container-runtime> installed.

Image:[ roboflow/roboflow-inference-server-jetson-4.6.1](https://hub.docker.com/r/roboflow/roboflow-inference-server-jetson-4.6.1/tags)

<pre class="language-bash"><code class="lang-bash">sudo docker volume create roboflow
<strong>docker run -it --rm -p 9001:9001 --runtime=nvidia --mount source=roboflow,target=/tmp/cache roboflow/roboflow-inference-server-jetson-4.6.1
</strong></code></pre>

## Jetson 5.1

Your Jetson Jetpack 5.1 will already have <https://github.com/NVIDIA/nvidia-container-runtime> installed.

Image: [roboflow/roboflow-inference-server-jetson-5.1.1](https://hub.docker.com/repository/docker/roboflow/roboflow-inference-server-jetson-5.1.1/general)

```bash
sudo docker volume create roboflow
docker run -it --rm -p 9001:9001 --runtime=nvidia --mount source=roboflow,target=/tmp/cache roboflow/roboflow-inference-server-jetson-5.1.1
```

## Running Inference

With your Inference server set up with local caching, you can run your model on images and video frames without an internet connection.

Refer to the "[Predict on an Image Over HTTP](https://inference.roboflow.com/quickstart/run_model_on_image/)" Inference documentation for guidance on how to run your model.

## Inference Results

The weights will be loaded from the your Roboflow account over the Internet (via the License Server if you have configured it) with SSL encryption and stored safely in the Docker volume for up to 30 days.

Your inference results will contain a new `expiration` key you can use to determine how long the Inference Server can continue to provide predictions before renewing its lease on the weights via an Internet or License Server connection. Once the weight expiration date drops below 7 days, the Inference Server will begin trying to renew the weights' lease once per hour until a connection to the Roboflow API is successfully made.

Once the lease has been renewed, the counter will reset to 30 days.

```json
{
    "predictions": [
        {
            "x": 340.9,
            "y": 263.6,
            "width": 284,
            "height": 360,
            "class": "example",
            "confidence": 0.867
        }
    ],
    "expiration": {
        "value": 29.91251408564815,
        "unit": "days"
    }
}
```

{% hint style="info" %}
If you have questions about deploying your model offline, contact your Roboflow representative for guidance.
{% endhint %}
