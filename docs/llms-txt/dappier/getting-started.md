# Getting Started

## Installation

To install the `langchain-dappier` package, run:

```bash  theme={null}
pip install langchain-dappier
```

## Setting API Credentials

Generate an API key from the [Dappier platform](https://platform.dappier.com/profile/api-keys) and set it as an environment variable:

```python Python theme={null}
import os
import getpass

if not os.environ.get("DAPPIER_API_KEY"):
    os.environ["DAPPIER_API_KEY"] = getpass.getpass("Dappier API key:")
```

For LangSmith tracing, set your API key:

```python Python theme={null}