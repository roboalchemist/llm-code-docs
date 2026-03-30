# Source: https://github.com/h2oai/h2o-llmstudio

Title: GitHub - h2oai/h2o-llmstudio: H2O LLM Studio - a framework and no-code GUI for fine-tuning LLMs. Documentation: https://docs.h2o.ai/h2o-llmstudio/

URL Source: https://github.com/h2oai/h2o-llmstudio

Markdown Content:
[![Image 1](https://github.com/h2oai/h2o-llmstudio/raw/main/llm_studio/app_utils/static/llm-studio-logo-light.png#gh-dark-mode-only)](https://github.com/h2oai/h2o-llmstudio/blob/main/llm_studio/app_utils/static/llm-studio-logo-light.png#gh-dark-mode-only)

[![Image 2](https://github.com/h2oai/h2o-llmstudio/raw/main/llm_studio/app_utils/static/llm-studio-logo.png#gh-light-mode-only)](https://github.com/h2oai/h2o-llmstudio/blob/main/llm_studio/app_utils/static/llm-studio-logo.png#gh-light-mode-only)

### Welcome to H2O LLM Studio, a framework and no-code GUI designed for

 fine-tuning state-of-the-art large language models (LLMs).

[](https://github.com/h2oai/h2o-llmstudio#----welcome-to-h2o-llm-studio-a-framework-and-no-code-gui-designed-for----fine-tuning-state-of-the-art-large-language-models-llms)

[![Image 3: home](https://user-images.githubusercontent.com/1069138/233859311-32aa1f8c-4d68-47ac-8cd9-9313171ff9f9.png)](https://user-images.githubusercontent.com/1069138/233859311-32aa1f8c-4d68-47ac-8cd9-9313171ff9f9.png)[![Image 4: logs](https://user-images.githubusercontent.com/1069138/233859315-e6928aa7-28d2-420b-8366-bc7323c368ca.png)](https://user-images.githubusercontent.com/1069138/233859315-e6928aa7-28d2-420b-8366-bc7323c368ca.png)

Jump to
-------

[](https://github.com/h2oai/h2o-llmstudio#jump-to)
*   [With H2O LLM Studio, you can](https://github.com/h2oai/h2o-llmstudio#with-h2o-llm-studio-you-can)
*   [Quickstart](https://github.com/h2oai/h2o-llmstudio#quickstart)
*   [What's New](https://github.com/h2oai/h2o-llmstudio#whats-new)
*   [Setup](https://github.com/h2oai/h2o-llmstudio#setup)
    *   [Recommended Install](https://github.com/h2oai/h2o-llmstudio#recommended-install)
    *   [Virtual Environments](https://github.com/h2oai/h2o-llmstudio#virtual-environments)

*   [Run H2O LLM Studio GUI](https://github.com/h2oai/h2o-llmstudio#run-h2o-llm-studio-gui)
*   [Run H2O LLM Studio GUI using Docker](https://github.com/h2oai/h2o-llmstudio#run-h2o-llm-studio-gui-using-docker)
*   [Run H2O LLM Studio with command line interface (CLI)](https://github.com/h2oai/h2o-llmstudio#run-h2o-llm-studio-with-command-line-interface-cli)
*   [Troubleshooting](https://github.com/h2oai/h2o-llmstudio#troubleshooting)
*   [Data format and example data](https://github.com/h2oai/h2o-llmstudio#data-format-and-example-data)
*   [Training your model](https://github.com/h2oai/h2o-llmstudio#training-your-model)
*   [Example: Run on OASST data via CLI](https://github.com/h2oai/h2o-llmstudio#example-run-on-oasst-data-via-cli)
*   [Model checkpoints](https://github.com/h2oai/h2o-llmstudio#model-checkpoints)
*   [Documentation](https://github.com/h2oai/h2o-llmstudio#documentation)
*   [Contributing](https://github.com/h2oai/h2o-llmstudio#contributing)
*   [License](https://github.com/h2oai/h2o-llmstudio#license)

With H2O LLM Studio, you can
----------------------------

[](https://github.com/h2oai/h2o-llmstudio#with-h2o-llm-studio-you-can)
*   easily and effectively fine-tune LLMs **without the need for any coding experience**.
*   use a **graphical user interface (GUI)** specially designed for large language models.
*   fine-tune any LLM using a large variety of hyperparameters.
*   use recent fine-tuning techniques such as [Low-Rank Adaptation (LoRA)](https://arxiv.org/abs/2106.09685) and 8-bit model training with a low memory footprint.
*   use Reinforcement Learning (RL) to fine-tune your model (experimental).
*   use advanced evaluation metrics to judge generated answers by the model.
*   track and compare your model performance visually. In addition, [Neptune](https://neptune.ai/) and [W&B](https://wandb.ai/) integration can be used.
*   chat with your model and get instant feedback on your model performance.
*   easily export your model to the [Hugging Face Hub](https://huggingface.co/) and share it with the community.

Quickstart
----------

[](https://github.com/h2oai/h2o-llmstudio#quickstart)
For questions, discussing, or just hanging out, come and join our [Discord](https://discord.gg/WKhYMWcVbq)!

Use cloud-based runpod.io instance to run the latest version of H2O LLM Studio with GUI.

[![Image 5: open_in_runpod](https://private-user-images.githubusercontent.com/1069138/358587931-0dffd945-0be0-4ef0-85cd-4e6f260d4e6c.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzMzNDk0MTMsIm5iZiI6MTc3MzM0OTExMywicGF0aCI6Ii8xMDY5MTM4LzM1ODU4NzkzMS0wZGZmZDk0NS0wYmUwLTRlZjAtODVjZC00ZTZmMjYwZDRlNmMucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDMxMiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAzMTJUMjA1ODMzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MGVmNTI4NmJiM2U2ZWVhMzFkOGE0ODRkODdiMDkzZjE4NTQwZTA5YjY5NmQ5MmE1ODU4Mjc2NTU4MmExNmVhMSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.cvQat6t1dMCd6EiFxPxVB1df9KQj7evUcROdSZrxrWA)](https://www.runpod.io/console/deploy?template=vf9ppiy56z)

Using CLI for fine-tuning LLMs:

[![Image 6: Kaggle](https://camo.githubusercontent.com/eadc2c97204abec941106030dd80d31e167037bd2c3d12de91c6301b69e77e8d/68747470733a2f2f6b6167676c652e636f6d2f7374617469632f696d616765732f6f70656e2d696e2d6b6167676c652e737667)](https://www.kaggle.com/code/ilu000/h2o-llm-studio-cli/)[![Image 7: Open in Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1soqfJjwDJwjjH-VzZYO_pUeLx5xY4N1K?usp=sharing)

What's New
----------

[](https://github.com/h2oai/h2o-llmstudio#whats-new)
*   [PR 788](https://github.com/h2oai/h2o-llmstudio/pull/788) New problem type for Causal Regression Modeling allows to train single target regression data using LLMs.
*   [PR 747](https://github.com/h2oai/h2o-llmstudio/pull/747) Fully removed RLHF in favor of DPO/IPO/KTO optimization.
*   [PR 741](https://github.com/h2oai/h2o-llmstudio/pull/741) Removing separate max length settings for prompt and answer in favor of a single `max_length` settings better resembling `chat_template` functionality from `transformers`.
*   [PR 592](https://github.com/h2oai/h2o-llmstudio/pull/599) Added `KTOPairLoss` for DPO modeling allowing to train models with simple preference data. Data currently needs to be manually prepared by randomly matching positive and negative examples as pairs.
*   [PR 592](https://github.com/h2oai/h2o-llmstudio/pull/592) Starting to deprecate RLHF in favor of DPO/IPO optimization. Training is disabled, but old experiments are still viewable. RLHF will be fully removed in a future release.
*   [PR 530](https://github.com/h2oai/h2o-llmstudio/pull/530) Introduced a new problem type for DPO/IPO optimization. This optimization technique can be used as an alternative to RLHF.
*   [PR 288](https://github.com/h2oai/h2o-llmstudio/pull/288) Introduced DeepSpeed for sharded training allowing to train larger models on machines with multiple GPUs. Requires NVLink. This feature replaces FSDP and offers more flexibility. DeepSpeed requires a system installation of CUDA Toolkit and we recommend using version 12.1. See [Recommended Install](https://github.com/h2oai/h2o-llmstudio#recommended-install).
*   [PR 449](https://github.com/h2oai/h2o-llmstudio/pull/449) New problem type for Causal Classification Modeling allows to train binary and multiclass models using LLMs.
*   [PR 364](https://github.com/h2oai/h2o-llmstudio/pull/364) User secrets are now handled more securely and flexible. Support for handling secrets using the 'keyring' library was added. User settings are tried to be migrated automatically.

Please note that due to current rapid development we cannot guarantee full backwards compatibility of new functionality. We thus recommend to pin the version of the framework to the one you used for your experiments. For resetting, please delete/backup your `data` and `output` folders.

Setup
-----

[](https://github.com/h2oai/h2o-llmstudio#setup)
H2O LLM Studio requires a machine with Ubuntu 16.04+ and at least one recent NVIDIA GPU with NVIDIA drivers version >= 470.57.02. For larger models, we recommend at least 24GB of GPU memory.

For more information about installation prerequisites, see the [Set up H2O LLM Studio](https://docs.h2o.ai/h2o-llmstudio/get-started/set-up-llm-studio#prerequisites) guide in the documentation.

For a performance comparison of different GPUs, see the [H2O LLM Studio performance](https://h2oai.github.io/h2o-llmstudio/get-started/llm-studio-performance) guide in the documentation.

### Recommended Install

[](https://github.com/h2oai/h2o-llmstudio#recommended-install)
The recommended way to install H2O LLM Studio is using `uv` with Python 3.10. To install Python 3.10 on Ubuntu 20.04+, execute the following commands:

#### Installing NVIDIA Drivers (if required)

[](https://github.com/h2oai/h2o-llmstudio#installing-nvidia-drivers-if-required)
If deploying on a 'bare metal' machine running Ubuntu, one may need to install the required NVIDIA drivers and CUDA. The following commands show how to retrieve the latest drivers for a machine running Ubuntu 20.04 as an example. One can update the following based on their OS.

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.4.0/local_installers/cuda-repo-ubuntu2204-12-4-local_12.4.0-550.54.14-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-12-4-local_12.4.0-550.54.14-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-4-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-4

### Virtual environments

[](https://github.com/h2oai/h2o-llmstudio#virtual-environments)
We offer various ways of setting up the necessary python environment.

#### UV virtual environment

[](https://github.com/h2oai/h2o-llmstudio#uv-virtual-environment)
The following command will create a virtual environment using `uv` and will install the dependencies:

make setup

#### Using requirements.txt

[](https://github.com/h2oai/h2o-llmstudio#using-requirementstxt)
If you wish to use another virtual environment, you can also install the dependencies using the requirements.txt file:

pip install -r requirements.txt
pip install flash-attn==2.8.3 --no-build-isolation  # optional for Flash Attention 2

You can start H2O LLM Studio using the following command:

make llmstudio

This command will start the [H2O Wave](https://github.com/h2oai/wave) server and app. Navigate to [http://localhost:10101/](http://localhost:10101/) (we recommend using Chrome) to access H2O LLM Studio and start fine-tuning your models!

If you are running H2O LLM Studio with a custom environment other than `uv`, you need to start the app as follows:

H2O_WAVE_MAX_REQUEST_SIZE=25MB \
H2O_WAVE_NO_LOG=true \
H2O_WAVE_PRIVATE_DIR="/download/@output/download" \
wave run llm_studio.app

Run H2O LLM Studio GUI using Docker
-----------------------------------

[](https://github.com/h2oai/h2o-llmstudio#run-h2o-llm-studio-gui-using-docker)
Install Docker first by following instructions from [NVIDIA Containers](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker). Make sure to have `nvidia-container-toolkit` installed on your machine as outlined in the instructions.

H2O LLM Studio images are stored in the h2oai Docker Hub container repository.

mkdir -p `pwd`/llmstudio_mnt
chmod 777 `pwd`/llmstudio_mnt

# make sure to pull latest image if you still have a prior version cached
docker pull h2oairelease/h2oai-llmstudio-app:latest

# run the container
docker run \
    --runtime=nvidia \
    --shm-size=64g \
    --init \
    --rm \
    -it \
    -u `id -u`:`id -g` \
    -p 10101:10101 \
    -v `pwd`/llmstudio_mnt:/mount \
    h2oairelease/h2oai-llmstudio-app:latest

Navigate to [http://localhost:10101/](http://localhost:10101/) (we recommend using Chrome) to access H2O LLM Studio and start fine-tuning your models!

(Note other helpful docker commands are `docker ps` and `docker kill`.)

Run H2O LLM Studio with command line interface (CLI)
----------------------------------------------------

[](https://github.com/h2oai/h2o-llmstudio#run-h2o-llm-studio-with-command-line-interface-cli)
You can also use H2O LLM Studio with the command line interface (CLI) and specify the configuration .yaml file that contains all the experiment parameters. To fine-tune using H2O LLM Studio with CLI use the following command:

uv run python llm_studio/train.py -Y {path_to_config_yaml_file}

To run on multiple GPUs in DDP mode, run the following command:

bash distributed_train.sh {NR_OF_GPUS} -Y {path_to_config_yaml_file}

By default, the framework will run on the first `k` GPUs. If you want to specify specific GPUs to run on, use the `CUDA_VISIBLE_DEVICES` environment variable before the command.

To start an interactive chat with your trained model, use the following command:

uv run python llm_studio/prompt.py -e {experiment_name}

where `experiment_name` is the output folder of the experiment you want to chat with (see configuration). The interactive chat will also work with model that were fine-tuned using the UI.

To publish the model to Hugging Face, use the following command:

uv run python llm_studio/publish_to_hugging_face.py -p {path_to_experiment} -d {device} -a {api_key} -u {user_id} -m {model_name} -s {safe_serialization}

`path_to_experiment` is the output folder of the experiment. `device` is the target device for running the model, either 'cpu' or 'cuda:0'. Default is 'cuda:0'. `api_key` is the Hugging Face API Key. If the user is logged in, it can be omitted. `user_id` is the Hugging Face user ID. If the user is logged in, it can be omitted. `model_name` is the name of the model to be published on Hugging Face. It can be omitted. `safe_serialization` is a flag indicating whether safe serialization should be used. Default is True.

Troubleshooting
---------------

[](https://github.com/h2oai/h2o-llmstudio#troubleshooting)
If running on cloud-based machines such as runpod, you may need to set the following environment variable to allow the H2O Wave server to accept connections from the proxy:

H2O_WAVE_ALLOWED_ORIGINS="*"

If you are experiencing timeouts when running the H2O Wave server remotely, you can increase the timeout by setting the following environment variables:

H2O_WAVE_APP_CONNECT_TIMEOUT="15"
H2O_WAVE_APP_WRITE_TIMEOUT="15"
H2O_WAVE_APP_READ_TIMEOUT="15"
H2O_WAVE_APP_POOL_TIMEOUT="15"

All default to 5 (seconds). Increase them if you are experiencing timeouts. Use -1 to disable the timeout.

Data format and example data
----------------------------

[](https://github.com/h2oai/h2o-llmstudio#data-format-and-example-data)
For details on the data format required when importing your data or example data that you can use to try out H2O LLM Studio, see [Data format](https://docs.h2o.ai/h2o-llmstudio/guide/datasets/data-connectors-format#data-format) in the H2O LLM Studio documentation.

Training your model
-------------------

[](https://github.com/h2oai/h2o-llmstudio#training-your-model)
With H2O LLM Studio, training your large language model is easy and intuitive. First, upload your dataset and then start training your model. Start by [creating an experiment](https://docs.h2o.ai/h2o-llmstudio/guide/experiments/create-an-experiment). You can then [monitor and manage your experiment](https://docs.h2o.ai/h2o-llmstudio/guide/experiments/view-an-experiment), [compare experiments](https://docs.h2o.ai/h2o-llmstudio/guide/experiments/compare-experiments), or [push the model to Hugging Face](https://docs.h2o.ai/h2o-llmstudio/guide/experiments/export-trained-model) to share it with the community.

Example: Run on OASST data via CLI
----------------------------------

[](https://github.com/h2oai/h2o-llmstudio#example-run-on-oasst-data-via-cli)
As an example, you can run an experiment on the OASST data via CLI. For instructions, see [Run an experiment on the OASST data](https://docs.h2o.ai/h2o-llmstudio/guide/experiments/create-an-experiment#run-an-experiment-on-the-oasst-data-via-cli) guide in the H2O LLM Studio documentation.

Model checkpoints
-----------------

[](https://github.com/h2oai/h2o-llmstudio#model-checkpoints)
All open-source datasets and models are posted on [H2O.ai's Hugging Face page](https://huggingface.co/h2oai/) and our [H2OGPT](https://github.com/h2oai/h2ogpt) repository.

Documentation
-------------

[](https://github.com/h2oai/h2o-llmstudio#documentation)
Detailed documentation and frequently asked questions (FAQs) for H2O LLM Studio can be found at [https://docs.h2o.ai/h2o-llmstudio/](https://docs.h2o.ai/h2o-llmstudio/). If you wish to contribute to the docs, navigate to the `/documentation` folder of this repo and refer to the [README.md](https://github.com/h2oai/h2o-llmstudio/blob/main/documentation/README.md) for more information.

Contributing
------------

[](https://github.com/h2oai/h2o-llmstudio#contributing)
We are happy to accept contributions to the H2O LLM Studio project. Please refer to the [CONTRIBUTING.md](https://github.com/h2oai/h2o-llmstudio/blob/main/CONTRIBUTING.md) file for more information.

License
-------

[](https://github.com/h2oai/h2o-llmstudio#license)
H2O LLM Studio is licensed under the Apache 2.0 license. Please see the [LICENSE](https://github.com/h2oai/h2o-llmstudio/blob/main/LICENSE) file for more information.
