# calculate accuracy rate across test cases
sum(accuracy_rates) / len(accuracy_rates)
```

</details>

<details>
<summary><b> Example 2: evaluate code generation</b></summary>

### Example 2: evaluate code generation

#### Evaluation data
Our second example involves generating Python code and assessing the generated code. To conduct the evaluation, both the Python instructions and the corresponding unit tests are required for the evaluation data. Here are two examples of such evaluation data sets:

```py
python_prompts = {
    "sort_string": {
        "prompt": "Write a python function to sort the given string.", 
        "test": "assert sort_string(\"data\") == \"aadt\""
    },
    "is_odd": {
        "prompt": "Write a python function to check whether the given number is odd or not using bitwise operator.", 
        "test": "assert is_odd(5) == True"
    }
}
```

#### How to evaluate? 

- Step 1: Define prompt template

We have designed a prompt that generates Python code snippets based on descriptions of specific tasks.

```py
def run_mistral(user_message, model="mistral-large-latest"):
    client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
    messages = [{"role":"user", "content": user_message}]
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
        response_format={"type": "json_object"},
    )
    return chat_response.choices[0].message.content