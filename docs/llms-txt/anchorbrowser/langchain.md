# Source: https://docs.anchorbrowser.io/agent-frameworks/langchain.md

# LangChain

AI agents can leverage browser sessions to complete tasks on the web using LangChain, a framework that provides easy integration for AI-driven workflows.

Anchor provides [LangChain tools](https://python.langchain.com/docs/integrations/tools/anchor_browser/) that allows you to use Anchor Browser as a tool in your LangChain workflows.
The package contains the following tools:

* `AnchorContentTool`: Get the content of a web page in markdown format.
* `AnchorScreenshotTool`: Take a screenshot of a web page.
* `AnchorWebTaskTools`: Perform intelligent web tasks using AI:
  * Simple - `SimpleAnchorWebTaskTool`
  * Advanced - `AdvancedAnchorWebTaskTool`

See Anchor Browser package for LangChain on [PyPi](https://pypi.org/project/langchain-anchorbrowser/) for more information.

## Quickstart

### Installation

Install the `langchain-anchorbrowser` package:

```bash  theme={null}
pip install langchain-anchorbrowser
```

### Usage

Import and utilize your intended tool. The full list of Anchor Browser available tools see **Tool Features** table in [Anchor Browser tool page](/docs/integrations/tools/anchor_browser)

```python  theme={null}
from langchain_anchorbrowser import AnchorContentTool

# Get Markdown Content for https://www.anchorbrowser.io
AnchorContentTool().invoke(
    {"url": "https://www.anchorbrowser.io", "format": "markdown"}
)
```

## Additional Resources

* [PyPi](https://pypi.org/project/langchain-anchorbrowser)
* [Github](https://github.com/anchorbrowser/langchain-anchorbrowser)
* [Anchor Browser Docs on LangChain](https://python.langchain.com/docs/integrations/tools/anchor_browser/)
