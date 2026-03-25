# Source: https://docs.mystic.ai/docs/how-to-reduce-cold-starts-in-ml-models.md

# How to reduce cold starts in ML models running in production

Cold boots take a long time in ML and AI, this guide covers what you can and can't do to help this fix this issue

# Overview

This guide covers approaches to reducing cold start times in your ML/AI models and also discusses how Mystic can help with this.

Due to the large size of both models and the libraries used to run them, cold starts are one of the largest problems companies face when running ML in production. It's common for a model to take 5-10 minutes to load for the first time, and this guide covers the following areas for reducing this:

1. Docker container optimisation
2. Container download speeds
3. Model weights downloading optimisations
4. Cloud optimisations
5. GPU availability
6. GPU provisioning

Firstly we will go through what you can, sort of can, and can't actually control.

> 📘 This guide gets updates
>
> More sections to this guide are being added and updated daily - check back again for more information!

# Typical cold start procedure

Companies and products will vary the model lifecycle for inference, but when starting for the first time the following procedure is the most common one followed (*this is assuming you're using docker for models running on a Kubernetes stack*):

1. A request hits an API to use a model
2. The model isn't warm (currently running anywhere) and the system triggers the autoscaler to request an instance to run the model on
3. A server is provisioned from the cloud provider
4. Nvidia drivers are installed on the server via a daemon process
5. Model docker container is downloaded
6. Container starts
7. Weights are downloaded and services start
8. Inference request begins to process

We will refer to these steps throughout this guide.

# What you can control

This is the most important thing to know for your system, in the standard flow described above steps, 2, 5, 6, 7, 8, are almost completely in your control to optimise. We will look at these items individually.

## Step 2 - Notifying the autoscaler

For low volume models the 0 -> 1 scaling speed is much more important than 1 -> n as you can not use queuing or any other logic to provide some result quickly.

Depending on how your stack is setup the scaling notification speed could be <1s or 30s. If you are scaling down to 0 the most common approach in Kubernetes is to use [KEDA](https://keda.sh/). KEDA allows you to scale down to 0 which is not possible using native Horizontal Pod Autoscalers (HPAs) in Kubernetes. It works by creating and deleting HPAs, and uses a similar metrics system. You can see a full list of Scalars (services KEDA can integrate with to gauge how to scale) [here](https://keda.sh/docs/2.13/scalers/).

An important thing to note here is the **polling frequency which has a high default setting of 30 seconds**. What this means is every 30 seconds KEDA checks whether to scale from 0 -> 1, this is a very very long time for cold starts especially when nothing useful is going on. You can find more on this [here](https://keda.sh/docs/2.13/concepts/scaling-deployments/). By reducing this to 1 second for example (assuming the scaling service you use can handle higher traffic) means that you won't have this long overhead.

## Step 5 - Model docker container downloading

This is a very important step that's easy to look over. It's also worth splitting into three parts outlined below.

### Step 5.1 - Making your container small

Typically, most models will run in a python based container. A simple way to reduce the size of the container is to make sure to use python-slim at the top of your Dockerfile:

```dockerfile
FROM python:3.10-slim
```

This saves GBs of size in the container making it faster to run.

### Step 5.2 - Private docker registry

Docker hub speeds can be quite volatile, and will not saturate the network bandwidth of the machines you will be running on. `a2` instances used by A100s on GCP run up to 100Gbps, but you will typically see sub 1Gbps when downloading from Docker hub. Private hosting a registry allows you to maximise you bandwidth as you will have a dedicated network line to your model store.

> 📘 More on this coming soon

### Step 5.3 - Kubernetes downloading

In a Deployment there are options for when to download a container. This is a common thing to overlook. To minimise the number of times a model is downloaded to a node you should configure the container pull policy (`imagePullPolicy`) to `IfNotPresent`. For example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        imagePullPolicy: IfNotPresent
```

This will require you to properly version your docker containers when pushing to your choice of docker registry. If you update `latest` and that's what your deployments point to then you will have to force pull, which is not trivial and can introduce service interruptions.

# More coming soon...

Check back later for more updates to this guide!