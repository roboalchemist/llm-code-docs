# Source: https://www.thundercompute.com/docs/guides/deepseek-r1-running-locally-on-thunder-compute.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Self-host Deepseek R1

> 5-minute guide. Run Deepseek R1 on your hardware.

# Easily Run DeepSeek R1 on Thunder Compute

Looking for the **cheapest way to run DeepSeek R1** or just want to **try DeepSeek R1** without buying hardware? Thunder Compute lets you spin up pay‑per‑minute A100 GPUs so you only pay for the time you use. Follow the steps below to get the model running in minutes.

> **Quick reminder:** Make sure your Thunder Compute account is set up. If not, start with our [Quickstart Guide](/vscode/quickstart).

If you prefer video instructions, watch this overview:

<iframe width="640" height="360" src="https://www.youtube.com/embed/EukG6P4s5QI?si=Sx3iWsISL8Ve58Uz" title="YouTube video player" frameborder="0" allowfullscreen />

## Step 1: Create a Cost‑Effective GPU Instance

Open your CLI and launch an 80 GB A100 GPU (perfect for the 70B variant):

```bash  theme={null}
tnr create --gpu "a100xl" --template "ollama"
```

For details on instance templates, see our [templates guide](/guides/using-instance-templates).

## Step 2: Check Status and Connect

Verify the instance is running:

```bash  theme={null}
tnr status
```

<img src="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/instance_creation_cli.png?fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=84823035ec9cdf999571cbbb8eec552c" alt="Instance creation in CLI" data-og-width="1506" width="1506" data-og-height="468" height="468" data-path="images/instance_creation_cli.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/instance_creation_cli.png?w=280&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=b600b30194083a44aab529d65096af76 280w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/instance_creation_cli.png?w=560&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=9ad5f3c003071f3a657c09eb4ff8e772 560w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/instance_creation_cli.png?w=840&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=4e83870a26094c040755c4d107593849 840w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/instance_creation_cli.png?w=1100&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=ab9132827a84a52356b16b7b258f228a 1100w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/instance_creation_cli.png?w=1650&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=52ec548b47666a30ef3deb5743440cb0 1650w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/instance_creation_cli.png?w=2500&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=b58137c53caee2f2d6f96d401cf4801f 2500w" />

Connect with its ID:

```bash  theme={null}
tnr connect <instance-id>
```

## Step 3: Start the Ollama Server

Inside the instance, start Ollama:

```bash  theme={null}
start-ollama
```

If you run into issues, check our [troubleshooting guide](/troubleshooting).

Wait about 30 seconds for the web UI to load.

<img src="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/start_ollama.png?fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=979eb17c404ebc35e39127c729b1c9fd" alt="Ollama server startup" data-og-width="1503" width="1503" data-og-height="664" height="664" data-path="images/start_ollama.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/start_ollama.png?w=280&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=863c91519c96b9538f5444cb4dc7b204 280w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/start_ollama.png?w=560&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=c03fec28b015568c626f48523f7a48c6 560w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/start_ollama.png?w=840&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=e8b103e46b2da27ff6871f65a49aa87d 840w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/start_ollama.png?w=1100&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=6335ca5417486639098cce2d1a3d294a 1100w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/start_ollama.png?w=1650&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=e2969b040e5db9ad0424182824cb1b31 1650w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/start_ollama.png?w=2500&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=59d01fec72ea65bb8e99b4de7a64bf89 2500w" />

## Step 4: Access the Web UI and Load DeepSeek R1

1. Visit `http://localhost:8080` in your browser.
2. Choose **DeepSeek R1** from the dropdown. On an 80 GB A100, pick the **70B** variant for peak performance.

<img src="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/web_ui_model_selection.png?fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=08f2a40c7903639955b497e24a18f169" alt="Web UI with model selection" data-og-width="1155" width="1155" data-og-height="409" height="409" data-path="images/web_ui_model_selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/web_ui_model_selection.png?w=280&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=d66a0bf435246015783aa186a0d07c80 280w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/web_ui_model_selection.png?w=560&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=5d11d8545f6e3cd7692da72df413d499 560w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/web_ui_model_selection.png?w=840&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=0897c8ccce1cc3e7f5a923d0ef14fb55 840w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/web_ui_model_selection.png?w=1100&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=a108e144ed812809f7441566bdd8ba8c 1100w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/web_ui_model_selection.png?w=1650&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=8cc08ca68934a47f298238a7994f45cf 1650w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/web_ui_model_selection.png?w=2500&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=766195fe035c68a6f3480fa188d265c0 2500w" />

## Step 5: Run DeepSeek R1

Type a prompt in the web interface. For example:

> *"If the concepts of rCUDA were applied at scale, overcoming latency, what would it mean for the cost of GPUs on cloud providers?"*

The model will think through the answer and respond. A full reply can take up to 200 seconds.

<img src="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/model_response_in_progress.png?fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=9f87e103e9731029652ce28ffc4e1749" alt="Model response in progress" data-og-width="1708" width="1708" data-og-height="513" height="513" data-path="images/model_response_in_progress.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/model_response_in_progress.png?w=280&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=a2d3636390f5f8510bbf4d515f504b4e 280w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/model_response_in_progress.png?w=560&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=a130753d42305e28b201248f48c4287c 560w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/model_response_in_progress.png?w=840&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=c1cb9bebc5c604b1aaaeb40c652c81dc 840w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/model_response_in_progress.png?w=1100&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=f5a2f9d696d101e5bddf865d6a6e6ee0 1100w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/model_response_in_progress.png?w=1650&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=fb2a7412e62c12b9df6fb670015dc838 1650w, https://mintcdn.com/thundercompute/IgIJAJ1ZHhruhHLo/images/model_response_in_progress.png?w=2500&fit=max&auto=format&n=IgIJAJ1ZHhruhHLo&q=85&s=e2ed88ea69df5336c8011433465d00c0 2500w" />

## Conclusion

That's the **cheapest way to run DeepSeek R1** and a quick way to **try DeepSeek R1** on Thunder Compute. Explore more guides:

* [Using Docker on Thunder Compute](/guides/using-docker-on-thundercompute)
* [Using Instance Templates](/guides/using-instance-templates)
* [Running Jupyter notebooks](/guides/running-jupyter-notebooks-on-thunder-compute)

Happy building!
