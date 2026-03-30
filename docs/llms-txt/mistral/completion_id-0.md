#                  'completion_id': 0})]}))
```

- Step 3: Calculate accuracy rate across test cases 

Now, we can go through all test cases, create a user message based on the prompt template, use the LLM to produce Python code, and evaluate the generated code for each test case. 

```py
refs = []
preds = []

for name in python_prompts:

    # define user message
    user_message = prompt_template.format(
        task=python_prompts[name]["prompt"], name=name
    )

    # run LLM
    response = run_mistral(user_message)

    refs.append(python_prompts[name]["test"])
    preds.append([response])