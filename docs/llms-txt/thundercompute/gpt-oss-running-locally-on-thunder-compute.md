# Source: https://www.thundercompute.com/docs/guides/gpt-oss-running-locally-on-thunder-compute.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Run GPT‑OSS 120B on Thunder Compute

> A guide to setting up and running GPT‑OSS 120B affordably on Thunder Compute.

# Run GPT‑OSS 120B on Thunder Compute

Looking for the **cheapest way to self‑host GPT‑OSS 120B** or just want to **try it out** without buying hardware? Thunder Compute lets you spin up pay‑per‑minute NVIDIA A100 GPUs, so you only pay for what you use. Follow the steps below to get the model running in minutes.

> **Prerequisite:** Ensure your Thunder Compute account is ready. If not, start with our [Quickstart Guide](/vscode/quickstart).

## Step 1 — Create a Cost‑Effective Prototyping‑Mode GPU Instance

Launch an 80 GB A100 instance (large enough to host the full 120 B model):

```bash  theme={null}
tnr create \
  --gpu a100xl \
  --vcpus 4 \
  --mode prototyping \
  --disk-size-gb 200 \
  --template "ollama"
```

This command starts a lower‑cost [prototyping‑mode](/prototyping-vs-production#prototyping-mode) instance with:

* **GPU:** A100 80 GB
* **vCPUs:** 4
* **Storage:** 200 GB (from the *Ollama* template)

> The GPU, vCPU Count, and Mode ([Prototyping](/prototyping-vs-production#prototyping-mode) / [Production](/prototyping-vs-production#production-mode)), can be changed later if your requirements change, and the amount of storage can be increased if needed.

For details on templates, see the [Instance Templates guide](/guides/using-instance-templates).

## Step 2 — Check Status and Connect

Verify that the instance is running, it can take a minute to spin up:

```bash  theme={null}
tnr status
```

<img src="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/InstanceStatus_v2.png?fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=8952e0d10187de007f34d8daf51d02f1" width="750" alt="Instance status output" data-og-width="1110" data-og-height="340" data-path="images/InstanceStatus_v2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/InstanceStatus_v2.png?w=280&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=87484681d86f337836e23c2a11ba3d90 280w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/InstanceStatus_v2.png?w=560&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=2a9e939515a93339528d6513b9b9ac95 560w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/InstanceStatus_v2.png?w=840&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=992bc7de3c696fb927f7a332b4b841d4 840w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/InstanceStatus_v2.png?w=1100&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=0ca9d41199b45f75b0f0e4f82f8877eb 1100w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/InstanceStatus_v2.png?w=1650&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=f7fdeca9a0ef4c51913b4f3476859455 1650w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/InstanceStatus_v2.png?w=2500&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=416e441e4de6b44401e9cd8fa8097280 2500w" />

Connect to the instance:

```bash  theme={null}
tnr connect <instance‑id>
```

## Step 3 — Start Ollama and Download the Model

Inside the instance, start Ollama (this also launches OpenWebUI and a Cloudflare tunnel):

```bash  theme={null}
start-ollama
```

While the UI is initializing, download the model, here we are downloading the 120B variant of GPT‑OSS, but any models can be downloaded from the [Ollama Model Library](https://ollama.com/library):

```bash  theme={null}
ollama pull gpt-oss:120b
```

> **Tip:** If you encounter issues, consult the [troubleshooting guide](/troubleshooting).

Give the UI about 60 seconds to finish loading.

<img src="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/Ollama_Status.png?fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=862015f33aca829bab32b4a34886a153" width="750" alt="Ollama status output" data-og-width="1218" data-og-height="1200" data-path="images/Ollama_Status.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/Ollama_Status.png?w=280&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=97c2da33bc3bc5cdbfaa6eab9c8ae485 280w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/Ollama_Status.png?w=560&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=b5f1268d086b161c3d089ee3d1c88029 560w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/Ollama_Status.png?w=840&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=8e0c5d31831791a27010f9ff008e85ce 840w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/Ollama_Status.png?w=1100&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=0969f51357adf0c62a1f020a8d6b9400 1100w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/Ollama_Status.png?w=1650&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=628e72313c8fa300dcc5761e0a58d7c4 1650w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/Ollama_Status.png?w=2500&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=9f69bbf3b3480a9370ff385990575519 2500w" />

## Step 4 — Access the Web UI and Select the Model

1. Open `http://localhost:8080` in your browser.
2. Choose **gpt-oss:120b** from the model dropdown.

<img src="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/OpenWebUI_ModelSelect.png?fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=32ca1090e916f64774bbe14450202c97" width="650" alt="OpenWebUI model selection" data-og-width="1110" data-og-height="888" data-path="images/OpenWebUI_ModelSelect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/OpenWebUI_ModelSelect.png?w=280&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=f4d3176bdb23d2acef0d52cff799144c 280w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/OpenWebUI_ModelSelect.png?w=560&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=acd0c762d73d8c130a2a4fc2315ba015 560w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/OpenWebUI_ModelSelect.png?w=840&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=a638fe64f8b42a0bc371f5916e3ef1e4 840w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/OpenWebUI_ModelSelect.png?w=1100&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=51e4bd78b725c776d8eb734a1987f924 1100w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/OpenWebUI_ModelSelect.png?w=1650&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=8d99e74c07ffa3a0d928d874a73b9091 1650w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/OpenWebUI_ModelSelect.png?w=2500&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=dc8a35c0240f4acb365f28a56c68d08d 2500w" />

## Step 5 — Run GPT‑OSS 120B

Enter a prompt in the web interface, for example:

> *“Tell a tale of a seaman who found the treasure of the clouds by following the sound of thunder.”*

## Conclusion

That's it—the **cheapest way to run GPT‑OSS 120B** on Thunder Compute. For more, check out:

* [Using Docker on Thunder Compute](/guides/using-docker-on-thundercompute)
* [Using Instance Templates](/guides/using-instance-templates)
* [Running Jupyter Notebooks](/guides/running-jupyter-notebooks-on-thunder-compute)

Happy building!
