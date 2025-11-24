# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/prompt-management-storage.md

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

![Mark Version as 'Selected'](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/m-s.png)

or from the Python client:

```Bash

from promptquality.helpers import select_template_version

select_template_version(version=<version-number>, project_id=<project-id>, template_id=<template-id>)
```

## Fetch 'Selected' Prompt

If you want to use this template version outside the experimentation setting, you can do so by fetching the prompt using the `promptquality` Python client.

```Bash

from promptquality.helpers import get_template

template = get_template(project_id=<project-id>, template_id=<template-id>)
```

The returned `template` will be of type [`BaseTemplateResponse`](https://docs.rungalileo.io/galileo/python-clients/index/promptquality.types#pydantic-model-basetemplateresponse), which includes the 'Selected' versions text in the `template` attribute.
