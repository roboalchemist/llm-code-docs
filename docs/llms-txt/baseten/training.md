# Source: https://docs.baseten.co/reference/sdk/training.md

# Training

> Reference documentation for Baseten's Training SDK classes and configuration.

The Training SDK provides classes for configuring and managing machine learning model training jobs on Baseten. This reference documents the key classes used to define training configurations.

# Deploy a `TrainingJob`

To deploy a training job, use the following command:

```bash  theme={"system"}
truss train push <path_to_config_file>
```

The following classes are used to configure and deploy training jobs:

## TrainingJob

Defines a complete training job configuration.

```python  theme={"system"}
class TrainingJob:
    image: Image              # Container image configuration
    compute: Compute         # Compute resource configuration
    runtime: Runtime        # Runtime environment configuration
```

Example usage:

```python  theme={"system"}
training_job = TrainingJob(
    image=Image(base_image="pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime"),
    compute=Compute(cpu_count=4, memory="16Gi"),
    runtime=Runtime(
        start_commands=["python train.py"],
        checkpointing_config=CheckpointingConfig(enabled=True),
        enable_cache=True,
    )
)
```

## TrainingProject

Organizes training jobs and provides project-level configuration.

```python  theme={"system"}
class TrainingProject:
    name: str           # Project name
    job: TrainingJob   # Training job configuration
```

Example usage:

```python  theme={"system"}
project = TrainingProject(
    name="llm-fine-tuning",
    job=training_job
)
```

## Image

Specifies the container image for the training environment.

```python  theme={"system"}
class Image:
    base_image: str  # Docker image to use for training
    docker_auth: Optional[DockerAuth] # Authentication details for private docker images
```

Example usage:

```python  theme={"system"}
image = Image(base_image="pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime")
```

### DockerAuth

Configures authentication for private Docker registries. Ensure that any SecretReference
used has been set in your Baseten Workspace. See [secrets](/observability/secrets) for more details.

```python  theme={"system"}
class DockerAuth:
    auth_method: truss_config.DockerAuthType  # Authentication method type
    registry: str                              # Docker registry URL
    aws_iam_docker_auth: Optional[AWSIAMDockerAuth] = None
    gcp_service_account_json_docker_auth: Optional[GCPServiceAccountJSONDockerAuth] = None
```

#### AWSIAMDockerAuth

Authenticates with AWS ECR using IAM credentials.

```python  theme={"system"}
class AWSIAMDockerAuth:
    access_key_secret_ref: SecretReference      # AWS access key ID as a secret reference
    secret_access_key_secret_ref: SecretReference  # AWS secret access key as a secret reference
```

#### GCPServiceAccountJSONDockerAuth

Authenticates with Google Container Registry using service account JSON.

```python  theme={"system"}
class GCPServiceAccountJSONDockerAuth:
    service_account_json_secret_ref: SecretReference  # GCP service account JSON secret reference
```

#### Example

Example usage with GCP:

```python  theme={"system"}
# Configure image with GCP authentication
image = Image(
    base_image="gcr.io/my-project/my-repo/my-private-image:latest",
    docker_auth=DockerAuth(
        auth_method=truss_config.DockerAuthType.GCP_SERVICE_ACCOUNT_JSON,
        registry="gcr.io",
        gcp_service_account_json_docker_auth=GCPServiceAccountJSONDockerAuth(
            service_account_json_secret_ref=SecretReference(name="gcp_service_account_json")
        )
    )
)
```

## Compute

Specifies compute resources for training jobs.

```python  theme={"system"}
class Compute:
    node_count: int = 1      # Number of nodes for distributed training
    cpu_count: int = 1       # Number of CPU cores
    memory: str = "2Gi"      # Memory allocation
    accelerator: Optional[AcceleratorSpec] = None  # GPU configuration
```

Example usage:

```python  theme={"system"}
# Configure a training job with 2 GPUs and 4 CPUs
compute = Compute(
    accelerator=AcceleratorSpec(accelerator="H100", count=4)
)
```

## Runtime

Defines the runtime environment for training jobs.

```python  theme={"system"}
class Runtime:
    start_commands: List[str] = []  # Commands to run at job start
    environment_variables: Dict[str, Union[str, SecretReference]] = {}
    enable_cache: bool = False      # Enable caching
    checkpointing_config: CheckpointingConfig = CheckpointingConfig()
```

Example usage:

```python  theme={"system"}
runtime = Runtime(
    start_commands=["python train.py"],
    environment_variables={
        "BATCH_SIZE": "32",
        "WANDB_API_KEY": SecretReference(name="WANDB_KEY")
    },
    checkpointing_config=CheckpointingConfig(enabled=True)
)
```

### Training Cache

When `enable_cache=True` is set in your `Runtime`, the training cache will be enabled.

The cache will be mounted at two locations:

