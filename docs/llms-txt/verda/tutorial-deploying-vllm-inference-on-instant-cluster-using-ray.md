# Source: https://docs.verda.com/clusters/instant-clusters/tutorial-deploying-vllm-inference-on-instant-cluster-using-ray.md

# Tutorial: deploying vllm inference on instant cluster using ray

If you need to run your inference on more than 8 GPUs, you can do so on our instant cluster using vllm with ray.

{% hint style="warning" %}
The vllm command and required steps might differ depending on the model you are trying to deploy
{% endhint %}

After you grab your instant cluster and ssh into the first node you need to install the environment:

```bash
apt install python3-venv
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env  # or restart shell

uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate

##create pyproject.toml and add dependencies to it
cat << EOF >> pyproject.toml
[project]
name = "vllm-ray"
version = "1.0.0"
dependencies = [
    "ray==2.52.0",
    "vllm",
]

[tool.uv.sources]
vllm = { url = "https://github.com/vllm-project/vllm/releases/download/v0.12.0/vllm-0.12.0+cu130-cp38-abi3-manylinux_2_31_x86_64.whl" }

[[tool.uv.index]]
url = "https://download.pytorch.org/whl/cu130"
EOF

uv sync --index-strategy unsafe-best-match
```

\
Then you need to download the model you want to run, remember to replace `YOUR_HF_TOKEN` with your actual huggingface token:

```bash
export HF_TOKEN=YOUR_HF_TOKEN
hf auth login --token $HF_TOKEN
hf download deepseek-ai/deepseek-llm-7b-chat # or any other model
```

After model has been downloaded, we can start ray on node 1:

```bash
export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export GLOO_SOCKET_IFNAME=eth0
ray start --head --num-gpus=8 --port=6379
```

Then on our worker nodes we also start ray, remember to replace `FIRST_NODE_IP` with actual IP of first node:

```bash
source .venv/bin/activate
ray start --address="FIRST_NODE_IP:6379" --num-gpus=8 --block
```

And then on the first node we can finally start serving with vllm, change `pipeline-parallel-size`'s value to the amount of nodes(including head node) you have available and `tensor-parallel-size` to number of GPUs per node:

```bash
source .venv/bin/activate # if not in venv already
python -m vllm.entrypoints.openai.api_server \
--model deepseek-ai/deepseek-llm-7b-chat \
--tensor-parallel-size 8 \
--pipeline-parallel-size 2 \
--distributed-executor-backend ray
```
