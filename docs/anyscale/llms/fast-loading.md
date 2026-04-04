# Source: https://docs.anyscale.com/services/fast-loading.md

# Fast model loading for PyTorch models

[View Markdown](/services/fast-loading.md)

# Fast model loading for PyTorch models

This page provides an overview of Anyscale support for fast model loading for PyTorch models on Anyscale services.

note

This feature is in alpha release. Contact [Anyscale support](mailto:support@anyscale.com) with any feedback.

For an example of using fast model loading, see [Tutorial: Load a custom PyTorch model](/services/fast-loading-tutorial.md).

## What is fast model loading?[​](#what-is "Direct link to What is fast model loading?")

Anyscale provides a library to download model weights saved in [safetensors](https://github.com/huggingface/safetensors) format in remote storage directly to a GPU. Anyscale streams the model weights chunk-by-chunk, avoiding a synchronous download to disk, which speeds up the end-to-end download time for large models. For more technical details and benchmarks, see [this blog post](https://www.anyscale.com/blog/loading-llama-2-70b-20x-faster-with-anyscale-endpoints).

## Requirements[​](#requirements "Direct link to Requirements")

Fast model loading with safetensors requires the following:

* A container image using Ray 2.36.0 or later.
* Save your model weights in a single file using the [safetensors](https://github.com/huggingface/safetensors) format.
  <!-- -->
  * Safetensors files don't include model code. You must initialize the code for your model separately.
* Store the safetensors file containing your model weights in a location accessible using HTTP, such as S3 or a Google Cloud Storage bucket.

## API and usage[​](#api "Direct link to API and usage")

Import and use the `ray.anyscale.safetensors.torch.load_file` function to download model weights from remote storage in a streaming fashion.

You capture the results from this function in a `state_dict` object that you then use to initialize a PyTorch model, as in the following example:

```
import torch
from typing import Dict

from ray.anyscale.safetensors.torch import load_file

# Stream model weights from remote storage onto the GPU.
state_dict: Dict[str, torch.Tensor] = load_file(
    "s3://my_bucket/model.safetensors", device="cuda",
)

# Initialize PyTorch model using the downloaded model weights.
model: torch.nn.Module = torch.nn.utils.skip_init(MyTorchModel)
model.load_state_dict(state_dict, assign=True)
```

The `load_file` function has the following parameters:

| Option     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file_uri` | A remote URI specifying the safetensors file. Supported storage URIs include the following:- `gs://`: Google Cloud Storage buckets.<br />- `s3://`: AWS S3 bucket. You must provide a region when using S3.<br />- `anyscale://`: The default cloud object storage for your Anyscale cloud. See [Access the default artifact storage path](/storage.md#artifact-storage).<br />- `http://` or `https://`: Any HTTP file server that supports the `Range` header. The client doesn't support authentication. |
| `device`   | The device where you're loading the tensors. `cpu` or `cuda`. Defaults to `cpu`.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `region`   | The region of your S3 bucket. Required when using an `s3://` URI.                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Enable local file caching[​](#local-caching "Direct link to Enable local file caching")

By default, the client streams model weights directly to the target device without writing the contents of the `safetensors` file to disk.

If your workflow loads the same model weights multiple times on the same machine, you can enable local file caching to write the file to disk and speed up subsequent loads.

note

Local file caching writes the file asynchronously, writing the file doesn't block using the downloaded tensors.

The following example shows using the `set_local_cache_dir` function to enable local file caching:

```
import torch
from typing import Dict

from ray.anyscale.safetensors.torch import load_file
from ray.anyscale.safetensors import set_local_cache_dir

# Enable local caching to a provided directory.
set_local_cache_dir("/mnt/local_storage/cache/safetensors/")

# Run the `set_local_cache_dir` again with `None` to disable local caching.
# set_local_cache_dir(None)

# The first download streams the model weights to the target device *and* the local cache directory.
# Subsequent downloads to the same URI use the file saved in the local cache directory.
state_dict: Dict[str, torch.Tensor] = load_file("s3://my_bucket/model.safetensors")
```

note

You must call `set_local_cache_dir` inside of your task or actor code rather than the global scope when running inside a Ray application.

## Limitations[​](#limitations "Direct link to Limitations")

Contact [Anyscale support](mailto:support@anyscale.com) if you encounter any issues or have workloads blocked by the following limitations.

The safetensors client:

* Only supports PyTorch tensors.
* Only supports `"cpu"` and `"cuda"` as target devices. You can't specify a specific CUDA device.
* Allocates CPU memory equal to the full size of the safetensors file during the download. Ensure that the instance type you're using has enough memory to accommodate this.
* Doesn't work for PyTorch models that use shared tensors. See the [safetensors documentation](https://huggingface.co/docs/safetensors/torch_shared_tensors) for an explanation.
