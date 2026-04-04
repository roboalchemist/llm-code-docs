# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/prompt-management-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompt Management-Storage

> Manage and store your AI prompts efficiently in Galileo Evaluate, with tools for organizing, versioning, and analyzing prompt performance at scale.

Galileo Prompt also includes a production-ready Prompt Store that can store various versions of your Prompt Templates. Prompt Templates are associated with your project to help organize them into a single place.

Prompt templates can be created from the Galileo Console or the `promptquality` Python client and are available for experiments or production workflows through either interaction mechanisms.

## Prompt Versioning

In the video below, you see an example of a summarization template, and how Galileo helps auto-track the changes made to the template via internal versioning.

<iframe src="https://cdn.iframe.ly/f47hplq" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

## Prompt Management

As you experiment with and evolve your prompt, newer versions of your template are created automatically. Prompt Versions are auto-incrementing integers. We also provide a simple way to version new prompts as you edit the template in the Galileo Console.

<iframe src="https://cdn.iframe.ly/QbSHEmE" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

Selecting or Retrieving Prompts

## Mark Version as 'Selected'

Once you've experimented with a few different prompt templates and have evaluated them, you can mark one version as the 'Selected' version. This can be done from the UI, by using the dropdown next to the template name:

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/m-s.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7fd0e36b3fc1463cd8e97ce081e125cb" alt="Mark Version as 'Selected'" data-og-width="800" width="800" data-og-height="254" height="254" data-path="images/m-s.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/m-s.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=e01eff91e89f2b6c77020a2562504362 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/m-s.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=5e3f8d40e494f70939d836098ebcbab6 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/m-s.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d44d3460698b5bbff2a1738c041d8b03 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/m-s.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7d7139932ef137d1ea86318a4c0ca6fe 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/m-s.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=b354514d3b3e915ebe9fa77b9fc1b2d5 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/m-s.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=5cb37694675f729a3dd58a8e706ab708 2500w" />

or from the Python client:

```Bash  theme={null}

from promptquality.helpers import select_template_version

select_template_version(version=<version-number>, project_id=<project-id>, template_id=<template-id>)
```

## Fetch 'Selected' Prompt

If you want to use this template version outside the experimentation setting, you can do so by fetching the prompt using the `promptquality` Python client.

```Bash  theme={null}

from promptquality.helpers import get_template

template = get_template(project_id=<project-id>, template_id=<template-id>)
```

The returned `template` will be of type [`BaseTemplateResponse`](https://docs.rungalileo.io/galileo/python-clients/index/promptquality.types#pydantic-model-basetemplateresponse), which includes the 'Selected' versions text in the `template` attribute.
