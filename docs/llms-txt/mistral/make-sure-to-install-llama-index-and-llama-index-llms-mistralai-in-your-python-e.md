# make sure to install `llama-index` and `llama-index-llms-mistralai` in your Python enviornment


from llama_index.core.llms import ChatMessage
from llama_index.llms.mistralai import MistralAI

api_key =  os.environ["MISTRAL_API_KEY"]
mistral_model = "codestral-latest"
messages = [
    ChatMessage(role="user", content="Write a function for fibonacci"),
]
MistralAI(api_key=api_key, model=mistral_model).chat(messages)
```
Check out more details on using Instruct and Fill In Middle(FIM) with LlamaIndex in this [notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/codestral.ipynb).

</details>

<details>
<summary><b>Integration with Jupyter AI</b></summary>

Jupyter AI seamlessly integrates Codestral into JupyterLab, offering users a streamlined and enhanced AI-assisted coding experience within the Jupyter ecosystem. This integration boosts productivity and optimizes users' overall interaction with Jupyter. 

To get started using Codestral and Jupyter AI in JupyterLab, first install needed packages in your Python environment:
```bash
pip install jupyterlab langchain-mistralai jupyter-ai pandas matplotlib
```

Then launch Jupyter Lab: 
```bash
jupyter lab
```

Afterwards, you can select Codestral as your model of choice, input your Mistral API key, and start coding with Codestral!

<iframe width="560" height="315" width="100%" src="https://www.youtube.com/embed/jNUSTZwlq9M?si=plx_V19ZakgrniHy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</details>

<details>
<summary><b>Integration with JupyterLite</b></summary>

JupyterLite is a project that aims to bring the JupyterLab environment to the web browser, allowing users to run Jupyter directly in their browser without the need for a local installation.

You can try Codestral with JupyterLite in your browser:
[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://jupyterlite.github.io/ai/lab/index.html)

<iframe width="560" height="315" width="100%" src="https://www.youtube.com/embed/edKyZSWy-Fw?si=pBzFV40vckyuCl6w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</details>

<details>
<summary><b>Integration with Tabby</b></summary>

Tabby is an open-source AI coding assistant. You can use Codestral for both code completion and chat via Tabby. 

To use Codestral in Tabby, configure your model configuration in `~/.tabby/config.toml` as follows.

```bash
[model.completion.http]
kind = "mistral/completion"
api_endpoint = "https://api.mistral.ai"
api_key = "secret-api-key"
```

You can check out [Tabby's documentation](https://tabby.tabbyml.com/docs/administration/model/#mistral--codestral) to learn more.  

<iframe width="560" height="315" width="100%" src="https://www.youtube.com/embed/ufHbMyC0oGA?si=kKlH8L3EtECMdtV7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</details>

<details>
<summary><b>Integration with E2B</b></summary>

E2B provides open-source secure sandboxes for AI-generated code execution. 
With E2B, it is easy for developers to add code interpreting capabilities to AI apps using Codestral.

In the following examples, the AI agent performs a data analysis task on an uploaded CSV file, executes the AI-generated code by Codestral in the sandboxed environment by E2B, and returns a chart, saving it as a PNG file.

Python implementation ([cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/E2B_Code_Interpreting/codestral-code-interpreter-python)): 
<iframe width="560" height="315" width="100%" src="https://www.youtube.com/embed/26Wd-kC35Og?si=FgamyNZdzW--6iR7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

JS implementation ([cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/E2B_Code_Interpreting/codestral-code-interpreter-js)):
<iframe width="560" height="315" width="100%" src="https://www.youtube.com/embed/3M1_79U9RZE?si=YlTWN2chAxUhxHfr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</details>

### Devstral Integrations

<details>
<summary><b>Integration with Open Hands</b></summary>

OpenHands is an open-source scaffolding tool designed for building AI agents focused on software development. It offers a comprehensive framework for creating and managing these agents that can modify code, run commands, browse the web, call APIs, and even copy code snippets from StackOverflow.

<iframe width="560" height="315" width="100%" src="https://www.youtube.com/embed/oV9tAkS2Xic?si=gERKTfB-hFsSzk7f" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

After creating a Mistral AI account, you can use the following commands to start the OpenHands Docker container:

```bash


mkdir -p ~/.openhands && echo '{"language":"en","agent":"CodeActAgent","max_iterations":null,"security_analyzer":null,"confirmation_mode":false,"llm_model":"mistral/devstral-small-2507","llm_api_key":"'$MISTRAL_API_KEY'","remote_runtime_resource_factor":null,"github_token":null,"enable_default_condenser":true}' > ~/.openhands-state/settings.json

docker pull docker.all-hands.dev/all-hands-ai/runtime:0.48-nikolaik

docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.48-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands:/.openhands \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.48
```

For more information visit the [OpenHands github repo](https://github.com/All-Hands-AI/OpenHands) and their [documentation](https://docs.all-hands.dev/usage/llms/local-llms).

</details>

<details>
<summary><b>Integration with Cline</b></summary>

Cline is an autonomous coding agent operating right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way. 

<video width="100%" controls>
  <source src="/video/clinevideo.mov" type="video/mp4"/>
</video>

For more information visit the [Cline github repo](https://github.com/cline/cline).

</details>


[Annotations]
Source: https://docs.mistral.ai/docs/capabilities/document_ai/annotations