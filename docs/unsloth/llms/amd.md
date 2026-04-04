# Source: https://unsloth.ai/docs/fr/commencer/install/amd.md

# Source: https://unsloth.ai/docs/de/loslegen/install/amd.md

# Source: https://unsloth.ai/docs/jp/hajimeni/install/amd.md

# Source: https://unsloth.ai/docs/zh/kai-shi-shi-yong/install/amd.md

# Source: https://unsloth.ai/docs/get-started/install/amd.md

# Fine-tuning LLMs on AMD GPUs with Unsloth Guide

You can now fine-tune LLMs on your own local AMD setup with Unsloth. Unsloth supports AMD Radeon RX, MI300X's (192GB) GPUs and more.

{% stepper %}
{% step %}
**Make a new isolated environment (Optional)**

To not break any system packages, you can make an isolated pip environment. Reminder to check what Python version you have! It might be `pip3`, `pip3.13`, `python3`, `python.3.13` etc.

{% code overflow="wrap" %}

```bash
apt install python3.10-venv python3.11-venv python3.12-venv python3.13-venv -y

python -m venv unsloth_env
source unsloth_env/bin/activate
```

{% endcode %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FCqOhjYTr4GqQ90ToPEig%2Famd1.png?alt=media&#x26;token=d8f96a07-90be-4d93-b848-ad182c262d1f" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Install PyTorch**

Install the latest PyTorch, TorchAO, Xformers from <https://pytorch.org/> Check your ROCM version via `amd-smi version` then change `https://download.pytorch.org/whl/rocm7.0` to match it.

{% code overflow="wrap" %}

```bash
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm7.0 --upgrade --force-reinstall
```

{% endcode %}

We also wrote a single terminal command to extract the correct ROCM version if it helps.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FJ1VZQ9QhzWFizDceg3ye%2Famd2.png?alt=media&#x26;token=937d1eba-3c7e-4c73-b6a6-9a9450d0e4ac" alt=""><figcaption></figcaption></figure>

```bash
ROCM_TAG="$({ command -v amd-smi >/dev/null 2>&1 && amd-smi version 2>/dev/null | awk -F'ROCm version: ' 'NF>1{split($2,a,"."); print "rocm"a[1]"."a[2]; ok=1; exit} END{exit !ok}'; } || { [ -r /opt/rocm/.info/version ] && awk -F. '{print "rocm"$1"."$2; exit}' /opt/rocm/.info/version; } || { command -v hipconfig >/dev/null 2>&1 && hipconfig --version 2>/dev/null | awk -F': *' '/HIP version/{split($2,a,"."); print "rocm"a[1]"."a[2]; ok=1; exit} END{exit !ok}'; } || { command -v dpkg-query >/dev/null 2>&1 && ver="$(dpkg-query -W -f="${Version}\n" rocm-core 2>/dev/null)" && [ -n "$ver" ] && awk -F'[.-]' '{print "rocm"$1"."$2; exit}' <<<"$ver"; } || { command -v rpm >/dev/null 2>&1 && ver="$(rpm -q --qf '%{VERSION}\n' rocm-core 2>/dev/null)" && [ -n "$ver" ] && awk -F'[.-]' '{print "rocm"$1"."$2; exit}' <<<"$ver"; })"; [ -n "$ROCM_TAG" ] && uv pip install torch torchvision torchaudio --index-url "https://download.pytorch.org/whl/$ROCM_TAG" --upgrade --force-reinstall
```

{% endstep %}

{% step %}
**Install Unsloth**

Install Unsloth's dedicated AMD branch:

{% code overflow="wrap" %}

```bash
pip install --no-deps unsloth unsloth-zoo
pip install --no-deps git+https://github.com/unslothai/unsloth-zoo.git
pip install "unsloth[amd] @ git+https://github.com/unslothai/unsloth"
```

{% endcode %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Frz8GOvVgST7beQ8pmgmC%2Famd3.png?alt=media&#x26;token=03a12c20-af1d-4b98-9aaf-18ccc6a1d4a4" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Start fine-tuning with Unsloth!**

And that's it. Try some examples in our [**Unsloth Notebooks**](https://unsloth.ai/docs/get-started/unsloth-notebooks) page!

You can view our dedicated [fine-tuning](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide) or [reinforcement learning](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) guides.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FlDpKitaEagbh0Er8wJFC%2Famd4.png?alt=media&#x26;token=f54448fe-0719-464f-bbd1-d73f82aedfc0" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### :1234: Reinforcement Learning on AMD GPUs

You can use our :ledger:[gpt-oss RL auto win 2048](https://github.com/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_Reinforcement_Learning_2048_Game_BF16.ipynb) example on a MI300X (192GB) GPU. The goal is to play the 2048 game automatically and win it with RL. The LLM (gpt-oss 20b) auto devises a strategy to win the 2048 game, and we calculate a high reward for winning strategies, and low rewards for failing strategies.

{% columns %}
{% column %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-2bc5a2e25a51781fd945ab9e87e73821ed4eb6c9%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
The reward over time is increasing after around 300 steps or so!

The goal for RL is to maximize the average reward to win the 2048 game.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-8d7ea897fd57156a796e4f74aa2e3b60afe9d405%2F2048%20Auto%20Win%20Game%20Reward.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

We used an AMD MI300X machine (192GB) to run the 2048 RL example with Unsloth, and it worked well!

<div><figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-174890aa5f63632ebe6f3f212f1ced0d0e8dc381%2FScreenshot%202025-10-17%20052504.png?alt=media" alt=""><figcaption></figcaption></figure> <figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-f907ba596705496515fdfb39b49d649697317ca7%2FScreenshot%202025-10-17%20052641.png?alt=media" alt=""><figcaption></figcaption></figure></div>

You can also use our :ledger:[automatic kernel gen RL notebook](https://github.com/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_GRPO_BF16.ipynb) also with gpt-oss to auto create matrix multiplication kernels in Python. The notebook also devices multiple methods to counteract reward hacking.

{% columns %}
{% column width="50%" %}
The prompt we used to auto create these kernels was:

{% code overflow="wrap" %}

````
Create a new fast matrix multiplication function using only native Python code.
You are given a list of list of numbers.
Output your new function in backticks using the format below:
```
python
def matmul(A, B):
    return ...
```
````

{% endcode %}
{% endcolumn %}

{% column width="50%" %}
The RL process learns for example how to apply the Strassen algorithm for faster matrix multiplication inside of Python.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-ddb993e5d2c986794ede1f2b0d08897469b78506%2Fimage%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?alt=media" alt="" width="375"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

### :books:AMD Free One-click notebooks

AMD provides one-click notebooks equipped with **free 192GB VRAM MI300X GPUs** through their Dev Cloud. Train large models completely for free (no signup or credit card required):

* [Qwen3 (32B)](https://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Qwen3_\(32B\)_A100-Reasoning-Conversational.ipynb)
* [Llama 3.3 (70B)](https://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Llama3.3_\(70B\)_A100-Conversational.ipynb)
* [Qwen3 (14B)](http://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb)
* [Mistral v0.3 (7B)](http://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-Alpaca.ipynb)
* [GPT OSS MXFP4 (20B)](http://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Kaggle-GPT_OSS_MXFP4_\(20B\)-Inference.ipynb) - Inference
* Reinforcement Learning notebook:

{% embed url="<https://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/gpt_oss_(20B)_Reinforcement_Learning_2048_Game_BF16.ipynb>" %}

You can use any Unsloth notebook by prepending ***<https://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb>*** in [unsloth-notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks "mention") by changing the link from <https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_(270M).ipynb> to <https://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Gemma3_(270M).ipynb>

{% columns %}
{% column width="33.33333333333333%" %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F7NNi4jLKvmZoRnLel9Kg%2Fimage.png?alt=media&#x26;token=0379eda9-569c-4614-afb5-ffec463a7676" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column width="66.66666666666667%" %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FRfKS1GAW7BqL9lGNTcxh%2Fimage.png?alt=media&#x26;token=3a8aeb01-62a7-4d55-89a9-98526052e305" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}
