# make sure to install `langchain` and `langchain-mistralai` in your Python environment


from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate 

api_key = os.environ["MISTRAL_API_KEY"]
mistral_model = "codestral-latest"
llm = ChatMistralAI(model=mistral_model, temperature=0, api_key=api_key)
llm.invoke([("user", "Write a function for fibonacci")])
```

For a more complex use case of self-corrective code generation using the instruct Codestral tool use, check out this [notebook](https://github.com/mistralai/cookbook/blob/main/third_party/langchain/langgraph_code_assistant_mistral.ipynb) and this video:

<iframe width="560" height="315" width="100%" src="https://www.youtube.com/embed/zXFxmI9f06M?si=8ZEoqNVECVJQFcVA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</details>

<details>
<summary><b>Integration with LlamaIndex</b></summary>

LlamaIndex provides support for Codestral Instruct and Fill In Middle (FIM) endpoints. Here is how you can use it in LlamaIndex: 

```py