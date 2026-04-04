# Sample OpenAI chat with function calling
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What’s the latest news on electric vehicle stocks?"}],
    functions=functions,
    function_call="auto"
)
```

***

## Conclusion

With **OpenAI Function Calling** and **Dappier SDK**, developers can create **AI-powered tools and workflows** that are grounded in **real-time, accurate information**. From **financial research** to **travel automation**, this integration unlocks the full potential of **LLMs combined with live, trusted data** for building powerful, scalable AI solutions.