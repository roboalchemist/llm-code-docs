# Source: https://docs.verda.com/containers/storage.md

# Storage

Verda Containers supports two types of persistent storage that can be attached to your deployments and batch jobs. Both are mounted into each replica and **persist independently of replica lifecycle** — storage is retained even when your deployment scales down to zero.

## Storage Types

### General Storage (scratch disk)

Each deployment or batch will by default have a scratch disk attached — a **500 GB** block storage volume dedicated to that deployment. It is automatically provisioned and requires no prior setup.

The default mount path is `/data`, but you can configure a custom path when creating or editing your deployment.

Use the scratch disk for:

* Caching model weights on first load to avoid re-downloading on every cold start
* Temporary working files generated during inference
* Output files for batch jobs before uploading to a final destination

### Shared Filesystem (SFS)

A [Shared Filesystem (SFS)](https://docs.verda.com/storage/shared-filesystems-sfs) is a network filesystem you provision separately and can attach to one or more deployments. Unlike the scratch disk, an SFS can be shared across multiple deployments simultaneously and its size is determined by what you provision.

The default mount path is `/mnt/<sfs-name>`, for example `/mnt/SFS-k3r7N33Z`. You can configure a custom path when attaching the SFS to your deployment.

Use SFS for:

* If you want to share storage between VM and container (for example training and inference)
* If you need interactive access to the storage

## Configuring Storage

Storage is configured per deployment in the Verda console or via the API. For each storage option you can set:

* **Mount path** — where the storage appears inside the container
* **Size** - for SFS you can in the Storage / Shared filesystems section of the console edit the size of an existing SFS volume.

Both storage types are available for serverless container deployments and batch jobs.

## Use Cases

### Caching Model Weights

Downloading large model weights on every cold start is slow and expensive. By pointing your model loading library to persistent storage, weights are downloaded once and reused across restarts.

### Hugging Face Transformers / Diffusers

Set the `HF_HOME` environment variable to a path on your scratch disk or SFS by editing the environment variables section of your container/jobs settings.

```bash
Name = HF_HOME
Value = /data/hf-cache
```

On first startup, the model is downloaded to `/data/hf-cache`. On subsequent cold starts, it loads directly from disk.

**Other common environment variables:**

| Variable             | Library               | Purpose                                    |
| -------------------- | --------------------- | ------------------------------------------ |
| `HF_HOME`            | Hugging Face (all)    | Cache dir for models, datasets, tokenizers |
| `TRANSFORMERS_CACHE` | Transformers (legacy) | Model weights cache                        |
| `HF_DATASETS_CACHE`  | Datasets              | Dataset cache                              |
| `TORCH_HOME`         | PyTorch               | Model hub cache                            |

### Sharing Weights Across Deployments

If you run multiple deployments using the same base model, attach the same SFS to each deployment. Download the weights once, and all deployments load from the shared volume:

```bash
Name = HF_HOME
Value = /mnt/my-sfs/hf-cache # replace the mount path of the SFS
```

### Training on a VM, Serving from a Container

A common workflow is to fine-tune or train a model on a GPU instance and then serve it directly from a container deployment without any intermediate upload/download step:

1. Provision a GPU instance and attach your SFS
2. Train or fine-tune your model, saving weights to the SFS (e.g. `/mnt/SFS-k3r7N33Z/my-model`)
3. Create a container deployment, attach the same SFS, and point your model loader to the SFS path

The inference container loads weights directly from the SFS — no S3 upload or re-download required.

### Interactive Access to SFS

If you need to browse, edit, or manage files on an SFS outside of a container deployment (e.g. to inspect outputs, upload datasets, or organize weights), provision a small CPU instance and mount the SFS to it. This gives you a persistent interactive shell with direct access to the filesystem.

See [Mounting a shared filesystem](https://docs.verda.com/storage/shared-filesystems-sfs/mounting-a-shared-filesystem) for instructions.

{% hint style="info" %}
Remember that scratch disk storage is **per deployment** — two different deployments each have their own separate scratch disk. Use SFS if you need to share files across deployments.
{% endhint %}
