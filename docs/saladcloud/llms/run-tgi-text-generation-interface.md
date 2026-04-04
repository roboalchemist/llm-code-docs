# Source: https://docs.salad.com/container-engine/how-to-guides/ai-machine-learning/run-tgi-text-generation-interface.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run TGI (Text Generation Interface) by Hugging Face

*Last Updated: August 04, 2025*

TGI (Text Generation Interface) is a toolkit for deploying and service Large Language Models (LLMs). TGI enables
high-performance text generation for the most popular open-source LLMs, including Llama, Falcon, StarCoder, BLOOM,
GPT-NeoX, and T5.

[Learn More Here](https://huggingface.co/docs/text-generation-inference/main/en/index)

[Github Repo](https://github.com/huggingface/text-generation-inference)

# Deploying TGI on Salad

## Container

Hugging Face provides a pre-built docker available via the Github Container registry.

```Text Docker theme={null}
ghcr.io/huggingface/text-generation-inference:1.1.1
```

In order to deploy the container on Salad, you will need to configure the container with your desired models, plus any
additional settings. These options can either be configured as part of the `CMD` or can be set as
[Environment Variables](/container-engine/how-to-guides/environment-variables) when creating your container group. Here
is a complete list of
[all TGI options](https://huggingface.co/docs/text-generation-inference/main/en/basic_tutorials/launcher)

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1074d8d-image.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b93e65c68a9aef7bc6a697fa7527ca40" data-og-width="535" width="535" data-og-height="899" height="899" data-path="container-engine/images/1074d8d-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1074d8d-image.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=7f5aa49dfc8c7465fe4fb06e1b6a1a6b 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1074d8d-image.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e18173e78494f4d12ef9f67e04453fca 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1074d8d-image.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=315d7d36c1c0cbb1f4b7cda27523ca4e 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1074d8d-image.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2efee100778e4d3e089b9a436b1fb90e 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1074d8d-image.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2eba2b8a990e71683baa4e774e7e25ee 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1074d8d-image.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1160a052e435ba5e07ba8f1749a9b226 2500w" />

## Required - Container Gateway Setup

In addition to any options that you need to run the model, you will need to configure TGI to use
[IPv6](/container-engine/how-to-guides/gateway/enabling-ipv6) in order to be compatible with SaladCloud's Container
Gateway feature. This is done by simply setting `HOSTNAME` to `::`

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/064f253-image.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=76f4789b8a75ba04b4c69b43f92deec5" data-og-width="535" width="535" data-og-height="524" height="524" data-path="container-engine/images/064f253-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/064f253-image.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6183b9cf59fd6b492f6dc0e4b3989acd 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/064f253-image.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=9aba9c511408b884e15bd1a64d2b5529 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/064f253-image.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b19d0a5bab4e40270a55607b4d77b3db 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/064f253-image.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5fe8ec829c6d1567fad67dce448e7e71 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/064f253-image.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=0168648f826eba61c145f276c446bd56 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/064f253-image.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e04187621dad918488280fc06c2702f0 2500w" />

## Recommended - Health Probes

[Health Probes](/container-engine/explanation/infrastructure-platform/health-probes) help ensure that your container
only serves traffic it is ready and ensures that the container continues to run as expected. When the TGI container
starts up, it begins to download the specific model before it can start serving requests. While the model is
downloading, the API is unavailable. The simplest health probe is to check the `/health` endpoint. If the endpoint is
running, then the model is ready to serve traffic.

### Exec Health Probe

The `exec` health probe will run the given command inside the container, if the command returns an exit code of 0, the
container is considered in a healthy state. Any other exit codes indicate the container is not ready yet.

The TGI container does not include `curl` or `wget` so in order to check the `:80/health` API we decided to use python's
requests to check the API.

```Text bin theme={null}
python -c "import requests,sys;sys.exit(0 if requests.get('http://localhost:80/health').status_code == 200 else -1)"
```

<img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e851b39-image.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=5bbe3d118818aaa5ee3e0388571ae67c" data-og-width="536" width="536" data-og-height="937" height="937" data-path="container-engine/images/e851b39-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e851b39-image.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=3a152dd34423c6dbdc5941509e86bbf8 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e851b39-image.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=b25c67165d7c861affa4bfb9e27c8e6f 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e851b39-image.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=8593fe8fbc4e96985a0deb772a6e1926 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e851b39-image.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=2de0974698f4c3367489ee6c8ca296e9 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e851b39-image.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=249cb08c0934f0a76f11e7cf68a59a09 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e851b39-image.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=b0d12207c3b7f046339843ea64e80e08 2500w" />

### Required Environment Variables

* `SHARDED=true` Enables TGI's sharded mode. If this is set and no additional options are provided, TGI will use **all
  visible GPUs**. Requires `CUDA_VISIBLE_DEVICES` to be set to expose GPUs to TGI.

* `NUM_SHARD=<int>` Specifies how many shards to split the model across. Must match the number of GPUs you want TGI to
  use (and must be ≤ the number of visible devices). If this environment variable is set, `SHARDED` is not required.
  `CUDA_VISIBLE_DEVICES` must still be set to expose specified GPUs to TGI.

* `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7` **Required to expose multiple GPUs to the TGI container.** By default, TGI will
  only detect one GPU unless this variable is set. You can also use this to run **multiple workloads** on a single 8-GPU
  node by isolating which GPUs are used by each container. To specify which GPUs TGI should use, provide a list of
  integers as a value.

#### Example: Use All 8 GPUs

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-1.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=538a6dfc792191247a6df825c9ee610b" data-og-width="573" width="573" data-og-height="86" height="86" data-path="container-engine/images/tgi-env-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-1.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=5b3a2d8a0849bb996b90fed379eda9e8 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-1.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d0d48de0d47ccb3198e07585d6208aff 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-1.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=2e82153a8a9c8bd234ef09b7b11bacc3 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-1.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=ab7d33c65229a3e6fe82b2c7215882db 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-1.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d62c39b843de92b58135de32e8317109 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-1.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=ad51c05c4d3f0ba6e045b2ee72ea1b69 2500w" />

or

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-2.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=0ab4d9867488aa78d347b54ce808ee44" data-og-width="577" width="577" data-og-height="86" height="86" data-path="container-engine/images/tgi-env-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-2.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=48de393e6cd64be541de153c8e9c8d09 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-2.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d9274713b8ba9f6bf63d4eb91ecd4273 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-2.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=6bfe87c9321b69c73327fc2f2cfd0539 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-2.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=1b31a6f39a5ab9614b0f61e892616bbd 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-2.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=0ee621e6bcac48199dc362b462ee48e4 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-2.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=55275629228ce7238c23287b0d518066 2500w" />

#### Example: Use Only 2 GPUs

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-3.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=06e9a888ee17485ba8cb2939b68e620c" data-og-width="565" width="565" data-og-height="79" height="79" data-path="container-engine/images/tgi-env-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-3.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=604a0b1919230f89a8614340da96e74c 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-3.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=790b3066ca7d0b2fe66d3bdd12af9cb4 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-3.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=79aa2db8f3e9cbc05c6f6879bd5aef0e 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-3.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=0c90bb3d5fc112b1b5b7da32397a1803 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-3.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=160e9637965ff1c0d5f9dfed8abb2adf 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-env-3.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=6df591a5cf50635774f73203b8de5adc 2500w" />