* `/root/.cache/huggingface`
* [`$BT_RW_CACHE_DIR`](#baseten-provided-environment-variables) - Baseten will export this variable in your job's environment.

The cache storage is separate from ephemeral storage limits of your training job. Training Projects provide storage segragation within the cache. Training jobs within the same project share the same cache, while training jobs in different projects cannot access each other's data.

### SecretReference

Used to securely reference secrets stored in your Baseten workspace.

```python  theme={"system"}
class SecretReference:
    name: str  # Name of the secret in your workspace
```

Example usage:

```python  theme={"system"}
# Reference a secret named "WANDB_API_KEY" 
secret_ref = SecretReference(name="WANDB_API_KEY")
```

### CheckpointingConfig

Configures model checkpointing behavior during training. Baseten will export the [`$BT_CHECKPOINT_DIR`](#baseten-provided-environment-variables) within
the Training Job's environment. The checkpointing storage is independent of the ephemeral stroage of the pod

```python  theme={"system"}
class CheckpointingConfig:
    enabled: bool = False              # Enable/disable checkpointing
    checkpoint_path: Optional[str] = None  # Custom checkpoint directory path
    volume_size_gib: Optional[int] = None # Custom size of your checkpointing directory
```

Example usage:

```python  theme={"system"}
# Enable checkpointing with default path
checkpointing = CheckpointingConfig(enabled=True)
```

### Baseten Provided Environment Variables

Baseten automatically provides several environment variables in your training job's environment to help integrate your code with the Baseten platform.

#### Environment Variables

| Environment Variable     | Description                                                 | Example                         |
| ------------------------ | ----------------------------------------------------------- | ------------------------------- |
| `BT_TRAINING_JOB_ID`     | ID of the Training Job                                      | `"gvpql31"`                     |
| `BT_NUM_GPUS`            | Number of available GPUs per node                           | `"4"`                           |
| `BT_RW_CACHE_DIR`        | Non-HuggingFace cache directory of the training cache mount | `"/root/.cache/user_artifacts"` |
| `BT_CHECKPOINT_DIR`      | Directory of the automated checkpointing mount              | `"/mnt/ckpts"`                  |
| `BT_LOAD_CHECKPOINT_DIR` | Directory of where loaded checkpoints will be               | `"/tmp/loaded_checkpoints"`     |
| `BT_TRAINING_JOB_NAME`   | Name your the Training Job                                  | `"gpt-oss-20b-lora"`            |

#### Multinode Environment Variables

The following environment variables are particularly useful for multinode training jobs:

| Environment Variable | Description                                 | Example      |
| -------------------- | ------------------------------------------- | ------------ |
| `BT_GROUP_SIZE`      | Number of nodes in the multinode deployment | `"2"`        |
| `BT_LEADER_ADDR`     | Address of the leader node                  | `"10.0.0.1"` |
| `BT_NODE_RANK`       | Rank of the node                            | `"0"`        |

For multinode deployments, any traditionally used port number (e.g. `29500`) will work. There is no specific port number required by Baseten.

# Deploy Checkpoints as a Model

## Deploy checkpoints CLI wizard

The easiest way to deploy your checkpoints is by using the CLI wizard:

```bash  theme={"system"}
truss train deploy_checkpoints --job-id <job id>
```

Follow the setup wizard to choose your hardware and the checkpoint you'd like to deploy. Baseten will automatically recognize checkpoints for full finetunes and LoRAs for LLMs and Whisper models. Note that FSDP checkpoints aren't supported by `deploy_checkpoints` today and must be manually configured in the truss config.

Once you've completed the wizard, Baseten will generate a truss and deploy a published model according to the specs provided.

## Deploy checkpoints via static configuration

If you'd like to keep a static config of your checkpoint deploy, you can create a python config file defining the configuration you'd like to reference:

```bash  theme={"system"}
truss train deploy_checkpoints <path_to_config_file>
```

## DeployCheckpointsRuntime

Configures the runtime environment for deployed checkpoints.

```python  theme={"system"}
class DeployCheckpointsRuntime:
    environment_variables: Dict[str, Union[str, SecretReference]] = {}
```

## Checkpoint

Represents metadata for a saved model checkpoint.

```python  theme={"system"}
class Checkpoint:
    training_job_id: str   # ID of the training job
    id: str               # Checkpoint ID
    name: str            # Checkpoint name 
    lora_rank: Optional[int] = None  # LoRA rank if applicable. Auto-detected if not specified.
```

## CheckpointList

Manages a collection of checkpoints and their download configuration.

```python  theme={"system"}
class CheckpointList:
    download_folder: str = "training_checkpoints"  # Local download location upon deployment
    base_model_id: Optional[str] = None           # Base model identifier. Auto-dtected if not specified.
    checkpoints: List[Checkpoint] = []            # List of checkpoints
```

## DeployCheckpointsConfig

Specifies configuration for deploying trained model checkpoints.

```python  theme={"system"}
class DeployCheckpointsConfig:
    checkpoint_details: Optional[CheckpointList] = None  # Checkpoints to deploy
    model_name: Optional[str] = None                    # Name for the deployed model
    deployment_name: Optional[str] = None               # Name for the deployment
    runtime: Optional[DeployCheckpointsRuntime] = None  # Runtime configuration
    compute: Optional[Compute] = None                   # Compute resources
```

Example usage:

```python  theme={"system"}
deploy_config = DeployCheckpointsConfig(
    model_name="fine-tuned-llm",
    deployment_name="production-llm",
    checkpoint_details=CheckpointList(
        checkpoints=[
            Checkpoint(
                training_job_id="gvpql31",
                id="checkpoint_1",
                name="checkpoint_1"
            )
        ]
    ),
    compute=Compute(
        accelerator=AcceleratorSpec(accelerator="H100", count=1)
    )
)
```
