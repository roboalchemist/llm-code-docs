# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-prompts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluate and Optimize Prompts

> How to use Galileo Evaluate for prompt engineering

Galileo Evaluate enables you to evaluate and optimize your prompts with out-of-the-box Guardrail metrics.

1. **Pip Install** `promptquality` and create runs in your Python notebook.

2. Next, you execute **promptquality.run()** like shown below.

```Bash  theme={null}

    import promptquality as pq

    pq.login({YOUR_GALILEO_URL})

    template = "Explain {{topic}} to me like I'm a 5 year old"

    data = {"topic": ["Quantum Physics", "Politics", "Large Language Models"]}

    pq.run(project_name='my_first_project',
           template=template,
           dataset=data,
           settings=pq.Settings(model_alias='ChatGPT (16K context)',
                                temperature=0.8,
                                max_tokens=400))
```

<Info>
  The code snippet above uses ChatGPT API endpoint from OpenAI. Want to use other models (Azure OpenAI, Cohere, Anthropic, Mistral, etc)? Check out the integration page
  [here](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/llms).
</Info>
