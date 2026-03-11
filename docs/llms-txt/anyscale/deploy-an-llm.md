# Source: https://docs.anyscale.com/tutorials/deploy-an-llm.md

# Deploy Llama 3.1 8b

[View Markdown](/tutorials/deploy-an-llm.md)

# Deploy Llama 3.1 8b

This example uses Ray Serve along with vLLM to deploy a Llama 3.1 8b model as an Anyscale service.

## Install the Anyscale CLI[​](#install "Direct link to Install the Anyscale CLI")

```
pip install -U anyscale
anyscale login
```

## Deploy the service[​](#deploy "Direct link to Deploy the service")

Clone the example from GitHub.

```
git clone https://github.com/anyscale/examples.git
cd examples/03_deploy_llama_3_8b
```

Deploy the service. Use `--env` to forward your Hugging Face token if you need authentication for gated models such as Llama 3.

```
export HF_TOKEN=<INSERT HUGGING FACE TOKEN HERE>
anyscale service deploy -f service.yaml --env HF_TOKEN=$HF_TOKEN
```

If you’re using an ungated model, go to your `LLMConfig` (in `serve_llama_3_1_8b.py`), and set `model_source` to that model. Then, you can omit the Hugging Face token from both the config and the `anyscale service deploy` command.

## Understanding the example[​](#understanding-the-example "Direct link to Understanding the example")

* The [application code](https://github.com/anyscale/examples/blob/main/03_deploy_llama_3_8b/serve_llama_3_1_8b.py) sets the required accelerator type with `accelerator_type="L4"`. To use a different accelerator, replace `"L4"` with the desired name. See the [list of supported accelerators](https://docs.ray.io/en/latest/ray-core/accelerator-types.html#accelerator-types) for available options.
* Ray Serve automatically autoscales the number of model replicas between `min_replicas` and `max_replicas`. Ray Serve adapts the number of replicas by monitoring queue sizes. For more information on configuring autoscaling, see the [AutoscalingConfig documentation](https://docs.ray.io/en/latest/serve/api/doc/ray.serve.config.AutoscalingConfig.html).
* This example uses vLLM, and the [Dockerfile](https://github.com/anyscale/examples/blob/main/03_deploy_llama_3_8b/Dockerfile) defines the service’s dependencies. When you run `anyscale service deploy`, the build process adds these dependencies on top of an Anyscale-provided base image.
* To configure vLLM, modify the `engine_kwargs` dictionary. See [Ray documentation for the `LLMConfig` object](https://docs.ray.io/en/latest/serve/api/doc/ray.serve.llm.LLMConfig.html#ray.serve.llm.LLMConfig).

## Query the service[​](#query-the-service "Direct link to Query the service")

The `anyscale service deploy` command outputs a line that looks like

```
curl -H "Authorization: Bearer <SERVICE_TOKEN>" <BASE_URL>
```

From the output, you can extract the service token and base URL. Open [query.py](https://github.com/anyscale/examples/blob/main/03_deploy_llama_3_8b/query.py) and add them to the appropriate fields.

```
token = <SERVICE_TOKEN> 
base_url = <BASE_URL> 
```

Query the model

```
pip install openai
python query.py
```

View the service in the [services tab](https://console.anyscale.com/services) of the Anyscale console.

## Shutdown[​](#shutdown "Direct link to Shutdown")

Shutdown your Anyscale Service:

```
anyscale service terminate -n deploy-llama-3-1-8b
```
