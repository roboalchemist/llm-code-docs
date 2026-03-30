# Prompt for the Open AI API key securely
openai_api_key = getpass('Enter your API key: ')
os.environ["OPENAI_API_KEY"] = openai_api_key
```

Your can go to [here](https://smith.langchain.com/o/dfdd86ea-11a8-5cda-aa11-d998a680bfce/settings) to get API Key from LangSmith.

```python Python theme={null}