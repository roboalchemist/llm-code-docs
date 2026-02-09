# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/concepts/template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Template

> Leverage templates in Galileo Evaluate to standardize metrics, model assessments, and workflows for efficient generative AI evaluation.

What is a Galileo template?

Galileo templates are a versioned way to manage your parameters as part of a single step [run](/galileo/gen-ai-studio-products/galileo-evaluate/concepts/run). These include the prompt, the model, and the keyword arguments to the model. As you make changes to your templates, they are automatically recognized and saved upon creating new runs with them.
<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/template.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=18a6400f05f97fbab293efdc3b8cd133" alt="The view upon clicking on a template in a project" data-og-width="425" width="425" data-og-height="210" height="210" data-path="images/template.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/template.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=5f28dc1f4b553c34937408f062293c8c 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/template.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1356e5e2eb2e3c6830fd762882873313 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/template.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=879f5bd323671a7c9e7d763c8ea74769 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/template.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=a7a89f68dfc712fbbca37b9d698d10cb 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/template.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=92d592d7f18f10f429a9268a3b8ae737 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/template.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=4cd4869da7e88e54acadd199cb8664ee 2500w" />
The view upon clicking on a template in a project

When viewing a template in a [project](/galileo/gen-ai-studio-products/galileo-evaluate/concepts/project), the options are to edit the template, view template code, or tag as production template. Editing the template brings you to the Playground, where you can modify the template. Viewing template code generates an OpenAI, Langchain, or cURL command to replicate the parameters of the template.

Production templates can be fetched programmatically as the below Python example illustrates:

```py  theme={null}
from promptquality.helpers import get_template

template = get_template(project_id=<project-id>, template_id=<template-id>)
```
