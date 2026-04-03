# Running Hugging Face Transformers and Diffusers on an NVIDIA GH200 instance -

Source: https://docs.lambda.ai/education/running-huggingface-diffusers-transformers-gh200/

---

[on-demand cloud ](../../tags/#tag:on-demand-cloud)
# Running Hugging Face Transformers and Diffusers on an NVIDIA GH200 instance [# ](#running-hugging-face-transformers-and-diffusers-on-an-nvidia-gh200-instance)

[Hugging Face ](https://huggingface.co/)provides several powerful Python libraries that provide easy access to a wide range of pre-trained models. Among the most popular are [Diffusers ](https://huggingface.co/docs/diffusers/index), which focuses on diffusion-based generative AI, and [Transformers ](https://huggingface.co/docs/transformers/en/index), which supports common AI/ML tasks across several different modalities. This tutorial demonstrates how to use these libraries to generate images and chatbot-style responses on an On-Demand Cloud (ODC) instance backed with the NVIDIA GH200 Grace Hopper Superchip. 

## Setting up your environment [# ](#setting-up-your-environment)

### Launch your GH200 instance [# ](#launch-your-gh200-instance)

Begin by launching a GH200 instance: 

- In the Lambda Cloud console, navigate to the [SSH keys page ](https://cloud.lambda.ai/ssh-keys), click **Add SSH Key **, and then add or generate a SSH key. 
- Navigate to the [Instances page ](https://cloud.lambda.ai/instances)and click **Launch Instance **. 
- Follow the steps in the instance launch wizard. 
  - *Instance type: *Select **1x GH200 (96 GB). **
  - *Region: *Select an available region. 
  - *Filesystem: *Don't attach a filesystem. 
  - *SSH key: *Use the key you created in step 1. 
- Click **Launch instance **. 
- Review the EULAs. If you agree to them, click **I agree to the above **to start launching your new instance. Instances can take up to five minutes to fully launch. 
### Set up your Python virtual environment [# ](#set-up-your-python-virtual-environment)

Next, create a new Python virtual environment and install the required libraries: 

- In the Lambda Cloud console, navigate to the [Instances page ](https://cloud.lambda.ai/instances), find the row for your instance, and then click **Launch **in the **Cloud IDE **column. JupyterLab opens in a new window. 
- In JupyterLab's **Launcher **tab, under **Other **, click **Terminal **to open a new terminal. 
- 
In your terminal, create a Python virtual environment: 

```
`[](#__codelineno-0-1)python -m venv --system-site-packages hf-tests
`
```
