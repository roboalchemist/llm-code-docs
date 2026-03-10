# Prompt for the Dappier API key securely
dappier_api_key = getpass("Enter your Dappier API key: ")
os.environ["DAPPIER_API_KEY"] = dappier_api_key
```

You can obtain your OpenAI API key from the [OpenAI API dashboard](https://platform.openai.com/account/api-keys).

```python Python theme={null}