# Installation and Setup

**Source:** https://github.com/OpenBMB/AgentVerse

## Installation

AgentVerse requires **Python 3.9 or higher**.

### Option 1: Manual Installation (Recommended)

Clone the repository and install in development mode:

```bash
git clone https://github.com/OpenBMB/AgentVerse.git --depth 1
cd AgentVerse
pip install -e .
```

### Option 2: Install via pip

Install the latest version from PyPI:

```bash
pip install -U agentverse
```

### Optional: Local Model Support

To use AgentVerse with local models such as LLaMA and Vicunna, install additional dependencies:

```bash
pip install -r requirements_local.txt
```

## Environment Variables

### OpenAI API Configuration

Set up your OpenAI API key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

### Azure OpenAI Configuration

For Azure OpenAI services, export both your API key and base URL:

```bash
export AZURE_OPENAI_API_KEY="your_api_key_here"
export AZURE_OPENAI_API_BASE="your_api_base_here"
```

### vLLM Support

To use vLLM for larger inference workloads, set up the vLLM server first by following the [vLLM installation guide](https://docs.vllm.ai/en/latest/getting_started/quickstart.html).

Then configure the following environment variables:

```bash
export VLLM_API_KEY="your_api_key_here"
export VLLM_API_BASE="http://your_vllm_url_here"
```

## Framework-Specific Module Requirements

### Simulation Framework

The simulation framework requires:

```
- agentverse
  - agents
    - simulation_agent
  - environments
    - simulation_env
```

### Task-Solving Framework

The task-solving framework requires:

```
- agentverse
  - agents
    - simulation_agent
  - environments
    - tasksolving_env
```

## Tools Integration

### BMTools Installation

If you want to run simulation cases with tools (e.g., `simulation/nlp_classroom_3players_withtool`), install BMTools:

```bash
git clone https://github.com/OpenBMB/BMTools.git
cd BMTools
pip install -r requirements.txt
python setup.py develop
```

This is optional. Simulation cases without tools will run normally without BMTools installed.

### XAgent ToolsServer

For tool-using task-solving cases (multi-agent systems using web browser, Jupyter notebook, Bing search, etc.), build the ToolsServer from [XAgent](https://github.com/OpenBMB/XAgent).

Follow the [XAgent setup instructions](https://github.com/OpenBMB/XAgent#%EF%B8%8F-build-and-setup-toolserver) to build and run the ToolServer.

## Local Model Configuration

### FSChat Integration

For local models like LLaMA and Vicunna via FastChat:

#### 1. Install Additional Dependencies

```bash
pip install -r requirements_local.txt
```

#### 2. Launch Local Model Server

Modify the `MODEL_PATH` and `MODEL_NAME` variables according to your needs, then run:

```bash
bash scripts/run_local_model_server.sh
```

This launches a service for Llama 7B chat model by default.

#### Supported Models

The `MODEL_NAME` in AgentVerse currently supports:
- `llama-2-7b-chat-hf`
- `llama-2-13b-chat-hf`
- `llama-2-70b-chat-hf`
- `vicuna-7b-v1.5`
- `vicuna-13b-v1.5`

For additional [FastChat-compatible models](https://github.com/lm-sys/FastChat/blob/main/docs/model_support.md), you need to:

1. Add the `MODEL_NAME` to `LOCAL_LLMS` in `agentverse/llms/__init__.py`
2. Add the mapping from `MODEL_NAME` to its Hugging Face identifier in `LOCAL_LLMS_MAPPING` in `agentverse/llms/__init__.py`

#### 3. Configure Your Config File

Set the `llm_type` to `local` and `model` to the `MODEL_NAME`:

```yaml
llm:
  llm_type: local
  model: llama-2-7b-chat-hf
  ...
```

Refer to `agentverse/tasks/tasksolving/commongen/llama-2-7b-chat-hf/config.yaml` for a complete example.

## Verification

After installation, verify everything works by running a simple example:

```bash
# For simulation
agentverse-simulation --task simulation/nlp_classroom_3players

# For task-solving
agentverse-tasksolving --task tasksolving/brainstorming
```
