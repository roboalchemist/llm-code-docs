# Source: https://docs.baseten.co/development/model/data-directory.md

# Data and storage

> Load model weights without Hugging Face or S3

Model files, such as weights, can be **large** (often **multiple GBs**). Truss supports **multiple ways** to load them efficiently:

* **Public Hugging Face models** (default)
* **Bundled directly in Truss**

### 1. Bundling model weights in Truss

Store model files **inside Truss** using the `data/` directory.

**Example: Stable Diffusion 2.1 Truss structure**

```pssql  theme={"system"}
data/
    scheduler/
        scheduler_config.json
    text_encoder/
        config.json
        diffusion_pytorch_model.bin
    tokenizer/
        merges.txt
        tokenizer_config.json
        vocab.json
    unet/
        config.json
        diffusion_pytorch_model.bin
    vae/
        config.json
        diffusion_pytorch_model.bin
    model_index.json
```

**Access bundled files in `model.py`:**

```python  theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self._data_dir = kwargs["data_dir"]

    def load(self):
        self.model = StableDiffusionPipeline.from_pretrained(
            str(self._data_dir),
            revision="fp16",
            torch_dtype=torch.float16,
        ).to("cuda")
```

<Warning>
  Limitation: Large weights increase deployment size, making it slower. Consider
  cloud storage instead.
</Warning>

## 2. Loading private model weights from S3

If using **private S3 storage**, first **configure secure authentication**.

### Step 1: Define AWS secrets in `config.yaml`

```yaml  theme={"system"}
secrets:
  aws_access_key_id: null
  aws_secret_access_key: null
  aws_region: null # e.g., us-east-1
  aws_bucket: null
```

<Warning>
  Do not store actual credentials here. Add them securely to [Baseten secrets
  manager](https://app.baseten.co/settings/secrets).
</Warning>

### Step 2: Authenticate with AWS in `model.py`

```python  theme={"system"}
import boto3

def __init__(self, **kwargs):
    self._config = kwargs.get("config")
    secrets = kwargs.get("secrets")
    self.s3_client = boto3.client(
        "s3",
        aws_access_key_id=secrets["aws_access_key_id"],
        aws_secret_access_key=secrets["aws_secret_access_key"],
        region_name=secrets["aws_region"],
    )
    self.s3_bucket = secrets["aws_bucket"]
```

### Step 3: Deploy

```sh  theme={"system"}
truss push
```
