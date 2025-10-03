# Source: https://docs.perplexity.ai/guides/api-key-management

## 
[​](https://docs.perplexity.ai/guides/api-key-management#overview)
Overview
API keys are essential for authenticating requests to the Perplexity API. This guide covers how to create, manage, and rotate your API keys using our authentication token management endpoints.
API keys should be treated as sensitive credentials. Store them securely and never expose them in client-side code or public repositories.
## 
[​](https://docs.perplexity.ai/guides/api-key-management#getting-started%3A-create-your-api-group-first)
Getting Started: Create Your API Group First
**Important Prerequisites** : Before you can generate any API keys, you must first create an API group through the Perplexity web interface.
1
Create an API Group
Navigate to the API Groups page and create your first group:**[Create API Group →](https://www.perplexity.ai/account/api/group)** API groups help organize your keys and manage access across different projects or environments.
Choose a descriptive name for your API group (e.g., “Production”, “Development”, or your project name) to help with organization.
2
Generate Your API Keys
Once you have an API group, navigate to the API Keys page to generate your first key:**[Generate API Keys →](https://www.perplexity.ai/account/api/keys)** You can create multiple keys within each group for different purposes or environments.
After creating your first API key through the web interface, you can use the programmatic endpoints below to generate and manage additional keys.
## 
[​](https://docs.perplexity.ai/guides/api-key-management#key-management-endpoints)
Key Management Endpoints
Perplexity provides two endpoints for managing API keys programmatically:
  * **`/generate_auth_token`**- Creates a new API key
  * **`/revoke_auth_token`**- Revokes an existing API key


Once an API key is revoked, it cannot be recovered. Make sure to update your applications with new keys before revoking old ones.
## 
[​](https://docs.perplexity.ai/guides/api-key-management#generating-api-keys)
Generating API Keys
Create new API keys programmatically with optional naming for better organization.
### 
[​](https://docs.perplexity.ai/guides/api-key-management#request)
Request
cURL
Python
TypeScript
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/generate_auth_token \
  --header "Authorization: Bearer YOUR_EXISTING_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "token_name": "Production API Key"
  }'

```

### 
[​](https://docs.perplexity.ai/guides/api-key-management#response)
Response
Copy
Ask AI
```
{
  "auth_token": "pplx-1234567890abcdef",
  "created_at_epoch_seconds": 1735689600,
  "token_name": "Production API Key"
}

```

Store the `auth_token` immediately and securely. This is the only time you’ll be able to see the full token value.
## 
[​](https://docs.perplexity.ai/guides/api-key-management#revoking-api-keys)
Revoking API Keys
Revoke API keys that are no longer needed or may have been compromised.
### 
[​](https://docs.perplexity.ai/guides/api-key-management#request-2)
Request
cURL
Python
TypeScript
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/revoke_auth_token \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "auth_token": "pplx-1234567890abcdef"
  }'

```

### 
[​](https://docs.perplexity.ai/guides/api-key-management#response-2)
Response
Returns a `200 OK` status code on successful revocation.
## 
[​](https://docs.perplexity.ai/guides/api-key-management#api-key-rotation)
API Key Rotation
Regular key rotation is a security best practice that minimizes the impact of potential key compromises. Here’s how to implement zero-downtime key rotation:
### 
[​](https://docs.perplexity.ai/guides/api-key-management#rotation-strategy)
Rotation Strategy
1
Generate New Key
Create a new API key while your current key is still active:
Copy
Ask AI
```
# Generate new key
new_key_response = requests.post(
    "https://api.perplexity.ai/generate_auth_token",
    headers={"Authorization": f"Bearer {current_key}"},
    json={"token_name": f"Rotated Key - {datetime.now().isoformat()}"}
)
new_key = new_key_response.json()["auth_token"]

```

2
Update Applications
Deploy the new key to your applications:
Copy
Ask AI
```
# Update environment variables or secrets management
os.environ["PERPLEXITY_API_KEY"] = new_key
# Verify new key works
test_response = requests.post(
    "https://api.perplexity.ai/chat/completions",
    headers={"Authorization": f"Bearer {new_key}"},
    json={
        "model": "sonar",
        "messages": [{"role": "user", "content": "Test"}]
    }
)
assert test_response.status_code == 200

```

3
Monitor Transition
Ensure all services are using the new key before proceeding:
Copy
Ask AI
```
# Monitor your application logs to confirm
# all instances are using the new key
time.sleep(300)  # Wait for propagation

```

4
Revoke Old Key
Once confirmed, revoke the old key:
Copy
Ask AI
```
# Revoke old key
revoke_response = requests.post(
    "https://api.perplexity.ai/revoke_auth_token",
    headers={"Authorization": f"Bearer {new_key}"},
    json={"auth_token": current_key}
)
assert revoke_response.status_code == 200
print("Key rotation completed successfully")

```

### 
[​](https://docs.perplexity.ai/guides/api-key-management#automated-rotation-example)
Automated Rotation Example
Here’s a complete example of an automated key rotation script:
Python
TypeScript
Copy
Ask AI
```
import requests
import os
import time
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class PerplexityKeyRotator:
    def __init__(self, current_key):
        self.base_url = "https://api.perplexity.ai"
        self.current_key = current_key
    def generate_new_key(self, name=None):
        """Generate a new API key"""
        url = f"{self.base_url}/generate_auth_token"
        headers = {"Authorization": f"Bearer {self.current_key}"}
        payload = {}
        if name:
            payload["token_name"] = name
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    def test_key(self, key):
        """Test if a key is valid"""
        url = f"{self.base_url}/chat/completions"
        headers = {"Authorization": f"Bearer {key}"}
        payload = {
            "model": "sonar",
            "messages": [{"role": "user", "content": "Test"}],
            "max_tokens": 1
        }
        try:
            response = requests.post(url, headers=headers, json=payload)
            return response.status_code == 200
        except:
            return False
    def revoke_key(self, key_to_revoke):
        """Revoke an API key"""
        url = f"{self.base_url}/revoke_auth_token"
        headers = {"Authorization": f"Bearer {self.current_key}"}
        payload = {"auth_token": key_to_revoke}
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    def rotate_key(self, update_callback=None):
        """Perform complete key rotation"""
        logger.info("Starting key rotation...")
        # Step 1: Generate new key
        new_key_data = self.generate_new_key(
            name=f"Rotated-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        )
        new_key = new_key_data["auth_token"]
        logger.info(f"New key generated: {new_key[:10]}...")
        # Step 2: Test new key
        if not self.test_key(new_key):
            raise Exception("New key validation failed")
        logger.info("New key validated successfully")
        # Step 3: Update application (callback)
        if update_callback:
            update_callback(new_key)
            logger.info("Application updated with new key")
        # Step 4: Wait for propagation
        logger.info("Waiting for propagation...")
        time.sleep(30)
        # Step 5: Revoke old key
        old_key = self.current_key
        self.current_key = new_key  # Use new key for revocation
        if self.revoke_key(old_key):
            logger.info("Old key revoked successfully")
        else:
            logger.warning("Failed to revoke old key")
        logger.info("Key rotation completed")
        return new_key
# Usage example
def update_environment(new_key):
    """Update your environment with the new key"""
    os.environ["PERPLEXITY_API_KEY"] = new_key
    # Update your secrets management system here
    # update_aws_secrets_manager(new_key)
    # update_kubernetes_secret(new_key)
# Perform rotation
rotator = PerplexityKeyRotator(os.environ["PERPLEXITY_API_KEY"])
new_key = rotator.rotate_key(update_callback=update_environment)
print(f"Rotation complete. New key: {new_key[:10]}...")

```

## 
[​](https://docs.perplexity.ai/guides/api-key-management#best-practices)
Best Practices
## Use Environment Variables
Never hardcode API keys in your source code. Store them in environment variables or secure secret management systems.**Good** : `os.environ["PERPLEXITY_API_KEY"]`**Bad** : `api_key = "pplx-1234567890abcdef"`
## Implement Key Rotation
Rotate your API keys regularly (e.g., every 90 days) to minimize the impact of potential compromises.Set up automated rotation scripts to ensure zero downtime during the rotation process.
## Use Descriptive Names
When generating keys, use the `token_name` parameter to identify their purpose and environment.Examples: “Production-Main”, “Development-Testing”, “CI/CD-Pipeline”
## Monitor Key Usage
Track which keys are being used in your applications and revoke unused keys promptly.Maintain an inventory of active keys and their purposes.
## 
[​](https://docs.perplexity.ai/guides/api-key-management#security-considerations)
Security Considerations
**Never expose API keys in:**
  * Client-side JavaScript code
  * Mobile applications
  * Public repositories
  * Log files or error messages
  * URLs or query parameters


### 
[​](https://docs.perplexity.ai/guides/api-key-management#if-a-key-is-compromised)
If a Key is Compromised
  1. **Immediately generate a new key** using `/generate_auth_token`
  2. **Update all applications** to use the new key
  3. **Revoke the compromised key** using `/revoke_auth_token`
  4. **Review access logs** to identify any unauthorized usage
  5. **Implement additional security measures** such as IP allowlisting if available


## 
[​](https://docs.perplexity.ai/guides/api-key-management#troubleshooting)
Troubleshooting
Issue | Solution  
---|---  
”Authentication failed” after rotation | Ensure the new key has propagated to all service instances  
Cannot revoke a key | Verify you’re using a valid API key with appropriate permissions  
Key generation fails | Check your account status and API tier limits  
Services still using old key | Implement proper secret rotation in your deployment pipeline  
For additional support with API key management, visit your [API settings page](https://www.perplexity.ai/settings/api) or contact our support team.
