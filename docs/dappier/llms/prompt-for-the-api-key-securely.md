# Prompt for the API key securely
openai_api_key = getpass('Enter your API key: ')
os.environ["OPENAI_API_KEY"] = openai_api_key
```

You can go to [here](https://app.agentops.ai/signin) to get **free** API Key from AgentOps

```python Python theme={null}