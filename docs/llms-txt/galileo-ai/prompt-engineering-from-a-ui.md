# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/quickstart/prompt-engineering-from-a-ui.md

# Prompt Engineering From A UI

> Explore UI-driven prompt engineering in Galileo Evaluate to create, test, and refine prompts with intuitive interfaces and robust evaluation tools.

Quickstart for how to try different templates, models or models settings for an individual LLM call from the Galileo UI.

Looking to prompt engineer individual calls to an LLM? Prompt Runs are your answer.

A *Prompt Run* is a quick and easy way to test a model + template + model settings combination for your use case. In order to create a prompt run, you'll need:

* An Evaluation Set - a list of user queries / inputs that you want to run your evaluation over

* A template / model combination you'd like to try.

If you already have an application or prototype you're looking to Evaluate, Prompt Runs are **not** for you. Instead, we recommend [integrating Evaluate into your existing application](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart/integrate-evaluate-into-my-existing-application-with-python).

## Creating a Prompt Run via the Playground UI

1. Login to the Galileo console

2. Create a **New Project** via the "+" button.

   1. Give your project a **Name**, or choose Galileo's proposed name

   2. Select "**Evaluate**"

   3. Click on **Create Project**

This will take you to the Galileo Playground. Next, we choose a template, model and hyperparemeter settings

### Choosing a Template, Model, and Tune Hyperparameters

1. Choose an LLM, and adjust hyperparameters settings. For **custom or self-hosted LLMs**, follow the section [Setting Up Your Custom LLMs](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/llms).

2. Give your template a name, or select a **pre-defined template**

3. Enter a **Prompt**. Put variables in curly braces e.g. `{topic}`

4. **Add Data**: There are 2 ways to add data

   1. Upload a CSV - with the first row representing *variable names* and each following row representing the *values*

   2. Manually add data by clicking on "**+ Add data**"

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/gen-ai.png" />
</Frame>

### Choosing Your Guardrail Metrics

Galileo offers a comprehensive selection of **Guardrail Metrics** for monitoring your LLM (Large Language Model) App in production. These metrics are meticulously chosen based on your specific use case, ensuring effective evaluation of your prompts and models. Our Guardrail Metrics encompass:

* **Industry-Standard Metrics:** These include well-known metrics such as BLEU (Bilingual Evaluation Understudy), ROUGE-1 (Recall-Oriented Understudy for Gisting Evaluation), and Perplexity.

* **Metrics from Galileo's ML Research Team:** Developed through rigorous research, our team has introduced innovative metrics like Uncertainty, Correctness, and Context Adherence. These metrics are designed to evaluate the reliability and authenticity of the generated content, ensuring it meets high standards of safety, accuracy, and relevance.

For detailed information on each metric and how they can be utilized to monitor your LLM App effectively in a production environment, refer to our [**List of Metrics**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) available through Galileo's platform.

<iframe src="https://cdn.iframe.ly/waFgcr9" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

Video Walkthrough of how to get started with Galileo Evaluate

The same workflow can also be executed with the Python client, check out Prompt Engineering with Galileo Evaluate [here](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-prompts).
