# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/concepts/template.md

# Template

> Leverage templates in Galileo Evaluate to standardize metrics, model assessments, and workflows for efficient generative AI evaluation.

What is a Galileo template?

Galileo templates are a versioned way to manage your parameters as part of a single step [run](/galileo/gen-ai-studio-products/galileo-evaluate/concepts/run). These include the prompt, the model, and the keyword arguments to the model. As you make changes to your templates, they are automatically recognized and saved upon creating new runs with them.
![The view upon clicking on a template in a project](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/template.png)
The view upon clicking on a template in a project

When viewing a template in a [project](/galileo/gen-ai-studio-products/galileo-evaluate/concepts/project), the options are to edit the template, view template code, or tag as production template. Editing the template brings you to the Playground, where you can modify the template. Viewing template code generates an OpenAI, Langchain, or cURL command to replicate the parameters of the template.

Production templates can be fetched programmatically as the below Python example illustrates:

```py
from promptquality.helpers import get_template

template = get_template(project_id=<project-id>, template_id=<template-id>)
```
