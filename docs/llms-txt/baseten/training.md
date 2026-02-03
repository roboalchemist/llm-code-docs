# Source: https://docs.baseten.co/reference/sdk/training.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Training SDK

> Configure and manage training jobs with Baseten's training SDK.

## Installation

The training SDK is included with Truss:

<Tabs>
  <Tab title="uv (recommended)">
    [uv](https://docs.astral.sh/uv/) is a fast Python package manager:

    ```sh  theme={"system"}
    uv pip install truss
    ```
  </Tab>

  <Tab title="pip (macOS/Linux)">
    ```sh  theme={"system"}
    pip install --upgrade truss
    ```
  </Tab>

  <Tab title="pip (Windows)">
    ```sh  theme={"system"}
    pip install --upgrade truss
    ```
  </Tab>
</Tabs>

Import classes from `truss_train`:

```python  theme={"system"}
from truss_train import definitions
```

***

## Programmatic job submission

### push

Submits a training job programmatically from Python code. Use this when you need to:

* Build an API endpoint that receives training requests.
* Dynamically configure training jobs based on user input.
* Integrate training into your application workflow.

<Note>
  Before using `push()`, authenticate with `truss login` or ensure your Baseten API key is configured.
  See [CLI authentication](/reference/cli/truss/login).
</Note>

```python  theme={"system"}
from truss_train.public_api import push

def push(
    config: Path,            # Path to config.py defining the training project
    remote: str = "baseten"  # Remote provider (defaults to "baseten")
) -> dict
```

The function returns a dictionary containing the created training project and job:

```python  theme={"system"}
{
    "training_project": TrainingProject,
    "training_job": TrainingJob,
}
```

**Example:**

To submit a training job programmatically, create a `config.py` file and call `push`:

```python  theme={"system"}
from pathlib import Path
from truss_train.public_api import push

result = push(config=Path("./training/config.py"))

print(f"Project ID: {result['training_project']['id']}")
print(f"Job ID: {result['training_job']['id']}")
```

For dynamic job configuration, write runtime parameters to a file before calling `push`:

```python  theme={"system"}
import json
import shutil
import tempfile
from pathlib import Path

from truss_train.public_api import push


def submit_training_job(dataset_id: str, model_id: str) -> dict:
    """Submit a training job with dynamic configuration."""
    template_dir = Path("./training_template")

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)

        # Copy training template
        shutil.copytree(template_dir, tmp_path, dirs_exist_ok=True)

        # Write runtime configuration
        runtime_config = {
            "dataset_id": dataset_id,
            "model_id": model_id,
        }
        (tmp_path / "runtime_config.json").write_text(
            json.dumps(runtime_config, indent=2)
        )

        # Submit the job
        return push(config=tmp_path / "config.py")


result = submit_training_job(
    dataset_id="HuggingFaceH4/Multilingual-Thinking",
    model_id="meta-llama/Llama-3.1-8B",
)
```

Your `config.py` can read the runtime configuration at import time:

```python  theme={"system"}
import json
from pathlib import Path

from truss.base import truss_config
from truss_train import definitions

# Read dynamic configuration
config_path = Path(__file__).parent / "runtime_config.json"
runtime_config = json.loads(config_path.read_text())

training_runtime = definitions.Runtime(
    start_commands=["python train.py"],
    environment_variables={
        "MODEL_ID": runtime_config["model_id"],
        "DATASET_ID": runtime_config["dataset_id"],
        "HF_TOKEN": definitions.SecretReference(name="hf_access_token"),
    },
    checkpointing_config=definitions.CheckpointingConfig(enabled=True),
)

training_compute = definitions.Compute(
    accelerator=truss_config.AcceleratorSpec(
        accelerator=truss_config.Accelerator.H100,
        count=2,
    ),
)

training_job = definitions.TrainingJob(
    image=definitions.Image(base_image="pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime"),
    compute=training_compute,
    runtime=training_runtime,
)

training_project = definitions.TrainingProject(
    name=runtime_config.get("project_name", "dynamic-training"),
    job=training_job,
)
```

**After submitting:**

Once a job is submitted, use the Training API to monitor progress:

* [Get job status](/reference/training-api/get-training-job).
* [Get job logs](/reference/training-api/get-training-job-logs).
* [Get job metrics](/reference/training-api/get-training-job-metrics).
* [List checkpoints](/reference/training-api/get-training-job-checkpoints).

For a complete working example, see the [programmatic training API recipe](https://github.com/basetenlabs/ml-cookbook/tree/main/recipes/programmatic-training-api).

***

## TrainingProject

Organizes training jobs and provides project-level configuration.

```python  theme={"system"}
class TrainingProject:
    name: str                        # Project name (required)
    job: TrainingJob                 # Training job configuration (required)
    team_name: Optional[str] = None  # Team that owns this project
```

**Example:**

```python  theme={"system"}
from truss_train import definitions

project = definitions.TrainingProject(
    name="llm-fine-tuning",
    job=training_job,
    team_name="my-team"  # Optional
)
```

## TrainingJob

Defines a complete training job configuration.

```python  theme={"system"}
class TrainingJob:
    image: Image                     # Container image configuration (required)
    compute: Compute = Compute()     # Compute resource configuration
    runtime: Runtime = Runtime()     # Runtime environment configuration
    name: Optional[str] = None       # Job name
```

**Example:**

```python  theme={"system"}
from truss_train import definitions
from truss.base import truss_config

training_job = definitions.TrainingJob(
    name="fine-tune-v1",
    image=definitions.Image(base_image="pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime"),
    compute=definitions.Compute(
        accelerator=truss_config.AcceleratorSpec(
            accelerator=truss_config.Accelerator.H100,
            count=4
        )
    ),
    runtime=definitions.Runtime(
        start_commands=["chmod +x ./run.sh && ./run.sh"],
        checkpointing_config=definitions.CheckpointingConfig(enabled=True),
        cache_config=definitions.CacheConfig(enabled=True),
    )
)
```

## Image

Specifies the container image for the training environment.

```python  theme={"system"}
class Image:
    base_image: str                          # Docker image to use (required)
    docker_auth: Optional[DockerAuth] = None # Authentication for private images
```

**Example:**

```python  theme={"system"}
image = definitions.Image(
    base_image="pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime"
)
```

### DockerAuth

Configures authentication for private Docker registries. Store secrets in your [Baseten workspace](/organization/secrets).

```python  theme={"system"}
class DockerAuth:
    auth_method: truss_config.DockerAuthType                                   # Authentication method
    registry: str                                                              # Docker registry URL
    aws_iam_docker_auth: Optional[AWSIAMDockerAuth] = None                     # AWS ECR auth
    gcp_service_account_json_docker_auth: Optional[GCPServiceAccountJSONDockerAuth] = None  # GCP auth
```

#### AWSIAMDockerAuth

Authenticates with AWS ECR using IAM credentials.

```python  theme={"system"}
class AWSIAMDockerAuth:
    access_key_secret_ref: SecretReference          # AWS access key ID
    secret_access_key_secret_ref: SecretReference   # AWS secret access key
```

**Example:**

```python  theme={"system"}
from truss.base import truss_config

image = definitions.Image(
    base_image="123456789.dkr.ecr.us-east-1.amazonaws.com/my-image:latest",
    docker_auth=definitions.DockerAuth(
        auth_method=truss_config.DockerAuthType.AWS_IAM,
        registry="123456789.dkr.ecr.us-east-1.amazonaws.com",
        aws_iam_docker_auth=definitions.AWSIAMDockerAuth(
            access_key_secret_ref=definitions.SecretReference(name="aws_access_key"),
            secret_access_key_secret_ref=definitions.SecretReference(name="aws_secret_key")
        )
    )
)
```

#### GCPServiceAccountJSONDockerAuth

Authenticates with Google Container Registry using service account JSON.

```python  theme={"system"}
class GCPServiceAccountJSONDockerAuth:
    service_account_json_secret_ref: SecretReference  # GCP service account JSON
```

**Example:**

```python  theme={"system"}
from truss.base import truss_config

image = definitions.Image(
    base_image="gcr.io/my-project/my-image:latest",
    docker_auth=definitions.DockerAuth(
        auth_method=truss_config.DockerAuthType.GCP_SERVICE_ACCOUNT_JSON,
        registry="gcr.io",
        gcp_service_account_json_docker_auth=definitions.GCPServiceAccountJSONDockerAuth(
            service_account_json_secret_ref=definitions.SecretReference(name="gcp_service_account_json")
        )
    )
)
```

## Compute

Specifies compute resources for training jobs.

```python  theme={"system"}
class Compute:
    node_count: int = 1                              # Number of nodes for distributed training
    cpu_count: int = 1                               # Number of CPU cores
    memory: str = "2Gi"                              # Memory allocation
    accelerator: Optional[AcceleratorSpec] = None    # GPU configuration
```

**Example:**

```python  theme={"system"}
from truss.base import truss_config

compute = definitions.Compute(
    node_count=2,
    cpu_count=8,
    memory="64Gi",
    accelerator=truss_config.AcceleratorSpec(
        accelerator=truss_config.Accelerator.H100,
        count=4
    )
)
```

### AcceleratorSpec

Configures GPU resources.

```python  theme={"system"}
class AcceleratorSpec:
    accelerator: Optional[Accelerator] = None  # GPU type
    count: int = 1                             # Number of GPUs
```

### Accelerator

Supported GPU types for training jobs.

| Value       | Description        |
| ----------- | ------------------ |
| `T4`        | NVIDIA T4          |
| `L4`        | NVIDIA L4          |
| `A10G`      | NVIDIA A10G        |
| `V100`      | NVIDIA V100        |
| `A100`      | NVIDIA A100 (80GB) |
| `A100_40GB` | NVIDIA A100 (40GB) |
| `H100`      | NVIDIA H100 (80GB) |
| `H100_40GB` | NVIDIA H100 (40GB) |
| `H200`      | NVIDIA H200        |
| `B200`      | NVIDIA B200        |

## Runtime

Defines the runtime environment for training jobs.

```python  theme={"system"}
class Runtime:
    start_commands: List[str] = []                                       # Commands to run at job start
    environment_variables: Dict[str, Union[str, SecretReference]] = {}   # Environment variables
    checkpointing_config: CheckpointingConfig = CheckpointingConfig()    # Checkpointing settings
    cache_config: Optional[CacheConfig] = None                           # Cache settings
    load_checkpoint_config: Optional[LoadCheckpointConfig] = None        # Load checkpoints from previous jobs
```

<Note>
  The `enable_cache` field is deprecated. Use `cache_config` with `enabled=True` instead.
</Note>

**Example:**

```python  theme={"system"}
runtime = definitions.Runtime(
    start_commands=["chmod +x ./run.sh && ./run.sh"],
    environment_variables={
        "BATCH_SIZE": "32",
        "WANDB_API_KEY": definitions.SecretReference(name="wandb_api_key"),
        "HF_TOKEN": definitions.SecretReference(name="hf_access_token"),
    },
    checkpointing_config=definitions.CheckpointingConfig(enabled=True),
    cache_config=definitions.CacheConfig(enabled=True),
)
```

### SecretReference

Securely references secrets stored in your [Baseten workspace](/organization/secrets).

```python  theme={"system"}
class SecretReference:
    name: str  # Name of the secret in your workspace
```

**Example:**

```python  theme={"system"}
secret_ref = definitions.SecretReference(name="wandb_api_key")
```

### CheckpointingConfig

Configures model checkpointing behavior during training. When enabled, Baseten exports `$BT_CHECKPOINT_DIR` in your job's environment. Save your model to this directory to preserve checkpoints for deployment.

```python  theme={"system"}
class CheckpointingConfig:
    enabled: bool = False                      # Enable checkpointing
    checkpoint_path: Optional[str] = None      # Custom checkpoint directory path
    volume_size_gib: Optional[int] = None      # Custom checkpoint volume size
```

**Example:**

```python  theme={"system"}
checkpointing = definitions.CheckpointingConfig(
    enabled=True,
    volume_size_gib=500  # 500 GiB checkpoint storage
)
```

### CacheConfig

Configures caching for training jobs. The cache persists data between jobs within a project or team.

```python  theme={"system"}
class CacheConfig:
    enabled: bool = False                 # Enable caching
    enable_legacy_hf_mount: bool = False  # Enable legacy Hugging Face cache mount
    require_cache_affinity: bool = True   # Prefer nodes with cached data
    mount_base_path: str = "/root/.cache" # Base path for cache mounts
```

When enabled, Baseten provides two cache directories.

| Environment Variable    | Description                                |
| ----------------------- | ------------------------------------------ |
| `$BT_PROJECT_CACHE_DIR` | Shared across jobs within the same project |
| `$BT_TEAM_CACHE_DIR`    | Shared across jobs within the same team    |

**Example:**

```python  theme={"system"}
cache = definitions.CacheConfig(
    enabled=True,
    require_cache_affinity=True
)
```

### LoadCheckpointConfig

Configures loading checkpoints from previous training jobs to resume training.

```python  theme={"system"}
class LoadCheckpointConfig:
    enabled: bool = False                    # Enable checkpoint loading
    checkpoints: List[BasetenCheckpoint]     # Checkpoints to load
    download_folder: str = "/tmp/loaded_checkpoints"  # Where to download checkpoints
```

**Example:**

```python  theme={"system"}
load_config = definitions.LoadCheckpointConfig(
    enabled=True,
    download_folder="/tmp/loaded_checkpoints",
    checkpoints=[
        definitions.BasetenCheckpoint.from_latest_checkpoint(project_name="my-project"),
        definitions.BasetenCheckpoint.from_named_checkpoint(
            checkpoint_name="checkpoint-24",
            job_id="abc123"
        )
    ]
)
```

### BasetenCheckpoint

Factory class for referencing checkpoints from previous training jobs.

#### from\_latest\_checkpoint

Load the most recent checkpoint from a project or job.

```python  theme={"system"}
BasetenCheckpoint.from_latest_checkpoint(
    project_name: Optional[str] = None,  # Project name
    job_id: Optional[str] = None         # Job ID
)
```

At least one of `project_name` or `job_id` is required.

#### from\_named\_checkpoint

Load a specific checkpoint by name.

```python  theme={"system"}
BasetenCheckpoint.from_named_checkpoint(
    checkpoint_name: str,  # Checkpoint name (required)
    job_id: str            # Job ID (required)
)
```

**Example:**

```python  theme={"system"}
# Load most recent checkpoint from a project
latest = definitions.BasetenCheckpoint.from_latest_checkpoint(
    project_name="my-fine-tuning-project"
)

# Load specific checkpoint
specific = definitions.BasetenCheckpoint.from_named_checkpoint(
    checkpoint_name="checkpoint-100",
    job_id="abc123"
)

# Use in LoadCheckpointConfig
runtime = definitions.Runtime(
    start_commands=["python train.py"],
    load_checkpoint_config=definitions.LoadCheckpointConfig(
        enabled=True,
        checkpoints=[latest, specific]
    )
)
```

## Environment variables

Baseten automatically provides environment variables in your training job's environment.

### Standard variables

| Variable                   | Description                     | Example                         |
| -------------------------- | ------------------------------- | ------------------------------- |
| `BT_TRAINING_JOB_ID`       | Training job ID                 | `"gvpql31"`                     |
| `BT_TRAINING_PROJECT_ID`   | Training project ID             | `"aghi527"`                     |
| `BT_TRAINING_JOB_NAME`     | Training job name               | `"gpt-oss-20b-lora"`            |
| `BT_TRAINING_PROJECT_NAME` | Training project name           | `"gpt-oss-finetunes"`           |
| `BT_NUM_GPUS`              | Number of GPUs per node         | `"4"`                           |
| `BT_CHECKPOINT_DIR`        | Checkpoint save directory       | `"/mnt/ckpts"`                  |
| `BT_LOAD_CHECKPOINT_DIR`   | Loaded checkpoints directory    | `"/tmp/loaded_checkpoints"`     |
| `BT_PROJECT_CACHE_DIR`     | Project-level cache directory   | `"/root/.cache/user_artifacts"` |
| `BT_TEAM_CACHE_DIR`        | Team-level cache directory      | `"/root/.cache/team_artifacts"` |
| `BT_RW_CACHE_DIR`          | Base read-write cache directory | `"/root/.cache"`                |
| `BT_RETRY_COUNT`           | Job retry attempt count         | `"0"`                           |

### Multi-node variables

For distributed training across multiple nodes:

| Variable         | Description                   | Example      |
| ---------------- | ----------------------------- | ------------ |
| `BT_GROUP_SIZE`  | Number of nodes in deployment | `"2"`        |
| `BT_LEADER_ADDR` | Leader node address           | `"10.0.0.1"` |
| `BT_NODE_RANK`   | Node rank (0 for leader)      | `"0"`        |

Any standard port number (e.g., `29500`) works for distributed training.

***

## Deploy checkpoints

Deploy trained model checkpoints to Baseten's inference platform.

### Deploy with CLI wizard

Deploy checkpoints interactively with the CLI wizard:

```bash  theme={"system"}
truss train deploy_checkpoints --job-id <job_id>
```

The wizard guides you through selecting checkpoints and configuring deployment. Baseten automatically recognizes checkpoints for full fine-tunes and LoRAs for LLMs and Whisper models.

<Note>
  FSDP checkpoints aren't supported by `deploy_checkpoints` and must be manually configured in the Truss config.
</Note>

<Note>
  For optimized inference with TensorRT-LLM, see [Deploy checkpoints with Engine Builder](/engines/performance-concepts/deployment-from-training-and-s3).
</Note>

### Deploy with static configuration

Create a Python config file for repeatable deployments:

```bash  theme={"system"}
truss train deploy_checkpoints --config <path_to_config_file>
```

## DeployCheckpointsConfig

Specifies configuration for deploying trained model checkpoints.

```python  theme={"system"}
class DeployCheckpointsConfig:
    checkpoint_details: Optional[CheckpointList] = None          # Checkpoints to deploy
    model_name: Optional[str] = None                             # Name for the deployed model
    runtime: Optional[DeployCheckpointsRuntime] = None           # Runtime configuration
    compute: Optional[Compute] = None                            # Compute resources
```

**Example:**

```python  theme={"system"}
from truss_train import definitions
from truss.base import truss_config

deploy_config = definitions.DeployCheckpointsConfig(
    model_name="fine-tuned-llm",
    checkpoint_details=definitions.CheckpointList(
        base_model_id="meta-llama/Llama-3.1-8B-Instruct",
        checkpoints=[
            definitions.LoRACheckpoint(
                training_job_id="gvpql31",
                checkpoint_name="checkpoint-100",
                lora_details=definitions.LoRADetails(rank=16)
            )
        ]
    ),
    compute=definitions.Compute(
        accelerator=truss_config.AcceleratorSpec(
            accelerator=truss_config.Accelerator.H100,
            count=1
        )
    )
)
```

### DeployCheckpointsRuntime

Configures the runtime environment for deployed checkpoints.

```python  theme={"system"}
class DeployCheckpointsRuntime:
    environment_variables: Dict[str, Union[str, SecretReference]] = {}
```

### CheckpointList

Manages a collection of checkpoints for deployment.

```python  theme={"system"}
class CheckpointList:
    download_folder: str = "/tmp/training_checkpoints"  # Download location
    base_model_id: Optional[str] = None                 # Base model identifier
    checkpoints: List[Checkpoint] = []                  # List of checkpoints
```

### Checkpoint types

Baseten supports two checkpoint types based on model weight format.

#### FullCheckpoint

For full model fine-tunes.

```python  theme={"system"}
class FullCheckpoint:
    training_job_id: str                                # Training job ID (required)
    checkpoint_name: str                                # Checkpoint name (required)
    model_weight_format: ModelWeightsFormat = "full"    # Auto-set
```

#### LoRACheckpoint

For LoRA adapter weights.

```python  theme={"system"}
class LoRACheckpoint:
    training_job_id: str                                # Training job ID (required)
    checkpoint_name: str                                # Checkpoint name (required)
    model_weight_format: ModelWeightsFormat = "lora"    # Auto-set
    lora_details: LoRADetails = LoRADetails()           # LoRA configuration
```

### LoRADetails

Configuration for LoRA adapters.

```python  theme={"system"}
class LoRADetails:
    rank: int = 16  # LoRA rank
```

**Valid ranks:** 8, 16, 32, 64, 128, 256, 320, 512.

### ModelWeightsFormat

Enum for checkpoint weight formats.

| Value  | Description          |
| ------ | -------------------- |
| `lora` | LoRA adapter weights |
| `full` | Full model weights   |
