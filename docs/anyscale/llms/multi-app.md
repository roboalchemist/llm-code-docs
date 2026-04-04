# Source: https://docs.anyscale.com/services/multi-app.md

# Multi-application services

[View Markdown](/services/multi-app.md)

# Multi-application services

This guide walks through deploying multiple applications in a single Anyscale service.

## Multiple applications[​](#multiple-apps "Direct link to Multiple applications")

In Ray Serve, an **application** is the smallest unit that can be independently upgraded without affecting other parts of the service. It consists of one or more **deployments** tied together in a directed acyclic graph using [model composition](https://docs.ray.io/en/latest/serve/model_composition.html). An application can be called by HTTP at the specified **route prefix**.

```
name: multi-app-service
applications:
  - name: app1
    ...
  - name: app2
    ...
```

Using model composition, you can deploy a mixture of ML models and business logic as a single application, and each deployment in the application can be configured and scaled independently. With multiple applications in a service you have extended flexibility for certain use cases.

* **Management overhead**: Instead of running a separate service for each new application, you can serve multiple models behind separate query-able endpoints within a single service.
* **Hardware utilization**: Even when you have groups of independent models, co-hosting them on shared compute allows you to increase hardware utilization.
* **Flexible updates**: You can update applications independently of each other.

### Query a multi-application service[​](#query-multi "Direct link to Query a multi-application service")

Each application within a multi-application service can be queried by HTTP at its own endpoint, determined by its `route_prefix`.

For instance, if you deploy application `app1` with route prefix `/endpoint1`, and application `app2` with route prefix `/endpoint2`, then you can query them separately like this:

```
# Query app1
curl https://my-service-abc.cld-def.s.anyscaleuserdata.com/endpoint1

# Query app2
curl https://my-service-abc.cld-def.s.anyscaleuserdata.com/endpoint2
```

### Add or remove applications[​](#add-remove "Direct link to Add or remove applications")

Using in-place updates, you can dynamically add applications to and remove applications from the cluster without having to bring down the service. All running applications in the service continue to serve traffic at their respective endpoints without interruption.

Note that while we normally caution against using [in-place updates](https://docs.ray.io/en/latest/serve/advanced-guides/inplace-updates.html), multi-application services is one case where in-place updates can be very useful. Of course, a cross-cluster upgrade is always the strictly safer option.

To add an application `app3`, add it as a new entry in your service YAML definition under `applications`:

```
name: multi-app-service
applications:
  - name: app1
    ...
  - name: app2
    ...
  - name: app3
    ...
```

Similarly, to remove an application `app1`, remove its entry in your service YAML definition under `applications`:

```
name: multi-app-service
applications:
  - name: app2
    ...
  - name: app3
    ...
```

### Example[​](#example-yaml "Direct link to Example")

This YAML file can be used to deploy a two-application service containing a sentiment analysis model and a Stable Diffusion model.

```
name: multi-app-service
image_uri: anyscale/ray-ml:2.30.0-py39
applications:
  - name: sentiment
    route_prefix: /sentiment
    import_path: sentiment_analysis.app:model
    runtime_env:
      working_dir: https://github.com/anyscale/docs_examples/archive/refs/heads/main.zip

  - name: stable_diffusion
    route_prefix: /diffusion
    import_path: stable-diffusion.app:entrypoint
    runtime_env:
      working_dir: https://github.com/anyscale/docs_examples/archive/refs/heads/main.zip
      pip:
        - accelerate==0.14.0
        - diffusers @ git+https://github.com/huggingface/diffusers.git@25f11424f62d8d9bef8a721b806926399a1557f2
        - Pillow==9.3.0
        - scipy==1.9.3
        - torch==1.13.0
        - torchvision==0.14.0
        - transformers==4.24.0
```

## Multiple applications in different containers[​](#multi-container-apps "Direct link to Multiple applications in different containers")

By default, all Ray Serve applications run in the container image that the Anyscale cluster starts with. However, you might want to run your applications in their own containers. This provides several benefits:

* You don't have to install per-application dependencies at runtime using `pip` or `conda` [runtime environments](https://docs.ray.io/en/latest/ray-core/handling-dependencies.html#runtime-environments). Instead, you can use a stable image that containerizes your application and its dependencies.
* You don't have to package all applications and their dependencies into one image, as a monolith image can grow very large. Instead, you can separate them out into per-application images.

However, note that this also puts more of the version management responsibility on the user. In particular, one requirement to keep in mind is that the Ray and Python version in the overall Anyscale service cluster ***must*** match that of the images used to run your applications.

### Container runtime environment[​](#container-runtime "Direct link to Container runtime environment")

Ray Serve uses [runtime environments](https://docs.ray.io/en/latest/ray-core/handling-dependencies.html#runtime-environments) to configure the per-application environment each of your models run in.

Runtime environments like `pip`, `conda`, or `working_dir` give your models dynamic access to dependencies and files they require through virtual environments and downloading files at runtime, but the models still run in the original service container image. Recall that the service itself runs within a container that is configured by the service's `image_uri`.

To run your applications in completely separate containers using different images from the service container image, configure an application's `image_uri` runtime environment.

```
name: multi-app-service
image_uri: anyscale/ray:2.30.0-py39
applications:
  - name: stable_diffusion
    runtime_env:
      image_uri: anyscale/image:custom-diffusion-image
```

The application's `image_uri` runtime environment, `anyscale/image:custom-diffusion-image`, overrides the `image_uri` of the overall service, `anyscale/ray:2.30.0-py39`, where all applications run by default.

### Example[​](#container-example "Direct link to Example")

This example deploys two applications, a ResNet model and a Whisper model, in a single service, but each application uses a separate image.

#### Build custom container images[​](#build-images "Direct link to Build custom container images")

Let's build two [custom container images](/container-image/custom-image.md) that neatly package the two respective models and their dependencies.

First, build a custom container image containing the application code for the [ResNet model](https://github.com/ray-project/ray/blob/master/doc/source/serve/doc_code/resnet50_example.py) (see the [source code](https://raw.githubusercontent.com/ray-project/ray/master/doc/source/serve/doc_code/resnet50_example.py)) and its dependencies:

* `torch==2.0.1`
* `torchvision==0.15.2`

Copy the image URI for later use; in our example, the image URI is `anyscale/image/resnet-cpu-image:1`. ![ResNet container image](/assets/images/resnet-container-image-c8a7b409d5fc5a1423bee3cc0e5cffab.png)

Next, build a custom container image containing the application code for the [Whisper model](https://github.com/ray-project/ray/blob/master/doc/source/serve/doc_code/whisper_example.py) (see the [source code](https://raw.githubusercontent.com/ray-project/ray/master/doc/source/serve/doc_code/whisper_example.py)) and its necessary dependencies:

* `faster_whisper==0.10.0`

Notice that in the Python definition of the Whisper application, the resource requirements include `"num_gpus": 1`. Since the model runs on GPUs, we need to run it in an image with CUDA support. This is why the image uses `anyscale/ray-ml:2.30.0-py39-gpu` as a base image.

Again, save the image URI for later use; in our example, it is `anyscale/image/whisper-gpu-image:1`. ![Whisper container image](/assets/images/whisper-container-image-798f27cf21e60aa3be58a92111a77a12.png)

#### Deploy service[​](#deploy-service "Direct link to Deploy service")

Now, let's deploy the ResNet and Whisper models to an Anyscale service with their respective container images.

To make use of the container images we just built, set the `image_uri` in each application's `runtime_env` to the image URIs you copied from the previous step. This will run the Ray Serve applications in separate containers from the service container image.

tip

Notice that the image for the general Anyscale service cluster, `anyscale/ray:2.30.0-py39`, uses Ray 2.30.0 and Python 3.9, and the base images for the custom container images we built above also use Ray 2.30.0 and Python 3.9. This is because the Ray and Python version in the service container image *must match* that of all images used to launch Serve applications in separate containers.

```
name: multi-app-service
image_uri: anyscale/ray:2.30.0-py39
applications:
  - name: resnet
    route_prefix: /resnet
    import_path: resnet50_example:app
    runtime_env:
      image_uri: anyscale/image/resnet-cpu-image:1
  - name: whisper
    route_prefix: /whisper
    import_path: whisper_example:entrypoint
    runtime_env:
      image_uri: anyscale/image/whisper-gpu-image:1
```

Deploy this service with `anyscale service deploy -f config.yaml`.

#### Query service[​](#query-service "Direct link to Query service")

Let's run the ResNet model on a [picture of an ox](https://serve-resnet-benchmark-data.s3.us-west-1.amazonaws.com/000000000019.jpeg).

```
❯ curl -H "Authorization: Bearer YOUR_APP_API_TOKEN" \
    YOUR_APP_BASE_URL \
    -d '{"uri": "https://serve-resnet-benchmark-data.s3.us-west-1.amazonaws.com/000000000019.jpeg"}'
# Output
ox
```

Next, let's run the Whisper model on this [audio recording](https://storage.googleapis.com/public-lyrebird-test/test_audio_22s.wav).

```
❯ curl -H "Authorization: Bearer YOUR_APP_API_TOKEN" \
    YOUR_APP_BASE_URL \
    -d '{"filepath": "https://storage.googleapis.com/public-lyrebird-test/test_audio_22s.wav"}' \
    | jq "."
# Output
{
  "language": "en",
  "language_probability": 1,
  "duration": 21.775,
  "transcript_text": " Well, think about the time of our ancestors. A ping, a ding, a rustling in the bushes is like, whoo, that means an immediate response. Oh my gosh, what's that thing? Oh my gosh, I have to do it right now. And dude, it's not a tiger, right? Like, but our, our body treats stress as if it's life-threatening. Cause to quote Robert Sapolsky or butcher his quote, he's a Robert Sapolsky is like one of the most incredible stress physiologists of,",
  "whisper_alignments": [
    [
      0,
      0.36,
      " Well,",
      0.30859375
    ],
    ...
  ]
}
```

### Multi-container applications on Kubernetes[​](#multi-container-applications-on-kubernetes "Direct link to Multi-container applications on Kubernetes")

For multi-container applications service running on Kubernetes, Anyscale leverages [Podman](https://podman.io/) to start and run application containers as nested containers inside the Ray container. This requires the Ray container of the pod to be privileged container so that Podman can use Linux user namespace to run rootless containers. To enable a privileged container for Ray, add the following [Kubernetes specific](/configuration/compute/kubernetes.md) instance advanced config into the compute config:

```
name: multi-app-service
image_uri: your_ray_image_uri_with_podman
compute_config:
  cloud: your_anyscale_cloud_name
  head_node:
    instance_type: 4CPU-16GB
  worker_nodes:
    - instance_type: 4CPU-16GB
      min_nodes: 1
      max_nodes: 10
  advanced_instance_config:
    spec:
      containers:
        - name: ray
          securityContext:
            privileged: true
applications:
...
```

You will also need to install Podman into your own Ray image for the Ray cluster, for example: ![Container image](/assets/images/podman-image-9e25711efa7f89c971a1a2527d39d518.png)
