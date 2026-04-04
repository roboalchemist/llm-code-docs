# Source: https://docs.mage.ai/development/dependencies/custom-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Import your own Python code

> You can import any Python code from any file that is in your Mage project directory.

<p align="center">
  <img alt="Python mecha" src="https://mage-ai.github.io/assets/development/python-2.png" width="250" />
</p>

## Importing custom Python code

When you’re writing code in Mage, you can import any other Python files using this format:

```python  theme={"system"}
from [project_name].foo import bar
```

For example, if your project name is `demo_project` and you have the following folder structure:

```
demo_project/
|   pipelines/
|   utils/
|   |   helpers/
|   |   |   shared.py
|   |   |   __init__.py
|   |   __init__.py
```

You can write the following import statement to use functions in the
`demo_project/utils/helpers/shared.py` file:

```python  theme={"system"}
from demo_project.utils.helpers import shared
```


Built with [Mintlify](https://mintlify.com).