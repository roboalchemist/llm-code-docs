# Get API key for direct access
0g-compute-cli inference get-secret --provider <PROVIDER_ADDRESS>
```

Option 3 - Direct API (OpenAI Compatible):
```bash
curl <service_url>/v1/proxy/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer app-sk-<YOUR_SECRET>" \
  -d '{
    "model": "<model_name>",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

**OpenAI SDK Integration**:
```python
from openai import OpenAI

client = OpenAI(
    api_key="app-sk-<YOUR_SECRET>",
    base_url="<service_url>/v1/proxy"
)

response = client.chat.completions.create(
    model="<model_name>",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)
```

**Fine-tuning Models**:
```bash