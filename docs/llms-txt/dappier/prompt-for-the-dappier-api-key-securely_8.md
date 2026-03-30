# Prompt for the Dappier API key securely
dappier_api_key = getpass('Enter your API key: ')
os.environ["DAPPIER_API_KEY"] = dappier_api_key
```

You can go to [here](https://platform.openai.com/settings/organization/api-keys) to get API Key from Open AI.

```python Python theme={null}