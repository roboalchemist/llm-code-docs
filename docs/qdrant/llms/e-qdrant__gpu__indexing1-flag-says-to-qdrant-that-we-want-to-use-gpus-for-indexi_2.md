# `-e QDRANT__GPU__INDEXING=1` flag says to Qdrant that we want to use GPUs for indexing.
docker run \
	--rm \
	--device /dev/kfd --device /dev/dri \
	-p 6333:6333 \
	-p 6334:6334 \
	-e QDRANT__LOG_LEVEL=debug \
	-e QDRANT__GPU__INDEXING=1 \
	qdrant/qdrant:gpu-amd-latest

```

Check logs to confirm GPU initialization. Example log output:

```text
2025-01-10T11:56:55.926466Z  INFO gpu::instance: Found GPU device: AMD Radeon Graphics (RADV GFX1103_R1)
2025-01-10T11:56:55.926485Z  INFO gpu::instance: Found GPU device: llvmpipe (LLVM 17.0.6, 256 bits)
2025-01-10T11:56:55.926504Z  INFO gpu::device: Create GPU device AMD Radeon Graphics (RADV GFX1103_R1)

```

This concludes the setup. In a basic scenario, you won’t need to configure anything else.

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#known-limitations) Known limitations

- **Platform Support:** Docker images are only available for Linux x86\_64. Windows, macOS, ARM, and other platforms are not supported.

- **Memory Limits:** Each GPU can process up to 16GB of vector data per indexing iteration.


Due to this limitation, you should not create segments where either original vectors OR quantized vectors are larger than 16GB.

For example, a collection with 1536d vectors and scalar quantization can have at most:

```text
16Gb / 1536 ~= 11 million vectors per segment

```

And without quantization:

```text
16Gb / 1536 * 4 ~= 2.7 million vectors per segment

```

The maximum size of each segment can be configured in the collection settings.
Use the following operation to [change](https://qdrant.tech/documentation/concepts/collections/#update-collection-parameters) on your existing collection:

```http
PATCH collections/{collection_name}
{
  "optimizers_config": {
    "max_segment_size": 1000000
  }
}

```

Note that `max_segment_size` is specified in KiloBytes.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/running-with-GPU.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/running-with-GPU.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-156-lllmstxt|>
## optimizer
- [Documentation](https://qdrant.tech/documentation/)
- [Concepts](https://qdrant.tech/documentation/concepts/)
- Optimizer