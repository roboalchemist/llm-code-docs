# Fine-tuning the Mochi video generation model on GH200 -

Source: https://docs.lambda.ai/education/fine-tune-mochi-gh200/

---

[generative ai](../../tags/#tag:generative-ai)[on-demand cloud](../../tags/#tag:on-demand-cloud)

# Fine-tuning the Mochi video generation model on GH200 [#](#fine-tuning-the-mochi-video-generation-model-on-gh200)

This guide helps you get started fine-tuning [Genmo's Mochi video generation model](https://www.genmo.ai/)using a [Lambda On-Demand Cloud](https://lambda.ai/service/gpu-cloud)GH200 instance.

## Launch your GH200 instance [#](#launch-your-gh200-instance)

Begin by launching a GH200 instance:

- In the Lambda Cloud console, navigate to the [SSH keys page](https://cloud.lambda.ai/ssh-keys), click **Add SSH Key **, and then add or generate a SSH key.
- Navigate to the [Instances page](https://cloud.lambda.ai/instances)and click **Launch Instance **.
- Follow the steps in the instance launch wizard.
  - *Instance type: *Select **1x GH200 (96 GB). **
  - *Region: *Select an available region.
  - *Filesystem: *Don't attach a filesystem.
  - *SSH key: *Use the key you created in step 1.
- Click **Launch instance **.
- Review the EULAs. If you agree to them, click **I agree to the above **to start launching your new instance. Instances can take up to five minutes to fully launch.

## Install dependencies [#](#install-dependencies)

-
Install the dependencies needed for this guide by running:

```bash
`[](#__codelineno-0-1)git clone https://github.com/genmoai/mochi.git
[](#__codelineno-0-2)cd mochi-tune
[](#__codelineno-0-3)pip install --upgrade pip setuptools wheel packaging
[](#__codelineno-0-4)pip install -e . --no-build-isolation
[](#__codelineno-0-5)pip install moviepy==1.0.3 pillow==9.5.0 av==13.1.0
[](#__codelineno-0-6)sudo apt -y install bc
`

```
