# Mouser API Authentication

## API Key

Mouser uses a static API key for authentication. The key is passed in the request body, not as a header.

### Obtaining an API Key

1. **Create Account**: Log into or create a [My Mouser](https://www.mouser.com/) account
2. **Request Access**: Complete the Search API Request Form at https://www.mouser.com/api-search/
3. **Receive Key**: Mouser sends your API key via email

### Using the API Key

The key is included in the JSON request body:

```json
{
  "apiKey": "YOUR_MOUSER_SEARCH_API_KEY",
  "SearchByKeywordRequest": {
    "keyword": "microcontroller"
  }
}
```

## Security Requirements

- Keep your API key secret
- Never expose keys in client-side code
- Use environment variables or secure vaults
- HTTPS is required for all API calls

## Terms of Service

You must comply with Mouser's [Search API Terms of Service](https://www.mouser.com/apiterms/), including:

- Acceptable use policies
- Attribution requirements
- Non-competitive use restrictions

## Environment Variable Example

```bash
# .env or shell config
export MOUSER_API_KEY="your-api-key-here"
```

```python
import os

api_key = os.environ.get("MOUSER_API_KEY")
```
