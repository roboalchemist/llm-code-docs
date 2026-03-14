# Source: https://novita.ai/docs/guides/lollmswebui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LoLLMS WebUI

> Easily integrate Novita AI with LoLLMS WebUI to enhance your productivity and simplify complex tasks.

LoLLMS WebUI, a centralized platform designed for effortless interaction with Large Language Models (LLMs) and multimodal AI systems, offers an intuitive interface to unlock the full potential of AI. The integration between Novita AI and LoLLMS WebUI will unleash transformative power,enabling you to simplify complex tasks, find answers, and explore new possibilities effortlessly.

By combining Novita AI with LoLLMS, you'll gain access to cutting-edge AI capabilities, making it your ultimate assistant for enhanced productivity. This guide provides a step-by-step walkthrough to help you maximize the benefits of this powerful integration.

## How to Leverage Novita AI with LoLLMS WebUI

You can find the GitHub repository of LoLLMS WebUI here: [ParisNeo/lollms-webui](https://github.com/ParisNeo/lollms-webui).

### Obtain Your Novita AI API Key

1. [Log in](https://novita.ai/user/login) to your Novita AI account.
2. Navigate to [the Key Management page](https://novita.ai/settings/key-management).
3. Generate a new API Key and copy it.

### Install LoLLMS WebUI

1. Automatic Installation:
   * Download the installation script from [the scripts folder](https://github.com/ParisNeo/lollms-webui/tree/main/scripts) and run it:
     * `lollms_installer.bat` for Windows.
     * `lollms_installer.sh` for Linux.
     * `lollms_installer_macos.sh` for Mac.
2. Manual Installation:
   * Ensure Python 3.11 is installed. Check your version with `python --version`.
   * If needed, download Python 3.11 from [Python.org](https://www.python.org/downloads/release/python-3118/).

Step 1: Clone the Repository

```bash  theme={"system"}
git clone --recursive https://github.com/ParisNeo/lollms-webui.git
cd lollms-webui
git submodule update --init --recursive
```

Step 2: Create and Activate a Virtual Environment

* Create a Virtual Environment:

```bash  theme={"system"}
python -m venv venv
```

* Activate the Virtual Environment:
  * On Windows:

    ```bash  theme={"system"}
    .\venv\Scripts\activate
    ```
  * On Linux/Mac:

    ```bash  theme={"system"}
    source venv/bin/activate
    ```

Step 3: Install Requirements

```bash  theme={"system"}
pip install -r requirements.txt
pip install -e ./lollms_core
```

Step 4: Create global\_paths\_cfg.yaml

```bash  theme={"system"}
mkdir -p $HOME/.lollms_personal_data

cat > global_paths_cfg.yaml << EOL
lollms_path: $(pwd)/lollms_core/lollms
lollms_personal_path: $HOME/.lollms_personal_data
EOL
```

### Configure Novita AI in LoLLMS WebUI

1. Install Novita AI Binding

* Set environment variables for Novita AI binding. For example:

  * On Windows:

  ```bash  theme={"system"}
  set NOVITA_AI_API_KEY="your_api_key_here"
  set NOVITA_AI_MODEL_NAME="your_model_name_here"
  ```

  * On Linux/Mac:

  ```bash  theme={"system"}
  export NOVITA_AI_API_KEY="your_api_key_here"
  export NOVITA_AI_MODEL_NAME="your_model_name_here"
  ```
* Run the script to finalize the setup:

  ```bash  theme={"system"}
  python zoos/bindings_zoo/novita_ai/__init__.py
  ```

2. Run the Server

```bash  theme={"system"}
python app.py
```

3. Use Novita AI in LoLLMS WebUI

* Open your browser and navigate to [http://localhost:9600](http://localhost:9600) (or the port shown in the terminal).
* Select Novita AI from the available bindings.
* Enter your Novita AI API key.
* Select your desired Novita AI model.

[******Here is an application: Vibe Coding Using Novita AI Bindings and Services on LoLLMS WebUI.******](https://www.youtube.com/watch?v=jyFaP4zTM9g)


Built with [Mintlify](https://mintlify.com).