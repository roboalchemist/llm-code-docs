# Virtual environments and Docker containers -

Source: https://docs.lambda.ai/education/programming/virtual-environments-containers/

---

[Virtualization ](../../../tags/#tag:virtualization)
# Virtual environments and Docker containers [# ](#virtual-environments-and-docker-containers)

## What are virtual environments? [# ](#what-are-virtual-environments)

Virtual environments allow you to create and maintain development environments that are isolated from each other. Lambda recommends using either: 

- [Python venv ](#creating-a-python-virtual-environment)
- [conda ](#creating-a-conda-virtual-environment)
### Creating a Python virtual environment [# ](#creating-a-python-virtual-environment)

- 
Create a Python virtual environment using the `venv`module by running: 

```
`[](#__codelineno-0-1)python -m venv --system-site-packages NAME
`
```
