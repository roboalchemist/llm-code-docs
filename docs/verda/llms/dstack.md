# Source: https://docs.verda.com/integrations/dstack.md

# dstack

[dstack](https://github.com/dstackai/dstack/) is an open-source, streamlined alternative to Kubernetes and Slurm, specifically designed for AI workloads. It simplifies container orchestration to accelerate the development, training, and deployment of AI models.

### Installation

To use `dstack` with Verda Cloud, you first need to configure dstack integration by providing access credentials.

1. [Log in](https://console.verda.com/) to your Verda Cloud account.
2. Navigate to the `Keys` page in the sidebar.
3. Find `Cloud API credentials` area and then click the `+ Create` button

Then, configure the backend via `~/.dstack/server/config.yml`:

```python
projects:
  - name: main
    backends:
      - type: datacrunch
        creds:
          type: api_key
          client_id: xfaHBqYEsArqhKWX-e52x3HH7w8T
          client_secret: B5ZU5Qx9Nt8oGMlmMhNI3iglK8bjMhagTbylZy4WzncZe39995f7Vxh8
```

See the `dstack` [documentation](https://dstack.ai/docs/concepts/backends/#nebius) for more configuration options.

Once the backend is configured, install the `dstack` server. Follow their official guide at <https://dstack.ai/docs/installation/> to install dstack locally.

```python
$ pip install "dstack[datacrunch]" -U
$ dstack server


Applying ~/.dstack/server/config.yml...

The admin token is "bbae0f28-d3dd-4820-bf61-8f4bb40815da"
The server is running at http://127.0.0.1:3000/
```

### Create a fleet

Before you can submit your first run, you have to create a [fleet](https://dstack.ai/docs/concepts/fleets/).

```python
type: fleet
name: default

# Allow to provision of up to 2 instances
nodes: 0..2

# Deprovision instances above the minimum if they remain idle
idle_duration: 1h

resources:
  # Allow to provision up to 8 GPUs
  gpu: 0..8
```

Pass the fleet configuration to `dstack apply`:

```python
$ dstack apply -f fleet.dstack.yml
```

Once the fleet is created, you can run dstack’s dev environments, tasks, and services.

### Dev environments

A [dev environment](https://dstack.ai/docs/concepts/dev-environments/) lets you provision an instance and access it using your desktop IDE (VS Code, Cursor, PyCharm, etc) or via SSH.

Example configuration:

```python
type: dev-environment
name: vscode

# If `image` is not specified, dstack uses its default image
python: "3.12"
#image: dstackai/base:py3.13-0.7-cuda-12.1

ide: vscode

resources:
  gpu: B200:1..8
```

To run a dev environment, apply the configuration:

```python
$ dstack apply -f .dstack.yml

Submit the run vscode? [y/n]: y

To open in VS Code Desktop, use this link:
  vscode://vscode-remote/ssh-remote+vscode/workflow
```

Open the link to access the dev environment from your desktop IDE.

### Tasks

A [task](https://dstack.ai/docs/concepts/tasks/) allows you to schedule a job or run a web app. Tasks can be distributed and support port forwarding.

Example training task configuration:

```python
type: task
# The name is optional, if not specified, generated randomly
name: trl-sft    

python: 3.12

# Uncomment to use a custom Docker image
#image: huggingface/trl-latest-gpu

env:
  - MODEL=Qwen/Qwen2.5-0.5B
  - DATASET=stanfordnlp/imdb

commands:
  - uv pip install trl
  - | 
    trl sft \
      --model_name_or_path $MODEL --dataset_name $DATASET
      --num_processes $DSTACK_GPUS_PER_NODE

resources:
  # One to two  GPUs
  gpu: B200:1..2
  shm_size: 24GB
```

To run the task, apply the configuration:

```python
$ dstack apply -f train.dstack.yml

Submit the run `trl-sft`? [y/n]: y
```

### Services

A [service](https://dstack.ai/docs/concepts/services/) allows you to deploy a model or any web app as a scalable and secure endpoint.

Example configuration:

```python
type: service
name: deepseek-r1-nvidia

image: lmsysorg/sglang:latest
env:
  - MODEL_ID=deepseek-ai/DeepSeek-R1-Distill-Llama-8B
commands:
    - python3 -m sglang.launch_server
      --model-path $MODEL_ID
      --port 8000
      --trust-remote-code

port: 8000
model: deepseek-ai/DeepSeek-R1-Distill-Llama-8B

resources:
  gpu: 24GB
```

To deploy the model, apply the configuration:

```python
$ dstack apply -f deepseek.dstack.yml

Submit the run `deepseek-r1-sglang`? [y/n]: y

Service is published at: 
  http://localhost:3000/proxy/services/main/deepseek-r1-sglang/
Model deepseek-ai/DeepSeek-R1 is published at:
  http://localhost:3000/proxy/models/main/
```

`dstack` can handle auto-scaling and authentication if the corresponding properties are set.

If deploying a model, once the service is up, you can access it via `dstack`’s UI in addition to the API endpoint.

### Clusters

Managed support for Verda’s instant clusters is coming to `dstack`. Meanwhile, in case you’ve created clusters with Verda, you can access them via `dstack` by creating an [SSH fleet](https://dstack.ai/docs/concepts/fleets/#ssh) and listing the IP addresses of each node in the cluster, along with SSH user and SSH private key for each host.

Example configuration:

```python
type: fleet
name: my-datacrunch-cluster

ssh_config:
  user: ubuntu
  identity_file: ~/.ssh/datacrunch_cluster_id_rsa
  hosts:
    - hostname: 12.34.567.890
      blocks: auto
    - hostname: 12.34.567.891
      blocks: auto
    - hostname: 12.34.567.892
      blocks: auto
    - hostname: 12.34.567.893
      blocks: auto


# Set to `cluster` if the instances are interconnected
placement: cluster
```

To create the fleet, apply the configuration:

```python
$ dstack apply -f my-datacrunch-fleet.dstack.yml

 FLEET                INSTANCE  RESOURCES      STATUS    CREATED 
 my-datacrunch-fleet  0         8xH100 (80GB)  0/8 busy  3 mins ago      
                      1         8xH100 (80GB)  0/8 busy  3 mins ago    
                      2         8xH100 (80GB)  0/8 busy  3 mins ago    
                      3         8xH100 (80GB)  0/8 busy  3 mins ago 
```

Once the fleet is created, you can use it for running dev environments, tasks, and services.

With clusters, it’s possible to run [distributed tasks](https://dstack.ai/docs/concepts/tasks/#distributed-tasks).

Example distributed training task configuration:

```python
type: task
name: train-distrib

# The size of the cluster
nodes: 2

python: 3.12
env:
  - NCCL_DEBUG=INFO
commands:
  - git clone https://github.com/pytorch/examples.git pytorch-examples
  - cd pytorch-examples/distributed/ddp-tutorial-series
  - uv pip install -r requirements.txt
  - |
    torchrun \
      --nproc-per-node=$DSTACK_GPUS_PER_NODE \
      --node-rank=$DSTACK_NODE_RANK \
      --nnodes=$DSTACK_NODES_NUM \
      --master-addr=$DSTACK_MASTER_NODE_IP \
      --master-port=12345 \
      multinode.py 50 10

resources:
  gpu: 24GB:1..8
  # Uncomment if using multiple GPUs
  shm_size: 24GB
```

To run the task, apply the configuration:

```python
$ dstack apply -f train.dstack.yml

Submit the run `train-distrib`? [y/n]: y
```

dstack automatically runs the container on each node while passing [system environment variables](https://github.com/dstackai/dstack/blob/master/docs/docs/concepts/tasks.md#system-environment-variables), which you can use with torchrun, accelerate, or other distributed frameworks.

### **dstack’s Documentation**

`dstack` supports a wide range of configurations, not only simplifying the development, training, and deployment of AI models but also optimizing cloud resource usage and reducing costs. Explore `dstack`’s official documentation for more details and configuration options.

* [Overview](https://dstack.ai/docs/)
* [Protips](https://dstack.ai/docs/guides/protips/)
