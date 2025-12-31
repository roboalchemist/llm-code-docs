# Source: https://docs.galileo.ai/client-reference/protect/python.md

# Source: https://docs.galileo.ai/client-reference/observe/python.md

# Source: https://docs.galileo.ai/client-reference/evaluate/python.md

# Source: https://docs.galileo.ai/client-reference/protect/python.md

# Source: https://docs.galileo.ai/client-reference/observe/python.md

# Source: https://docs.galileo.ai/client-reference/evaluate/python.md

# Source: https://docs.galileo.ai/client-reference/protect/python.md

# Source: https://docs.galileo.ai/client-reference/observe/python.md

# Source: https://docs.galileo.ai/client-reference/evaluate/python.md

# Source: https://docs.galileo.ai/client-reference/protect/python.md

# Source: https://docs.galileo.ai/client-reference/observe/python.md

# Source: https://docs.galileo.ai/client-reference/evaluate/python.md

# Source: https://docs.galileo.ai/client-reference/protect/python.md

# Source: https://docs.galileo.ai/client-reference/observe/python.md

# Source: https://docs.galileo.ai/client-reference/evaluate/python.md

# Python Client Reference | Galileo Evaluate

> Integrate Galileo's Evaluate module into your Python applications with this guide, featuring installation steps and examples for prompt quality assessment.

<Tip>
  For a full reference of promptquality check out: <a href="https://promptquality.docs.rungalileo.io/">[https://promptquality.docs.rungalileo.io/](https://promptquality.docs.rungalileo.io/)</a>
</Tip>

## Installation

`pip install promptquality`

## Evaluate

```py
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
