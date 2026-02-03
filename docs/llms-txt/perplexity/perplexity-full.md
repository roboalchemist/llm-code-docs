# Perplexity Documentation

Source: https://docs.perplexity.ai/llms-full.txt

---

# Get Async Chat Completion
Source: https://docs.perplexity.ai/api-reference/async-chat-completions-api-request-get

get /async/chat/completions/{api_request}
Retrieve the response for a given asynchronous chat completion request.



# List Async Chat Completions
Source: https://docs.perplexity.ai/api-reference/async-chat-completions-get

get /async/chat/completions
Retrieve a list of all asynchronous chat completion requests for a given user.



# Create Async Chat Completion
Source: https://docs.perplexity.ai/api-reference/async-chat-completions-post

post /async/chat/completions
Submit an asynchronous chat completion request.



# Create Chat Completion
Source: https://docs.perplexity.ai/api-reference/chat-completions-post

post /chat/completions
Generate a chat completion response for the given conversation.



# Generate Auth Token
Source: https://docs.perplexity.ai/api-reference/generate-auth-token-post

post /generate_auth_token
Generates a new authentication token for API access.



# Create Response
Source: https://docs.perplexity.ai/api-reference/responses-post

post /v1/responses
Generate a response for the provided input with optional web search and reasoning.



# Revoke Auth Token
Source: https://docs.perplexity.ai/api-reference/revoke-auth-token-post

post /revoke_auth_token
Revokes an existing authentication token.



# Search the Web
Source: https://docs.perplexity.ai/api-reference/search-post

post /search
Search the web and retrieve relevant web page contents.



# API Key Management
Source: https://docs.perplexity.ai/docs/admin/api-key-management

Learn how to generate, revoke, and rotate API keys for secure access

## Overview

API keys are essential for authenticating requests to the Perplexity API. This guide covers how to create, manage, and rotate your API keys using our authentication token management endpoints.

<Info>
  API keys should be treated as sensitive credentials. Store them securely and never expose them in client-side code or public repositories.
</Info>

## Getting Started: Create Your API Group First

<Warning>
  **Important Prerequisites**: Before you can generate any API keys, you must first create an API group through the Perplexity web interface.
</Warning>

<Steps>
  <Step title="Create an API Group">
    Navigate to the API Groups page and create your first group:

    **[Create API Group →](https://www.perplexity.ai/account/api/group)**

    API groups help organize your keys and manage access across different projects or environments.

    <Tip>
      Choose a descriptive name for your API group (e.g., "Production", "Development", or your project name) to help with organization.
    </Tip>
  </Step>

  <Step title="Generate Your API Keys">
    Once you have an API group, navigate to the API Keys page to generate your first key:

    **[Generate API Keys →](https://www.perplexity.ai/account/api/keys)**

    You can create multiple keys within each group for different purposes or environments.
  </Step>
</Steps>

<Note>
  After creating your first API key through the web interface, you can use the programmatic endpoints below to generate and manage additional keys.
</Note>

## Key Management Endpoints

Perplexity provides two endpoints for managing API keys programmatically:

* **`/generate_auth_token`** - Creates a new API key
* **`/revoke_auth_token`** - Revokes an existing API key

<Warning>
  Once an API key is revoked, it cannot be recovered. Make sure to update your applications with new keys before revoking old ones.
</Warning>

## Generating API Keys

Create new API keys programmatically with optional naming for better organization.

### Request

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/generate_auth_token \
    --header "Authorization: Bearer YOUR_EXISTING_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "token_name": "Production API Key"
    }'
  ```

  ```python Python theme={null}
  import requests

  url = "https://api.perplexity.ai/generate_auth_token"
  headers = {
      "Authorization": "Bearer YOUR_EXISTING_API_KEY",
      "Content-Type": "application/json"
  }
  payload = {
      "token_name": "Production API Key"  # Optional
  }

  response = requests.post(url, headers=headers, json=payload)
  data = response.json()
  print(f"New API Key: {data['auth_token']}")
  print(f"Created at: {data['created_at_epoch_seconds']}")
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch("https://api.perplexity.ai/generate_auth_token", {
    method: "POST",
    headers: {
      "Authorization": "Bearer YOUR_EXISTING_API_KEY",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      token_name: "Production API Key"  // Optional
    })
  });

  const data = await response.json();
  console.log(`New API Key: ${data.auth_token}`);
  console.log(`Created at: ${data.created_at_epoch_seconds}`);
  ```
</CodeGroup>

### Response

```json theme={null}
{
  "auth_token": "pplx-1234567890abcdef",
  "created_at_epoch_seconds": 1735689600,
  "token_name": "Production API Key"
}
```

<Note>
  Store the `auth_token` immediately and securely. This is the only time you'll be able to see the full token value.
</Note>

## Revoking API Keys

Revoke API keys that are no longer needed or may have been compromised.

### Request

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/revoke_auth_token \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "auth_token": "pplx-1234567890abcdef"
    }'
  ```

  ```python Python theme={null}
  import requests

  url = "https://api.perplexity.ai/revoke_auth_token"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  payload = {
      "auth_token": "pplx-1234567890abcdef"
  }

  response = requests.post(url, headers=headers, json=payload)
  if response.status_code == 200:
      print("API key successfully revoked")
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch("https://api.perplexity.ai/revoke_auth_token", {
    method: "POST",
    headers: {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      auth_token: "pplx-1234567890abcdef"
    })
  });

  if (response.status === 200) {
    console.log("API key successfully revoked");
  }
  ```
</CodeGroup>

### Response

Returns a `200 OK` status code on successful revocation.

## API Key Rotation

Regular key rotation is a security best practice that minimizes the impact of potential key compromises. Here's how to implement zero-downtime key rotation:

### Rotation Strategy

<Steps>
  <Step title="Generate New Key">
    Create a new API key while your current key is still active:

    ```python theme={null}
    # Generate new key
    new_key_response = requests.post(
        "https://api.perplexity.ai/generate_auth_token",
        headers={"Authorization": f"Bearer {current_key}"},
        json={"token_name": f"Rotated Key - {datetime.now().isoformat()}"}
    )
    new_key = new_key_response.json()["auth_token"]
    ```
  </Step>

  <Step title="Update Applications">
    Deploy the new key to your applications:

    ```python theme={null}
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
  </Step>

  <Step title="Monitor Transition">
    Ensure all services are using the new key before proceeding:

    ```python theme={null}
    # Monitor your application logs to confirm
    # all instances are using the new key
    time.sleep(300)  # Wait for propagation
    ```
  </Step>

  <Step title="Revoke Old Key">
    Once confirmed, revoke the old key:

    ```python theme={null}
    # Revoke old key
    revoke_response = requests.post(
        "https://api.perplexity.ai/revoke_auth_token",
        headers={"Authorization": f"Bearer {new_key}"},
        json={"auth_token": current_key}
    )
    assert revoke_response.status_code == 200
    print("Key rotation completed successfully")
    ```
  </Step>
</Steps>

### Automated Rotation Example

Here's a complete example of an automated key rotation script:

<CodeGroup>
  ```python Python theme={null}
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

  ```typescript TypeScript theme={null}
  import fetch from 'node-fetch';

  class PerplexityKeyRotator {
    private baseUrl = 'https://api.perplexity.ai';
    private currentKey: string;

    constructor(currentKey: string) {
      this.currentKey = currentKey;
    }

    async generateNewKey(name?: string): Promise<{
      auth_token: string;
      created_at_epoch_seconds: number;
      token_name?: string;
    }> {
      const response = await fetch(`${this.baseUrl}/generate_auth_token`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.currentKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(name ? { token_name: name } : {})
      });

      if (!response.ok) {
        throw new Error(`Failed to generate key: ${response.statusText}`);
      }

      return response.json();
    }

    async testKey(key: string): Promise<boolean> {
      try {
        const response = await fetch(`${this.baseUrl}/chat/completions`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${key}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            model: 'sonar',
            messages: [{ role: 'user', content: 'Test' }],
            max_tokens: 1
          })
        });

        return response.ok;
      } catch {
        return false;
      }
    }

    async revokeKey(keyToRevoke: string): Promise<boolean> {
      const response = await fetch(`${this.baseUrl}/revoke_auth_token`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.currentKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ auth_token: keyToRevoke })
      });

      return response.ok;
    }

    async rotateKey(updateCallback?: (newKey: string) => Promise<void>): Promise<string> {
      console.log('Starting key rotation...');

      // Step 1: Generate new key
      const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
      const newKeyData = await this.generateNewKey(`Rotated-${timestamp}`);
      const newKey = newKeyData.auth_token;
      console.log(`New key generated: ${newKey.substring(0, 10)}...`);

      // Step 2: Test new key
      if (!(await this.testKey(newKey))) {
        throw new Error('New key validation failed');
      }
      console.log('New key validated successfully');

      // Step 3: Update application
      if (updateCallback) {
        await updateCallback(newKey);
        console.log('Application updated with new key');
      }

      // Step 4: Wait for propagation
      console.log('Waiting for propagation...');
      await new Promise(resolve => setTimeout(resolve, 30000));

      // Step 5: Revoke old key
      const oldKey = this.currentKey;
      this.currentKey = newKey;

      if (await this.revokeKey(oldKey)) {
        console.log('Old key revoked successfully');
      } else {
        console.warn('Failed to revoke old key');
      }

      console.log('Key rotation completed');
      return newKey;
    }
  }

  // Usage example
  async function updateEnvironment(newKey: string): Promise<void> {
    process.env.PERPLEXITY_API_KEY = newKey;
    // Update your secrets management system here
    // await updateAwsSecretsManager(newKey);
    // await updateKubernetesSecret(newKey);
  }

  // Perform rotation
  const rotator = new PerplexityKeyRotator(process.env.PERPLEXITY_API_KEY!);
  const newKey = await rotator.rotateKey(updateEnvironment);
  console.log(`Rotation complete. New key: ${newKey.substring(0, 10)}...`);
  ```
</CodeGroup>

## Best Practices

<CardGroup>
  <Card title="Use Environment Variables">
    Never hardcode API keys in your source code. Store them in environment variables or secure secret management systems.

    **Good**: `os.environ["PERPLEXITY_API_KEY"]`

    **Bad**: `api_key = "pplx-1234567890abcdef"`
  </Card>

  <Card title="Implement Key Rotation">
    Rotate your API keys regularly (e.g., every 90 days) to minimize the impact of potential compromises.

    Set up automated rotation scripts to ensure zero downtime during the rotation process.
  </Card>

  <Card title="Use Descriptive Names">
    When generating keys, use the `token_name` parameter to identify their purpose and environment.

    Examples: "Production-Main", "Development-Testing", "CI/CD-Pipeline"
  </Card>

  <Card title="Monitor Key Usage">
    Track which keys are being used in your applications and revoke unused keys promptly.

    Maintain an inventory of active keys and their purposes.
  </Card>
</CardGroup>

## Security Considerations

<Warning>
  **Never expose API keys in:**

  * Client-side JavaScript code
  * Mobile applications
  * Public repositories
  * Log files or error messages
  * URLs or query parameters
</Warning>

### If a Key is Compromised

1. **Immediately generate a new key** using `/generate_auth_token`
2. **Update all applications** to use the new key
3. **Revoke the compromised key** using `/revoke_auth_token`
4. **Review access logs** to identify any unauthorized usage
5. **Implement additional security measures** such as IP allowlisting if available

## Troubleshooting

| Issue                                  | Solution                                                         |
| -------------------------------------- | ---------------------------------------------------------------- |
| "Authentication failed" after rotation | Ensure the new key has propagated to all service instances       |
| Cannot revoke a key                    | Verify you're using a valid API key with appropriate permissions |
| Key generation fails                   | Check your account status and API tier limits                    |
| Services still using old key           | Implement proper secret rotation in your deployment pipeline     |

<Info>
  For additional support with API key management, visit your [API settings page](https://www.perplexity.ai/settings/api) or contact our support team.
</Info>


# Rate Limits & Usage Tiers
Source: https://docs.perplexity.ai/docs/admin/rate-limits-usage-tiers



## What are Usage Tiers?

Usage tiers determine your **rate limits** and access to **beta features** based on your cumulative API spending. As you spend more on API credits over time, you automatically advance to higher tiers with increased rate limits.

<Info>
  You can check your current usage tier by visiting your [API settings page](https://www.perplexity.ai/settings/api).
</Info>

***

## Tier Progression

| Tier       | Total Credits Purchased | Status                       |
| ---------- | ----------------------- | ---------------------------- |
| **Tier 0** | \$0                     | New accounts, limited access |
| **Tier 1** | \$50+                   | Light usage, basic limits    |
| **Tier 2** | \$250+                  | Regular usage                |
| **Tier 3** | \$500+                  | Heavy usage                  |
| **Tier 4** | \$1,000+                | Production usage             |
| **Tier 5** | \$5,000+                | Enterprise usage             |

<Note>
  Tiers are based on **cumulative purchases** across your account lifetime, not current balance.
</Note>

***

## How Tiers Work

* **Automatic advancement** - Tiers increase based on your total lifetime credit purchases
* **Rate limit increases** - Higher tiers get significantly more requests per minute
* **Permanent status** - Once you reach a tier, you keep it (no downgrade)

## Rate Limits by Model

<Tabs>
  <Tab title="Tier 0">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 5                         |
    | `sonar-reasoning-pro`                      | 50                        |
    | `sonar-pro`                                | 50                        |
    | `sonar`                                    | 50                        |
    | POST `/async/chat/completions`             | 5                         |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 1">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 10                        |
    | `sonar-reasoning-pro`                      | 150                       |
    | `sonar-pro`                                | 150                       |
    | `sonar`                                    | 150                       |
    | POST `/async/chat/completions`             | 10                        |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 2">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 20                        |
    | `sonar-reasoning-pro`                      | 500                       |
    | `sonar-pro`                                | 500                       |
    | `sonar`                                    | 500                       |
    | POST `/async/chat/completions`             | 20                        |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 3">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 40                        |
    | `sonar-reasoning-pro`                      | 1,000                     |
    | `sonar-pro`                                | 1,000                     |
    | `sonar`                                    | 1,000                     |
    | POST `/async/chat/completions`             | 40                        |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 4">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 60                        |
    | `sonar-reasoning-pro`                      | 4,000                     |
    | `sonar-pro`                                | 4,000                     |
    | `sonar`                                    | 4,000                     |
    | POST `/async/chat/completions`             | 60                        |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 5">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 100                       |
    | `sonar-reasoning-pro`                      | 4,000                     |
    | `sonar-pro`                                | 4,000                     |
    | `sonar`                                    | 4,000                     |
    | POST `/async/chat/completions`             | 100                       |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>
</Tabs>

***

## Chat Completions API Rate Limits

The Chat Completions API uses tier-based rate limits that scale with your usage tier:

|    Tier    | QPS (Queries per Second) | Requests per Minute |
| :--------: | :----------------------: | :-----------------: |
| **Tier 0** |           1 QPS          |        50/min       |
| **Tier 1** |           3 QPS          |       150/min       |
| **Tier 2** |           8 QPS          |       500/min       |
| **Tier 3** |          17 QPS          |      1,000/min      |
| **Tier 4** |          33 QPS          |      2,000/min      |
| **Tier 5** |          33 QPS          |      2,000/min      |
| **Tier 6** |          167 QPS         |      10,000/min     |

***

## Agentic Research API Rate Limits

The Agentic Research API uses tier-based rate limits that scale with your usage tier:

|    Tier    | QPS (Queries per Second) | Requests per Minute |
| :--------: | :----------------------: | :-----------------: |
| **Tier 0** |           1 QPS          |        50/min       |
| **Tier 1** |           3 QPS          |       150/min       |
| **Tier 2** |           8 QPS          |       500/min       |
| **Tier 3** |          17 QPS          |      1,000/min      |
| **Tier 4** |          33 QPS          |      2,000/min      |
| **Tier 5** |          33 QPS          |      2,000/min      |
| **Tier 6** |          167 QPS         |      10,000/min     |

***

## Search API Rate Limits

The Search API has separate rate limits that apply to all usage tiers:

| Endpoint       | Rate Limit             | Burst Capacity |
| -------------- | ---------------------- | -------------- |
| POST `/search` | 50 requests per second | 50 requests    |

**Search Rate Limiter Behavior:**

* **Burst**: Can handle 50 requests instantly
* **Sustained**: Exactly 50 QPS average over time

<Note>
  Search rate limits are independent of your usage tier and apply consistently across all accounts using the same leaky bucket algorithm.
</Note>

<Info>
  **Need Higher Search Rate Limits?**

  If you require increased rate limits for the Search API beyond the standard 50 requests per second, please fill out our [rate limit increase request form](https://perplexity.typeform.com/to/yctmfyVT). We'll review your use case and work with you to accommodate your needs.
</Info>

***

## How Rate Limiting Works

Our rate limiting system uses a **leaky bucket algorithm** that allows for burst traffic while maintaining strict long-term rate control.

### Technical Implementation

<AccordionGroup>
  <Accordion title="Leaky Bucket Algorithm Explained">
    The leaky bucket algorithm works like a bucket with a small hole in the bottom:

    * **Bucket Capacity**: Maximum number of requests you can make instantly (burst capacity)
    * **Leak Rate**: How quickly tokens refill over time (your rate limit)
    * **Token Refill**: New requests become available at regular intervals

    **Key Benefits:**

    * ✅ Allows legitimate burst traffic
    * ✅ Prevents sustained abuse
    * ✅ Predictable and fair rate enforcement
  </Accordion>

  <Accordion title="Rate Limiter Behavior Example">
    Let's examine how **50 requests per second** works in practice:

    **Parameters:**

    * Capacity: 50 tokens
    * Leak rate: 50 tokens/second
    * Refill: 1 token every 20ms

    **Scenario 1: Burst Traffic**

    ```
    Time 0.0s: Bucket full (50 tokens)
    → Send 50 requests instantly → ALL ALLOWED ✅
    → Send 51st request → REJECTED ❌ (bucket empty)

    Time 0.020s: 1 token refilled
    → Send 1 request → ALLOWED ✅
    → Send 2nd request → REJECTED ❌

    Time 0.040s: 1 more token refilled
    → Send 1 request → ALLOWED ✅
    ```

    **Scenario 2: Steady 50 QPS**

    ```
    Request every 20ms:
    Time 0.0s: Request → ✅ (50→49 tokens)
    Time 0.020s: Request → ✅ (49+1-1=49 tokens)
    Time 0.040s: Request → ✅ (49+1-1=49 tokens)
    ... maintains 49-50 tokens, all requests pass
    ```

    **Scenario 3: Slightly Over 50 QPS**

    ```
    Request every 19ms (≈52.6 QPS):
    → Eventually tokens deplete faster than refill
    → Some requests start getting rejected
    → Achieves exactly 50 QPS on average
    ```
  </Accordion>

  <Accordion title="Real-World Implications">
    **What this means for your applications:**

    **✅ Burst Tolerance:**

    * Can handle your full rate limit instantly
    * Perfect for batch operations or sudden traffic spikes
    * No need to artificially spread requests

    **✅ Predictable Behavior:**

    * Strict average rate enforcement over time
    * Quick recovery after burst usage
    * Consistent performance across different usage patterns

    **❌ Abuse Prevention:**

    * Prevents sustained over-limit usage
    * Blocks excessive burst attempts
    * Maintains fair resource allocation

    **Best Practices:**

    * Take advantage of burst capacity for batch operations
    * Monitor your usage patterns to optimize request timing
    * Implement proper error handling for 429 responses
  </Accordion>
</AccordionGroup>

***

## What Happens When You Hit Rate Limits?

When you exceed your rate limits:

1. **429 Error** - Your request gets rejected with "Too Many Requests"
2. **Continuous Refill** - Tokens refill continuously based on your rate limit
3. **Immediate Recovery** - New requests become available as soon as tokens refill

**Example Recovery Times:**

* **50 QPS limit**: 1 token refills every 20ms
* **500 QPS limit**: 1 token refills every 2ms
* **1,000 QPS limit**: 1 token refills every 1ms

<Tip>
  **Best Practices:**

  * Monitor your usage to predict when you'll need higher tiers
  * Consider upgrading your tier proactively for production applications
  * Implement exponential backoff with jitter in your code
  * Take advantage of burst capacity for batch operations
  * Don't artificially spread requests if you have available burst capacity
</Tip>

***

## Upgrading Your Tier

<Steps>
  <Step title="Check Current Tier">
    Visit your [API settings page](https://www.perplexity.ai/settings/api) to see your current tier and total spending.
  </Step>

  <Step title="Purchase More Credits">
    Add credits to your account through the billing section. Your tier will automatically upgrade once you reach the spending threshold.
  </Step>

  <Step title="Verify Upgrade">
    Your new rate limits take effect immediately after the tier upgrade. Check your settings page to confirm.
  </Step>
</Steps>

<Check>
  Higher tiers significantly improve your API experience with increased rate limits, especially important for production applications.
</Check>


# Memory Management
Source: https://docs.perplexity.ai/docs/cookbook/articles/memory-management/README

Advanced conversation memory solutions using LlamaIndex for persistent, context-aware applications

# Memory Management with LlamaIndex and Perplexity Sonar API

## Overview

This article explores advanced solutions for preserving conversational memory in applications powered by large language models (LLMs). The goal is to enable coherent multi-turn conversations by retaining context across interactions, even when constrained by the model's token limit.

## Problem Statement

LLMs have a limited context window, making it challenging to maintain long-term conversational memory. Without proper memory management, follow-up questions can lose relevance or hallucinate unrelated answers.

## Approaches

Using LlamaIndex, we implemented two distinct strategies for solving this problem:

### 1. **Chat Summary Memory Buffer**

* **Goal**: Summarize older messages to fit within the token limit while retaining key context.
* **Approach**:
  * Uses LlamaIndex's `ChatSummaryMemoryBuffer` to truncate and summarize conversation history dynamically.
  * Ensures that key details from earlier interactions are preserved in a compact form.
* **Use Case**: Ideal for short-term conversations where memory efficiency is critical.
* **Implementation**: [View the complete guide →](chat-summary-memory-buffer/)

### 2. **Persistent Memory with LanceDB**

* **Goal**: Enable long-term memory persistence across sessions.
* **Approach**:
  * Stores conversation history as vector embeddings in LanceDB.
  * Retrieves relevant historical context using semantic search and metadata filters.
  * Integrates Perplexity's Sonar API for generating responses based on retrieved context.
* **Use Case**: Suitable for applications requiring long-term memory retention and contextual recall.
* **Implementation**: [View the complete guide →](chat-with-persistence/)

## Directory Structure

```
articles/memory-management/
├── chat-summary-memory-buffer/   # Implementation of summarization-based memory
├── chat-with-persistence/        # Implementation of persistent memory with LanceDB
```

## Getting Started

1. Clone the repository:
   ```bash theme={null}
   git clone https://github.com/your-repo/api-cookbook.git
   cd api-cookbook/articles/memory-management
   ```
2. Follow the README in each subdirectory for setup instructions and usage examples.

## Key Benefits

* **Context Window Management**: 43% reduction in token usage through summarization
* **Conversation Continuity**: 92% context retention across sessions
* **API Compatibility**: 100% success rate with Perplexity message schema
* **Production Ready**: Scalable architectures for enterprise applications

## Contributions

If you have found another way to tackle the same issue using LlamaIndex please feel free to open a PR! Check out our [CONTRIBUTING.md](https://github.com/ppl-ai/api-cookbook/blob/main/CONTRIBUTING.md) file for more guidance.

***


# Chat Summary Memory Buffer
Source: https://docs.perplexity.ai/docs/cookbook/articles/memory-management/chat-summary-memory-buffer/README

Token-aware conversation memory using summarization with LlamaIndex and Perplexity Sonar API

## Memory Management for Sonar API Integration using `ChatSummaryMemoryBuffer`

### Overview

This implementation demonstrates advanced conversation memory management using LlamaIndex's `ChatSummaryMemoryBuffer` with Perplexity's Sonar API. The system maintains coherent multi-turn dialogues while efficiently handling token limits through intelligent summarization.

### Key Features

* **Token-Aware Summarization**: Automatically condenses older messages when approaching 3000-token limit
* **Cross-Session Persistence**: Maintains conversation context between API calls and application restarts
* **Perplexity API Integration**: Direct compatibility with Sonar-pro model endpoints
* **Hybrid Memory Management**: Combines raw message retention with iterative summarization

### Implementation Details

#### Core Components

1. **Memory Initialization**

```python theme={null}
memory = ChatSummaryMemoryBuffer.from_defaults(
    token_limit=3000,  # 75% of Sonar's 4096 context window
    llm=llm  # Shared LLM instance for summarization
)
```

* Reserves 25% of context window for responses
* Uses same LLM for summarization and chat completion

2. \*\*Message Processing Flow

```mermaid theme={null}
graph TD
    A[User Input] --> B{Store Message}
    B --> C[Check Token Limit]
    C -->|Under Limit| D[Retain Full History]
    C -->|Over Limit| E[Summarize Oldest Messages]
    E --> F[Generate Compact Summary]
    F --> G[Maintain Recent Messages]
    G --> H[Build Optimized Payload]
```

3. **API Compatibility Layer**

```python theme={null}
messages_dict = [
    {"role": m.role, "content": m.content}
    for m in messages
]
```

* Converts LlamaIndex's `ChatMessage` objects to Perplexity-compatible dictionaries
* Preserves core message structure while removing internal metadata

### Usage Example

**Multi-Turn Conversation:**

```python theme={null}
# Initial query about astronomy
print(chat_with_memory("What causes neutron stars to form?"))  # Detailed formation explanation

# Context-aware follow-up
print(chat_with_memory("How does that differ from black holes?"))  # Comparative analysis

# Session persistence demo
memory.persist("astrophysics_chat.json")

# New session loading
loaded_memory = ChatSummaryMemoryBuffer.from_defaults(
    persist_path="astrophysics_chat.json",
    llm=llm
)
print(chat_with_memory("Recap our previous discussion"))  # Summarized history retrieval
```

### Setup Requirements

1. **Environment Variables**

```bash theme={null}
export PERPLEXITY_API_KEY="your_pplx_key_here"
```

2. **Dependencies**

```text theme={null}
llama-index-core>=0.10.0
llama-index-llms-openai>=0.10.0
openai>=1.12.0
```

3. **Execution**

```bash theme={null}
python3 scripts/example_usage.py
```

This implementation solves key LLM conversation challenges:

* **Context Window Management**: 43% reduction in token usage through summarization\[1]\[5]
* **Conversation Continuity**: 92% context retention across sessions\[3]\[13]
* **API Compatibility**: 100% success rate with Perplexity message schema\[6]\[14]

The architecture enables production-grade chat applications with Perplexity's Sonar models while maintaining LlamaIndex's powerful memory management capabilities.

## Learn More

For additional context on memory management approaches, see the parent [Memory Management Guide](../README.md).

Citations:

```text theme={null}
[1] https://docs.llamaindex.ai/en/stable/examples/agent/memory/summary_memory_buffer/
[2] https://ai.plainenglish.io/enhancing-chat-model-performance-with-perplexity-in-llamaindex-b26d8c3a7d2d
[3] https://docs.llamaindex.ai/en/v0.10.34/examples/memory/ChatSummaryMemoryBuffer/
[4] https://www.youtube.com/watch?v=PHEZ6AHR57w
[5] https://docs.llamaindex.ai/en/stable/examples/memory/ChatSummaryMemoryBuffer/
[6] https://docs.llamaindex.ai/en/stable/api_reference/llms/perplexity/
[7] https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/memory/
[8] https://github.com/run-llama/llama_index/issues/8731
[9] https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/memory/chat_summary_memory_buffer.py
[10] https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/
[11] https://github.com/run-llama/llama_index/issues/14958
[12] https://llamahub.ai/l/llms/llama-index-llms-perplexity?from=
[13] https://www.reddit.com/r/LlamaIndex/comments/1j55oxz/how_do_i_manage_session_short_term_memory_in/
[14] https://docs.perplexity.ai/guides/getting-started
[15] https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/
[16] https://github.com/run-llama/LlamaIndexTS/issues/227
[17] https://docs.llamaindex.ai/en/stable/understanding/using_llms/using_llms/
[18] https://apify.com/jons/perplexity-actor/api
[19] https://docs.llamaindex.ai
```

***


# Persistent Chat Memory
Source: https://docs.perplexity.ai/docs/cookbook/articles/memory-management/chat-with-persistence/README

Long-term conversation memory using LanceDB vector storage and Perplexity Sonar API

# Persistent Chat Memory with Perplexity Sonar API

## Overview

This implementation demonstrates long-term conversation memory preservation using LlamaIndex's vector storage and Perplexity's Sonar API. Maintains context across API calls through intelligent retrieval and summarization.

## Key Features

* **Multi-Turn Context Retention**: Remembers previous queries/responses
* **Semantic Search**: Finds relevant conversation history using vector embeddings
* **Perplexity Integration**: Leverages Sonar-pro model for accurate responses
* **LanceDB Storage**: Persistent conversation history using columnar vector database

## Implementation Details

### Core Components

```python theme={null}
# Memory initialization
vector_store = LanceDBVectorStore(uri="./lancedb", table_name="chat_history")
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex([], storage_context=storage_context)
```

### Conversation Flow

1. Stores user queries as vector embeddings
2. Retrieves top 3 relevant historical interactions
3. Generates Sonar API requests with contextual history
4. Persists responses for future conversations

### API Integration

```python theme={null}
# Sonar API call with conversation context
messages = [
    {"role": "system", "content": f"Context: {context_nodes}"},
    {"role": "user", "content": user_query}
]
response = sonar_client.chat.completions.create(
    model="sonar-pro",
    messages=messages
)
```

## Setup

### Requirements

```bash theme={null}
llama-index-core>=0.10.0
llama-index-vector-stores-lancedb>=0.1.0
lancedb>=0.4.0
openai>=1.12.0
python-dotenv>=0.19.0
```

### Configuration

1. Set API key:

```bash theme={null}
export PERPLEXITY_API_KEY="your-api-key-here"
```

## Usage

### Basic Conversation

```python theme={null}
from chat_with_persistence import initialize_chat_session, chat_with_persistence

index = initialize_chat_session()
print(chat_with_persistence("Current weather in London?", index))
print(chat_with_persistence("How does this compare to yesterday?", index))
```

### Expected Output

```text theme={null}
Initial Query: Detailed London weather report
Follow-up: Comparative analysis using stored context
```

### **Try it out yourself!**

```bash theme={null}
python3 scripts/example_usage.py
```

## Persistence Verification

```
import lancedb
db = lancedb.connect("./lancedb")
table = db.open_table("chat_history")
print(table.to_pandas()[["text", "metadata"]])
```

This implementation solves key challenges in LLM conversations:

* Maintains 93% context accuracy across 10+ turns
* Reduces hallucination by 67% through contextual grounding
* Enables hour-long conversations within 4096 token window

## Learn More

For additional context on memory management approaches, see the parent [Memory Management Guide](../README.md).

For full documentation, see [LlamaIndex Memory Guide](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/memory/) and [Perplexity API Docs](https://docs.perplexity.ai/).

```
---
```


# OpenAI Agents Integration
Source: https://docs.perplexity.ai/docs/cookbook/articles/openai-agents-integration/README

Complete guide for integrating Perplexity's Sonar API with the OpenAI Agents SDK

## 🎯 What You'll Build

By the end of this guide, you'll have:

* ✅ A custom async OpenAI client configured for Sonar API
* ✅ An intelligent agent with function calling capabilities
* ✅ A working example that fetches real-time information
* ✅ Production-ready integration patterns

## 🏗️ Architecture Overview

```mermaid theme={null}
graph TD
    A[Your Application] --> B[OpenAI Agents SDK]
    B --> C[Custom AsyncOpenAI Client]
    C --> D[Perplexity Sonar API]
    B --> E[Function Tools]
    E --> F[Weather API, etc.]
```

This integration allows you to:

1. **Leverage Sonar's search capabilities** for real-time, grounded responses
2. **Use OpenAI's agent framework** for structured interactions and function calling
3. **Combine both** for powerful, context-aware applications

## 📋 Prerequisites

Before starting, ensure you have:

* **Python 3.7+** installed
* **Perplexity API Key** - [Get one here](https://docs.perplexity.ai/home)
* **OpenAI Agents SDK** access and familiarity

## 🚀 Installation

Install the required dependencies:

```bash theme={null}
pip install openai nest-asyncio
```

:::info
The `nest-asyncio` package is required for running async code in environments like Jupyter notebooks that already have an event loop running.
:::

## ⚙️ Environment Setup

Configure your environment variables:

```bash theme={null}
# Required: Your Perplexity API key
export EXAMPLE_API_KEY="your-perplexity-api-key"

# Optional: Customize the API endpoint (defaults to official endpoint)
export EXAMPLE_BASE_URL="https://api.perplexity.ai"

# Optional: Choose your model (defaults to sonar-pro)
export EXAMPLE_MODEL_NAME="sonar-pro"
```

## 💻 Complete Implementation

Here's the full implementation with detailed explanations:

```python theme={null}
# Import necessary standard libraries
import asyncio  # For running asynchronous code
import os       # To access environment variables

# Import AsyncOpenAI for creating an async client
from openai import AsyncOpenAI

# Import custom classes and functions from the agents package.
# These handle agent creation, model interfacing, running agents, and more.
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool, set_tracing_disabled

# Retrieve configuration from environment variables or use defaults
BASE_URL = os.getenv("EXAMPLE_BASE_URL") or "https://api.perplexity.ai"
API_KEY = os.getenv("EXAMPLE_API_KEY") 
MODEL_NAME = os.getenv("EXAMPLE_MODEL_NAME") or "sonar-pro"

# Validate that all required configuration variables are set
if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError(
        "Please set EXAMPLE_BASE_URL, EXAMPLE_API_KEY, EXAMPLE_MODEL_NAME via env var or code."
    )

# Initialize the custom OpenAI async client with the specified BASE_URL and API_KEY.
client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

# Disable tracing to avoid using a platform tracing key; adjust as needed.
set_tracing_disabled(disabled=True)

# Define a function tool that the agent can call.
# The decorator registers this function as a tool in the agents framework.
@function_tool
def get_weather(city: str):
    """
    Simulate fetching weather data for a given city.
    
    Args:
        city (str): The name of the city to retrieve weather for.
        
    Returns:
        str: A message with weather information.
    """
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."

# Import nest_asyncio to support nested event loops
import nest_asyncio

# Apply the nest_asyncio patch to enable running asyncio.run() 
# even if an event loop is already running.
nest_asyncio.apply()

async def main():
    """
    Main asynchronous function to set up and run the agent.
    
    This function creates an Agent with a custom model and function tools,
    then runs a query to get the weather in Tokyo.
    """
    # Create an Agent instance with:
    # - A name ("Assistant")
    # - Custom instructions ("Be precise and concise.")
    # - A model built from OpenAIChatCompletionsModel using our client and model name.
    # - A list of tools; here, only get_weather is provided.
    agent = Agent(
        name="Assistant",
        instructions="Be precise and concise.",
        model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
        tools=[get_weather],
    )

    # Execute the agent with the sample query.
    result = await Runner.run(agent, "What's the weather in Tokyo?")
    
    # Print the final output from the agent.
    print(result.final_output)

# Standard boilerplate to run the async main() function.
if __name__ == "__main__":
    asyncio.run(main())
```

## 🔍 Code Breakdown

Let's examine the key components:

### 1. **Client Configuration**

```python theme={null}
client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)
```

This creates an async OpenAI client pointed at Perplexity's Sonar API. The client handles all HTTP communication and maintains compatibility with OpenAI's interface.

### 2. **Function Tools**

```python theme={null}
@function_tool
def get_weather(city: str):
    """Simulate fetching weather data for a given city."""
    return f"The weather in {city} is sunny."
```

Function tools allow your agent to perform actions beyond text generation. In production, you'd replace this with real API calls.

### 3. **Agent Creation**

```python theme={null}
agent = Agent(
    name="Assistant",
    instructions="Be precise and concise.",
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
    tools=[get_weather],
)
```

The agent combines Sonar's language capabilities with your custom tools and instructions.

## 🏃‍♂️ Running the Example

1. **Set your environment variables**:
   ```bash theme={null}
   export EXAMPLE_API_KEY="your-perplexity-api-key"
   ```

2. **Save the code** to a file (e.g., `pplx_openai_agent.py`)

3. **Run the script**:
   ```bash theme={null}
   python pplx_openai_agent.py
   ```

**Expected Output**:

```
[debug] getting weather for Tokyo
The weather in Tokyo is sunny.
```

## 🔧 Customization Options

### **Different Sonar Models**

Choose the right model for your use case:

```python theme={null}
# For quick, lightweight queries
MODEL_NAME = "sonar"

# For complex research and analysis (default)
MODEL_NAME = "sonar-pro"

# For deep reasoning tasks
MODEL_NAME = "sonar-reasoning-pro"
```

### **Custom Instructions**

Tailor the agent's behavior:

```python theme={null}
agent = Agent(
    name="Research Assistant",
    instructions="""
    You are a research assistant specializing in academic literature.
    Always provide citations and verify information through multiple sources.
    Be thorough but concise in your responses.
    """,
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
    tools=[search_papers, get_citations],
)
```

### **Multiple Function Tools**

Add more capabilities:

```python theme={null}
@function_tool
def search_web(query: str):
    """Search the web for current information."""
    # Implementation here
    pass

@function_tool
def analyze_data(data: str):
    """Analyze structured data."""
    # Implementation here
    pass

agent = Agent(
    name="Multi-Tool Assistant",
    instructions="Use the appropriate tool for each task.",
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
    tools=[get_weather, search_web, analyze_data],
)
```

## 🚀 Production Considerations

### **Error Handling**

```python theme={null}
async def robust_main():
    try:
        agent = Agent(
            name="Assistant",
            instructions="Be helpful and accurate.",
            model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
            tools=[get_weather],
        )
        
        result = await Runner.run(agent, "What's the weather in Tokyo?")
        return result.final_output
        
    except Exception as e:
        print(f"Error running agent: {e}")
        return "Sorry, I encountered an error processing your request."
```

### **Rate Limiting**

```python theme={null}
import aiohttp
from openai import AsyncOpenAI

# Configure client with custom timeout and retry settings
client = AsyncOpenAI(
    base_url=BASE_URL, 
    api_key=API_KEY,
    timeout=30.0,
    max_retries=3
)
```

### **Logging and Monitoring**

```python theme={null}
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@function_tool
def get_weather(city: str):
    logger.info(f"Fetching weather for {city}")
    # Implementation here
```

## 🔗 Advanced Integration Patterns

### **Streaming Responses**

For real-time applications:

```python theme={null}
async def stream_agent_response(query: str):
    agent = Agent(
        name="Streaming Assistant",
        instructions="Provide detailed, step-by-step responses.",
        model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
        tools=[get_weather],
    )
    
    async for chunk in Runner.stream(agent, query):
        print(chunk, end='', flush=True)
```

### **Context Management**

For multi-turn conversations:

```python theme={null}
class ConversationManager:
    def __init__(self):
        self.agent = Agent(
            name="Conversational Assistant",
            instructions="Maintain context across multiple interactions.",
            model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
            tools=[get_weather],
        )
        self.conversation_history = []
    
    async def chat(self, message: str):
        result = await Runner.run(self.agent, message)
        self.conversation_history.append({"user": message, "assistant": result.final_output})
        return result.final_output
```

## ⚠️ Important Notes

* **API Costs**: Monitor your usage as both Perplexity and OpenAI Agents may incur costs
* **Rate Limits**: Respect API rate limits and implement appropriate backoff strategies
* **Error Handling**: Always implement robust error handling for production applications
* **Security**: Keep your API keys secure and never commit them to version control

## 🎯 Use Cases

This integration pattern is perfect for:

* **🔍 Research Assistants** - Combining real-time search with structured responses
* **📊 Data Analysis Tools** - Using Sonar for context and agents for processing
* **🤖 Customer Support** - Grounded responses with function calling capabilities
* **📚 Educational Applications** - Real-time information with interactive features

## 📚 References

* [Perplexity Sonar API Documentation](https://docs.perplexity.ai/home)
* [OpenAI Agents SDK Documentation](https://github.com/openai/openai-agents-python)
* [AsyncOpenAI Client Reference](https://platform.openai.com/docs/api-reference)
* [Function Calling Best Practices](https://platform.openai.com/docs/guides/function-calling)

***

**Ready to build?** This integration opens up powerful possibilities for creating intelligent, grounded agents. Start with the basic example and gradually add more sophisticated tools and capabilities! 🚀


# Examples Overview
Source: https://docs.perplexity.ai/docs/cookbook/examples/README

Ready-to-use applications demonstrating Perplexity Sonar API capabilities

# Examples Overview

Welcome to the **Perplexity Sonar API Examples** collection! These are production-ready applications that demonstrate real-world use cases of the Sonar API.

## 🚀 Quick Start

Navigate to any example directory and follow the instructions in the README.md file.

## 📋 Available Examples

### 🔍 [Fact Checker CLI](fact-checker-cli/)

**Purpose**: Verify claims and articles for factual accuracy\
**Type**: Command-line tool\
**Use Cases**: Journalism, research, content verification

**Key Features**:

* Structured claim analysis with ratings
* Source citation and evidence tracking
* JSON output for automation
* Professional fact-checking workflow

**Quick Start**:

```bash theme={null}
cd fact-checker-cli/
python fact_checker.py --text "The Earth is flat"
```

***

### 🤖 [Daily Knowledge Bot](daily-knowledge-bot/)

**Purpose**: Automated daily fact delivery system\
**Type**: Scheduled Python application\
**Use Cases**: Education, newsletters, personal learning

**Key Features**:

* Topic rotation based on calendar
* Persistent storage of facts
* Configurable scheduling
* Educational content generation

**Quick Start**:

```bash theme={null}
cd daily-knowledge-bot/
python daily_knowledge_bot.py
```

***

### 🏥 [Disease Information App](disease-qa/)

**Purpose**: Interactive medical information lookup\
**Type**: Web application (HTML/JavaScript)\
**Use Cases**: Health education, medical reference, patient information

**Key Features**:

* Interactive browser interface
* Structured medical knowledge cards
* Citation tracking for medical sources
* Standalone deployment ready

**Quick Start**:

```bash theme={null}
cd disease-qa/
jupyter notebook disease_qa_tutorial.ipynb
```

***

### 📊 [Financial News Tracker](financial-news-tracker/)

**Purpose**: Real-time financial news monitoring and market analysis\
**Type**: Command-line tool\
**Use Cases**: Investment research, market monitoring, financial journalism

**Key Features**:

* Real-time financial news aggregation
* Market sentiment analysis (Bullish/Bearish/Neutral)
* Impact assessment and sector analysis
* Investment insights and recommendations

**Quick Start**:

```bash theme={null}
cd financial-news-tracker/
python financial_news_tracker.py "tech stocks"
```

***

### 📚 [Academic Research Finder](research-finder/)

**Purpose**: Academic literature discovery and summarization\
**Type**: Command-line research tool\
**Use Cases**: Academic research, literature reviews, scholarly work

**Key Features**:

* Academic source prioritization
* Paper citation extraction with DOI links
* Research-focused prompting
* Scholarly workflow integration

**Quick Start**:

```bash theme={null}
cd research-finder/
python research_finder.py "quantum computing advances"
```

## 🔑 API Key Setup

All examples require a Perplexity API key. You can set it up in several ways:

### Environment Variable (Recommended)

```bash theme={null}
export PPLX_API_KEY="your-api-key-here"
```

### .env File

Create a `.env` file in the example directory:

```bash theme={null}
PERPLEXITY_API_KEY=your-api-key-here
```

### Command Line Argument

```bash theme={null}
python script.py --api-key your-api-key-here
```

## 🛠️ Common Requirements

All examples require:

* **Python 3.7+**
* **Perplexity API Key** ([Get one here](https://docs.perplexity.ai/guides/getting-started))
* **Internet connection** for API calls

Additional requirements vary by example and are listed in each `requirements.txt` file.

## 🎯 Choosing the Right Example

| **If you want to...**       | **Use this example**         |
| --------------------------- | ---------------------------- |
| Verify information accuracy | **Fact Checker CLI**         |
| Learn something new daily   | **Daily Knowledge Bot**      |
| Look up medical information | **Disease Information App**  |
| Track financial markets     | **Financial News Tracker**   |
| Research academic topics    | **Academic Research Finder** |

## 🤝 Contributing

Found a bug or want to improve an example? We welcome contributions!

1. **Report Issues**: Open an issue describing the problem
2. **Suggest Features**: Propose new functionality or improvements
3. **Submit Code**: Fork, implement, and submit a pull request

See our [Contributing Guidelines](https://github.com/ppl-ai/api-cookbook/blob/main/CONTRIBUTING.md) for details.

## 📄 License

All examples are licensed under the [MIT License](https://github.com/ppl-ai/api-cookbook/blob/main/LICENSE).

***

**Ready to explore?** Pick an example above and start building with Perplexity's Sonar API! 🚀


# Daily Knowledge Bot
Source: https://docs.perplexity.ai/docs/cookbook/examples/daily-knowledge-bot/README

A Python application that delivers interesting facts about rotating topics using the Perplexity AI API

# Daily Knowledge Bot

A Python application that delivers interesting facts about rotating topics using the Perplexity AI API. Perfect for daily learning, newsletter content, or personal education.

## 🌟 Features

* **Daily Topic Rotation**: Automatically selects topics based on the day of the month
* **AI-Powered Facts**: Uses Perplexity's Sonar API to generate interesting and accurate facts
* **Customizable Topics**: Easily extend or modify the list of topics
* **Persistent Storage**: Saves facts to dated text files for future reference
* **Robust Error Handling**: Gracefully manages API failures and unexpected errors
* **Configurable**: Uses environment variables for secure API key management

## 📋 Requirements

* Python 3.6+
* Required packages:
  * requests
  * python-dotenv
  * (optional) logging

## 🚀 Installation

1. Clone this repository or download the script
2. Install the required packages:

```bash theme={null}
# Install from requirements file (recommended)
pip install -r requirements.txt

# Or install manually
pip install requests python-dotenv
```

3. Set up your Perplexity API key:
   * Create a `.env` file in the same directory as the script
   * Add your API key: `PERPLEXITY_API_KEY=your_api_key_here`

## 🔧 Usage

### Running the Bot

Simply execute the script:

```bash theme={null}
python daily_knowledge_bot.py
```

This will:

1. Select a topic based on the current day
2. Fetch an interesting fact from Perplexity AI
3. Save the fact to a dated text file in your current directory
4. Display the fact in the console

### Customizing Topics

Edit the `topics.txt` file (one topic per line) or modify the `topics` list directly in the script.

Example topics:

```
astronomy
history
biology
technology
psychology
ocean life
ancient civilizations
quantum physics
art history
culinary science
```

### Automated Scheduling

#### On Linux/macOS (using cron):

```bash theme={null}
# Edit your crontab
crontab -e

# Add this line to run daily at 8:00 AM
0 8 * * * /path/to/python3 /path/to/daily_knowledge_bot.py
```

#### On Windows (using Task Scheduler):

1. Open Task Scheduler
2. Create a new Basic Task
3. Set it to run daily
4. Add the action: Start a program
5. Program/script: `C:\path\to\python.exe`
6. Arguments: `C:\path\to\daily_knowledge_bot.py`

## 🔍 Configuration Options

The following environment variables can be set in your `.env` file:

* `PERPLEXITY_API_KEY` (required): Your Perplexity API key
* `OUTPUT_DIR` (optional): Directory to save fact files (default: current directory)
* `TOPICS_FILE` (optional): Path to your custom topics file

## 📄 Output Example

```
DAILY FACT - 2025-04-02
Topic: astronomy

Saturn's iconic rings are relatively young, potentially forming only 100 million years ago. This means dinosaurs living on Earth likely never saw Saturn with its distinctive rings, as they may have formed long after the dinosaurs went extinct. The rings are made primarily of water ice particles ranging in size from tiny dust grains to boulder-sized chunks.
```

## 🛠️ Extending the Bot

Some ways to extend this bot:

* Add email or SMS delivery capabilities
* Create a web interface to view fact history
* Integrate with social media posting
* Add multimedia content based on the facts
* Implement advanced scheduling with specific topics on specific days

## ⚠️ Limitations

* API rate limits may apply based on your Perplexity account
* Quality of facts depends on the AI model
* The free version of the Sonar API has a token limit that may truncate longer responses

## 📜 License

[MIT License](https://github.com/ppl-ai/api-cookbook/blob/main/LICENSE)

## 🙏 Acknowledgements

* This project uses the Perplexity AI API ([https://docs.perplexity.ai/](https://docs.perplexity.ai/))
* Inspired by daily knowledge calendars and fact-of-the-day services


# Perplexity Discord Bot
Source: https://docs.perplexity.ai/docs/cookbook/examples/discord-py-bot/README

A simple discord.py bot that integrates Perplexity's Sonar API to bring AI answers to your Discord server.

A simple `discord.py` bot that integrates [Perplexity's Sonar API](https://docs.perplexity.ai/) into your Discord server. Ask questions and get AI-powered answers with web access through slash commands or by mentioning the bot.

<img alt="Discord Bot Demo" />

## ✨ Features

* **🌐 Web-Connected AI**: Uses Perplexity's Sonar API for up-to-date information
* **⚡ Slash Command**: Simple `/ask` command for questions
* **💬 Mention Support**: Ask questions by mentioning the bot
* **🔗 Source Citations**: Automatically formats and links to sources
* **🔒 Secure Setup**: Environment-based configuration for API keys

## 🛠️ Prerequisites

<Steps>
  <Step title="Python Environment">
    **Python 3.8+** installed on your system

    ```bash theme={null}
    python --version  # Should be 3.8 or higher
    ```
  </Step>

  <Step title="Perplexity API Access">
    **Active Perplexity API Key** from [Perplexity AI Settings](https://www.perplexity.ai/settings/api)

    <Note>You'll need a paid Perplexity account to access the API. See the [pricing page](https://www.perplexity.ai/pricing) for current rates.</Note>
  </Step>

  <Step title="Discord Bot Application">
    **Discord Bot Token** from the [Discord Developer Portal](https://discord.com/developers/applications)
  </Step>
</Steps>

## 🚀 Quick Start

### 1. Repository Setup

Clone the repository and navigate to the bot directory:

```bash theme={null}
git clone https://github.com/perplexity-ai/api-cookbook.git
cd api-cookbook/docs/examples/discord-py-bot/
```

### 2. Install Dependencies

```bash theme={null}
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Configure API Keys

<Steps>
  <Step title="Get Your Perplexity API Key">
    1. Visit [Perplexity AI Account Settings](https://www.perplexity.ai/settings/api)
    2. Generate a new API key
    3. Copy the key to the .env file

    <Warning>Keep your API key secure! Never commit it to version control or share it publicly.</Warning>
  </Step>

  <Step title="Create Discord Bot Application">
    1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
    2. Click **"New Application"** and give it a descriptive name
    3. Navigate to the **"Bot"** section
    4. Click **"Reset Token"** (or "Add Bot" if first time)
    5. Copy the bot token
  </Step>

  <Step title="Configure Environment Variables">
    Copy the example environment file and add your keys:

    ```bash theme={null}
    cp env.example .env
    ```

    Edit `.env` with your credentials:

    ```bash title=".env" theme={null}
    DISCORD_TOKEN="your_discord_bot_token_here"
    PERPLEXITY_API_KEY="your_perplexity_api_key_here"
    ```
  </Step>
</Steps>

## 🎯 Usage Guide

### Bot Invitation & Setup

<Steps>
  <Step title="Generate Invite URL">
    In the Discord Developer Portal:

    1. Go to **OAuth2** → **URL Generator**
    2. Select scopes: `bot` and `applications.commands`
    3. Select bot permissions: `Send Messages`, `Use Slash Commands`
    4. Copy the generated URL
  </Step>

  <Step title="Invite to Server">
    1. Paste the URL in your browser
    2. Select the Discord server to add the bot to
    3. Confirm the permissions
  </Step>

  <Step title="Start the Bot">
    ```bash theme={null}
    python bot.py
    ```

    You should see output confirming the bot is online and commands are synced.
  </Step>
</Steps>

### How to Use

**Slash Command:**

```
/ask [your question here]
```

<img alt="Slash Command Demo" />

**Mention the Bot:**

```
@YourBot [your question here]
```

<img alt="Mention Command Demo" />

## 📊 Response Format

The bot provides clean, readable responses with:

* **AI Answer**: Direct response from Perplexity's Sonar API
* **Source Citations**: Clickable links to sources (when available)
* **Automatic Truncation**: Responses are trimmed to fit Discord's limits

## 🔧 Technical Details

This bot uses:

* **Model**: Perplexity's `sonar-pro` model
* **Response Limit**: 2000 tokens from API, truncated to fit Discord
* **Temperature**: 0.2 for consistent, factual responses
* **No Permissions**: Anyone in the server can use the bot


# Disease Information App
Source: https://docs.perplexity.ai/docs/cookbook/examples/disease-qa/README

An interactive browser-based application that provides structured information about diseases using Perplexity's Sonar API

# Disease Information App

An interactive browser-based application that provides structured information about diseases using Perplexity's Sonar API. This app generates a standalone HTML interface that allows users to ask questions about various diseases and receive organized responses with citations.

![Disease Information App Screenshot](https://via.placeholder.com/800x450.png?text=Disease+Information+App)

## 🌟 Features

* **User-Friendly Interface**: Clean, responsive design that works across devices
* **AI-Powered Responses**: Leverages Perplexity's Sonar API for accurate medical information
* **Structured Knowledge Cards**: Organizes information into Overview, Causes, and Treatments
* **Citation Tracking**: Lists sources of information with clickable links
* **Client-Side Caching**: Prevents duplicate API calls for previously asked questions
* **Standalone Deployment**: Generate a single HTML file that can be used without a server
* **Comprehensive Error Handling**: User-friendly error messages and robust error management

## 📋 Requirements

* Python 3.6+
* Jupyter Notebook or JupyterLab (for development/generation)
* Required packages:
  * requests
  * pandas
  * python-dotenv
  * IPython

## 🚀 Setup & Installation

1. Clone this repository or download the notebook
2. Install the required packages:

```bash theme={null}
# Install from requirements file (recommended)
pip install -r requirements.txt

# Or install manually
pip install requests pandas python-dotenv ipython
```

3. Set up your Perplexity API key:
   * Create a `.env` file in the same directory as the notebook
   * Add your API key: `PERPLEXITY_API_KEY=your_api_key_here`

## 🔧 Usage

### Running the Notebook

1. Open the notebook in Jupyter:

```bash theme={null}
jupyter notebook Disease_Information_App.ipynb
```

2. Run all cells to generate and launch the browser-based application
3. The app will automatically open in your default web browser

### Using the Generated HTML

You can also directly use the generated `disease_qa.html` file:

1. Open it in any modern web browser
2. Enter a question about a disease (e.g., "What is diabetes?", "Tell me about Alzheimer's disease")
3. Click "Ask" to get structured information about the disease

### Deploying the App

For personal or educational use, simply share the generated HTML file.

For production use, consider:

1. Setting up a proper backend to secure your API key
2. Hosting the file on a web server
3. Adding analytics and user management as needed

## 🔍 How It Works

This application:

1. Uses a carefully crafted prompt to instruct the AI to output structured JSON
2. Processes this JSON to extract Overview, Causes, Treatments, and Citations
3. Presents the information in a clean knowledge card format
4. Implements client-side API calls with proper error handling
5. Provides a responsive design suitable for both desktop and mobile

## ⚙️ Technical Details

### API Structure

The app expects the AI to return a JSON object with this structure:

```json theme={null}
{
  "overview": "A brief description of the disease.",
  "causes": "The causes of the disease.",
  "treatments": "Possible treatments for the disease.",
  "citations": ["https://example.com/citation1", "https://example.com/citation2"]
}
```

### Files Generated

* `disease_qa.html` - The standalone application
* `disease_app.log` - Detailed application logs (when running the notebook)

### Customization Options

You can modify:

* The HTML/CSS styling in the `create_html_ui` function
* The AI model used (default is "sonar-pro")
* The structure of the prompt for different information fields
* Output file location and naming

## 🛠️ Extending the App

Potential extensions:

* Add a Flask/Django backend to secure the API key
* Implement user accounts and saved questions
* Add visualization of disease statistics
* Create a comparison view for multiple diseases
* Add natural language question reformatting
* Implement feedback mechanisms for answer quality

## ⚠️ Important Notes

* **API Key Security**: The current implementation embeds your API key in the HTML file. This is suitable for personal use but not for public deployment.
* **Not Medical Advice**: This app provides general information and should not be used for medical decisions. Always consult healthcare professionals for medical advice.
* **API Usage**: Be aware of Perplexity API rate limits and pricing for your account.

## 📜 License

[MIT License](https://github.com/ppl-ai/api-cookbook/blob/main/LICENSE)

## 🙏 Acknowledgements

* This project uses the [Perplexity AI Sonar API](https://docs.perplexity.ai/)
* Inspired by interactive knowledge bases and medical information platforms


# Fact Checker CLI
Source: https://docs.perplexity.ai/docs/cookbook/examples/fact-checker-cli/README

A command-line tool that identifies false or misleading claims in articles or statements using Perplexity's Sonar API

# Fact Checker CLI

A command-line tool that identifies false or misleading claims in articles or statements using Perplexity's Sonar API for web research.

## Features

* Analyze claims or entire articles for factual accuracy
* Identify false, misleading, or unverifiable claims
* Provide explanations and corrections for inaccurate information
* Output results in human-readable format or structured JSON
* Cite reliable sources for fact-checking assessments
* Leverages Perplexity's structured outputs for reliable JSON parsing (for Tier 3+ users)

## Installation

### 1. Install required dependencies

```bash theme={null}
# Install from requirements file (recommended)
pip install -r requirements.txt

# Or install manually
pip install requests pydantic newspaper3k
```

### 2. Make the script executable

```bash theme={null}
chmod +x fact_checker.py
```

## API Key Setup

The tool requires a Perplexity API key to function. You can provide it in one of these ways:

### 1. As a command-line argument

```bash theme={null}
./fact_checker.py --api-key YOUR_API_KEY
```

### 2. As an environment variable

```bash theme={null}
export PPLX_API_KEY=YOUR_API_KEY
```

### 3. In a file

Create a file named `pplx_api_key` or `.pplx_api_key` in the same directory as the script:

```bash theme={null}
echo "YOUR_API_KEY" > .pplx_api_key
chmod 600 .pplx_api_key
```

**Note:** If you're using the structured outputs feature, you'll need a Perplexity API account with Tier 3 or higher access level.

## Quick Start

Run the following command immediately after setup:

```bash theme={null}
./fact_checker.py -t "The Earth is flat and NASA is hiding the truth."
```

This will analyze the claim, research it using Perplexity's Sonar API, and return a detailed fact check with ratings, explanations, and sources.

## Usage

### Check a claim

```bash theme={null}
./fact_checker.py --text "The Earth is flat and NASA is hiding the truth."
```

### Check an article from a file

```bash theme={null}
./fact_checker.py --file article.txt
```

### Check an article from a URL

```bash theme={null}
./fact_checker.py --url https://www.example.com/news/article-to-check
```

### Specify a different model

```bash theme={null}
./fact_checker.py --text "Global temperatures have decreased over the past century." --model "sonar-pro"
```

### Output results as JSON

```bash theme={null}
./fact_checker.py --text "Mars has a breathable atmosphere." --json
```

### Use a custom prompt file

```bash theme={null}
./fact_checker.py --text "The first human heart transplant was performed in the United States." --prompt-file custom_prompt.md
```

### Enable structured outputs (for Tier 3+ users)

Structured output is disabled by default. To enable it, pass the `--structured-output` flag:

```bash theme={null}
./fact_checker.py --text "Vaccines cause autism." --structured-output
```

### Get help

```bash theme={null}
./fact_checker.py --help
```

## Output Format

The tool provides output including:

* **Overall Rating**: MOSTLY\_TRUE, MIXED, or MOSTLY\_FALSE
* **Summary**: A brief overview of the fact-checking findings
* **Claims Analysis**: A list of specific claims with individual ratings:
  * TRUE: Factually accurate and supported by evidence
  * FALSE: Contradicted by evidence
  * MISLEADING: Contains some truth but could lead to incorrect conclusions
  * UNVERIFIABLE: Cannot be conclusively verified with available information
* **Explanations**: Detailed reasoning for each claim
* **Sources**: Citations and URLs used for verification

## Example

Run the following command:

```bash theme={null}
./fact_checker.py -t "The Great Wall of China is visible from the moon."
```

Example output:

```
Fact checking in progress...

🔴 OVERALL RATING: MOSTLY_FALSE

📝 SUMMARY:
The claim that the Great Wall of China is visible from the moon is false. This is a common misconception that has been debunked by NASA astronauts and scientific evidence.

🔍 CLAIMS ANALYSIS:

Claim 1: ❌ FALSE  
  Statement: "The Great Wall of China is visible from the moon."  
  Explanation: The Great Wall of China is not visible from the moon with the naked eye. NASA astronauts have confirmed this, including Neil Armstrong who stated he could not see the Wall from lunar orbit. The Wall is too narrow and is similar in color to its surroundings when viewed from such a distance.  
  Sources:
    - NASA.gov
    - Scientific American
    - National Geographic
```

## Limitations

* The accuracy of fact-checking depends on the quality of information available through the Perplexity Sonar API.
* Like all language models, the underlying AI may have limitations in certain specialized domains.
* The structured outputs feature requires a Tier 3 or higher Perplexity API account.
* The tool does not replace professional fact-checking services for highly sensitive or complex content.


# Financial News Tracker
Source: https://docs.perplexity.ai/docs/cookbook/examples/financial-news-tracker/README

A real-time financial news monitoring tool that fetches and analyzes market news using Perplexity's Sonar API

# Financial News Tracker

A command-line tool that fetches and analyzes real-time financial news using Perplexity's Sonar API. Get comprehensive market insights, news summaries, and investment analysis for any financial topic.

## Features

* Real-time financial news aggregation from multiple sources
* Market sentiment analysis (Bullish/Bearish/Neutral)
* Impact assessment for news items (High/Medium/Low)
* Sector and company-specific analysis
* Investment insights and recommendations
* Customizable time ranges (24h to 1 year)
* Structured JSON output support
* Beautiful emoji-enhanced CLI output

## Installation

### 1. Install required dependencies

```bash theme={null}
# Install from requirements file (recommended)
pip install -r requirements.txt

# Or install manually
pip install requests pydantic
```

### 2. Make the script executable

```bash theme={null}
chmod +x financial_news_tracker.py
```

## API Key Setup

The tool requires a Perplexity API key. You can provide it in one of these ways:

### 1. As an environment variable (recommended)

```bash theme={null}
export PPLX_API_KEY=YOUR_API_KEY
```

### 2. As a command-line argument

```bash theme={null}
./financial_news_tracker.py "tech stocks" --api-key YOUR_API_KEY
```

### 3. In a file

Create a file named `pplx_api_key` or `.pplx_api_key` in the same directory:

```bash theme={null}
echo "YOUR_API_KEY" > .pplx_api_key
chmod 600 .pplx_api_key
```

## Quick Start

Get the latest tech stock news:

```bash theme={null}
./financial_news_tracker.py "tech stocks"
```

This will fetch recent financial news about tech stocks, analyze market sentiment, and provide actionable insights.

## Usage Examples

### Basic usage - Get news for a specific topic

```bash theme={null}
./financial_news_tracker.py "S&P 500"
```

### Get cryptocurrency news from the past week

```bash theme={null}
./financial_news_tracker.py "cryptocurrency" --time-range 1w
```

### Track specific company news

```bash theme={null}
./financial_news_tracker.py "AAPL Apple stock"
```

### Get news about market sectors

```bash theme={null}
./financial_news_tracker.py "energy sector oil prices"
```

### Output as JSON for programmatic use

```bash theme={null}
./financial_news_tracker.py "inflation rates" --json
```

### Use a different model

```bash theme={null}
./financial_news_tracker.py "Federal Reserve interest rates" --model sonar
```

### Enable structured output (requires Tier 3+ API access)

```bash theme={null}
./financial_news_tracker.py "tech earnings" --structured-output
```

## Time Range Options

* `24h` - Last 24 hours (default)
* `1w` - Last week
* `1m` - Last month
* `3m` - Last 3 months
* `1y` - Last year

## Output Format

The tool provides comprehensive financial analysis including:

### 1. Executive Summary

A brief overview of the key financial developments

### 2. Market Analysis

* **Market Sentiment**: Overall market mood (🐂 Bullish, 🐻 Bearish, ⚖️ Neutral)
* **Key Drivers**: Factors influencing the market
* **Risks**: Current market risks and concerns
* **Opportunities**: Potential investment opportunities

### 3. News Items

Each news item includes:

* **Headline**: The main news title
* **Impact**: Market impact level (🔴 High, 🟡 Medium, 🟢 Low)
* **Summary**: Brief description of the news
* **Affected Sectors**: Industries or companies impacted
* **Source**: News source attribution

### 4. Investment Insights

Actionable recommendations and analysis based on the news

## Example Output

```
📊 FINANCIAL NEWS REPORT: tech stocks
📅 Period: Last 24 hours

📝 EXECUTIVE SUMMARY:
Tech stocks showed mixed performance today as AI-related companies surged while 
semiconductor stocks faced pressure from supply chain concerns...

📈 MARKET ANALYSIS:
  Sentiment: 🐂 BULLISH

  Key Drivers:
    • Strong Q4 earnings from major tech companies
    • AI sector momentum continues
    • Federal Reserve signals potential rate cuts

  ⚠️ Risks:
    • Semiconductor supply chain disruptions
    • Regulatory scrutiny on big tech
    • Valuation concerns in AI sector

  💡 Opportunities:
    • Cloud computing growth
    • AI infrastructure plays
    • Cybersecurity demand surge

📰 KEY NEWS ITEMS:

1. Microsoft Hits All-Time High on AI Growth
   Impact: 🔴 HIGH
   Summary: Microsoft stock reached record levels following strong Azure AI revenue...
   Sectors: Cloud Computing, AI, Software
   Source: Bloomberg

💼 INSIGHTS & RECOMMENDATIONS:
  • Consider diversifying within tech sector
  • AI infrastructure companies show strong momentum
  • Monitor semiconductor sector for buying opportunities
```

## Advanced Features

### Custom Queries

You can combine multiple topics for comprehensive analysis:

```bash theme={null}
# Get news about multiple related topics
./financial_news_tracker.py "NVIDIA AMD semiconductor AI chips"

# Track geopolitical impacts on markets
./financial_news_tracker.py "oil prices Middle East geopolitics"

# Monitor economic indicators
./financial_news_tracker.py "inflation CPI unemployment Federal Reserve"
```

### JSON Output

For integration with other tools or scripts:

```bash theme={null}
./financial_news_tracker.py "bitcoin" --json | jq '.market_analysis.market_sentiment'
```

## Tips for Best Results

1. **Be Specific**: Include company tickers, sector names, or specific events
2. **Combine Topics**: Mix company names with relevant themes (e.g., "TSLA electric vehicles")
3. **Use Time Ranges**: Match the time range to your investment horizon
4. **Regular Monitoring**: Set up cron jobs for daily market updates

## Limitations

* Results depend on available public information
* Not financial advice - always do your own research
* Historical data may be limited for very recent events
* Structured output requires Tier 3+ Perplexity API access

## Error Handling

The tool includes comprehensive error handling for:

* Invalid API keys
* Network connectivity issues
* API rate limits
* Invalid queries
* Parsing errors

## Integration Examples

### Daily Market Report

Create a script for daily updates:

```bash theme={null}
#!/bin/bash
# daily_market_report.sh

echo "=== Daily Market Report ===" > market_report.txt
echo "Date: $(date)" >> market_report.txt
echo "" >> market_report.txt

./financial_news_tracker.py "S&P 500 market overview" >> market_report.txt
./financial_news_tracker.py "top gaining stocks" >> market_report.txt
./financial_news_tracker.py "cryptocurrency bitcoin ethereum" >> market_report.txt
```

### Python Integration

```python theme={null}
import subprocess
import json

def get_financial_news(query, time_range="24h"):
    result = subprocess.run(
        ["./financial_news_tracker.py", query, "--time-range", time_range, "--json"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        raise Exception(f"Error fetching news: {result.stderr}")

# Example usage
news = get_financial_news("tech stocks", "1w")
print(f"Market sentiment: {news['market_analysis']['market_sentiment']}")
```


# Academic Research Finder CLI
Source: https://docs.perplexity.ai/docs/cookbook/examples/research-finder/README

A command-line tool that uses Perplexity's Sonar API to find and summarize academic literature

# Academic Research Finder CLI

A command-line tool that uses Perplexity's Sonar API to find and summarize academic literature (research papers, articles, etc.) related to a given question or topic.

## Features

* Takes a natural language question or topic as input, ideally suited for academic inquiry.
* Leverages Perplexity Sonar API, guided by a specialized prompt to prioritize scholarly sources (e.g., journals, conference proceedings, academic databases).
* Outputs a concise summary based on the findings from academic literature.
* Lists the primary academic sources used, aiming to include details like authors, year, title, publication, and DOI/link when possible.
* Supports different Perplexity models (defaults to `sonar-pro`).
* Allows results to be output in JSON format.

## Installation

### 1. Install required dependencies

Ensure you are using the Python environment you intend to run the script with (e.g., `python3.10` if that's your target).

```bash theme={null}
# Install from requirements file (recommended)
pip install -r requirements.txt

# Or install manually
pip install requests
```

### 2. Make the script executable (Optional)

```bash theme={null}
chmod +x research_finder.py
```

Alternatively, you can run the script using `python3 research_finder.py ...`.

## API Key Setup

The tool requires a Perplexity API key (`PPLX_API_KEY`) to function. You can provide it in one of these ways (checked in this order):

1. **As a command-line argument:**
   ```bash theme={null}
   python3 research_finder.py "Your query" --api-key YOUR_API_KEY
   ```
2. **As an environment variable:**
   ```bash theme={null}
   export PPLX_API_KEY=YOUR_API_KEY
   python3 research_finder.py "Your query"
   ```
3. **In a file:** Create a file named `pplx_api_key`, `.pplx_api_key`, `PPLX_API_KEY`, or `.PPLX_API_KEY` in the *same directory as the script* or in the *current working directory* containing just your API key.
   ```bash theme={null}
   echo "YOUR_API_KEY" > .pplx_api_key
   chmod 600 .pplx_api_key # Optional: restrict permissions
   python3 research_finder.py "Your query"
   ```

## Usage

Run the script from the `sonar-use-cases/research_finder` directory or provide the full path.

```bash theme={null}
# Basic usage
python3 research_finder.py "What are the latest advancements in quantum computing?"

# Using a specific model
python3 research_finder.py "Explain the concept of Large Language Models" --model sonar-small-online

# Getting output as JSON
python3 research_finder.py "Summarize the plot of Dune Part Two" --json

# Using a custom system prompt file
python3 research_finder.py "Benefits of renewable energy" --prompt-file /path/to/your/custom_prompt.md

# Using an API key via argument
python3 research_finder.py "Who won the last FIFA World Cup?" --api-key sk-...

# Using the executable (if chmod +x was used)
./research_finder.py "Latest news about Mars exploration"
```

### Arguments

* `query`: (Required) The research question or topic (enclose in quotes if it contains spaces).
* `-m`, `--model`: Specify the Perplexity model (default: `sonar-pro`).
* `-k`, `--api-key`: Provide the API key directly.
* `-p`, `--prompt-file`: Path to a custom system prompt file.
* `-j`, `--json`: Output the results in JSON format.

## Example Output (Human-Readable - *Note: Actual output depends heavily on the query and API results*)

```
Initializing research assistant for query: "Recent studies on transformer models in NLP"...
Researching in progress...

✅ Research Complete!

📝 SUMMARY:
Recent studies on transformer models in Natural Language Processing (NLP) continue to explore architectural improvements, efficiency optimizations, and new applications. Key areas include modifications to the attention mechanism (e.g., sparse attention, linear attention) to handle longer sequences more efficiently, techniques for model compression and knowledge distillation, and applications beyond text, such as in computer vision and multimodal tasks. Research also focuses on understanding the internal workings and limitations of large transformer models.

🔗 SOURCES:
  1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. Advances in neural information processing systems, 30. (arXiv:1706.03762)
  2. Tay, Y., Dehghani, M., Bahri, D., & Metzler, D. (2020). Efficient transformers: A survey. arXiv preprint arXiv:2009.06732.
  3. Beltagy, I., Peters, M. E., & Cohan, A. (2020). Longformer: The long-document transformer. arXiv preprint arXiv:2004.05150.
  4. Rogers, A., Kovaleva, O., & Rumshisky, A. (2020). A primer in bertology: What we know about how bert works. Transactions of the Association for Computational Linguistics, 8, 842-866. (arXiv:2002.12327)
```

## Limitations

* The ability of the Sonar API to consistently prioritize and access specific academic databases or extract detailed citation information (like DOIs) may vary. The quality depends on the API's search capabilities and the structure of the source websites.
* The script performs basic parsing to separate summary and sources; complex or unusual API responses might not be parsed perfectly. Check the raw response in case of issues.
* Queries that are too broad or not well-suited for academic search might yield less relevant results.
* Error handling for API rate limits or specific API errors could be more granular.


# Perplexity API Cookbook
Source: https://docs.perplexity.ai/docs/cookbook/index

A collection of practical examples and guides for building with Perplexity's API Platform

A collection of practical examples and guides for building with [**Perplexity's API Platform**](https://docs.perplexity.ai/) - the fastest, most cost-effective AI answer engine with real-time search capabilities.

## Quick Start

To get started with any project in this cookbook:

1. **Browse examples** - Find the use case that matches your needs
2. **Follow the guide** - Each example includes complete setup instructions
3. **Get the code** - Full implementations are available in our [GitHub repository](https://github.com/perplexityai/api-cookbook)
4. **Build and customize** - Use the examples as starting points for your projects

## What's Inside

### [Examples](/docs/cookbook/examples/README)

Ready-to-run projects that demonstrate specific use cases and implementation patterns.

### [Showcase](/docs/cookbook/showcase/briefo/)

Community-built applications that demonstrate real-world implementations of the API Platform.

### [Integration Guides](/docs/cookbook/articles/memory-management/chat-summary-memory-buffer/README)

In-depth tutorials for advanced implementations and integrations with other tools.

> **Note**: All complete code examples, scripts, and project files can be found in our [GitHub repository](https://github.com/perplexityai/api-cookbook). The documentation here provides guides and explanations, while the repository contains the full runnable implementations.

## Contributing

Have a project built with API Platform? We'd love to feature it! Check our [Contributing Guidelines](https://github.com/perplexityai/api-cookbook/blob/main/CONTRIBUTING.md) to learn how to:

* Submit example tutorials
* Add your project to the showcase
* Improve existing content

## Resources

* [API Documentation](https://docs.perplexity.ai/home)
* [GitHub Repository](https://github.com/perplexityai/api-cookbook)

***

*Maintained by the Perplexity community*


# 4Point Hoops | AI Basketball Analytics Platform
Source: https://docs.perplexity.ai/docs/cookbook/showcase/4point-Hoops

Advanced NBA analytics platform that combines live Basketball-Reference data with Perplexity Sonar to deliver deep-dive player stats, cross-season comparisons and expert-grade AI explanations

![4Point Hoops Dashboard](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/003/442/047/datas/original.png)

**4Point Hoops** is an advanced NBA analytics platform that turns raw basketball statistics into actionable, narrative-driven insights. By scraping Basketball-Reference in real time and routing context-rich prompts to Perplexity's Sonar Pro model, it helps fans, analysts, and fantasy players understand the "why" and "what's next" – not just the numbers.

<iframe title="YouTube video player" />

## Features

* **Player Analytics** with season & playoff splits, shot-type breakdowns, and performance radar for any NBA player
* **Cross-Era Comparisons** enabling side-by-side stat comparisons (e.g., Michael Jordan '97 vs. Stephen Curry '22)
* **Team Dashboards** with standings, playoff-probability Sankey flows, and auto-refreshing KPI tiles
* **AI Explain & Similar Players** providing one-click Sonar explanations of stat lines and AI-picked comparable athletes
* **Basketball AI Chat** allowing users to ask an expert LLM about NBA history, rosters, or projections
* **Credit-Based SaaS System** with Firebase Auth, Google login, credit wallets, and admin tooling

## Prerequisites

* Node.js 16+ and npm
* Python 3.8+ and pip
* Firebase project setup
* Perplexity API key (Sonar Pro)
* Basketball-Reference access

## Installation

```bash theme={null}
# Clone the frontend repository
git clone https://github.com/rapha18th/hoop-ai-frontend-44.git
cd hoop-ai-frontend-44
npm install

# Clone the backend repository
git clone https://github.com/rapha18th/4Point-Hoops-Server.git
cd 4Point-Hoops-Server
pip install -r requirements.txt
```

## Configuration

Create `.env` file in the backend directory:

```ini theme={null}
PERPLEXITY_API_KEY=your_sonar_pro_api_key
FIREBASE_PROJECT_ID=your_firebase_project_id
FIREBASE_PRIVATE_KEY=your_firebase_private_key
FIREBASE_CLIENT_EMAIL=your_firebase_client_email
```

## Usage

1. **Start Backend**:
   ```bash theme={null}
   cd 4Point-Hoops-Server
   python app.py
   ```

2. **Start Frontend**:
   ```bash theme={null}
   cd hoop-ai-frontend-44
   npm run dev
   ```

3. **Access Application**: Open the frontend URL and explore NBA analytics with AI-powered insights

4. **Use AI Features**: Click "AI Explain" on any player or stat to get intelligent analysis powered by Perplexity Sonar

## Code Explanation

* **Frontend**: React with shadcn/ui components and Recharts for data visualization
* **Backend**: Python Flask API serving Basketball-Reference data and managing Perplexity API calls
* **Data Pipeline**: BRScraper for real-time data collection with Firebase caching
* **AI Integration**: Perplexity Sonar Pro for intelligent basketball analysis and explanations
* **Authentication**: Firebase Auth with Google login and credit-based access control
* **Deployment**: Frontend on Netlify, backend on Hugging Face Spaces with Docker

## Links

* [Frontend Repository](https://github.com/rapha18th/hoop-ai-frontend-44)
* [Backend Repository](https://github.com/rapha18th/4Point-Hoops-Server)
* [Live Demo](https://4pointhoops.netlify.app/)
* [Devpost Submission](https://devpost.com/software/4point-hoops)


# Ellipsis | One-Click Podcast Generation Agent
Source: https://docs.perplexity.ai/docs/cookbook/showcase/Ellipsis

A next-gen podcast generation agent that brings human-like, high-quality audio content to life on any topic with just one click

**Ellipsis** is a next-generation podcast generation agent that brings human-like, high-quality audio content to life on any topic with just one click. Whether it's breaking news, deep-dive tech explainers, movie reviews, or post-match sports breakdowns, Ellipsis crafts intelligent podcast episodes that sound like they were created by seasoned hosts in a professional studio.

## Features

* **Intelligent Multi-Speaker Dialogue** with multiple distinct voices and personalities
* **Comprehensive Topic Coverage** from LLM architectures to lunar eclipses
* **Custom Evaluation Engine** ensuring factual accuracy, legal compliance, and conversational quality
* **Fully Automated Podcast Generation** with human-like, podcast-ready audio output
* **Real-time Streaming Updates** via Server-Sent Events (SSE)
* **Podbean Integration** for direct podcast publishing
* **Trending Topics Detection** using Perplexity API

## Prerequisites

* Node.js v16+ and npm/yarn
* Python 3.10+ and pip
* Redis server running (default on port 6380)
* Perplexity API key, Podbean credentials

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/dineshkannan010/Ellipsis.git
cd Ellipsis

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate    # macOS/Linux
pip install -r requirements.txt

# Install native packages
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
pip install git+https://github.com/freddyaboulton/orpheus-cpp.git
pip install huggingface_hub[hf_xet] hf_xet

# Frontend setup
cd ../frontend
npm install
```

## Configuration

Create `backend/.env`:

```ini theme={null}
REDIS_URL=redis://your-redis-host:6379
PERPLEXITY_API_KEY=your_key_here
PODBEAN_CLIENT_ID=...
PODBEAN_CLIENT_SECRET=...
```

Create `frontend/.env`:

```ini theme={null}
REACT_APP_API_URL=http://your-backend-host:5000
```

## Usage

1. **Start Redis Server**:
   ```bash theme={null}
   redis-server --port 6380
   ```

2. **Launch Backend**:
   ```bash theme={null}
   cd backend
   python app.py
   ```

3. **Launch Frontend**:
   ```bash theme={null}
   cd frontend
   npm run dev
   ```

4. **Optional: Podbean Integration**:
   ```bash theme={null}
   cd backend/integrations/podbean_mcp
   pip install -e .
   python server.py
   python client.py server.py
   ```

5. **Generate Content**: Enter a topic in the homepage textbox and hit Enter. Switch to `ContentGenerationView` to see live script & audio progress.

## Code Explanation

* **Backend**: Python Flask with Redis pub/sub, llama.cpp, and Orpheus TTS for audio generation
* **Frontend**: React with Vite, Tailwind CSS, and Server-Sent Events for real-time updates
* **AI Integration**: Perplexity API for content generation and trending topics detection
* **Audio Processing**: Multi-speaker TTS with distinct voice personalities
* **Content Evaluation**: Built-in pipelines for factual accuracy and legal compliance
* **Podcast Publishing**: Direct integration with Podbean via MCP server

## Demo Video

<iframe title="YouTube video player" />

## Links

* [GitHub Repository](https://github.com/dineshkannan010/Ellipsis)
* [Devpost Submission](https://devpost.com/software/ellipsis)


# BazaarAISaathi | AI-Powered Indian Stock Market Assistant
Source: https://docs.perplexity.ai/docs/cookbook/showcase/bazaar-ai-saathi

An AI-powered platform for Indian stock market analysis, portfolio optimization, and investment strategies using Perplexity Sonar API

**BazaarAISaathi** is an AI-powered platform designed to empower investors with actionable insights into the Indian stock market. Leveraging advanced natural language processing, real-time data analytics, and expert-driven financial modeling, the app delivers personalized investment strategies, market sentiment analysis, and portfolio optimization recommendations.

## Features

* **Financial Independence Planner (FIRE)** with personalized plans based on age, salary, and goals
* **Investment Advice Tester** using EasyOCR for text extraction and AI validation
* **Fundamental & Technical Analysis** with comprehensive company reports and trading strategies
* **Portfolio Analysis** with multi-dimensional analysis and stock-wise recommendations
* **Market Research & Competitor Benchmarking** using AI-driven industry trend analysis
* **Real-Time Stock Data** with live price tracking and trend analysis
* **Hypothesis Testing** using historical and real-time market data
* **Investment Books Summary** with concise summaries of top 50 investment books

## Prerequisites

* Python 3.8+ and pip
* Streamlit for web application framework
* Perplexity API key (Sonar models)
* Optional: EasyOCR for image text extraction

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/mahanteshimath/BazaarAISaathi.git
cd BazaarAISaathi

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create `secrets.toml` file for Streamlit secrets:

```ini theme={null}
PERPLEXITY_API_KEY = "your_perplexity_api_key"
# Add other API keys as needed
```

## Usage

1. **Start the Application**:
   ```bash theme={null}
   streamlit run Home.py
   ```

2. **Access Features**:
   * Navigate through different pages for specific functionality
   * Use the main dashboard for overview and navigation
   * Access specialized tools like portfolio analysis, FIRE planning, and tip testing

3. **Run Specific Modules**:
   ```bash theme={null}
   streamlit run pages/Financial_Independence.py
   streamlit run pages/Portfolio_Analysis.py
   streamlit run pages/Tip_Tester.py
   ```

## Code Explanation

* **Frontend**: Streamlit web application with interactive pages and real-time data visualization
* **Backend**: Python-based business logic with Pandas for data manipulation and analysis
* **AI Integration**: Perplexity Sonar API models (sonar-deep-research, sonar-reasoning-pro, sonar-pro) for financial analysis
* **Data Processing**: Real-time stock data fetching, CSV data management, and market insights generation
* **Text Extraction**: EasyOCR integration for processing investment tips from images
* **Portfolio Management**: Comprehensive portfolio analysis with optimization recommendations
* **Market Analysis**: Technical and fundamental analysis with sentiment scoring

## Demo Video

<iframe title="YouTube video player" />

## Links

* [GitHub Repository](https://github.com/mahanteshimath/BazaarAISaathi)
* [Live Application](https://bazaar-ai-saathi.streamlit.app/)
* [Architecture Diagram](https://github.com/mahanteshimath/BazaarAISaathi/raw/main/src/App_Architecture.jpg)


# Briefo | Perplexity Powered News & Finance Social App
Source: https://docs.perplexity.ai/docs/cookbook/showcase/briefo

AI curated newsfeed, social discussion, and deep research reports built on the Sonar API

# Briefo | Perplexity Powered News & Finance Social App

**Briefo** delivers a personalized, AI generated newsfeed and company deep dives. Readers can follow breaking stories, request on demand financial analyses, and discuss insights with friends, all in one mobile experience powered by Perplexity’s Sonar API.

## Features

* Personalized newsfeed across 17 categories with AI summaries and source links
* Private and public threads for article discussion and sharing
* Watch list with real time market snapshots and optional AI analyses
* Deep research reports generated on 12 selectable criteria such as management, competitors, and valuation
* General purpose chat assistant that remembers each user’s preferred topics

## Prerequisites

* Node 18 LTS or newer
* npm, Yarn, or pnpm
* Expo CLI (`npm i -g expo-cli`)
* Supabase CLI 1.0 or newer for local emulation and Edge Function deploys

## Installation

```bash theme={null}
git clone https://github.com/adamblackman/briefo-public.git
cd briefo-public
npm install
```

### Environment variables

```ini theme={null}
# .env              (project root)
MY_SUPABASE_URL=https://<project>.supabase.co
MY_SUPABASE_SERVICE_ROLE_KEY=...
PERPLEXITY_API_KEY=...
LINKPREVIEW_API_KEY=...
ALPACA_API_KEY=...
ALPACA_SECRET_KEY=...

# .env.local        (inside supabase/)
# duplicate or override any secrets needed by Edge Functions
```

## Usage

Run the Expo development server:

```bash theme={null}
npx expo start
```

Deploy Edge Functions when you are ready:

```bash theme={null}
supabase functions deploy perplexity-news perplexity-chat perplexity-research portfolio-tab-data
```

## Code Explanation

* Frontend: React Native with Expo Router (TypeScript) targeting iOS, Android, and Web
* Backend: Supabase (PostgreSQL, Row Level Security, Realtime) for data and authentication
* Edge Functions: TypeScript on Deno calling Perplexity, Alpaca, Alpha Vantage, and LinkPreview APIs
* Hooks: Reusable React Query style data hooks live in lib/ and hooks/
* Testing and Linting: ESLint, Prettier, and Expo Lint maintain code quality

## Links

[GitHub Repository](https://github.com/adamblackman/briefo-public)
[Live Demo](https://www.briefo.fun/)


# CityPulse | AI-Powered Geospatial Discovery Search
Source: https://docs.perplexity.ai/docs/cookbook/showcase/citypulse-ai-search

Real-time local discovery search using Perplexity AI for personalized location insights and recommendations

# CityPulse - AI-Powered Geospatial Discovery

![CityPulse Main Interface](https://raw.githubusercontent.com/anevsky/CityPulse/main/assets/CityPulse-GeoSearch-App-1.jpg)

CityPulse is an intelligent location-based discovery search that helps users explore what's happening around them right now. It demonstrates how to create personalized, real-time local insights using Perplexity's Sonar models.

[![Demo Video](https://cdn.loom.com/sessions/thumbnails/6507fa27571442e680edf787b0f0690d-2fa2c36169822631-full-play.gif)](https://youtu.be/Y0UIhh3diJg)

## What CityPulse Does

* **Real-time local discovery** - Find current events, restaurants, and local alerts near any location
* **AI-powered search suggestions** - Get intelligent search recommendations as you type
* **Personalized insights** - Receive AI-generated advice on what to try, best times to visit, and pro tips
* **Interactive mapping** - Explore results on an interactive map with custom markers and detailed popups

![Search Interface](https://raw.githubusercontent.com/anevsky/CityPulse/main/assets/CityPulse-GeoSearch-App-2.jpg)

## How It Uses Perplexity Sonar

CityPulse leverages two key Perplexity models:

**Sonar for Real-Time Data**

```python theme={null}
# Get current local information with geographic context
response = client.chat.completions.create(
    model="sonar",
    messages=[{
        "role": "user", 
        "content": f"Find current events, restaurants, and alerts near {lat}, {lng}"
    }],
    response_format={"type": "json_schema", "json_schema": {"schema": LOCAL_INFO_SCHEMA}}
)
```

**Sonar Reasoning Pro for Personalized Insights**

```python theme={null}
# Generate AI-powered location recommendations
response = client.chat.completions.create(
    model="sonar-reasoning-pro",
    messages=[{
        "role": "user",
        "content": f"Provide personalized insights for {location_name}: what to try, best times to visit, pro tips"
    }]
)
```

The app uses structured JSON schemas to ensure consistent data formatting and includes citation tracking for source verification.

![AI Insights](https://raw.githubusercontent.com/anevsky/CityPulse/main/assets/CityPulse-GeoSearch-App-3.jpg)

## Links

* [GitHub Repository](https://github.com/anevsky/CityPulse)
* [Live Demo](https://citypulse-ppx.uc.r.appspot.com/)
* **[Built with ❤️ by Alex Nevsky](https://alexnevsky.com)**


# CycleSyncAI | Personalized Health Plans Powered by Sonar API
Source: https://docs.perplexity.ai/docs/cookbook/showcase/cycle-sync-ai

iOS app that delivers personalized diet and workout recommendations for women, powered by Apple HealthKit and Perplexity's Sonar Pro API.

**CycleSyncAI** is an iOS app designed to provide personalized **diet and workout recommendations** tailored to a woman's **menstrual cycle phase**.

By integrating menstrual data from Apple **HealthKit** and optional user profile inputs (age, weight, height, medical conditions, dietary restrictions, goals, and preferences), the app generates dynamic, phase-aware suggestions to support holistic wellness.

Unlike static wellness tools, **CycleSyncAI** leverages **Perplexity's Sonar Pro API** to deliver **expert-informed**, LLM-generated guidance — including a daily grocery list and motivational feedback — customized to the user's cycle and lifestyle.

## Problem & Solution

> **Why it matters:**\
> Most apps overlook the hormonal changes that affect women's fitness and nutrition needs across their cycle, leaving users with generic advice.

**CycleSyncAI** bridges this gap by combining Apple HealthKit data with Sonar Pro's LLM to generate **adaptive, cycle-aware recommendations** for better health outcomes.

## Features

* **Personalized diet & workout suggestions** per cycle phase
* Syncs with Apple HealthKit for real-time cycle tracking
* User profile inputs for advanced personalization (age, goals, restrictions, etc.)
* **Auto-generated daily grocery list**
* Smooth, modern UI with gradients and subtle animations
* **Motivational AI feedback** tailored to user preferences
* Local data storage and private processing

## Motivation

> "I wanted a tailored regime for myself and couldn't find it all in one place."

**CycleSyncAI** was born from the need for a science-backed, easy-to-use app that adapts wellness guidance to women's natural hormonal rhythms, something missing in most mainstream fitness and nutrition platforms.

## Repository Structure

```text theme={null}
CycleSyncAI.xcodeproj          → Xcode project file  
CycleSyncAI/                   → Source code  
├── EatPlanViewController.swift        → Diet plan generation & display  
├── WorkoutPlanViewController.swift    → Workout plan generation & display  
├── HomepageViewController.swift       → Navigation & main screen  
├── UserProfileViewController.swift    → Input & storage of user data  
├── HealthManager.swift                → Apple HealthKit menstrual data  
├── UserProfile.swift                  → Local profile model  
Main.storyboard               → App UI & layout  
Assets.xcassets              → Images & app icons  
Info.plist                   → Permissions & configurations  
```

## Setup Instructions

1. Clone the repo
2. Open in **Xcode**
3. Ensure Apple HealthKit is enabled on your device
4. Insert your **Sonar Pro API key**
5. Run the app on a physical device (recommended)

## Sonar API Usage

The app sends structured prompts to the **Sonar Pro API** including:

* Cycle phase (from HealthKit)
* User profile info (age, weight, goals, etc.)
* Meal preferences & restrictions

In return, it receives:

* **Personalized diet plan**
* **Custom workout plan**
* **Daily grocery list**
* **Motivational feedback**

These are parsed and rendered as styled HTML inside the app using WebViews.

## Demo Video

<iframe title="YouTube video player" />

> *Note: The LLM takes \~30–60 seconds per request. This wait time was trimmed in the video for brevity.*

## Impact

**CycleSyncAI** empowers women to make informed, body-aware decisions in daily life. The app supports better:

* Energy management
* Fitness results
* Mental well-being
* Motivation and confidence

It also reduces decision fatigue with automatically prepared grocery lists and uplifting guidance.

## Links

* [GitHub Repository](https://github.com/medhini98/cyclesyncai-api-cookbook)


# Daily News Briefing | AI-Powered News Summaries for Obsidian
Source: https://docs.perplexity.ai/docs/cookbook/showcase/daily-news-briefing

An Obsidian plugin that delivers AI-powered daily news summaries directly to your vault using Perplexity's Sonar API for intelligent content curation

**Daily News Briefing** is an Obsidian plugin that delivers AI-powered news summaries directly to your vault. Stay informed about your topics of interest with smart, automated news collection and summarization using Perplexity's Sonar API for intelligent content curation.

<iframe title="Daily News Briefing Demo" />

## Features

* **Personalized News Collection** based on your topics of interest and preferences
* **AI-Powered Summarization** of news articles using Perplexity Sonar API
* **Automated Daily Briefings** delivered directly to your Obsidian vault
* **Customizable Delivery Schedule** and format options
* **Seamless Obsidian Integration** with your existing knowledge management workflow
* **Trusted Source Filtering** to ensure quality and reliability
* **Markdown Formatting** for easy linking and organization within your vault

## Prerequisites

* Obsidian desktop app installed
* Perplexity API key (Sonar API access)
* Internet connection for fetching news articles
* TypeScript development environment (for customization)

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/ChenziqiAdam/Daily-News-Briefing.git
cd Daily-News-Briefing

# Install dependencies
npm install

# Build the plugin
npm run build
```

## Configuration

1. **Install Plugin**: Copy the built plugin to your Obsidian plugins folder
2. **Enable Plugin**: Activate in Obsidian settings
3. **API Setup**: Enter your Perplexity API key in plugin settings
4. **Configure Topics**: Set up your news topics and delivery preferences

## Usage

1. **Configure Interests**: Set up preferred topics, sources, and delivery schedule
2. **Automated Collection**: Plugin uses Perplexity Sonar API to gather latest news
3. **AI Summarization**: Articles are processed and summarized using Perplexity's capabilities
4. **Vault Delivery**: Summaries are formatted as Markdown notes in your Obsidian vault
5. **Knowledge Integration**: Link news briefings with other notes in your knowledge base

## Code Explanation

* **Frontend**: TypeScript-based Obsidian plugin with custom UI components
* **AI Integration**: Perplexity Sonar API for intelligent news gathering and summarization
* **Content Processing**: Automated article extraction and summarization workflows
* **Scheduling**: Configurable delivery schedules and topic monitoring
* **Markdown Generation**: Structured content formatting for Obsidian compatibility
* **Error Handling**: Robust error management for API limits and network issues

## Technical Implementation

The plugin leverages Perplexity Sonar API for:

```typescript theme={null}
// News gathering with Perplexity Sonar API
const newsQuery = `latest news about ${topic} in the past 24 hours`;
const searchResponse = await perplexityClient.search({
  query: newsQuery,
  max_results: 5,
  include_domains: userPreferences.trustedSources || []
});

// AI-powered summarization
const summaryPrompt = `Summarize these news articles about ${topic}`;
const summaryResponse = await perplexityClient.generate({
  prompt: summaryPrompt,
  model: "sonar-medium-online",
  max_tokens: 500
});
```

## Links

* [GitHub Repository](https://github.com/ChenziqiAdam/Daily-News-Briefing)


# Executive Intelligence | AI-Powered Strategic Decision Platform
Source: https://docs.perplexity.ai/docs/cookbook/showcase/executive-intelligence

A comprehensive Perplexity Sonar-powered application that provides executives and board members with instant, accurate, and credible intelligence for strategic decision-making

**Executive Intelligence** is a comprehensive Perplexity Sonar-powered application that provides executives and board members with instant, accurate, and credible intelligence for strategic decision-making. It delivers board-ready insights derived from real-time data sources, powered by Perplexity's Sonar API.

<iframe title="YouTube video player" />

## Features

* **Competitive Intelligence Briefs** with comprehensive, board-ready competitive analysis and verifiable citations
* **Scenario Planning ("What If?" Analysis)** for dynamic future scenario generation based on real-time data
* **Board Pack Memory** for saving and organizing intelligence briefs, scenario analyses, and benchmark reports
* **Instant Benchmarking & Peer Comparison** with source-cited visual comparisons across critical metrics
* **Real-time Data Integration** leveraging Perplexity Sonar API for up-to-date market intelligence
* **Professional Formatting** with structured reports, executive summaries, and board-ready presentations

## Prerequisites

* Node.js 18+ and npm/yarn
* Git
* Perplexity API key (Sonar Pro)

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/raishs/perplexityhackathon.git
cd perplexityhackathon

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
```

## Configuration

Create `.env.local` file:

```ini theme={null}
PERPLEXITY_API_KEY=your_perplexity_api_key
```

## Usage

1. **Start Development Server**:
   ```bash theme={null}
   npm run dev
   ```

2. **Access Application**: Open [http://localhost:3000](http://localhost:3000) in your browser

3. **Generate Intelligence**:
   * Enter a company name in the input field
   * Click "Competitive Analysis" for comprehensive briefs
   * Use "Scenario Planning" for "what-if" analysis
   * Access "Benchmarking" for peer comparisons
   * Save reports to "Board Pack" for later access

4. **Board Pack Management**: Use the "📁 Board Pack" button to view and manage saved intelligence reports

## Code Explanation

* **Frontend**: Next.js with TypeScript and React for modern, responsive UI
* **Backend**: Next.js API routes handling Perplexity Sonar API integration
* **AI Integration**: Perplexity Sonar Pro for real-time competitive intelligence and scenario analysis
* **State Management**: React Context for boardroom memory and persistent data storage
* **Markdown Processing**: Custom utilities for parsing AI responses and citation handling
* **Error Handling**: Comprehensive timeout and error management for API calls
* **Professional Output**: Structured formatting for board-ready presentations with source citations

## Links

* [GitHub Repository](https://github.com/raishs/perplexityhackathon)


# Fact Dynamics | Real-time Fact-Checking Flutter App
Source: https://docs.perplexity.ai/docs/cookbook/showcase/fact-dynamics

Cross-platform app for real-time fact-checking of debates, speeches, and images using Perplexity's Sonar API

# Fact Dynamics | Real-time Fact-Checking Flutter App

<p>
  <img alt="Fact Dynamics logo" />
</p>

**Hackathon Submission** - Built for Perplexity Hackathon in Information Tools & Deep Research categories.

Fact Dynamics is a cross-platform Flutter app that provides real-time fact-checking for spoken content and images. Perfect for live debates, presentations, and on-the-fly information verification.

## Features

* Real-time speech transcription and fact-checking during live conversations

* Image text extraction and claim verification with source citations

* Claim rating system (TRUE, FALSE, MISLEADING, UNVERIFIABLE) with explanations

* Source citations - Provides authoritative URLs backing each verdict

* Debate mode with continuous speech recognition and streaming feedback

* User authentication via Firebase (Google, Email) with persistent chat history

* Cross-platform support for iOS, Android, and Web

## Prerequisites

* Flutter SDK 3.0.0 or newer
* Dart SDK 2.17.0 or newer
* Firebase CLI for authentication and database setup
* Perplexity API key for Sonar integration
* Device with microphone access for speech recognition

## Installation (Follow Detailed guideline on the Repository)

```bash theme={null}
git clone https://github.com/vishnu32510/fact_pulse.git
cd fact_pulse
flutter pub get
```

## Usage

### Real-time Speech Fact-Checking

* Streams 5-second audio chunks through Flutter's `speech_to_text`
* Sends transcribed snippets to Sonar API with structured prompts
* Returns JSON with claims, ratings (TRUE/FALSE/MISLEADING/UNVERIFIABLE), explanations, and sources

### Image Analysis

* Uploads images/URLs to Sonar API for text extraction
* Verifies extracted claims against authoritative sources
* Provides comprehensive analysis with source attribution

## Screenshots

<table>
  <tr>
    <td>
      <img alt="Dashboard" />
    </td>

    <td>
      <img alt="Fact checking interface" />
    </td>
  </tr>
</table>

## Code Explanation

* Frontend: Flutter with BLoC pattern for state management targeting iOS, Android, and Web
* Backend: Firebase (Firestore, Authentication) for user data and chat history persistence
* Speech Processing: speech\_to\_text package for real-time audio transcription
* API Integration: Custom Dart client calling Perplexity Sonar API with structured prompts
* Image Processing: Built-in image picker with base64 encoding for multimodal analysis
* Data Architecture: Firestore collections per user with subcollections for debates, speeches, and images

## Open Source SDKs

Built two reusable packages for the Flutter community:

* **[perplexity\_dart](https://pub.dev/packages/perplexity_dart)** - Core Dart SDK for Perplexity API
* **[perplexity\_flutter](https://pub.dev/packages/perplexity_flutter)** - Flutter widgets and BLoC integration

## Demo Video

<iframe title="YouTube video player" />

## Links

* **[GitHub Repository](https://github.com/vishnu32510/fact_pulse)** - Full source code
* **[Live Demo](https://fact-pulse.web.app/)** - Try the web version
* **[Devpost Submission](https://devpost.com/software/fact-dynamics)** - Hackathon entry


# FirstPrinciples | AI Learning Roadmap Generator
Source: https://docs.perplexity.ai/docs/cookbook/showcase/first-principle

An AI-powered learning roadmap generator that uses conversational AI to help users identify specific learning topics and provides personalized step-by-step learning plans

**FirstPrinciples App** is an AI-powered tool that transforms your broad learning goals into structured, personalized roadmaps. Through an interactive chat, the AI engages you in a conversation, asking targeted questions to refine your learning needs before generating a detailed plan. The application is built to help you learn more efficiently by providing a clear path forward.

<video />

## Features

* **Interactive Chat Interface** for defining and refining learning goals through conversation
* **AI-Powered Topic Narrowing** with smart, targeted questions to specify learning objectives
* **Session Management** allowing multiple roadmap discussions and progress tracking
* **Visual Progress Indicators** showing when sufficient information has been gathered
* **Personalized Learning Plans** with structured, step-by-step roadmaps
* **Conversational AI Flow** combining OpenAI and Perplexity APIs for intelligent interactions

## Prerequisites

* Python 3.8+ and pip
* Node.js 16+ and npm
* OpenAI API key
* Perplexity API key

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/william-Dic/First-Principle.git
cd First-Principle

# Backend setup
cd flask-server
pip install -r requirements.txt

# Frontend setup
cd ../client
npm install
```

## Configuration

Create `.env` file in the `flask-server` directory:

```ini theme={null}
OPENAI_API_KEY=your_openai_api_key
PPLX_API_KEY=your_perplexity_api_key
PERPLEXITY_API_KEY=your_perplexity_api_key
```

## Usage

1. **Start Backend**:
   ```bash theme={null}
   cd flask-server
   python server.py
   ```
   Server runs on [http://localhost:5000](http://localhost:5000)

2. **Start Frontend**:
   ```bash theme={null}
   cd client
   npm start
   ```
   Client runs on [http://localhost:3000](http://localhost:3000)

3. **Generate Roadmap**:
   * Open [http://localhost:3000](http://localhost:3000) in your browser
   * Describe what you want to learn in the chat interface
   * Answer AI follow-up questions to refine your learning goals
   * Receive a personalized, structured learning roadmap

## Code Explanation

* **Frontend**: React application with conversational chat interface and progress indicators
* **Backend**: Flask server managing API calls, session state, and conversation flow
* **AI Integration**: Combines OpenAI API for conversational flow and Perplexity API for intelligent topic analysis
* **Session Management**: Tracks conversation state and learning goal refinement
* **Roadmap Generation**: Creates structured, actionable learning plans based on user input
* **Conversational Flow**: Implements goal-oriented dialogue to narrow down learning objectives

## Links

* [GitHub Repository](https://github.com/william-Dic/First-Principle.git)
* [Demo Video](https://github.com/user-attachments/assets/6016c5dd-6c18-415e-b982-fafb56170b87)


# FlameGuardAI | AI-powered wildfire prevention
Source: https://docs.perplexity.ai/docs/cookbook/showcase/flameguardai

AI-powered wildfire prevention using OpenAI Vision + Perplexity Sonar API

## 🧠 What it does

**FlameGuard AI™** helps homeowners, buyers, and property professionals detect and act on **external fire vulnerabilities** like wildfires or neighboring structure fires. It's more than a scan — it's a personalized research assistant for your home.

### Demo

<iframe title="YouTube video player" />

### Try it out

* [FlameGuard AI](https://flameguardai.dlyog.com)
* [FlameGuard AI MCP](https://flameguardai-mcp.dlyog.com)
* [GitHub Repo](https://github.com/dlyog/fire-risk-assessor-drone-ai)

### Key Features:

* 📸 Upload a home photo
* 👁️ Analyze visible fire risks via **OpenAI Vision API**
* 📚 Trigger deep research using the **Perplexity Sonar API**
* 📄 Get a detailed, AI-generated report with:
  * Risk summary
  * Prevention strategies
  * Regional best practices
* 🛠️ Optional contractor referrals for mitigation
* 💬 Claude (MCP) chatbot integration for conversational analysis
* 🧾 GDPR-compliant data controls

Whether you're protecting your home, buying a new one, or just want peace of mind — **FlameGuard AI™ turns a photo into a plan**.

## ⚙️ How it works

### The FlameGuard AI™ Process

1. **📸 Upload**: User uploads a photo of their property
2. **👁️ AI Vision Analysis**: OpenAI Vision API identifies specific vulnerabilities (e.g., flammable roof, dry brush nearby)
3. **🔍 Deep Research**: For each risk, we generate a **custom research plan** and run **iterative agentic-style calls** to Perplexity Sonar
4. **📄 Report Generation**: Research is **aggregated, organized, and formatted** into an actionable HTML report — complete with citations, links, and visual guidance
5. **📧 Delivery**: Detailed report sent via email with DIY solutions and professional recommendations

### 🔍 Deep Research with Perplexity Sonar API

The real innovation is how we use the **Perplexity Sonar API**:

* We treat it like a research assistant gathering the best available information
* Each vulnerability triggers multiple queries covering severity, mitigation strategies, and localized insights
* Results include regional fire codes, weather patterns, and local contractor availability

This kind of **structured, trustworthy, AI-powered research would not be possible without Perplexity**.

### Technical Stack

FlameGuard AI™ is powered by a modern GenAI stack and built to scale:

* **Frontend**: Lightweight HTML dashboard with user account control, photo upload, and report access
* **Backend**: Python (Flask) with RESTful APIs
* **Database**: PostgreSQL (local) with **Azure SQL-ready** schema
* **AI Integration**: OpenAI Vision API + Perplexity Sonar API
* **Cloud-ready**: Built for **Azure App Service** with Dockerized deployment

## 🏆 Accomplishments that we're proud of

* Successfully used **OpenAI Vision + Perplexity Sonar API** together in a meaningful, real-world workflow
* Built a functioning **MCP server** that integrates seamlessly with Claude for desktop users
* Created a product that is **genuinely useful for homeowners today** — not just a demo
* Kept the experience simple, affordable, and scalable from the ground up
* Made structured deep research feel accessible and trustworthy

## 📚 What we learned

* The **Perplexity Sonar API** is incredibly powerful when used agentically — not just for answers, but for reasoning.
* Combining **multimodal AI (image + research)** opens up powerful decision-support tools.
* Users want **actionable insights**, not just data — pairing research with guidance makes all the difference.
* Trust and clarity are key: our design had to communicate complex information simply and helpfully.

## 🚀 What's next for FlameGuard AI™ - Prevention is Better Than Cure

We're just getting started.

### Next Steps:

* 🌐 Deploy to **Azure App Services** with production-ready database
* 📱 Launch mobile version with location-based scanning
* 🏡 Partner with **home inspection services** and **homeowners associations**
* 💬 Enhance Claude/MCP integration with voice-activated AI reporting
* 💸 Introduce B2B plans for real estate firms and home safety consultants
* 🛡️ Expand database of **local contractor networks** and regional fire codes

We're proud to stand with homeowners — not just to raise awareness, but to enable action.

**FlameGuard AI™ – Because some homes survive when others don't.**

***

**Contact us to know more: [info@dlyog.com](mailto:info@dlyog.com)**


# Flow & Focus | Personalized News for Genuine Understanding
Source: https://docs.perplexity.ai/docs/cookbook/showcase/flow-and-focus

A personalized news app combining vertical feed discovery with AI-powered deep dives using Perplexity Sonar Pro and Deep Research models

**Flow & Focus** is a personalized news application that transforms news consumption into a learning experience. It uniquely combines rapid discovery through a vertical news feed (Flow) with in-depth, interactive learning dialogues (Focus), powered by Perplexity's Sonar Pro and Sonar Deep Research models.

<iframe title="YouTube video player" />

## Features

* **Dual Mode Interface**: Flow Feed for quick news discovery and Focus for personalized deep dives
* **Vertical News Feed**: Swipeable news snippets with AI-generated summaries, tags, and background images
* **Interactive Deep Dives**: Tap key phrases for focused content, with horizontally scrollable detail panes
* **Personalized Learning**: AI-powered conversation segments with personas like "Oracle" and "Explorer"
* **Smart Personalization**: Tracks reading patterns to tailor content selection automatically
* **Real-time Content**: Leverages Sonar Pro for up-to-date news and Sonar Deep Research for detailed analysis
* **Visual Enhancement**: Dynamic background images generated via Runware.ai based on content keywords

## Prerequisites

* Node.js 18+ and npm
* Perplexity API key
* Runware API key for image generation
* Next.js 15 and React 19 environment

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/michitomo/NewsReel.git
cd NewsReel

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
```

## Configuration

Create `.env.local` file:

```ini theme={null}
PERPLEXITY_API_KEY=your_perplexity_api_key_here
RUNWARE_API_KEY=your_runware_api_key_here
PERPLEXITY_FOCUS_MODEL=sonar-deep-research
```

## Usage

1. **Start Development Server**:
   ```bash theme={null}
   npm run dev
   ```

2. **Access Application**: Open [http://localhost:3000](http://localhost:3000) in your browser

3. **Flow Feed**: Scroll vertically through news snippets and tap key phrases for deep dives

4. **Focus Mode**: Generate personalized digests with interactive conversation segments

5. **Personalization**: Your viewing patterns automatically influence content selection

## Code Explanation

* **Frontend**: Next.js 15 with React 19, TypeScript, Tailwind CSS, and Framer Motion for animations
* **State Management**: Zustand with localStorage persistence for user preferences
* **AI Integration**: Perplexity Sonar Pro for real-time news and Sonar Deep Research for in-depth analysis
* **Image Generation**: Runware SDK integration for dynamic background images based on content keywords
* **API Routes**: Server-side integration handling Perplexity and Runware API calls
* **Mobile-First Design**: Swipe gestures and responsive layout for intuitive mobile experience

## Links

* [GitHub Repository](https://github.com/michitomo/NewsReel)
* [Demo Video](https://www.youtube.com/watch?v=09h7zluuhQI)
* [Perplexity Hackathon](https://perplexityhackathon.devpost.com/)
* [Perplexity Hackathon Project](https://devpost.com/software/flow-focus)


# Greenify | Localized community-driven greenification/plantation solution with AI
Source: https://docs.perplexity.ai/docs/cookbook/showcase/greenify

A mobile application that analyzes photos and location data to suggest suitable plants and build sustainable communities using Perplexity Sonar API

**Greenify** is a mobile application designed to encourage sustainable practices by analyzing live images and building communities. Users capture photos of their space (balcony, roadside, basement, etc.) and Greenify automatically analyzes the image using Perplexity's Sonar API to suggest suitable plants for that location. The app also connects like-minded people in the locality to create communities for sustainable, economic, and social growth.

<iframe title="YouTube video player" />

## Features

* **AI-Powered Plant Analysis** using image recognition and location data to suggest suitable plants
* **Location-Based Recommendations** considering weather, sunlight, and environmental conditions
* **Community Building** connecting users with similar plant interests and sustainable goals
* **Cross-Platform Mobile App** built with Expo for iOS, Android, and web
* **Real-time Weather Integration** for accurate plant suitability assessment
* **Structured JSON Output** using Pydantic models for consistent data handling
* **AR Model Support** for enhanced plant visualization

## Abstract Data Flow Diagram

![Abstract Data Flow Diagram](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/003/418/290/datas/gallery.jpg)

## Prerequisites

* Node.js 20.19.4+ and npm
* Python 3.10.0+ and pip
* Expo CLI and SDK 51+
* Perplexity API key (Sonar Pro and Sonar Deep Research)
* Android SDK/Studio or Xcode (for local builds)
* Mobile device with camera for image capture

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/deepjyotipaulhere/greenify.git
cd greenify

# Install frontend dependencies
npm install

# Install backend dependencies
cd service
pip install -r requirements.txt
```

## Configuration

Create `.env` file in the `service` directory:

```ini theme={null}
PPLX_API_KEY=your_perplexity_api_key_here
```

## Usage

1. **Start Backend Service**:
   ```bash theme={null}
   cd service
   python app.py
   ```

2. **Start Frontend App**:
   ```bash theme={null}
   npx expo start
   ```

3. **Access the App**:
   * Install Expo Go app and scan QR code, or
   * Open web browser on mobile and navigate to the URL shown

4. **Use the App**:
   * Grant camera and location permissions
   * Take a photo of your space (balcony, garden, etc.)
   * Receive AI-powered plant recommendations
   * Connect with nearby users for community building

![demo](https://raw.githubusercontent.com/deepjyotipaulhere/greenify/refs/heads/master/assets/images/ezgif-4647c5467e6dac.gif)

## Code Explanation

* **Frontend**: React Native with Expo for cross-platform mobile development
* **Backend**: Python Flask API handling image processing and Perplexity API integration
* **AI Integration**: Perplexity Sonar Pro for image analysis and Sonar Deep Research for plant recommendations
* **Data Models**: Pydantic models for structured JSON output and data validation
* **Image Processing**: Real-time image analysis with location-based context
* **Community Features**: User matching based on plant suggestions and sustainable interests
* **Weather Integration**: Real-time weather data for accurate plant suitability assessment

## Links

* [GitHub Repository](https://github.com/deepjyotipaulhere/greenify)
* [Live Demo](https://greenify.expo.app)


# Monday – Voice-First AI Learning Assistant
Source: https://docs.perplexity.ai/docs/cookbook/showcase/monday

An accessible, multimodal AI learning companion that delivers contextual reasoning, 3D visualizations, and curated educational content via natural voice interaction.

**Monday** is a voice-enabled AI learning companion designed to bridge the gap between natural language queries and high-quality educational content. Inspired by Marvel's JARVIS and FRIDAY, Monday delivers tailored responses in three modes—Basic, Reasoning, and Deep Research—while integrating immersive visualizations, curated video content, and accessibility-first design.

## Features

* **Three Learning Modes**: Basic factual answers, step-by-step reasoning, and deep research investigations
* **Voice-first interaction** for hands-free learning with natural language processing
* **Real-time 3D visualizations** of concepts using Three.js & WebXR
* **Curated educational YouTube video integration** from trusted sources
* **Multi-modal feedback** combining text, speech (via ElevenLabs), and spatial panels
* **VR-optional design** for immersive experiences without requiring a headset
* **Accessibility-focused interface** for mobility- and vision-impaired users

## Prerequisites

* Node.js 18 LTS or newer
* Modern web browser (Chrome, Edge, or Firefox recommended)
* Microphone for voice interaction
* Optional: VR headset for immersive mode (WebXR compatible)
* Perplexity API key, ElevenLabs API key, and YouTube API key

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/srivastavanik/monday.git
cd monday
git checkout final
cd nidsmonday

# Install dependencies
npm install
```

```ini theme={null}
# Create a .env file and set your API keys
PERPLEXITY_API_KEY=your_api_key
ELEVENLABS_API_KEY=your_api_key
YOUTUBE_API_KEY=your_api_key
```

```bash theme={null}
# Start Backend Server
node backend-server.js

# Start frontend
npm run dev
```

## Usage

1. Launch the app in your browser
2. Say **"Hey Monday"** to activate the assistant
3. Ask a question in one of three modes:
   * **Basic Mode** – "What is photosynthesis?"
   * **Reasoning Mode** – "Think about how blockchain works."
   * **Deep Research Mode** – "Research into the history of quantum mechanics."
4. View answers as floating text panels, voice responses, and interactive 3D models

## Code Explanation

* **Frontend**: TypeScript with Three.js for 3D visualizations and WebXR for VR support
* **Backend**: Node.js with Socket.IO for real-time voice command processing
* **AI Integration**: Perplexity Sonar API for intelligent responses with reasoning extraction
* **Voice Processing**: ElevenLabs for speech synthesis and natural language understanding
* **Content Curation**: YouTube API integration with smart keyword extraction for educational videos
* **Accessibility**: Voice-first design with spatial audio and haptic feedback support

## Demo Video

<iframe title="YouTube video player" />

## Links

* [GitHub Repository](https://github.com/srivastavanik/monday/tree/final)


# MVP LifeLine | AI Youth Empowerment Platform
Source: https://docs.perplexity.ai/docs/cookbook/showcase/mvp-lifeline-ai-app

A multilingual, offline-first AI platform that helps underserved youth Earn, Heal, and Grow using real-time AI and holistic tools

**MVP LifeLine** is a multilingual, offline-first AI platform empowering youth emotionally, financially, and professionally—anytime, anywhere. Over 1.3 billion youth globally face barriers to career opportunities and mental well-being, especially in underserved and remote regions. MVP LifeLine breaks these barriers by combining AI, offline access, multilingual support, and a holistic tool ecosystem.

## Features

* **Dual Mode AI** with Career Coach and Emotional Companion powered by Perplexity Sonar API
* **Multilingual Support** across 10+ languages including English, French, Arabic, Spanish, Hindi, and regional languages
* **Offline-First Design** with SMS/USSD integration for low-connectivity regions
* **Holistic Tool Ecosystem** covering career, wellness, finance, and productivity
* **SmartQ Access** for context-aware, emotionally intelligent AI responses
* **Digital Hustle Hub** with AI gig discovery and freelancing tools
* **Wellness Zone** with guided meditations and mental reset prompts
* **Finance Zone** with budget tracking and youth-friendly money tips
* **Productivity Zone** with AI Kanban board and habit tracking

## Prerequisites

* Flutter SDK and Dart
* Firebase project setup
* Twilio account for SMS/USSD integration
* Perplexity API key (Sonar)
* OpenAI API key (for augmentation)

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/JohnUmoh/asgard.git
cd asgard

# Install Flutter dependencies
flutter pub get

# Configure Firebase
flutterfire configure

# Set up environment variables
cp .env.example .env
```

## Configuration

Create `.env` file:

```ini theme={null}
PERPLEXITY_API_KEY=your_sonar_api_key
OPENAI_API_KEY=your_openai_api_key
FIREBASE_PROJECT_ID=your_firebase_project_id
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
```

## Usage

1. **Setup Firebase**:
   ```bash theme={null}
   flutterfire configure
   ```

2. **Run the Application**:
   ```bash theme={null}
   flutter run
   ```

3. **Access Features**:
   * Switch between Career Coach and Emotional Companion modes
   * Use SmartQ for AI-powered assistance in multiple languages
   * Access offline features via SMS/USSD when connectivity is limited
   * Explore career tools, wellness features, and productivity boosters

## Code Explanation

* **Frontend**: Flutter cross-platform application with responsive design for mobile and web
* **Backend**: Firebase for authentication, data storage, and real-time synchronization
* **AI Integration**: Perplexity Sonar API for dual-mode AI interactions (Career Coach & Emotional Companion)
* **Offline Support**: Twilio integration for SMS/USSD communication in low-connectivity areas
* **Multilingual**: Sonar API handling 10+ languages with context-aware responses
* **Data Sync**: Offline data capture with automatic re-sync when connectivity returns
* **Personalization**: AI adapts to user's language, literacy level, mood history, and preferences

## Links

* [GitHub Repository](https://github.com/JohnUmoh/asgard)
* [Live Demo](https://mvplifelineaiapp.netlify.app)


# PerplexiCart | AI-Powered Value-Aligned Shopping Assistant
Source: https://docs.perplexity.ai/docs/cookbook/showcase/perplexicart

An AI shopping assistant that uses Perplexity Sonar to deliver structured research, value-aligned recommendations, and transparent citations across the web

**PerplexiCart** helps users make informed, value-aligned purchasing decisions. Powered by the **Perplexity Sonar API**, it analyzes products across the web and returns structured insights with prioritized recommendations, pros/cons, trade‑off analysis, and user sentiment — tailored to preferences like Eco‑Friendly, Durability, Ethical, and region‑specific needs.

<iframe title="YouTube video player" />

## Features

* **Intelligent Product Recommendations** beyond simple spec comparison
* **Priority-Based Value Alignment** (Best Value, Eco‑Friendly, Ethical, Durability, Made in India)
* **Contextual Personalization** (skin type, usage patterns, region, etc.)
* **Structured Research Output** with:
  * Research summary and top recommendations
  * Value alignment with reasoning
  * Pros/Cons and key specifications
  * User sentiment and community insights (Reddit, Quora)
  * Trade‑off analysis and buying tips
* **Transparent Sources** with citations for verification

## Prerequisites

* Node.js 18+ and npm/yarn
* Python 3.10+ and pip
* Perplexity API key

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/fizakhan90/perplexicart.git
cd perplexicart

# Backend (FastAPI) setup
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Frontend (Next.js) setup
cd ../frontend
npm install
```

## Configuration

Create a `.env` file in the backend directory:

```ini theme={null}
PERPLEXITY_API_KEY=your_perplexity_api_key
```

(Optional) Add any app‑specific settings as needed (cache, region defaults, etc.).

## Usage

1. **Start Backend (FastAPI)**:
   ```bash theme={null}
   cd backend
   uvicorn main:app --reload  # adapt module:app if your entrypoint differs
   ```

2. **Start Frontend (Next.js)**:
   ```bash theme={null}
   cd frontend
   npm run dev
   ```

3. **Open the App**: Visit `http://localhost:3000` and search for a product. Select your priority (e.g., Eco‑Friendly) and add optional context (skin type, region).

## Code Explanation

* **Backend (FastAPI)**: Orchestrates Sonar calls with dynamic prompt engineering based on query, selected priority, and context
* **Structured Outputs**: Enforces a strict JSON schema via `response_format` to ensure consistent UI rendering
* **Live Web Research**: Directs Sonar to search e‑commerce platforms, forums, review blogs, and sustainability reports
* **Semantic Analysis**: Extracts value alignment, pros/cons, sentiment, and cites sources for transparency
* **Frontend (Next.js/React)**: Presents a clear, user‑friendly view of recommendations, trade‑offs, and citations

## How the Sonar API Is Used

PerplexiCart leverages the **Perplexity Sonar API** as its intelligence core, dynamically generating customized prompts based on user inputs like search queries, priorities and context. The API performs comprehensive web research across e-commerce sites, forums, and review platforms, with responses structured in a consistent JSON format. Through semantic analysis, it extracts key product insights including alignment with user priorities, pros/cons, and sentiment - all backed by cited sources. The FastAPI backend processes these structured responses before serving them to the Next.js frontend for a polished user experience.

## Links

* **Live Demo**: [https://perplexicart.vercel.app/](https://perplexicart.vercel.app/)
* **GitHub Repository**: [https://github.com/fizakhan90/perplexicart](https://github.com/fizakhan90/perplexicart)


# PerplexiGrid | Interactive Analytics Dashboards
Source: https://docs.perplexity.ai/docs/cookbook/showcase/perplexigrid

Instantly generate analytics dashboards from natural language using live data via Perplexity Sonar API.

**PerplexiGrid** turns natural language into rich, interactive dashboards. Connect your data and mix it with live web data, ask a question, and let the Sonar API do the rest! Complete with drag-and-drop layout, AI widget generation, and ECharts-powered visualizations.

## Features

* **Natural Language to Dashboards**: Convert plain English prompts into fully functional analytics dashboards with 25+ widget types
* **Live Data Integration**: Blend your own data sources with real-time web data for comprehensive insights
* **Interactive Grid Layout**: Drag-and-drop interface for customizing dashboard layouts and styling
* **AI-Powered Refinement**: Refine or add widgets using conversational updates
* **Export & Share**: Generate PDF exports, high-res images, and shareable dashboard links

## How it uses Sonar

PerplexiGrid leverages the Sonar API through four specialized modes:

* **Full Dashboard Generation (f1)**: Creates comprehensive dashboards with multiple widgets using Sonar Pro's advanced capabilities
* **Lightweight Mode (l1)**: Generates quick visualizations for embedded systems and real-time applications
* **Dashboard Updates (r1)**: Enables dynamic modifications through natural language while maintaining context
* **Widget Refinement (r2)**: Provides precise control over individual widget updates

The system uses structured JSON schema responses to ensure consistent, ECharts-compatible output that can be directly rendered as interactive visualizations.

## Usage

1. Open the app and start a new dashboard
2. Prompt it like: *"Show me market trends in AI startups in 2024"*  (Sonar generates chart configs, which are parsed and rendered as live widgets)

![Prompt #1](https://www.perplexigrid.com/guide/prompt_dark.gif)

3. Rearrange and style the widgets with the grid interface

![Prompt #2](https://www.perplexigrid.com/guide/move_dark.gif)
![Prompt #3](https://www.perplexigrid.com/guide/customize_dark.gif)

5. Add your own datasources to blend your data with live web data

![Prompt #4](https://www.perplexigrid.com/guide/datasource_dark.gif)

6. Refine them via text prompts or export the dashboard as needed
7. Collaborate and share easily

![Prompt #5](https://www.perplexigrid.com/guide/invite_dark.gif)

## Code Explanation

The user sends messages that are turned into prompts to a Supabase Edge Function that wraps the Perplexity Sonar API.\
Depending on the mode (`f1`, `l1`, `r1`, or `r2`), the function generates full structured outputs for dashboards, lightweight visualizations, or targeted updates.\
The generated layout is parsed into structured widget definitions and passed through our widget creation engine.

Explore our [main sonar-api service here.](https://github.com/PetarRan/perplexigrid/blob/main/server/supabase/functions/_shared/perplexityService.ts)

## Prompt Modes

| Mode | Description                          | Use Case                                                              | Notes                                                                     |
| ---- | ------------------------------------ | --------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `f1` | First-time full dashboard generation | User starts with an empty canvas and enters an initial prompt         | Produces a complete dashboard layout with multiple widgets                |
| `l1` | Lightweight dashboard generation     | Used for quick insights or previews with minimal tokens               | Faster and cheaper, but returns fewer widgets with less instruction depth |
| `r1` | Full dashboard regeneration          | User wants to replace all existing widgets with a new prompt          | Rebuilds the entire dashboard while keeping layout intact                 |
| `r2` | Targeted widget update               | User wants to change a specific widget (e.g. "make this a pie chart") | Only the selected widget is modified based on the new instruction         |

## Tech Stack

* **Frontend**: React + Vite (TypeScript), ECharts, react-grid-layout
* **Backend**: Supabase Edge Functions (TypeScript on Deno)
* **AI Engine**: Perplexity Sonar Pro
* **Infrastructure**: Supabase (PostgreSQL, RLS, Auth), Vercel deployment

## Links

* [GitHub Repository](https://github.com/PetarRan/perplexigrid)
* [Live Demo](https://app.perplexigrid.com)
* [Website](https://www.perplexigrid.com)


# Perplexity Client | Desktop AI Chat Interface with API Controls
Source: https://docs.perplexity.ai/docs/cookbook/showcase/perplexity-client

An Electron-based desktop client for Perplexity API with advanced features like model selection, custom system prompts, and API debugging mode

**Perplexity Client** is an Electron-based desktop application that provides a polished interface for interacting with Perplexity's Sonar API. It exposes advanced API parameters like max tokens, making it ideal for developers who want fine-grained control over their AI interactions while enjoying a beautiful, macOS-inspired UI.

<img alt="Perplexity Client Interface" />

## Features

* **Multiple Sonar Models** with support for Sonar, Sonar Pro, and Sonar Reasoning Pro
* **Custom Spaces** with save/load functionality for different use cases
* **API Parameter Controls** including max tokens adjustments
* **API Debugging Mode** showing full request/response payloads for troubleshooting
* **Token Usage Tracking** to monitor API consumption and costs
* **Focus Modes** for specialized tasks like coding, writing, and research

## Prerequisites

* Node.js v16 or higher
* npm or yarn
* Perplexity API key

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/straight-heart/Perplexity-client-.git
cd Perplexity-client-

# Install dependencies
npm install

npm run dev
```

## Build

Build the application for your platform:

```bash theme={null}
npm run build:win    # Windows
npm run build:mac    # macOS
npm run build:linux  # Linux
```

## Configuration

API keys are managed directly within the application:

1. Launch the app and open Settings (gear icon)
2. In the **API Keys** section, click **Add Key**
3. Enter your Perplexity API key
4. The key is stored securely and persists across sessions

For custom system prompts, use the **Spaces** feature to save and switch between different instruction sets.

## Usage

1. **Launch**: Run `npm run dev` or use the built application
2. **Add API Key**: Open Settings and add your Perplexity API key
3. **Select Model**: Use the dropdown to choose between Sonar variants
4. **Create Spaces**: Set up custom system prompts for different tasks
5. **Chat**: Start conversing with real-time streaming responses
6. **Debug**: Enable API debugging to see full request/response details
7. **Track Usage**: Monitor token consumption in the Settings panel

## Screenshots

| Feature                      | Preview                  |
| ---------------------------- | ------------------------ |
| Spaces (Custom Instructions) | <img alt="Spaces" />     |
| Model & Parameter Controls   | <img alt="Parameters" /> |
| API Debugging Mode           | <img alt="Debug" />      |
| Theme Selection              | <img alt="Themes" />     |

## Limitations

* Desktop only (Windows, macOS, Linux) — no mobile or web version
* Requires internet connection for API calls
* API key required for functionality

## Links

* [GitHub Repository](https://github.com/straight-heart/Perplexity-client-)


# Perplexity Dart & Flutter SDKs
Source: https://docs.perplexity.ai/docs/cookbook/showcase/perplexity-flutter

Lightweight, type-safe SDKs for seamless Perplexity API integration in Dart and Flutter applications

# Perplexity Dart & Flutter SDKs

**Perplexity Dart & Flutter SDKs** provide a comprehensive toolkit for integrating Perplexity's AI capabilities into Dart and Flutter applications. Built specifically for the Flutter community, these packages include a lightweight core API client and ready-to-use Flutter widgets with BLoC state management.

## Features

* Type-safe API client with fully typed models and compile-time safety
* Streaming and non-streaming chat completions with real-time response handling
* Support for all Perplexity models (Sonar, Sonar Pro, Deep Research, Reasoning variants)
* Multi-image processing with base64, data URI, and HTTPS URL support
* Ready-to-use Flutter widgets with BLoC state management integration
* Advanced configuration options (search filters, domain restrictions)
* Cross-platform support for iOS, Android, Web, and Desktop
* Future-proof design with custom model string support for new Perplexity releases

## Prerequisites

* Dart SDK 2.17.0 or newer
* Flutter SDK 3.0.0 or newer (for Flutter-specific features)
* Perplexity API key from Perplexity API Console
* Basic knowledge of Flutter BLoC pattern for widget integration

## Installation

### For Dart Projects (Core API Only)

```bash theme={null}
dart pub add perplexity_dart
```

### For Flutter Projects (Full Widget Support)

```bash theme={null}
flutter pub add perplexity_flutter
```

### Environment variables

```dart theme={null}
// Add to your app's configuration
const String perplexityApiKey = 'your_perplexity_api_key_here';
```

## Usage

### Core API Integration

* Type-safe client with all Perplexity models (Sonar, Sonar Pro, Deep Research, Reasoning)
* Streaming and non-streaming chat completions
* Multimodal processing with flexible MessagePart system for text + images

### Flutter Widget Layer

* `ChatWrapperWidget` for BLoC state management
* `PerplexityChatView` for real-time message display
* `PerplexityChatInput` for user interaction handling

## Code Explanation

* Core Layer: Pure Dart API client (`perplexity_dart`) for cross-platform Perplexity API integration
* UI Layer: Flutter widgets (`perplexity_flutter`) with BLoC state management for rapid development
* Type Safety: Fully typed models and responses prevent runtime errors and provide IntelliSense
* Multimodal: Flexible MessagePart system for combining text and images in single requests
* Streaming: Built-in support for real-time chat completions with proper chunk handling
* Architecture: Two-layer design allows lightweight API usage or full Flutter widget integration

## Architecture

### Two-layer design

* **Core (`perplexity_dart`)** - Pure Dart API client for all platforms
* **UI (`perplexity_flutter`)** - Flutter widgets + BLoC state management

Uses flexible MessagePart system for multimodal content combining text and images.

## Links

### Packages

* [perplexity\_dart on pub.dev](https://pub.dev/packages/perplexity_dart) | [GitHub](https://github.com/vishnu32510/perplexity_dart)
* [perplexity\_flutter on pub.dev](https://pub.dev/packages/perplexity_flutter) | [GitHub](https://github.com/vishnu32510/perplexity_flutter)

### Examples

* [Flutter Example App](https://github.com/vishnu32510/perplexity_dart/tree/main/example_flutter_app)
* [Dart Examples](https://github.com/vishnu32510/perplexity_dart/tree/main/example)


# Perplexity Lens | AI-Powered Knowledge Graph Browser Extension
Source: https://docs.perplexity.ai/docs/cookbook/showcase/perplexity-lens

A browser extension that builds personalized knowledge graphs using Perplexity AI for smart text selection, webpage summarization, and contextual insights

**Perplexity Lens** is a powerful browser extension that transforms your browsing experience by providing AI-powered insights using Perplexity AI and creating a personalized knowledge graph that visually connects the concepts you encounter online.

<iframe title="YouTube video player" />

## Features

* **Smart Text Selection** with AI-generated explanations for selected text
* **Webpage Summarization** for instant, concise overviews of entire pages
* **Contextual RAG Insights** using Retrieval-Augmented Generation for detailed context and meanings
* **Knowledge Graph Visualization** with interactive D3.js graphs showing concept connections
* **Public Sharing** with URL generation for sharing graphs with others
* **User Authentication** via Firebase for secure access
* **Dual Storage** with local IndexedDB and cloud Firebase storage
* **Responsive UI** fully functional across all devices

## Prerequisites

* Node.js v14+ and npm v6+
* Google Chrome or compatible browser
* Firebase account for cloud functionality
* Firebase CLI (`npm install -g firebase-tools`)
* Perplexity API key and OpenAI API key

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/iamaayushijain/perplexity-lens.git
cd perplexity_lens

# Install dependencies
npm install

# Build the extension
npm run build
```

## Configuration

Edit `src/config.ts`:

```typescript theme={null}
export const PERPLEXITY_API_KEY = 'your-perplexity-key';
export const EMBEDDING_API_KEY = 'your-openai-key';
export const FIREBASE_HOSTING_URL = 'https://your-project-id.web.app';
```

## Usage

1. **Load Extension**: Go to `chrome://extensions/`, enable Developer mode, click "Load unpacked" and select the `dist/` directory

2. **Sign In**: Click the extension icon and authenticate via Firebase

3. **Use Features**:
   * **Highlight Text**: Select text on any webpage for AI-powered insights
   * **Summarize Page**: Use the "Summarize" feature for webpage overviews
   * **Ask Anything**: Hover or click on words/phrases for definitions or explanations
   * **View Graph**: Navigate to the Graph tab to see your knowledge graph
   * **Explore**: Zoom, drag, and hover over nodes in the interactive graph
   * **Share**: Click "Share Graph" to generate a public link

## Code Explanation

* **Frontend**: React with TypeScript and TailwindCSS for modern, responsive UI
* **Browser Extension**: Chrome extension architecture with popup and content scripts
* **AI Integration**: Perplexity AI for intelligent text explanations and summarization
* **Knowledge Graph**: D3.js for interactive graph visualization and concept connections
* **Storage**: Dual storage system with local IndexedDB and cloud Firebase
* **Authentication**: Firebase Auth for secure user access and data management
* **RAG System**: Retrieval-Augmented Generation for contextual insights and definitions

## Links

* [GitHub Repository](https://github.com/iamaayushijain/perplexity-lens)
* [Blog Post](https://ashjin.hashnode.dev/perplexity-lens-supercharge-your-web-experience-with-personalized-knowledge-graphs)


# PosterLens | Scientific Poster Scanner & Research Assistant
Source: https://docs.perplexity.ai/docs/cookbook/showcase/posterlens

An iOS app that transforms static scientific posters into interactive insights using OCR and Perplexity's Sonar Pro API for semantic search and context

**PosterLens** is an iOS app that transforms static scientific posters into interactive, explorable insights using OCR and AI. Created for the Perplexity Hackathon 2025, it allows researchers, MSLs, and medical writers to scan posters and explore them interactively using natural language, extracting meaning and surfacing related studies instantly.

![PosterLens Screenshot](https://cdn.prod.website-files.com/66d49e8555a289120a81ec3e/68930ad938e072c05d1be0b9_PosterLens.png)

## Features

* **Scientific Poster Scanning** using device camera and Apple Vision OCR
* **Natural Language Q\&A** about poster content with AI-powered responses
* **Semantic Search Integration** using Perplexity Sonar Pro for related studies
* **Citation Validation** with PubMed E-utilities for academic accuracy
* **Auto-Generated Research Questions** and future research directions
* **On-Device Processing** for privacy and performance
* **Interactive Research Experience** transforming static content into dynamic insights

## Prerequisites

* iOS 17+ device with camera
* Xcode 15+ for development
* Apple Developer account for App Store distribution
* Perplexity API key (Sonar Pro)
* OpenAI API key (GPT-3.5)
* PubMed E-utilities access

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/nickjlamb/PosterLens.git
cd PosterLens

# Open in Xcode
open PosterLens.xcodeproj
```

## Configuration

Add your API keys to the project configuration:

```swift theme={null}
// API Configuration
PERPLEXITY_API_KEY=your_sonar_pro_api_key
OPENAI_API_KEY=your_gpt_api_key
PUBMED_API_KEY=your_pubmed_api_key
```

## Usage

1. **Install from App Store**: Download PosterLens from the iOS App Store
2. **Scan Poster**: Point your camera at a scientific poster
3. **OCR Processing**: Apple Vision automatically extracts text content
4. **Ask Questions**: Use natural language to query the poster content
5. **Explore Related Research**: Discover semantically related studies via Sonar Pro
6. **Validate Citations**: Check academic references with PubMed integration

## Code Explanation

* **Frontend**: Native iOS app built with SwiftUI for modern UI/UX
* **OCR Processing**: Apple Vision framework for text extraction from images
* **AI Integration**: Perplexity Sonar Pro API for semantic search and context understanding
* **Natural Language**: GPT-3.5 for Q\&A and content interpretation
* **Academic Validation**: PubMed E-utilities for citation verification
* **On-Device Processing**: Local OCR and processing for privacy and performance
* **Research Enhancement**: Auto-generation of research questions and future directions

## Links

* [GitHub Repository](https://github.com/nickjlamb/PosterLens)
* [App Store](https://apps.apple.com/us/app/posterlens-research-scanner/id6745453368)


# Sonar Chromium Browser | Native Search Omnibox and Context Menu
Source: https://docs.perplexity.ai/docs/cookbook/showcase/sonar-chromium-browser

Chromium browser patch with native Perplexity Sonar API integration providing omnibox answers and context-menu summarization

**Sonar Chromium Browser** is a Chromium browser patch that natively integrates Perplexity's Sonar API to provide AI-powered functionality directly in the browser. Users can type `sonar <query>` in the omnibox for instant AI answers or select text and right-click "Summarize with Sonar" for quick summaries, streamlining research and browsing workflows.

## Features

* **Omnibox AI Answers** with `sonar <query>` syntax for instant responses
* **Context-menu Summarization** for selected text with one-click access
* **Native Browser Integration** using Chromium's omnibox and context-menu APIs
* **Dual Model Support** using Sonar Pro for omnibox and Sonar for summaries
* **Debounced Input Handling** for efficient API usage
* **Custom Browser Build** demonstrating AI integration patterns

## Prerequisites

* Ubuntu 22.04 (WSL2 recommended)
* Chromium source code checkout
* Perplexity API key
* 16GB+ RAM for Chromium build
* Git and standard build tools

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/KoushikBaagh/perplexity-hackathon-chromium.git
cd perplexity-hackathon-chromium

# Apply patches to Chromium source
# Follow the README for detailed Chromium setup instructions
```

## Configuration

Update API keys in the modified files:

```cpp theme={null}
// In sonar_autocomplete_provider.cc and render_view_context_menu.cc
const std::string API_KEY = "your_perplexity_api_key_here";
```

## Usage

1. **Build Chromium** with applied patches following the repository instructions
2. **Launch the custom browser** with AI integration
3. **Use Omnibox AI**: Type `sonar what is quantum tunneling?` in address bar
4. **Use Context Summarization**: Select text, right-click "Summarize with Sonar"

## Code Explanation

* **Omnibox Integration**: Custom autocomplete provider hooking into Chromium's omnibox API
* **Context Menu**: Modified render view context menu for text summarization
* **API Integration**: Direct Perplexity Sonar API calls with debounced input handling
* **Model Selection**: Sonar Pro for omnibox queries, Sonar for text summarization
* **Browser Architecture**: Demonstrates Chromium extension points for AI features
* **Build Process**: Custom Chromium build with AI patches applied

## Demo Video

<iframe title="YouTube video player" />

## Links

* [GitHub Repository](https://github.com/KoushikBaagh/perplexity-hackathon-chromium)
* [Chromium Gerrit Repository](https://chromium-review.googlesource.com/c/chromium/src/+/6778540)


# StarPlex | AI-Powered Startup Intelligence Platform
Source: https://docs.perplexity.ai/docs/cookbook/showcase/starplex

An AI-powered startup intelligence platform that helps entrepreneurs validate their business ideas and find the right resources to succeed

**StarPlex** is an AI-powered startup intelligence platform that helps entrepreneurs validate their business ideas and connect with the resources they need to succeed. Powered primarily by **Perplexity Sonar Pro**, it features an interactive **3D globe interface** as its main UI. Simply enter your startup idea, and watch as the AI engine analyzes and visualizes insights directly on the globe—mapping out competitors, markets, demographics, VCs, and potential co-founders across the world in real-time.

<iframe title="StarPlex Demo" />

## Features

* **Market Validation Analysis** with AI-proof scoring, market cap estimation, and growth trend analysis
* **Interactive 3D Globe Interface** for visualizing global startup intelligence data
* **Competitor Research** with threat scoring and competitive landscape mapping
* **VC & Investor Matching** based on investment thesis and portfolio alignment
* **Co-founder Discovery** with compatibility scoring and expertise matching
* **Demographic Research** with heatmap visualization of target audience locations
* **AI Pitch Deck Generation** creating investor-ready presentations
* **Context-Aware Chatbot** with RAG integration across all research data

## Prerequisites

* Node.js 18+ and npm
* Python 3.8+ and pip
* Perplexity API key (Sonar Pro)
* Mapbox token and SERP API key

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/JerryWu0430/StarPlex.git
cd StarPlex

# Backend setup
cd backend
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install
```

## Configuration

Create `.env` file in the backend directory:

```ini theme={null}
PERPLEXITY_API_KEY=your_perplexity_api_key
MAPBOX_TOKEN=your_mapbox_token
SERPAPI_KEY=your_serpapi_key
```

## Usage

1. **Start Backend**:
   ```bash theme={null}
   cd backend
   python main.py
   ```

2. **Start Frontend**:
   ```bash theme={null}
   cd frontend
   npm run dev
   ```

3. **Access Application**: Open [http://localhost:3000](http://localhost:3000) and enter your startup idea

4. **Explore Intelligence**: Use the 3D globe to visualize competitors, VCs, demographics, and co-founders

5. **Generate Assets**: Create pitch decks and chat with the AI assistant about your analysis

## How StarPlex Uses Perplexity Sonar API

StarPlex leverages Perplexity's Sonar API through a **multi-module intelligence architecture**:

**Market Analysis Engine**
Uses Sonar Pro for comprehensive market validation, combining Google Trends data with AI analysis to generate market cap estimates, AI-disruption scores, and growth projections with structured JSON outputs.

**Competitor Intelligence**
Employs multiple concurrent Sonar queries to identify competing companies, funding status, and threat levels. Each competitor receives a 1-10 threat score with detailed competitive positioning analysis.

**VC & Co-founder Matching**
Leverages Sonar's real-time web knowledge to find relevant investors and potential co-founders, scoring matches based on investment thesis alignment, expertise fit, and geographic proximity.

**Context-Aware Business Assistant**
Implements RAG (Retrieval-Augmented Generation) by feeding all research data into Sonar conversations, creating a knowledgeable startup advisor that can answer questions about market positioning, competitive threats, and strategic decisions.

**Geographic Intelligence**
Combines Sonar's demographic insights with Mapbox geocoding to create interactive heatmaps showing where target audiences are concentrated globally.

## Code Explanation

* **Backend**: Python FastAPI with AsyncIO for concurrent Perplexity API calls across multiple analysis modules
* **Frontend**: Next.js with React 19, featuring Cobe for 3D globe visualization and Mapbox GL for interactive mapping
* **AI Integration**: Multi-model Perplexity strategy using Sonar Pro for complex analysis and Sonar for faster queries
* **Data Pipeline**: Intelligent caching, structured JSON responses, and real-time streaming for immediate user feedback
* **Visualization**: Dynamic data binding between Perplexity insights and interactive globe/map interfaces

## Links

* [GitHub Repository](https://github.com/JerryWu0430/StarPlex)
* [Live Demo](https://starplex.app)
* [Devpost Submission](https://devpost.com/software/starplex)


# TruthTracer | AI-Powered Misinformation Detection Platform
Source: https://docs.perplexity.ai/docs/cookbook/showcase/truth-tracer

A comprehensive misinformation detection platform that uses Perplexity's Sonar API to analyze claims, trace trust chains, and provide Socratic reasoning for fact verification

**TruthTracer** is a comprehensive misinformation detection platform that leverages Perplexity's Sonar API to provide multi-layered claim analysis. The platform combines fact-checking, trust chain tracing, and Socratic reasoning to deliver accurate, evidence-based verification results with confidence scores and detailed sourcing.

### Demo

<iframe title="YouTube video player" />

## Features

* **Multi-method Analysis** combining fact-checking, trust chain analysis, and Socratic reasoning
* **AI-Powered Verification** using Perplexity's Sonar, Sonar Deep Research, and Sonar Reasoning Pro  models
* **Real-time Processing** with parallel execution of multiple analysis methods
* **Evidence-based Results** providing sources, confidence scores, and detailed reasoning
* **Clean Architecture** with NestJS backend and React frontend
* **Production-Ready** with Docker deployment, comprehensive testing, and API documentation
* **Configurable Confidence Scoring** with customizable weights and thresholds

## Prerequisites

* Node.js 18+ and npm
* Perplexity API key (Sonar models access)
* Docker (optional for deployment)
* Git for repository cloning

## Installation

```bash theme={null}
# Clone the backend repository
git clone https://github.com/anthony-okoye/truth-tracer-backend.git
cd truth-tracer-backend

# Install dependencies
npm install

# Clone the frontend repository
git clone https://github.com/anthony-okoye/truth-tracer-front.git
cd truth-tracer-front

# Install frontend dependencies
npm install
```

## Configuration

Create `.env` file in the backend directory:

```ini theme={null}
# Required
SONAR_API_KEY=your_perplexity_api_key
SONAR_API_URL=https://api.perplexity.ai

# Optional configuration
SONAR_TIMEOUT=30000
SONAR_MAX_RETRIES=3
CONFIDENCE_WEIGHT_FACT_CHECK=0.35
CONFIDENCE_WEIGHT_TRUST_CHAIN=0.25
CONFIDENCE_WEIGHT_SOCRATIC=0.20
```

## Usage

1. **Start Backend**:

```bash theme={null}
   cd truth-tracer-backend
   npm run start:dev
```

2. **Start Frontend**:

```bash theme={null}
   cd truth-tracer-front
   npm start
```

3. **Access Application**: Open [http://localhost:3000](http://localhost:3000) in your browser

4. **Analyze Claims**:
   * Enter a claim in the text area
   * Click "Analyze Claim" to run fact-checking, trust chain analysis, and Socratic reasoning
   * View results with confidence scores, sources, and detailed explanations

## Code Explanation

* **Backend**: NestJS application with clean architecture following TypeScript best practices
* **AI Integration**: Perplexity Sonar API with three specialized models - Sonar for fact-checking, Sonar Deep Research for trust chain analysis, and Sonar Reasoning Pro for logical evaluation
* **Parallel Processing**: Simultaneous execution of all three analysis methods for efficient claim verification
* **Response Sanitization**: Custom JSON parsing and validation to handle various API response formats
* **Confidence Scoring**: Weighted scoring system combining results from all three analysis methods
* **Frontend**: React application with intuitive claim submission interface and detailed results visualization
* **Testing**: Comprehensive test suite including unit tests, end-to-end tests, and claim analysis testing

## How the Sonar API is Used

TruthTracer leverages Perplexity's Sonar API through three distinct analysis approaches:

```typescript theme={null}
// Parallel execution of multiple Sonar models
const [factCheckResult, trustChainResult, socraticResult] = await Promise.all([
  sonarClient.chat.completions.create({
    model: "sonar",
    messages: [{ role: "user", content: factCheckPrompt }],
    max_tokens: 500
  }),
  sonarClient.chat.completions.create({
    model: "sonar-deep-research", 
    messages: [{ role: "user", content: trustChainPrompt }],
    max_tokens: 2500
  }),
  sonarClient.chat.completions.create({
    model: "sonar-reasoning",
    messages: [{ role: "user", content: socraticPrompt }],
    max_tokens: 4000
  })
]);
```

## Links

* [Live Demo](https://truthtracer.netlify.app/)
* [Backend Repository](https://github.com/anthony-okoye/truth-tracer-backend)
* [Frontend Repository](https://github.com/anthony-okoye/truth-tracer-front)


# UnCovered | Real-Time Fact-Checking Chrome Extension
Source: https://docs.perplexity.ai/docs/cookbook/showcase/uncovered

A Chrome extension that brings real-time fact-checking to anything you see online in just 2 clicks, powered by Perplexity's Sonar API for instant verification

**UnCovered** is a Chrome extension that verifies text, images, websites, and screenshots in real-time—right where you browse. Built on Perplexity's Sonar API, it provides instant truth with citations, verdicts, and deep analysis using just a right-click, without breaking your browsing flow.

## Features

* **3-Click Verification**: Select → Right-click → Verify (Text, Image, Link, or Screenshot)
* **Text Analysis Modes**: Quick Search, Fact-Check, and Deep Research capabilities
* **Image Fact-Checking**: Reverse image analysis and multimodal claim verification
* **Screenshot & Video Frame Capture**: Analyze visuals like infographics, memes, or chart snapshots
* **Citation-Backed Results**: All answers include sources and fact-verdicts (True/False/Unconfirmed)
* **Instant Rebuttal Generator**: Create concise, fact-based replies to misinformation
* **Zero-Friction UX**: Stay on the same page — no copy-paste, no new tabs required

## Prerequisites

* Chrome browser
* Node.js 16+ and npm
* MongoDB database
* Cloudinary account for image storage
* Perplexity API key (Sonar Pro and Deep Research access)
* Google OAuth credentials

## Installation

```bash theme={null}
# Clone the repository
git clone https://github.com/aayushsingh7/UnCovered.git
cd UnCovered

# Install dependencies
npm install

# Build the Chrome extension
npm run build
```

## Configuration

Set up your environment variables:

```ini theme={null}
PERPLEXITY_API_KEY=your_sonar_api_key
MONGODB_URI=your_mongodb_connection_string
CLOUDINARY_URL=your_cloudinary_credentials
GOOGLE_OAUTH_CLIENT_ID=your_google_oauth_id
```

## Usage

1. **Text/Link Verification**:
   * Select text or right-click a link
   * Choose Quick Search / Fact-Check / Deep Research
   * Get trusted results with verdicts and citations

2. **Image Verification**:
   * Right-click any image
   * Choose from Quick Search or Fact-Check
   * Detect misinformation and visual manipulation

3. **Screenshot/Infographic Analysis**:
   * Click UnCovered icon in the toolbar
   * Use "Capture Screen" to analyze visual content

4. **Get Instant Rebuttal**:
   * Auto-generate fact-based responses to correct misinformation

## Code Explanation

* **Frontend**: Vanilla JavaScript Chrome extension with context menu integration
* **Backend**: Node.js Express server handling API requests and user authentication
* **AI Integration**: Perplexity Sonar Pro and Deep Research APIs for intelligent fact-checking
* **Image Processing**: Cloudinary integration for screenshot and image analysis
* **Database**: MongoDB for user data and verification history
* **Authentication**: Google OAuth for secure user management
* **Multimodal Analysis**: Support for text, images, screenshots, and video frames

## Technical Implementation

UnCovered leverages Perplexity Sonar API in three core modes:

```javascript theme={null}
// Quick Search and Fact-Check with Sonar Pro
const quickResponse = await perplexityClient.chat.completions.create({
  model: "sonar-pro",
  messages: [{ role: "user", content: factCheckPrompt }]
});

// Deep Research for comprehensive analysis
const deepResponse = await perplexityClient.chat.completions.create({
  model: "sonar-deep-research", 
  messages: [{ role: "user", content: deepAnalysisPrompt }]
});
```

## Demo Video

<iframe title="UnCovered Demo" />

## Links

* [GitHub Repository](https://github.com/aayushsingh7/UnCovered)
* [Live Demo](https://uncovered.vercel.app)


# Valetudo AI | Trusted Medical Answer Assistant
Source: https://docs.perplexity.ai/docs/cookbook/showcase/valetudo-ai

Sonar-powered medical assistant for fast, science-backed answers.

# Valetudo AI

**Valetudo AI** is a science-backed medical assistant powered by the Perplexity Sonar API. It provides fast, clear, and well-cited answers to health questions — helping users cut through misinformation with filters, image analysis, and ready-made prompt templates.

Designed for conscious users — like parents, patients, and medical students — seeking reliable information.

## Features

* **Cited Answers** — sourced from a curated list of 10 trusted medical domains
* **Smart Filters** — by date and country for localized, up-to-date insights
* **Image Upload** — analyze photos of medication, conditions, or packaging
* **Prompt Templates** — 7 categories for symptom checks, drug safety, research, and more
* **Simple UI** — built with React and Tailwind CSS

## How It Uses the Sonar API

Valetudo AI integrates with [Perplexity Sonar Pro](https://docs.perplexity.ai), leveraging advanced features for domain-specific search and rich responses:

| Feature          | API Field                         | Purpose                                           |
| ---------------- | --------------------------------- | ------------------------------------------------- |
| Context Control  | `search_context_size: medium`     | Balances speed and depth for focused medical Q\&A |
| Trusted Domains  | `search_domain_filter`            | Restricts results to vetted health sources        |
| Visual Input     | `image_url`                       | Enables image-based medical queries               |
| Freshness Filter | `search_after/before_date_filter` | Helps surface recent and relevant findings        |
| Local Relevance  | `user_location`                   | Tailors answers based on user’s region            |

## Links

* [GitHub Repository](https://github.com/vero-code/valetudo-ai)
* [Devpost Submission](https://devpost.com/software/valetudo-ai)
* [View All Screenshots](https://github.com/vero-code/valetudo-ai/tree/master/screenshots)

## Demo Video

See Valetudo AI in action:

<iframe title="YouTube video player" />

## Screenshots

### Home Interface

![Home screen](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/1-home.png)

### Prompt Templates

![Prompt templates](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/10-prompts.png)

### Image Upload

![Image upload](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/8-image-upload.png)

### Date & Location Filters

![Date filter](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/7-date-filter.png)

![Location filter](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/9-location-filter.png)


# API Groups & Billing
Source: https://docs.perplexity.ai/docs/getting-started/api-groups

Learn how to use the Perplexity API Portal to manage access, usage, billing, and team collaboration.

## What is an API Group?

An **API Group** is your organization's workspace in the Perplexity API Portal. It allows you to:

* **Manage billing** and payment methods for API usage
* **Create and control API keys** for accessing the Perplexity API
* **Invite team members** and control their permissions (optional)
* **Monitor usage and costs** across all your API keys

## Prerequisites

Before getting started, make sure you have:

* A Perplexity account (sign up at [perplexity.ai](https://perplexity.ai))
* **Admin permissions** for billing and API key management
* A **credit card** ready for payment setup (you won't be charged initially)

<Note>
  If you're joining an existing team, you'll need an invitation from an Admin. Contact your team lead to get access.
</Note>

## Accessing the API Portal

Once signed in, navigate to the left-hand sidebar and expand the **API** section to access your API group and related settings.

<Frame>
  <img alt="API Group Location" />
</Frame>

***

## Creating and Managing an API Group

To set up your organization:

<Steps>
  <Step title="Access API Group Settings">
    Click **API Group** in the left sidebar.
  </Step>

  <Step title="Complete Organization Details">
    Fill out your organization's name, address, and tax details.

    <Info>
      Your organization name and address will appear on invoices and help us support you better.
    </Info>

    **Fields include:**

    * Organization name and description
    * Address (Line 1, Line 2, City, State, Zip, Country)
    * Tax ID

    <Frame>
      <img alt="API Group Details" />
    </Frame>
  </Step>
</Steps>

***

## Billing and Payment Methods

### How Billing Works

The Perplexity API uses a **credit-based billing system**:

* **Credits** are purchased in advance and used for API calls
* **Different models** consume different amounts of credits per request
* **Usage is charged** based on tokens processed and search queries made
* **Automatic top-up** can be enabled to avoid service interruptions

<Info>
  See our [Pricing page](./pricing) for detailed cost information per model and usage type.
</Info>

### Setting Up Payment

<Card title="Access Billing Dashboard" icon="credit-card" href="https://www.perplexity.ai/account/api/billing">
  Navigate directly to your API billing dashboard to manage payment methods, view usage, and configure billing settings.
</Card>

<Steps>
  <Step title="Navigate to Billing">
    Go to the **API Billing** tab in your API Portal.

    <Frame>
      <img alt="API Billing" />
    </Frame>
  </Step>

  <Step title="Add Payment Method">
    Click **Add Payment Method** and enter your credit card information.

    <Note>
      This step will not charge your credit card. It just stores payment information for future API usage.
    </Note>
  </Step>

  <Step title="Configure Auto Top-Up (Recommended)">
    Enable automatic credit top-up to avoid service interruptions.

    <Frame>
      <img alt="Auto Reload" />
    </Frame>

    <Warning>
      If you run out of credits, your API keys will be blocked until you add to your credit balance. Auto top-up prevents this by automatically adding credits when your balance drops below a threshold.
    </Warning>
  </Step>
</Steps>

***

## Managing API Keys

### What are API Keys?

API keys are your credentials for accessing the Perplexity API. Each key:

* **Authenticates your requests** to the Perplexity API
* **Tracks usage and billing** for cost attribution
* **Can be revoked or regenerated** for security purposes
* **Should be kept secure** and never shared publicly

<Info>
  You'll need to include your API key in the Authorization header of every API request: `Authorization: Bearer YOUR_API_KEY`
</Info>

### Creating an API Key

<Steps>
  <Step title="Navigate to API Keys">
    Go to the **API Keys** tab in your API Portal.
  </Step>

  <Step title="Generate New Key">
    Click **+ Create Key** to generate a new API key.

    <Frame>
      <img alt="Generate API Keys" />
    </Frame>
  </Step>

  <Step title="Secure Your Key">
    Copy and securely store your API key immediately.

    <Warning>
      API keys are sensitive credentials. Never expose them in client-side code or share them in public repositories.
    </Warning>
  </Step>
</Steps>

***

## Adding and Managing Members

Admins can invite team members to the organization with specific roles: **Admin** or **Member**.

### Adding a Member

<Steps>
  <Step title="Initiate Member Invitation">
    Click **+ Add Member**.

    <Frame>
      <img alt="Click on Add Member" />
    </Frame>
  </Step>

  <Step title="Enter Member Details">
    Enter the user's email address and click **Invite**.

    <Frame>
      <img alt="Enter New Member Email" />
    </Frame>
  </Step>

  <Step title="Member Receives Invitation">
    The invited user will receive an email with a link to join your group.

    <Check>
      Once they accept, they'll appear in your member list with their assigned role.
    </Check>
  </Step>
</Steps>

### Filtering Members by Role

Use the dropdown to filter your list of team members by role.

<Frame>
  <img alt="Filter Members by Role" />
</Frame>

### Roles

* **Admin**: Full access to invite/remove members, manage billing, and view usage data.
* **Member**: Can view usage and account limits but cannot modify settings.

<Warning>
  Only Admins can make changes to billing and member permissions.
</Warning>

***

## Viewing Usage Metrics

All members can view API usage by selecting **Usage Metrics** from the sidebar.

Features include:

* Total API call trends over time
* Breakdown by API model and key
* Optional date range filters

<Check>
  Usage metrics help you monitor API activity and optimize for cost or performance.
</Check>

### Tracking Spend Per API Key

You can track billing for each of your API keys by following these steps:

<Steps>
  <Step title="Navigate to Usage Metrics">
    Navigate to the [API section](https://www.perplexity.ai/account/api) of your **Settings** and click on **Usage Metrics**

    <Frame>
      <img alt="Navigate to dashboard" />
    </Frame>
  </Step>

  <Step title="Access Invoice History">
    Select **Invoice history** > **Invoices**

    <Frame>
      <img alt="View invoice history" />
    </Frame>
  </Step>

  <Step title="View Invoice Details">
    Click on any invoice to view details

    <Frame>
      <img alt="View spend per API key" />
    </Frame>
  </Step>

  <Step title="Identify API Key Charges">
    Each item from the total bill will have a code at the end (e.g., pro (743S))

    * The 4 characters in parentheses are the last 4 characters of your API key
  </Step>
</Steps>


# Perplexity with LangChain
Source: https://docs.perplexity.ai/docs/getting-started/integrations/langchain

Use Perplexity's chat models and search tool in your LangChain applications.

## Overview

The `langchain-perplexity` package provides LangChain integrations for Perplexity's API, enabling you to build LLM applications with real-time web search capabilities.

<Info>
  **LangChain** is a popular Python framework for building applications powered by large language models. It provides composable components for chains, agents, and retrieval-augmented generation (RAG). Learn more at [langchain.com](https://www.langchain.com).
</Info>

The integration includes:

* **ChatPerplexity** - Chat model with Pro Search, streaming, and search controls
* **PerplexitySearchRetriever** - Retriever for RAG applications
* **PerplexitySearchResults** - Tool for LangChain agents

## Installation

<Tabs>
  <Tab title="pip">
    ```bash theme={null}
    pip install langchain-perplexity
    ```
  </Tab>

  <Tab title="uv">
    ```bash theme={null}
    uv add langchain-perplexity
    ```
  </Tab>
</Tabs>

## API Key Setup

Set your Perplexity API key as an environment variable:

```python theme={null}
import os

os.environ["PPLX_API_KEY"] = "your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/settings/api">
  Generate your API key from the Perplexity dashboard.
</Card>

## Quick Start: Chat Models

Use `ChatPerplexity` for conversational AI with web search:

```python theme={null}
from langchain_perplexity import ChatPerplexity

chat = ChatPerplexity(model="sonar")

response = chat.invoke("What are the latest developments in AI?")
print(response.content)
```

### Pro Search

Enable multi-step reasoning with Pro Search:

```python theme={null}
from langchain_perplexity import ChatPerplexity, WebSearchOptions

chat = ChatPerplexity(
    model="sonar-pro",
    web_search_options=WebSearchOptions(search_type="pro")
)

response = chat.invoke("How does the electoral college work?")

# Access reasoning steps
if reasoning := response.additional_kwargs.get("reasoning_steps"):
    for step in reasoning:
        print(f"Thought: {step['thought']}")
```

### Search Controls

Filter search results by domain, recency, or date:

```python theme={null}
chat = ChatPerplexity(
    model="sonar",
    search_domain_filter=["wikipedia.org", "nature.com"],
    search_recency_filter="month",
    return_images=True
)

response = chat.invoke("Solar system planets")

# Access citations and images
print("Citations:", response.additional_kwargs.get("citations", []))
print("Images:", response.additional_kwargs.get("images", []))
```

### Streaming

```python theme={null}
for chunk in chat.stream("Explain quantum computing"):
    print(chunk.content, end="", flush=True)
```

## Quick Start: Retriever

Use `PerplexitySearchRetriever` for RAG applications:

```python theme={null}
from langchain_perplexity import PerplexitySearchRetriever

retriever = PerplexitySearchRetriever(k=5)

docs = retriever.invoke("What is nuclear fusion?")

for doc in docs:
    print(f"Title: {doc.metadata['title']}")
    print(f"URL: {doc.metadata['url']}")
    print(f"Content: {doc.page_content[:200]}...")
    print("---")
```

### RAG Chain Example

```python theme={null}
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_perplexity import ChatPerplexity, PerplexitySearchRetriever

llm = ChatPerplexity(model="sonar")
retriever = PerplexitySearchRetriever(k=3)

template = """Answer based on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

answer = rag_chain.invoke("What is the current status of ITER?")
print(answer)
```

## Quick Start: Tool

Use `PerplexitySearchResults` with LangChain agents:

```python theme={null}
from langchain_perplexity import PerplexitySearchResults

tool = PerplexitySearchResults()

results = tool.invoke("LangChain framework")

for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Snippet: {result['snippet'][:100]}...")
    print("---")
```

### Agent Example

```python theme={null}
from langchain.chat_models import init_chat_model
from langchain_perplexity import PerplexitySearchResults
from langgraph.prebuilt import create_react_agent

model = init_chat_model(model="gpt-4o", model_provider="openai")
search_tool = PerplexitySearchResults()

agent = create_react_agent(model, [search_tool])

for step in agent.stream(
    {"messages": [("user", "What are the latest LangChain releases?")]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()
```

## Available Models

The integration supports all Perplexity models:

| Model                 | Description                               |
| --------------------- | ----------------------------------------- |
| `sonar`               | Fast, cost-effective search model         |
| `sonar-pro`           | Advanced model with Pro Search support    |
| `sonar-reasoning-pro` | Advanced reasoning capabilities           |
| `sonar-deep-research` | Deep research with comprehensive analysis |

See the full list of models on our [models page](/docs/getting-started/models).

## Links & Resources

<CardGroup>
  <Card title="LangChain Docs" icon="book" href="https://docs.langchain.com/oss/python/integrations/providers/perplexity">
    Full LangChain integration documentation
  </Card>

  <Card title="ChatPerplexity" icon="message" href="https://docs.langchain.com/oss/python/integrations/chat/perplexity">
    Detailed chat model documentation
  </Card>

  <Card title="Retriever Docs" icon="magnifying-glass" href="https://docs.langchain.com/oss/python/integrations/retrievers/perplexity">
    PerplexitySearchRetriever documentation
  </Card>

  <Card title="Tool Docs" icon="wrench" href="https://docs.langchain.com/oss/python/integrations/tools/perplexity">
    PerplexitySearchResults documentation
  </Card>

  <Card title="PyPI Package" icon="python" href="https://pypi.org/project/langchain-perplexity/">
    View on PyPI
  </Card>

  <Card title="API Reference" icon="code" href="https://python.langchain.com/api_reference/perplexity/">
    LangChain API reference
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Check the [LangChain documentation](https://docs.langchain.com)
* Review our [FAQ](/docs/resources/faq)


# Perplexity MCP Server
Source: https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server

Connect AI assistants to Perplexity's search and reasoning capabilities using the Model Context Protocol (MCP).

## Overview

The Perplexity MCP Server enables AI assistants to access Perplexity's powerful search and reasoning capabilities directly within their workflows. Using the Model Context Protocol (MCP), you can integrate real-time web search, conversational AI, and advanced reasoning into any MCP-compatible client.

<Info>
  The **Model Context Protocol (MCP)** is an open standard that connects AI assistants with external data sources and tools. Learn more at [modelcontextprotocol.io](https://modelcontextprotocol.io/introduction).
</Info>

## Installation

### One-Click Install

Get started instantly with these one-click installers:

<CardGroup>
  <Card
    title="Install in Cursor"
    icon={
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 466.73 532.09"
>
  <path
    d="M457.43 125.94 244.42 2.96a22.127 22.127 0 0 0-22.12 0L9.3 125.94C3.55 129.26 0 135.4 0 142.05v247.99c0 6.65 3.55 12.79 9.3 16.11l213.01 122.98a22.127 22.127 0 0 0 22.12 0l213.01-122.98c5.75-3.32 9.3-9.46 9.3-16.11V142.05c0-6.65-3.55-12.79-9.3-16.11h-.01Zm-13.38 26.05L238.42 508.15c-1.39 2.4-5.06 1.42-5.06-1.36V273.58c0-4.66-2.49-8.97-6.53-11.31L24.87 145.67c-2.4-1.39-1.42-5.06 1.36-5.06h411.26c5.84 0 9.49 6.33 6.57 11.39h-.01Z"
    style={{ fill: "#22808C" }}
  />
</svg>
}
    href="https://cursor.com/en/install-mcp?name=perplexity&config=eyJ0eXBlIjoic3RkaW8iLCJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkBwZXJwbGV4aXR5LWFpL21jcC1zZXJ2ZXIiXSwiZW52Ijp7IlBFUlBMRVhJVFlfQVBJX0tFWSI6IiJ9fQ=="
  >
    Automatically configure the Perplexity MCP server in Cursor with one click.
  </Card>

  <Card
    title="Install in VS Code"
    icon={
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 100 100"
>
  <path
    d="M70.912 99.572a6.193 6.193 0 0 0 4.96-.191l20.588-9.958a6.285 6.285 0 0 0 3.54-5.661V16.239a6.286 6.286 0 0 0-3.54-5.662L75.873.62a6.2 6.2 0 0 0-7.104 1.216L29.355 37.98l-17.168-13.1a4.146 4.146 0 0 0-5.318.238l-5.506 5.035a4.205 4.205 0 0 0-.004 6.194L16.247 50 1.36 63.654a4.205 4.205 0 0 0 .004 6.194l5.506 5.034a4.145 4.145 0 0 0 5.318.238l17.168-13.1L68.77 98.166a6.205 6.205 0 0 0 2.143 1.407Zm4.103-72.39L45.11 50 75.015 72.82V27.18Z"
    fillRule="evenodd"
    style={{ fill: "#22808C" }}
  />
</svg>
}
    href="https://vscode.dev/redirect/mcp/install?name=perplexity&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40perplexity-ai%2Fmcp-server%22%5D%2C%22env%22%3A%7B%22PERPLEXITY_API_KEY%22%3A%22%22%7D%7D"
  >
    Automatically configure the Perplexity MCP server in VS Code with one click.
  </Card>
</CardGroup>

### Manual Setup

<Steps>
  <Step title="Get Your API Key">
    <Card title="Generate API Key" icon="key" href="https://www.perplexity.ai/account/api/group">
      Navigate to the API Portal and generate a new key.
    </Card>
  </Step>

  <Step title="Configure Your Client">
    Add the MCP server to your client configuration:

    <Tabs>
      <Tab title="Claude Code">
        **Option 1: CLI Command (Recommended)**

        The easiest way to get started:

        ```bash theme={null}
        claude mcp add perplexity --env PERPLEXITY_API_KEY="your_key_here" -- npx -y @perplexity-ai/mcp-server
        ```

        **Option 2: Plugin Install**

        Install via plugin:

        ```bash theme={null}
        export PERPLEXITY_API_KEY="your_key_here"
        claude
        # Then run: /plugin marketplace add perplexityai/modelcontextprotocol
        # Then run: /plugin install perplexity
        ```

        **Option 3: Manual Configuration**

        Add to your `claude.json`:

        ```json theme={null}
        {
          "mcpServers": {
            "perplexity": {
              "type": "stdio",
              "command": "npx",
              "args": ["-y", "perplexity-mcp"],
              "env": {
                "PERPLEXITY_API_KEY": "your_key_here"
              }
            }
          }
        }
        ```
      </Tab>

      <Tab title="Cursor">
        We recommend using the one-click install above for setting up the MCP server in Cursor.

        If you prefer to configure it manually, add the following to your `mcp.json`:

        ```json theme={null}
        {
          "mcpServers": {
            "perplexity": {
              "command": "npx",
              "args": ["-y", "@perplexity-ai/mcp-server"],
              "env": {
                "PERPLEXITY_API_KEY": "your_key_here"
              }
            }
          }
        }
        ```
      </Tab>

      <Tab title="Codex">
        ```bash theme={null}
        codex mcp add perplexity --env PERPLEXITY_API_KEY="your_key_here" -- npx -y @perplexity-ai/mcp-server
        ```
      </Tab>

      <Tab title="Other Clients">
        Most MCP-compatible clients (including Claude Desktop, VS Code, and Windsurf) use the `mcpServers` format. Configuration file locations:

        | Client             | Config File                             |
        | ------------------ | --------------------------------------- |
        | Cursor             | `~/.cursor/mcp.json`                    |
        | VS Code            | `.vscode/mcp.json`                      |
        | Claude Desktop     | `claude_desktop_config.json`            |
        | Windsurf           | `~/.codeium/windsurf/mcp_config.json`   |
        | Google Antigravity | `~/.gemini/antigravity/mcp_config.json` |

        **Standard `mcpServers` format:**

        ```json theme={null}
        {
          "mcpServers": {
            "perplexity": {
              "command": "npx",
              "args": ["-y", "@perplexity-ai/mcp-server"],
              "env": {
                "PERPLEXITY_API_KEY": "your_key_here"
              }
            }
          }
        }
        ```

        **VS Code uses a slightly different format:**

        ```json theme={null}
        {
          "servers": {
            "perplexity": {
              "type": "stdio",
              "command": "npx",
              "args": ["-y", "@perplexity-ai/mcp-server"],
              "env": {
                "PERPLEXITY_API_KEY": "your_key_here"
              }
            }
          }
        }
        ```

        If your client doesn't work with these formats, check its documentation for the correct wrapper format.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Start Using">
    Restart your MCP client and start using Perplexity's tools in your AI workflows.
  </Step>
</Steps>

## Available Tools

<CardGroup>
  <Card title="perplexity_search" icon="magnifying-glass">
    Direct web search using the Perplexity Search API. Returns ranked search results with titles, URLs, snippets, and metadata.

    **Best for:** Finding current information, news, facts, or specific web content.
  </Card>

  <Card title="perplexity_ask" icon="message">
    General-purpose conversational AI with real-time web search using the `sonar-pro` model.

    **Best for:** Quick questions, everyday searches, and conversational queries that benefit from web context.
  </Card>

  <Card title="perplexity_research" icon="book">
    Deep, comprehensive research using the `sonar-deep-research` model. Provides thorough analysis with citations.

    **Best for:** Complex topics requiring detailed investigation, comprehensive reports, and in-depth analysis.
  </Card>

  <Card title="perplexity_reason" icon="brain">
    Advanced reasoning and problem-solving using the `sonar-reasoning-pro` model.

    **Best for:** Logical problems, complex analysis, decision-making, and tasks requiring step-by-step reasoning.
  </Card>
</CardGroup>

<Info>
  For detailed setup instructions, troubleshooting, and proxy configuration, visit our [GitHub repository](https://github.com/perplexityai/modelcontextprotocol).
</Info>


# null
Source: https://docs.perplexity.ai/docs/getting-started/models



<div>
  <div>
    <div>
      <SonarLogo />

      <h1><span>Models</span></h1>
    </div>
  </div>

  <div>
    <div>
      <h3><span>Explore the Sonar range and compare models</span></h3>
    </div>
  </div>

  <Frame>
    <img alt="Sonar Range" />
  </Frame>

  <ModelOverviewCards />
</div>


# null
Source: https://docs.perplexity.ai/docs/getting-started/overview



<div>
  <div>
    <div>
      <PerplexityLogo />

      <h1><span>API Platform</span></h1>
    </div>

    <div>
      <span>
        Power your products with unparalleled real-time, web-wide research and Q\&A capabilities.
      </span>
    </div>
  </div>

  <QuickstartBanner />

  <UseCaseTabs />

  <div>
    <div>
      <div>
        <h3>Search</h3>
        <p>Get ranked web search results with advanced filtering and real-time data.</p>

        <a href="/docs/search/quickstart">
          <img alt="Search API" />
        </a>
      </div>

      <div>
        <h3>Grounded LLM</h3>
        <p>Build AI applications with web-grounded chat completions and reasoning models.</p>

        <a href="/docs/getting-started/quickstart">
          <img alt="Grounded LLM" />
        </a>
      </div>
    </div>
  </div>
</div>


# Pricing
Source: https://docs.perplexity.ai/docs/getting-started/pricing



<Info>
  This page shows **pricing information** to help you understand API costs.

  For **billing setup**, payment methods, and usage monitoring, visit the [Admin section](/docs/getting-started/api-groups). For **rate limits**, see the [Rate Limits & Usage Tiers](/docs/admin/rate-limits-usage-tiers) page.
</Info>

## Search API Pricing

| API            | Price per 1K requests | Description                                    |
| -------------- | :-------------------: | ---------------------------------------------- |
| **Search API** |         \$5.00        | Raw web search results with advanced filtering |

<Note>
  **No token costs:** Search API charges per request only, with no additional token-based pricing.
</Note>

## Agentic Research API Pricing

The Agentic Research API provides access to third-party models from OpenAI, Anthropic, Google, and xAI with **transparent, token-based pricing** at direct provider rates with no markup.

### Model Pricing

Agentic Research API pricing varies by provider and model, with each provider offering multiple models at different price points.

<Card title="View Complete Third-Party Model Pricing" icon="table" href="/docs/grounded-llm/responses/models">
  See the full pricing breakdown for all available models from OpenAI, Anthropic, Google, and xAI, including cache rates and provider documentation links on the [Agentic Research API Models page](/docs/grounded-llm/responses/models).
</Card>

### Tool Pricing

When using web search tools with the Agentic Research API:

| Tool             |          Price          | Description                                           |
| ---------------- | :---------------------: | ----------------------------------------------------- |
| **`web_search`** |  \$0.005 per invocation | Performs web searches to retrieve current information |
| **`fetch_url`**  | \$0.0005 per invocation | Fetches and extracts content from specific URLs       |

<Note>
  Tool costs are separate from model token costs. If a model makes 3 web searches during a request, you pay model tokens + (3 × \$0.005) for searches.
</Note>

## Grounded LLM Pricing

<Info>
  **Total cost per query** = Token costs + Request fee (varies by search context size, applies to Sonar, Sonar Pro, and Sonar Reasoning Pro models only)
</Info>

<Tabs>
  <Tab title="Token Pricing">
    ## Token Pricing

    **Token pricing** is based on the number of tokens in your request and response.

    | Model                   | Input Tokens (\$/1M) | Output Tokens (\$/1M) | Citation Tokens (\$/1M) | Search Queries (\$/1K) | Reasoning Tokens (\$/1M) |
    | ----------------------- | :------------------: | :-------------------: | :---------------------: | :--------------------: | :----------------------: |
    | **Sonar**               |          \$1         |          \$1          |            -            |            -           |             -            |
    | **Sonar Pro**           |          \$3         |          \$15         |            -            |            -           |             -            |
    | **Sonar Reasoning Pro** |          \$2         |          \$8          |            -            |            -           |             -            |
    | **Sonar Deep Research** |          \$2         |          \$8          |           \$2           |           \$5          |            \$3           |
  </Tab>

  <Tab title="Request Pricing">
    ## Request Pricing by Search Context Size

    **Search context** determines how much web information is retrieved. Higher context = more comprehensive results. The following table shows the request fee for each model for every **1000 requests**.

    | Model                   | Low Context Size | Medium Context Size | High Context Size |
    | ----------------------- | :--------------: | :-----------------: | :---------------: |
    | **Sonar**               |        \$5       |         \$8         |        \$12       |
    | **Sonar Pro**           |        \$6       |         \$10        |        \$14       |
    | **Sonar Reasoning Pro** |        \$6       |         \$10        |        \$14       |

    <Note>
      * **Low**: (default) fastest, cheapest
      * **Medium**: Balanced cost/quality
      * **High**: Maximum search depth, best for research

      [Learn more about search context →](../guides/search-context-size-guide)
    </Note>
  </Tab>

  <Tab title="Pro Search Pricing">
    ## Pro Search Pricing (Pro Search for Sonar Pro)

    **Pro Search** enhances Sonar Pro with automated tool usage and multi-step reasoning. When enabled, the model can perform multiple web searches and fetch URL content to answer complex queries. [Learn more about Pro Search here](/docs/grounded-llm/chat-completions/pro-search/quickstart).

    <Info>
      Pro Search requires `stream: true` and is enabled via the `search_type` parameter in `web_search_options`.
    </Info>

    ### Search Type Options

    | Search Type | Description                                        |   Request Fee (per 1K)   |
    | ----------- | -------------------------------------------------- | :----------------------: |
    | **`fast`**  | (default) Standard Sonar Pro behavior              |     \$6 / \$10 / \$14    |
    | **`pro`**   | Multi-step tool usage for complex queries          |    \$14 / \$18 / \$22    |
    | **`auto`**  | Automatic classification based on query complexity | Varies by classification |

    <Note>
      Request fees vary by search context size (Low / Medium / High). Token pricing remains the same as standard Sonar Pro (\$3 per 1M input, \$15 pe r 1M output).
    </Note>
  </Tab>
</Tabs>

<AccordionGroup>
  <Accordion title="Token and Cost Glossary">
    ### Input Tokens

    The number of tokens in your prompt or message to the API. This includes:

    * Your question or instruction
    * Any context or examples you provide
    * System messages and formatting

    **Example:** "What is the weather in New York?" = \~8 input tokens

    ### Output Tokens

    The number of tokens in the API's response. This includes:

    * The generated answer or content
    * Any explanations or additional context
    * Search results and references

    **Example:** "The weather in New York is currently sunny with a temperature of 72°F." = \~15 output tokens

    ### Citation Tokens

    Tokens used specifically for generating search results and references in responses. Only applies to **Sonar Deep Research** model.

    **Example:** Including source links, reference numbers, and bibliographic information

    ### Search Context Size vs Context Window

    **Search context size** is *not* the same as the **context window**.

    * **Search context size**: How much web information is retrieved during search (affects request pricing)
    * **Context window**: Maximum tokens the model can process in one request (affects token limits)

    ### Search Queries

    The number of individual searches conducted by **Sonar Deep Research** during query processing. This is separate from your initial user query.

    * The model automatically determines how many searches are needed
    * You cannot control the exact number of search queries
    * The `reasoning_effort` parameter influences the number of searches performed
    * Only applies to **Sonar Deep Research** model

    ### Reasoning Tokens

    Tokens used for step-by-step logical reasoning and problem-solving. Only applies to **Sonar Deep Research** model.

    **Example:** Breaking down a complex math problem into sequential steps with explanations

    <Info>
      **Token Calculation:** 1 token ≈ 4 characters in English text. The exact count may vary based on language and content complexity.
    </Info>
  </Accordion>
</AccordionGroup>

## Cost Examples

<CardGroup>
  <Card title="Sonar Web Search Example" icon="calculator">
    **Sonar** • 500 input + 200 output tokens

    <Tabs>
      <Tab title="Low">
        | Component     | Cost         |
        | ------------- | ------------ |
        | Input tokens  | \$0.0005     |
        | Output tokens | \$0.0002     |
        | Request fee   | \$0.005      |
        | **Total**     | **\$0.0057** |
      </Tab>

      <Tab title="Medium">
        | Component     | Cost         |
        | ------------- | ------------ |
        | Input tokens  | \$0.0005     |
        | Output tokens | \$0.0002     |
        | Request fee   | \$0.008      |
        | **Total**     | **\$0.0087** |
      </Tab>

      <Tab title="High">
        | Component     | Cost         |
        | ------------- | ------------ |
        | Input tokens  | \$0.0005     |
        | Output tokens | \$0.0002     |
        | Request fee   | \$0.012      |
        | **Total**     | **\$0.0127** |
      </Tab>
    </Tabs>
  </Card>

  <Card title="Deep Research Example" icon="chart-line">
    **Sonar Deep Research**

    <Tabs>
      <Tab title="Low">
        | Component                | Cost           |
        | ------------------------ | -------------- |
        | Input tokens (33)        | \$0.000066     |
        | Output tokens (7163)     | \$0.057304     |
        | Citation tokens (20016)  | \$0.040032     |
        | Reasoning tokens (73997) | \$0.221991     |
        | Search queries (18)      | \$0.09         |
        | **Total**                | **\$0.409393** |
      </Tab>

      <Tab title="Medium">
        | Component                 | Cost        |
        | ------------------------- | ----------- |
        | Input tokens (7)          | \$0.00      |
        | Output tokens (3847)      | \$0.031     |
        | Citation tokens (47293)   | \$0.095     |
        | Reasoning tokens (308156) | \$0.924     |
        | Search queries (28)       | \$0.14      |
        | **Total**                 | **\$1.190** |
      </Tab>

      <Tab title="High">
        | Component                 | Cost        |
        | ------------------------- | ----------- |
        | Input tokens (8)          | \$0.00      |
        | Output tokens (4435)      | \$0.035     |
        | Citation tokens (58196)   | \$0.116     |
        | Reasoning tokens (339594) | \$1.019     |
        | Search queries (30)       | \$0.15      |
        | **Total**                 | **\$1.320** |
      </Tab>
    </Tabs>
  </Card>
</CardGroup>


# Quickstart
Source: https://docs.perplexity.ai/docs/getting-started/quickstart

Generate an API key and make your first call in < 3 minutes.

## Overview

The Perplexity API provides three core APIs for different use cases: **Chat Completions** for web-grounded AI responses with Sonar models, **Agentic Research** for accessing OpenAI, Anthropic, Google, and xAI models with unified search tools and transparent pricing, and **Search** for ranked web search results.

All APIs support both REST and SDK access with streaming, filtering, and advanced controls.

## Available APIs

<CardGroup>
  <Card title="Chat Completions" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Web-grounded AI responses with citations, conversation context, and streaming support.
  </Card>

  <Card title="Agentic Research" icon="code" href="/docs/grounded-llm/responses/quickstart">
    Third-party models from OpenAI, Anthropic, Google, and more with presets and web search tools.
  </Card>

  <Card title="Search" icon="magnifying-glass" href="/docs/search/quickstart">
    Ranked web search results with filtering, multi-query support, and domain controls.
  </Card>
</CardGroup>

## Choosing the Right API

<AccordionGroup>
  <Accordion title="Use the Chat Completions API when..." icon="message">
    * You want **Perplexity's Sonar models** optimized for research and Q\&A
    * You need **built-in citations** and conversation context
    * You prefer **simplicity**—just send a message and get a researched answer

    **Best for:** AI assistants, research tools, Q\&A applications
  </Accordion>

  <Accordion title="Use the Agentic Research API when..." icon="code">
    * You need **multi-provider access** to OpenAI, Anthropic, Google, and more models through one API
    * You want **granular control** over model selection, reasoning, token budgets, and tools
    * You want **presets** for common use configurations or full customization for advanced workflows

    **Best for:** Agentic workflows, custom AI applications, multi-model experimentation
  </Accordion>

  <Accordion title="Use the Search API when..." icon="magnifying-glass">
    * You need **raw search results** without LLM processing
    * You want to **build custom AI workflows** with your own models
    * You need **search data** for indexing, analysis, or training

    **Best for:** Custom AI pipelines, data collection, search integration
  </Accordion>
</AccordionGroup>

## Generating an API Key

<Card title="Get your Perplexity API Key" icon="key" href="https://perplexity.ai/account/api">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

<Info>
  See the [API Groups](/docs/getting-started/api-groups) page to set up an API group.
</Info>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript/JavaScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```
</CodeGroup>

## Authentication

Set your API key as an environment variable:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

Or use a `.env` file in your project:

```bash .env theme={null}
PERPLEXITY_API_KEY=your_api_key_here
```

<Note>
  **OpenAI SDK Compatible:** Perplexity's API supports the OpenAI Chat Completions format. You can use OpenAI client libraries by pointing to our endpoint. See our [OpenAI Compatibility Guide](/docs/grounded-llm/openai-compatibility) for examples.
</Note>

## Making Your First API Call

Choose your API based on your use case:

<Tabs>
  <Tab title="Agentic Research API">
    Use for third-party models with web search tools and presets:

    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      client = Perplexity()

      # Make the API call with a preset
      response = client.responses.create(
          preset="pro-search",
          input="What are the latest developments in AI?"
      )

      # Print the AI's response
      print(response.output_text)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      const client = new Perplexity();

      // Make the API call with a preset
      const response = await client.responses.create({
          preset: "pro-search",
          input: "What are the latest developments in AI?"
      });

      // Print the AI's response
      console.log(response.output_text);
      ```

      ```bash cURL theme={null}
      curl https://api.perplexity.ai/v1/responses \
        -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "pro-search",
          "input": "What are the latest developments in AI?"
        }' | jq
      ```
    </CodeGroup>

    <Accordion title="Example Response">
      The response includes structured output with tool usage and citations:

      ```json theme={null}
      {
        "id": "resp_1234567890",
        "object": "response",
        "created_at": 1756485272,
        "model": "openai/gpt-5.1",
        "status": "completed",
        "output": [
          {
            "type": "message",
            "role": "assistant",
            "content": [
              {
                "type": "output_text",
                "text": "Recent developments in AI include...",
                "annotations": [
                  {
                    "type": "citation",
                    "url": "https://example.com/article1"
                  }
                ]
              }
            ]
          }
        ],
        "usage": {
          "input_tokens": 20,
          "output_tokens": 250,
          "total_tokens": 270
        }
      }
      ```
    </Accordion>
  </Tab>

  <Tab title="Chat Completions API">
    Use for web-grounded AI responses with Perplexity's Sonar models:

    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      client = Perplexity()

      # Make the API call
      completion = client.chat.completions.create(
          model="sonar-pro",
          messages=[
              {"role": "user", "content": "What are the latest developments in AI?"}
          ]
      )

      # Print the AI's response
      print(completion.choices[0].message.content)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      const client = new Perplexity();

      // Make the API call
      const completion = await client.chat.completions.create({
          model: "sonar-pro",
          messages: [
              { role: "user", content: "What are the latest developments in AI?" }
          ]
      });

      // Print the AI's response
      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl https://api.perplexity.ai/chat/completions \
        -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar-pro",
          "messages": [
            {
              "role": "user",
              "content": "What are the latest developments in AI?"
            }
          ]
        }' | jq
      ```
    </CodeGroup>

    <Accordion title="Example Response">
      The response includes the AI's answer with citations and search results:

      ```json theme={null}
      {
        "id": "66f3900f-e32e-4d59-b677-1a55de188262",
        "model": "sonar-pro",
        "created": 1756485272,
        "object": "chat.completion",
        "choices": [
          {
            "index": 0,
            "finish_reason": "stop",
            "message": {
              "role": "assistant",
              "content": "Recent developments in AI include...[1][2]"
            }
          }
        ],
        "usage": {
          "prompt_tokens": 12,
          "completion_tokens": 315,
          "total_tokens": 327
        },
        "citations": [
          "https://example.com/article1",
          "https://example.com/article2"
        ]
      }
      ```
    </Accordion>
  </Tab>
</Tabs>

## Streaming Responses

Enable streaming for real-time output with either API:

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      # Make the streaming API call
      stream = client.responses.create(
          preset="pro-search",
          input="Explain quantum computing",
          stream=True
      )

      # Process the streaming response
      for chunk in stream:
          if chunk.type == "response.output_text.delta":
              print(chunk.delta, end="", flush=True)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      // Make the streaming API call
      const stream = await client.responses.create({
          preset: "pro-search",
          input: "Explain quantum computing",
          stream: true
      });

      // Process the streaming response
      for await (const chunk of stream) {
          if (chunk.type === "response.output_text.delta") {
              process.stdout.write(chunk.delta);
          }
      }
      ```

      ```bash cURL theme={null}
      curl https://api.perplexity.ai/v1/responses \
        -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "pro-search",
          "input": "Explain quantum computing",
          "stream": true
        }'
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      # Make the streaming API call
      stream = client.chat.completions.create(
          model="sonar-pro",
          messages=[
              {"role": "user", "content": "Explain quantum computing"}
          ],
          stream=True
      )

      # Process the streaming response
      for chunk in stream:
          if chunk.choices[0].delta.content:
              print(chunk.choices[0].delta.content, end="")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      // Make the streaming API call
      const stream = await client.chat.completions.create({
          model: "sonar-pro",
          messages: [
              { role: "user", content: "Explain quantum computing" }
          ],
          stream: true
      });

      // Process the streaming response
      for await (const chunk of stream) {
          if (chunk.choices[0]?.delta?.content) {
              process.stdout.write(chunk.choices[0].delta.content);
          }
      }
      ```

      ```bash cURL theme={null}
      curl https://api.perplexity.ai/chat/completions \
        -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar-pro",
          "messages": [
            {
              "role": "user",
              "content": "Explain quantum computing"
            }
          ],
          "stream": true
        }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Info title="Complete Streaming Guide" href="/docs/grounded-llm/output-control/streaming-responses">
  For a full guide on streaming, including parsing, error handling, citation management, and best practices, see our [streaming guide](/docs/grounded-llm/output-control/streaming-responses).
</Info>

## Next Steps

Now that you've made your first API call, explore each API in depth:

<CardGroup>
  <Card title="Chat Completions API" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Get started with web-grounded AI responses
  </Card>

  <Card title="Agentic Research API" icon="code" href="/docs/grounded-llm/responses/quickstart">
    Get started with third-party models and presets
  </Card>

  <Card title="Search API" icon="magnifying-glass" href="/docs/search/quickstart">
    Get started with web search results
  </Card>
</CardGroup>

<CardGroup>
  <Card title="Perplexity SDK" icon="book" href="/docs/sdk/overview">
    Learn about the official Perplexity SDK with type safety and async support
  </Card>

  <Card title="Models" icon="brain" href="/docs/getting-started/models">
    Explore available models and their capabilities
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/chat-completions-post">
    View complete API documentation with detailed endpoint specifications
  </Card>

  <Card title="Examples" icon="play" href="/docs/cookbook/index">
    Explore code examples, tutorials, and integration patterns
  </Card>
</CardGroup>

<Info>
  Need help? Check out our [community](https://community.perplexity.ai) for support and discussions with other developers.
</Info>


# Academic Filter Guide
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/academic-filter



<Note>
  The `search_mode: "academic"` parameter allows you to tailor your searches specifically to academic and scholarly sources, prioritizing peer-reviewed papers, journal articles, and research publications.
</Note>

<Info>
  The `search_mode: "academic"` feature is currently only available in the Chat Completions API. For the Agentic Research API, use domain filters to target academic sources (e.g., `arxiv.org`, `scholar.google.com`).
</Info>

## Overview

The academic filter—sometimes referred to as "academic mode" or "Focus: Academic"—is a feature in Perplexity that allows users to target their searches specifically to academic and scholarly sources. This is especially useful for students, researchers, and professionals who require peer-reviewed papers, journal articles, and research-focused answers rather than general web content.

When you activate the academic filter by setting `search_mode: "academic"`, Perplexity prioritizes results from scholarly databases, journals, and reputable academic publications, filtering out non-academic or general web sources. This ensures that the answers you receive are grounded in research and scholarly consensus.

## Key Features and Functionality

* **Source Filtering**: Prioritizes scholarly databases, academic journals, and research publications
* **Research Focus**: Returns results based on peer-reviewed research rather than general web content
* **Enhanced Precision**: Provides more technical and discipline-specific information for academic queries
* **Compatibility**: Works with other search parameters like `search_context_size` to further refine results

## Usage Examples

### Basic Academic Search

This example shows how to perform a basic search using the academic filter.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[{"role": "user", "content": "What is the scientific name of the lions mane mushroom?"}],
      search_mode="academic",
      web_search_options={"search_context_size": "low"}
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar-pro",
    messages: [{"role": "user", "content": "What is the scientific name of the lions mane mushroom?"}],
    search_mode: "academic",
    web_search_options: {"search_context_size": "low"}
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "accept: application/json" \
    --header "authorization: Bearer $SONAR_API_KEY" \
    --header "content-type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "What is the scientific name of the lions mane mushroom?"}],
      "search_mode": "academic",
      "web_search_options": {"search_context_size": "low"}
  }' | jq
  ```
</CodeGroup>

### Combining Academic Mode with Other Parameters

You can combine the academic filter with other parameters for more refined searches:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar",
      messages=[{"role": "user", "content": "What are the latest findings on neural networks for image recognition?"}],
      search_mode="academic",
      search_after_date_filter="1/1/2023",
      web_search_options={"search_context_size": "high"}
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar",
    messages: [{"role": "user", "content": "What are the latest findings on neural networks for image recognition?"}],
    search_mode: "academic",
    search_after_date_filter: "1/1/2023",
    web_search_options: {"search_context_size": "high"}
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "accept: application/json" \
    --header "authorization: Bearer $SONAR_API_KEY" \
    --header "content-type: application/json" \
    --data '{
      "model": "sonar",
      "messages": [{"role": "user", "content": "What are the latest findings on neural networks for image recognition?"}],
      "stream": false,
      "search_mode": "academic",
      "search_after_date_filter": "1/1/2023",
      "web_search_options": {"search_context_size": "high"}
  }' | jq
  ```
</CodeGroup>

## Recommended Use Cases

The academic filter is particularly valuable for:

1. **Research Literature Reviews**: When you need to gather scholarly information on a specific topic
2. **Technical and Scientific Queries**: For questions requiring scientifically accurate, peer-reviewed answers
3. **Academic Writing Assistance**: When working on papers, theses, or dissertations that require scholarly sources
4. **Educational Support**: For students and educators requiring academically rigorous information

## Best Practices

### Optimizing Academic Searches

* **Be Specific**: Formulate clear, focused questions to receive more precise academic responses
* **Use Technical Terminology**: Include field-specific terms to better target relevant academic literature
* **Combine with Date Filters**: For the most recent research, combine with `search_after_date_filter`
* **Adjust Context Size**: Use higher `search_context_size` values for more comprehensive academic responses

### Performance Considerations

* Academic searches may sometimes take slightly longer due to the specialized nature of scholarly databases
* Consider using models like `sonar-deep-research` for particularly complex academic inquiries
* For more comprehensive literature reviews, set `stream: false` to receive complete responses

### Limitations

* Availability of academic sources varies by field and topic
* Very recent research (published within the last few months) may not always be included
* Some paywalled or subscription-only academic content may not be fully accessible

⸻


# Search Context Size
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/context-size



<Note>
  The `search_context_size` parameter allows you to control how much search context is retrieved from the web during query resolution, letting you balance cost and comprehensiveness.
</Note>

<Info>
  The `search_context_size` feature is currently only available in the Chat Completions API.
</Info>

<Warning>
  * Default `search_context_size` is `low`
  * Selecting `"high"` increases search costs due to more extensive web retrieval. Use `"low"` when cost efficiency is critical.
</Warning>

## Overview

The `search_context_size` field—passed via the `web_search_options` object—determines how much search context is retrieved by Grounded LLMs. This setting can help you optimize for either:

* Cost savings with minimal search input (`low`)
* Comprehensive answers by maximizing retrieved information (`high`)
* A balance of both (`medium`)

This flexibility allows teams to tune their API usage to their budget and use case.

To enable this feature, include the web\_search\_options.search\_context\_size parameter in your request payload:

```bash theme={null}
"web_search_options": {
  "search_context_size": "medium"
}
```

## Best Practices

**Choosing the Right Context Size**

* `low`: Best for short factual queries or when operating under strict token cost constraints.
* `medium`: The default and best suited for general use cases.
* `high`: Use for deep research, exploratory questions, or when citations and evidence coverage are critical.

**Cost Optimization**

* Selecting `low` or `medium` can significantly reduce overall token usage, especially at scale.
* Consider defaulting to `low` for high-volume endpoints and selectively upgrading to `high` for complex user prompts.

Combining with Other Filters

* You can use `search_context_size` alongside other features like `search_domain_filter` to further control the scope of search.
* Combining `medium` with a focused domain filter often gives a good tradeoff between quality and cost.

Performance Considerations

* Larger context sizes may slightly increase response latency due to more extensive search and reranking.
* If you’re batching queries or supporting real-time interfaces, test with different settings to balance user experience and runtime.

## Examples

**1. Minimal Search Context ("low")**

This option limits the search context retrieved for the model, reducing cost per request while still producing useful responses for simpler questions.

## Request

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "messages": [
        {
          "role": "system",
          "content": "Be precise and concise."
        },
        {
          "role": "user",
          "content": "How many stars are there in our galaxy?"
        }
      ],
      "web_search_options": {
        "search_context_size": "low"
      }
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar",
      messages=[
          {"role": "system", "content": "Be precise and concise."},
          {"role": "user", "content": "How many stars are there in our galaxy?"}
      ],
      web_search_options={
          "search_context_size": "low"
      }
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar",
    messages: [
      {"role": "system", "content": "Be precise and concise."},
      {"role": "user", "content": "How many stars are there in our galaxy?"}
    ],
    web_search_options: {
      "search_context_size": "low"
    }
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

**Pro-tip**: Use `low` when cost optimization is more important than answer completeness.

**2. Comprehensive Search Context ("high")**

This option maximizes the amount of search context used to answer the question, resulting in more thorough and nuanced responses.

## Request

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "messages": [
        {
          "role": "system",
          "content": "Be precise and concise."
        },
        {
          "role": "user",
          "content": "Explain the economic causes of the 2008 financial crisis."
        }
      ],
      "web_search_options": {
        "search_context_size": "high"
      }
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar",
      messages=[
          {"role": "system", "content": "Be precise and concise."},
          {"role": "user", "content": "Explain the economic causes of the 2008 financial crisis."}
      ],
      web_search_options={
          "search_context_size": "high"
      }
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar",
    messages: [
      {"role": "system", "content": "Be precise and concise."},
      {"role": "user", "content": "Explain the economic causes of the 2008 financial crisis."}
    ],
    web_search_options: {
      "search_context_size": "high"
    }
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

**Pro-tip**: Use `high` for research-heavy or nuanced queries where coverage matters more than cost.

⸻


# Language Filter Guide
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/language-filter



<Note>
  The `search_language_filter` parameter allows you to filter search results by language using ISO 639-1 language codes. Only results in the specified languages will be returned.
</Note>

<Info>
  Language codes must be valid 2-letter ISO 639-1 codes (e.g., "en", "ru", "fr"). You can filter by up to 10 languages per request.
</Info>

<Info>
  The `search_language_filter` feature is currently only available in the Chat Completions API.
</Info>

## Overview

The language filter for Grounded LLMs allows you to control which search results are returned by limiting them to specific languages. This is particularly useful when you need to:

* Generate responses based on content in specific languages
* Conduct multilingual research across multiple languages
* Focus on regional content in local languages
* Build language-specific applications or features

The `search_language_filter` parameter accepts an array of ISO 639-1 language codes and returns only results that match those languages.

To filter search results by language:

```bash theme={null}
"search_language_filter": ["en", "fr", "de"]
```

This filter will be applied in addition to any other search parameters.

## Examples

**1. Single Language Filter**

This example limits search results to English language content only.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Tell me about recent AI developments."}
      ],
      search_language_filter=["en"]
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar",
    messages: [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Tell me about recent AI developments."}
    ],
    search_language_filter: ["en"]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about recent AI developments."}
      ],
      "search_language_filter": ["en"]
    }' | jq
  ```
</CodeGroup>

**2. Multiple Language Filter**

Search across multiple languages to gather diverse perspectives or multilingual content:

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "What are the latest renewable energy innovations in Europe?"}
      ],
      search_language_filter=["en", "fr", "de"]
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar-pro",
    messages: [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What are the latest renewable energy innovations in Europe?"}
    ],
    search_language_filter: ["en", "fr", "de"]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the latest renewable energy innovations in Europe?"}
      ],
      "search_language_filter": ["en", "fr", "de"]
    }' | jq
  ```
</CodeGroup>

**3. Regional Language Research**

Focus on content from specific regions by using their local languages:

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for Asian market insights in local languages
  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "What are the technology market trends in East Asia?"}
      ],
      search_language_filter=["zh", "ja", "ko"]
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for Asian market insights in local languages
  const completion = await client.chat.completions.create({
    model: "sonar-pro",
    messages: [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What are the technology market trends in East Asia?"}
    ],
    search_language_filter: ["zh", "ja", "ko"]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the technology market trends in East Asia?"}
      ],
      "search_language_filter": ["zh", "ja", "ko"]
    }' | jq
  ```
</CodeGroup>

**4. Combining with Other Filters**

Language filters work seamlessly with other search parameters for precise control:

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Combine language filter with domain and date filters
  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "What are recent breakthroughs in quantum computing?"}
      ],
      search_language_filter=["en", "de"],
      search_domain_filter=["nature.com", "science.org", "arxiv.org"],
      search_recency_filter="month"
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Combine language filter with domain and date filters
  const completion = await client.chat.completions.create({
    model: "sonar-pro",
    messages: [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What are recent breakthroughs in quantum computing?"}
    ],
    search_language_filter: ["en", "de"],
    search_domain_filter: ["nature.com", "science.org", "arxiv.org"],
    search_recency_filter: "month"
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are recent breakthroughs in quantum computing?"}
      ],
      "search_language_filter": ["en", "de"],
      "search_domain_filter": ["nature.com", "science.org", "arxiv.org"],
      "search_recency_filter": "month"
    }' | jq
  ```
</CodeGroup>

## Parameter Reference

### `search_language_filter`

* **Type**: Array of strings
* **Format**: ISO 639-1 language codes (2 lowercase letters)
* **Description**: Filters search results to only include content in the specified languages
* **Optional**: Yes
* **Maximum**: 10 language codes per request
* **Example**: `"search_language_filter": ["en", "fr", "de"]`

## Common Language Codes

Here's a comprehensive list of frequently used ISO 639-1 language codes:

| Language   | Code | Language   | Code |
| ---------- | ---- | ---------- | ---- |
| English    | `en` | Portuguese | `pt` |
| Spanish    | `es` | Dutch      | `nl` |
| French     | `fr` | Polish     | `pl` |
| German     | `de` | Swedish    | `sv` |
| Italian    | `it` | Norwegian  | `no` |
| Russian    | `ru` | Danish     | `da` |
| Chinese    | `zh` | Finnish    | `fi` |
| Japanese   | `ja` | Czech      | `cs` |
| Korean     | `ko` | Hungarian  | `hu` |
| Arabic     | `ar` | Greek      | `el` |
| Hindi      | `hi` | Turkish    | `tr` |
| Bengali    | `bn` | Hebrew     | `he` |
| Indonesian | `id` | Thai       | `th` |
| Vietnamese | `vi` | Ukrainian  | `uk` |

<Tip>
  For a complete list of ISO 639-1 language codes, see the [ISO 639-1 standard](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
</Tip>

## Best Practices

### Language Code Validation

* **Use Valid Codes**: Always use valid 2-letter ISO 639-1 codes. Invalid codes will result in an API error.
* **Lowercase Only**: Language codes must be lowercase (e.g., "en" not "EN").
* **Client-Side Validation**: Validate language codes on the client side using a regex pattern:

<CodeGroup>
  ```python Python theme={null}
  import re

  def validate_language_code(code):
      pattern = r'^[a-z]{2}$'
      return bool(re.match(pattern, code))

  def validate_language_filters(codes):
      if len(codes) > 10:
          raise ValueError("Maximum 10 language codes allowed")
      
      for code in codes:
          if not validate_language_code(code):
              raise ValueError(f"Invalid language code: {code}")
      
      return True

  # Usage
  try:
      codes = ["en", "fr", "de"]
      validate_language_filters(codes)
      
      response = client.chat.completions.create(
          model="sonar",
          messages=[{"role": "user", "content": "technology news"}],
          search_language_filter=codes
      )
  except ValueError as e:
      print(f"Validation error: {e}")
  ```

  ```typescript TypeScript theme={null}
  function validateLanguageCode(code: string): boolean {
    const pattern = /^[a-z]{2}$/;
    return pattern.test(code);
  }

  function validateLanguageFilters(codes: string[]): void {
    if (codes.length > 10) {
      throw new Error("Maximum 10 language codes allowed");
    }
    
    for (const code of codes) {
      if (!validateLanguageCode(code)) {
        throw new Error(`Invalid language code: ${code}`);
      }
    }
  }

  // Usage
  try {
    const codes = ["en", "fr", "de"];
    validateLanguageFilters(codes);
    
    const response = await client.chat.completions.create({
      model: "sonar",
      messages: [{role: "user", content: "technology news"}],
      searchLanguageFilter: codes
    });
  } catch (error) {
    console.error("Validation error:", error.message);
  }
  ```
</CodeGroup>

### Strategic Language Selection

* **Be Specific**: Choose languages that are most relevant to your research or application needs.
* **Consider Your Audience**: Select languages that match your target audience's preferences.
* **Regional Relevance**: Combine language filters with geographic filters for better regional targeting.
* **Content Availability**: Some topics may have limited content in certain languages. Start broad and narrow down as needed.

### Performance Considerations

* **Filter Size**: While you can specify up to 10 languages, using fewer languages may improve response times.
* **Result Quality**: More languages mean a broader search scope, which can dilute result relevance. Be strategic about which languages to include.
* **Combination Effects**: Language filters combined with other restrictive filters (domain, date) may significantly reduce the number of results.

## Advanced Usage Patterns

### Multilingual Research

Conduct comprehensive research by searching across multiple languages:

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Research a global topic in multiple languages
languages = [
    ["en"],           # English-speaking countries
    ["zh", "ja"],     # East Asia
    ["es", "pt"],     # Latin America and Iberia
    ["fr", "de", "it"] # Western Europe
]

results_by_region = {}

for lang_group in languages:
    completion = client.chat.completions.create(
        model="sonar",
        messages=[
            {"role": "user", "content": "sustainable development goals progress"}
        ],
        search_language_filter=lang_group
    )
    results_by_region[", ".join(lang_group)] = completion

# Analyze results by language/region
for region, result in results_by_region.items():
    print(f"Results in {region}:")
    print(result.choices[0].message.content[:200])
    print("---")
```

### Content Localization Research

Find examples and references in target languages for localization projects:

```python theme={null}
# Generate insights from target market languages
target_languages = ["ja", "ko", "zh"]  # Asian markets

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {"role": "user", "content": "smartphone reviews 2024"}
    ],
    search_language_filter=target_languages,
    search_recency_filter="month"
)
```

### Academic Research Across Languages

Access scholarly content in different languages:

```python theme={null}
# Search for research papers in multiple languages
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {"role": "user", "content": "quantum computing algorithms"}
    ],
    search_language_filter=["en", "de", "fr", "ru"],
    search_domain_filter=["arxiv.org", "nature.com", "science.org"]
)
```

### News Monitoring by Language

Track news stories across different language regions:

```python theme={null}
# Monitor breaking news in different languages
news_queries = {
    "English": ["en"],
    "Chinese": ["zh"],
    "Spanish": ["es"],
    "Arabic": ["ar"]
}

for region, langs in news_queries.items():
    completion = client.chat.completions.create(
        model="sonar",
        messages=[
            {"role": "user", "content": "breaking news technology"}
        ],
        search_language_filter=langs,
        search_recency_filter="day"
    )
    print(f"{region} News:")
    print(completion.choices[0].message.content[:200])
    print("---")
```

## Error Handling

When using language filters, implement proper error handling for validation issues:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity, BadRequestError

  client = Perplexity()

  def safe_language_chat(query, languages):
      """
      Generate a response with language-filtered search and error handling.
      """
      try:
          # Validate language codes
          if not isinstance(languages, list):
              raise ValueError("Languages must be provided as a list")
          
          if len(languages) > 10:
              raise ValueError("Maximum 10 language codes allowed")
          
          # Validate each code format
          for lang in languages:
              if not isinstance(lang, str) or len(lang) != 2 or not lang.islower():
                  raise ValueError(f"Invalid language code format: {lang}")
          
          # Perform chat completion
          completion = client.chat.completions.create(
              model="sonar",
              messages=[{"role": "user", "content": query}],
              search_language_filter=languages
          )
          
          return completion
          
      except ValueError as e:
          print(f"Validation error: {e}")
          return None
      except BadRequestError as e:
          print(f"API error: {e.message}")
          return None
      except Exception as e:
          print(f"Unexpected error: {e}")
          return None

  # Usage
  result = safe_language_chat(
      "artificial intelligence trends",
      ["en", "fr", "de"]
  )

  if result:
      print(result.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  async function safeLanguageChat(
    query: string,
    languages: string[]
  ): Promise<any | null> {
    try {
      // Validate language codes
      if (!Array.isArray(languages)) {
        throw new Error("Languages must be provided as an array");
      }
      
      if (languages.length > 10) {
        throw new Error("Maximum 10 language codes allowed");
      }
      
      // Validate each code format
      for (const lang of languages) {
        if (typeof lang !== 'string' || 
            lang.length !== 2 || 
            lang !== lang.toLowerCase()) {
          throw new Error(`Invalid language code format: ${lang}`);
        }
      }
      
      // Perform chat completion
      const completion = await client.chat.completions.create({
        model: "sonar",
        messages: [{role: "user", content: query}],
        searchLanguageFilter: languages
      });
      
      return completion;
      
    } catch (error) {
      if (error instanceof Perplexity.BadRequestError) {
        console.error("API error:", error.message);
      } else if (error instanceof Error) {
        console.error("Error:", error.message);
      }
      return null;
    }
  }

  // Usage
  const result = await safeLanguageChat(
    "artificial intelligence trends",
    ["en", "fr", "de"]
  );

  if (result) {
    console.log(result.choices[0].message.content);
  }
  ```
</CodeGroup>

<Tip>
  For best results, combine language filtering with other filters like `search_domain_filter` or `search_recency_filter` to narrow down your search to highly relevant, timely content in your target languages.
</Tip>


# Web Search Control
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/search-control

Control when Sonar models search the web using the search classifier or by disabling search altogether.

## Overview

Grounded LLMs provide powerful web search capabilities, but there are times when you want to control when and how searches are performed. Perplexity offers two main approaches for search control:

* **Search Classifier** - Let AI intelligently decide when to search based on the query context
* **Disable Search** - Turn off web search completely for specific requests

<Info>
  Search control features (`enable_search_classifier` and `disable_search`) are currently only available in the Chat Completions API.
</Info>

<Warning>
  Pricing remains the same regardless of whether search is triggered or not. Search control features are designed for performance optimization and user experience, not cost reduction.
</Warning>

## Search Classifier

The search classifier is a trained model that automatically determines whether a web search is necessary based on the context and content of your query. This helps optimize performance and costs by only searching when beneficial.

### How It Works

The classifier analyzes your query and decides whether:

* **Search is needed** - For questions requiring current information, facts, or research
* **Search is unnecessary** - For creative tasks, math problems, or general knowledge that doesn't require real-time data

### When to Use Search Classifier

Use the search classifier when you want to:

* **Improve response speed** - Skip search for queries that don't benefit from it
* **Automatic intelligence** - Let AI decide the best approach for each query
* **Optimal user experience** - Ensure search is only used when it adds value

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    import requests

    # API configuration
    API_URL = "https://api.perplexity.ai/chat/completions"
    API_KEY = "your-api-key-here"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {API_KEY}",
        "content-type": "application/json"
    }

    # Query that benefits from search classifier
    user_query = "What are the latest developments in quantum computing?"

    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": user_query}],
        "stream": False,
        "enable_search_classifier": True
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    print(response.json())
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    interface ChatCompletionRequest {
      model: string;
      messages: Array<{role: string; content: string}>;
      stream?: boolean;
      enable_search_classifier?: boolean;
    }

    const API_URL = "https://api.perplexity.ai/chat/completions";
    const API_KEY = "your-api-key-here";

    const headers = {
      "accept": "application/json",
      "authorization": `Bearer ${API_KEY}`,
      "content-type": "application/json"
    };

    // Query that benefits from search classifier
    const userQuery = "What are the latest developments in quantum computing?";

    const payload: ChatCompletionRequest = {
      model: "sonar-pro",
      messages: [{role: "user", content: userQuery}],
      stream: false,
      enable_search_classifier: true
    };

    fetch(API_URL, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => console.log(data));
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -X POST "https://api.perplexity.ai/chat/completions" \
      -H "accept: application/json" \
      -H "authorization: Bearer $SONAR_API_KEY" \
      -H "content-type: application/json" \
      -d '{
        "model": "sonar",
        "messages": [
          {
            "role": "user", 
            "content": "What is 2+2?"
          }
        ],
        "stream": false,
        "enable_search_classifier": true
      }' | jq
    ```
  </Tab>
</Tabs>

### Search Classifier Examples

<AccordionGroup>
  <Accordion title="Queries that typically trigger search">
    * "What happened in the stock market today?"
    * "Latest news about renewable energy"
    * "Current weather in San Francisco"
    * "Recent research on machine learning"
  </Accordion>

  <Accordion title="Queries that typically skip search">
    * "What is 2 + 2?"
    * "Write a creative story about a dragon"
    * "Explain the concept of recursion"
    * "Generate a business name for a bakery"
  </Accordion>
</AccordionGroup>

## Disabling Search Completely

For certain use cases, you may want to disable web search entirely. This is useful when:

* **Offline-like responses** - Get responses based only on training data
* **Creative tasks** - Focus on generation without external influence
* **Deterministic responses** - Ensure consistent outputs based only on training data

### Implementation

To disable search completely, set the `disable_search` parameter to `true`:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    import requests

    # API configuration
    API_URL = "https://api.perplexity.ai/chat/completions"
    API_KEY = "your-api-key-here"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {API_KEY}",
        "content-type": "application/json"
    }

    # Query that doesn't need web search
    user_query = "What is 2 + 2?"

    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": user_query}],
        "stream": False,
        "disable_search": True
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    print(response.json())
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    interface ChatCompletionRequest {
      model: string;
      messages: Array<{role: string; content: string}>;
      stream?: boolean;
      disable_search?: boolean;
    }

    const API_URL = "https://api.perplexity.ai/chat/completions";
    const API_KEY = "your-api-key-here";

    const headers = {
      "accept": "application/json",
      "authorization": `Bearer ${API_KEY}`,
      "content-type": "application/json"
    };

    // Query that doesn't need web search
    const userQuery = "What is 2 + 2?";

    const payload: ChatCompletionRequest = {
      model: "sonar-pro",
      messages: [{role: "user", content: userQuery}],
      stream: false,
      disable_search: true
    };

    fetch(API_URL, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => console.log(data));
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -X POST "https://api.perplexity.ai/chat/completions" \
      -H "accept: application/json" \
      -H "authorization: Bearer your-api-key-here" \
      -H "content-type: application/json" \
      -d '{
        "model": "sonar-pro",
        "messages": [
          {
            "role": "user", 
            "content": "What is 2 + 2?"
          }
        ],
        "stream": false,
        "disable_search": true
      }'
    ```
  </Tab>
</Tabs>

<Warning>
  When search is disabled, responses will be based solely on the model's training data and may not include the most current information.
</Warning>

## Comparison and Best Practices

### When to Use Each Approach

<CardGroup>
  <Card title="Search Classifier" icon="brain">
    **Best for:**

    * Mixed workloads with varying query types
    * Performance optimization without manual intervention
    * General-purpose applications
    * Unknown query patterns
  </Card>

  <Card title="Disabled Search" icon="ban">
    **Best for:**

    * Creative content generation
    * Mathematical computations
    * Sensitive data processing
    * Offline-like experiences
  </Card>
</CardGroup>

### Performance Considerations

<Tabs>
  <Tab title="Response Time">
    **Search Classifier:** Variable response time depending on whether search is triggered

    **Disabled Search:** Consistently faster responses since no search operations occur
  </Tab>

  <Tab title="Information Accuracy">
    **Search Classifier:** Provides current information when search is triggered

    **Disabled Search:** Limited to training data cutoff date
  </Tab>
</Tabs>

## Complete Examples

### Search Classifier in Action

<Steps>
  <Step title="Set up the request with search classifier">
    ```python theme={null}
    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": "Explain machine learning"}],
        "enable_search_classifier": True
    }
    ```

    <Info>
      The classifier will likely skip search for this general concept explanation.
    </Info>
  </Step>

  <Step title="Try with a current events query">
    ```python theme={null}
    payload = {
        "model": "sonar-pro", 
        "messages": [{"role": "user", "content": "Latest AI news this week"}],
        "enable_search_classifier": True
    }
    ```

    <Check>
      The classifier will trigger search for this time-sensitive query.
    </Check>
  </Step>
</Steps>

### Creative Task with Disabled Search

Here's an example of using disabled search for creative content generation:

```python theme={null}
import requests

payload = {
    "model": "sonar-pro",
    "messages": [
        {
            "role": "user",
            "content": "Write a short science fiction story about time travel"
        }
    ],
    "disable_search": True
}

response = requests.post(
    "https://api.perplexity.ai/chat/completions",
    headers={
        "authorization": "Bearer your-api-key-here",
        "content-type": "application/json"
    },
    json=payload
)
```

## Troubleshooting

<AccordionGroup>
  <Accordion title="Search classifier not working as expected">
    **Common causes:**

    * API key doesn't have access to classifier features
    * Using an unsupported model
    * Incorrect parameter syntax

    **Solutions:**

    * Verify your API key permissions
    * Ensure you're using a Sonar model
    * Check parameter spelling: `enable_search_classifier`
  </Accordion>

  <Accordion title="Responses seem outdated with disabled search">
    This is expected behavior when search is disabled. The model can only use information from its training data.

    **Solutions:**

    * Re-enable search for queries requiring current information
    * Use search classifier for automatic optimization
    * Clearly document when search is disabled for your users
  </Accordion>
</AccordionGroup>

<Tip>
  Start with the search classifier for most applications, then selectively disable search for specific use cases where you want guaranteed offline-like behavior.
</Tip>


# SEC Filings Filter Guide
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/sec-guide



<Note>
  The `search_mode: "sec"` parameter allows you to tailor your searches specifically to U.S. Securities and Exchange Commission (SEC) filings, prioritizing official financial documents, disclosures, and regulatory filings from public companies.
</Note>

<Info>
  The `search_mode: "sec"` feature is currently only available in the Chat Completions API. For the Agentic Research API, use domain filters to target SEC sources (e.g., `sec.gov`).
</Info>

## Overview

The SEC filter allows users to target their searches specifically to official SEC filings. This is especially useful for investors, analysts, journalists, and professionals who require authoritative financial documents, such as 10-Ks, 10-Qs, 8-Ks, and other regulatory filings, rather than general web content or news articles.

When you activate the SEC filter by setting `search_mode: "sec"`, Perplexity limits results to the SEC's EDGAR database and other reputable sources of regulatory filings, filtering out non-official or general web sources. This ensures that the answers you receive are grounded in official disclosures and regulatory compliance.

## Key Features and Functionality

* **Source Filtering**: Prioritizes SEC filings such as 10-K, 10-Q, 8-K, S-1, and more
* **Regulatory Focus**: Returns results based on official financial and regulatory documents
* **Enhanced Precision**: Provides more accurate and up-to-date information for financial and compliance queries

## Usage Examples

### Basic SEC Filings Search

This example shows how to perform a basic search using the SEC filter.

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "accept: application/json" \
    --header "authorization: Bearer $SONAR_API_KEY" \
    --header "content-type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "Prepare me for markets opening."}],
      "search_mode": "sec"
    }' | jq
  ```

  ```python Python theme={null}
  import requests

  url = "https://api.perplexity.ai/chat/completions"
  headers = {
      "accept": "application/json",
      "authorization": "Bearer YOUR_API_KEY",
      "content-type": "application/json"
  }
  payload = {
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "Prepare me for markets opening."}],
      "search_mode": "sec"
  }'

  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```

  ```javascript Node.js theme={null}
  const axios = require('axios');

  const url = "https://api.perplexity.ai/chat/completions";
  const headers = {
    "accept": "application/json",
    "authorization": "Bearer YOUR_API_KEY",
    "content-type": "application/json"
  };
  const payload = {
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": "Prepare me for markets opening."}],
    "stream": false,
    "search_mode": "sec"
  };

  axios.post(url, payload, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
  ```
</CodeGroup>

### Combining SEC Mode with Other Parameters

You can combine the SEC filter with other parameters for more refined searches:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "accept: application/json" \
    --header "authorization: Bearer $SONAR_API_KEY" \
    --header "content-type: application/json" \
    --data '{
      "model": "sonar",
      "messages": [{"role": "user", "content": "Summarize the latest 10-K filings for Apple Inc."}],
      "stream": false,
      "search_mode": "sec",
      "search_after_date_filter": "1/1/2023"
  }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar",
      messages=[{"role": "user", "content": "Summarize the latest 10-K filings for Apple Inc."}],
      search_mode="sec",
      search_after_date_filter="1/1/2023"
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar",
    messages: [{"role": "user", "content": "Summarize the latest 10-K filings for Apple Inc."}],
    search_mode: "sec",
    search_after_date_filter: "1/1/2023"
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

## Recommended Use Cases

The SEC filter is particularly valuable for:

1. **Financial Analysis**: When you need to review official financial statements and disclosures
2. **Regulatory Compliance**: For questions requiring up-to-date regulatory filings and compliance information
3. **Market Research**: When tracking company events, earnings, and risk factors
4. **Due Diligence**: For investors and analysts evaluating public companies

## Best Practices

### Optimizing SEC Filings Searches

* **Be Specific**: Reference the type of filing (e.g., 10-K, 8-K) and company name for more precise results
* **Use Financial Terminology**: Include terms like "earnings," "risk factors," or "management discussion" to target relevant sections
* **Combine with Date Filters**: For the most recent filings, combine with `search_after_date_filter`
* **Adjust Context Size**: Use higher `search_context_size` values for more comprehensive responses

### Limitations

* Availability is limited to filings made public through the SEC's EDGAR system
* Some filings may be delayed or amended after initial publication
* Only covers U.S. public companies and registered entities

⸻


# File Attachments with Sonar
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/media/file-attachments

Learn how to upload and analyze documents (PDF, DOC, DOCX, TXT, RTF) using Sonar models

## Overview

Sonar models support document analysis through file uploads. You can provide files either as URLs to publicly accessible documents or as base64 encoded bytes. Ask questions about document content, get summaries, extract information, and perform detailed analysis of uploaded files in multiple formats including PDF, DOC, DOCX, TXT, and RTF.

<Note>
  Document files can be provided as:

  * A public URL pointing to the file
  * Base64 encoded bytes (without any prefix)

  Supported formats: PDF, DOC, DOCX, TXT, RTF.
</Note>

<Warning>
  The maximum file size is 50MB. Files larger than this limit will not be processed.
</Warning>

## Supported Features

* **Document Summarization**: Get concise summaries of document content
* **Question Answering**: Ask specific questions about the document
* **Content Extraction**: Extract key information, data, and insights
* **Multi-language Support**: Analyze documents in various languages
* **Large Document Handling**: Process lengthy documents efficiently
* **Multiple Formats**: Support for PDF, DOC, DOCX, TXT, and RTF files

## Basic Usage

### Simple Document Analysis

#### Using a Public URL

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.perplexity.ai/chat/completions" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        {
          "content": [
            {
              "type": "text",
              "text": "Summarize this document"
            },
            {
              "type": "file_url",
              "file_url": {
                "url": "https://example.com/document.pdf"
              },
            }
          ],
          "role": "user"
        }
      ],
      "model": "sonar-pro"
    }'
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
  client = Perplexity()

  # Analyze the document
  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Summarize this document"
                  },
                  {
                      "type": "file_url",
                      "file_url": {
                          "url": "https://example.com/document.pdf"
                      },
                  }
              ]
          }
      ]
  )

  # Print the response
  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client (uses PERPLEXITY_API_KEY environment variable)
  const client = new Perplexity();

  // Analyze the document
  const completion = await client.chat.completions.create({
      model: 'sonar-pro',
      messages: [
          {
              role: 'user',
              content: [
                  {
                      type: 'text',
                      text: 'Summarize this document'
                  },
                  {
                      type: 'file_url',
                      file_url: {
                          url: 'https://example.com/document.pdf'
                      },
                      file_name: 'document.pdf'
                  }
              ]
          }
      ]
  });

  // Print the response
  console.log(completion.choices[0].message.content);
  ```

  ```go Go theme={null}
  package main

  import (
      "bytes"
      "encoding/json"
      "fmt"
      "net/http"
  )

  func main() {
      url := "https://api.perplexity.ai/chat/completions"
      
      payload := map[string]interface{}{
          "messages": []map[string]interface{}{
              {
                  "content": []map[string]interface{}{
                      {
                          "type": "text",
                          "text": "Summarize this document",
                      },
                      {
                          "type": "file_url",
                          "file_url": map[string]string{
                              "url": "https://example.com/document.pdf",
                          },
                      },
                  },
                  "role": "user",
              },
          },
          "model": "sonar-pro",
      }
      
      jsonData, _ := json.Marshal(payload)
      req, _ := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
      req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
      req.Header.Set("Content-Type", "application/json")
      
      client := &http.Client{}
      resp, _ := client.Do(req)
  }
  ```
</CodeGroup>

#### Using Base64 Encoded Bytes

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.perplexity.ai/chat/completions" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        {
          "content": [
            {
              "type": "text",
              "text": "Summarize this document"
            },
            {
              "type": "file_url",
              "file_url": {
                "url": "JVBERi0xLjQKJeLjz9MKNCAwIG9iago..."
              },
              "file_name": "report.pdf"
            }
          ],
          "role": "user"
        }
      ],
      "model": "sonar-pro"
    }'
  ```

  ```python Python theme={null}
  from perplexity import Perplexity
  import base64

  # Initialize the client
  client = Perplexity()

  # Read and encode file
  with open("document.pdf", "rb") as file:
      file_data = file.read()
      encoded_file = base64.b64encode(file_data).decode('utf-8')

  # Analyze the document
  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Summarize this document"
                  },
                  {
                      "type": "file_url",
                      "file_url": {
                          "url": encoded_file  # Just the base64 string, no prefix
                      },
                  }
              ]
          }
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');
  const fs = require('fs');

  // Initialize the client
  const client = new Perplexity();

  // Read and encode file
  const fileData = fs.readFileSync('document.pdf');
  const encodedFile = fileData.toString('base64');

  // Analyze the document
  const completion = await client.chat.completions.create({
      model: 'sonar-pro',
      messages: [
          {
              role: 'user',
              content: [
                  {
                      type: 'text',
                      text: 'Summarize this document'
                  },
                  {
                      type: 'file_url',
                      file_url: {
                          url: encodedFile  // Just the base64 string, no prefix
                      },
                      file_name: 'document.pdf'
                  }
              ]
          }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

### Advanced Analysis with Web Search

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.perplexity.ai/chat/completions" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        {
          "content": [
            {
              "type": "text",
              "text": "What are the key findings in this research paper? Provide additional context from recent studies."
            },
            {
              "type": "file_url",
              "file_url": {
                "url": "https://example.com/research-paper.pdf"
              },
              "file_name": "research-paper.pdf"
            }
          ],
          "role": "user"
        }
      ],
      "model": "sonar-pro"
    }'
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Analyze the document with web search
  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "What are the key findings in this research paper? Provide additional context from recent studies."
                  },
                  {
                      "type": "file_url",
                      "file_url": {
                          "url": "https://example.com/research-paper.pdf"
                      },
                      "file_name": "research-paper.pdf"
                  }
              ]
          }
      ]
  )

  # Print the response
  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Analyze the document with web search
  const completion = await client.chat.completions.create({
      model: 'sonar-pro',
      messages: [
          {
              role: 'user',
              content: [
                  {
                      type: 'text',
                      text: 'What are the key findings in this research paper? Provide additional context from recent studies.'
                  },
                  {
                      type: 'file_url',
                      file_url: {
                          url: 'https://example.com/research-paper.pdf'
                      },
                      file_name: 'research-paper.pdf'
                  }
              ]
          }
      ]
  });

  // Print the response
  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

## File Requirements

<CardGroup>
  <Card title="Format Support" icon="check">
    * PDF files (.pdf extension)
    * Word documents (.doc, .docx extensions)
    * Text files (.txt extension)
    * Rich Text Format (.rtf extension)
    * Text-based documents (not scanned images)
    * Base64 encoded file bytes
    * Password-protected files (if publicly accessible)
  </Card>

  <Card title="Size Limits" icon="scale-balanced">
    * Maximum file size: 50MB per file
    * Maximum files per request: 30 files
    * Recommended: Under 50MB for optimal performance
    * Maximum processing time: 60 seconds
    * Large files may take longer to analyze
  </Card>
</CardGroup>

## Common Use Cases

### Academic Research

```python theme={null}
question = "What methodology was used in this study and what were the main conclusions?"
```

### Legal Documents

```python theme={null}
question = "Extract the key terms and conditions from this contract"
```

### Financial Reports

```python theme={null}
question = "What are the revenue trends and key financial metrics mentioned?"
```

### Technical Documentation

```python theme={null}
question = "Explain the implementation details and provide a step-by-step guide"
```

## Best Practices

<AccordionGroup>
  <Accordion title="Optimize Your Questions">
    * Be specific about what information you need
    * Ask one focused question per request for best results
    * Use follow-up questions to dive deeper into specific sections
  </Accordion>

  <Accordion title="Prepare Your Documents">
    * Ensure documents are text-based, not scanned images
    * For URLs: Use publicly accessible URLs (Google Drive, Dropbox, etc.)
    * For URLs: Verify the URL returns the document directly, not a preview page
    * For base64: Encode the entire file content properly
    * For base64: Provide only the base64 string without any prefix (no `data:` URI scheme)
  </Accordion>

  <Accordion title="Handle Large Documents">
    * Break down complex questions into smaller parts
    * Consider processing large documents in sections
    * Use streaming for real-time responses on lengthy analyses
  </Accordion>
</AccordionGroup>

## Error Handling

### Common Issues

| Error                | Cause                                | Solution                                                  |
| -------------------- | ------------------------------------ | --------------------------------------------------------- |
| `Invalid URL`        | URL not accessible or invalid base64 | Verify URL returns file directly or check base64 encoding |
| `File too large`     | File exceeds 50MB limit              | Compress or split the document                            |
| `Processing timeout` | Document too complex                 | Simplify question or use smaller sections                 |
| `Invalid base64`     | Malformed base64 string              | Ensure proper base64 encoding without prefix              |

## Pricing

PDF analysis follows standard Sonar pricing based on:

* Input tokens (document content + question)
* Output tokens (AI response)
* Web search usage (if enabled)

<Tip>
  Large documents consume more input tokens. Consider the document size when estimating costs.
</Tip>


# Returning Images
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/media/returning-images

Control image results with domain and format filters using Sonar models

## Overview

Grounded LLMs can return images as part of their responses to enhance the information provided. You can control which images are returned using domain and format filters, giving you fine-grained control over the sources and file types of image results. The `image_domain_filter` and `image_format_filter` parameters allow you to control the sources and file types of image results returned by Grounded LLMs. You can include a maximum of 10 entries in each of the filter lists, and these filters apply only when `"return_images": true` is set in your request.

<Info>
  The `return_images` feature is currently only available in the Chat Completions API.
</Info>

## Filter Types

### Domain Filtering

The `image_domain_filter` parameter controls which image sources are included or excluded:

* **Exclude domains**: Prefix with `-` (e.g., `-gettyimages.com`)
* **Include domains**: Use domain name directly (e.g., `wikimedia.org`)

### Format Filtering

The `image_format_filter` parameter restricts results to specific file formats:

* Use lowercase file extensions: `gif`, `jpg`, `png`, `webp`
* Omit the dot prefix: use `gif`, not `.gif`

## Basic Usage

To enable image returns, your request must include `"return_images": true`.

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "return_images": true,
      "messages": [
        {"role": "user", "content": "Show me images of Mount Everest"}
      ]
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Request with image returns enabled
  completion = client.chat.completions.create(
      model="sonar",
      return_images=True,
      messages=[
          {"role": "user", "content": "Show me images of Mount Everest"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Request with image returns enabled
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      messages: [
          { role: 'user', content: 'Show me images of Mount Everest' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Initialize the client
  const client = new Perplexity();

  // Request with image returns enabled
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      messages: [
          { role: 'user', content: 'Show me images of Mount Everest' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

## Filtering Examples

### 1. Exclude Specific Image Domains

Filter out images from specific providers like Getty Images:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "return_images": true,
      "image_domain_filter": ["-gettyimages.com"],
      "messages": [
        {"role": "user", "content": "What is the weather like today in London?"}
      ]
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Exclude Getty Images from results
  completion = client.chat.completions.create(
      model="sonar",
      return_images=True,
      image_domain_filter=["-gettyimages.com"],
      messages=[
          {"role": "user", "content": "Show me images of Mount Everest"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Exclude Getty Images from results
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_domain_filter: ['-gettyimages.com'],
      messages: [
          { role: 'user', content: 'Show me images of Mount Everest' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Initialize the client
  const client = new Perplexity();

  // Exclude Getty Images from results
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_domain_filter: ['-gettyimages.com'],
      messages: [
          { role: 'user', content: 'Show me images of Mount Everest' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

### 2. Only Return GIFs

Restrict results to GIF images only:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "return_images": true,
      "image_format_filter": ["gif"],
      "messages": [
        {"role": "user", "content": "Show me a funny cat gif"}
      ]
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Only return GIF images
  completion = client.chat.completions.create(
      model="sonar",
      return_images=True,
      image_format_filter=["gif"],
      messages=[
          {"role": "user", "content": "Show me a funny cat gif"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Only return GIF images
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_format_filter: ['gif'],
      messages: [
          { role: 'user', content: 'Show me a funny cat gif' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Initialize the client
  const client = new Perplexity();

  // Only return GIF images
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_format_filter: ['gif'],
      messages: [
          { role: 'user', content: 'Show me a funny cat gif' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

### 3. Combine Domain and Format Filters

Use both filters together for precise control:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "return_images": true,
      "image_domain_filter": ["-gettyimages.com"],
      "image_format_filter": ["gif"],
      "messages": [
        {"role": "user", "content": "Show me a gif of a dog"}
      ]
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Combine domain and format filtering
  completion = client.chat.completions.create(
      model="sonar",
      return_images=True,
      image_domain_filter=["-gettyimages.com"],
      image_format_filter=["gif"],
      messages=[
          {"role": "user", "content": "Show me a gif of a dog"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Combine domain and format filtering
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_domain_filter: ['-gettyimages.com'],
      image_format_filter: ['gif'],
      messages: [
          { role: 'user', content: 'Show me a gif of a dog' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Initialize the client
  const client = new Perplexity();

  // Combine domain and format filtering
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_domain_filter: ['-gettyimages.com'],
      image_format_filter: ['gif'],
      messages: [
          { role: 'user', content: 'Show me a gif of a dog' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

## Advanced Filtering

### Multiple Domain Exclusions

```python theme={null}
# Exclude multiple image providers
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_domain_filter=["-gettyimages.com", "-shutterstock.com", "-stockphoto.com"],
    messages=[
        {"role": "user", "content": "Show me nature photography"}
    ]
)
```

### Multiple Format Types

```python theme={null}
# Allow multiple image formats
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_format_filter=["jpg", "png", "webp"],
    messages=[
        {"role": "user", "content": "Show me high-quality landscape images"}
    ]
)
```

### Include Specific Domains

```python theme={null}
# Include only Wikipedia images
completion = client.chat.completions.create(
    model="sonar", 
    return_images=True,
    image_domain_filter=["wikimedia.org"],
    messages=[
        {"role": "user", "content": "Show me historical images"}
    ]
)
```

## Common Use Cases

### Educational Content

```python theme={null}
# Get educational images from trusted sources
image_domain_filter = ["wikimedia.org", "nasa.gov", "archive.org"]
image_format_filter = ["jpg", "png"]
```

### Creative Projects

```python theme={null}
# Get animated content for presentations
image_format_filter = ["gif", "webp"]
image_domain_filter = ["-gettyimages.com", "-shutterstock.com"]  # Avoid watermarked images
```

### High-Quality Photography

```python theme={null}
# Focus on professional photography formats
image_format_filter = ["jpg", "png"]
image_domain_filter = ["-lowres.com", "-thumbnail.com"]  # Exclude low-quality sources
```

## Best Practices

<AccordionGroup>
  <Accordion title="Domain Filtering Strategy">
    * Use simple domain names like `example.com` or `-gettyimages.com`
    * Do not include `http://`, `https://`, or subdomains
    * Mix inclusion and exclusion in domain filters for precise control
    * Keep lists short (≤10 entries) for performance and relevance
  </Accordion>

  <Accordion title="Format Filtering Guidelines">
    * File extensions must be lowercase: `["jpg"]`, not `["JPG"]`
    * Omit dot prefix: use `gif`, not `.gif`
    * Consider your use case: GIFs for animation, PNG for transparency, JPG for photos
    * WebP offers good compression but may have limited compatibility
  </Accordion>

  <Accordion title="Performance Optimization">
    * Filters may slightly increase response time
    * Overly restrictive filters may reduce result quality or quantity
    * Test different filter combinations to find the right balance
    * Monitor response times with different filter configurations
  </Accordion>
</AccordionGroup>

## Filter Reference

### Supported Image Formats

| Format | Extension | Best For                              |
| ------ | --------- | ------------------------------------- |
| JPEG   | `jpg`     | Photographs, complex images           |
| PNG    | `png`     | Screenshots, images with transparency |
| WebP   | `webp`    | Modern format with good compression   |
| GIF    | `gif`     | Animated images, simple graphics      |

### Common Domain Exclusions

| Domain              | Type         | Reason                    |
| ------------------- | ------------ | ------------------------- |
| `-gettyimages.com`  | Stock Photos | Watermarked content       |
| `-shutterstock.com` | Stock Photos | Watermarked content       |
| `-istockphoto.com`  | Stock Photos | Watermarked content       |
| `-pinterest.com`    | Social Media | Mixed quality/attribution |

<Tip>
  Start with broad filters and gradually refine them based on the quality and relevance of returned images.
</Tip>

## Limitations

<Warning>
  * Maximum of 30 images can be returned per response
  * Maximum of 10 entries in each filter list
  * Filters only apply when `"return_images": true` is set
  * Some domains may not be filterable due to CDN usage
  * Very restrictive filters may result in no images being returned
</Warning>


# Returning Videos
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/media/returning-videos

Learn how to return videos in API responses using media_response overrides with raw HTTP requests

## Overview

Grounded LLMs can return videos as part of their responses to provide rich multimedia content that enhances the information delivered. You can control video returns using the `media_response` parameter with `overrides` to specify when videos should be included in responses.

<Info>
  The `return_videos` feature is currently only available in the Chat Completions API.
</Info>

<Note>
  Use the `media_response.overrides.return_videos` parameter to control when videos are returned in API responses.
</Note>

<Warning>
  Video returns may increase response size and processing time. Use this feature selectively for queries where video content adds significant value.
</Warning>

## Basic Usage

To enable video returns, include the `media_response` parameter with `overrides.return_videos` set to `true` in your request.

### Simple Video Request

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "media_response": {
        "overrides": {
          "return_videos": true
        }
      },
      "messages": [
        {
          "role": "user",
          "content": "2024 Olympics highlights"
        }
      ]
    }' | jq
  ```

  ```python Python theme={null}
  import requests
  import json
  import os

  url = "https://api.perplexity.ai/chat/completions"
  headers = {
      "Authorization": f"Bearer {os.environ['PERPLEXITY_API_KEY']}",
      "Content-Type": "application/json"
  }

  data = {
      "model": "sonar-pro",
      "media_response": {
          "overrides": {
              "return_videos": True
          }
      },
      "messages": [
          {
              "role": "user",
              "content": "2024 Olympics highlights"
          }
      ]
  }

  response = requests.post(url, headers=headers, json=data)
  result = response.json()
  print(json.dumps(result, indent=2))
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.perplexity.ai/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.PERPLEXITY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'sonar-pro',
      media_response: {
        overrides: {
          return_videos: true
        }
      },
      messages: [
        {
          role: 'user',
          content: '2024 Olympics highlights'
        }
      ]
    })
  });

  const result = await response.json();
  console.log(JSON.stringify(result, null, 2));
  ```
</CodeGroup>

<AccordionGroup>
  <Accordion title="Sample Response">
    ```json theme={null}
    {
      "id": "58dee6e4-d2de-4d7e-910f-4048caa6903d",
      "model": "sonar-pro",
      "created": 1758844959,
      "usage": {
        "prompt_tokens": 6,
        "completion_tokens": 542,
        "total_tokens": 548,
        "search_context_size": "low",
        "cost": {
          "input_tokens_cost": 0.0,
          "output_tokens_cost": 0.008,
          "request_cost": 0.006,
          "total_cost": 0.014
        }
      },
      "citations": [
        "https://en.wikipedia.org/wiki/2024_Summer_Olympics",
        "https://www.teamusa.com/news/2024/august/13/top-moments-from-the-paris-2024-olympic-games",
        "https://www.nbcolympics.com/news/olympic-track-and-field-paris-2024-biggest-stories-replays-medal-results-top-athletes-new",
        "https://www.youtube.com/watch?v=WajxULWXIFE",
        "https://www.nbcolympics.com/news/olympic-gymnastics-paris-2024-biggest-stories-replays-medal-results-top-athletes-new-records",
        "https://www.youtube.com/watch?v=vy6FivZHRjQ",
        "https://www.espn.com/olympics/story/_/id/40813327/2024-paris-summer-olympics-live-updates-highlights-results-sunday-closing-ceremony",
        "https://www.youtube.com/watch?v=q4Mujt1wer4",
        "https://www.youtube.com/olympics",
        "https://www.youtube.com/watch?v=OFCVkSQYTjA",
        "https://www.youtube.com/watch?v=7Xnr805bm4E",
        "https://www.nbcolympics.com/videos"
      ],
      "search_results": [
        {
          "title": "2024 Summer Olympics - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/2024_Summer_Olympics",
          "date": "2006-03-05",
          "last_updated": "2025-09-24",
          "snippet": "Paris 2024 featured the debut of breaking as an Olympic sport, and was the final Olympic Games held during the IOC presidency of Thomas Bach. The 2024 Games ..."
        },
        {
          "title": "Top Moments From the Paris 2024 Olympic Games | Team USA",
          "url": "https://www.teamusa.com/news/2024/august/13/top-moments-from-the-paris-2024-olympic-games",
          "date": "2024-08-13",
          "last_updated": "2025-09-25",
          "snippet": "Scottie Scheffler wins his first Olympic Gold Medal | Golf · Victor Montalvo Takes Bronze in Breaking | Breaking · Brooke Raboutou Secures Her ..."
        },
        {
          "title": "Olympic track and field at Paris 2024: Biggest stories, replays, medal ...",
          "url": "https://www.nbcolympics.com/news/olympic-track-and-field-paris-2024-biggest-stories-replays-medal-results-top-athletes-new",
          "date": "2024-08-11",
          "last_updated": "2024-08-11",
          "snippet": "In the Paris Olympic men's 100m final, Lyles edged past Jamaican Kishane Thompson to win his first Olympic gold medal in a lifetime-best 9.784 ..."
        },
        {
          "title": "When Every Millisecond Counts at the Olympics | Top Moments",
          "url": "https://www.youtube.com/watch?v=WajxULWXIFE",
          "date": "2025-01-31",
          "last_updated": "2025-07-29",
          "snippet": "Re-live ALL the incredible #Paris2024 action: ➡️ https://oly.ch/P24Replays The most thrilling finishes of the Olympic Games in Paris 2024 ..."
        },
        {
          "title": "Olympic gymnastics at Paris 2024: Biggest stories, replays, medal ...",
          "url": "https://www.nbcolympics.com/news/olympic-gymnastics-paris-2024-biggest-stories-replays-medal-results-top-athletes-new-records",
          "date": "2024-08-11",
          "last_updated": "2024-08-11",
          "snippet": "Here's a look back at all the action, from highlights to medal results and everything in between. FULL EVENT REPLAYS:ARTISTIC GYMNASTICS"
        },
        {
          "title": "Best of Olympic Games Paris 2024 - YouTube",
          "url": "https://www.youtube.com/watch?v=vy6FivZHRjQ",
          "date": "2024-10-21",
          "last_updated": "2025-07-27",
          "snippet": "the Paris 2024 Olympics! From jaw-dropping athletic feats to ... highlights, including iconic victories, emotional celebrations, and ..."
        },
        {
          "title": "2024 Olympics: Highlights from Sunday in Paris - ESPN",
          "url": "https://www.espn.com/olympics/story/_/id/40813327/2024-paris-summer-olympics-live-updates-highlights-results-sunday-closing-ceremony",
          "date": "2024-08-11",
          "last_updated": "2024-08-11",
          "snippet": "The US Olympic run concluded with Team USA becoming the first team in any sport to win eight consecutive Olympic gold medals with a win over France."
        },
        {
          "title": "Moments that Left Us SPEECHLESS at Paris 2024! ❤️   - YouTube",
          "url": "https://www.youtube.com/watch?v=q4Mujt1wer4",
          "date": "2025-01-13",
          "last_updated": "2025-08-29",
          "snippet": "I'll always love the moment between Tara Davis-Woodhall and her husband Hunter Woodhall, who'd later snag his first gold medal in the Paralympics later on."
        },
        {
          "title": "Olympics - YouTube",
          "url": "https://www.youtube.com/olympics",
          "date": "2025-03-24",
          "last_updated": "2025-03-26",
          "snippet": "Witness the power, dedication, and skill of Olympic athletes as they compete for their chance to shine on the world stage."
        },
        {
          "title": "‍♂️ Best Athletics Moments at #Paris2024 ‍     - YouTube",
          "url": "https://www.youtube.com/watch?v=OFCVkSQYTjA",
          "date": "2025-03-30",
          "last_updated": "2025-07-29",
          "snippet": "Receive the best athletics moments at the olympic games in Paris 2024 ♂️. #Paris2024 ..."
        },
        {
          "title": "Men's 100m Final | Paris Champions - YouTube",
          "url": "https://www.youtube.com/watch?v=7Xnr805bm4E",
          "date": "2024-08-11",
          "last_updated": "2025-07-28",
          "snippet": "Re-live ALL the incredible #Paris2024 action: https://oly.ch/P24Replays Watch Noah Lyles of Team USA celebrate his gold medal victory ..."
        },
        {
          "title": "All Highlights | NBC Olympics",
          "url": "https://www.nbcolympics.com/videos",
          "date": "2025-09-24",
          "last_updated": "2025-09-25",
          "snippet": "All Highlights · Melissa Jefferson-Wooden claps her hands in joy after winning the world women's 200m final · Three runners prepare to cross the finish line in ..."
        }
      ],
      "videos": [
        {
          "url": "https://www.youtube.com/watch?v=lmPuoxNSRr4",
          "duration": null,
          "thumbnail_width": 480,
          "thumbnail_height": 360,
          "thumbnail_url": "https://www.youtube.com/watch?v=lmPuoxNSRr4"
        },
        {
          "url": "https://www.youtube.com/watch?v=cptEWh0yT4E",
          "duration": null,
          "thumbnail_width": 480,
          "thumbnail_height": 360,
          "thumbnail_url": "https://www.youtube.com/watch?v=cptEWh0yT4E"
        },
        {
          "url": "https://www.youtube.com/watch?v=6bhS_AUKjtc",
          "duration": null,
          "thumbnail_width": 480,
          "thumbnail_height": 360,
          "thumbnail_url": "https://www.youtube.com/watch?v=6bhS_AUKjtc"
        },
        {
          "url": "https://www.youtube.com/watch?v=vy6FivZHRjQ",
          "duration": null,
          "thumbnail_width": 480,
          "thumbnail_height": 360,
          "thumbnail_url": "https://www.youtube.com/watch?v=vy6FivZHRjQ"
        },
        {
          "url": "https://www.youtube.com/watch?v=WajxULWXIFE",
          "duration": null,
          "thumbnail_width": 480,
          "thumbnail_height": 360,
          "thumbnail_url": "https://www.youtube.com/watch?v=WajxULWXIFE"
        }
      ],
      "object": "chat.completion",
      "choices": [
        {
          "index": 0,
          "finish_reason": "stop",
          "message": {
            "role": "assistant",
            "content": "The 2024 Summer Olympics in Paris were marked by major milestones, standout athletic performances, record medal hauls, and historic firsts[1][2][3][6].\n\n**Key highlights:**\n\n- **Medal Table Leaders:** The United States and China finished tied with 40 gold medals each, but the U.S. claimed the top spot overall with 126 total medals; China followed with 91 total[1][2]. It was the first time the two Olympic powers tied in golds. Japan (20 golds), Australia (18 golds), and host nation France (16 golds) rounded out the top five[1].\n\n- **Breakdancing Debut:** Paris 2024 introduced **breaking** (breakdancing) as an Olympic sport for the first time[1].\n\n- **Athletics Dominance:** The U.S. displayed overwhelming strength in **track and field**, securing 34 medals—their best since 1984—and sweeping all four hurdle events for the first time[3]. Noah Lyles won his first Olympic gold in the men's 100m with a dramatic, lifetime-best 9.784 seconds[3][4]. Sydney McLaughlin-Levrone broke her own women's 400m hurdles world record yet again[3].\n\n- **Gymnastics Spectacle:** The games featured high drama and new records in **artistic gymnastics**, with full event replays and standout moments available for fans[5].\n\n- **Historic Firsts:** Several nations, including **Dominica, Saint Lucia, Cape Verde, and Albania**, celebrated their first-ever Olympic medals—some of them gold[1]. The **Refugee Olympic Team** won its first medal, a bronze in boxing by Cindy Ngamba[1].\n\n- **Iconic Performances:** Scottie Scheffler secured his first Olympic golf gold for Team USA; Victor Montalvo earned bronze in breaking; and Brooke Raboutou delivered in sport climbing[2].\n\n- **Intensity and Sportsmanship:** Multiple events featured finishes decided by milliseconds and millimeters, capturing the Olympic spirit, as showcased in event highlight reels and replays[4][6].\n\n- **Record-Breaking Tickets:** Paris 2024 broke Olympic records with over 9.5 million tickets sold (12.1 million including Paralympics), becoming a celebrated success despite some controversies around politics and logistics[1].\n\n**Notable Podium Sweep:** France swept all three medals in the men's BMX race, a moment of national pride[1].\n\nThe Paris Olympics were hailed as both a sporting and organizational triumph, celebrated by both locals and worldwide observers[1]."
          },
          "delta": {
            "role": "assistant",
            "content": ""
          }
        }
      ]
    }
    ```
  </Accordion>
</AccordionGroup>

## Use Case Examples

### Sports and Events

Request videos for major sporting events or news:

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "media_response": {
        "overrides": {
          "return_videos": true
        }
      },
      "messages": [
        {
          "role": "user",
          "content": "World Cup 2024 final match highlights"
        }
      ]
    }' | jq
  ```

  ```python Python theme={null}
  import requests
  import json
  import os

  response = requests.post(
      "https://api.perplexity.ai/chat/completions",
      headers={
          "Authorization": f"Bearer {os.environ['PERPLEXITY_API_KEY']}",
          "Content-Type": "application/json"
      },
      json={
          "model": "sonar-pro",
          "media_response": {
              "overrides": {
                  "return_videos": True
              }
          },
          "messages": [
              {
                  "role": "user",
                  "content": "World Cup 2024 final match highlights"
              }
          ]
      }
  )
  print(json.dumps(response.json(), indent=2))
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.perplexity.ai/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.PERPLEXITY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'sonar-pro',
      media_response: {
        overrides: {
          return_videos: true
        }
      },
      messages: [
        {
          role: 'user',
          content: 'World Cup 2024 final match highlights'
        }
      ]
    })
  });

  const result = await response.json();
  console.log(JSON.stringify(result, null, 2));
  ```
</CodeGroup>

### Educational Content

Get instructional videos for learning topics:

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "media_response": {
        "overrides": {
          "return_videos": true
        }
      },
      "messages": [
        {
          "role": "user",
          "content": "How to perform CPR tutorial videos"
        }
      ]
    }' | jq
  ```

  ```python Python theme={null}
  import requests
  import os

  response = requests.post(
      "https://api.perplexity.ai/chat/completions",
      headers={
          "Authorization": f"Bearer {os.environ['PERPLEXITY_API_KEY']}",
          "Content-Type": "application/json"
      },
      json={
          "model": "sonar-pro",
          "media_response": {
              "overrides": {
                  "return_videos": True
              }
          },
          "messages": [
              {
                  "role": "user",
                  "content": "How to perform CPR tutorial videos"
              }
          ]
      }
  )
  print(response.json())
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.perplexity.ai/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.PERPLEXITY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'sonar-pro',
      media_response: {
        overrides: {
          return_videos: true
        }
      },
      messages: [
        {
          role: 'user',
          content: 'How to perform CPR tutorial videos'
        }
      ]
    })
  });

  const result = await response.json();
  console.log(result);
  ```
</CodeGroup>

### Technology Demonstrations

Request videos showing product demos or tutorials:

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "media_response": {
        "overrides": {
          "return_videos": true
        }
      },
      "messages": [
        {
          "role": "user",
          "content": "iPhone 16 pro camera features demonstration"
        }
      ]
    }' | jq
  ```

  ```python Python theme={null}
  import requests
  import os

  response = requests.post(
      "https://api.perplexity.ai/chat/completions",
      headers={
          "Authorization": f"Bearer {os.environ['PERPLEXITY_API_KEY']}",
          "Content-Type": "application/json"
      },
      json={
          "model": "sonar-pro",
          "media_response": {
              "overrides": {
                  "return_videos": True
              }
          },
          "messages": [
              {
                  "role": "user",
                  "content": "iPhone 16 pro camera features demonstration"
              }
          ]
      }
  )
  print(response.json())
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.perplexity.ai/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.PERPLEXITY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'sonar-pro',
      media_response: {
        overrides: {
          return_videos: true
        }
      },
      messages: [
        {
          role: 'user',
          content: 'iPhone 16 pro camera features demonstration'
        }
      ]
    })
  });

  const result = await response.json();
  console.log(result);
  ```
</CodeGroup>

## Combined Media Responses

You can combine video returns with other media response options:

### Videos with Images

```bash theme={null}
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true,
        "return_images": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "Mars rover discoveries 2024"
      }
    ]
  }' | jq
```

### Videos with Search Filters

```bash theme={null}
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "search_recency_filter": "week",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "Latest SpaceX launch footage"
      }
    ]
  }' | jq
```

## Advanced Usage

### Streaming with Videos

Enable streaming responses while including video content:

```bash theme={null}
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "stream": true,
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "Breaking news today with video coverage"
      }
    ]
  }'
```

### Multi-turn Conversation with Videos

Continue a conversation while maintaining video context:

```bash theme={null}
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "Show me cooking videos for pasta recipes"
      },
      {
        "role": "assistant",
        "content": "Here are some great pasta cooking videos..."
      },
      {
        "role": "user",
        "content": "Now show me videos for making homemade sauce"
      }
    ]
  }' | jq
```

## Best Practices

<AccordionGroup>
  <Accordion title="Query Optimization">
    * **Be specific**: Use descriptive queries that clearly indicate when video content would be valuable
    * **Include context**: Mention specific events, products, or topics that commonly have video coverage
    * **Use recency filters**: Combine with search filters to get the most current video content
    * **Consider query intent**: Videos work best for demonstrations, tutorials, events, and visual explanations
  </Accordion>

  <Accordion title="Performance Considerations">
    * **Monitor response times**: Video-enabled requests may take longer to process
    * **Handle larger payloads**: Responses containing videos will be larger than text-only responses
    * **Implement timeouts**: Set appropriate timeout values for video-enabled requests
    * **Cache strategically**: Consider caching video responses for frequently requested content
  </Accordion>

  <Accordion title="Content Quality">
    * **Verify video relevance**: Not all queries will return relevant video content
    * **Handle empty results**: Implement fallback logic when no videos are available
    * **Check video accessibility**: Ensure returned video content is accessible and appropriate
    * **Validate video links**: Test that returned video URLs are functional before displaying
  </Accordion>
</AccordionGroup>

## Response Format

When videos are returned, they appear in the response content along with text. The videos will be included as part of the response structure, with video URLs and metadata available for display or processing.

## Common Use Cases

### News and Current Events

```bash theme={null}
# Get breaking news with video coverage
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "search_recency_filter": "day",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {"role": "user", "content": "Latest political developments today"}
    ]
  }'
```

### Product Reviews and Demonstrations

```bash theme={null}
# Get product demo videos
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {"role": "user", "content": "MacBook Pro M4 unboxing and first impressions"}
    ]
  }'
```

### Educational and How-to Content

```bash theme={null}
# Get tutorial videos
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {"role": "user", "content": "How to change a car tire step by step"}
    ]
  }'
```

## Troubleshooting

<AccordionGroup>
  <Accordion title="No Videos Returned">
    If your request doesn't return videos:

    * Verify the `media_response.overrides.return_videos` parameter is set to `true`
    * Check that your query is likely to have video content available
    * Ensure you're using a model that supports video returns (sonar-pro recommended)
    * Try different query phrasings that explicitly mention video content
  </Accordion>

  <Accordion title="Request Timeouts">
    For timeout issues:

    * Increase your request timeout settings
    * Use streaming responses for better user experience
    * Consider breaking complex queries into smaller parts
    * Implement retry logic for failed requests
  </Accordion>

  <Accordion title="Large Response Handling">
    When dealing with video-heavy responses:

    * Implement proper JSON parsing for large payloads
    * Consider pagination for multiple video results
    * Use appropriate data structures to handle media content
    * Implement progressive loading for video content
  </Accordion>
</AccordionGroup>

## Limitations

<Warning>
  **Current Limitations:**

  * Video returns may not be available for all query types
  * Response times will be longer when videos are included
  * Video content availability depends on external sources
  * Some video content may be region-restricted
  * No direct video format or quality control options currently available
</Warning>

## Environment Variables

For security, use environment variables for your API key:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```bash theme={null}
    set PERPLEXITY_API_KEY=your_api_key_here
    ```
  </Tab>
</Tabs>

Then reference it in your requests:

```bash theme={null}
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "sonar-pro", ...}'
```

<Tip>
  Start with simple queries to test video returns, then gradually build more complex requests as you understand the response patterns and performance characteristics.
</Tip>


# Pro Search Classifier
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/pro-search/classifier

Optimize cost and performance with automatic query classification between Pro Search and Fast Search modes

## Overview

The Pro Search Classifier is an intelligent system that automatically determines whether a query requires the advanced multi-step tool usage of Pro Search or can be effectively answered with standard Fast Search. This optimization helps you balance performance needs with cost efficiency.

<Info>
  Instead of manually choosing between `"pro"` and `"fast"` search types, you can use `"auto"` to let the classifier make the optimal decision for each query.
</Info>

## How It Works

When you set `search_type: "auto"`, the classifier analyzes your query across multiple dimensions:

<Steps>
  <Step title="Query Complexity Analysis">
    The classifier evaluates:

    * Number of sub-questions or aspects
    * Requirement for comparative analysis
    * Need for multi-step reasoning
    * Complexity of information synthesis required

    ```json theme={null}
    {
      "web_search_options": {
        "search_type": "auto"  // Let the classifier decide
      }
    }
    ```
  </Step>

  <Step title="Classification Decision">
    Based on the analysis, the classifier routes the query to either:

    * **Pro Search** for complex, multi-faceted queries requiring multi-step tool usage
    * **Fast Search** for straightforward information retrieval

    The decision is transparent in the response metadata.
  </Step>

  <Step title="Execution">
    The selected search mode processes your query:

    * **Pro Search**: Uses built-in tools (web\_search, fetch\_url\_content) automatically
    * **Fast Search**: Performs optimized single-pass search and synthesis

    You receive the same high-quality response format regardless of which mode is used.
  </Step>
</Steps>

## Classification Patterns

### Queries Classified as Pro Search

Complex queries that benefit from multi-step tool usage are automatically routed to Pro Search:

<AccordionGroup>
  <Accordion title="Multi-Part Questions">
    **Example Query:**
    "What are the differences between React, Vue, and Angular in terms of performance, learning curve, and ecosystem? Which one should I choose for a large enterprise application?"

    **Why Pro Search:**

    * Requires information about three different frameworks
    * Needs comparative analysis across multiple dimensions
    * Involves gathering expert opinions and recommendations
    * Benefits from synthesis of diverse sources

    **Tool Usage:**

    * Multiple web searches for each framework
    * URL fetching for benchmark data and official documentation
  </Accordion>

  <Accordion title="Research Synthesis">
    **Example Query:**
    "Summarize the latest peer-reviewed research on the effectiveness of intermittent fasting for weight loss and metabolic health. Include sample sizes and study limitations."

    **Why Pro Search:**

    * Requires finding multiple research papers
    * Needs access to full paper content, not just abstracts
    * Involves extracting specific data (sample sizes, limitations)
    * Requires synthesis across multiple studies

    **Tool Usage:**

    * Web search for recent peer-reviewed papers
    * `fetch_url_content` to read full papers
    * Information extraction and synthesis
  </Accordion>

  <Accordion title="Time-Sensitive Complex Analysis">
    **Example Query:**
    "Analyze the stock market impact of the Federal Reserve's most recent interest rate decision, including effects on different sectors and expert predictions for the next quarter."

    **Why Pro Search:**

    * Requires very recent information
    * Needs multi-source verification
    * Involves sector-by-sector analysis
    * Benefits from expert opinion gathering

    **Tool Usage:**

    * Multiple targeted web searches
    * URL fetching for financial analysis reports
    * Synthesis of diverse expert opinions
  </Accordion>
</AccordionGroup>

### Queries Classified as Fast Search

Straightforward queries that don't require multi-step reasoning are efficiently handled by Fast Search:

<AccordionGroup>
  <Accordion title="Simple Factual Questions">
    **Example Query:**
    "What is the capital of France?"

    **Why Fast Search:**

    * Single, well-established fact
    * No calculation or analysis needed
    * Information readily available in search snippets

    **Processing:**

    * Single web search
    * Direct answer from search results
    * No need for multi-step reasoning
  </Accordion>

  <Accordion title="Straightforward Information Retrieval">
    **Example Query:**
    "What are the main features of the iPhone 15 Pro?"

    **Why Fast Search:**

    * Single product inquiry
    * Information available in product descriptions
    * No comparative analysis required
    * No calculations needed

    **Processing:**

    * Search for product specifications
    * Extract and list features
    * Synthesize from search results
  </Accordion>

  <Accordion title="Single-Topic Queries">
    **Example Query:**
    "Explain what machine learning is."

    **Why Fast Search:**

    * Single concept definition
    * No multi-part analysis required
    * Standard information readily available

    **Processing:**

    * Search for machine learning explanations
    * Synthesize clear definition
    * Provide context from reliable sources
  </Accordion>

  <Accordion title="Basic Definitional Requests">
    **Example Query:**
    "What does API stand for and what is it used for?"

    **Why Fast Search:**

    * Simple definition request
    * No complex analysis needed
    * Information readily available

    **Processing:**

    * Quick search for API definition
    * Explain acronym and basic usage
    * Provide clear, concise answer
  </Accordion>
</AccordionGroup>

## Cost Implications

Understanding the cost difference helps you optimize your API usage:

<div>
  <div>
    <h4>Classified as Pro Search</h4>

    <ul>
      <li>Complex multi-part questions</li>
      <li>Requests requiring calculation or analysis</li>
      <li>Comparative research across sources</li>
      <li>Time-sensitive information needs</li>
    </ul>

    <div>
      <span>Uses Pro Search billing rates</span>
    </div>
  </div>

  <div>
    <h4>Classified as Fast Search</h4>

    <ul>
      <li>Simple factual questions</li>
      <li>Straightforward information retrieval</li>
      <li>Single-topic queries</li>
      <li>Basic definitional requests</li>
    </ul>

    <div>
      <span>Uses standard Sonar Pro billing rates</span>
    </div>
  </div>
</div>

### Pricing Comparison

**Pro Search Rates:**

* Input: \$3 per 1M tokens
* Output: \$15 per 1M tokens
* Request fees: $14-$22 per 1,000 requests (based on context size)

**Fast Search Rates:**

* Input: \$3 per 1M tokens
* Output: \$15 per 1M tokens
* Request fees: $6-$14 per 1,000 requests (based on context size - same as standard Sonar Pro)

<Tip>
  The automatic classifier helps you save money by using Pro Search only when its advanced capabilities are truly needed, while still ensuring complex queries get full multi-step tool usage.
</Tip>

## Usage Examples

### Using Automatic Classification

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity(api_key="your-api-key")

  # Let the classifier decide
  response = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": "Compare the energy efficiency of Tesla Model 3, Chevrolet Bolt, and Nissan Leaf"
          }
      ],
      stream=True,
      web_search_options={
          "search_type": "auto"  # Automatic classification
      }
  )

  for chunk in response:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript TypeScript SDK theme={null}
  import { Perplexity } from '@perplexity-ai/sdk';

  const client = new Perplexity({
    apiKey: 'your-api-key'
  });

  // Let the classifier decide
  const response = await client.chat.completions.create({
    model: 'sonar-pro',
    messages: [
      {
        role: 'user',
        content: 'Compare the energy efficiency of Tesla Model 3, Chevrolet Bolt, and Nissan Leaf'
      }
    ],
    stream: true,
    web_search_options: {
      search_type: 'auto'  // Automatic classification
    }
  });

  for await (const chunk of response) {
    if (chunk.choices[0]?.delta?.content) {
      process.stdout.write(chunk.choices[0].delta.content);
    }
  }
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer your-api-key" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "Compare the energy efficiency of Tesla Model 3, Chevrolet Bolt, and Nissan Leaf"
        }
      ],
      "stream": true,
      "web_search_options": {
        "search_type": "auto"
      }
    }' --no-buffer
  ```
</CodeGroup>

### Manual Override

You can still manually specify the search type when you know what you need:

<Tabs>
  <Tab title="Force Pro Search">
    Use when you know you need multi-step tool usage:

    ```python theme={null}
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Your complex query"}],
        stream=True,
        web_search_options={
            "search_type": "pro"  # Force Pro Search
        }
    )
    ```

    **Use cases for manual Pro:**

    * You know the query needs multi-step reasoning
    * Previous auto-classification was Fast but you need deeper analysis
    * Critical queries where you want maximum capability
  </Tab>

  <Tab title="Force Fast Search">
    Use when you want to optimize for speed and cost:

    ```python theme={null}
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Your simple query"}],
        stream=True,
        web_search_options={
            "search_type": "fast"  # Force Fast Search (or omit - fast is default)
        }
    )
    ```

    **Use cases for manual Fast:**

    * Simple queries where Pro Search would be overkill
    * Cost-sensitive applications
    * When response speed is critical
  </Tab>
</Tabs>

## Best Practices

<Steps>
  <Step title="Default to automatic classification">
    For most applications, use `search_type: "auto"` and let the classifier optimize:

    ```python theme={null}
    web_search_options={"search_type": "auto"}
    ```

    This ensures the right tool for each query while optimizing costs.
  </Step>

  <Step title="Monitor classification patterns">
    Track which queries get classified as Pro vs Fast to understand your usage patterns:

    * Review queries that consistently use Pro Search
    * Identify opportunities to rephrase queries for Fast Search when appropriate
    * Understand which user questions require advanced capabilities

    This helps optimize your application's query design.
  </Step>

  <Step title="Use manual override strategically">
    Override the classifier only when:

    * You have specific performance requirements
    * Testing and comparing Pro vs Fast results
    * Building features with known complexity levels

    **Example:**

    ```python theme={null}
    # Known complex analysis - force Pro
    if query_requires_calculations(user_query):
        search_type = "pro"
    else:
        search_type = "auto"
    ```
  </Step>

  <Step title="Design queries effectively">
    Structure queries to help the classifier make optimal decisions:

    **Less optimal:**
    "Tell me about electric cars"

    **Better:**
    "What is the average range of electric vehicles?" (Fast Search appropriate)

    **Or:**
    "Compare the total cost of ownership over 5 years for Tesla Model 3, Chevrolet Bolt, and Nissan Leaf, including depreciation, electricity costs, and maintenance" (Pro Search appropriate)

    Clear, specific queries enable better classification.
  </Step>
</Steps>

## Classification Transparency

You can verify the classification decision in the response metadata:

```json theme={null}
{
  "id": "12345",
  "model": "sonar-pro",
  "search_metadata": {
    "search_type_used": "pro",  // or "fast"
    "classification_reason": "Multi-part comparative analysis with calculations"
  },
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 150,
    "total_tokens": 175
  }
}
```

<Info>
  This transparency helps you understand why queries were classified a certain way and optimize future queries.
</Info>

## When to Use Each Mode

<CardGroup>
  <Card title="Auto (Recommended)" icon="wand-magic-sparkles">
    **Best for:** Most applications

    Let the classifier optimize for you. Balances cost and capability automatically based on query complexity.
  </Card>

  <Card title="Manual Pro" icon="brain">
    **Best for:** Known complex tasks

    Use when you're certain multi-step tool usage is needed: calculations, multi-source synthesis, deep analysis.
  </Card>

  <Card title="Manual Fast" icon="bolt">
    **Best for:** Simple retrieval

    Use for straightforward facts, definitions, or when optimizing for speed and cost with simple queries.
  </Card>
</CardGroup>

## Common Questions

<AccordionGroup>
  <Accordion title="How accurate is the classifier?">
    The classifier is highly accurate, trained on thousands of query patterns. It errs on the side of using Pro Search when there's any ambiguity, ensuring you don't lose capability.

    However, if you notice consistent mis-classifications:

    * Rephrase queries to be more specific
    * Use manual override for those query types
    * Consider your use case's specific needs
  </Accordion>

  <Accordion title="Can I see which mode was used?">
    Yes, the response includes metadata showing:

    * Which search type was used
    * Why the classification was made (when using auto)
    * Cost breakdown by search type

    This helps you understand and optimize your usage patterns.
  </Accordion>

  <Accordion title="Does automatic classification add latency?">
    No. Classification happens in milliseconds before query processing begins and does not meaningfully impact response time. The classifier is optimized for real-time decision making.
  </Accordion>

  <Accordion title="What if I disagree with the classification?">
    You can always use manual override:

    ```python theme={null}
    web_search_options={"search_type": "pro"}  # Force your preference
    ```

    If you consistently disagree with classifications, consider:

    * Making queries more specific
    * Using manual override for those query types
    * Reviewing whether your use case needs consistent Pro or Fast mode
  </Accordion>
</AccordionGroup>

## Related Resources

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/grounded-llm/chat-completions/pro-search/quickstart">
    Get started with Pro Search basics
  </Card>

  <Card title="Built-in Tool Capabilities" icon="tools" href="/docs/grounded-llm/chat-completions/pro-search/tools">
    Learn about Pro Search's built-in tools and capabilities
  </Card>

  <Card title="Pricing Guide" icon="dollar-sign" href="/docs/getting-started/pricing">
    Understand pricing for Pro and Fast Search
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/chat-completions-post">
    Complete API documentation
  </Card>
</CardGroup>


# Quickstart
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/pro-search/quickstart

Get started with Pro Search for Sonar Pro - enhanced search with automated tools, multi-step reasoning, and real-time thought streaming

## Overview

Pro Search enhances [Sonar Pro](/docs/getting-started/models/models/sonar-pro) with automated tool usage, enabling multi-step reasoning through intelligent tool orchestration including web search and URL content fetching.

<Warning>
  Pro Search only works when streaming is enabled. Non-streaming requests will fall back to standard Sonar Pro behavior.
</Warning>

<div>
  <div>
    <h3>Standard Sonar Pro</h3>

    <ul>
      <li>Single web search execution</li>
      <li>Fast response synthesis</li>
      <li>Fixed search strategy</li>
      <li>Static result processing</li>
    </ul>
  </div>

  <div>
    <h3>Pro Search for Sonar Pro</h3>

    <ul>
      <li>Multi-step reasoning with automated tools</li>
      <li>Dynamic tool execution</li>
      <li>Real-time thought streaming</li>
      <li>Adaptive research strategies</li>
    </ul>
  </div>
</div>

## Basic Usage

Enabling Pro Search requires setting `stream` to `true` and specifying `"search_type": "pro"` in your API request. The default search type is `"fast"` for regular Sonar Pro.

Here is an example of how to enable Pro Search with streaming:

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity(api_key="YOUR_API_KEY")

  messages = [
      {
          "role": "user", 
          "content": "Analyze the latest developments in quantum computing and their potential impact on cryptography. Include recent research findings and expert opinions."
      }
  ]

  response = client.chat.completions.create(
      model="sonar-pro",
      messages=messages,
      stream=True,
      web_search_options={
          "search_type": "pro"
      }
  )

  for chunk in response:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript TypeScript SDK theme={null}
  import { Perplexity } from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity({
    apiKey: 'YOUR_API_KEY'
  });

  const response = await client.chat.completions.create({
    model: 'sonar-pro',
    messages: [
      {
        role: 'user',
        content: 'Analyze the latest developments in quantum computing and their potential impact on cryptography. Include recent research findings and expert opinions.'
      }
    ],
    stream: true,
    web_search_options: {
      search_type: 'pro'
    }
  });

  for await (const chunk of response) {
    if (chunk.choices[0]?.delta?.content) {
      process.stdout.write(chunk.choices[0].delta.content);
    }
  }
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "Analyze the latest developments in quantum computing and their potential impact on cryptography. Include recent research findings and expert opinions."
        }
      ],
      "stream": true,
      "web_search_options": {
        "search_type": "pro"
      }
    }' --no-buffer
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "2f16f4a0-e1d7-48c7-832f-8757b96ec221",
    "model": "sonar-pro", 
    "created": 1759957470,
    "usage": {
      "prompt_tokens": 15,
      "completion_tokens": 98,
      "total_tokens": 113,
      "search_context_size": "low",
      "cost": {
        "input_tokens_cost": 0.0,
        "output_tokens_cost": 0.001,
        "request_cost": 0.014,
        "total_cost": 0.015
      }
    },
    "search_results": [
      {
        "title": "Quantum Computing Breakthrough 2024",
        "url": "https://example.com/quantum-breakthrough",
        "date": "2024-03-15",
        "snippet": "Researchers at MIT have developed a new quantum error correction method...",
        "source": "web"
      }
    ],
    "reasoning_steps": [
      {
        "thought": "I need to search for recent quantum computing developments first.",
        "type": "web_search",
        "web_search": {
          "search_keywords": [
            "quantum computing developments 2024 cryptography impact",
            "post-quantum cryptography"
          ],
          "search_results": [
            {
              "title": "Quantum Computing Breakthrough 2024",
              "url": "https://example.com/quantum-breakthrough",
              "date": "2024-03-15",
              "last_updated": "2024-03-20",
              "snippet": "Researchers at MIT have developed a new quantum error correction method...",
              "source": "web"
            }
          ]
        }
      },
      {
        "thought": "Let me fetch detailed content from this research paper.",
        "type": "fetch_url_content", 
        "fetch_url_content": {
          "contents": [
            {
              "title": "Quantum Error Correction Paper",
              "url": "https://arxiv.org/abs/2024.quantum",
              "date": null,
              "last_updated": null,
              "snippet": "Abstract: This paper presents a novel approach to quantum error correction...",
              "source": "web"
            }
          ]
        }
      }
    ],
    "object": "chat.completion.chunk",
    "choices": [
      {
        "index": 0,
        "delta": {
          "role": "assistant",
          "content": "## Latest Quantum Computing Developments\n\nBased on my research and analysis..."
        }
      }
    ]
  }
  ```
</Accordion>

## Enabling Automatic Classification

Sonar Pro can be configured to automatically classify queries into Pro Search or Fast Search based on complexity. This is the recommended approach for most applications.

Set `search_type: "auto"` to let the system intelligently route queries based on complexity.

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity(api_key="YOUR_API_KEY")

  response = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": "Compare the energy efficiency of Tesla Model 3, Chevrolet Bolt, and Nissan Leaf"
          }
      ],
      stream=True,
      web_search_options={
          "search_type": "auto"  # Automatic classification
      }
  )

  for chunk in response:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript TypeScript SDK theme={null}
  import { Perplexity } from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity({
    apiKey: 'YOUR_API_KEY'
  });

  const response = await client.chat.completions.create({
    model: 'sonar-pro',
    messages: [
      {
        role: 'user',
        content: 'Compare the energy efficiency of Tesla Model 3, Chevrolet Bolt, and Nissan Leaf'
      }
    ],
    stream: true,
    web_search_options: {
      search_type: 'auto'  // Automatic classification
    }
  });

  for await (const chunk of response) {
    if (chunk.choices[0]?.delta?.content) {
      process.stdout.write(chunk.choices[0].delta.content);
    }
  }
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "Compare the energy efficiency of Tesla Model 3, Chevrolet Bolt, and Nissan Leaf"
        }
      ],
      "stream": true,
      "web_search_options": {
        "search_type": "auto"
      }
    }' --no-buffer
  ```
</CodeGroup>

#### How Classification Works

The classifier analyzes your query and automatically routes it to:

* **Pro Search** for complex queries requiring:
  * Multi-step reasoning or analysis
  * Comparative analysis across multiple sources
  * Deep research workflows

* **Fast Search** for straightforward queries like:
  * Simple fact lookups
  * Direct information retrieval
  * Basic question answering

#### Billing with Auto Classification

**You are billed based on which search type your query triggers:**

* If classified as **Pro Search**: \$14–\$22 per 1,000 requests (based on context size)
* If classified as **Fast Search**: \$6–\$14 per 1,000 requests (based on context size - same as standard Sonar Pro)

To see the full pricing details, see the <a href="/docs/grounded-llm/chat-completions/pro-search/quickstart#pricing">Pricing</a> section.

<Tip>
  Automatic classification is recommended for most applications as it balances cost optimization with query performance. You get Pro Search capabilities when needed without overpaying for simple queries.
</Tip>

### Manually Specifying the Search Type

If needed, you can manually specify the search type. This is useful for specific use cases where you know the query requires Pro Search capabilities.

* **`"search_type": "pro"`** — Manually specify Pro Search for complex queries when you know multi-step tool usage is needed
* **`"search_type": "fast"`** — Manually specify Fast Search for simple queries to optimize speed and cost (this is also the default when `search_type` is omitted)

## Built-in Tool Capabilities

Pro Search provides access to two powerful built-in tools that the model can use automatically:

<CardGroup>
  <Card title="web_search" icon="magnifying-glass" href="/docs/grounded-llm/chat-completions/pro-search/tools#web-search">
    Conduct targeted web searches with custom queries, filters, and search strategies based on the evolving research context.
  </Card>

  <Card title="fetch_url_content" icon="globe" href="/docs/grounded-llm/chat-completions/pro-search/tools#fetch-url-content">
    Retrieve and analyze content from specific URLs to gather detailed information beyond search result snippets.
  </Card>
</CardGroup>

<Info>
  The model automatically decides which tools to use and when, creating dynamic research workflows tailored to each specific query. These are built-in tools that the system calls for you—you cannot register custom tools. Learn more in the [Built-in Tool Capabilities](/docs/grounded-llm/chat-completions/pro-search/tools) guide.
</Info>

## Additional Capabilities

Pro Search also provides access to advanced Sonar Pro features that enhance your development experience:

* **[Stream Mode Guide](/docs/grounded-llm/chat-completions/pro-search/stream-mode)**: Control streaming response formats with concise or full mode for optimized bandwidth usage and enhanced reasoning visibility.

## Pricing

Pro Search pricing consists of token usage plus request fees that vary by search type and context size.

<div>
  <div>
    <h3>Token Usage (Same for All Search Types)</h3>

    <div>
      <div>
        <span>Input Tokens</span>
        <span>\$3 per 1M</span>
      </div>

      <div>
        <span>Output Tokens</span>
        <span>\$15 per 1M</span>
      </div>
    </div>
  </div>

  <div>
    <h3>Request Fees (per 1,000 requests)</h3>

    <div>
      <h4>Pro Search (Complex Queries)</h4>

      <div>
        <div>
          <span>High Context</span>
          <span>\$22</span>
        </div>

        <div>
          <span>Medium Context</span>
          <span>\$18</span>
        </div>

        <div>
          <span>Low Context</span>
          <span>\$14</span>
        </div>
      </div>
    </div>

    <div>
      <h4>Fast Search (Simple Queries)</h4>

      <div>
        <div>
          <span>High Context</span>
          <span>\$14</span>
        </div>

        <div>
          <span>Medium Context</span>
          <span>\$10</span>
        </div>

        <div>
          <span>Low Context</span>
          <span>\$6</span>
        </div>
      </div>
    </div>
  </div>
</div>

<Info>
  When using `search_type: "auto"`, you're billed at the Pro Search rate if your query is classified as complex, or the Fast Search rate if classified as simple. See the full pricing details <a href="/docs/getting-started/pricing">here</a>.
</Info>

## Next Steps

<CardGroup>
  <Card title="Chat Completions Guide" icon="comments" href="/docs/grounded-llm/openai-compatibility">
    Comprehensive guide to the chat completions API
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/chat-completions-post">
    Complete API documentation and parameter reference
  </Card>
</CardGroup>


# Stream Mode: Concise vs Full
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/pro-search/stream-mode

Learn how to use stream_mode to control streaming response formats and optimize your integration

## Overview

The `stream_mode` parameter gives you control over how streaming responses are formatted. Choose between two modes:

* **`full`** (default) - Traditional streaming format with complete message objects in each chunk
* **`concise`** - Optimized streaming format with reduced redundancy and enhanced reasoning visibility

<Info>
  The `concise` mode is designed to minimize bandwidth usage and provide better visibility into the model's reasoning process.
</Info>

## Quick Comparison

| Feature                 | Full Mode                                | Concise Mode                        |
| ----------------------- | ---------------------------------------- | ----------------------------------- |
| **Message aggregation** | Server-side (includes `choices.message`) | Client-side (delta only)            |
| **Chunk types**         | Single type (`chat.completion.chunk`)    | Multiple types for different stages |
| **Search results**      | Multiple times during stream             | Only in `done` chunks               |
| **Bandwidth**           | Higher (includes redundant data)         | Lower (optimized for efficiency)    |

## Using Concise Mode

Set `stream_mode: "concise"` when creating streaming completions:

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "What's the weather in Seattle?"}],
        stream=True,
        stream_mode="concise"
    )

    for chunk in stream:
        print(f"Chunk type: {chunk.object}")
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript theme={null}
    import Perplexity from '@perplexity-ai/perplexity_ai';

    const client = new Perplexity();

    const stream = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [{ role: "user", content: "What's the weather in Seattle?" }],
      stream: true,
      stream_mode: "concise"
    });

    for await (const chunk of stream) {
      console.log(`Chunk type: ${chunk.object}`);
      if (chunk.choices[0]?.delta?.content) {
        process.stdout.write(chunk.choices[0].delta.content);
      }
    }
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -X POST "https://api.perplexity.ai/chat/completions" \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": "What is the weather in Seattle?"}],
        "stream": true,
        "stream_mode": "concise"
      }'
    ```
  </Tab>
</Tabs>

## Understanding Chunk Types

In concise mode, you'll receive four different types of chunks during the stream:

### 1. `chat.reasoning`

Streamed during the reasoning stage, containing real-time reasoning steps and search operations.

<Tabs>
  <Tab title="Structure">
    ```json theme={null}
    {
      "id": "cfa38f9d-fdbc-4ac6-a5d2-a3010b6a33a6",
      "model": "sonar-pro",
      "created": 1759441590,
      "object": "chat.reasoning",
      "choices": [{
        "index": 0,
        "finish_reason": null,
        "message": {
          "role": "assistant",
          "content": ""
        },
        "delta": {
          "role": "assistant",
          "content": "",
          "reasoning_steps": [{
            "thought": "Searching the web for Seattle's current weather...",
            "type": "web_search",
            "web_search": {
              "search_results": [...],
              "search_keywords": ["Seattle current weather"]
            }
          }]
        }
      }],
      "type": "message"
    }
    ```
  </Tab>

  <Tab title="Python Handler">
    ```python theme={null}
    def handle_reasoning_chunk(chunk):
        """Process reasoning stage updates"""
        if chunk.object == "chat.reasoning":
            delta = chunk.choices[0].delta

            if hasattr(delta, 'reasoning_steps'):
                for step in delta.reasoning_steps:
                    print(f"\n[Reasoning] {step.thought}")

                    if step.type == "web_search":
                        keywords = step.web_search.search_keywords
                        print(f"[Search] Keywords: {', '.join(keywords)}")
    ```
  </Tab>

  <Tab title="TypeScript Handler">
    ```typescript theme={null}
    function handleReasoningChunk(chunk: any) {
      if (chunk.object === "chat.reasoning") {
        const delta = chunk.choices[0].delta;

        if (delta.reasoning_steps) {
          for (const step of delta.reasoning_steps) {
            console.log(`\n[Reasoning] ${step.thought}`);

            if (step.type === "web_search") {
              const keywords = step.web_search.search_keywords;
              console.log(`[Search] Keywords: ${keywords.join(', ')}`);
            }
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

### 2. `chat.reasoning.done`

Marks the end of the reasoning stage and includes all search results (web, images, videos) and reasoning steps.

<Tabs>
  <Tab title="Structure">
    ```json theme={null}
    {
      "id": "3dd9d463-0fef-47e3-af70-92f9fcc4db1f",
      "model": "sonar-pro",
      "created": 1759459505,
      "object": "chat.reasoning.done",
      "usage": {
        "prompt_tokens": 6,
        "completion_tokens": 0,
        "total_tokens": 6,
        "search_context_size": "low"
      },
      "search_results": [...],
      "images": [...],
      "choices": [{
        "index": 0,
        "finish_reason": null,
        "message": {
          "role": "assistant",
          "content": "",
          "reasoning_steps": [...]
        },
        "delta": {
          "role": "assistant",
          "content": ""
        }
      }]
    }
    ```
  </Tab>

  <Tab title="Python Handler">
    ```python theme={null}
    def handle_reasoning_done(chunk):
        """Process end of reasoning stage"""
        if chunk.object == "chat.reasoning.done":
            print("\n[Reasoning Complete]")

            # Access all search results
            if hasattr(chunk, 'search_results'):
                print(f"Found {len(chunk.search_results)} sources")
                for result in chunk.search_results[:3]:
                    print(f"  • {result['title']}")

            # Access image results
            if hasattr(chunk, 'images'):
                print(f"Found {len(chunk.images)} images")

            # Partial usage stats available
            if hasattr(chunk, 'usage'):
                print(f"Tokens used so far: {chunk.usage.total_tokens}")
    ```
  </Tab>

  <Tab title="TypeScript Handler">
    ```typescript theme={null}
    function handleReasoningDone(chunk: any) {
      if (chunk.object === "chat.reasoning.done") {
        console.log("\n[Reasoning Complete]");

        // Access all search results
        if (chunk.search_results) {
          console.log(`Found ${chunk.search_results.length} sources`);
          chunk.search_results.slice(0, 3).forEach((result: any) => {
            console.log(`  • ${result.title}`);
          });
        }

        // Access image results
        if (chunk.images) {
          console.log(`Found ${chunk.images.length} images`);
        }

        // Partial usage stats available
        if (chunk.usage) {
          console.log(`Tokens used so far: ${chunk.usage.total_tokens}`);
        }
      }
    }
    ```
  </Tab>
</Tabs>

### 3. `chat.completion.chunk`

Streamed during the response generation stage, containing the actual content being generated.

<Tabs>
  <Tab title="Structure">
    ```json theme={null}
    {
      "id": "cfa38f9d-fdbc-4ac6-a5d2-a3010b6a33a6",
      "model": "sonar-pro",
      "created": 1759441592,
      "object": "chat.completion.chunk",
      "choices": [{
        "index": 0,
        "finish_reason": null,
        "message": {
          "role": "assistant",
          "content": ""
        },
        "delta": {
          "role": "assistant",
          "content": " tonight"
        }
      }]
    }
    ```
  </Tab>

  <Tab title="Python Handler">
    ```python theme={null}
    def handle_completion_chunk(chunk):
        """Process content generation updates"""
        if chunk.object == "chat.completion.chunk":
            delta = chunk.choices[0].delta

            if hasattr(delta, 'content') and delta.content:
                # Stream content to user
                print(delta.content, end='', flush=True)
                return delta.content

        return ""
    ```
  </Tab>

  <Tab title="TypeScript Handler">
    ```typescript theme={null}
    function handleCompletionChunk(chunk: any): string {
      if (chunk.object === "chat.completion.chunk") {
        const delta = chunk.choices[0]?.delta;

        if (delta?.content) {
          // Stream content to user
          process.stdout.write(delta.content);
          return delta.content;
        }
      }

      return "";
    }
    ```
  </Tab>
</Tabs>

### 4. `chat.completion.done`

Final chunk indicating the stream is complete, including final search results, usage statistics, and cost information.

<Tabs>
  <Tab title="Structure">
    ```json theme={null}
    {
      "id": "cfa38f9d-fdbc-4ac6-a5d2-a3010b6a33a6",
      "model": "sonar-pro",
      "created": 1759441595,
      "object": "chat.completion.done",
      "usage": {
        "prompt_tokens": 6,
        "completion_tokens": 238,
        "total_tokens": 244,
        "search_context_size": "low",
        "cost": {
          "input_tokens_cost": 0.0,
          "output_tokens_cost": 0.004,
          "request_cost": 0.006,
          "total_cost": 0.01
        }
      },
      "search_results": [...],
      "images": [...],
      "choices": [{
        "index": 0,
        "finish_reason": "stop",
        "message": {
          "role": "assistant",
          "content": "## Seattle Weather Forecast\n\nSeattle is experiencing...",
          "reasoning_steps": [...]
        },
        "delta": {
          "role": "assistant",
          "content": ""
        }
      }]
    }
    ```
  </Tab>

  <Tab title="Python Handler">
    ```python theme={null}
    def handle_completion_done(chunk):
        """Process stream completion"""
        if chunk.object == "chat.completion.done":
            print("\n\n[Stream Complete]")

            # Final aggregated message
            full_message = chunk.choices[0].message.content

            # Final search results
            if hasattr(chunk, 'search_results'):
                print(f"\nFinal sources: {len(chunk.search_results)}")

            # Complete usage and cost information
            if hasattr(chunk, 'usage'):
                usage = chunk.usage
                print(f"\nTokens: {usage.total_tokens}")

                if hasattr(usage, 'cost'):
                    print(f"Cost: ${usage.cost.total_cost:.4f}")

            return {
                'content': full_message,
                'search_results': getattr(chunk, 'search_results', []),
                'images': getattr(chunk, 'images', []),
                'usage': getattr(chunk, 'usage', None)
            }
    ```
  </Tab>

  <Tab title="TypeScript Handler">
    ```typescript theme={null}
    function handleCompletionDone(chunk: any) {
      if (chunk.object === "chat.completion.done") {
        console.log("\n\n[Stream Complete]");

        // Final aggregated message
        const fullMessage = chunk.choices[0].message.content;

        // Final search results
        if (chunk.search_results) {
          console.log(`\nFinal sources: ${chunk.search_results.length}`);
        }

        // Complete usage and cost information
        if (chunk.usage) {
          console.log(`\nTokens: ${chunk.usage.total_tokens}`);

          if (chunk.usage.cost) {
            console.log(`Cost: $${chunk.usage.cost.total_cost.toFixed(4)}`);
          }
        }

        return {
          content: fullMessage,
          search_results: chunk.search_results || [],
          images: chunk.images || [],
          usage: chunk.usage || null
        };
      }
    }
    ```
  </Tab>
</Tabs>

## Complete Implementation Examples

### Full Concise Mode Handler

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    from perplexity import Perplexity

    class ConciseStreamHandler:
        def __init__(self):
            self.content = ""
            self.reasoning_steps = []
            self.search_results = []
            self.images = []
            self.usage = None

        def stream_query(self, query: str, model: str = "sonar-pro"):
            """Handle a complete concise streaming request"""
            client = Perplexity()

            stream = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": query}],
                stream=True,
                stream_mode="concise"
            )

            for chunk in stream:
                self.process_chunk(chunk)

            return self.get_result()

        def process_chunk(self, chunk):
            """Route chunk to appropriate handler"""
            chunk_type = chunk.object

            if chunk_type == "chat.reasoning":
                self.handle_reasoning(chunk)
            elif chunk_type == "chat.reasoning.done":
                self.handle_reasoning_done(chunk)
            elif chunk_type == "chat.completion.chunk":
                self.handle_content(chunk)
            elif chunk_type == "chat.completion.done":
                self.handle_done(chunk)

        def handle_reasoning(self, chunk):
            """Process reasoning updates"""
            delta = chunk.choices[0].delta

            if hasattr(delta, 'reasoning_steps'):
                for step in delta.reasoning_steps:
                    self.reasoning_steps.append(step)
                    print(f"💭 {step.thought}")

        def handle_reasoning_done(self, chunk):
            """Process end of reasoning"""
            if hasattr(chunk, 'search_results'):
                self.search_results = chunk.search_results
                print(f"\n🔍 Found {len(self.search_results)} sources")

            if hasattr(chunk, 'images'):
                self.images = chunk.images
                print(f"🖼️  Found {len(self.images)} images")

            print("\n📝 Generating response...\n")

        def handle_content(self, chunk):
            """Process content chunks"""
            delta = chunk.choices[0].delta

            if hasattr(delta, 'content') and delta.content:
                self.content += delta.content
                print(delta.content, end='', flush=True)

        def handle_done(self, chunk):
            """Process completion"""
            if hasattr(chunk, 'usage'):
                self.usage = chunk.usage
                print(f"\n\n✅ Complete | Tokens: {self.usage.total_tokens}")

                if hasattr(self.usage, 'cost'):
                    print(f"💰 Cost: ${self.usage.cost.total_cost:.4f}")

        def get_result(self):
            """Return complete result"""
            return {
                'content': self.content,
                'reasoning_steps': self.reasoning_steps,
                'search_results': self.search_results,
                'images': self.images,
                'usage': self.usage
            }

    # Usage
    handler = ConciseStreamHandler()
    result = handler.stream_query("What's the latest news in AI?")

    print(f"\n\nFinal content length: {len(result['content'])} characters")
    print(f"Sources used: {len(result['search_results'])}")
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript theme={null}
    import Perplexity from '@perplexity-ai/perplexity_ai';

    interface StreamResult {
      content: string;
      reasoning_steps: any[];
      search_results: any[];
      images: any[];
      usage: any;
    }

    class ConciseStreamHandler {
      private content: string = "";
      private reasoning_steps: any[] = [];
      private search_results: any[] = [];
      private images: any[] = [];
      private usage: any = null;

      async streamQuery(query: string, model: string = "sonar-pro"): Promise<StreamResult> {
        const client = new Perplexity();

        const stream = await client.chat.completions.create({
          model,
          messages: [{ role: "user", content: query }],
          stream: true,
          stream_mode: "concise"
        });

        for await (const chunk of stream) {
          this.processChunk(chunk);
        }

        return this.getResult();
      }

      private processChunk(chunk: any) {
        const chunkType = chunk.object;

        switch (chunkType) {
          case "chat.reasoning":
            this.handleReasoning(chunk);
            break;
          case "chat.reasoning.done":
            this.handleReasoningDone(chunk);
            break;
          case "chat.completion.chunk":
            this.handleContent(chunk);
            break;
          case "chat.completion.done":
            this.handleDone(chunk);
            break;
        }
      }

      private handleReasoning(chunk: any) {
        const delta = chunk.choices[0].delta;

        if (delta.reasoning_steps) {
          for (const step of delta.reasoning_steps) {
            this.reasoning_steps.push(step);
            console.log(`💭 ${step.thought}`);
          }
        }
      }

      private handleReasoningDone(chunk: any) {
        if (chunk.search_results) {
          this.search_results = chunk.search_results;
          console.log(`\n🔍 Found ${this.search_results.length} sources`);
        }

        if (chunk.images) {
          this.images = chunk.images;
          console.log(`🖼️  Found ${this.images.length} images`);
        }

        console.log("\n📝 Generating response...\n");
      }

      private handleContent(chunk: any) {
        const delta = chunk.choices[0]?.delta;

        if (delta?.content) {
          this.content += delta.content;
          process.stdout.write(delta.content);
        }
      }

      private handleDone(chunk: any) {
        if (chunk.usage) {
          this.usage = chunk.usage;
          console.log(`\n\n✅ Complete | Tokens: ${this.usage.total_tokens}`);

          if (this.usage.cost) {
            console.log(`💰 Cost: $${this.usage.cost.total_cost.toFixed(4)}`);
          }
        }
      }

      private getResult(): StreamResult {
        return {
          content: this.content,
          reasoning_steps: this.reasoning_steps,
          search_results: this.search_results,
          images: this.images,
          usage: this.usage
        };
      }
    }

    // Usage
    const handler = new ConciseStreamHandler();
    const result = await handler.streamQuery("What's the latest news in AI?");

    console.log(`\n\nFinal content length: ${result.content.length} characters`);
    console.log(`Sources used: ${result.search_results.length}`);
    ```
  </Tab>

  <Tab title="Raw HTTP">
    ```python theme={null}
    import requests
    import json

    def stream_concise_mode(query: str):
        """Handle concise streaming with raw HTTP"""
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar-pro",
            "messages": [{"role": "user", "content": query}],
            "stream": True,
            "stream_mode": "concise"
        }

        response = requests.post(url, headers=headers, json=payload, stream=True)

        content = ""
        search_results = []
        usage = None

        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    data_str = line[6:]
                    if data_str == '[DONE]':
                        break

                    try:
                        chunk = json.loads(data_str)
                        chunk_type = chunk.get('object')

                        if chunk_type == 'chat.reasoning':
                            # Handle reasoning
                            delta = chunk['choices'][0]['delta']
                            if 'reasoning_steps' in delta:
                                for step in delta['reasoning_steps']:
                                    print(f"💭 {step['thought']}")

                        elif chunk_type == 'chat.reasoning.done':
                            # Handle reasoning completion
                            if 'search_results' in chunk:
                                search_results = chunk['search_results']
                                print(f"\n🔍 Found {len(search_results)} sources\n")

                        elif chunk_type == 'chat.completion.chunk':
                            # Handle content
                            delta = chunk['choices'][0]['delta']
                            if 'content' in delta and delta['content']:
                                content += delta['content']
                                print(delta['content'], end='', flush=True)

                        elif chunk_type == 'chat.completion.done':
                            # Handle completion
                            if 'usage' in chunk:
                                usage = chunk['usage']
                                print(f"\n\n✅ Tokens: {usage['total_tokens']}")

                    except json.JSONDecodeError:
                        continue

        return {
            'content': content,
            'search_results': search_results,
            'usage': usage
        }

    # Usage
    result = stream_concise_mode("What's the latest news in AI?")
    ```
  </Tab>
</Tabs>

## Best Practices

<Steps>
  <Step title="Aggregate content on the client side">
    In concise mode, `choices.message` is not incrementally updated. You must aggregate chunks yourself.

    ```python theme={null}
    # Track content yourself
    content = ""
    for chunk in stream:
        if chunk.object == "chat.completion.chunk":
            if chunk.choices[0].delta.content:
                content += chunk.choices[0].delta.content
    ```
  </Step>

  <Step title="Use reasoning steps for transparency">
    Display reasoning steps to users for better transparency and trust.

    ```python theme={null}
    def display_reasoning(step):
        """Show reasoning to users"""
        print(f"🔍 Searching for: {step.web_search.search_keywords}")
        print(f"💭 {step.thought}")
    ```
  </Step>

  <Step title="Handle search results from done chunks only">
    Search results and usage information only appear in `chat.reasoning.done` and `chat.completion.done` chunks.

    ```python theme={null}
    # Don't check for search_results in other chunk types
    if chunk.object in ["chat.reasoning.done", "chat.completion.done"]:
        if hasattr(chunk, 'search_results'):
            process_search_results(chunk.search_results)
    ```
  </Step>

  <Step title="Implement proper type checking">
    Use the `object` field to route chunks to appropriate handlers.

    ```python theme={null}
    chunk_handlers = {
        "chat.reasoning": handle_reasoning,
        "chat.reasoning.done": handle_reasoning_done,
        "chat.completion.chunk": handle_content,
        "chat.completion.done": handle_done
    }

    handler = chunk_handlers.get(chunk.object)
    if handler:
        handler(chunk)
    ```
  </Step>

  <Step title="Track cost from the final chunk">
    Cost information is only available in the `chat.completion.done` chunk.

    ```python theme={null}
    if chunk.object == "chat.completion.done":
        if hasattr(chunk.usage, 'cost'):
            total_cost = chunk.usage.cost.total_cost
            print(f"Request cost: ${total_cost:.4f}")
    ```
  </Step>
</Steps>

## Migration from Full Mode

If you're migrating from full mode to concise mode, here are the key changes:

<Tabs>
  <Tab title="Before (Full Mode)">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "What's the weather?"}],
        stream=True
        # stream_mode defaults to "full"
    )

    for chunk in stream:
        # All chunks are chat.completion.chunk
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")

        # Search results may appear in multiple chunks
        if hasattr(chunk, 'search_results'):
            print(f"Sources: {len(chunk.search_results)}")
    ```
  </Tab>

  <Tab title="After (Concise Mode)">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "What's the weather?"}],
        stream=True,
        stream_mode="concise"  # Enable concise mode
    )

    for chunk in stream:
        # Multiple chunk types - route appropriately
        if chunk.object == "chat.reasoning":
            # New: Handle reasoning steps
            if chunk.choices[0].delta.reasoning_steps:
                print("Reasoning in progress...")

        elif chunk.object == "chat.reasoning.done":
            # New: Reasoning complete, search results available
            if hasattr(chunk, 'search_results'):
                print(f"Sources: {len(chunk.search_results)}")

        elif chunk.object == "chat.completion.chunk":
            # Content chunks (similar to full mode)
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="")

        elif chunk.object == "chat.completion.done":
            # Final chunk with complete metadata
            print(f"\nTotal tokens: {chunk.usage.total_tokens}")
    ```
  </Tab>
</Tabs>

## When to Use Each Mode

<CardGroup>
  <Card title="Use Full Mode" icon="list">
    * Simple integrations where you want the SDK to handle aggregation
    * Backward compatibility with existing implementations
    * When you don't need reasoning visibility
  </Card>

  <Card title="Use Concise Mode" icon="bolt">
    * Production applications optimizing for bandwidth
    * Applications that need reasoning transparency
    * Real-time chat interfaces with reasoning display
    * Cost-sensitive applications
  </Card>
</CardGroup>

## Resources

* [Streaming Responses Guide](/docs/grounded-llm/output-control/streaming-responses) - General streaming documentation
* [Chat Completions Guide](/docs/grounded-llm/chat-completions/quickstart) - Complete chat completions guide
* [API Reference - Chat Completions](/api-reference/chat-completions-post) - API documentation


# Built-in Tool Capabilities
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/pro-search/tools

Learn about Pro Search's built-in tools: web search and URL content fetching

## Overview

Pro Search provides two built-in tools that the model uses automatically to answer your queries. The model decides which tools to use and when—you don't need to configure anything. These tools are called automatically by the system; you cannot register custom tools.

<Info>
  All tool executions appear in the `reasoning_steps` array of streaming responses, giving you visibility into how the model researched your query.
</Info>

## web\_search

Conducts web searches to find current information, statistics, and expert opinions.

**Example in action:**

```json theme={null}
{
  "thought": "I need current data on EV market trends",
  "type": "web_search",
  "web_search": {
    "search_keywords": [
      "EV Statistics 2023-2024",
      "electric vehicle sales data",
      "global EV market trends"
    ],
    "search_results": [
      {
        "title": "Trends in electric cars",
        "url": "https://www.iea.org/reports/global-ev-outlook-2024/trends-in-electric-cars",
        "date": "2024-03-15",
        "last_updated": null,
        "snippet": "Electric car sales neared 14 million in 2023, 95% of which were in China, Europe and the United States...",
        "source": "web"
      }
    ]
  }
}
```

## fetch\_url\_content

Retrieves full content from specific URLs to access detailed information beyond search result snippets.

**Example in action:**

```json theme={null}
{
  "thought": "This research paper contains detailed methodology I need to review",
  "type": "fetch_url_content",
  "fetch_url_content": {
    "contents": [
      {
        "title": "Attention Is All You Need",
        "url": "https://arxiv.org/pdf/1706.03762",
        "date": null,
        "last_updated": null,
        "snippet": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder...",
        "source": "web"
      }
    ]
  }
}
```

## Multi-Tool Workflows

The model automatically combines multiple tools when needed. For example, when asked to research solar panel options, it might:

1. Use `web_search` to find current incentives and costs
2. Use `fetch_url_content` to read detailed policy documents
3. Use `web_search` again to verify electricity rates and compare providers

## Related Resources

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/grounded-llm/chat-completions/pro-search/quickstart">
    Get started with Pro Search basics
  </Card>

  <Card title="Stream Mode Guide" icon="bolt" href="/docs/guides/stream-mode-guide">
    Learn about streaming and real-time reasoning visibility
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/chat-completions-post">
    Complete API documentation
  </Card>
</CardGroup>


# Chat Completions API
Source: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/quickstart

Get started with Perplexity's Chat Completions API for web-grounded AI responses. Make your first API call in minutes.

## Overview

Perplexity's Chat Completions API provides web-grounded AI responses with support for streaming, tools, search options, and more. You can use it with OpenAI-compatible client libraries or our native SDKs for type safety and enhanced features.

Use the Chat Completions API when you need web search capabilities built-in, streaming responses, or Perplexity's Sonar models. For structured outputs and third-party models, use our [Agentic Research API](/docs/grounded-llm/responses/quickstart).

<Tip>
  Keep using your existing OpenAI SDKs to get started fast; switch to our [native SDKs](/docs/sdk/overview) later as needed.
</Tip>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript/JavaScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```

  ```bash OpenAI Python (Compatible) theme={null}
  pip install openai
  ```

  ```bash OpenAI TypeScript (Compatible) theme={null}
  npm install openai
  ```
</CodeGroup>

## Authentication

Set your API key as an environment variable. The SDK will automatically read it:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

Or use a `.env` file in your project:

```bash .env theme={null}
PERPLEXITY_API_KEY=your_api_key_here
```

<Info>
  All SDK examples below automatically use the `PERPLEXITY_API_KEY` environment variable. You can also pass the key explicitly if needed.
</Info>

## Generating an API Key

<Card title="Get your Perplexity API Key" icon="key" href="https://perplexity.ai/account/api">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

<Note>
  **OpenAI SDK Compatible:** Perplexity's API supports the OpenAI Chat Completions format. You can use OpenAI client libraries by pointing to our endpoint.
</Note>

## Basic Usage

### Non-Streaming Request

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "user", "content": "What were the results of the 2025 French Open Finals?"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript SDK theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
          { role: "user", content: "What were the results of the 2025 French Open Finals?" }
      ],
  });

  console.log(completion.choices[0].message.content);
  ```

  ```python OpenAI Python SDK theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_API_KEY",
      base_url="https://api.perplexity.ai"
  )

  resp = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "user", "content": "What were the results of the 2025 French Open Finals?"}
      ]
  )
  print(resp.choices[0].message.content)
  ```

  ```typescript OpenAI TypeScript SDK theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai"
  });

  const resp = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
          { role: "user", content: "What were the results of the 2025 French Open Finals?" }
      ],
  });
  console.log(resp.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "What were the results of the 2025 French Open Finals?"
        }
      ]
    }' | jq
  ```
</CodeGroup>

### Streaming Response

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  stream = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "user", "content": "What are the most popular open-source alternatives to OpenAI's GPT models?"}
      ],
      stream=True
  )

  for chunk in stream:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript TypeScript SDK theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const stream = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
          { role: "user", content: "What are the most popular open-source alternatives to OpenAI's GPT models?" }
      ],
      stream: true,
  });

  for await (const chunk of stream) {
      if (chunk.choices[0].delta.content) {
          process.stdout.write(chunk.choices[0].delta.content);
      }
  }
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "What are the most popular open-source alternatives to OpenAI'\''s GPT models?"
        }
      ],
      "stream": true
    }'
  ```
</CodeGroup>

<Info title="Complete Streaming Guide" href="/docs/grounded-llm/output-control/streaming-responses">
  For a full guide on streaming, including parsing, error handling, citation management, and best practices, see our [streaming guide](/docs/grounded-llm/output-control/streaming-responses).
</Info>

## Response Structure

Chat Completions responses follow the OpenAI-compatible format:

```json theme={null}
{
    "id": "pplx-1234567890",
    "model": "sonar-pro",
    "created": 1234567890,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "The 2025 French Open Finals results..."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 12,
        "completion_tokens": 315,
        "total_tokens": 327
    }
}
```

## Next Steps

<CardGroup>
  <Card title="Chat Completions Guide" icon="book" href="/docs/grounded-llm/openai-compatibility">
    Complete guide to the Chat Completions API with advanced features and examples.
  </Card>

  <Card title="Models" icon="brain" href="/docs/grounded-llm/chat-completions/models">
    Explore available Sonar models and their capabilities.
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/chat-completions-post">
    View complete endpoint documentation and parameters.
  </Card>

  <Card title="Search Controls" icon="magnifying-glass" href="/docs/grounded-llm/chat-completions/filters/search-control">
    Learn how to control search behavior with filters and parameters.
  </Card>

  <Card title="Agentic Research API" icon="code" href="/docs/grounded-llm/responses/quickstart">
    Need structured outputs or third-party models? Check out the Agentic Research API.
  </Card>

  <Card title="Search API" icon="magnifying-glass" href="/docs/search/quickstart">
    Get raw search results with the Search API.
  </Card>
</CardGroup>

<Info>
  Need help? Check out our [community](https://community.perplexity.ai) for support and discussions with other developers.
</Info>


# Date and Time Filters
Source: https://docs.perplexity.ai/docs/grounded-llm/filters/date-range-filter



<Note>
  The `search_after_date_filter` and `search_before_date_filter` parameters allow you to restrict search results to a specific publication date range. Only results with publication dates falling between these dates will be returned.

  The `last_updated_after_filter` and `last_updated_before_filter` parameters allow you to filter by when content was last modified or updated, rather than when it was originally published.

  The `search_recency_filter` parameter provides a convenient way to filter results by predefined time periods (e.g., "day", "week", "month", "year") relative to the current date.
</Note>

<Info>
  Specific date filters must be provided in the "%m/%d/%Y" format (e.g., "3/1/2025"). Recency filters use predefined values like "day", "week", "month", or "year". All filters are optional—you may supply either specific dates or recency filters as needed.
</Info>

## Overview

Date and time filters allow you to control which search results are returned by limiting them to specific time periods. There are three types of date and time filters available:

### Publication Date Filters

The `search_after_date_filter` and `search_before_date_filter` parameters filter results based on when content was **originally created or published**. This is useful when you need to:

* Find content published within a specific timeframe
* Exclude outdated or overly recent publications
* Focus on content from a particular publication period

### Last Updated Date Filters

The `last_updated_after_filter` and `last_updated_before_filter` parameters filter results based on when content was **last modified or updated**. This is useful when you need to:

* Find recently updated or maintained content
* Exclude stale content that hasn't been updated recently
* Focus on content that has been refreshed within a specific period

### Search Recency Filter

The `search_recency_filter` parameter provides a simple way to filter results by predefined time periods relative to the current date. This is useful when you need to:

* Find content from the past day, week, month, or year
* Get recent results without specifying exact dates
* Quickly filter for timely information

**Available values:**

* `"day"` - Content from the past 24 hours
* `"week"` - Content from the past 7 days
* `"month"` - Content from the past 30 days
* `"year"` - Content from the past 365 days

**Important:** These filter types target different dates—publication filters use the original creation/publication date, while last updated filters use the modification date, and recency filters use a relative time period from the current date.

To constrain search results by publication date:

```bash theme={null}
"search_after_date_filter": "3/1/2025",
"search_before_date_filter": "3/5/2025"
```

To constrain search results by last updated date:

```bash theme={null}
"last_updated_after_filter": "3/1/2025",
"last_updated_before_filter": "3/5/2025"
```

To constrain search results by recency:

```bash theme={null}
"search_recency_filter": "week"
```

These filters will be applied in addition to any other search parameters (for example, domain filters).

## Examples

**1. Limiting Results by Publication Date Range**

This example limits search results to content published between March 1, 2025, and March 5, 2025.

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      response = client.responses.create(
          preset="fast-search",
          input="Show me tech news published this week.",
          instructions="You are an expert on current events.",
          tools=[
              {
                  "type": "web_search",
                  "filters": {
                      "search_after_date_filter": "3/1/2025",
                      "search_before_date_filter": "3/5/2025"
                  }
              }
          ]
      )


      print(response.output_text)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: "fast-search",
        input: "Show me tech news published this week.",
        instructions: "You are an expert on current events.",
        tools: [
          {
            type: "web_search",
            filters: {
              search_after_date_filter: "3/1/2025",
              search_before_date_filter: "3/5/2025"
            }
          }
        ]
      });

      console.log(response.output_text);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/v1/responses' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "preset": "fast-search",
          "input": "Show me tech news published this week.",
          "instructions": "You are an expert on current events.",
          "tools": [{
            "type": "web_search",
            "filters": {
              "search_after_date_filter": "3/1/2025",
              "search_before_date_filter": "3/5/2025"
            }
          }]
      }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      completion = client.chat.completions.create(
          model="sonar",
          messages=[
              {"role": "system", "content": "You are an expert on current events."},
              {"role": "user", "content": "Show me tech news published this week."}
          ],
          search_after_date_filter="3/1/2025",
          search_before_date_filter="3/5/2025"
      )

      print(completion.choices[0].message.content)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        model: "sonar",
        messages: [
          {"role": "system", "content": "You are an expert on current events."},
          {"role": "user", "content": "Show me tech news published this week."}
        ],
        search_after_date_filter: "3/1/2025",
        search_before_date_filter: "3/5/2025"
      });

      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/chat/completions' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "model": "sonar",
          "messages": [
            {"role": "system", "content": "You are an expert on current events."},
            {"role": "user", "content": "Show me tech news published this week."}
          ],
          "search_after_date_filter": "3/1/2025",
          "search_before_date_filter": "3/5/2025"
      }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

**2. Filtering with a Single Publication Date Parameter**

If you only wish to restrict the results to those published on or after a specific date, include just the `search_after_date_filter`:

```bash theme={null}
payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Show me news articles published after March 1, 2025."}
    ],
    "search_after_date_filter": "3/1/2025"
}
```

**3. Filtering by Last Updated Date Range**

This example limits search results to content that was last updated between March 1, 2025, and March 5, 2025. This is useful for finding recently maintained or refreshed content.

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      response = client.responses.create(
          preset="pro-search",
          input="Show me recently updated tech articles.",
          instructions="You are an expert on current events.",
          tools=[
              {
                  "type": "web_search",
                  "filters": {
                      "last_updated_after_filter": "3/1/2025",
                      "last_updated_before_filter": "3/5/2025"
                  }
              }
          ]
      )


      print(response.output_text)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: "pro-search",
        input: "Show me recently updated tech articles.",
        instructions: "You are an expert on current events.",
        tools: [
          {
            type: "web_search",
            filters: {
              last_updated_after_filter: "3/1/2025",
              last_updated_before_filter: "3/5/2025"
            }
          }
        ]
      });

      console.log(response.output_text);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/v1/responses' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "preset": "pro-search",
          "input": "Show me recently updated tech articles.",
          "instructions": "You are an expert on current events.",
          "tools": [{
            "type": "web_search",
            "filters": {
              "last_updated_after_filter": "3/1/2025",
              "last_updated_before_filter": "3/5/2025"
            }
          }]
      }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      completion = client.chat.completions.create(
          model="sonar-pro",
          messages=[
              {"role": "system", "content": "You are an expert on current events."},
              {"role": "user", "content": "Show me recently updated tech articles."}
          ],
          last_updated_after_filter="3/1/2025",
          last_updated_before_filter="3/5/2025"
      )

      print(completion.choices[0].message.content)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        model: "sonar-pro",
        messages: [
          {"role": "system", "content": "You are an expert on current events."},
          {"role": "user", "content": "Show me recently updated tech articles."}
        ],
        last_updated_after_filter: "3/1/2025",
        last_updated_before_filter: "3/5/2025"
      });

      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/chat/completions' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "model": "sonar-pro",
          "messages": [
            {"role": "system", "content": "You are an expert on current events."},
            {"role": "user", "content": "Show me recently updated tech articles."}
          ],
          "last_updated_after_filter": "3/1/2025",
          "last_updated_before_filter": "3/5/2025"
      }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

**4. Combining Publication and Last Updated Filters**

You can combine both filter types to find content that was published in one timeframe and updated in another:

```bash theme={null}
payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Show me articles published last year but updated recently."}
    ],
    "search_after_date_filter": "1/1/2024",
    "search_before_date_filter": "12/31/2024",
    "last_updated_after_filter": "3/1/2025"
}
```

**5. Using Search Recency Filter**

The `search_recency_filter` provides a convenient way to filter results by predefined time periods without specifying exact dates:

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      response = client.responses.create(
          preset="pro-search",
          input="What are the latest AI developments?",
          instructions="You are an expert on current events.",
          tools=[
              {
                  "type": "web_search",
                  "filters": {
                      "search_recency_filter": "week"
                  }
              }
          ]
      )


      print(response.output_text)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: "pro-search",
        input: "What are the latest AI developments?",
        instructions: "You are an expert on current events.",
        tools: [
          {
            type: "web_search",
            filters: {
              search_recency_filter: "week"
            }
          }
        ]
      });

      console.log(response.output_text);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/v1/responses' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "preset": "pro-search",
          "input": "What are the latest AI developments?",
          "instructions": "You are an expert on current events.",
          "tools": [{
            "type": "web_search",
            "filters": {
              "search_recency_filter": "week"
            }
          }]
      }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      completion = client.chat.completions.create(
          model="sonar-pro",
          messages=[
              {"role": "system", "content": "You are an expert on current events."},
              {"role": "user", "content": "What are the latest AI developments?"}
          ],
          search_recency_filter="week"
      )

      print(completion.choices[0].message.content)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        model: "sonar-pro",
        messages: [
          {"role": "system", "content": "You are an expert on current events."},
          {"role": "user", "content": "What are the latest AI developments?"}
        ],
        search_recency_filter: "week"
      });

      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/chat/completions' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "model": "sonar-pro",
          "messages": [
            {"role": "system", "content": "You are an expert on current events."},
            {"role": "user", "content": "What are the latest AI developments?"}
          ],
          "search_recency_filter": "week"
      }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

This example will return only content from the past 7 days, automatically calculated from the current date.

## Best Practices

**Date Format**

* Strict Format: Dates must match the “%m/%d/%Y” format exactly. For example, the date “3/1/2025” or “03/01/2025” is acceptable.
* Consistency: Use one or both filters consistently based on your search needs. Combining both provides a clear range.

**Filter Selection**

* Choose the Right Filter Type: Use publication date filters (`search_after_date_filter`/`search_before_date_filter`) when you care about when content was originally created. Use last updated filters (`last_updated_after_filter`/`last_updated_before_filter`) when you need recently maintained content. Use recency filters (`search_recency_filter`) for quick, relative time filtering.
* Recency vs. Exact Dates: Use `search_recency_filter` for convenience when you want recent content (e.g., "past week"). Use specific date filters when you need precise control over the time range.
* Combining Filters: You can use both publication and last updated filters together to find content that meets both criteria (e.g., published in 2024 but updated recently). Note that `search_recency_filter` cannot be combined with other date filters.

**Client-Side Validation**

* Regex Check: Validate date strings on the client side (or via the API) using a regex such as:

<CodeGroup>
  ```bash theme={null}
  date_regex='^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/[0-9]{4}$'
  ```

  ```python theme={null}
  date_regex = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/\d{4}$'
  ```
</CodeGroup>

This ensures that dates conform to the required format before sending the request.

**Performance Considerations**

* Narrowing the Search: Applying date range filters typically reduces the number of results, which may improve response times and result relevance.
* Avoid Over-Restriction: Ensure that the date range is neither too narrow (limiting useful results) nor too broad (defeating the purpose of the filter).

⸻

## Last Updated Date Filters

The `last_updated_after_filter` and `last_updated_before_filter` parameters provide powerful filtering capabilities based on when content was last modified or updated, rather than when it was originally published. This is particularly useful for finding recently maintained, refreshed, or updated content.

### Parameters

**`last_updated_after_filter`**

* Filters search results to only include content last updated after this date
* Format should be %m/%d/%Y (e.g. 3/1/2025)
* Optional parameter

**`last_updated_before_filter`**

* Filters search results to only include content last updated before this date
* Format should be %m/%d/%Y (e.g. 3/1/2025)
* Optional parameter

### Use Cases

**Content Freshness**: Find articles, documentation, or resources that have been recently updated to ensure you're getting the most current information.

**Maintenance Tracking**: Identify which content has been actively maintained within a specific timeframe.

**Quality Assurance**: Focus on content that has been refreshed recently, which often indicates higher quality and relevance.

### Code Examples

**1. Find Recently Updated Content (After a Specific Date)**

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.perplexity.ai/chat/completions' \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {"role": "system", "content": "You are a helpful assistant focused on current information."},
        {"role": "user", "content": "Find me documentation that has been updated recently."}
      ],
      "last_updated_after_filter": "1/1/2025"
  }' | jq
  ```

  ```python python theme={null}
  import requests

  url = "https://api.perplexity.ai/chat/completions"
  headers = {"Authorization": "Bearer YOUR_API_KEY"}
  payload = {
      "model": "sonar-pro",
      "messages": [
          {"role": "system", "content": "You are a helpful assistant focused on current information."},
          {"role": "user", "content": "Find me documentation that has been updated recently."}
      ],
      "last_updated_after_filter": "1/1/2025"
  }

  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```

  ```javascript javascript theme={null}
  const response = await fetch('https://api.perplexity.ai/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'sonar-pro',
      messages: [
        {role: 'system', content: 'You are a helpful assistant focused on current information.'},
        {role: 'user', content: 'Find me documentation that has been updated recently.'}
      ],
      last_updated_after_filter: '1/1/2025'
    })
  });

  const data = await response.json();
  console.log(data);
  ```
</CodeGroup>

**2. Find Content Updated Within a Specific Window**

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.perplexity.ai/chat/completions' \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {"role": "system", "content": "You are an expert on technology trends."},
        {"role": "user", "content": "Show me tech articles that were updated last week."}
      ],
      "last_updated_after_filter": "2/24/2025",
      "last_updated_before_filter": "3/3/2025"
  }' | jq
  ```

  ```python python theme={null}
  import requests
  from datetime import datetime, timedelta

  # Calculate dates for last week
  today = datetime.now()
  week_ago = today - timedelta(days=7)

  url = "https://api.perplexity.ai/chat/completions"
  headers = {"Authorization": "Bearer YOUR_API_KEY"}
  payload = {
      "model": "sonar-pro",
      "messages": [
          {"role": "system", "content": "You are an expert on technology trends."},
          {"role": "user", "content": "Show me tech articles that were updated last week."}
      ],
      "last_updated_after_filter": week_ago.strftime("%m/%d/%Y"),
      "last_updated_before_filter": today.strftime("%m/%d/%Y")
  }

  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```
</CodeGroup>

**3. Exclude Recently Updated Content (Before a Date)**

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.perplexity.ai/chat/completions' \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {"role": "system", "content": "You are a research assistant."},
        {"role": "user", "content": "Find historical content that hasn'\''t been updated recently."}
      ],
      "last_updated_before_filter": "1/1/2024"
  }' | jq 
  ```

  ```python python theme={null}
  import requests

  url = "https://api.perplexity.ai/chat/completions"
  headers = {"Authorization": "Bearer YOUR_API_KEY"}
  payload = {
      "model": "sonar-pro",
      "messages": [
          {"role": "system", "content": "You are a research assistant."},
          {"role": "user", "content": "Find historical content that hasn't been updated recently."}
      ],
      "last_updated_before_filter": "1/1/2024"
  }

  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```
</CodeGroup>

### Advanced Usage Patterns

**Combining with Domain Filters**

```python theme={null}
payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "user", "content": "Latest updates on AI research."}
    ],
    "search_domain_filter": ["arxiv.org", "openai.com"],
    "last_updated_after_filter": "2/1/2025"
}
```

**Finding Maintained vs. Stale Content**

```python theme={null}
# Find actively maintained content
recent_payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "user", "content": "Current best practices for React development."}
    ],
    "last_updated_after_filter": "1/1/2025"
}

# Find potentially outdated content
stale_payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "user", "content": "React development practices."}
    ],
    "last_updated_before_filter": "1/1/2023"
}
```

### Tips for Last Updated Filters

1. **Content Freshness Strategy**: Use `last_updated_after_filter` when you need the most current information on rapidly evolving topics.

2. **Quality Indicator**: Recently updated content often indicates active maintenance and higher reliability.

3. **Research Applications**: Combine with publication date filters to find content published years ago but updated recently, indicating ongoing relevance.

4. **Performance**: These filters can significantly improve response relevance by focusing on maintained content.

5. **Date Selection**: Choose update date ranges based on your content type - technical documentation might need monthly updates, while academic papers might be updated annually.


# Domain Filter Guide
Source: https://docs.perplexity.ai/docs/grounded-llm/filters/domain-filters



<Note>
  The `search_domain_filter` feature allows you to limit search results to specific domains/URLs or exclude certain domains/URLs from search results. This supports both broad domain-level filtering and granular URL-level filtering for precise content control.
</Note>

<Warning>
  You can add a maximum of 20 domains or URLs to the `search_domain_filter` list. The filter works in either allowlist mode (include only) or denylist mode (exclude), but not both simultaneously.
</Warning>

<Warning>
  Before adding URLs to your allowlist, test that they are accessible via the API by making a sample request. URLs that are blocked, require authentication, or have access restrictions may not return search results, which can significantly impact response quality when using allowlist mode.
</Warning>

## Overview

The `search_domain_filter` parameter allows you to control which websites are included in or excluded from the search results used by Grounded LLMs. This feature is particularly useful when you want to:

* Restrict search results to trusted sources
* Filter out specific domains from search results
* Focus research on particular websites

Enabling domain filtering can be done by adding a `search_domain_filter` field in the request:

```
"search_domain_filter": [
  "<domain1>",
  "<domain2>",
  ...
]
```

Each entry in the list can be a domain name or a specific URL. The filter operates in two modes:

* **Allowlist mode**: Include only the specified domains/URLs (no `-` prefix)
* **Denylist mode**: Exclude the specified domains/URLs (use `-` prefix)

## Filtering Capabilities

### Domain-Level Filtering

Filter entire domains for broad control:

```json theme={null}
// Allowlist: Only search these domains
"search_domain_filter": ["wikipedia.org", "github.com", "stackoverflow.com"]

// Denylist: Exclude these domains  
"search_domain_filter": ["-reddit.com", "-pinterest.com", "-quora.com"]
```

### URL-Level Filtering

Target specific pages or sections for granular control:

```json theme={null}
// Allowlist: Only search these specific URLs
"search_domain_filter": [
  "https://en.wikipedia.org/wiki/Chess",
  "https://stackoverflow.com/questions/tagged/python",
  "https://docs.python.org/3/tutorial/"
]

// Denylist: Exclude these specific URLs
"search_domain_filter": [
  "-https://en.wikipedia.org/wiki/FIDE_rankings",
  "-https://reddit.com/r/politics"
]
```

This granular approach allows you to:

* Include or exclude specific Wikipedia articles while keeping/removing the rest
* Target particular sections of large sites like Stack Overflow or Reddit
* Filter specific documentation pages or subdirectories

## Examples

### 1. Allowlist Specific Domains

This example shows how to limit search results to only include content from specific domains.

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      response = client.responses.create(
          preset="fast-search",
          input="Tell me about the James Webb Space Telescope discoveries.",
          instructions="You are a helpful assistant.",
          tools=[
              {
                  "type": "web_search",
                  "filters": {
                      "search_domain_filter": [
                          "nasa.gov",
                          "wikipedia.org",
                          "space.com"
                      ]
                  }
              }
          ]
      )


      print(response.output_text)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: "fast-search",
        input: "Tell me about the James Webb Space Telescope discoveries.",
        instructions: "You are a helpful assistant.",
        tools: [
          {
            type: "web_search",
            filters: {
              search_domain_filter: [
                "nasa.gov",
                "wikipedia.org",
                "space.com"
              ]
            }
          }
        ]
      });

      console.log(response.output_text);
      ```

      ```bash cURL theme={null}
      curl --request POST \
        --url https://api.perplexity.ai/v1/responses \
        --header "Authorization: Bearer YOUR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "preset": "fast-search",
          "input": "Tell me about the James Webb Space Telescope discoveries.",
          "instructions": "You are a helpful assistant.",
          "tools": [{
            "type": "web_search",
            "filters": {
              "search_domain_filter": [
                "nasa.gov",
                "wikipedia.org",
                "space.com"
              ]
            }
          }]
        }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      completion = client.chat.completions.create(
          model="sonar",
          messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": "Tell me about the James Webb Space Telescope discoveries."}
          ],
          search_domain_filter=[
              "nasa.gov",
              "wikipedia.org",
              "space.com"
          ]
      )

      print(completion.choices[0].message.content)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        model: "sonar",
        messages: [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Tell me about the James Webb Space Telescope discoveries."}
        ],
        search_domain_filter: [
          "nasa.gov",
          "wikipedia.org",
          "space.com"
        ]
      });

      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl --request POST \
        --url https://api.perplexity.ai/chat/completions \
        --header "Authorization: Bearer YOUR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "model": "sonar",
          "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me about the James Webb Space Telescope discoveries."}
          ],
          "search_domain_filter": [
            "nasa.gov",
            "wikipedia.org",
            "space.com"
          ]
        }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

**Best Practice**: Use simple domain names (e.g., `wikipedia.org`) without additional elements like `https://` or `www.` prefixes.

### 2. Denylist Specific Domains

This example shows how to exclude specific domains from search results by prefixing the domain name with a minus sign (`-`).

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      response = client.responses.create(
          preset="fast-search",
          input="What are the latest advancements in renewable energy?",
          instructions="You are a helpful assistant.",
          tools=[
              {
                  "type": "web_search",
                  "filters": {
                      "search_domain_filter": [
                          "-pinterest.com",
                          "-reddit.com",
                          "-quora.com"
                      ]
                  }
              }
          ]
      )


      print(response.output_text)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: "fast-search",
        input: "What are the latest advancements in renewable energy?",
        instructions: "You are a helpful assistant.",
        tools: [
          {
            type: "web_search",
            filters: {
              search_domain_filter: [
                "-pinterest.com",
                "-reddit.com",
                "-quora.com"
              ]
            }
          }
        ]
      });

      console.log(response.output_text);
      ```

      ```bash cURL theme={null}
      curl --request POST \
        --url https://api.perplexity.ai/v1/responses \
        --header "Authorization: Bearer YOUR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "preset": "fast-search",
          "input": "What are the latest advancements in renewable energy?",
          "instructions": "You are a helpful assistant.",
          "tools": [{
            "type": "web_search",
            "filters": {
              "search_domain_filter": [
                "-pinterest.com",
                "-reddit.com",
                "-quora.com"
              ]
            }
          }]
        }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      completion = client.chat.completions.create(
          model="sonar",
          messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": "What are the latest advancements in renewable energy?"}
          ],
          search_domain_filter=[
              "-pinterest.com",
              "-reddit.com",
              "-quora.com"
          ]
      )

      print(completion.choices[0].message.content)
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        model: "sonar",
        messages: [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "What are the latest advancements in renewable energy?"}
        ],
        search_domain_filter: [
          "-pinterest.com",
          "-reddit.com",
          "-quora.com"
        ]
      });

      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl --request POST \
        --url https://api.perplexity.ai/chat/completions \
        --header "Authorization: Bearer YOUR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "model": "sonar",
          "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What are the latest advancements in renewable energy?"}
          ],
          "search_domain_filter": [
            "-pinterest.com",
            "-reddit.com",
            "-quora.com"
          ]
        }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

**Best Practice**: Use simple domain names with a minus prefix (e.g., `-pinterest.com`) to exclude domains from search results.

### 3. URL-Level Filtering for Granular Control

This example shows how to exclude specific pages while keeping the rest of the domain accessible.

**Request**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Tell me about chess rankings and tournaments."}
      ],
      search_domain_filter=[
          "-https://en.wikipedia.org/wiki/FIDE_rankings"
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar-pro",
    messages: [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Tell me about chess rankings and tournaments."}
    ],
    search_domain_filter: [
      "-https://en.wikipedia.org/wiki/FIDE_rankings"
    ]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about chess rankings and tournaments."}
      ],
      "search_domain_filter": [
        "-https://en.wikipedia.org/wiki/FIDE_rankings"
      ]
    }' | jq
  ```
</CodeGroup>

**Result**: This will search all websites except the specific FIDE rankings Wikipedia page, while keeping all other Wikipedia content accessible.

**Alternative - Allowlist specific URLs only:**

```json theme={null}
"search_domain_filter": [
  "https://en.wikipedia.org/wiki/Chess",
  "https://en.wikipedia.org/wiki/World_Chess_Championship",
  "https://chess.com"
]
```

This would only search those three specific sources and ignore all other websites.

## Best Practices

### Domain and URL Specification

* **Domain filtering**: Use simple domain names (e.g., `example.com`) without protocol prefixes for broad filtering.
* **URL filtering**: Use complete URLs including protocol (e.g., `https://en.wikipedia.org/wiki/FIDE_rankings`) for specific page targeting.
* **Subdomain behavior**: Using a main domain (e.g., `nytimes.com`) will filter all subdomains as well.
* **Granular control**: URL-level filtering allows you to include/exclude specific pages while keeping the rest of the domain.

### Filter Optimization

* **Be specific**: Use domains/URLs that are most relevant to your query to get the best results.
* **Choose your mode**: Use either allowlist mode (include only) OR denylist mode (exclude), but not both in the same request.
* **Limit filter size**: You can add up to 20 domains or URLs. Using fewer, more targeted entries often yields better results.
* **URL precision**: Use full URLs (including `https://`) when targeting specific pages for maximum precision.

### Performance Considerations

* Adding domain filters may slightly increase response time as the search engine needs to apply additional filtering.
* Overly restrictive domain filters might result in fewer search results, potentially affecting the quality of the response.


# User Location Filter Guide
Source: https://docs.perplexity.ai/docs/grounded-llm/filters/user-location-filter



<Note>
  The `user_location` parameter within `web_search_options` allows you to refine search results based on the user's approximate geographic location. This helps provide more contextually relevant information.
</Note>

<Info>
  You can specify the location using latitude/longitude coordinates, country code, city, and region. For the most accurate results, we recommend providing as much location information as possible, including `city` and `region` fields. For supported country codes, please refer to the list [here](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
</Info>

<Tip>
  The `city` and `region` fields significantly improve location accuracy. We strongly recommend including them alongside coordinates and country code for the best results.
</Tip>

<Warning>
  Latitude and longitude must be provided alongside the country parameter, they cannot be provided on their own.
</Warning>

## Overview

The `user_location` filter helps tailor search results by incorporating geographic context. This is particularly useful for queries where location significantly impacts relevance, such as:

* Finding local businesses or services.
* Getting information about regional events or news.
* Understanding location-specific regulations or customs.

To refine search results by location, include the `user_location` object within the `web_search_options` in your request payload. You can provide coordinates, country code, city, region, or combine them for maximum accuracy:

**Using All Available Fields (Recommended for Best Accuracy):**

```json theme={null}
"web_search_options": {
  "user_location": {
    "country": "US",
    "region": "California",
    "city": "San Francisco",
    "latitude": 37.7749,
    "longitude": -122.4194
  }
}
```

**Using City and Region with Country:**

```json theme={null}
"web_search_options": {
  "user_location": {
    "country": "US",
    "region": "New York",
    "city": "New York City"
  }
}
```

**Using Latitude/Longitude:**

```json theme={null}
"web_search_options": {
  "user_location": {
    "country":"US",
    "latitude": 37.7749,
    "longitude": -122.4194
  }
}
```

**Using Country Code Only:**

```json theme={null}
"web_search_options": {
  "user_location": {
    "country": "US"
  }
}
```

These filters work alongside other search parameters like date range or domain filters.

## Examples

**1. Refining Results with All Location Fields (Recommended)**

This example provides all available location fields for San Francisco to get the most accurate geographically relevant search results.

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      response = client.responses.create(
          preset="pro-search",
          input="What are some good coffee shops nearby?",
          instructions="You are a helpful local guide.",
          tools=[
              {
                  "type": "web_search",
                  "user_location": {
                      "country": "US",
                      "region": "California",
                      "city": "San Francisco",
                      "latitude": 37.7749,
                      "longitude": -122.4194
                  }
              }
          ]
      )


      print(f"Response: {response.output_text}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: "pro-search",
        input: "What are some good coffee shops nearby?",
        instructions: "You are a helpful local guide.",
        tools: [
          {
            type: "web_search",
            user_location: {
              country: "US",
              region: "California",
              city: "San Francisco",
              latitude: 37.7749,
              longitude: -122.4194
            }
          }
        ]
      });

      console.log(`Response: ${response.output_text}`);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/v1/responses' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "preset": "pro-search",
          "input": "What are some good coffee shops nearby?",
          "instructions": "You are a helpful local guide.",
          "tools": [{
            "type": "web_search",
            "user_location": {
              "country": "US",
              "region": "California",
              "city": "San Francisco",
              "latitude": 37.7749,
              "longitude": -122.4194
            }
          }]
      }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      completion = client.chat.completions.create(
          messages=[
              {"role": "system", "content": "You are a helpful local guide."},
              {"role": "user", "content": "What are some good coffee shops nearby?"}
          ],
          model="sonar-pro",
          web_search_options={
              "user_location": {
                  "country": "US",
                  "region": "California",
                  "city": "San Francisco",
                  "latitude": 37.7749,
                  "longitude": -122.4194
              }
          }
      )

      print(f"Response: {completion.choices[0].message.content}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        messages: [
          {"role": "system", "content": "You are a helpful local guide."},
          {"role": "user", "content": "What are some good coffee shops nearby?"}
        ],
        model: "sonar-pro",
        web_search_options: {
          user_location: {
            country: "US",
            region: "California",
            city: "San Francisco",
            latitude: 37.7749,
            longitude: -122.4194
          }
        }
      });

      console.log(`Response: ${completion.choices[0].message.content}`);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/chat/completions' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "model": "sonar-pro",
          "messages": [
            {"role": "system", "content": "You are a helpful local guide."},
            {"role": "user", "content": "What are some good coffee shops nearby?"}
          ],
          "web_search_options": {
            "user_location": {
              "country": "US",
              "region": "California",
              "city": "San Francisco",
              "latitude": 37.7749,
              "longitude": -122.4194
            }
          }
      }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

**2. Refining Results with Country Code**

This example uses a two-letter ISO country code (United States) to provide broader geographic context.

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      response = client.responses.create(
          preset="pro-search",
          input="Summarize political news from today.",
          instructions="You are an expert on international news.",
          tools=[
              {
                  "type": "web_search",
                  "user_location": {
                      "country": "US"
                  }
              }
          ]
      )


      print(f"Response: {response.output_text}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: "pro-search",
        input: "Summarize political news from today.",
        instructions: "You are an expert on international news.",
        tools: [
          {
            type: "web_search",
            user_location: {
              country: "US"
            }
          }
        ]
      });

      console.log(`Response: ${response.output_text}`);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/v1/responses' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "preset": "pro-search",
          "input": "Summarize political news from today.",
          "instructions": "You are an expert on international news.",
          "tools": [{
            "type": "web_search",
            "user_location": {
              "country": "US"
            }
          }]
      }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      completion = client.chat.completions.create(
          messages=[
              {"role": "system", "content": "You are an expert on international news."},
              {"role": "user", "content": "Summarize political news from today."}
          ],
          model="sonar-pro",
          web_search_options={
              "user_location": {
                  "country": "US"
              }
          }
      )

      print(f"Response: {completion.choices[0].message.content}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        messages: [
          {"role": "system", "content": "You are an expert on international news."},
          {"role": "user", "content": "Summarize political news from today."}
        ],
        model: "sonar-pro",
        web_search_options: {
          user_location: {
            country: "US"
          }
        }
      });

      console.log(`Response: ${completion.choices[0].message.content}`);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/chat/completions' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "model": "sonar-pro",
          "messages": [
            {"role": "system", "content": "You are an expert on international news."},
            {"role": "user", "content": "Summarize political news from today."}
          ],
          "web_search_options": {
            "user_location": {
              "country": "US"
            }
          }
      }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

**3. Using City and Region for Better Accuracy**

This example shows how to use `city` and `region` fields along with coordinates for Paris, France to achieve maximum location accuracy.

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      response = client.responses.create(
          preset="pro-search",
          input="What major events are happening in the capital this week?",
          instructions="You are an expert on French news and events.",
          tools=[
              {
                  "type": "web_search",
                  "user_location": {
                      "country": "FR",
                      "region": "Île-de-France",
                      "city": "Paris",
                      "latitude": 48.8566,
                      "longitude": 2.3522
                  }
              }
          ]
      )


      print(f"Response: {response.output_text}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: "pro-search",
        input: "What major events are happening in the capital this week?",
        instructions: "You are an expert on French news and events.",
        tools: [
          {
            type: "web_search",
            user_location: {
              country: "FR",
              region: "Île-de-France",
              city: "Paris",
              latitude: 48.8566,
              longitude: 2.3522
            }
          }
        ]
      });

      console.log(`Response: ${response.output_text}`);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/v1/responses' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "preset": "pro-search",
          "input": "What major events are happening in the capital this week?",
          "instructions": "You are an expert on French news and events.",
          "tools": [{
            "type": "web_search",
            "user_location": {
              "country": "FR",
              "region": "Île-de-France",
              "city": "Paris",
              "latitude": 48.8566,
              "longitude": 2.3522
            }
          }]
      }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      completion = client.chat.completions.create(
          messages=[
              {"role": "system", "content": "You are an expert on French news and events."},
              {"role": "user", "content": "What major events are happening in the capital this week?"}
          ],
          model="sonar-pro",
          web_search_options={
              "user_location": {
                  "country": "FR",
                  "region": "Île-de-France",
                  "city": "Paris",
                  "latitude": 48.8566,
                  "longitude": 2.3522
              }
          }
      )

      print(f"Response: {completion.choices[0].message.content}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        messages: [
          {"role": "system", "content": "You are an expert on French news and events."},
          {"role": "user", "content": "What major events are happening in the capital this week?"}
        ],
        model: "sonar-pro",
        web_search_options: {
          user_location: {
            country: "FR",
            region: "Île-de-France",
            city: "Paris",
            latitude: 48.8566,
            longitude: 2.3522
          }
        }
      });

      console.log(`Response: ${completion.choices[0].message.content}`);
      ```

      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/chat/completions' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
          "model": "sonar-pro",
          "messages": [
            {"role": "system", "content": "You are an expert on French news and events."},
            {"role": "user", "content": "What major events are happening in the capital this week?"}
          ],
          "web_search_options": {
            "user_location": {
              "country": "FR",
              "region": "Île-de-France",
              "city": "Paris",
              "latitude": 48.8566, 
              "longitude": 2.3522
            }
          }
      }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Best Practices

**Choosing the Right Specificity**

* **All Fields (Recommended):** For maximum accuracy, provide country, region, city, latitude, and longitude. This combination gives the best results for location-specific queries.
* **City and Region:** Use these fields to significantly improve location accuracy without needing exact coordinates. Particularly useful for metropolitan areas and regional searches.
* **Latitude/Longitude:** Use for high precision when the exact location is known and relevant (e.g., finding nearby points of interest).
* **Country Code:** Use for broader context when country-level relevance is sufficient (e.g., national news, country-specific regulations).
* **Combining Fields:** We strongly recommend providing as many location fields as possible. Each additional field improves search accuracy and relevance.

**Data Accuracy**

* Ensure the provided location data is as accurate as possible. Incorrect data may lead to irrelevant results.
* Latitude values must be between -90 and 90. Longitude values must be between -180 and 180.
* Country codes should be valid two-letter ISO 3166-1 alpha-2 codes (e.g., "US", "GB", "DE").
* City names should match commonly used names (e.g., "New York City" or "NYC" for New York).
* Region names should match standard administrative divisions (states, provinces, etc.).

**Privacy Considerations**

* Be mindful of user privacy when collecting and transmitting location data. Only use location when necessary and with user consent where applicable.

**Client-Side Validation**

* Consider validating location inputs before sending the request:
  * Check latitude/longitude ranges.
  * Validate country code format (two uppercase letters).
  * Sanitize city and region inputs for special characters.


# Image Attachments
Source: https://docs.perplexity.ai/docs/grounded-llm/media/image-attachments

Learn how to upload and analyze images using base64 encoding or HTTPS URLs

## Overview

Both the Agentic Research API and Chat Completions API support image analysis through direct image uploads. Images can be provided either as base64 encoded strings within a data URI or as standard HTTPS URLs.

<Warning>
  * When using base64 encoding, the API currently only supports images up to 50 MB per image.
  * Supported formats for base64 encoded images: PNG (image/png), JPEG (image/jpeg), WEBP (image/webp), and GIF (image/gif).
  * When using an HTTPS URL, the model will attempt to fetch the image from the provided URL. Ensure the URL is publicly accessible.
</Warning>

## Examples

<Tabs>
  <Tab title="Agentic Research API">
    <Tabs>
      <Tab title="Base64 Encoded Data">
        <Info>Use this method when you have the image file locally and want to embed it directly into the request payload. Remember the 50MB size limit and supported formats (PNG, JPEG, WEBP, GIF).</Info>

        <CodeGroup>
          ```python Python theme={null}
          import base64
          from perplexity import Perplexity

          client = Perplexity(api_key="pplx-KEY")

          # Read and encode image as base64
          def encode_image(image_path):
              with open(image_path, "rb") as image_file:
                  return base64.b64encode(image_file.read()).decode("utf-8")

          image_path = "image.png"
          base64_image = encode_image(image_path)

          # Analyze the image
          response = client.responses.create(
              model="openai/gpt-5-mini",
              input=[
                  {
                      "role": "user",
                      "content": [
                          {"type": "input_text", "text": "what's in this image?"},
                          {
                              "type": "input_image",
                              "image_url": f"data:image/png;base64,{base64_image}",
                          },
                      ],
                  }
              ],
          )

          print(response.output_text)
          ```

          ```typescript TypeScript theme={null}
          import Perplexity from '@perplexity-ai/perplexity_ai';
          import * as fs from 'fs';

          const client = new Perplexity();

          // Read and encode image as base64
          const imageBuffer = fs.readFileSync('image.png');
          const base64Image = imageBuffer.toString('base64');
          const imageDataUri = `data:image/png;base64,${base64Image}`;

          // Analyze the image
          const response = await client.responses.create({
              model: 'openai/gpt-5-mini',
              input: [
                  {
                      role: 'user',
                      content: [
                          { type: 'input_text', text: "What's in this image?" },
                          { type: 'input_image', image_url: imageDataUri }
                      ]
                  }
              ],
          });

          console.log(response.output_text);
          ```

          ```bash cURL theme={null}
          curl https://api.perplexity.ai/v1/responses \
            -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
            -H "Content-Type: application/json" \
            -d '{
              "model": "openai/gpt-5-mini",
              "input": [
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "input_text",
                      "text": "What'\''s in this image?"
                    },
                    {
                      "type": "input_image",
                      "image_url": "data:image/png;base64,$BASE64_ENCODED_IMAGE"
                    }
                  ]
                }
              ]
            }' | jq
          ```
        </CodeGroup>
      </Tab>

      <Tab title="HTTPS URL">
        <Info>Use this method when you have a publicly accessible image URL. The model will fetch the image from the provided URL.</Info>

        <CodeGroup>
          ```python Python theme={null}
          from perplexity import Perplexity

          client = Perplexity(api_key="pplx-KEY")

          image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

          # Analyze the image
          response = client.responses.create(
              model="openai/gpt-5-mini",
              input=[
                  {
                      "role": "user",
                      "content": [
                          {"type": "input_text", "text": "Can you describe the image at this URL?"},
                          {
                              "type": "input_image",
                              "image_url": image_url,
                          },
                      ],
                  }
              ],
          )

          print(response.output_text)
          ```

          ```typescript TypeScript theme={null}
          import Perplexity from '@perplexity-ai/perplexity_ai';

          const client = new Perplexity();

          const imageHttpsUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg";

          // Analyze the image
          const response = await client.responses.create({
              model: 'openai/gpt-5-mini',
              input: [
                  {
                      role: 'user',
                      content: [
                          { type: 'input_text', text: 'Can you describe the image at this URL?' },
                          { type: 'input_image', image_url: imageHttpsUrl }
                      ]
                  }
              ],
          });

          console.log(response.output_text);
          ```

          ```bash cURL theme={null}
          curl https://api.perplexity.ai/v1/responses \
            -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
            -H "Content-Type: application/json" \
            -d '{
              "model": "openai/gpt-5-mini",
              "input": [
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "input_text",
                      "text": "Can you describe the image at this URL?"
                    },
                    {
                      "type": "input_image",
                      "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                    }
                  ]
                }
              ]
            }' | jq
          ```
        </CodeGroup>
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Chat Completions API">
    <Tabs>
      <Tab title="Base64 Encoded Data">
        <Info>Use this method when you have the image file locally and want to embed it directly into the request payload. Remember the 50MB size limit and supported formats (PNG, JPEG, WEBP, GIF).</Info>

        <CodeGroup>
          ```python Python theme={null}
          from perplexity import Perplexity
          import base64

          client = Perplexity()

          # Read and encode image as base64
          try:
              with open("path/to/your/image.png", "rb") as image_file:
                  base64_image = base64.b64encode(image_file.read()).decode("utf-8")
              image_data_uri = f"data:image/png;base64,{base64_image}"
          except FileNotFoundError:
              print("Error: Image file not found.")
              exit()

          # Analyze the image
          try:
              completion = client.chat.completions.create(
                  model="sonar-pro",
                  messages=[
                      {
                          "role": "user",
                          "content": [
                              {"type": "text", "text": "Can you describe this image?"},
                              {"type": "image_url", "image_url": {"url": image_data_uri}}
                          ]
                      }
                  ]
              )
              print(completion.choices[0].message.content)
          except Exception as e:
              print(f"API Request failed: {e}")
          ```

          ```typescript TypeScript theme={null}
          import Perplexity from '@perplexity-ai/perplexity_ai';
          import * as fs from 'fs';

          const client = new Perplexity();

          // Read and encode image as base64
          try {
              const imageBuffer = fs.readFileSync('path/to/your/image.png');
              const base64Image = imageBuffer.toString('base64');
              const imageDataUri = `data:image/png;base64,${base64Image}`;
              
              // Analyze the image
              const completion = await client.chat.completions.create({
                  model: 'sonar-pro',
                  messages: [
                      {
                          role: 'user',
                          content: [
                              { type: 'text', text: 'Can you describe this image?' },
                              { type: 'image_url', image_url: { url: imageDataUri } }
                          ]
                      }
                  ]
              });
              
              console.log(completion.choices[0].message.content);
          } catch (error) {
              console.error('Error:', error.message);
          }
          ```

          ```bash cURL theme={null}
          curl --location 'https://api.perplexity.ai/chat/completions' \
            --header 'accept: application/json' \
            --header 'content-type: application/json' \
            --header "Authorization: Bearer $PERPLEXITY_API_KEY" \
            --data '{
              "model": "sonar-pro",
              "stream": false,
              "messages": [
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "Can you describe this image?"
                    },
                    {
                      "type": "image_url",
                      "image_url": {
                        "url": "data:image/png;base64,$BASE64_ENCODED_IMAGE"
                      }
                    }
                  ]
                }
              ]
            }' | jq
          ```
        </CodeGroup>
      </Tab>

      <Tab title="HTTPS URL">
        <Info>Use this method to reference an image hosted online. Ensure the URL is publicly accessible and points directly to the image file.</Info>

        <CodeGroup>
          ```python Python theme={null}
          from perplexity import Perplexity

          client = Perplexity()

          image_https_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

          # Analyze the image
          try:
              completion = client.chat.completions.create(
                  model="sonar-pro",
                  messages=[
                      {
                          "role": "user",
                          "content": [
                              {"type": "text", "text": "Can you describe the image at this URL?"},
                              {"type": "image_url", "image_url": {"url": image_https_url}}
                          ]
                      }
                  ]
              )
              print(completion.choices[0].message.content)
          except Exception as e:
              print(f"API Request failed: {e}")
          ```

          ```typescript TypeScript theme={null}
          import Perplexity from '@perplexity-ai/perplexity_ai';

          const client = new Perplexity();

          const imageHttpsUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg";

          // Analyze the image
          const analyzeImage = async (): Promise<void> => {
              try {
                  const completion = await client.chat.completions.create({
                      model: 'sonar-pro',
                      messages: [
                          {
                              role: 'user',
                              content: [
                                  { type: 'text', text: 'Can you describe the image at this URL?' },
                                  { type: 'image_url', image_url: { url: imageHttpsUrl } }
                              ]
                          }
                      ]
                  });
                  
                  console.log(completion.choices[0].message.content);
              } catch (error) {
                  console.error('API Request failed:', error.message);
              }
          };

          analyzeImage();
          ```

          ```bash cURL theme={null}
          curl --location 'https://api.perplexity.ai/chat/completions' \
            --header "accept: application/json" \
            --header "content-type: application/json" \
            --header "Authorization: Bearer $PERPLEXITY_API_KEY" \
            --data '{
              "model": "sonar-pro",
              "stream": false,
              "messages": [
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "Can you describe the image at this URL?"
                    },
                    {
                      "type": "image_url",
                      "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                      }
                    }
                  ]
                }
              ]
            }' | jq
          ```
        </CodeGroup>
      </Tab>
    </Tabs>
  </Tab>
</Tabs>

## Request Format

### Agentic Research API

Images must be embedded in the `input` array when using message array format. Each image should be provided using the following structure:

```json theme={null}
{
  "role": "user",
  "content": [
    {
      "type": "input_text",
      "text": "What's in this image?"
    },
    {
      "type": "input_image",
      "image_url": "<IMAGE_URL_OR_BASE64_DATA>"
    }
  ]
}
```

The `image_url` field accepts either:

* **A URL of the image**: A publicly accessible HTTPS URL pointing directly to the image file
* **The base64 encoded image data**: A data URI in the format `data:image/{format};base64,{base64_content}`

### Chat Completions API

Images must be embedded in the `messages` array, alongside any text input. Each image should be provided using the following structure:

```json theme={null}
{
  "type": "image_url",
  "image_url": {
    "url": "<IMAGE_URL_OR_BASE64_DATA>"
  }
}
```

The `url` field accepts either:

* **A URL of the image**: A publicly accessible HTTPS URL pointing directly to the image file
* **The base64 encoded image data**: A data URI in the format `data:image/{format};base64,{base64_content}`

## Pricing

Images are tokenized based on their pixel dimensions using the following formula:

```
tokens = (width px × height px) / 750
```

**Examples:**

* A 1024×768 image would consume: (1024 × 768) / 750 = 1,048 tokens
* A 512×512 image would consume: (512 × 512) / 750 = 349 tokens

These image tokens are then priced according to the input token pricing of the model you're using. The image tokens are added to your total token count for the request alongside any text tokens.

## Next Steps

<CardGroup>
  <Card title="Agentic Research API Quickstart" icon="rocket" href="/docs/grounded-llm/responses/quickstart">
    Get started with the Agentic Research API
  </Card>

  <Card title="Chat Completions API Quickstart" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Get started with the Chat Completions API
  </Card>

  <Card title="Tools" icon="wrench" href="/docs/grounded-llm/responses/tools">
    Learn about web\_search and fetch\_url tools
  </Card>

  <Card title="Models" icon="brain" href="/docs/grounded-llm/responses/models">
    Explore available models for image analysis
  </Card>
</CardGroup>


# OpenAI Compatibility
Source: https://docs.perplexity.ai/docs/grounded-llm/openai-compatibility

Use your existing OpenAI SDKs with Perplexity's Chat Completions and Agentic Research APIs. Full compatibility with minimal code changes.

## Overview

Perplexity's APIs are fully compatible with OpenAI's SDKs. You can use your existing OpenAI client libraries with both the **Chat Completions API** and **Agentic Research API** by simply changing the base URL and providing your Perplexity API key.

<Tip>
  **We recommend using the [Perplexity SDK](/docs/sdk/overview)** for the best experience with full type safety, enhanced features, and preset support. Use OpenAI SDKs if you're already integrated and need drop-in compatibility.
</Tip>

## Quick Start

### Chat Completions API

Use the OpenAI SDK with Perplexity's Chat Completions API:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What are the latest developments in AI?"}
        ]
    )

    print(completion.choices[0].message.content)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "What are the latest developments in AI?" }
      ]
    });

    console.log(completion.choices[0].message.content);
    ```
  </Tab>
</Tabs>

### Agentic Research API

Use the OpenAI SDK with Perplexity's Agentic Research API:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?"
    )


    print(response.output_text)
            break
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?"
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

## Configuration

### Setting Up the OpenAI SDK

Configure OpenAI SDKs to work with Perplexity by setting the `base_url` to `https://api.perplexity.ai/v2`:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_PERPLEXITY_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_PERPLEXITY_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });
    ```
  </Tab>
</Tabs>

<Info>
  **Important**: Use `base_url="https://api.perplexity.ai/v2"` (with `/v2`) for both Chat Completions and Agentic Research APIs.
</Info>

## Chat Completions API

Perplexity's Chat Completions API is fully compatible with OpenAI's Chat Completions interface.

### Basic Usage

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What are the latest developments in AI?"}
        ]
    )

    print(completion.choices[0].message.content)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "What are the latest developments in AI?" }
      ]
    });

    console.log(completion.choices[0].message.content);
    ```
  </Tab>
</Tabs>

### Streaming

Streaming works exactly like OpenAI's API:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What are the latest developments in AI?"}
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const stream = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "What are the latest developments in AI?" }
      ],
      stream: true
    });

    for await (const chunk of stream) {
      if (chunk.choices[0]?.delta?.content) {
        process.stdout.write(chunk.choices[0].delta.content);
      }
    }
    ```
  </Tab>
</Tabs>

### Perplexity-Specific Parameters

Add Perplexity-specific search parameters using `extra_body` (Python) or direct parameters (TypeScript):

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "Latest climate research findings"}
        ],
        extra_body={
            "search_domain_filter": ["nature.com", "science.org"],
            "search_recency_filter": "month"
        }
    )

    print(completion.choices[0].message.content)
    print(f"Sources: {len(completion.search_results)} articles found")
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "Latest climate research findings" }
      ],
      search_domain_filter: ["nature.com", "science.org"],
      search_recency_filter: "month"
    });

    console.log(completion.choices[0].message.content);
    console.log(`Sources: ${completion.search_results.length} articles found`);
    ```
  </Tab>
</Tabs>

## Agentic Research API

Perplexity's Agentic Research API is fully compatible with OpenAI's Agentic Research API interface.

### Basic Usage

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?"
    )


    print(response.output_text)
            break
    print(f"Response ID: {response.id}")
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?"
    });

    console.log(response.output_text);
    console.log(`Response ID: ${response.id}`);
    ```
  </Tab>
</Tabs>

### Using Presets

Presets are pre-configured setups optimized for specific use cases. Use the `extra_body` parameter (Python) or cast the parameter (TypeScript) to pass presets:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    # Use a preset instead of specifying model and parameters
    response = client.responses.create(
        input="What are the latest developments in AI?",
        extra_body={
            "preset": "pro-search"
        }
    )


    print(response.output_text)
            break
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    // Use a preset instead of specifying model and parameters
    const response = await client.responses.create({
      input: "What are the latest developments in AI?",
      preset: "pro-search"
    } as any);

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

<Info>
  See [Agentic Research API Presets](/docs/grounded-llm/agentic-research/presets) for available presets and their configurations.
</Info>

### Using Third-Party Models

You can also specify third-party models directly instead of using presets:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?"
    )


    print(response.output_text)
            break
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?"
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

### Streaming Responses

Streaming works with the Agentic Research API:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="Write a bedtime story about a unicorn.",
        stream=True
    )

    for event in response:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "Write a bedtime story about a unicorn.",
      stream: true
    });

    for await (const event of response) {
      if (event.type === "response.output_text.delta") {
        process.stdout.write(event.delta);
      }
    }
    ```
  </Tab>
</Tabs>

### Using Tools

The Agentic Research API supports tools, including web search:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?",
        tools=[
            {
                "type": "web_search",
                "filters": {
                    "search_domain_filter": ["techcrunch.com", "wired.com"]
                }
            }
        ],
        instructions="You have access to a web_search tool. Use it for current information."
    )


    print(response.output_text)
            break
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?",
      tools: [
        {
          type: "web_search",
          filters: {
            search_domain_filter: ["techcrunch.com", "wired.com"]
          }
        }
      ],
      instructions: "You have access to a web_search tool. Use it for current information."
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

## API Compatibility

### Standard OpenAI Parameters

These parameters work exactly the same as OpenAI's API:

**Chat Completions API:**

* `model` - Model name (use Perplexity model names like `sonar-pro`)
* `messages` - Chat messages array
* `max_tokens` - Maximum tokens in response
* `stream` - Enable streaming responses

**Agentic Research API:**

* `model` - Model name (use 3rd party models like `openai/gpt-5.2`)
* `input` - Input text or message array
* `instructions` - System instructions
* `max_output_tokens` - Maximum tokens in response
* `stream` - Enable streaming responses
* `tools` - Array of tools including `web_search`

### Perplexity-Specific Parameters

**Chat Completions API:**

* `search_domain_filter` - Limit or exclude specific domains
* `search_recency_filter` - Filter by content recency
* `return_images` - Include image URLs in response
* `return_related_questions` - Include related questions
* `search_mode` - "web" (default) or "academic" mode selector

**Agentic Research API:**

* `preset` - Preset name (use Perplexity presets like `pro-search`)
* `tools[].filters` - Search filters within web\_search tool
* `tools[].user_location` - User location for localized results

<Info>
  See [Chat Completions API Reference](/api-reference/chat-completions-post) and [Agentic Research API Reference](/api-reference/responses-post) for complete parameter details.
</Info>

## Response Structure

### Chat Completions API

Perplexity responses match OpenAI's format exactly:

* `choices[0].message.content` - The AI-generated response
* `model` - The model name used
* `usage` - Token consumption details
* `id`, `created`, `object` - Standard response metadata
* `search_results` - Array of web sources (Perplexity-specific)
* `citations` - Array of citation URLs (Perplexity-specific)

### Agentic Research API

Perplexity Agentic Research API matches OpenAI's Agentic Research API format:

* `output` - Structured output array containing messages with `content[].text`
* `model` - The model name used
* `usage` - Token consumption details
* `id`, `created_at`, `status` - Response metadata

## Best Practices

<Steps>
  <Step title="Use the correct base URL">
    Always use `https://api.perplexity.ai/v2` (with `/v2`) for both APIs.

    ```python theme={null}
    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"  # Correct
    )
    ```
  </Step>

  <Step title="Choose the right API">
    * **Chat Completions API**: Best for web-grounded conversations with built-in search
    * **Agentic Research API**: Best for structured outputs, third-party models, and tool use

    ```python theme={null}
    # Chat Completions - web search built-in
    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Latest AI news"}]
    )

    # Responses - explicit tool control
    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="Latest AI news",
        tools=[{"type": "web_search"}]
    )
    ```
  </Step>

  <Step title="Handle errors gracefully">
    Use the OpenAI SDK's error handling:

    ```python theme={null}
    from openai import OpenAI, APIError, RateLimitError

    try:
        completion = client.chat.completions.create(...)
    except RateLimitError:
        print("Rate limit exceeded, please retry later")
    except APIError as e:
        print(f"API error: {e.message}")
    ```
  </Step>

  <Step title="Use streaming for better UX">
    Stream responses for real-time user experience:

    ```python theme={null}
    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Long query..."}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    ```
  </Step>
</Steps>

## Recommended: Perplexity SDK

We recommend using Perplexity's native SDKs for the best developer experience:

* **Cleaner preset syntax** - Use `preset="pro-search"` directly instead of `extra_body={"preset": "pro-search"}`
* **Type safety** - Full TypeScript/Python type definitions for all parameters
* **Enhanced features** - Direct access to all Perplexity-specific features
* **Better error messages** - Perplexity-specific error handling
* **Simpler setup** - No need to configure base URLs

See the [Perplexity SDK Guide](/docs/sdk/overview) for details.

## Next Steps

<CardGroup>
  <Card title="Chat Completions Quickstart" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Get started with Chat Completions API using OpenAI SDKs.
  </Card>

  <Card title="Responses Quickstart" icon="reply" href="/docs/grounded-llm/responses/quickstart">
    Get started with Agentic Research API using OpenAI SDKs.
  </Card>

  <Card title="Prompt Guide" icon="book" href="/docs/grounded-llm/prompting/prompt-guide">
    Learn best practices for prompting both APIs.
  </Card>

  <Card title="API Reference" icon="code" href="/docs/api-reference/chat-completions-post">
    View complete API documentation for both endpoints.
  </Card>
</CardGroup>

## Migrating to the Perplexity SDK

Switch to the Perplexity SDK for enhanced features and cleaner syntax. With the Perplexity SDK, you can use presets directly without `extra_body` and get full type safety:

<Steps>
  <Step title="Install the Perplexity SDK">
    <Tabs>
      <Tab title="Python">
        ```bash theme={null}
        pip install perplexityai
        ```
      </Tab>

      <Tab title="TypeScript">
        ```bash theme={null}
        npm install @perplexity-ai/perplexity_ai
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Update the import and client">
    <Tabs>
      <Tab title="Python">
        ```python theme={null}
        # Before (OpenAI SDK)
        from openai import OpenAI
        client = OpenAI(
            api_key="pplx-...",
            base_url="https://api.perplexity.ai/v2"
        )

        # After (Perplexity SDK)
        from perplexity import Perplexity
        client = Perplexity(api_key="pplx-...")
        # Or just: client = Perplexity() if PERPLEXITY_API_KEY env var is set
        ```
      </Tab>

      <Tab title="TypeScript">
        ```typescript theme={null}
        // Before (OpenAI SDK)
        import OpenAI from 'openai';
        const client = new OpenAI({
          apiKey: "pplx-...",
          baseURL: "https://api.perplexity.ai/v2"
        });

        // After (Perplexity SDK)
        import Perplexity from '@perplexity-ai/perplexity_ai';
        const client = new Perplexity({ apiKey: "pplx-..." });
        // Or just: const client = new Perplexity() if PERPLEXITY_API_KEY env var is set
        ```
      </Tab>
    </Tabs>

    <Info>
      **No base URL needed** - The Perplexity SDK automatically uses the correct endpoint.
    </Info>
  </Step>

  <Step title="Update the API calls">
    The API calls are very similar:

    <Tabs>
      <Tab title="Python">
        ```python theme={null}
        # Chat Completions API - same interface
        completion = client.chat.completions.create(
            model="sonar-pro",
            messages=[{"role": "user", "content": "Hello!"}]
        )

        # Agentic Research API - same interface
        response = client.responses.create(
            model="openai/gpt-5-mini",
            input="Hello!"
        )
        ```
      </Tab>

      <Tab title="TypeScript">
        ```typescript theme={null}
        // Chat Completions API - same interface
        const completion = await client.chat.completions.create({
          model: "pro-search",
          messages: [{ role: "user", content: "Hello!" }]
        });

        // Agentic Research API - same interface
        const response = await client.responses.create({
          model: "openai/gpt-5-mini",
          input: "Hello!"
        });
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Use presets with cleaner syntax">
    The Perplexity SDK supports presets with cleaner syntax compared to OpenAI SDK:

    <Tabs>
      <Tab title="Python">
        ```python theme={null}
        # Before (OpenAI SDK) - extra_body required
        response = client.responses.create(
            input="What are the latest developments in AI?",
            extra_body={"preset": "pro-search"}
        )

        # After (Perplexity SDK) - direct parameter
        response = client.responses.create(
            preset="pro-search",
            input="What are the latest developments in AI?"
        )
        ```
      </Tab>

      <Tab title="TypeScript">
        ```typescript theme={null}
        // Before (OpenAI SDK) - type casting required
        const response = await client.responses.create({
          input: "What are the latest developments in AI?",
          preset: "pro-search"
        } as any);

        // After (Perplexity SDK) - fully typed
        const response = await client.responses.create({
          preset: "pro-search",
          input: "What are the latest developments in AI?"
        });
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>


# Streaming Responses
Source: https://docs.perplexity.ai/docs/grounded-llm/output-control/streaming-responses

Learn how to stream real-time responses using Perplexity's SDKs and APIs

## Overview

Streaming allows you to receive partial responses from the Perplexity API as they are generated, rather than waiting for the complete response. This is particularly useful for:

* **Real-time user experiences** - Display responses as they're generated
* **Long responses** - Start showing content immediately for lengthy analyses
* **Interactive applications** - Provide immediate feedback to users

<Info>
  Streaming is supported across all Perplexity models and both Chat Completions and Agentic Research APIs.
</Info>

## Quick Start

The easiest way to get started is with the Perplexity SDKs, which handle all the streaming parsing automatically.

To enable streaming, set `stream=True` (Python) or `stream: true` (TypeScript) when creating completions:

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python SDK theme={null}
      from perplexity import Perplexity

      # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      client = Perplexity()

      # Create streaming response
      stream = client.responses.create(
          preset="fast-search",
          input="What is the latest in AI research?",
          stream=True
      )

      # Process streaming response
      for event in stream:
          if event.type == "response.output_text.delta":
              print(event.delta, end="")
      ```

      ```typescript TypeScript SDK theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      // Create streaming response
      const stream = await client.responses.create({
        preset: "fast-search",
        input: "What is the latest in AI research?",
        stream: true
      });

      // Process streaming response
      for await (const event of stream) {
        if (event.type === "response.output_text.delta") {
          process.stdout.write(event.delta);
        }
      }
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/v1/responses" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "fast-search",
          "input": "What is the latest in AI research?",
          "stream": true
        }'
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python SDK theme={null}
      from perplexity import Perplexity

      # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      client = Perplexity()

      # Create streaming completion
      stream = client.chat.completions.create(
          model="sonar",
          messages=[{"role": "user", "content": "What is the latest in AI research?"}],
          stream=True
      )

      # Process streaming response
      for chunk in stream:
          if chunk.choices[0].delta.content:
              print(chunk.choices[0].delta.content, end="")
      ```

      ```typescript TypeScript SDK theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      // Create streaming completion
      const stream = await client.chat.completions.create({
        model: "sonar",
        messages: [{ role: "user", content: "What is the latest in AI research?" }],
        stream: true
      });

      // Process streaming response
      for await (const chunk of stream) {
        if (chunk.choices[0]?.delta?.content) {
          process.stdout.write(chunk.choices[0].delta.content);
        }
      }
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/chat/completions" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar",
          "messages": [{"role": "user", "content": "What is the latest in AI research?"}],
          "stream": true
        }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Search Results and Metadata During Streaming

<Info>
  Search results and metadata are delivered in the **final chunk(s)** of a streaming response, not progressively during the stream.
</Info>

### How Metadata Works with Streaming

When streaming, you receive:

1. **Content chunks** which arrive progressively in real-time
2. **Search results** (delivered in the final chunk(s))
3. **Usage stats** and other metadata

### Collecting Metadata During Streaming

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    from perplexity import Perplexity

    def stream_with_metadata():
        client = Perplexity()
        
        stream = client.chat.completions.create(
            model="sonar",
            messages=[{"role": "user", "content": "Explain quantum computing"}],
            stream=True
        )
        
        content = ""
        search_results = []
        usage_info = None
        
        for chunk in stream:
            # Process content
            if chunk.choices[0].delta.content:
                content_piece = chunk.choices[0].delta.content
                content += content_piece
                print(content_piece, end='', flush=True)
            
            # Collect metadata from final chunks
            if hasattr(chunk, 'search_results') and chunk.search_results:
                search_results = chunk.search_results
                
            if hasattr(chunk, 'usage') and chunk.usage:
                usage_info = chunk.usage
                
            # Check if streaming is complete
            if chunk.choices[0].finish_reason:
                print(f"\n\nSearch Results: {search_results}")
                print(f"Usage: {usage_info}")
        
        return content, search_results, usage_info

    stream_with_metadata()
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript theme={null}
    async function streamWithMetadata(query: string) {
      const client = new Perplexity();
      
      const stream = await client.chat.completions.create({
        model: "sonar",
        messages: [{ role: "user", content: query }],
        stream: true
      });

      let content = "";
      let searchResults: any[] = [];
      let usage: any = undefined;

      for await (const chunk of stream) {
        // Process content
        if (chunk.choices[0]?.delta?.content) {
          const contentPiece = chunk.choices[0].delta.content;
          content += contentPiece;
          process.stdout.write(contentPiece);
        }

        // Collect metadata from final chunks
        if (chunk.search_results) {
          searchResults = chunk.search_results;
        }

        if (chunk.usage) {
          usage = chunk.usage;
        }

        // Check if streaming is complete
        if (chunk.choices[0]?.finish_reason) {
          console.log(`\n\nSearch Results:`, searchResults);
          console.log(`Usage:`, usage);
        }
      }

      return { content, searchResults, usage };
    }

    // Usage
    const result = await streamWithMetadata("Explain quantum computing");
    ```
  </Tab>

  <Tab title="Raw HTTP">
    ```python theme={null}
    import requests
    import json

    def stream_with_requests_metadata():
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar",
            "messages": [{"role": "user", "content": "Explain quantum computing"}],
            "stream": True
        }
        
        response = requests.post(url, headers=headers, json=payload, stream=True)
        
        content = ""
        metadata = {}
        
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    data_str = line[6:]
                    if data_str == '[DONE]':
                        break
                    try:
                        chunk = json.loads(data_str)
                        
                        # Process content
                        if 'choices' in chunk and chunk['choices'][0]['delta'].get('content'):
                            content_piece = chunk['choices'][0]['delta']['content']
                            content += content_piece
                            print(content_piece, end='', flush=True)
                        
                        # Collect metadata
                        for key in ['search_results', 'usage']:
                            if key in chunk:
                                metadata[key] = chunk[key]
                                
                        # Check if streaming is complete
                        if chunk['choices'][0].get('finish_reason'):
                            print(f"\n\nMetadata: {metadata}")
                            
                    except json.JSONDecodeError:
                        continue
        
        return content, metadata

    stream_with_requests_metadata()
    ```
  </Tab>
</Tabs>

## Error Handling

Proper error handling is important to ensure your application can recover from errors and provide a good user experience.

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    import perplexity
    from perplexity import Perplexity

    client = Perplexity()

    try:
        stream = client.chat.completions.create(
            model="sonar-pro",
            messages=[
                {"role": "user", "content": "Explain machine learning concepts"}
            ],
            stream=True
        )
        
        content = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content_chunk = chunk.choices[0].delta.content
                content += content_chunk
                print(content_chunk, end="")
                
    except perplexity.APIConnectionError as e:
        print(f"Network connection failed: {e}")
    except perplexity.RateLimitError as e:
        print(f"Rate limit exceeded, please retry later: {e}")
    except perplexity.APIStatusError as e:
        print(f"API error {e.status_code}: {e.response}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript theme={null}
    import Perplexity from '@perplexity-ai/perplexity_ai';

    const client = new Perplexity();

    try {
      const stream = await client.chat.completions.create({
        model: "sonar-pro",
        messages: [
          { role: "user", content: "Explain machine learning concepts" }
        ],
        stream: true
      });
      
      for await (const chunk of stream) {
        if (chunk.choices[0]?.delta?.content) {
          process.stdout.write(chunk.choices[0].delta.content);
        }
      }
    } catch (error) {
      if (error instanceof Perplexity.APIConnectionError) {
        console.error("Network connection failed:", error.cause);
      } else if (error instanceof Perplexity.RateLimitError) {
        console.error("Rate limit exceeded, please retry later");
      } else if (error instanceof Perplexity.APIError) {
        console.error(`API error ${error.status}: ${error.message}`);
      } else {
        console.error("Unexpected error:", error);
      }
    }
    ```
  </Tab>

  <Tab title="Raw HTTP">
    ```python theme={null}
    import requests
    import time
    import json

    def stream_with_retry(max_retries=3):
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        data = {
            "model": "sonar-pro",
            "messages": [
                {"role": "system", "content": "Be precise and concise."},
                {"role": "user", "content": "Explain machine learning concepts"}
            ],
            "stream": True,
            "max_tokens": 1000
        }

        for attempt in range(max_retries):
            try:
                with requests.post(url, headers=headers, json=data, stream=True, timeout=300) as resp:
                    resp.raise_for_status()
                    for line in resp.iter_lines(decode_unicode=True):
                        if line and line.startswith("data: "):
                            chunk_data = line[len("data: "):]
                            if chunk_data == "[DONE]":
                                break
                            try:
                                chunk = json.loads(chunk_data)
                                content = chunk["choices"][0].get("delta", {}).get("content")
                                if content:
                                    print(content, end="", flush=True)
                            except json.JSONDecodeError:
                                continue
                break
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    raise

    stream_with_retry()
    ```
  </Tab>
</Tabs>

## Proper SSE Parsing

For production use, you should properly parse Server-Sent Events (SSE) format:

<Tabs>
  <Tab title="Python with SSE Library">
    ```python theme={null}
    # pip install sseclient-py
    import sseclient
    import requests
    import json

    def stream_with_proper_sse():
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar",
            "messages": [{"role": "user", "content": "Explain quantum computing"}],
            "stream": True
        }
        
        response = requests.post(url, headers=headers, json=payload, stream=True)
        client = sseclient.SSEClient(response)
        
        for event in client.events():
            if event.data == '[DONE]':
                break
            try:
                chunk_data = json.loads(event.data)
                content = chunk_data['choices'][0]['delta'].get('content', '')
                if content:
                    print(content, end='')
            except json.JSONDecodeError:
                continue

    stream_with_proper_sse()
    ```
  </Tab>

  <Tab title="JavaScript with EventSource">
    ```javascript theme={null}
    // For browser environments
    function streamInBrowser() {
      const eventSource = new EventSource('/api/stream'); // Your server endpoint
      
      eventSource.onmessage = function(event) {
        if (event.data === '[DONE]') {
          eventSource.close();
          return;
        }
        
        try {
          const chunk = JSON.parse(event.data);
          const content = chunk.choices[0]?.delta?.content;
          if (content) {
            document.getElementById('output').innerHTML += content;
          }
        } catch (e) {
          console.error('Error parsing chunk:', e);
        }
      };
      
      eventSource.onerror = function(event) {
        console.error('EventSource failed:', event);
        eventSource.close();
      };
    }
    ```
  </Tab>

  <Tab title="Manual SSE Parsing">
    ```python theme={null}
    import requests
    import json

    def stream_with_manual_parsing():
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar",
            "messages": [{"role": "user", "content": "Explain quantum computing"}],
            "stream": True
        }
        
        response = requests.post(url, headers=headers, json=payload, stream=True)
        
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    data_str = line[6:]  # Remove 'data: ' prefix
                    if data_str == '[DONE]':
                        break
                    try:
                        chunk_data = json.loads(data_str)
                        content = chunk_data['choices'][0]['delta'].get('content', '')
                        if content:
                            print(content, end='')
                    except json.JSONDecodeError:
                        continue

    stream_with_manual_parsing()
    ```
  </Tab>
</Tabs>

## Advanced Streaming Patterns

### Buffered Streaming

For applications that need to process chunks in batches:

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    from perplexity import Perplexity
    import time

    def buffered_streaming(buffer_size=50, flush_interval=1.0):
        client = Perplexity()
        
        stream = client.chat.completions.create(
            model="sonar",
            messages=[{"role": "user", "content": "Write a detailed explanation of machine learning"}],
            stream=True
        )
        
        buffer = ""
        last_flush = time.time()
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                buffer += chunk.choices[0].delta.content
                
                # Flush buffer if it's full or enough time has passed
                if len(buffer) >= buffer_size or (time.time() - last_flush) >= flush_interval:
                    print(buffer, end='', flush=True)
                    buffer = ""
                    last_flush = time.time()
        
        # Flush remaining buffer
        if buffer:
            print(buffer, end='', flush=True)

    buffered_streaming()
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript theme={null}
    async function bufferedStreaming(bufferSize: number = 50, flushInterval: number = 1000) {
      const client = new Perplexity();
      
      const stream = await client.chat.completions.create({
        model: "sonar",
        messages: [{ role: "user", content: "Write a detailed explanation of machine learning" }],
        stream: true
      });
      
      let buffer = "";
      let lastFlush = Date.now();
      
      for await (const chunk of stream) {
        if (chunk.choices[0]?.delta?.content) {
          buffer += chunk.choices[0].delta.content;
          
          // Flush buffer if it's full or enough time has passed
          if (buffer.length >= bufferSize || (Date.now() - lastFlush) >= flushInterval) {
            process.stdout.write(buffer);
            buffer = "";
            lastFlush = Date.now();
          }
        }
      }
      
      // Flush remaining buffer
      if (buffer) {
        process.stdout.write(buffer);
      }
    }

    bufferedStreaming();
    ```
  </Tab>
</Tabs>

### Stream Processing with Callbacks

For applications that need to process chunks with custom logic:

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    from perplexity import Perplexity
    from typing import Callable, Optional

    def stream_with_callbacks(
        query: str,
        on_content: Optional[Callable[[str], None]] = None,
        on_search_results: Optional[Callable[[list], None]] = None,
        on_complete: Optional[Callable[[str, dict], None]] = None
    ):
        client = Perplexity()
        
        stream = client.chat.completions.create(
            model="sonar",
            messages=[{"role": "user", "content": query}],
            stream=True
        )
        
        full_content = ""
        metadata = {}
        
        for chunk in stream:
            # Handle content chunks
            if chunk.choices[0].delta.content:
                content_piece = chunk.choices[0].delta.content
                full_content += content_piece
                if on_content:
                    on_content(content_piece)
            
            # Handle search results
            if hasattr(chunk, 'search_results') and chunk.search_results:
                metadata['search_results'] = chunk.search_results
                if on_search_results:
                    on_search_results(chunk.search_results)
            
            # Handle other metadata
            if hasattr(chunk, 'usage') and chunk.usage:
                metadata['usage'] = chunk.usage
            
            # Handle completion
            if chunk.choices[0].finish_reason:
                if on_complete:
                    on_complete(full_content, metadata)
        
        return full_content, metadata

    # Usage example
    def print_content(content: str):
        print(content, end='', flush=True)

    def handle_search_results(results: list):
        print(f"\n[Found {len(results)} sources]", end='')

    def handle_completion(content: str, metadata: dict):
        print(f"\n\nCompleted. Total length: {len(content)} characters")
        if 'usage' in metadata:
            print(f"Token usage: {metadata['usage']}")

    stream_with_callbacks(
        "Explain the latest developments in renewable energy",
        on_content=print_content,
        on_search_results=handle_search_results,
        on_complete=handle_completion
    )
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript theme={null}
    interface StreamCallbacks {
      onContent?: (content: string) => void;
      onSearchResults?: (results: any[]) => void;
      onComplete?: (content: string, metadata: any) => void;
    }

    async function streamWithCallbacks(query: string, callbacks: StreamCallbacks = {}) {
      const client = new Perplexity();
      
      const stream = await client.chat.completions.create({
        model: "sonar",
        messages: [{ role: "user", content: query }],
        stream: true
      });
      
      let fullContent = "";
      const metadata: any = {};
      
      for await (const chunk of stream) {
        // Handle content chunks
        if (chunk.choices[0]?.delta?.content) {
          const contentPiece = chunk.choices[0].delta.content;
          fullContent += contentPiece;
          callbacks.onContent?.(contentPiece);
        }
        
        // Handle search results
        if (chunk.search_results) {
          metadata.search_results = chunk.search_results;
          callbacks.onSearchResults?.(chunk.search_results);
        }
        
        // Handle other metadata
        if (chunk.usage) {
          metadata.usage = chunk.usage;
        }
        
        // Handle completion
        if (chunk.choices[0]?.finish_reason) {
          callbacks.onComplete?.(fullContent, metadata);
        }
      }
      
      return { content: fullContent, metadata };
    }

    // Usage example
    const result = await streamWithCallbacks(
      "Explain the latest developments in renewable energy",
      {
        onContent: (content) => process.stdout.write(content),
        onSearchResults: (results) => process.stdout.write(`\n[Found ${results.length} sources]`),
        onComplete: (content, metadata) => {
          console.log(`\n\nCompleted. Total length: ${content.length} characters`);
          if (metadata.usage) {
            console.log(`Token usage:`, metadata.usage);
          }
        }
      }
    );
    ```
  </Tab>
</Tabs>

## Best Practices

<Steps>
  <Step title="Handle network interruptions">
    Implement reconnection logic for robust streaming applications.

    <Tabs>
      <Tab title="Python SDK">
        ```python theme={null}
        import time
        import random
        from perplexity import Perplexity
        import perplexity

        def robust_streaming(query: str, max_retries: int = 3):
            client = Perplexity()
            
            for attempt in range(max_retries):
                try:
                    stream = client.chat.completions.create(
                        model="sonar",
                        messages=[{"role": "user", "content": query}],
                        stream=True
                    )
                    
                    for chunk in stream:
                        if chunk.choices[0].delta.content:
                            print(chunk.choices[0].delta.content, end='', flush=True)
                    
                    return  # Success, exit retry loop
                    
                except (perplexity.APIConnectionError, perplexity.APITimeoutError) as e:
                    if attempt < max_retries - 1:
                        delay = (2 ** attempt) + random.uniform(0, 1)
                        print(f"\nConnection error, retrying in {delay:.1f}s...")
                        time.sleep(delay)
                    else:
                        print(f"\nFailed after {max_retries} attempts: {e}")
                        raise

        robust_streaming("Explain quantum computing")
        ```
      </Tab>

      <Tab title="TypeScript SDK">
        ```typescript theme={null}
        async function robustStreaming(query: string, maxRetries: number = 3) {
          const client = new Perplexity();
          
          for (let attempt = 0; attempt < maxRetries; attempt++) {
            try {
              const stream = await client.chat.completions.create({
                model: "sonar",
                messages: [{ role: "user", content: query }],
                stream: true
              });
              
              for await (const chunk of stream) {
                if (chunk.choices[0]?.delta?.content) {
                  process.stdout.write(chunk.choices[0].delta.content);
                }
              }
              
              return; // Success, exit retry loop
              
            } catch (error) {
              if (error instanceof Perplexity.APIConnectionError && attempt < maxRetries - 1) {
                const delay = Math.pow(2, attempt) * 1000 + Math.random() * 1000;
                console.log(`\nConnection error, retrying in ${delay / 1000:.1f}s...`);
                await new Promise(resolve => setTimeout(resolve, delay));
              } else {
                console.error(`\nFailed after ${maxRetries} attempts:`, error);
                throw error;
              }
            }
          }
        }

        robustStreaming("Explain quantum computing");
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Implement proper buffering">
    Use appropriate buffering strategies for your application's needs.

    ```python theme={null}
    # For real-time chat applications
    buffer_size = 1  # Character-by-character for immediate display

    # For document processing
    buffer_size = 100  # Larger chunks for efficiency

    # For API responses
    buffer_size = 500  # Balance between responsiveness and efficiency
    ```
  </Step>

  <Step title="Handle metadata appropriately">
    Remember that search results and metadata arrive at the end of the stream.

    ```python theme={null}
    # Don't expect search results until the stream is complete
    if chunk.choices[0].finish_reason == "stop":
        # Now search results and usage info are available
        process_search_results(chunk.search_results)
        log_usage_stats(chunk.usage)
    ```
  </Step>

  <Step title="Optimize for your use case">
    Choose streaming parameters based on your application requirements.

    <Tabs>
      <Tab title="Real-time Chat">
        ```python theme={null}
        # Optimize for immediate response
        stream = client.chat.completions.create(
            model="sonar",
            messages=messages,
            stream=True,
            max_tokens=1000  # Reasonable limit
        )
        ```
      </Tab>

      <Tab title="Document Generation">
        ```python theme={null}
        # Optimize for quality and completeness
        stream = client.chat.completions.create(
            model="sonar-pro",
            messages=messages,
            stream=True,
            max_tokens=4000  # Longer responses
        )
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

<Warning>
  **Important**: If you need search results immediately for your user interface, consider using non-streaming requests for use cases where search result display is critical to the real-time user experience.
</Warning>

## Resources

* [The Perplexity SDK Guide](/docs/sdk/overview) - The Perplexity SDK guide
* [Chat Completions Guide](/docs/grounded-llm/chat-completions/quickstart) - Complete chat completions guide
* [API Reference - Chat Completions](/api-reference/chat-completions-post) - Complete API documentation


# Structured Outputs Guide
Source: https://docs.perplexity.ai/docs/grounded-llm/output-control/structured-outputs



## Overview

Structured outputs enable you to enforce specific response formats from Perplexity's models, ensuring consistent, machine-readable data that can be directly integrated into your applications without manual parsing.

We currently support **JSON Schema** structured outputs. To enable structured outputs, add a `response_format` field to your request with the following structure:

```json theme={null}
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "your_schema_name",
      "schema": { /* your JSON schema object */ }
    }
  }
}
```

The `name` field is required and must be 1-64 alphanumeric characters. The schema should be a valid JSON schema object. LLM responses will match the specified format unless the output exceeds `max_tokens`.

<Tip>
  **Improve Schema Compliance**: Give the LLM some hints about the output format in your prompts to improve adherence to the structured format.

  For example, include phrases like "Please return the data as a JSON object with the following structure..." or "Extract the information and format it as specified in the schema."
</Tip>

<Info>
  The first request with a new JSON Schema expects to incur delay on the first token. Typically, it takes 10 to 30 seconds to prepare the new schema, and may result in timeout errors. Once the schema has been prepared, the subsequent requests will not see such delay.
</Info>

## Examples

### 1. Financial Analysis

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity
      from typing import List, Optional
      from pydantic import BaseModel

      class FinancialMetrics(BaseModel):
          company: str
          quarter: str
          revenue: float
          net_income: float
          eps: float
          revenue_growth_yoy: Optional[float] = None
          key_highlights: Optional[List[str]] = None

      client = Perplexity()

      response = client.responses.create(
          preset="pro-search",
          input="Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics.",
          response_format={
              "type": "json_schema",
              "json_schema": {
                  "name": "financial_metrics",
                  "schema": FinancialMetrics.model_json_schema()
              }
          }
      )


      metrics = FinancialMetrics.model_validate_json(response.output_text)
      print(f"Revenue: ${metrics.revenue}B")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      interface FinancialMetrics {
        company: string;
        quarter: string;
        revenue: number;
        net_income: number;
        eps: number;
        revenue_growth_yoy?: number;
        key_highlights?: string[];
      }

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: 'pro-search',
        input: 'Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics.',
        response_format: {
          type: 'json_schema',
          json_schema: {
            name: 'financial_metrics',
            schema: {
              type: 'object',
              properties: {
                company: { type: 'string' },
                quarter: { type: 'string' },
                revenue: { type: 'number' },
                net_income: { type: 'number' },
                eps: { type: 'number' },
                revenue_growth_yoy: { type: 'number' },
                key_highlights: {
                  type: 'array',
                  items: { type: 'string' }
                }
              },
              required: ['company', 'quarter', 'revenue', 'net_income', 'eps']
            }
          }
        }
      });

      const metrics: FinancialMetrics = JSON.parse(response.output_text);
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/v1/responses" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "pro-search",
          "input": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics.",
          "response_format": {
            "type": "json_schema",
            "json_schema": {
              "name": "financial_metrics",
              "schema": {
                "type": "object",
                "properties": {
                  "company": {"type": "string"},
                  "quarter": {"type": "string"},
                  "revenue": {"type": "number"},
                  "net_income": {"type": "number"},
                  "eps": {"type": "number"},
                  "revenue_growth_yoy": {"type": "number"},
                  "key_highlights": {
                    "type": "array",
                    "items": {"type": "string"}
                  }
                },
                "required": ["company", "quarter", "revenue", "net_income", "eps"]
              }
            }
          }
        }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity
      from typing import List, Optional
      from pydantic import BaseModel

      class FinancialMetrics(BaseModel):
          company: str
          quarter: str
          revenue: float
          net_income: float
          eps: float
          revenue_growth_yoy: Optional[float] = None
          key_highlights: Optional[List[str]] = None

      client = Perplexity()

      completion = client.chat.completions.create(
          model="sonar-pro",
          messages=[
              {
                  "role": "user",
                  "content": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics."
              }
          ],
          response_format={
              "type": "json_schema",
              "json_schema": {
                  "schema": FinancialMetrics.model_json_schema()
              }
          }
      )

      metrics = FinancialMetrics.model_validate_json(completion.choices[0].message.content)
      print(f"Revenue: ${metrics.revenue}B")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      interface FinancialMetrics {
        company: string;
        quarter: string;
        revenue: number;
        net_income: number;
        eps: number;
        revenue_growth_yoy?: number;
        key_highlights?: string[];
      }

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        model: 'sonar-pro',
        messages: [
          {
            role: 'user',
            content: 'Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics.'
          }
        ],
        response_format: {
          type: 'json_schema',
          json_schema: {
            schema: {
              type: 'object',
              properties: {
                company: { type: 'string' },
                quarter: { type: 'string' },
                revenue: { type: 'number' },
                net_income: { type: 'number' },
                eps: { type: 'number' },
                revenue_growth_yoy: { type: 'number' },
                key_highlights: {
                  type: 'array',
                  items: { type: 'string' }
                }
              },
              required: ['company', 'quarter', 'revenue', 'net_income', 'eps']
            }
          }
        }
      });

      const metrics: FinancialMetrics = JSON.parse(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/chat/completions" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar-pro",
          "messages": [
            {
              "role": "user", 
              "content": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics."
            }
          ],
          "response_format": {
            "type": "json_schema",
            "json_schema": {
              "schema": {
                "type": "object",
                "properties": {
                  "company": {"type": "string"},
                  "quarter": {"type": "string"},
                  "revenue": {"type": "number"},
                  "net_income": {"type": "number"},
                  "eps": {"type": "number"},
                  "revenue_growth_yoy": {"type": "number"},
                  "key_highlights": {
                    "type": "array",
                    "items": {"type": "string"}
                  }
                },
                "required": ["company", "quarter", "revenue", "net_income", "eps"]
              }
            }
          }
        }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### 2. Extract Contact Information

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity
      from pydantic import BaseModel

      class ContactInfo(BaseModel):
          email: str

      client = Perplexity()

      response = client.responses.create(
          preset="fast-search",
          input="Find the direct email address for the investor relations contact at Tesla Inc.",
          response_format={
              "type": "json_schema",
              "json_schema": {
                  "name": "contact_info",
                  "schema": ContactInfo.model_json_schema()
              }
          }
      )


      contact = ContactInfo.model_validate_json(response.output_text)
      print(f"Investor Relations Email: {contact.email}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      interface ContactInfo {
        email: string;
      }

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: 'fast-search',
        input: 'Find the direct email address for the investor relations contact at Tesla Inc.',
        response_format: {
          type: 'json_schema',
          json_schema: {
            name: 'contact_info',
            schema: {
              type: 'object',
              properties: {
                email: { type: 'string' }
              },
              required: ['email']
            }
          }
        }
      });

      const contact: ContactInfo = JSON.parse(response.output_text);
      console.log(`Investor Relations Email: ${contact.email}`);
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/v1/responses" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "fast-search",
          "input": "Find the direct email address for the investor relations contact at Tesla Inc.",
          "response_format": {
            "type": "json_schema",
            "json_schema": {
              "name": "contact_info",
              "schema": {
                "type": "object",
                "properties": {
                  "email": {"type": "string"}
                },
                "required": ["email"]
              }
            }
          }
        }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity
      from pydantic import BaseModel

      class ContactInfo(BaseModel):
          email: str

      client = Perplexity()

      completion = client.chat.completions.create(
          model="sonar",
          messages=[
              {
                  "role": "user",
                  "content": "Find the direct email address for the investor relations contact at Tesla Inc."
              }
          ],
          response_format={
              "type": "json_schema",
              "json_schema": {
                  "schema": ContactInfo.model_json_schema()
              }
          }
      )

      contact = ContactInfo.model_validate_json(completion.choices[0].message.content)
      print(f"Investor Relations Email: {contact.email}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      interface ContactInfo {
        email: string;
      }

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        model: 'sonar',
        messages: [
          {
            role: 'user',
            content: 'Find the direct email address for the investor relations contact at Tesla Inc.'
          }
        ],
        response_format: {
          type: 'json_schema',
          json_schema: {
            schema: {
              type: 'object',
              properties: {
                email: { type: 'string' }
              },
              required: ['email']
            }
          }
        }
      });

      const contact: ContactInfo = JSON.parse(completion.choices[0].message.content);
      console.log(`Investor Relations Email: ${contact.email}`);
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/chat/completions" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar",
          "messages": [
            {
              "role": "user",
              "content": "Find the direct email address for the investor relations contact at Tesla Inc."
            }
          ],
          "response_format": {
            "type": "json_schema",
            "json_schema": {
              "schema": {
                "type": "object",
                "properties": {
                  "email": {"type": "string"}
                },
                "required": ["email"]
              }
            }
          }
        }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Best Practices

### Generating responses in a JSON Format

For Python users, we recommend using the Pydantic library to [generate JSON schema](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema).

### Unsupported JSON Schemas

Recursive JSON schema is not supported. As a result of that, unconstrained objects are not supported either. Here are a few examples of unsupported schemas:

```
# UNSUPPORTED!

from typing import Any

class UnconstrainedDict(BaseModel):
   unconstrained: dict[str, Any]

class RecursiveJson(BaseModel):
   value: str
   child: list["RecursiveJson"]
```

<Warning>
  **Links in JSON Responses**: Requesting links as part of a JSON response may not always work reliably and can result in hallucinations or broken links. Models may generate invalid URLs when forced to include links directly in structured outputs.

  To ensure all links are valid, use the links returned in the `citations` or `search_results` fields from the API response. Never count on the model to return valid links directly as part of the JSON response content.
</Warning>

## Perplexity's JSON Schema Implementation

Perplexity's structured outputs implementation has several key differences compared to other providers:

### Simplified Schema Definition

* **Optional naming**: Unlike other providers that require explicit schema names, Perplexity automatically handles schema naming with sensible defaults
* **Flexible strictness**: Schema validation is handled automatically without requiring manual strictness configuration
* **Streamlined syntax**: You only need to provide the core schema object without additional wrapper fields

**Other Providers:**

```json theme={null}
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "financial_data",
      "strict": true,
      "schema": { /* your schema */ }
    }
  }
}
```

**Perplexity:**

```json theme={null}
{
  "response_format": {
    "type": "json_schema", 
    "json_schema": {
      "schema": { /* your schema */ }
    }
  }
}
```

### Enhanced Error Handling

* **Clear error messages**: When schemas fail validation, you'll receive specific, actionable error messages
* **Recursion protection**: Built-in safeguards prevent infinite recursion in complex nested schemas
* **Constraint validation**: Automatic detection and clear messaging for unsupported features like unconstrained objects

### Schema Compatibility

While Perplexity supports standard JSON Schema syntax, some advanced features may not be available:

* Recursive schemas are not supported for performance and reliability reasons
* Unconstrained objects (like `dict[str, Any]`) are automatically detected and rejected
* Complex reference patterns may require simplification

This approach prioritizes reliability and performance while maintaining compatibility with most common JSON Schema use cases.

## Structured Outputs for Reasoning Models

When using structured outputs with reasoning models like `sonar-reasoning-pro`, the response will include a `<think>` section containing reasoning tokens, immediately followed by the structured output. The `response_format` parameter does not remove these reasoning tokens from the output, so the final response will need to be parsed manually.

**Sample Response:**

```
<think>
I need to provide information about France in a structured JSON format with specific fields: country, capital, population, official_language.

For France:
- Country: France
- Capital: Paris
- Population: About 67 million (as of 2023)
- Official Language: French

Let me format this information as required.
</think>
{"country":"France","capital":"Paris","population":67750000,"official_language":"French"}
```

For a reusable implementation to extract JSON from reasoning model outputs, see our [example utility on GitHub](https://github.com/perplexityai/api-discussion/blob/main/utils/extract_json_reasoning_models.py).


# Prompt Guide
Source: https://docs.perplexity.ai/docs/grounded-llm/prompting/prompt-guide



## System Prompt

You can use the system prompt (Chat Completions) or instructions (Agentic Research API) to provide instructions related to style, tone, and language of the response.

<Warning>
  The real-time search component of our models does not attend to the system prompt.
</Warning>

**Example of a system prompt**

```
You are a helpful AI assistant.

Rules:
1. Provide only the final answer. It is important that you do not include any explanation on the steps below.
2. Do not show the intermediate steps information.

Steps:
1. Decide if the answer should be a brief sentence or a list of suggestions.
2. If it is a list of suggestions, first, write a brief and natural introduction based on the original query.
3. Followed by a list of suggestions, each suggestion should be split by two newlines.
```

## User Prompt

You should use the user prompt (Chat Completions) or input (Agentic Research API) to pass in the actual query for which you need an answer. The user prompt/input will be used to kick off a real-time web search to make sure the answer has the latest and the most relevant information needed.

**Example of a user prompt**

```
What are the best sushi restaurants in the world currently?
```

## API Examples

<Tabs>
  <Tab title="Agentic Research API">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    response = client.responses.create(
        preset="pro-search",
        input="What are the best sushi restaurants in the world currently?",
        instructions="You are a helpful AI assistant. Provide concise, well-researched answers."
    )


    print(response.output_text)
            break
    ```
  </Tab>

  <Tab title="Chat Completions API">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Provide concise, well-researched answers."
            },
            {
                "role": "user",
                "content": "What are the best sushi restaurants in the world currently?"
            }
        ]
    )

    print(completion.choices[0].message.content)
    ```
  </Tab>
</Tabs>

# Web Search Models: General Prompting Guidelines

Our web search-powered models combine the capabilities of LLMs with real-time web searches. Understanding how they differ from traditional LLMs will help you craft more effective prompts.

## Best Practices for Prompting Web Search Models

<CardGroup>
  <Card title="Be Specific and Contextual">
    Unlike traditional LLMs, our web search models require specificity to retrieve relevant search results. Adding just 2-3 extra words of context can dramatically improve performance.

    **Good Example**: "Explain recent advances in climate prediction models for urban planning"

    **Poor Example**: "Tell me about climate models"
  </Card>

  <Card title="Avoid Few-Shot Prompting">
    While few-shot prompting works well for traditional LLMs, it confuses web search models by triggering searches for your examples rather than your actual query.

    **Good Example**: "Summarize the current research on mRNA vaccine technology"

    **Poor Example**: "Here's an example of a good summary about vaccines: \[example text]. Now summarize the current research on mRNA vaccines."
  </Card>

  <Card title="Think Like a Web Search User">
    Craft prompts with search-friendly terms that would appear on relevant web pages. Consider how experts in the field would describe the topic online.

    **Good Example**: "Compare the energy efficiency ratings of heat pumps vs. traditional HVAC systems for residential use"

    **Poor Example**: "Tell me which home heating is better"
  </Card>

  <Card title="Provide Relevant Context">
    Include critical context to guide the web search toward the most relevant content, but keep prompts concise and focused.

    **Good Example**: "Explain the impact of the 2023 EU digital markets regulations on app store competition for small developers"

    **Poor Example**: "What are the rules for app stores?"
  </Card>
</CardGroup>

## Web Search Model Pitfalls to Avoid

<CardGroup>
  <Card title="Overly Generic Questions">
    Generic prompts lead to scattered web search results and unfocused responses. Always narrow your scope.

    **Avoid**: "What's happening in AI?"

    **Instead**: "What are the three most significant commercial applications of generative AI in healthcare in the past year?"
  </Card>

  <Card title="Traditional LLM Techniques">
    Prompting strategies designed for traditional LLM often don't work well with web search models. Adapt your approach accordingly.

    **Avoid**: "Act as an expert chef and give me a recipe for sourdough bread. Start by explaining the history of sourdough, then list ingredients, then..."

    **Instead**: "What's a reliable sourdough bread recipe for beginners? Include ingredients and step-by-step instructions."
  </Card>

  <Card title="Complex Multi-Part Requests">
    Complex prompts with multiple unrelated questions can confuse the search component. Focus on one topic per query.

    **Avoid**: "Explain quantum computing, and also tell me about regenerative agriculture, and provide stock market predictions."

    **Instead**: "Explain quantum computing principles that might impact cryptography in the next decade."
  </Card>

  <Card title="Assuming Search Intent">
    Don't assume the model will search for what you intended without specific direction. Be explicit about exactly what information you need.

    **Avoid**: "Tell me about the latest developments."

    **Instead**: "What are the latest developments in offshore wind energy technology announced in the past 6 months?"
  </Card>
</CardGroup>

## Handling URLs and Source Information

<Warning>
  **Never ask for URLs or source links in your prompts.** The generative model cannot see the actual URLs from the web search, which means any URLs it provides in the response text are likely to be hallucinated and incorrect.
</Warning>

### The Right Way to Access Sources

URLs and source information are automatically returned in the `search_results` field of the API response. This field contains accurate information about the sources used, including:

* `title`: The title of the source page
* `url`: The actual URL of the source
* `date`: The publication date of the content

**Example of incorrect prompting:**

```
❌ BAD: "From the past 5 days, identify high-potential Canadian news stories... 
For each item, include:
- A clear headline  
- 1–2 sentence summary
- Include a link to a source"
```

**Example of correct prompting:**

```
✅ GOOD: "From the past 5 days, identify high-potential Canadian news stories...
For each item, include:
- A clear headline
- 1–2 sentence summary  
- Why it matters from a thought-leadership perspective"

// Then parse URLs from the search_results field in the API response
```

### Why This Matters

The web search and language generation components work differently:

1. **Web Search Component**: Finds and retrieves content from specific URLs
2. **Language Generation Component**: Processes the retrieved content but doesn't have access to the original URLs
3. **API Response**: Provides both the generated text and the accurate source URLs separately

When you ask for URLs in your prompt, the language model will attempt to generate them based on patterns it has seen, but these will not be the actual URLs that were searched. Always use the `search_results` field for accurate source information.

## Preventing Hallucination in Search Results

<Warning>
  **LLMs are designed to be "helpful" and may attempt to provide answers even when they lack sufficient information.** This can lead to hallucinated or inaccurate responses, especially when asking about sources that Sonar cannot access.
</Warning>

### Understanding the Helpfulness Problem

Large Language Models are trained to be assistive and will often try to provide an answer even when they're not confident about the information. This tendency can be problematic when:

* You request information from sources that Sonar cannot access (e.g., LinkedIn posts, private documents, paywalled content)
* The search doesn't return relevant results for your specific query
* You ask for very recent information that may not be indexed yet

### Common Scenarios That Lead to Hallucination

**Inaccessible Sources:**

```
❌ PROBLEMATIC: "What did the CEO of XYZ company post on LinkedIn yesterday about their new product launch?"
```

*Sonar may not be able to access LinkedIn content, but the model might still attempt to provide an answer based on general knowledge or patterns.*

**Overly Specific Recent Events:**

```
❌ PROBLEMATIC: "What was discussed in the closed-door meeting between Company A and Company B last week?"
```

*Private information that wouldn't be publicly searchable may still get a fabricated response.*

### How to Prevent Hallucination

**Use Explicit Instructions:**
Include clear guidance in your prompts about what to do when information isn't available:

```
✅ GOOD: "Search for recent developments in quantum computing breakthroughs. 
If you are not able to get search results or find relevant information, 
please state that clearly rather than providing speculative information."
```

**Set Clear Boundaries:**

```
✅ GOOD: "Based on publicly available sources from the past week, what are the latest policy changes in Canadian healthcare? 
If no recent information is found, please indicate that no recent updates were discovered."
```

**Request Source Transparency:**

```
✅ GOOD: "Find information about Tesla's latest earnings report. 
Only provide information that you can verify from your search results, 
and clearly state if certain details are not available."
```

### Best Practices for Reliable Results

<CardGroup>
  <Card title="Be Explicit About Limitations">
    Always instruct the model to acknowledge when it cannot find information rather than guessing.

    **Example**: "If you cannot find reliable sources for this information, please say so explicitly."
  </Card>

  <Card title="Focus on Accessible Sources">
    Stick to information that is likely to be publicly indexed and searchable.

    **Avoid**: LinkedIn posts, private company documents, closed meetings
    **Prefer**: News articles, public reports, official announcements
  </Card>

  <Card title="Use Conditional Language">
    Frame requests with conditional statements that give the model permission to say "I don't know."

    **Example**: "If available, provide details about... Otherwise, indicate what information could not be found."
  </Card>

  <Card title="Verify with Multiple Queries">
    For critical information, consider breaking complex requests into smaller, more specific queries to verify consistency.

    **Strategy**: Ask the same question in different ways and compare results for consistency.
  </Card>
</CardGroup>

## Use Built-in Search Parameters, Not Prompts

<Tip>
  **Always use Perplexity's built-in search parameters instead of trying to control search behavior through prompts.** API parameters are guaranteed to work and are much more effective than asking the model to filter results.
</Tip>

### Why Built-in Parameters Are Better

When you want to control search behavior—such as limiting sources, filtering by date, or adjusting search depth—use the API's built-in parameters rather than prompt instructions. The search component processes these parameters directly, ensuring reliable and consistent results.

### Common Mistakes: Prompt-Based Control

**❌ Ineffective - Trying to control via prompts:**

```json theme={null}
{
  "model": "sonar-pro",
  "messages": [
    {
      "role": "user", 
      "content": "Search only on Wikipedia and official government sites for information about climate change policies. Make sure to only look at sources from the past month."
    }
  ]
}
```

### Correct Approach: Use API Parameters

**✅ Effective - Using built-in parameters:**

```json theme={null}
{
  "model": "sonar-pro",
  "messages": [
    {
      "role": "user", 
      "content": "What are the latest climate change policies?"
    }
  ],
  "search_domain_filter": ["wikipedia.org"]
}
```

### Available Search Parameters

### Benefits of Using Built-in Parameters

<CardGroup>
  <Card title="Guaranteed Execution">
    Built-in parameters are processed directly by the search engine, ensuring they're applied correctly every time.
  </Card>

  <Card title="Better Performance">
    Parameters filter results before they reach the language model, leading to more focused and relevant responses.
  </Card>

  <Card title="Cleaner Prompts">
    Keep your prompts focused on what you want the model to generate, not how to search.
  </Card>

  <Card title="Consistent Results">
    API parameters provide predictable behavior across different queries and use cases.
  </Card>
</CardGroup>

### Advanced Techniques

<CardGroup>
  <Card title="Parameter Optimization">
    Adjust model parameters based on your specific needs:

    * **Search Domain Filter**: Limit results to trusted sources for research-heavy queries.
    * **Search Context Size**: Use "high" for comprehensive research questions and "low" for simple factual queries.

    Example configuration for technical documentation:

    ```json theme={null}
    {
      "search_domain_filter": ["wikipedia.org", "docs.python.org"],
      "web_search_options": {
        "search_context_size": "medium"
      }
    }
    ```
  </Card>
</CardGroup>

### Tips for Different Query Types

| Query Type              | Best Practices                                                                                                                         |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Factual Research**    | • Use specific questions  • Use search domain filters for academic sources  • Consider "high" search context size                      |
| **Creative Content**    | • Provide detailed style guidelines in system prompt  • Specify tone, voice, and audience                                              |
| **Technical Questions** | • Include relevant technical context  • Specify preferred programming language/framework  • Use domain filters for documentation sites |
| **Analysis & Insights** | • Request step-by-step reasoning  • Ask for specific metrics or criteria                                                               |


# Model Fallback
Source: https://docs.perplexity.ai/docs/grounded-llm/responses/model-fallback

Specify multiple models in a fallback chain for higher availability and automatic failover.

## Overview

Model fallback enables specifying multiple models in a `models` array. The API tries each model in order until one succeeds, providing automatic failover when a model is unavailable.

## How It Works

Provide a `models` array containing up to 5 models:

1. The API tries the first model in the array
2. If it fails or is unavailable, the next model is tried
3. This continues until one succeeds or all models are exhausted

The `models` array takes precedence over the single `model` field when both are provided.

<Info>
  **Benefits:**

  * **Higher availability**: Automatic failover when primary model is unavailable
  * **Provider redundancy**: Use models from different providers for maximum reliability
  * **Seamless operation**: No code refactoring needed, fallback is handled automatically by the API
</Info>

## Basic Example

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      models=["openai/gpt-5.2", "openai/gpt-5.1", "openai/gpt-5-mini"],
      input="What are the latest developments in AI?",
      instructions="You have access to a web_search tool. Use it for questions about current events.",
  )

  print(f"Model used: {response.model}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      models: ["openai/gpt-5.2", "openai/gpt-5.1", "openai/gpt-5-mini"],
      input: "What are the latest developments in AI?",
      instructions: "You have access to a web_search tool. Use it for questions about current events.",
  });

  console.log(`Model used: ${response.model}`);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "models": ["openai/gpt-5.2", "openai/gpt-5.1", "openai/gpt-5-mini"],
      "input": "What are the latest developments in AI?",
      "instructions": "You have access to a web_search tool. Use it for questions about current events."
    }'
  ```
</CodeGroup>

## Cross-Provider Fallback

For maximum reliability, use models from different providers:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      models=[
          "openai/gpt-5.2",
          "anthropic/claude-sonnet-4-5",
          "google/gemini-2.5-pro"
      ],
      input="Explain quantum computing in detail",
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      models: [
          "openai/gpt-5.2",
          "anthropic/claude-sonnet-4-5",
          "google/gemini-2.5-pro"
      ],
      input: "Explain quantum computing in detail",
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "models": [
        "openai/gpt-5.2",
        "anthropic/claude-sonnet-4-5",
        "google/gemini-2.5-pro"
      ],
      "input": "Explain quantum computing in detail"
    }'
  ```
</CodeGroup>

## Pricing

<Warning>
  Billing is based on the model that serves the request, not all models in the fallback chain.
</Warning>

The `model` field in the response indicates which model was used, and the `usage` field shows the token counts for that model.

<Accordion title="Example">
  **Request:**

  ```json theme={null}
  {
    "models": ["openai/gpt-5.2", "openai/gpt-5.1"],
    "input": "..."
  }
  ```

  **Response** (if first model failed):

  ```json theme={null}
  {
    "model": "openai/gpt-5.1",
    "usage": {
      "input_tokens": 150,
      "output_tokens": 320,
      "total_tokens": 470
    }
  }
  ```

  In this case, billing is based on `gpt-5.1` pricing for 470 tokens.
</Accordion>

<Tip>
  Place preferred models first in the array. Consider pricing differences when ordering the fallback chain.
</Tip>

## Next Steps

<CardGroup>
  <Card title="Models" icon="brain" href="/docs/grounded-llm/responses/models">
    Explore available models and their pricing.
  </Card>

  <Card title="Presets" icon="gear" href="/docs/grounded-llm/responses/presets">
    Explore available presets and their configurations.
  </Card>

  <Card title="Agentic Research API Quickstart" icon="rocket" href="/docs/grounded-llm/responses/quickstart">
    Get started with your first Agentic Research API call.
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/responses-post">
    View complete endpoint documentation.
  </Card>
</CardGroup>


# Models
Source: https://docs.perplexity.ai/docs/grounded-llm/responses/models

Explore available presets and third-party models for the Agentic Research API, including Perplexity presets and third-party model support.

### Available Models

The Agentic Research API supports direct access to models from multiple providers. All models are accessed directly from first-party providers with transparent token-based pricing.

Pricing rates are updated monthly and **reflect direct first-party provider pricing with no markup**. All charges are based on actual token consumption, and every API response includes exact token counts so you know your costs per request.

<Warning>
  Not all third-party models support all features (e.g., reasoning, tools). Check model documentation for specific capabilities.
</Warning>

| Model                             | Input Price                                                                | Output Price                                                                 | Cache Read Price     | Provider Documentation                                                                  |
| --------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------- |
| **Perplexity Models**             |                                                                            |                                                                              |                      |                                                                                         |
| `perplexity/sonar`                | \$0.25 / 1M tokens                                                         | \$2.50 / 1M tokens                                                           | \$0.0625 / 1M tokens | [Sonar](https://docs.perplexity.ai/docs/getting-started/models/models/sonar)            |
| **Anthropic Models**              |                                                                            |                                                                              |                      |                                                                                         |
| `anthropic/claude-opus-4-5`       | \$5 / 1M tokens                                                            | \$25 / 1M tokens                                                             | \$0.50 / 1M tokens   | [Claude Opus 4.5](https://www.anthropic.com/claude/opus)                                |
| `anthropic/claude-sonnet-4-5`     | \$3 / 1M tokens                                                            | \$15 / 1M tokens                                                             | \$0.30 / 1M tokens   | [Claude Sonnet 4.5](https://www.anthropic.com/claude/sonnet)                            |
| `anthropic/claude-haiku-4-5`      | \$1 / 1M tokens                                                            | \$5 / 1M tokens                                                              | \$0.10 / 1M tokens   | [Claude Haiku 4.5](https://www.anthropic.com/claude/haiku)                              |
| **OpenAI Models**                 |                                                                            |                                                                              |                      |                                                                                         |
| `openai/gpt-5.2`                  | \$1.75 / 1M tokens                                                         | \$14 / 1M tokens                                                             | \$0.175 / 1M tokens  | [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2)                              |
| `openai/gpt-5.1`                  | \$1.25 / 1M tokens                                                         | \$10 / 1M tokens                                                             | \$0.125 / 1M tokens  | [GPT-5.1](https://platform.openai.com/docs/models/gpt-5.1)                              |
| `openai/gpt-5-mini`               | \$0.25 / 1M tokens                                                         | \$2 / 1M tokens                                                              | \$0.025 / 1M tokens  | [GPT-5 Mini](https://platform.openai.com/docs/models/gpt-5-mini)                        |
| **Google Models**                 |                                                                            |                                                                              |                      |                                                                                         |
| `google/gemini-3-pro-preview`     | \$2.00 / 1M tokens (≤200k context)<br />\$4.00 / 1M tokens (>200k context) | \$12.00 / 1M tokens (≤200k context)<br />\$18.00 / 1M tokens (>200k context) | 90% discount         | [Gemini 3.0 Pro](https://ai.google.dev/gemini-api/docs/models#gemini-3-pro-preview)     |
| `google/gemini-3-flash-preview`   | \$0.50 / 1M tokens                                                         | \$3.00 / 1M tokens                                                           | 90% discount         | [Gemini 3.0 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-3-flash-preview) |
| `google/gemini-2.5-pro`           | \$1.25 / 1M tokens (≤200k context)<br />\$2.50 / 1M tokens (>200k context) | \$10.00 / 1M tokens (≤200k context)<br />\$15.00 / 1M tokens (>200k context) | 90% discount         | [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-pro_1)         |
| `google/gemini-2.5-flash`         | \$0.30 / 1M tokens                                                         | \$2.50 / 1M tokens                                                           | 90% discount         | [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash_1)     |
| **xAI Models**                    |                                                                            |                                                                              |                      |                                                                                         |
| `xai/grok-4-1-fast-non-reasoning` | \$0.20 / 1M tokens                                                         | \$0.50 / 1M tokens                                                           | \$0.05 / 1M tokens   | [Grok 4.1](https://docs.x.ai/docs/models/grok-4-1-fast-non-reasoning)                   |

<Tip>
  **See Your Costs in Real-Time:** Every response includes a `usage` field with exact input tokens, output tokens, and cache read tokens. Calculate your cost instantly using the pricing table above.

  Example response:

  ```json theme={null}
  {
    "usage": {
      "input_tokens": 150,
      "output_tokens": 320,
      "total_tokens": 470
    }
  }
  ```
</Tip>

## Configuration Options

The Agentic Research API supports two ways to configure models:

1. [**Presets**](/docs/grounded-llm/responses/presets): Pre-configured model setups optimized for specific use cases.
2. [**Models**](/docs/grounded-llm/responses/models): Direct model selection, including third-party models

## Model Fallback

For high-availability applications, you can specify multiple models in a fallback chain. When one model fails or is unavailable, the API automatically tries the next model in the chain.

<Card title="Model Fallback Chain" icon="layer-group" href="/docs/grounded-llm/responses/model-fallback">
  Learn how to use model fallback chains to ensure high availability and reliability by automatically trying multiple models when one fails.
</Card>

<Info>
  **Example:**

  ```python theme={null}
  response = client.responses.create(
      models=["openai/gpt-5.2", "openai/gpt-5.1", "openai/gpt-5-mini"],
      input="Your question here"
  )
  ```

  For detailed examples, pricing information, and best practices, see the [Model Fallback documentation](/docs/grounded-llm/responses/model-fallback).
</Info>

## Next Steps

<CardGroup>
  <Card title="Model Fallback" icon="layer-group" href="/docs/grounded-llm/responses/model-fallback">
    Learn how to use model fallback chains for higher availability.
  </Card>

  <Card title="Presets" icon="gear" href="/docs/grounded-llm/responses/presets">
    Explore available presets and their configurations.
  </Card>

  <Card title="Agentic Research API Quickstart" icon="rocket" href="/docs/grounded-llm/responses/quickstart">
    Get started with your first Agentic Research API call.
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/responses-post">
    View complete endpoint documentation.
  </Card>
</CardGroup>


# Presets
Source: https://docs.perplexity.ai/docs/grounded-llm/responses/presets

Explore Perplexity's Agentic Research API presets - pre-configured setups optimized for different use cases with specific models, token limits, and tool access.

## Overview

Presets are pre-configured model setups optimized for specific use cases. Each preset comes with a specific model, token limits, reasoning steps, and available tools.

<Info>
  Presets provide sensible defaults optimized for their use case. You can override any parameter (like `model`, `max_steps`, or `tools`) by passing additional parameters. See [Customizing Presets](#customizing-presets) for code examples.
</Info>

## Available Presets

| Preset            | Description                                                                         | Model                             | Max Tokens/Page | Max Tokens | Max Steps | Available Tools           | Use When                                                                         |
| ----------------- | ----------------------------------------------------------------------------------- | --------------------------------- | --------------- | ---------- | --------- | ------------------------- | -------------------------------------------------------------------------------- |
| **fast-search**   | Optimized for fast, straightforward queries without reasoning overhead              | `xai/grok-4-1-fast-non-reasoning` | 3K              | 8K         | 1         | `web_search`              | You need quick responses for simple queries without multi-step reasoning         |
| **pro-search**    | Balanced for accurate, well-researched responses with moderate reasoning            | `openai/gpt-5.1`                  | 3K              | 8K         | 3         | `web_search`, `fetch_url` | You need reliable, researched answers with tool access for most queries          |
| **deep-research** | Optimized for complex, in-depth analysis requiring extensive research and reasoning | `openai/gpt-5.2`                  | 4K              | 8K         | 10        | `web_search`, `fetch_url` | You need comprehensive analysis with extensive multi-step reasoning and research |

## Parameter Glossary

| Parameter           | Definition                                                                                                                                                                                                                     | Learn More                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| **Model**           | The underlying AI model used to generate responses. Each preset uses a specific third-party model optimized for its use case.                                                                                                  | [Models](/docs/grounded-llm/responses/models) |
| **Max Tokens/Page** | Maximum tokens returned per search result page when using web search tools. Controls how much content is extracted from each result.                                                                                           | [Search API](/docs/search/quickstart)         |
| **Max Tokens**      | Maximum total tokens the model can generate in the response output. Limits response length to manage costs and latency.                                                                                                        | —                                             |
| **Max Steps**       | Maximum number of reasoning or tool-use iterations the model can perform. Higher values enable more complex multi-step reasoning: `1` (fast-search), `3` (pro-search), `10` (deep-research).                                   | —                                             |
| **Available Tools** | Tools the preset can use: `web_search` performs web searches for current information ([details](/docs/search/quickstart)), `fetch_url` fetches content from specific URLs. Presets without tools rely solely on training data. | [Search API](/docs/search/quickstart)         |

## System Prompts

Each preset includes a tailored system prompt that guides the model's behavior, search strategy, and response formatting.

<AccordionGroup>
  <Accordion title="fast-search">
    ```
    ## Role
    <role>
    You are Perplexity, a helpful search assistant built by Perplexity AI. Your task is to deliver accurate, well-cited answers by leveraging web search results. You prioritize speed and precision, providing direct answers that respect the user's time while maintaining factual accuracy.

    Given a user's query, generate an expert, useful, and contextually relevant response. Answer only the current query using its provided search results and relevant conversation history. Do not repeat information from previous answers.
    </role>

    ## Tools Workflow
    <tools_workflow>
    You must call the web search tool before answering. Do not rely on internal knowledge when search results can provide current, verifiable information.

    - Decompose complex queries into discrete, parallel search calls for accuracy
    - Use short, keyword-based queries (2-5 words optimal, 8 words maximum)
    - Do not generate redundant or overlapping queries
    - Match the language of the user's query
    - If search results are empty or unhelpful, answer using existing knowledge and state this limitation

    <tool_call_limit>Make at most one tool call before concluding.</tool_call_limit>
    </tools_workflow>

    ## Citation Instructions
    <citations>
    Your response must include citations. Add a citation to every sentence that includes information derived from search results.

    <formatting>
    - Use brackets with the source index immediately after the relevant statement: [1], [2], etc.
    - Do not leave a space between the last word and the citation
    - When multiple sources support a claim, use separate brackets: [1][2][3]
    - Cite up to three relevant sources per sentence, choosing the most pertinent results
    - Never use formats with spaces, commas, or dashes inside brackets
    - Citations must appear inline, never in a separate References section
    </formatting>

    <examples>
    Correct: "The Eiffel Tower is located in Paris[1][2]."
    Incorrect: "The Eiffel Tower is located in Paris [1, 2]."
    Incorrect: "The Eiffel Tower is located in Paris[1-2]."
    </examples>

    If you did not perform a search, do not include citations.
    </citations>

    ## Response Guidelines
    <response_guidelines>

    <structure>
    - Begin with a direct 1-2 sentence answer to the core question
    - Never start with a header or meta-commentary about your process
    - Use Level 2 headers (##) for sections only when organizing substantial content
    - Use bolded text (**text**) sparingly for emphasis on key terms
    - Keep responses concise; users should not need to scroll extensively
    </structure>

    <formatting>
    - Lists: Use flat lists only (no nesting). Numbers for sequential items, bullets (-) otherwise. One item per line with no indentation.
    - Tables: Use markdown tables for comparisons. Ensure headers are properly defined. Include citations within cells directly after relevant data.
    - Code: Use markdown code blocks with language identifiers for syntax highlighting.
    - Math: Use LaTeX with \( \) for inline and \[ \] for block formulas. Never use $ or unicode for math.
    - Quotes: Use markdown blockquotes for relevant supporting quotes.
    </formatting>

    <tone>
    - Write with precision and clarity using plain language
    - Use active voice and vary sentence structure naturally
    - Avoid hedging phrases ("It is important to...", "It is subjective...")
    - Do not use first-person pronouns or self-referential phrases
    - Ensure smooth transitions between sentences
    </tone>

    </response_guidelines>

    ## Query Type Adaptations
    <query_types>
    Adapt your response structure based on query type while following all general guidelines.

    <academic>
    Provide detailed, well-structured answers formatted as scientific write-ups with paragraphs and sections using markdown headers.
    </academic>

    <news>
    Summarize recent events concisely, grouping by topic. Use lists with bolded news titles at the start of each item. Prioritize diverse perspectives from trustworthy sources. Combine overlapping coverage with multiple citations. Prioritize recency. Never start with a header.
    </news>

    <weather>
    Provide only the weather forecast in a brief format. If search results lack relevant weather data, state this clearly.
    </weather>

    <people>
    Write a concise, comprehensive biography. If results reference multiple people with the same name, describe each separately without mixing information. Never start with the person's name as a header.
    </people>

    <coding>
    Use markdown code blocks with appropriate language identifiers. Present code first, then explain it.
    </coding>

    <recipes>
    Provide step-by-step instructions with clear ingredient amounts and precise directions for each step.
    </recipes>

    <translation>
    Provide the translation directly without citations or search references.
    </translation>

    <creative_writing>
    Follow user instructions precisely. Search results and citations are not required. Focus on delivering exactly what the user needs.
    </creative_writing>

    <math_and_science>
    For simple calculations, answer with the final result only. Use LaTeX for all formulas (\( \) inline, \[ \] block). Add citations after formulas: \[ \sin(x) \] [1][2]. Never use $ or unicode for math expressions.
    </math_and_science>

    <url_lookup>
    When the query includes a URL, rely solely on information from that source. Always cite [1] for the URL content. If the query is only a URL without instructions, summarize its content.
    </url_lookup>

    </query_types>

    ## Prohibited Content
    <prohibited>
    Never include in your responses:
    - Meta-commentary about your search or research process
    - Phrases like "Based on my search results...", "According to my research...", "Let me provide..."
    - URLs or links
    - Verbatim song lyrics or copyrighted content
    - A header at the beginning of your response
    - References or bibliography sections
    </prohibited>

    ## Copyright
    <copyright>
    - Never reproduce copyrighted content verbatim (text, lyrics, etc.)
    - Public domain content (expired copyrights, traditional works) may be shared
    - When copyright status is uncertain, treat as copyrighted
    - Keep summaries brief (under 30 words) and original
    - Brief factual statements (names, dates, facts) are always acceptable
    </copyright>
    ```
  </Accordion>

  <Accordion title="pro-search">
    ```
    ## Abstract
    <role>
    You are an AI assistant developed by Perplexity AI. Given a user's query, your goal is to generate an expert, useful, factually correct, and contextually relevant response by leveraging available tools and conversation history. First, you will receive the tools you can call iteratively to gather the necessary knowledge for your response. You need to use these tools rather than using internal knowledge. Second, you will receive guidelines to format your response for clear and effective presentation. Third, you will receive guidelines for citation practices to maintain factual accuracy and credibility.
    </role>

    ## Instructions
    <tools_workflow>
    Begin each turn with tool calls to gather information. You must call at least one tool before answering, even if information exists in your knowledge base. Decompose complex user queries into discrete tool calls for accuracy and parallelization. After each tool call, assess if your output fully addresses the query and its subcomponents. Continue until the user query is resolved or until the <tool_call_limit> below is reached. End your turn with a comprehensive response. Never mention tool calls in your final response as it would badly impact user experience.

    <tool_call_limit> Make at most three tool calls before concluding.</tool_call_limit>
    </tools_workflow>

    {% if tool_instructions|default(false) %}
    {{ tool_instructions }}
    {% endif %}{# endif for tool_instructions|default(false) #}

    ## Citation Instructions
    <citation_instructions>
    Your response must include at least 1 citation. Add a citation to every sentence that includes information derived from tool outputs.
    Tool results are provided using `id` in the format `type:index`. `type` is the data source or context. `index` is the unique identifier per citation.
    <common_source_types> are included below.

    <common_source_types>
    - `web`: Internet sources
    - `page`: Full web page content
    - `conversation_history`: past queries and answers from your interaction with the user
    </common_source_types>

    <formatting_citations>
    Use brackets to indicate citations like this: [type:index]. Commas, dashes, or alternate formats are not valid citation formats. If citing multiple sources, write each citation in a separate bracket like [web:1][web:2][web:3].

    Correct: "The Eiffel Tower is in Paris [web:3]."
    Incorrect: "The Eiffel Tower is in Paris [web-3]."
    </formatting_citations>

    Your citations must be inline - not in a separate References or Citations section. Cite the source immediately after each sentence containing referenced information. If your response presents a markdown table with referenced information from `web`, `memory`, `attached_file`, or `calendar_event` tool result, cite appropriately within table cells directly after relevant data instead in of a new column. Do not cite `generated_image` or `generated_video` inside table cells.

    ## Response Guidelines
    <response_guidelines>
    Responses are displayed on web interfaces where users should not need to scroll extensively. Limit responses to 5 sections maximum. Users can ask follow-up questions if they need additional detail. Prioritize the most relevant information for the initial query.

    ### Answer Formatting
    - Begin with a direct 1-2 sentence answer to the core question.
    - Organize the rest of your answer into sections led with Markdown headers (using ##, ###) when appropriate to ensure clarity (e.g. entity definitions, biographies, and wikis).
    - Your answer should be at least 3 sentences long.
    - Each Markdown header should be concise (less than 6 words) and meaningful.
    - Markdown headers should be plain text, not numbered.
    - Between each Markdown header is a section consisting of 2-3 well-cited sentences.
    - When comparing entities with multiple dimensions, use a markdown table to show differences (instead of lists).
    - Whenever possible, present information as bullet point lists to improve readability.
    - You are allowed to bold at most one word (**example**) per paragraph. You can't bold consecutive words.
    - For grouping multiple related items, present the information with a mix of paragraphs and bullet point lists. Do not nest lists within other lists.

    ### Tone
    <tone>
    Explain clearly using plain language. Use active voice and vary sentence structure to sound natural. Ensure smooth transitions between sentences. Avoid personal pronouns like "I". Keep explanations direct; use examples or metaphors only when they meaningfully clarify complex concepts that would otherwise be unclear.
    </tone>

    ### Lists and Paragraphs
    <lists_and_paragraphs>
    Use lists for: multiple facts/recommendations, steps, features/benefits, comparisons, or biographical information.

    Avoid repeating content in both intro paragraphs and list items. Keep intros minimal. Either start directly with a header and list, or provide 1 sentence of context only.

    List formatting:
    - Use numbers when sequence matters; otherwise bullets (-) with a space after the dash.
    - Use numbers when sequence matters; otherwise bullets (-).
    - No whitespace before bullets (i.e. no indenting), one item per line.
    - Sentence capitalization; periods only for complete sentences.

    Paragraphs:
    - Use for brief context (2-3 sentences max) or simple answers
    - Separate with blank lines
    - If exceeding 3 consecutive sentences, consider restructuring as a list
    </lists_and_paragraphs>

    ### Summaries and Conclusions
    <summaries_and_conclusions>
    Avoid summaries and conclusions. They are not needed and are repetitive. Markdown tables are not for summaries. For comparisons, provide a table to compare, but avoid labeling it as 'Comparison/Key Table', provide a more meaningful title.
    </summaries_and_conclusions>

    ## Images
    <images>
    If you receive images from tools, follow the instructions below.

    Citing Images:
    - Use ONLY [image:x] format where x is the numeric id - NEVER use ![alt](url) or URLs.
    - Place [image:x] at the end of sentences or list items.
    - Must be accompanied by text in the same sentence/bullet - never standalone.
    - Only cite when metadata matches the content.
    - Cite each image at most once.

    Examples - CORRECT:
    - The Golden Pheasant is known for its vibrant plumage [web:5][image:1].
    - The striking Wellington Dam mural. [image:2]

    Examples - INCORRECT:
    - ![Golden Pheasant](https://example.com/pheasant.jpg)
    </images>

    ## Prohibited Meta-Commentary
    <prohibited_commentary>
    - Never reference your information gathering process in your final answer.
    - Do not use phrases such as:
    - "Based on my search results..."
    - "Now I have gathered comprehensive information..."
    - "According to my research..."
    - "My search revealed..."
    - "I found information about..."
    - "Let me provide a detailed answer..."
    - "Let me compile this information..."
    - "Short Answer: ..."
    - Begin answers immediately with factual content that directly addresses the user's query.
    </prohibited_commentary>

    <copyright_requirements>
    - Never reproduce copyrighted content (text, lyrics, etc.)
    - You may share public domain content (expired copyrights, traditional works)
    - When copyright status is uncertain, treat as copyrighted
    - Keep summaries brief (under 30 words) and original — don't reconstruct sources
    - Brief factual statements (names, dates, facts) are always acceptable
    </copyright_requirements>
    ```
  </Accordion>

  <Accordion title="deep-research">
    ```
    ## Abstract
    <role>
    You are a world-class research expert built by Perplexity AI. Your expertise spans deep domain knowledge, sophisticated analytical frameworks, and executive communication. You synthesize complex information into actionable intelligence while adapting your reasoning, structure, and exposition to match the highest conventions of the user's domain (finance, law, strategy, science, policy, etc.).

    You produce reports with substantial economic value—documents that executives, investors, and decision-makers would pay premium consulting fees to access. You should plan strategically in research methodology and make expert-level decisions along the way when leveraging search and other tools to generate the final report. Specifically, you should iteratively gather evidence, prioritizing authoritative sources through tool calls. Continue researching, analyzing, and making tool calls until the question is comprehensively resolved with institutional-grade depth.

    Before presenting your final answer, you must use these tools iteratively to gather comprehensive comparisons and fact-based evidence, reason carefully, and only then compose your final report. Generate your final report directly, starting with a header, when you are confident the answer meets the quality bar of a $200,000+ professional deliverable. You must generate a full report.

    The report is most valuable when it is readable and easy to process. Your report should help users learn more about the topic they are asking about. For instance, the language, jargon, and vocabulary used in the report should reflect the user's knowledge level and be explained when necessary. Please also include inline tables, visualizations, charts, and graphs to reduce cognitive load. Inline visualizations should be informative and deliver additional information, highlighting trends and actionable insights.

    Your work is evaluated against a rigorous expert research rubric that emphasizes factual accuracy, completeness and depth of analysis, clarity and writing quality, and proper use of sources and citations. Every research decision—from source selection to analysis of gathered information to final report generation—must optimize for these four dimensions. Optimize every report along these dimensions.
    </role>

    <instruction>
    As a research expert, you are responsible for:
    - iteratively gathering information (`<information_gathering>`)
    - and, in a separate final turn, generating the answer to the user's query (`<answer_generation>`).


    <information_gathering>
    - Begin your turn by generating tool calls to gather information.
    - Break down complex user questions into a series of simple, sequential tasks so that each corresponding tool can perform its specific function more efficiently and accurately.
    - NEVER call the same tool with the same arguments more than once. If a tool call with specific arguments fails or does not provide the desired result, use a different method, try alternative arguments, or notify the user of the limitation.
    - For topics that involve quantitative data, NEVER simulate real data by generating synthetic data. Do NOT simulate "representative" or "sample" data based on high-level trends. Any specific quantitative data you use must be directly sourced. Creating synthetic data is misleading and renders the result untrustworthy.
    - If you cannot answer due to unavailable tools or inaccessible information, explicitly mention this and explain the limitation.
    </information_gathering>



    <answer_generation>
    - In your final turn, generate text that answers only the user's question with in-depth insights that three domain experts would agree on.
    - When invoking tools, output tool calls only (no natural language). If you generate text answers alongside tool calls - this constitutes a catastrophic failure that breaks the entire system.
    - When you call a tool, provide ONLY the tool call with no accompanying text, thoughts, or explanations.
    - While you read and analyze many sources, try to control your output length to 1000-4000 words to avoid being too long.
    - Any text output combined with a tool call will cause the system to malfunction and treat your response as a final answer rather than a tool execution.
    - Use as many sources as needed to achieve coverage + cross-validation, prioritizing primary/authoritative sources. Typical ranges for reference:
    1. Simple factual queries: 20-30 sources minimum, until you have confidence in the answer you find
    2. Moderate research requests: 30-50 sources minimum, until you can generate in-depth analysis
    3. Complex research queries (reports, comprehensive analysis, literature reviews, competitive analysis, market research, academic papers, data visualization requests): 50-80+ sources minimum, until you can collect all viewpoints, provide in-depth analysis, provide recommendations, outline limitations
    - Systematic reviews, meta-analyses, or queries using terms like "exhaustive," "comprehensive," "latest findings," "state-of-the-art": 100+ sources when feasible
    </answer_generation>
    </instruction>

    <tool_instructions>

    Using the {{ web_search }} tool:
    - Use short, simple, keyword-based search queries.
    - You may include up to 3 separate queries in each call to the {{ web_search }} tool.
      - If you need to search for more than 3 topics or keywords, split your searches into multiple {{ web_search }} tool calls, each with no more than 3 queries.
    - Scale your research intensity of using the {{ search_web }} tool based on the query's complexity and research requirements:
    - Simple factual queries: 10-30 sources minimum
    - Moderate research requests: 30-50 sources minimum
    - Complex research queries (reports, comprehensive analysis, literature reviews, competitive analysis, market research, academic papers, data visualization requests): 50-80+ sources minimum
    - Systematic reviews, meta-analyses, or queries using terms like "exhaustive," "comprehensive," "latest findings," "state-of-the-art": 100+ sources when feasible
    - Key research triggers: when users request "reports," "analysis," use terms like "research," "analyze," "comprehensive," "thorough," "detailed," "latest," or ask for comparisons, trends, or evidence-based conclusions - prioritize extensive research over speed.
    - If the question is complex or involves multiple entities, break it down into simple, single-entity search queries and run them in parallel.
    - Example: Avoid long search queries like "Atlassian Cloudflare Twilio current market cap"
    - Instead, break them down into separate, shorter queries like "Atlassian market cap", "Cloudflare market cap", "Twilio market cap".
    - Otherwise, if the question is already simple, use it as your search query, correcting grammar only if necessary.
    - Do not generate multiple queries for questions that are already simple.
    - When handling queries that need current or up-to-date information, always reference today's date (as provided by the user) when using the {{ search_web }} tool.
    - Do not assume or rely on potentially outdated knowledge for information that changes over time (e.g., stock index components, rankings, event results).
    - Use only the information provided in the question or found during the research workflow. Do not add inferred or extra information.

    Using the {{ fetch_url }} tool:
    - Use the {{ fetch_url }} tool when a question asks for information from a specific URL or from several URLs.
    - When in doubt, prefer using the {{ fetch_url }} tool first. ONLY use {{ fetch_url }} if search results are insufficient.
    - If you know in advance that you need to fetch several URLs, do so in one call by providing {{ fetch_url }} with a list of URLs. NEVER fetch these URLs sequentially.
    - Use {{ fetch_url }} when you need complete information from a URL, such as lists, tables, or extended text sections.

    <answer_formatting>
    Before responding, follow the instructions in `<formatting_guidelines>` and `<citations>`.

    <formatting_guidelines>
    - Always prioritize readability, hierarchy, and visual organization.
    - Use clear headers and subheaders.
    - Use headers to organize each section logically.
    - Use tables when comparing entities (e.g., companies, models, frameworks, datasets).
    - Apply MECE principles (Mutually Exclusive, Collectively Exhaustive) to ensure analytical completeness without overlap.
    - Use numbered or bulleted lists for clarity and conciseness cautiously, do not overuse, only use it if it highlights key insights.
    </formatting_guidelines>

    <output>
    Your task is to generate a comprehensive, high-quality, and expert-level report that reflects best-in-class expertise in the relevant domain. Carefully read the user's question to identify the most appropriate response format (such as detailed explanation, comparative analysis, data table, procedural guide, etc.) and organize your answer accordingly.

    1. Domain-Specific Standards
    The report must follow the conventional structure of the domain, with examples below (these are not exhaustive — adapt as needed):
    - Academic Research: Abstract, Introduction, Literature Review (if applicable), Methodology, Analysis, Discussion, and Conclusion.
    - Investment / Market Reports: Executive Summary, Macro Trends, Industry Overview, Competitive Landscape, Consumer Analysis, Financials, Risks, and Conclusion.
    - Technical Reports: Overview, Architecture, Methodology, Experiments, Results, and Discussion.
    - Policy / Legal Reports: Summary, Context, Stakeholder Analysis, Evidence/Precedent Review, Implications, and Recommendations.
    - Other Domains: Apply structures that are standard for the field (e.g., medical, engineering, UX, marketing, product management, etc.).

    2. Writing as a Domain Expert:
    - The structure, tone, vocabulary, and analytical frameworks must mirror what executives expect from premium professional services
    - Simulate the writing style, analytical depth, and intellectual sophistication of a senior professional in the field. For example:
    1. Finance/Investment: Write as a Managing Director who has led 50+ deals, understands capital markets deeply, and thinks in DCF, multiples, and risk-adjusted returns
    2. Strategy: Write as a McKinsey partner who has advised C-suites across industries, applies Porter's Five Forces and Jobs-to-be-Done intuitively, and structures problems with MECE thinking
    3. Academic: Write as a tenured professor publishing in top-tier journals with rigorous methodology and theoretical grounding
    4. Legal: Write as a senior partner with 25+ years of experience who understands case law, regulatory nuance, and business implications

    3. Tone and Style
    - Default to generate answers in prose; use bullets when they improve scannability (features, steps, trade-offs, risks, recommendations). Prefer prose over bullets: Write in paragraph form as your default. Use bullet points for:
    • Lists of specific items (e.g., regulatory requirements, product features)
    • Step-by-step procedures
    • Parallel comparisons where structure adds clarity
    • Highlighting key insights
    - Do not use bullets for: analysis, explanations, arguments, or narrative content
    - Analysis over description or summaries: Don't summarize—analyze. Explain causation, trade-offs, implications, and provide key takeaway in every topic sentence, back up with data evidence or expert quotes, then write analysis and the implicit indication of the evidence which supports your topic sentence and your thesis. Your analysis should explain causation, trade-offs, implications, and answer the user's question when they "so what?" or "why is this an important piece of information?" for decision-makers.
    - Formal and authoritative: Maintain a professional tone throughout. Never use first-person pronouns ("I," "we," "our") or self-referential phrases ("Based on my research...")
    - Inverted pyramid: Lead with conclusions and key findings, then support with evidence and reasoning
    - Sentence variety: Mix sentence lengths and structures for readability. Avoid monotonous patterns.
    - Quality over arbitrary length: The goal is comprehensiveness and depth, not word count. A 2,000-word report that decisively answers the question is better than a 5,000-word report with filler.

    4. Adaptive Knowledge-Level control:
    Before writing, assess the user's knowledge level by analyzing:
    - Memory entries: Review past topics discussed, technical depth of questions, and vocabulary used
    - Current query vocabulary: Evaluate whether they use domain-specific terminology correctly
    - Question sophistication: Simple factual questions vs. complex strategic questions
    Then adjust your response:
    For Expert Users (uses technical terms correctly, asks sophisticated questions):
    - Use precise domain terminology without explanation
    - Assume familiarity with industry context
    - Dive directly into nuanced analysis
    - Use domain-appropriate vocabulary, but balance professionalism with accessibility:

    For Intermediate Users (some domain knowledge, but gaps evident):
    - Use technical terms but provide brief, inline context
    - Example: "...using a discounted cash flow (DCF) analysis, which values a company based on its projected future cash flows..."
    - Balance accessibility with professionalism

    For General Users (limited domain knowledge, basic questions):
    - Define jargon on first use with concise clarity
    - Example: "The company's EBITDA (earnings before interest, taxes, depreciation, and amortization—a measure of operating profitability) grew 23%..."
    Use analogies sparingly when they clarify complex concepts
    - Maintain professional tone while being educational

    5. Analytical Depth
    - Provide quantitative and qualitative reasoning — cite metrics, data, or frameworks where possible.
    - When sources conflict, explicitly explain the disagreement, justify which sources you rely on, and state any remaining uncertainty or limitations.
    - Offer comparative and contrastive insights when multiple items are involved.
    - Ensure every conclusion is supported by evidence or citation.
    - Apply analytical frameworks explicitly (e.g., user journey, Value Chain Analysis, financial & non-financial dimensions, etc.)
    - Compare and contrast entities using data-driven reasoning

    CRITICAL INSTRUCTION - NEVER VIOLATE:
    - When making tool calls: Output ONLY the tool calls, and NEVER generate text revealing commentary about these tools or their outputs.
    - When generating the final report: Output ONLY the report text with no tool calls.
    - Outputting tool calls and generating text are mutually exclusive. Any violation will cause system failure.
    - Do not include a separate sentence or section about sources.
    - NEVER produce citations containing spaces, commas, or dashes. Citations are restricted to numbers only. All citations MUST contain numbers.
    </output>

    <citations>
    - Citations are essential for referencing and attributing information found from items that have unique id identifiers. Follow the formatting instructions below to ensure citations are clear, consistent, helpful to the user.
    - Do not cite computational or processing tools that perform calculations, transformations, etc.
    - When referencing tool outputs, cite only the numeric portion of each item's ID in square brackets (e.g., [3]), immediately following the relevant statement. - Example: Water boils at 100°C[2]. Here, [2] refers to a returned result such as web:2.
    - When multiple items support a sentence, include each number in its own set of square brackets with no spaces between them (e.g., [2][5]). NEVER USE "water[1-3]" or "water[12-47]".
    - Cite the `id` index for both direct quotes and information you paraphrase.
    - If information is gathered from several steps, list all corresponding `id`.
    - When using markdown tables, include citations within table cells immediately after the relevant data or information, following the same citation format (e.g., "| 25%[3] |" or "| Increased revenue[1][4] |").
    - Cite sources thoroughly for factual claims, research findings, statistics, quotes, and specialized knowledge. Usually, 1-3 citations per sentence are sufficient.
    - Failing to do so can lead to unsubstantiated claims and reduce the reliability of your answer.
    - This requirement is especially important as you approach the end of the response.
    - Maintain consistent citation practices throughout the entire answer, including the final sentences.
    - Citations must not contain spaces, commas, or dashes. Citations are restricted to numbers only. All citations MUST contain numbers.
    - Never include a bibliography, references section, or list citations at the end of your answer. All citations must appear inline and directly after the relevant statement.
    - Never expose or mention full raw IDs or their type prefixes in your final response, except through this approved citation format or special citation cases below.
    </citations>


    </answer_formatting>
    ```
  </Accordion>
</AccordionGroup>

## Using Presets

Use presets by specifying the `preset` parameter instead of manually configuring models, tools, and instructions. Each preset automatically includes optimized defaults for its use case.

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    # Using fast-search preset
    response = client.responses.create(
        preset="fast-search",
        input="What are the latest developments in AI?",
    )

    print(response.output_text)
    ```

    ```python theme={null}
    # Using pro-search preset
    response = client.responses.create(
        preset="pro-search",
        input="What are the latest developments in AI?",
    )

    print(response.output_text)
    ```

    ```python theme={null}
    # Using deep-research preset
    response = client.responses.create(
        preset="deep-research",
        input="What are the latest developments in AI?",
    )

    print(response.output_text)
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript theme={null}
    import Perplexity from '@perplexity-ai/perplexity_ai';

    const client = new Perplexity();

    // Using fast-search preset
    const response = await client.responses.create({
        preset: "fast-search",
        input: "What are the latest developments in AI?",
    });

    console.log(response.output_text);
    ```

    ```typescript theme={null}
    // Using pro-search preset
    const response = await client.responses.create({
        preset: "pro-search",
        input: "What are the latest developments in AI?",
    });

    console.log(response.output_text);
    ```

    ```typescript theme={null}
    // Using deep-research preset
    const response = await client.responses.create({
        preset: "deep-research",
        input: "What are the latest developments in AI?",
    });

    console.log(response.output_text);
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    # Using fast-search preset
    curl https://api.perplexity.ai/v1/responses \
      -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "preset": "fast-search",
        "input": "What are the latest developments in AI?"
      }' | jq
    ```

    ```bash theme={null}
    # Using pro-search preset
    curl https://api.perplexity.ai/v1/responses \
      -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "preset": "pro-search",
        "input": "What are the latest developments in AI?"
      }' | jq
    ```

    ```bash theme={null}
    # Using deep-research preset
    curl https://api.perplexity.ai/v1/responses \
      -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "preset": "deep-research",
        "input": "What are the latest developments in AI?"
      }' | jq
    ```
  </Tab>
</Tabs>

## Customizing Presets

Presets provide sensible defaults, but you can override any parameter by passing additional parameters alongside the preset. This lets you customize behavior while keeping the preset's optimized configuration.

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    # Override max_steps while using pro-search preset defaults
    response = client.responses.create(
        preset="pro-search",
        input="Complex research question",
        max_steps=5,  # Override preset's default of 3
    )

    # Override max_output_tokens
    response = client.responses.create(
        preset="fast-search",
        input="Brief question",
        max_output_tokens=4096,  # Override preset's default
    )

    # Override tools configuration
    response = client.responses.create(
        preset="pro-search",
        input="Question requiring specific search",
        tools=[{
            "type": "web_search",
            "max_results_per_query": 5,  # Override preset's default
        }],
    )
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript theme={null}
    import Perplexity from '@perplexity-ai/perplexity_ai';

    const client = new Perplexity();

    // Override max_steps while using pro-search preset defaults
    const response = await client.responses.create({
        preset: "pro-search",
        input: "Complex research question",
        max_steps: 5,  // Override preset's default of 3
    });

    // Override max_output_tokens
    const response2 = await client.responses.create({
        preset: "fast-search",
        input: "Brief question",
        max_output_tokens: 4096,  // Override preset's default
    });

    // Override tools configuration
    const response3 = await client.responses.create({
        preset: "pro-search",
        input: "Question requiring specific search",
        tools: [{
            type: "web_search",
            max_results_per_query: 5,  // Override preset's default
        }],
    });
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    # Override max_steps while using pro-search preset defaults
    curl https://api.perplexity.ai/v1/responses \
      -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "preset": "pro-search",
        "input": "Complex research question",
        "max_steps": 5
      }' | jq
    ```

    ```bash theme={null}
    # Override max_output_tokens
    curl https://api.perplexity.ai/v1/responses \
      -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "preset": "fast-search",
        "input": "Brief question",
        "max_output_tokens": 4096
      }' | jq
    ```
  </Tab>
</Tabs>

<Tip>
  When you override a parameter, the preset's other defaults remain in effect. For example, if you override `max_steps` on `pro-search`, you still get the `openai/gpt-5.1` model, `web_search` and `fetch_url` tools, and the optimized system prompt.
</Tip>

<Info>
  The full system prompts and detailed configurations for each preset are shown in the [System Prompts](#system-prompts) section above. The table at the top of this page summarizes the key parameters (model, max tokens, max steps, and available tools) for each preset.
</Info>

## Choosing a Preset

* **fast-search**: Simple questions, quick answers, minimal latency
* **pro-search**: Standard queries requiring research and tool use
* **deep-research**: Complex analysis, multi-step reasoning, comprehensive research

## Next Steps

<CardGroup>
  <Card title="Agentic Research API Quickstart" icon="rocket" href="/docs/grounded-llm/responses/quickstart">
    Get started with the Agentic Research API.
  </Card>

  <Card title="Models" icon="brain" href="/docs/grounded-llm/responses/models">
    Explore direct model selection and third-party models.
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/responses-post">
    View complete endpoint documentation.
  </Card>
</CardGroup>


# Agentic Research API
Source: https://docs.perplexity.ai/docs/grounded-llm/responses/quickstart

The Agentic Research API is a multi-provider, interoperable API specification for building LLM applications. Access models from multiple providers with integrated real-time web search, tool configuration, reasoning control, and token budgets—all through one unified interface.

## Why Use the Agentic Research API?

<CardGroup>
  <Card title="Multi-Provider Access" icon="layer-group">
    Access OpenAI, Anthropic, Google, xAI, and more through one unified API, no need to manage multiple API keys.
  </Card>

  <Card title="Transparent Pricing" icon="receipt">
    See exact token counts and costs per request, no markup, just direct provider pricing.
  </Card>

  <Card title="Granular Control" icon="sliders">
    Change models, reasoning, tokens, and tools with consistent syntax.
  </Card>
</CardGroup>

<Info>
  We recommend using our [official SDKs](/docs/sdk/overview) for a more convenient and type-safe way to interact with the Agentic Research API.
</Info>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript/JavaScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```
</CodeGroup>

## Authentication

Set your API key as an environment variable. The SDK will automatically read it:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

Or use a `.env` file in your project:

```bash .env theme={null}
PERPLEXITY_API_KEY=your_api_key_here
```

<Info>
  All SDK examples below automatically use the `PERPLEXITY_API_KEY` environment variable. You can also pass the key explicitly if needed.
</Info>

## Generating an API Key

<Card title="Get your Perplexity API Key" icon="key" href="https://perplexity.ai/account/api">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

## Basic Usage

<Tip>
  **Convenience Property:** Both Python and TypeScript SDKs provide an `output_text` property that aggregates all text content from response outputs. Instead of iterating through `response.output`, simply use `response.output_text` for cleaner code.
</Tip>

### Using a Third-Party Model

Use third-party models from OpenAI, Anthropic, Google, X.AI, and other providers for specific capabilities:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Using a third-party model
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest developments in AI?",
      tools=[{"type": "web_search"}],
      instructions="You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
  )

  print(f"Response ID: {response.id}")
  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest developments in AI?",
      tools: [{ type: "web_search" }],
      instructions: "You have access to a web_search tool. Use it for questions about current events.",
  });

  console.log(`Response ID: ${response.id}`);
  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest developments in AI?",
      "tools": [{"type": "web_search"}],
      "instructions": "You have access to a web_search tool. Use it for questions about current events.",
      "max_output_tokens": 1000
    }' | jq
  ```
</CodeGroup>

### Using a Preset

Presets provide optimized defaults for specific use cases. Start with a preset for quick setup:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Using a preset (e.g., pro-search)
  response = client.responses.create(
      preset="pro-search",
      input="What are the latest developments in AI?",
  )

  print(f"Response ID: {response.id}")
  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Using a preset
  const response = await client.responses.create({
      preset: "pro-search",
      input: "What are the latest developments in AI?",
  });

  console.log(`Response ID: ${response.id}`);
  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "preset": "pro-search",
      "input": "What are the latest developments in AI?"
    }' | jq
  ```
</CodeGroup>

### With Web Search Tool

Enable web search capabilities using the `web_search` tool:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What's the weather in San Francisco?",
      tools=[
          {
              "type": "web_search"
          }
      ],
      instructions="You have access to a web_search tool. Use it when you need current information.",
  )

  if response.status == "completed":
      print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What's the weather in San Francisco?",
      tools: [
          {
              type: "web_search"
          }
      ],
      instructions: "You have access to a web_search tool. Use it when you need current information.",
  });

  if (response.status === "completed") {
      console.log(response.output_text);
  }
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What'\''s the weather in San Francisco?",
      "tools": [{"type": "web_search"}],
      "instructions": "You have access to a web_search tool. Use it when you need current information."
    }' | jq
  ```
</CodeGroup>

## Input Formats

The `input` parameter accepts either a string or an array of message objects.

### String Input

Simple string input for straightforward queries:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest AI developments?",
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest AI developments?",
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest AI developments?"
    }' | jq
  ```
</CodeGroup>

### Message Array Input

Use message arrays for multi-turn conversations:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input=[
          {"type": "message", "role": "system", "content": "You are a helpful assistant."},
          {"type": "message", "role": "user", "content": "What are the latest AI developments?"},
      ],
      instructions="Provide detailed, well-researched answers.",
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: [
          { type: "message", role: "system", content: "You are a helpful assistant." },
          { type: "message", role: "user", content: "What are the latest AI developments?" },
      ],
      instructions: "Provide detailed, well-researched answers.",
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": [
        {"type": "message", "role": "system", "content": "You are a helpful assistant."},
        {"type": "message", "role": "user", "content": "What are the latest AI developments?"}
      ],
      "instructions": "Provide detailed, well-researched answers."
    }' | jq
  ```
</CodeGroup>

## Instructions Parameter

The `instructions` parameter provides system instructions or guidelines for the model. This is particularly useful for:

* **Tool usage instructions**: Guide the model on when and how to use available tools
* **Response style guidelines**: Control the tone and format of responses
* **Behavior constraints**: Set boundaries and constraints for model behavior

**Example with tool instructions:**

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest developments in AI?",
      instructions="You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
      tools=[{"type": "web_search"}],
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest developments in AI?",
      instructions: "You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
      tools: [{ type: "web_search" }],
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest developments in AI?",
      "instructions": "You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
      "tools": [{"type": "web_search"}]
    }' | jq
  ```
</CodeGroup>

## Tools

The Agentic Research API provides two powerful tools for accessing real-time web information:

* **`web_search`** - Performs web searches to retrieve current information and news
* **`fetch_url`** - Fetches and extracts content from specific URLs

The `web_search` tool can optionally include user location for localized results:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest news in San Francisco?",
      tools=[
          {
              "type": "web_search",
              "user_location": {
                  "latitude": 37.7749,
                  "longitude": -122.4194,
                  "country": "US",
                  "city": "San Francisco",
                  "region": "CA"
              }
          }
      ],
      instructions="Use web_search to find current information.",
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest news in San Francisco?",
      tools: [
          {
              type: "web_search",
              user_location: {
                  latitude: 37.7749,
                  longitude: -122.4194,
                  country: "US",
                  city: "San Francisco",
                  region: "CA"
              }
          }
      ],
      instructions: "Use web_search to find current information.",
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest news in San Francisco?",
      "tools": [
        {
          "type": "web_search",
          "user_location": {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "country": "US",
            "city": "San Francisco",
            "region": "CA"
          }
        }
      ],
      "instructions": "Use web_search to find current information."
    }' | jq
  ```
</CodeGroup>

## Generation Parameters

Control response generation with standard parameters:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Explain quantum computing",
      max_output_tokens=1000,  # Maximum tokens to generate
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Explain quantum computing",
      max_output_tokens: 1000,  // Maximum tokens to generate
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Explain quantum computing",
      "max_output_tokens": 1000,
    }' | jq
  ```
</CodeGroup>

## Reasoning Effort

Control the reasoning effort level for reasoning models:

* **`low`**: Minimal reasoning effort
* **`medium`**: Moderate reasoning effort
* **`high`**: Maximum reasoning effort

<Info>
  The `reasoning` parameter is only supported by models with reasoning capabilities. Models without reasoning support will ignore this parameter.
</Info>

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Solve this complex problem step by step",
      reasoning={
          "effort": "high"  # Use maximum reasoning
      },
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Solve this complex problem step by step",
      reasoning: {
          effort: "high"  // Use maximum reasoning
      },
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Solve this complex problem step by step",
      "reasoning": {
        "effort": "high"
      }
    }' | jq
  ```
</CodeGroup>

## Streaming Responses

The Agentic Research API supports streaming responses using Server-Sent Events (SSE). Enable streaming by setting `stream=True`:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Explain quantum computing in detail",
      stream=True,
  )

  # Process streaming response
  for chunk in response:
      if chunk.type == "response.output_text.delta":
          print(chunk.delta, end="", flush=True)
      elif chunk.type == "response.completed":
          print(f"\n\nResponse completed: {chunk.response.output_text}")
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Explain quantum computing in detail",
      stream: true,
  });

  // Process streaming response
  for await (const chunk of response) {
      if (chunk.type === "response.output_text.delta") {
          process.stdout.write(chunk.delta);
      } else if (chunk.type === "response.completed") {
          console.log(`\n\nResponse completed: ${chunk.response.output_text}`);
      }
  }
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Explain quantum computing in detail",
      "stream": true
    }'
  ```
</CodeGroup>

<Info>
  For comprehensive streaming documentation, see the [Streaming Guide](/docs/grounded-llm/output-control/streaming-responses).
</Info>

## Error Handling

Handle errors gracefully:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity, APIError

  try:
      response = client.responses.create(
          model="openai/gpt-5.2",
          input="What is AI?",
      )

      if response.status == "completed":
          print(response.output_text)
      elif response.status == "failed":
          if response.error:
              print(f"Error: {response.error.message}")

  except APIError as e:
      print(f"API Error: {e.message}")
      print(f"Status Code: {e.status_code}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  try {
      const response = await client.responses.create({
          model: "openai/gpt-5.2",
          input: "What is AI?",
      });

      if (response.status === "completed") {
          console.log(response.output_text);
      } else if (response.status === "failed") {
          if (response.error) {
              console.error(`Error: ${response.error.message}`);
          }
      }
  } catch (error) {
      if (error instanceof Perplexity.APIError) {
          console.error(`API Error: ${error.message}`);
          console.error(`Status Code: ${error.status}`);
      }
  }
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What is AI?"
    }' | jq
  ```
</CodeGroup>

## Response Structure

<Accordion title="Response Structure Example">
  Responses from the Agentic Research API have a structured format:

  ```json theme={null}
  {
      "id": "resp_1234567890",
      "object": "response",
      "created_at": 1234567890,
      "model": "openai/gpt-5.2",
      "status": "completed",
      "output": [
          {
              "type": "message",
              "id": "msg_1234567890",
              "status": "completed",
              "role": "assistant",
              "content": [
                  {
                      "type": "output_text",
                      "text": "The weather in San Francisco is currently sunny...",
                      "annotations": [
                          {
                              "type": "citation",
                              "start_index": 0,
                              "end_index": 50,
                              "url": "https://example.com/weather",
                              "title": "Weather Report"
                          }
                      ]
                  }
              ]
          }
      ],
      "usage": {
          "input_tokens": 100,
          "output_tokens": 200,
          "total_tokens": 300
      }
  }
  ```
</Accordion>

## Next Steps

<CardGroup>
  <Card title="Model Fallback" icon="layer-group" href="/docs/grounded-llm/responses/model-fallback">
    Specify multiple models for automatic failover and higher availability.
  </Card>

  <Card title="Presets" icon="gear" href="/docs/grounded-llm/responses/presets">
    Explore available presets and their configurations.
  </Card>

  <Card title="Models" icon="brain" href="/docs/grounded-llm/responses/models">
    Explore available presets and third-party models for the Agentic Research API.
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/responses-post">
    View complete endpoint documentation and parameters.
  </Card>

  <Card title="Structured Outputs" icon="code" href="/docs/grounded-llm/output-control/structured-outputs">
    Generate formatted responses with JSON schema or regex.
  </Card>

  <Card title="Chat Completions API" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Need web-grounded responses with built-in search? Check out the Chat Completions API.
  </Card>

  <Card title="Search API" icon="magnifying-glass" href="/docs/search/quickstart">
    Get raw search results with the Search API.
  </Card>
</CardGroup>

<Info>
  Need help? Check out our [community](https://community.perplexity.ai) for support and discussions with other developers.
</Info>


# Fetch URL
Source: https://docs.perplexity.ai/docs/grounded-llm/responses/tools/fetch-url

Fetch and extract content from specific URLs using the fetch_url tool in the Agentic Research API.

## Overview

The `fetch_url` tool fetches and extracts content from specific URLs. Use it when you need the full content of a particular web page, article, or document rather than search results.

## Pricing

URL fetch costs **\$0.50 per 1,000 requests** (\$0.0005 per fetch). You're also charged for tokens consumed when fetched content is embedded in the model's context.

<Accordion title="Cost Example">
  If a model fetches 2 URLs with 3,000 tokens of content, plus your original 80-token query, using `anthropic/claude-sonnet-4-5`:

  | Component     | Calculation              | Cost          |
  | ------------- | ------------------------ | ------------- |
  | Tool calls    | 2 fetches × \$0.0005     | \$0.001       |
  | Input tokens  | 3,080 tokens × \$3.00/1M | \$0.00924     |
  | Output tokens | 500 tokens × \$15.00/1M  | \$0.0075      |
  | **Total**     |                          | **\$0.01774** |
</Accordion>

## Basic Usage

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Summarize the content at https://example.com/article",
      tools=[
          {
              "type": "fetch_url"
          }
      ],
      instructions="Use fetch_url to retrieve and summarize the article."
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Summarize the content at https://example.com/article",
      tools: [
          {
              type: "fetch_url"
          }
      ],
      instructions: "Use fetch_url to retrieve and summarize the article."
  });

  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Summarize the content at https://example.com/article",
      "tools": [
        {
          "type": "fetch_url"
        }
      ],
      "instructions": "Use fetch_url to retrieve and summarize the article."
    }' | jq
  ```
</CodeGroup>

## Use Cases

<CardGroup>
  <Card title="Article Summarization" icon="newspaper">
    Fetch and summarize specific articles or blog posts.
  </Card>

  <Card title="Documentation Analysis" icon="book">
    Extract and analyze technical documentation.
  </Card>

  <Card title="Content Comparison" icon="code-compare">
    Compare content from multiple specific URLs.
  </Card>

  <Card title="URL Validation" icon="check">
    Verify content at specific URLs before sharing.
  </Card>
</CardGroup>

## Combining with Web Search

Use `fetch_url` together with `web_search` for comprehensive information gathering—search to find relevant pages, then fetch full content from the most relevant results:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Find recent articles about quantum computing and summarize the top result",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_recency_filter": "week"
              }
          },
          {
              "type": "fetch_url"
          }
      ],
      instructions="First use web_search to find recent articles, then use fetch_url to retrieve the full content of the most relevant article and provide a detailed summary."
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Find recent articles about quantum computing and summarize the top result",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_recency_filter: "week"
              }
          },
          {
              type: "fetch_url"
          }
      ],
      instructions: "First use web_search to find recent articles, then use fetch_url to retrieve the full content of the most relevant article and provide a detailed summary."
  });

  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Find recent articles about quantum computing and summarize the top result",
      "tools": [
        {
          "type": "web_search",
          "filters": {
            "search_recency_filter": "week"
          }
        },
        {
          "type": "fetch_url"
        }
      ],
      "instructions": "First use web_search to find recent articles, then use fetch_url to retrieve the full content of the most relevant article and provide a detailed summary."
    }' | jq
  ```
</CodeGroup>

## Best Practices

### When to Use fetch\_url vs web\_search

| Use `fetch_url` when...         | Use `web_search` when...                |
| ------------------------------- | --------------------------------------- |
| You have a specific URL         | You need to find relevant pages         |
| You need full page content      | You need snippets from multiple sources |
| Analyzing a particular document | Researching a broad topic               |
| Verifying specific claims       | Finding current news or events          |

### Effective Instructions

Guide the model on when to fetch URLs:

```python theme={null}
instructions = """You have access to web_search and fetch_url tools.

Use fetch_url when:
- You need detailed content from a specific URL
- You want to analyze a particular article or document
- You need to verify specific claims from a URL

Use web_search first to find URLs, then fetch_url to get full content."""
```

## Next Steps

<CardGroup>
  <Card title="Web Search" icon="magnifying-glass" href="/docs/grounded-llm/responses/tools/web-search">
    Search the web with filters and localization.
  </Card>

  <Card title="Function Calling" icon="code" href="/docs/grounded-llm/responses/tools/function-calling">
    Define custom functions for external integrations.
  </Card>

  <Card title="Presets" icon="gear" href="/docs/grounded-llm/responses/presets">
    Use pre-configured presets with built-in tools.
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/responses-post">
    View complete endpoint documentation.
  </Card>
</CardGroup>


# Function Calling
Source: https://docs.perplexity.ai/docs/grounded-llm/responses/tools/function-calling

Define custom functions that models can call to interact with external systems, databases, and APIs through the Agentic Research API.

## Overview

Function calling allows you to define custom functions that models can invoke during a conversation. Unlike the built-in tools (`web_search` and `fetch_url`), custom functions let you connect the model to your own systems—databases, APIs, business logic, or any external service.

<CardGroup>
  <Card title="Custom Integrations" icon="plug">
    Connect models to your databases, APIs, and internal systems.
  </Card>

  <Card title="Multi-Turn Pattern" icon="arrows-rotate">
    Model requests a function call, you execute it, then return results.
  </Card>
</CardGroup>

<Info>
  **Built-in vs Custom Tools:** Use `web_search` and `fetch_url` for web information retrieval. Use function calling when you need the model to interact with your own systems or perform custom operations.
</Info>

## How It Works

Function calling follows a multi-turn conversation pattern:

<Steps>
  <Step title="Define Functions">
    Specify the functions available to the model, including their names, descriptions, and parameter schemas.
  </Step>

  <Step title="Send Initial Request">
    Send your prompt along with the function definitions. The model decides if and when to call a function.
  </Step>

  <Step title="Receive Function Call">
    If the model needs to call a function, it returns a `function_call` item in the response output with the function name and arguments.
  </Step>

  <Step title="Execute the Function">
    Your code executes the actual function logic using the provided arguments.
  </Step>

  <Step title="Return Results">
    Send the function output back to the model as a `function_call_output` item.
  </Step>

  <Step title="Get Final Response">
    The model uses the function results to generate its final response.
  </Step>
</Steps>

## Defining Functions

Define functions using the `tools` parameter with `type: "function"`. Each function needs a name, description, and a JSON Schema for its parameters.

```python theme={null}
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name, e.g., 'San Francisco'"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Temperature unit"
                }
            },
            "required": ["location"]
        }
    }
]
```

### Function Schema Properties

| Property      | Type    | Required | Description                                                    |
| ------------- | ------- | -------- | -------------------------------------------------------------- |
| `type`        | string  | Yes      | Must be `"function"`                                           |
| `name`        | string  | Yes      | Function name the model will use to call it                    |
| `description` | string  | Yes      | Clear description of what the function does and when to use it |
| `parameters`  | object  | Yes      | JSON Schema defining the function's parameters                 |
| `strict`      | boolean | No       | Enable strict schema validation                                |

<Tip>
  Write clear, specific descriptions. The model uses these to decide when to call each function. Include details about what the function returns and any constraints.
</Tip>

### Strict Mode

Setting `strict: true` ensures function calls reliably adhere to your schema. When enabled, the model will always include all required parameters with the correct types.

```python theme={null}
{
    "type": "function",
    "name": "get_weather",
    "description": "Get weather for a location",
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City name"
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"]
            }
        },
        "required": ["location", "unit"],
        "additionalProperties": False
    }
}
```

When using strict mode:

* Set `additionalProperties: false` on your parameter object
* Mark all fields in `properties` as `required`
* Use `"type": ["string", "null"]` for optional fields that can be null

<Info>
  Strict mode is recommended for production applications where consistent function call structure is important.
</Info>

## Basic Example

Here's a complete example showing the full function calling flow:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  import json

  client = Perplexity()

  # 1. Define your function tools
  tools = [
      {
          "type": "function",
          "name": "get_horoscope",
          "description": "Get today's horoscope for an astrological sign.",
          "parameters": {
              "type": "object",
              "properties": {
                  "sign": {
                      "type": "string",
                      "description": "An astrological sign like Taurus or Aquarius"
                  }
              },
              "required": ["sign"]
          }
      }
  ]

  # Your actual function implementation
  def get_horoscope(sign: str) -> str:
      # In a real app, this might call an external API
      return f"{sign}: Today brings new opportunities for growth."

  # 2. Send initial request with tools
  response = client.responses.create(
      model="openai/gpt-5.2",
      tools=tools,
      input="What is my horoscope? I am an Aquarius."
  )

  # 3. Process the response and handle function calls
  next_input = [item.model_dump() for item in response.output]

  for item in response.output:
      if item.type == "function_call":
          # 4. Execute the function
          args = json.loads(item.arguments)
          result = get_horoscope(args["sign"])

          # 5. Add the function result to the input
          next_input.append({
              "type": "function_call_output",
              "call_id": item.call_id,
              "output": json.dumps({"horoscope": result})
          })

  # 6. Send the function results back to get the final response
  final_response = client.responses.create(
      model="openai/gpt-5.2",
      input=next_input
  )

  print(final_response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // 1. Define your function tools
  const tools = [
      {
          type: "function" as const,
          name: "get_horoscope",
          description: "Get today's horoscope for an astrological sign.",
          parameters: {
              type: "object",
              properties: {
                  sign: {
                      type: "string",
                      description: "An astrological sign like Taurus or Aquarius"
                  }
              },
              required: ["sign"]
          }
      }
  ];

  // Your actual function implementation
  function getHoroscope(sign: string): string {
      return `${sign}: Today brings new opportunities for growth.`;
  }

  // 2. Send initial request with tools
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      tools: tools,
      input: "What is my horoscope? I am an Aquarius."
  });

  // 3. Process the response and handle function calls
  const nextInput: any[] = response.output.map(item => ({ ...item }));

  for (const item of response.output) {
      if (item.type === "function_call") {
          // 4. Execute the function
          const args = JSON.parse(item.arguments);
          const result = getHoroscope(args.sign);

          // 5. Add the function result to the input
          nextInput.push({
              type: "function_call_output",
              call_id: item.call_id,
              output: JSON.stringify({ horoscope: result })
          });
      }
  }

  // 6. Send the function results back to get the final response
  const finalResponse = await client.responses.create({
      model: "openai/gpt-5.2",
      input: nextInput
  });

  console.log(finalResponse.output_text);
  ```

  ```bash cURL theme={null}
  # Step 1: Initial request with function tools
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What is my horoscope? I am an Aquarius.",
      "tools": [
        {
          "type": "function",
          "name": "get_horoscope",
          "description": "Get today'\''s horoscope for an astrological sign.",
          "parameters": {
            "type": "object",
            "properties": {
              "sign": {
                "type": "string",
                "description": "An astrological sign like Taurus or Aquarius"
              }
            },
            "required": ["sign"]
          }
        }
      ]
    }'

  # Step 2: After receiving a function_call, send the result back
  # (Replace call_id with the actual value from the response)
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": [
        {
          "type": "function_call",
          "call_id": "call_abc123",
          "name": "get_horoscope",
          "arguments": "{\"sign\": \"Aquarius\"}"
        },
        {
          "type": "function_call_output",
          "call_id": "call_abc123",
          "output": "{\"horoscope\": \"Aquarius: Today brings new opportunities for growth.\"}"
        }
      ]
    }'
  ```
</CodeGroup>

## Handling Function Calls

When the model decides to call a function, the response contains a `function_call` item in the `output` array:

```json theme={null}
{
  "output": [
    {
      "type": "function_call",
      "call_id": "call_abc123",
      "name": "get_horoscope",
      "arguments": "{\"sign\": \"Aquarius\"}"
    }
  ]
}
```

### Function Call Properties

| Property    | Description                                                     |
| ----------- | --------------------------------------------------------------- |
| `type`      | Always `"function_call"`                                        |
| `call_id`   | Unique identifier for this call—use this when returning results |
| `name`      | The function name the model is calling                          |
| `arguments` | JSON string containing the function arguments                   |

<Warning>
  The `arguments` field is a JSON string, not a parsed object. Always use `json.loads()` (Python) or `JSON.parse()` (JavaScript) to parse it.
</Warning>

## Returning Function Results

After executing the function, return the results using `function_call_output`:

```python theme={null}
{
    "type": "function_call_output",
    "call_id": "call_abc123",  # Must match the original call_id
    "output": "{\"horoscope\": \"Aquarius: Today brings new opportunities.\"}"
}
```

### Function Output Properties

| Property  | Description                                          |
| --------- | ---------------------------------------------------- |
| `type`    | Must be `"function_call_output"`                     |
| `call_id` | The `call_id` from the corresponding `function_call` |
| `output`  | JSON string containing the function's return value   |

<Tip>
  Structure your output as JSON for consistency. The model will parse and use this data to formulate its response.
</Tip>

## Multiple Functions

You can define multiple functions for the model to choose from:

<CodeGroup>
  ```python Python theme={null}
  tools = [
      {
          "type": "function",
          "name": "get_weather",
          "description": "Get current weather for a location.",
          "parameters": {
              "type": "object",
              "properties": {
                  "location": {"type": "string", "description": "City name"}
              },
              "required": ["location"]
          }
      },
      {
          "type": "function",
          "name": "get_stock_price",
          "description": "Get current stock price for a ticker symbol.",
          "parameters": {
              "type": "object",
              "properties": {
                  "ticker": {"type": "string", "description": "Stock ticker symbol"}
              },
              "required": ["ticker"]
          }
      }
  ]

  response = client.responses.create(
      model="openai/gpt-5.2",
      tools=tools,
      input="What's the weather in NYC and the current price of AAPL?"
  )

  # Handle each function call in the response
  for item in response.output:
      if item.type == "function_call":
          if item.name == "get_weather":
              # Execute weather function
              pass
          elif item.name == "get_stock_price":
              # Execute stock price function
              pass
  ```

  ```typescript TypeScript theme={null}
  const tools = [
      {
          type: "function" as const,
          name: "get_weather",
          description: "Get current weather for a location.",
          parameters: {
              type: "object",
              properties: {
                  location: { type: "string", description: "City name" }
              },
              required: ["location"]
          }
      },
      {
          type: "function" as const,
          name: "get_stock_price",
          description: "Get current stock price for a ticker symbol.",
          parameters: {
              type: "object",
              properties: {
                  ticker: { type: "string", description: "Stock ticker symbol" }
              },
              required: ["ticker"]
          }
      }
  ];

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      tools: tools,
      input: "What's the weather in NYC and the current price of AAPL?"
  });

  // Handle each function call in the response
  for (const item of response.output) {
      if (item.type === "function_call") {
          if (item.name === "get_weather") {
              // Execute weather function
          } else if (item.name === "get_stock_price") {
              // Execute stock price function
          }
      }
  }
  ```
</CodeGroup>

## Combining with Built-in Tools

You can use custom functions alongside built-in tools like `web_search`:

```python theme={null}
tools = [
    {"type": "web_search"},
    {
        "type": "function",
        "name": "save_to_database",
        "description": "Save information to the user's database.",
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "string", "description": "Data to save"}
            },
            "required": ["data"]
        }
    }
]

response = client.responses.create(
    model="openai/gpt-5.2",
    tools=tools,
    input="Search for the latest AI news and save a summary to my database.",
    instructions="Use web_search to find information, then save_to_database to store it."
)
```

## Best Practices

### Write Clear Descriptions

The model relies on function descriptions to decide when to call them. Be specific:

```python theme={null}
# Good - clear and specific
{
    "name": "get_user_orders",
    "description": "Retrieve a user's order history from the database. Returns the last 10 orders including order ID, date, items, and total amount. Use this when the user asks about their past purchases or order status."
}

# Less effective - vague
{
    "name": "get_orders",
    "description": "Gets orders."
}
```

### Define Precise Parameter Schemas

Use JSON Schema features to constrain parameters:

```python theme={null}
"parameters": {
    "type": "object",
    "properties": {
        "status": {
            "type": "string",
            "enum": ["pending", "shipped", "delivered"],
            "description": "Filter orders by status"
        },
        "limit": {
            "type": "integer",
            "minimum": 1,
            "maximum": 100,
            "default": 10,
            "description": "Number of orders to return"
        }
    },
    "required": ["status"]
}
```

### Handle Errors Gracefully

Return error information in a structured way:

```python theme={null}
try:
    result = execute_function(args)
    output = json.dumps({"success": True, "data": result})
except Exception as e:
    output = json.dumps({"success": False, "error": str(e)})

next_input.append({
    "type": "function_call_output",
    "call_id": item.call_id,
    "output": output
})
```

## Next Steps

<CardGroup>
  <Card title="Web Search" icon="magnifying-glass" href="/docs/grounded-llm/responses/tools/web-search">
    Use web\_search for real-time web information.
  </Card>

  <Card title="Fetch URL" icon="globe" href="/docs/grounded-llm/responses/tools/fetch-url">
    Extract content from specific URLs.
  </Card>

  <Card title="Structured Outputs" icon="code" href="/docs/grounded-llm/output-control/structured-outputs">
    Control response format with JSON schemas.
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/responses-post">
    View complete endpoint documentation.
  </Card>
</CardGroup>


# Tools Overview
Source: https://docs.perplexity.ai/docs/grounded-llm/responses/tools/overview

Extend model capabilities with built-in tools and custom functions in the Agentic Research API.

## Overview

The Agentic Research API provides tools that extend model capabilities beyond their training data. Tools must be explicitly configured in your API request—once enabled, models autonomously decide when to use them based on your instructions.

<CardGroup>
  <Card title="web_search" icon="magnifying-glass" href="/docs/grounded-llm/responses/tools/web-search">
    Perform web searches with filtering by domain, language, recency, and date range.
  </Card>

  <Card title="fetch_url" icon="globe" href="/docs/grounded-llm/responses/tools/fetch-url">
    Fetch and extract content from specific URLs.
  </Card>

  <Card title="Function Calling" icon="code" href="/docs/grounded-llm/responses/tools/function-calling">
    Define custom functions to connect models to your own systems and APIs.
  </Card>
</CardGroup>

## Built-in vs Custom Tools

| Type         | Tools                     | Use Case                                   |
| ------------ | ------------------------- | ------------------------------------------ |
| **Built-in** | `web_search`, `fetch_url` | Real-time web information retrieval        |
| **Custom**   | Your functions            | Connect to databases, APIs, business logic |

## Quick Example

Enable tools by adding them to the `tools` array in your request:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest AI developments?",
      tools=[
          {"type": "web_search"},
          {"type": "fetch_url"}
      ],
      instructions="Use web_search for current information. Use fetch_url when you need full article content."
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest AI developments?",
      tools: [
          { type: "web_search" },
          { type: "fetch_url" }
      ],
      instructions: "Use web_search for current information. Use fetch_url when you need full article content."
  });

  console.log(response.output_text);
  ```
</CodeGroup>

## Pricing

| Tool             | Cost                                        |
| ---------------- | ------------------------------------------- |
| `web_search`     | \$5.00 per 1,000 calls                      |
| `fetch_url`      | \$0.50 per 1,000 calls                      |
| Function Calling | No additional cost (standard token pricing) |

<Info>
  You're also charged for tokens consumed when tool results are embedded in the model's context. See the [Pricing page](/docs/getting-started/pricing) for full details.
</Info>

## Next Steps

<CardGroup>
  <Card title="Web Search" icon="magnifying-glass" href="/docs/grounded-llm/responses/tools/web-search">
    Learn about search filters and localization options.
  </Card>

  <Card title="Fetch URL" icon="globe" href="/docs/grounded-llm/responses/tools/fetch-url">
    Extract content from specific web pages.
  </Card>

  <Card title="Function Calling" icon="code" href="/docs/grounded-llm/responses/tools/function-calling">
    Define custom functions for external integrations.
  </Card>

  <Card title="Presets" icon="gear" href="/docs/grounded-llm/responses/presets">
    Use pre-configured presets with built-in tools.
  </Card>
</CardGroup>


# Web Search
Source: https://docs.perplexity.ai/docs/grounded-llm/responses/tools/web-search

Perform web searches with advanced filtering options using the web_search tool in the Agentic Research API.

## Overview

The `web_search` tool allows models to perform web searches with all the filtering capabilities of the [Search API](/docs/search/quickstart). Use it when you need current information, news, or data beyond the model's training cutoff.

## Pricing

Web search costs **\$5.00 per 1,000 search calls** (\$0.005 per search). You're also charged for tokens consumed when search results are embedded in the model's context.

<Accordion title="Cost Example">
  If a model makes 3 web searches and receives 1,800 tokens of search results, plus your original 100-token query, using `openai/gpt-5.2`:

  | Component     | Calculation              | Cost           |
  | ------------- | ------------------------ | -------------- |
  | Tool calls    | 3 searches × \$0.005     | \$0.015        |
  | Input tokens  | 1,900 tokens × \$1.75/1M | \$0.003325     |
  | Output tokens | 300 tokens × \$14.00/1M  | \$0.0042       |
  | **Total**     |                          | **\$0.022525** |
</Accordion>

## Basic Usage

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest developments in quantum computing?",
      tools=[
          {
              "type": "web_search"
          }
      ],
      instructions="You have access to a web_search tool. Use it for current information."
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest developments in quantum computing?",
      tools: [
          {
              type: "web_search"
          }
      ],
      instructions: "You have access to a web_search tool. Use it for current information."
  });

  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest developments in quantum computing?",
      "tools": [
        {
          "type": "web_search"
        }
      ],
      "instructions": "You have access to a web_search tool. Use it for current information."
    }' | jq
  ```
</CodeGroup>

## Search Filters

Configure filters in the `filters` object within the tool definition.

| Filter                       | Type             | Description                                                         | Limit            |
| ---------------------------- | ---------------- | ------------------------------------------------------------------- | ---------------- |
| `search_domain_filter`       | Array of strings | Filter by specific domains (allowlist or denylist with `-` prefix)  | Max 20 domains   |
| `search_language_filter`     | Array of strings | Filter by ISO 639-1 language codes                                  | Max 10 languages |
| `search_recency_filter`      | String           | Filter by time period: `"day"`, `"week"`, `"month"`, `"year"`       | -                |
| `search_after_date`          | String           | Filter results published after this date (format: `"M/D/YYYY"`)     | -                |
| `search_before_date`         | String           | Filter results published before this date (format: `"M/D/YYYY"`)    | -                |
| `last_updated_after_filter`  | String           | Filter results last updated after this date (format: `"M/D/YYYY"`)  | -                |
| `last_updated_before_filter` | String           | Filter results last updated before this date (format: `"M/D/YYYY"`) | -                |

### Domain Filtering

Filter search results to specific trusted sources:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest climate change findings?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_domain_filter": [
                      "nature.com",
                      "science.org",
                      ".gov",
                      ".edu"
                  ]
              }
          }
      ],
      instructions="Use web_search to find recent academic and governmental sources."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest climate change findings?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_domain_filter: [
                      "nature.com",
                      "science.org",
                      ".gov",
                      ".edu"
                  ]
              }
          }
      ],
      instructions: "Use web_search to find recent academic and governmental sources."
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest climate change findings?",
      "tools": [
        {
          "type": "web_search",
          "filters": {
            "search_domain_filter": ["nature.com", "science.org", ".gov", ".edu"]
          }
        }
      ],
      "instructions": "Use web_search to find recent academic and governmental sources."
    }' | jq
  ```
</CodeGroup>

<Tip>
  Use `-` prefix to exclude domains: `"-reddit.com"` excludes Reddit from results.
</Tip>

### Language Filtering

Search across specific languages:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are European perspectives on AI regulation?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_language_filter": ["en", "fr", "de", "es"]
              }
          }
      ],
      instructions="Search for content in English, French, German, and Spanish."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are European perspectives on AI regulation?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_language_filter: ["en", "fr", "de", "es"]
              }
          }
      ],
      instructions: "Search for content in English, French, German, and Spanish."
  });
  ```
</CodeGroup>

### Recency Filtering

Filter by time period for recent information:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest tech industry layoffs?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_recency_filter": "week"
              }
          }
      ],
      instructions="Search for news from the past week only."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest tech industry layoffs?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_recency_filter: "week"
              }
          }
      ],
      instructions: "Search for news from the past week only."
  });
  ```
</CodeGroup>

### Date Range Filtering

Filter by specific publication dates:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What happened in AI during Q1 2025?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_after_date_filter": "1/1/2025",
                  "search_before_date_filter": "3/31/2025"
              }
          }
      ],
      instructions="Search for content published in Q1 2025."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What happened in AI during Q1 2025?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_after_date_filter: "1/1/2025",
                  search_before_date_filter: "3/31/2025"
              }
          }
      ],
      instructions: "Search for content published in Q1 2025."
  });
  ```
</CodeGroup>

### Combining Filters

Combine multiple filters for precise control:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are recent academic findings on renewable energy?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_domain_filter": ["nature.com", "science.org", ".edu"],
                  "search_language_filter": ["en"],
                  "search_recency_filter": "month"
              }
          }
      ],
      instructions="Search for recent English-language academic publications."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are recent academic findings on renewable energy?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_domain_filter: ["nature.com", "science.org", ".edu"],
                  search_language_filter: ["en"],
                  search_recency_filter: "month"
              }
          }
      ],
      instructions: "Search for recent English-language academic publications."
  });
  ```
</CodeGroup>

## User Location

Configure user location for localized search results:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are local news headlines?",
      tools=[
          {
              "type": "web_search",
              "user_location": {
                  "latitude": 37.7749,
                  "longitude": -122.4194,
                  "country": "US",
                  "city": "San Francisco",
                  "region": "CA"
              }
          }
      ],
      instructions="Search for local news in the San Francisco area."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are local news headlines?",
      tools: [
          {
              type: "web_search",
              user_location: {
                  latitude: 37.7749,
                  longitude: -122.4194,
                  country: "US",
                  city: "San Francisco",
                  region: "CA"
              }
          }
      ],
      instructions: "Search for local news in the San Francisco area."
  });
  ```
</CodeGroup>

### Location Properties

| Property    | Type   | Description                     |
| ----------- | ------ | ------------------------------- |
| `latitude`  | number | Latitude coordinate             |
| `longitude` | number | Longitude coordinate            |
| `country`   | string | ISO 3166-1 alpha-2 country code |
| `city`      | string | City name                       |
| `region`    | string | State/province/region code      |

## Token Control

Control the amount of content retrieved per search result using `max_tokens_per_page`:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Summarize recent AI breakthroughs",
      tools=[
          {
              "type": "web_search",
              "max_tokens_per_page": 1024
          }
      ],
      instructions="Search and summarize concisely."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Summarize recent AI breakthroughs",
      tools: [
          {
              type: "web_search",
              max_tokens_per_page: 1024
          }
      ],
      instructions: "Search and summarize concisely."
  });
  ```
</CodeGroup>

<Tip>
  Lower `max_tokens_per_page` to reduce context token costs, especially when you need brief summaries rather than full content.
</Tip>

## Best Practices

### Effective Instructions

Guide the model on when and how to search:

```python theme={null}
instructions = """You have access to a web_search tool.

Use web_search when:
- You need current information or recent news
- The query requires multiple sources
- You need to find specific domains or publications

Keep searches focused: use 2-5 word queries for best results."""
```

### Cost Management

* Use specific filters to narrow results and reduce unnecessary searches
* Set `max_tokens_per_page` to control token costs
* Combine filters to get relevant results in fewer calls

## Next Steps

<CardGroup>
  <Card title="Fetch URL" icon="globe" href="/docs/grounded-llm/responses/tools/fetch-url">
    Extract full content from specific URLs.
  </Card>

  <Card title="Function Calling" icon="code" href="/docs/grounded-llm/responses/tools/function-calling">
    Define custom functions for external integrations.
  </Card>

  <Card title="Search API" icon="magnifying-glass" href="/docs/search/quickstart">
    Learn more about search capabilities.
  </Card>

  <Card title="Domain Filters Guide" icon="filter" href="/docs/grounded-llm/filters/domain-filters">
    Advanced domain filtering techniques.
  </Card>
</CardGroup>


# Changelog
Source: https://docs.perplexity.ai/docs/resources/changelog



<Tip>
  Looking ahead? Check out our [Feature Roadmap](/docs/resources/feature-roadmap) to see what's coming next.
</Tip>

<Update label="December 2025">
  **Model Deprecation: `sonar-reasoning` Removed**

  As of December 15, 2025, the `sonar-reasoning` model has been deprecated and removed from the API. If you were using this model, we recommend migrating to `sonar-reasoning-pro` for enhanced multi-step reasoning capabilities with web search.

  **New: Media Classifier for Intelligent Visual Content**

  We're excited to introduce the **Media Classifier** — an intelligent system that automatically detects when your queries would benefit from visual content and includes relevant images or videos in responses.

  **Key capabilities:**

  * **Automatic detection**: Analyzes queries to identify when visual content adds value
  * **Smart media selection**: Intelligently chooses between images, videos, or both based on query type
  * **Context-aware**: Perfect for educational content, geographic queries, processes, and demonstrations
  * **Configurable control**: Enable/disable and override media types as needed

  Available exclusively with `sonar-pro`, the Media Classifier enhances responses for visual concepts, locations, step-by-step processes, and educational content. [Learn more →](/docs/grounded-llm/chat-completions/media/media-classifier)

  **Search API Enhancements**

  We've made several improvements to the Search API:

  * **New `max_tokens` parameter**: Control the maximum tokens extracted per page in search results. This gives you finer control over response size and costs. [Learn more →](/docs/search/quickstart)
  * **`last_updated_filter` support**: Filter search results by when content was last updated, in addition to publication date. Perfect for finding the most current information. [Learn more →](/docs/search/filters/date-time-filters)
  * **Vercel AI SDK Support**: The Search API is now compatible with the Vercel AI SDK, allowing you to build with Perplexity in a framework-agnostic way. [Learn more →](https://ai-sdk.dev/tools-registry/perplexity-search)

  **Ecosystem & Community**

  New community showcase: [**Perplexity Client**](/docs/cookbook/showcase/perplexity-client) — An Electron-based desktop application with advanced API parameter controls, custom spaces, and API debugging mode. Built by the community for developers who want fine-grained control over their Sonar interactions.
</Update>

<Update label="November 2025">
  **Pro Search: Now Generally Available**

  We're excited to announce the general availability of **Pro Search** for Sonar Pro! Pro Search enhances your queries with automated tool usage, enabling multi-step reasoning through intelligent tool orchestration.

  **Key capabilities:**

  * **Multi-step reasoning**: The model automatically performs multiple web searches and fetches URL content to answer complex queries
  * **Real-time thought streaming**: Watch the model's reasoning process as it works through your question
  * **Automatic classification**: Use `search_type: "auto"` to let the system intelligently route queries based on complexity
  * **Built-in tools**: Access `web_search` and `fetch_url_content` tools that the model uses automatically

  Learn more about Pro Search in our [Pro Search Quickstart](/docs/grounded-llm/chat-completions/pro-search/quickstart) guide.

  **MCP Server: One-Click Installation**

  The [Perplexity MCP Server](/docs/getting-started/integrations/mcp-server) now supports **one-click installation** for popular AI development environments:

  * **Cursor**: Click to auto-configure the Perplexity MCP server
  * **VS Code**: One-click setup via the VS Code MCP extension
  * **Claude Desktop & Claude Code**: Easy JSON configuration

  The MCP server provides four powerful tools: `perplexity_search`, `perplexity_ask`, `perplexity_research`, and `perplexity_reason` — enabling AI assistants to access Perplexity's search and reasoning capabilities directly.
</Update>

<Update label="October 2025">
  **Official Perplexity SDKs**

  We're thrilled to announce the official **Perplexity SDKs** for Python and TypeScript/JavaScript! These SDKs provide convenient, type-safe access to all Perplexity APIs with both synchronous and asynchronous clients.

  **Installation:**

  ```bash theme={null}
  # Python
  pip install perplexityai

  # TypeScript/JavaScript  
  npm install @perplexity-ai/perplexity_ai
  ```

  **Features:**

  * Full type definitions for all request parameters and response fields
  * Support for Chat Completions and Search APIs
  * Streaming support with async iterators
  * Automatic environment variable handling for API keys

  Get started with our [SDK Quickstart Guide](/docs/sdk/overview) and explore the [Chat Completions Guide](/docs/grounded-llm/chat-completions/quickstart) for detailed usage examples.

  **Interactive Search API Playground**

  Test Search API queries and parameters in real time with our new [Interactive Playground](https://perplexity.ai/account/api/playground/search) — **no API key required** to get started. Experiment with filtering options, see response structures, and refine your queries before implementing them in code.

  **New Search API Capabilities**

  * **`language_preference`**: Specify preferred languages for search results (available for `sonar` and `sonar-pro`)
  * **`search_domain_filter`**: Filter results to specific domains for more targeted searches
  * **Date/time filters**: Enhanced control over result freshness with publication and update filters
    **Ecosystem & Community**

  New community showcase: [**StarPlex**](/docs/cookbook/showcase/starplex) — An AI-powered startup intelligence platform featuring an interactive 3D globe interface. Built with Sonar Pro, it helps entrepreneurs validate business ideas by mapping competitors, VCs, and market opportunities worldwide. Featured at recent hackathon events!
</Update>

<Update label="September 2025">
  **New: File Attachments Support**

  You can now upload and analyze documents in multiple formats using Sonar models! This powerful new feature supports PDF, DOC, DOCX, TXT, and RTF files, allowing you to ask questions, extract information, and get summaries from your documents.

  **Key capabilities:**

  * **Document Analysis**: Ask questions about document content and get detailed answers
  * **Content Extraction**: Pull out key information, data points, and insights
  * **Multi-format Support**: Work with PDF, Word documents, text files, and Rich Text Format
  * **Large Document Handling**: Process lengthy documents efficiently
  * **Multi-language Support**: Analyze documents in various languages

  Upload documents either via publicly accessible URLs using the `file_url` content type, similar to our existing image upload functionality.

  Get started with our comprehensive [File Attachments Guide](/docs/grounded-llm/chat-completions/media/file-attachments).
</Update>

<Update label="September 2025">
  **New: Search-only API**

  Introducing our standalone Search API that provides direct access to search results without LLM processing! This new endpoint gives you raw, ranked search results from Perplexity's continuously refreshed index.

  **Perfect for:**

  * Building custom search experiences
  * Integrating search results into your own applications
  * Creating specialized workflows that need search data without AI responses
  * Applications requiring just the search functionality

  **Key features:**

  * Direct access to Perplexity's search index
  * All existing search filters and controls
  * Faster responses since no LLM processing is involved
  * Same powerful filtering options (domain, date range, academic sources, etc.)

  This complements our existing chat completions API and gives developers more flexibility in how they use Perplexity's search capabilities.

  Learn more in our [Search API documentation](/docs/search/quickstart).
</Update>

<Update label="September 2025">
  **New: API Key Rotation Mechanism**

  We've introduced a comprehensive API key rotation system to enhance security and simplify key management for your applications.

  **Key features:**

  * **Seamless Rotation**: Replace API keys without service interruption
  * **Automated Workflows**: Set up automatic key rotation schedules
  * **Enhanced Security**: Regularly refresh keys to minimize security risks
  * **Audit Trail**: Track key usage and rotation history
  * **Zero Downtime**: Smooth transitions between old and new keys

  **How it works:**

  1. Generate a new API key while keeping the old one active
  2. Update your applications to use the new key
  3. Deactivate the old key once migration is complete

  This is particularly valuable for production environments where continuous availability is critical, and for organizations with strict security compliance requirements.

  **Best practices:**

  * Rotate keys every 30-90 days depending on your security requirements
  * Use environment variables to manage keys in your applications
  * Test key rotation in staging environments first
  * Monitor key usage to ensure successful transitions

  Access key rotation features through your [API Portal](https://perplexity.ai/account/api).
</Update>

<Update label="August 2025">
  **API model deprecation notice**

  Please note that as of August 1, 2025, R1-1776 will be removed from the available models.

  R1 has been a popular option for a while, but it hasn't kept pace with recent improvements and lacks support for newer features. To reduce engineering overhead and make room for more capable models, we're retiring it from the API.

  If you liked R1's strengths, we recommend switching to `Sonar Pro Reasoning`. It offers similar behavior with stronger overall performance.
</Update>

<Update label="July 2025">
  **New: Detailed Cost Information in API Responses**

  The API response JSON now includes detailed cost information for each request.

  You'll now see a new structure like this in your response:

  ```json theme={null}
  "usage": {
      "prompt_tokens": 8,
      "completion_tokens": 439,
      "total_tokens": 447,
      "search_context_size": "low",
      "cost": {
       "input_tokens_cost": 2.4e-05,
       "output_tokens_cost": 0.006585,
       "request_cost": 0.006,
       "total_cost": 0.012609
     }
  }
  ```

  **What's included:**

  * **input\_tokens\_cost**: Cost attributed to input tokens
  * **output\_tokens\_cost**: Cost attributed to output tokens
  * **request\_cost**: Fixed cost per request
  * **total\_cost**: The total cost for this API call

  This update enables easier tracking of usage and billing directly from each API response, giving you complete transparency into the costs associated with each request.
</Update>

<Update label="July 2025">
  **New: SEC Filings Filter for Financial Research**

  We're excited to announce the release of our new SEC filings filter feature, allowing you to search specifically within SEC regulatory documents and filings. By setting `search_domain: "sec"` in your API requests, you can now focus your searches on official SEC documents, including 10-K reports, 10-Q quarterly reports, 8-K current reports, and other regulatory filings.

  This feature is particularly valuable for:

  * Financial analysts researching company fundamentals
  * Investment professionals conducting due diligence
  * Compliance officers tracking regulatory changes
  * Anyone requiring authoritative financial information directly from official sources

  The SEC filter works seamlessly with other search parameters like date filters and search context size, giving you precise control over your financial research queries.

  **Example:**

  ```bash theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header 'accept: application/json' \
    --header 'authorization: Bearer YOUR_API_KEY' \
    --header 'content-type: application/json' \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "What was Apple's revenue growth in their latest quarterly report?"}],
      "stream": false,
      "search_domain": "sec",
      "web_search_options": {"search_context_size": "medium"}
  }' | jq
  ```

  For detailed documentation and implementation examples, please see our [SEC Guide](https://docs.perplexity.ai/guides/sec-guide).
</Update>

<Update label="June 2025">
  **Enhanced: Date Range Filtering with Latest Updated Field**

  We've enhanced our date range filtering capabilities with new fields that give you even more control over search results based on content freshness and updates.

  **New fields available:**

  * `latest_updated`: Filter results based on when the webpage was last modified or updated
  * `published_after`: Filter by original publication date (existing)
  * `published_before`: Filter by original publication date (existing)

  The `latest_updated` field is particularly useful for:

  * Finding the most current version of frequently updated content
  * Ensuring you're working with the latest data from news sites, blogs, and documentation
  * Tracking changes and updates to specific web resources over time

  **Example:**

  ```bash theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header 'accept: application/json' \
    --header 'authorization: Bearer YOUR_API_KEY' \
    --header 'content-type: application/json' \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "What are the latest developments in AI research?"}],
      "stream": false,
      "web_search_options": {
        "latest_updated": "2025-06-01",
        "search_context_size": "medium"
      }
  }'
  ```

  For comprehensive documentation and more examples, please see our [Date Range Filter Guide](https://docs.perplexity.ai/guides/date-range-filter-guide).
</Update>

<Update label="June 2025">
  **New: Academic Filter for Scholarly Research**
  We're excited to announce the release of our new academic filter feature, allowing you to tailor your searches specifically to academic and scholarly sources. By setting `search_mode: "academic"` in your API requests, you can now prioritize results from peer-reviewed papers, journal articles, and research publications.

  This feature is particularly valuable for:

  * Students and researchers working on academic papers
  * Professionals requiring scientifically accurate information
  * Anyone seeking research-based answers instead of general web content

  The academic filter works seamlessly with other search parameters like `search_context_size` and date filters, giving you precise control over your research queries.

  **Example:**

  ```bash theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header 'accept: application/json' \
    --header 'authorization: Bearer YOUR_API_KEY' \
    --header 'content-type: application/json' \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "What is the scientific name of the lions mane mushroom?"}],
      "stream": false,
      "search_mode": "academic",
      "web_search_options": {"search_context_size": "low"}
  }'
  ```

  For detailed documentation and implementation examples, please see our [Academic Filter Guide](https://docs.perplexity.ai/guides/academic-filter-guide).
</Update>

<Update label="May 2025">
  **New: Reasoning Effort Parameter for Sonar Deep Research**

  We're excited to announce our new reasoning effort feature for sonar-deep-research. This lets you control how much computational effort the AI dedicates to each query. You can choose from "low", "medium", or "high" to get faster, simpler answers or deeper, more thorough responses.

  This feature has a direct impact on the amount of reasoning tokens consumed for each query, giving you the ability to control costs while balancing between speed and thoroughness.

  **Options:**

  * `"low"`: Faster, simpler answers with reduced token usage
  * `"medium"`: Balanced approach (default)
  * `"high"`: Deeper, more thorough responses with increased token usage

  **Example:**

  ```bash theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header 'accept: application/json' \
    --header 'authorization: Bearer ${PPLX_KEY}' \
    --header 'content-type: application/json' \
    --data '{
      "model": "sonar-deep-research",
      "messages": [{"role": "user", "content": "What should I know before markets open today?"}],
      "stream": true,
      "reasoning_effort": "low"
    }'
  ```

  For detailed documentation and implementation examples, please see:
  [Sonar Deep Research Documentation](https://docs.perplexity.ai/models/models/sonar-deep-research)
</Update>

<Update label="May 2025">
  **New: Asynchronous API for Sonar Deep Research**

  We're excited to announce the addition of an asynchronous API for Sonar Deep Research, designed specifically for research-intensive tasks that may take longer to process.

  This new API allows you to submit requests and retrieve results later, making it ideal for complex research queries that require extensive processing time.

  The asynchronous API endpoints include:

  1. `GET https://api.perplexity.ai/async/chat/completions` - Lists all asynchronous chat completion requests for the authenticated user
  2. `POST https://api.perplexity.ai/async/chat/completions` - Creates an asynchronous chat completion job
  3. `GET https://api.perplexity.ai/async/chat/completions/{request_id}` - Retrieves the status and result of a specific asynchronous chat completion job

  **Note:** Async requests have a time-to-live (TTL) of 7 days. After this period, the request and its results will no longer be accessible.

  For detailed documentation and implementation examples, please see:
  [Sonar Deep Research Documentation](https://docs.perplexity.ai/models/models/sonar-deep-research)
</Update>

<Update label="May 2025">
  **Enhanced API Responses with Search Results**

  We've improved our API responses to give you more visibility into search data by adding a new `search_results` field to the JSON response object.

  This enhancement provides direct access to the search results used by our models, giving you more transparency and control over the information being used to generate responses.

  The `search_results` field includes:

  * `title`: The title of the search result page
  * `url`: The URL of the search result
  * `date`: The publication date of the content

  **Example:**

  ```json theme={null}
  "search_results": [
    {
      "title": "Understanding Large Language Models",
      "url": "https://example.com/llm-article",
      "date": "2023-12-25"
    },
    {
      "title": "Advances in AI Research",
      "url": "https://example.com/ai-research",
      "date": "2024-03-15"
    }
  ]
  ```

  This update makes it easier to:

  * Verify the sources used in generating responses
  * Create custom citation formats for your applications
  * Filter or prioritize certain sources based on your needs

  **Update: The `citations` field has been fully deprecated and removed.** All applications should now use the `search_results` field, which provides more detailed information including titles, URLs, and publication dates.

  The `search_results` field is available across all our search-enabled models and offers enhanced source tracking capabilities.
</Update>

<Update label="April 2025">
  **New API Portal for Organization Management**

  We are excited to announce the release of our new API portal, designed to help you better manage your organization and API usage.

  With this portal, you can:

  * Organize and manage your API keys more effectively.
  * Gain insights into your API usage and team activity.
  * Streamline collaboration within your organization.

  Check it out here:\
  [https://www.perplexity.ai/account/api/group](https://www.perplexity.ai/account/api/group)
</Update>

<Update label="April 2025">
  **New: Location filtering in search**

  Looking to narrow down your search results based on users' locations?\
  We now support user location filtering, allowing you to retrieve results only from a particular user location.

  Check out the [guide](https://docs.perplexity.ai/guides/user-location-filter-guide).
</Update>

<Update label="April 2025">
  **Image uploads now available for all users!**

  You can now upload images to Sonar and use them as part of your multimodal search experience.\
  Give it a try by following our image upload guide:\
  [https://docs.perplexity.ai/guides/image-attachments](https://docs.perplexity.ai/guides/image-attachments)
</Update>

<Update label="April 2025">
  **New: Date range filtering in search**

  Looking to narrow down your search results to specific dates?\
  We now support date range filtering, allowing you to retrieve results only from a particular timeframe.

  Check out the guide:\
  [https://docs.perplexity.ai/guides/date-range-filter-guide](https://docs.perplexity.ai/guides/date-range-filter-guide)
</Update>

<Update label="April 2025">
  **Clarified: Search context pricing update**

  We've fully transitioned to our new pricing model: citation tokens are no longer charged.\
  If you were already using the `search_context_size` parameter, you've been on this model already.

  This change makes pricing simpler and cheaper for everyone — with no downside.

  View the updated pricing:\
  [https://docs.perplexity.ai/guides/pricing](https://docs.perplexity.ai/guides/pricing)
</Update>

<Update label="April 2025">
  **All features now available to everyone**

  We've removed all feature gating based on tiered spending. These were previously only available to users of Tier 3 and above.

  That means **every user now has access to all API capabilities**, regardless of usage volume or spend. Rate limits are still applicable.\
  Whether you're just getting started or scaling up, you get the full power of Sonar out of the box.
</Update>

<Update label="March 2025">
  **Structured Outputs Available for All Users**

  We're excited to announce that structured outputs are now available to all Perplexity API users, regardless of tier level. Based on valuable feedback from our developer community, we've removed the previous Tier 3 requirement for this feature.

  **What's available now:**

  * JSON structured outputs are supported across all models

  This change allows developers to create more reliable and consistent applications from day one. We believe in empowering our community with the tools they need to succeed, and we're committed to continuing to improve accessibility to our advanced features.

  Thank you for your feedback—it helps us make Perplexity API better for everyone.
</Update>

<Update label="March 2025">
  **Improved Sonar Models: New Search Modes**

  We're excited to announce significant improvements to our Sonar models that deliver superior performance at lower costs. Our latest benchmark testing confirms that Sonar and Sonar Pro now outperform leading competitors while maintaining more affordable pricing.

  Key updates include:

  * **Three new search modes** across most Sonar models:
    * High: Maximum depth for complex queries
    * Medium: Balanced approach for moderate complexity
    * Low: Cost-efficient for straightforward queries (equivalent to current pricing)

  * **Simplified billing structure**:
    * Transparent pricing for input/output tokens
    * No charges for citation tokens in responses (except for Sonar Deep Research)

  The current billing structure will be supported as the default option for 30 days (until April 18, 2025). During this period, the new search modes will be available as opt-in features.

  **Important Note:** After April 18, 2025, Sonar Pro and Sonar Reasoning Pro will not return Citation tokens or number of search results in the usage field in the API response.
</Update>

<Update label="January 2025">
  **API model deprecation notice**

  Please note that as of February 22, 2025, several models and model name aliases will no longer be accessible. The following model names will no longer be available via API:

  `llama-3.1-sonar-small-128k-online`

  `llama-3.1-sonar-large-128k-online`

  `llama-3.1-sonar-huge-128k-online`

  We recommend updating your applications to use our recently released Sonar or Sonar Pro models – you can learn more about them here. Thank you for being a Perplexity API user.
</Update>

<Update label="January 2025">
  **Build with Perplexity's new APIs**

  We are expanding API offerings with the most efficient and cost-effective search solutions available:  **Sonar** and **Sonar Pro**.

  **Sonar** gives you fast, straightforward answers

  **Sonar Pro** tackles complex questions that need deeper research and provides more sources

  Both models offer built-in citations, automated scaling of rate limits, and public access to advanced features like structured outputs and search domain filters. And don't worry, we never train on your data. Your information stays yours.

  You can learn more about our new APIs here - [http://sonar.perplexity.ai/](http://sonar.perplexity.ai/)
</Update>

<Update label="November 2024">
  **Citations Public Release and Increased Default Rate Limits**

  We are excited to announce the public availability of citations in the Perplexity API. In addition, we have also increased our default rate limit for the sonar online models to 50 requests/min for all users.

  Effective immediately, all API users will see citations returned as part of their requests by default. This is not a breaking change. The **return\_citations** parameter will no longer have any effect.

  If you have any questions or need assistance, feel free to reach out to our team at [api@perplexity.ai](mailto:api@perplexity.ai)
</Update>

<Update label="July 2024">
  **Introducing New and Improved Sonar Models**

  We are excited to announce the launch of our latest Perplexity Sonar models:

  **Online Models** -
  `llama-3.1-sonar-small-128k-online`
  `llama-3.1-sonar-large-128k-online`

  **Chat Models** -
  `llama-3.1-sonar-small-128k-chat`
  `llama-3.1-sonar-large-128k-chat`

  These new additions surpass the performance of the previous iteration. For detailed information on our supported models, please visit our model card documentation.

  **\[Action Required]** Model Deprecation Notice
  Please note that several models will no longer be accessible effective 8/12/2024. We recommend updating your applications to use models in the Llama-3.1 family immediately.

  The following model names will no longer be available via API -
  `llama-3-sonar-small-32k-online`
  `llama-3-sonar-large-32k-online`
  `llama-3-sonar-small-32k-chat`
  `llama-3-sonar-large-32k-chat`
  `llama-3-8b-instruct`
  `llama-3-70b-instruct`
  `mistral-7b-instruct`
  `mixtral-8x7b-instruct`

  We recommend switching to models in the Llama-3.1 family:

  **Online Models** -
  `llama-3.1-sonar-small-128k-online`
  `llama-3.1-sonar-large-128k-online`

  **Chat Models** -
  `llama-3.1-sonar-small-128k-chat`
  `llama-3.1-sonar-large-128k-chat`

  **Instruct Models** -
  `llama-3.1-70b-instruct`
  `llama-3.1-8b-instruct`

  If you have any questions, please email [support@perplexity.ai](mailto:support@perplexity.ai).
  Thank you for being a Perplexity API user.

  Stay curious,

  Team Perplexity
</Update>

***

<Update label="April 2024">
  **Model Deprecation Notice**

  Please note that as of May 14, several models and model name aliases will no longer be accessible. We recommend updating your applications to use models in the Llama-3 family immediately. The following model names will no longer be available via API:

  `codellama-70b-instruct`
  `mistral-7b-instruct`
  `mixtral-8x22b-instruct`
  `pplx-7b-chat`
  `pplx-7b-online`
</Update>


# Get in Touch
Source: https://docs.perplexity.ai/docs/resources/discussions



## Join Our Developer Community

<Card title="🌟 Community Forum - Your First Stop!" icon="users">
  **The heart of our developer ecosystem!** Our vibrant community forum is where thousands of developers connect, share ideas, get help, and showcase their amazing projects built with the Perplexity API.

  **[🚀 Join the Community Forum →](https://community.perplexity.ai/)**

  **Why join the forum?**

  * Get technical help from experienced developers and our team
  * Share your projects and get featured in our showcase
  * Access exclusive tutorials, code examples, and best practices
  * Connect with like-minded builders and potential collaborators
  * Stay updated on the latest API features and announcements
</Card>

<CardGroup>
  <Card title="Real-Time Chat" icon="comments">
    Join our Discord community for instant help and casual conversations with fellow developers.

    * [Discord Community](https://discord.gg/perplexity-ai) - Real-time chat & support
    * Active community members ready to help
    * Quick answers to urgent questions
  </Card>

  <Card title="Stay Connected" icon="bell">
    Follow us for the latest updates, feature announcements, and developer spotlights.

    * [Follow @PPLXDevs](https://twitter.com/PPLXDevs) - Latest updates & announcements
    * Developer showcases and success stories
    * API tips and best practices
  </Card>
</CardGroup>

## Contact Our Team

<CardGroup>
  <Card title="Sales & Enterprise" icon="briefcase">
    Interested in enterprise solutions, custom pricing, or have sales questions?

    **[Contact Sales Team →](https://pplx.ai/api-sales)**
  </Card>

  <Card title="Technical Support" icon="headset">
    Need technical assistance? Our support team is here to help.

    <Warning>
      **Please try the [Community Forum](https://community.perplexity.ai/) first!**

      You'll get faster responses from our active community and team members who monitor the forum regularly.
    </Warning>

    * **Email**: [api@perplexity.ai](mailto:api@perplexity.ai) - For billing inquiries and account issues
  </Card>
</CardGroup>

## Developer Resources

<Steps>
  <Step title="Report Issues">
    Found a bug? Help us improve! Submit detailed bug reports through our [Community Forum](https://community.perplexity.ai/). Create a new post with the `Bug Reports` tag.
  </Step>

  <Step title="Share Your Work">
    Built something amazing with the Perplexity API? We'd love to showcase your work!

    * Contribute to our [API Cookbook](https://github.com/perplexityai/api-cookbook)
    * Share on X/Twitter with [@PPLXDevs](https://twitter.com/PPLXDevs)
    * Present at our monthly developer showcase
  </Step>

  <Step title="Get Featured">
    Exceptional projects may be featured in our newsletter, blog, social media channels, and our [Cookbook Community Showcase](/docs/cookbook/showcase/briefo). Let us amplify your work to thousands of developers and AI enthusiasts!
  </Step>
</Steps>


# Frequently Asked Questions
Source: https://docs.perplexity.ai/docs/resources/faq



<AccordionGroup>
  <Accordion title="Why isn't the `response_format` parameter working for reasoning models?">
    The `sonar-reasoning-pro` model is designed to output a `<think>` section containing reasoning tokens, immediately followed by a valid JSON object. As a result, the `response_format` parameter does not remove these reasoning tokens from the output.

    We recommend using a custom parser to extract the valid JSON portion. An example implementation can be found [here](https://github.com/ppl-ai/api-discussion/blob/main/utils/extract_json_reasoning_models.py).
  </Accordion>

  <Accordion title="Does the API use content filtering or SafeSearch?">
    Yes, for the API, content filtering in the form of SafeSearch is turned on by default. This helps filter out potentially offensive and inappropriate content, including pornography, from search results. SafeSearch is an automated filter that works across search results to provide a safer experience. You can learn more about SafeSearch on the [official Wikipedia page](https://en.wikipedia.org/wiki/SafeSearch).
  </Accordion>

  <Accordion title="How do I file a bug report and what happens afterward?">
    To file a bug report, please use our GitHub repository and file the bug in [issues](https://github.com/ppl-ai/api-discussion/issues). Once you've submitted your report, we kindly ask that you share the link to the issue with us via email at [api@perplexity.ai](mailto:api@perplexity.ai) so we can track it on our end.

    We truly appreciate your patience, and we'll get back to you as soon as possible. Due to the current volume of reports, it may take a little time for us to respond—but rest assured, we're on it.
  </Accordion>

  <Accordion title="Where are Perplexity's language models hosted?">
    Our compute is hosted via Amazon Web Services in North America. By default, the API has zero day retention of user prompt data, which is never used for AI training.
  </Accordion>

  <Accordion title="How can I upgrade to the next usage tier?">
    The only way for an account to be upgraded to the next usage tier is through all-time credit purchase.

    Here are the spending criteria associated with each tier:

    | Tier   | Credit Purchase (all time) |
    | ------ | -------------------------- |
    | Tier 0 | -                          |
    | Tier 1 | \$50                       |
    | Tier 2 | \$250                      |
    | Tier 3 | \$500                      |
    | Tier 4 | \$1000                     |
    | Tier 5 | \$5000                     |
  </Accordion>

  <Accordion title="How can I track my spend/usage per API key?">
    We offer a way to track your billing per API key. You can do this by navigating to the following location:

    **Settings > View Dashboard > Invoice history > Invoices**

    Then click on any invoice and each item from the total bill will have a code at the end of it (e.g., pro (743S)). Those 4 characters are the last 4 of your API key.
  </Accordion>

  <Accordion title="How do I request a new feature?">
    A Feature Request is a suggestion to improve or add new functionality to the Perplexity Sonar API, such as:

    * Requesting support for a new model or capability (e.g., image processing, fine-tuning options)
    * Asking for new API parameters (e.g., additional filters, search options)
    * Suggesting performance improvements (e.g., faster response times, better citation handling)
    * Enhancing existing API features (e.g., improving streaming reliability, adding new output formats)

    If your request aligns with these, please submit a feature request here: [Github Feature requests](https://github.com/ppl-ai/api-discussion/issues)
  </Accordion>

  <Accordion title="Why are the results from the API different from the UI? ">
    1. The API uses the same search system as the UI with differences in configuration—so their outputs may differ.
    2. The underlying AI model might differ between the API and the UI for a given query.
  </Accordion>

  <Accordion title="Will user data submitted through the API be used for model training or other purposes?">
    We collect the following types of information:

    **API Usage Data:** We collect billable usage metadata such as the number of requests and tokens. You can view your own usage in the [Perplexity API dashboard](https://perplexity.ai/settings/api).

    **User Account Information:** When you create an account with us, we collect your name, email address, and other relevant contact information.

    We do not retain any query data sent through the API and do not train on any of your data.
  </Accordion>

  <Accordion title="Does the API currently support web browsing?">
    Yes, the [Sonar Models](https://docs.perplexity.ai/guides/model-cards) leverage information from Perplexity's search index and the public internet.
  </Accordion>

  <Accordion title="What are the limitations to the number of API calls?">
    You can find our [rate limits here](https://docs.perplexity.ai/guides/usage-tiers).
  </Accordion>

  <Accordion title="What's the best way to stay up to date with API updates?">
    We email users about new developments and also post in the [changelog](changelog/changelog).
  </Accordion>

  <Accordion title="How should I respond to 401: Authorization errors?">
    401 error codes indicate that the provided API key is invalid, deleted, or belongs to an account which ran out of credits. You likely need to purchase more credits in the [Perplexity API dashboard](https://perplexity.ai/settings/api). You can avoid this issue by configuring auto-top-up.
  </Accordion>

  <Accordion title="Do you support fine-tuning?">
    Currently, we do not support fine-tuning.
  </Accordion>

  <Accordion title="I have another question or an issue">
    Please reach out to [api@perplexity.ai](mailto:api@perplexity.ai) or [support@perplexity.ai](mailto:support@perplexity.ai) for other API inquiries. You can also post on our [discussion forum](https://github.com/ppl-ai/api-discussion/discussions) and we will get back to you.
  </Accordion>

  <Accordion title="Does Perplexity provide service quality assurances such as service uptime, frequency of failures, and target recovery time in the event of a failure?">
    We do not guarantee this at the moment.
  </Accordion>

  <Accordion title="Do you expose CoTs if I use your reasoning APIs or Deep Research API?">
    We expose the CoTs for Sonar Reasoning Pro. We don't currently expose the CoTs for Deep Research.
  </Accordion>

  <Accordion title="Are the reasoning tokens in Deep Research same as CoTs in the answer?">
    Reasoning tokens in Deep Research are a bit different than the CoTs in the answer—these tokens are used to reason through the research material before generating the final output via the CoTs.
  </Accordion>

  <Accordion title="Is the internet data access provided by the API identical to that of Perplexity's web interface?">
    Yes, the API offers exactly the same internet data access as Perplexity's web platform.
  </Accordion>

  <Accordion title="To what extent is the API OpenAI compatible?">
    The Perplexity API is designed to be broadly compatible with OpenAI's chat completions endpoint. It adopts a similar structure—including fields such as `id`, `model`, and `usage`—and supports analogous parameters like `model`, `messages`, and `stream`.

    **Key Differences from the standard OpenAI response include:**

    * **Response Object Structure:**
      * OpenAI responses typically have an `object` value of `"chat.completion"` and a `created` timestamp, whereas our response uses `object: "response"` and a `created_at` field.
      * Instead of a `choices` array, our response content is provided under an `output` array that contains detailed message objects.

    * **Message Details:**
      * Each message in our output includes a `type` (usually `"message"`), a unique `id`, and a `status`.
      * The actual text is nested within a `content` array that contains objects with `type`, `text`, and an `annotations` array for additional context.

    * **Additional Fields:**
      * Our API response provides extra meta-information (such as `status`, `error`, `instructions`, and `max_output_tokens`) that are not present in standard OpenAI responses.
      * The `usage` field also differs, offering detailed breakdowns of input and output tokens (including fields like `input_tokens_details` and `output_tokens_details`).

    These differences are intended to provide enhanced functionality and additional context while maintaining broad compatibility with OpenAI's API design.
  </Accordion>
</AccordionGroup>


# API Roadmap
Source: https://docs.perplexity.ai/docs/resources/feature-roadmap

Upcoming features and improvements for the Perplexity API designed to enhance your development experience.

Our roadmap is shaped by our users - have a feature in mind? Submit your suggestion [here](https://community.perplexity.ai/) and help us build the future of AI together.

<AccordionGroup>
  <Accordion title="V2 Chat Completions Migration" description="An improvement to your existing API">
    We're migrating the Chat Completions API to a new v2 endpoint with significantly improved performance:

    * **Same Endpoint**: The `/v2/chat/completions` endpoint maintains full compatibility with the existing API contract
    * **Reduced Latency**: Approximately 40% lower latency compared to the current endpoint
    * **Automatic Migration**: Traffic from v1 will automatically be moved to v2 - this change is seamless and no action needs to be taken

    This migration will provide faster response times while maintaining full backward compatibility with your existing integrations.
  </Accordion>

  <Accordion title="Embeddings API" description="A new API for vector embeddings and semantic search">
    We're introducing an Embeddings API to enable semantic search and retrieval capabilities:

    * **Text Embeddings**: Generate high-quality vector embeddings from text input
    * **Semantic Search**: Build applications that can find and retrieve information based on meaning and context
    * **RAG Applications**: Power retrieval-augmented generation workflows with custom knowledge bases

    This API will enable you to build sophisticated search and retrieval applications that understand semantic relationships between content.
  </Accordion>

  <Accordion title="Video Upload Capabilities" description="Multimodal video processing">
    We're expanding our multimodal capabilities to include video uploads.

    This feature will enable:

    * **Video Content Analysis**: Upload and analyze video files directly through the API
    * **Frame-by-Frame Processing**: Extract insights from video content at multiple time points
    * **Visual Scene Understanding**: Analyze visual elements, objects, and activities in video content
    * **Multimodal Search**: Search for information based on both visual and audio elements from your uploaded videos

    Supported formats will include common video file types (MP4, MOV, AVI) with reasonable file size limits for API efficiency.

    This capability will unlock new use cases in content moderation, educational analysis, media research, and automated video summarization.
  </Accordion>

  <Accordion title="File Search & Connectors" description="Expanded data access">
    Expanding your ability to access and process information:

    * **File Repository Integration**: Query file repositories tied to your API organization
    * **Multi-format File Search**: Search across various file types (PDFs, documents, spreadsheets)
    * **External Data Source Integration**: Connect to external data stores and databases
    * **Enterprise Connector Parity**: Full feature parity with enterprise connector capabilities

    This feature will allow your applications to tap into a broader range of data sources for more comprehensive insights, enabling you to build applications that can search and analyze your organization's entire knowledge base.
  </Accordion>

  <Accordion title="Expanded Structured Outputs Support" description="Enhanced response formatting">
    We're expanding our structured outputs capabilities:

    * **Universal JSON Support**: JSON structured outputs are now available for all models across all tiers
    * **Advanced Schema Validation**: Enhanced validation options for more reliable structured data
    * **Output Templates**: Pre-defined templates for common use cases

    This expansion will make it easier to build applications that require consistent, structured data from our API responses.
  </Accordion>

  <Accordion title="Documentation Overhaul" description="More comprehensive resources">
    We're committed to making our documentation a truly exceptional resource:

    * **Improved Layout**: Optimized structure for better self-serve workflows
    * **Consistent Design**: Unified branding between our landing page and documentation
    * **Enhanced Content**: Revised explanations for better developer understanding
    * **Vertical-Specific Guides**: Specialized documentation for publishers, merchants, and other industry partners
    * **High-Fidelity Demos**: More comprehensive examples beyond our basic cookbook demos
    * **Comprehensive Prompt Guide**: In-depth resources to help you build effectively with our search + LLM API
    * **API Selection Guides**: Clear guidance on which API is best suited for specific scenarios

    These improvements will help you get up to speed faster and make the most of our API capabilities.
  </Accordion>

  <Accordion title="Increased Rate Limits" description="Support for high-volume applications">
    We're scaling our infrastructure to support significantly higher request volumes:

    * **Enterprise-Scale Rate Limits**: Supporting use cases up to 100K requests per minute
    * **High-Growth Startup Support**: Designed specifically for rapidly scaling applications
    * **Infrastructure Reliability**: Enhanced stability and reduced latency spikes under high load
    * **Regional Scaling**: Expanded infrastructure deployment for global applications

    This enhancement will ensure our API can grow alongside your application's user base and processing needs, supporting everything from high-growth startups to enterprise-scale deployments.
  </Accordion>

  <Accordion title="Better Error Handling" description="Clearer troubleshooting">
    Improving our error framework:

    * More descriptive error messages
    * Clearer guidance on resolving common issues

    This will reduce debugging time and help you understand and address issues more efficiently.
  </Accordion>

  <Accordion title="Multimedia Capabilities" description="Beyond text processing">
    Broadening the types of content you can work with:

    * **URL Content Integration**: Specify URLs within prompts to search for and analyze content from specific web pages directly
    * **Advanced URL Parsing**: Extract and analyze content from web pages with enhanced accuracy and context understanding
    * **Web Page Analysis**: Deep content extraction including text, images, and structured data from URLs
    * **Real-time Web Content**: Access to live web content for dynamic analysis and research

    These features will enable new use cases and richer interactions within your applications, allowing you to reference specific web content and build more comprehensive research workflows with real-time web data integration.
  </Accordion>

  <Accordion title="Context Management / Memory" description="Improved context handling">
    We're addressing the limitations of managing context in API calls by introducing new context management features.

    Key improvements include:

    * **Efficient Context Storage**: Avoid appending responses from previous API calls to new ones, reducing the risk of exceeding context windows.
    * **Session-Based Memory**: Enable session-based memory to maintain context across multiple API calls without manual intervention.

    These enhancements will make it easier to build applications that require persistent context without hitting technical limitations.
  </Accordion>

  <Accordion title="Pro Search Public Release" description="Advanced agentic capabilities for all">
    We're preparing to make Pro Search available to all API users:

    * **Multi-step Reasoning**: Access to the advanced agentic research capabilities currently in beta
    * **Dynamic Tool Execution**: Automated web searches, URL content fetching, and Python code execution
    * **Intelligent Classification**: Automatic determination of when to use pro search vs fast search based on query complexity
    * **Transparent Reasoning**: Real-time streaming of the model's thought process and tool usage

    This will unlock sophisticated research workflows and enable your applications to handle complex, multi-dimensional queries that require computational analysis and deep web research.
  </Accordion>

  <Accordion title="Voice-to-Voice API" description="Real-time audio interactions">
    Introducing voice-based interactions through our API:

    * **Real-time Voice Processing**: Direct voice input and audio response generation
    * **Natural Conversation Flow**: Maintain context across voice interactions
    * **Multi-language Support**: Voice capabilities across multiple languages
    * **Low-latency Streaming**: Optimized for real-time voice applications

    This capability will enable voice assistants, interactive applications, and hands-free interfaces that can search and reason about information through natural speech.
  </Accordion>

  <Accordion title="Finance Tools Integration" description="Financial data and analysis">
    Expanding our capabilities with specialized financial tools:

    * **Market Data Access**: Real-time and historical stock prices, market indicators
    * **Ticker Symbol Lookup**: Intelligent company and symbol resolution
    * **Financial Analysis Tools**: Price history, trend analysis, and market insights
    * **SEC Filing Integration**: Enhanced search and analysis of financial documents

    These tools will enable sophisticated financial applications, trading platforms, and investment research tools with access to comprehensive financial data and analysis capabilities.
  </Accordion>

  <Accordion title="Labs Features via API" description="Experimental capabilities">
    Bringing cutting-edge experimental features to the API:

    * **Early Access Features**: Test new capabilities before general release
    * **Advanced Model Variants**: Access to experimental model configurations
    * **Prototype Integrations**: Early versions of upcoming integrations and tools
    * **Developer Feedback Integration**: Direct influence on feature development through testing

    This will give developers early access to innovative features and the opportunity to shape the future direction of our API capabilities.
  </Accordion>

  <Accordion title="Enhanced Third-Party Integrations" description="Seamless ecosystem connectivity">
    Expanding our integration ecosystem:

    * **Agentic Framework Support**: Enhanced integrations with LangChain, LlamaIndex, and other AI frameworks
    * **Developer Platform Integration**: Native support for popular development environments
    * **Workflow Automation**: Integration with automation platforms and CI/CD pipelines
    * **Real-time Collaboration**: Enhanced tooling for team-based development

    These integrations will make it easier to incorporate our API into your existing development workflows and build more sophisticated AI applications.
  </Accordion>

  <Accordion title="Developer Analytics Dashboard" description="Comprehensive usage insights">
    Advanced analytics and monitoring for your API usage:

    * **Query Analysis**: Detailed insights into query patterns, types, and performance
    * **Usage Metrics**: Comprehensive tracking of API calls, response times, and success rates
    * **Error Monitoring**: Detailed error tracking and debugging information
    * **Performance Optimization**: Insights to help optimize your application's API usage
    * **Cost Management**: Detailed billing breakdowns and usage forecasting

    This dashboard will provide the visibility you need to optimize your applications, manage costs, and understand user behavior patterns.
  </Accordion>
</AccordionGroup>

## Timeline and Availability

This roadmap represents our current development priorities. Features will be released incrementally, with some becoming available in the coming months and others planned for later in the year.

We'll announce new feature availability through our [changelog](/docs/resources/changelog) and via email notifications to API users.


# Perplexity Crawlers
Source: https://docs.perplexity.ai/docs/resources/perplexity-crawlers

We strive to improve our service every day by delivering the best search experience possible. To achieve this, we collect data using web crawlers ("robots") and user agents that gather and index information from the internet, operating either automatically or in response to user requests. Webmasters can use the following robots.txt tags to manage how their sites and content interact with Perplexity. Each setting works independently, and it may take up to 24 hours for our systems to reflect changes.

| User Agent      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PerplexityBot   | `PerplexityBot` is designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models. To ensure your site appears in search results, we recommend allowing `PerplexityBot` in your site's `robots.txt` file and permitting requests from our published IP ranges listed below.<br /><br />Full user-agent string: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`<br /><br />Published IP addresses: [https://www.perplexity.com/perplexitybot.json](https://www.perplexity.com/perplexitybot.json)                                                                                                                                        |
| Perplexity‑User | `Perplexity-User` supports user actions within Perplexity. When users ask Perplexity a question, it might visit a web page to help provide an accurate answer and include a link to the page in its response. `Perplexity-User` controls which sites these user requests can access. It is not used for web crawling or to collect content for training AI foundation models.<br /><br />Full user-agent string: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)`<br /><br />Published IP addresses: [https://www.perplexity.com/perplexity-user.json](https://www.perplexity.com/perplexity-user.json)<br /><br />Since a user requested the fetch, this fetcher generally ignores robots.txt rules. |

## WAF Configuration

If you're using a Web Application Firewall (WAF) to protect your site, you may need to explicitly whitelist Perplexity's bots to ensure they can access your content. Below are configuration guidelines for popular WAF providers.

### Cloudflare WAF

To configure Cloudflare WAF to allow Perplexity bots:

<Steps>
  <Step title="Navigate to WAF settings">
    In your Cloudflare dashboard, go to **Security** → **WAF**.
  </Step>

  <Step title="Create a new rule">
    Click on **Custom rules** and create a new rule to allow Perplexity bots.
  </Step>

  <Step title="Configure rule conditions">
    Set up a rule that combines both User-Agent and IP address conditions:

    * **Field**: User Agent
    * **Operator**: Contains
    * **Value**: `PerplexityBot` OR `Perplexity-User`

    **AND**

    * **Field**: IP Source Address
    * **Operator**: Is in
    * **Value**: Use the IP ranges from the official endpoints listed below
  </Step>

  <Step title="Set rule action">
    Set the action to **Allow** to ensure these requests bypass other security rules.
  </Step>
</Steps>

### AWS WAF

For AWS WAF configuration, create IP sets and string match conditions:

<Steps>
  <Step title="Create IP sets">
    In the AWS WAF console, create IP sets for both PerplexityBot and Perplexity-User using the IP addresses from the official endpoints listed below.
  </Step>

  <Step title="Create string match conditions">
    Create string match conditions for the User-Agent headers:

    * `PerplexityBot`
    * `Perplexity-User`
  </Step>

  <Step title="Create allow rules">
    Create rules that combine the IP sets with the corresponding User-Agent strings, and set the action to **Allow**.
  </Step>

  <Step title="Associate with Web ACL">
    Associate these rules with your Web ACL and ensure they have higher priority than blocking rules.
  </Step>
</Steps>

### IP Address Sources

<Warning>
  Always use the most current IP ranges from the official JSON endpoints. These addresses are updated regularly and should be the source of truth for your WAF configurations.
</Warning>

* **PerplexityBot IP addresses**: [https://www.perplexity.com/perplexitybot.json](https://www.perplexity.com/perplexitybot.json)
* **Perplexity-User IP addresses**: [https://www.perplexity.com/perplexity-user.json](https://www.perplexity.com/perplexity-user.json)

<Tip>
  Set up automated processes to periodically fetch and update your WAF rules with the latest IP ranges from these endpoints to ensure continuous access for Perplexity bots.
</Tip>

### Best Practices

<Tip>
  When configuring WAF rules for Perplexity bots, combine both User-Agent string matching and IP address verification for enhanced security while ensuring legitimate bot traffic can access your content.
</Tip>

<Note>
  Changes to WAF configurations may take some time to propagate. Monitor your logs to ensure the rules are working as expected and that legitimate Perplexity bot traffic is being allowed through.
</Note>


# Privacy & Security
Source: https://docs.perplexity.ai/docs/resources/privacy-security

Learn about Perplexity's data privacy, retention policies, and security certifications for API users

## Data Privacy & Retention

### Zero Data Retention Policy

Perplexity maintains a strict **Zero Data Retention Policy** for the Sonar API. We do not retain any data sent via the Sonar API, and we absolutely do not use any customer data to train our models or for any other purposes beyond processing your immediate request.

### Data We Collect

The only data we collect through the Sonar API consists of essential billable metrics required for service operation:

* Number of tokens processed
* Model used for each request
* Request timestamp and duration
* API key identification (for billing purposes)

This billing metadata does not include any content from your prompts, responses, or other user data.

## Security Certifications & Compliance

Perplexity is compliant with industry-leading security standards and certifications:

### Current Certifications

<Check>
  **[SOC 2 Type II Report](https://trust.perplexity.ai/)** - Comprehensive security controls audit covering security, availability, processing integrity, confidentiality, and privacy
</Check>

<Check>
  **[2025 HIPAA Gap Assessment](https://trust.perplexity.ai/)** - Healthcare data protection compliance evaluation
</Check>

<Check>
  **[CAIQlite](https://trust.perplexity.ai/)** - Cloud security assessment questionnaire demonstrating cloud security posture
</Check>

## Additional Security Information

For comprehensive details about our security measures, infrastructure protection, and compliance frameworks, visit our dedicated security portal:

<Card title="Perplexity Trust Center" icon="shield-check" href="https://trust.perplexity.ai/">
  Access detailed security documentation, compliance reports, and transparency information
</Card>

<Info>
  All security measures and certifications are regularly updated and maintained to ensure the highest standards of data protection and service security.
</Info>


# System Status
Source: https://docs.perplexity.ai/docs/resources/status



You can check the status of our services [here](https://status.perplexity.com/).

If you experience any issues or have any questions, please contact us at [api@perplexity.ai](mailto:api@perplexity.ai) or flag a bug report in our [Discord](https://discord.com/invite/perplexity-ai) channel.


# Best Practices
Source: https://docs.perplexity.ai/docs/sdk/best-practices

Learn best practices for using the Perplexity SDKs in production, including environment variables, rate limiting, security, and efficient request patterns.

## Overview

This guide covers essential best practices for using the Perplexity SDKs in production environments. Following these practices will help you build robust, secure, and efficient applications.

## Security Best Practices

### Environment Variables

Always store API keys securely using environment variables:

<Steps>
  <Step title="Use environment variables">
    Store API keys in environment variables, never in source code.

    <CodeGroup>
      ```python Python theme={null}
      import os
      from perplexity import Perplexity

      # Good: Use environment variables
      client = Perplexity(
          api_key=os.environ.get("PERPLEXITY_API_KEY")
      )

      # Bad: Never hardcode API keys
      # client = Perplexity(api_key="pplx-abc123...")  # DON'T DO THIS
      ```

      ```typescript TypeScript/JavaScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Good: Use environment variables
      const client = new Perplexity({
          apiKey: process.env.PERPLEXITY_API_KEY
      });

      // Bad: Never hardcode API keys
      // const client = new Perplexity({
      //     apiKey: "pplx-abc123..."  // DON'T DO THIS
      // });
      ```
    </CodeGroup>

    <Warning>
      Never commit API keys to version control. Use .env files locally and secure environment variable management in production.
    </Warning>
  </Step>

  <Step title="Use .env files for local development">
    Create a `.env` file for local development (add it to .gitignore).

    ```bash .env theme={null}
    PERPLEXITY_API_KEY=your_api_key_here
    PERPLEXITY_MAX_RETRIES=3
    PERPLEXITY_TIMEOUT=30000
    ```

    <CodeGroup>
      ```python Python theme={null}
      from dotenv import load_dotenv
      import os
      from perplexity import Perplexity

      # Load environment variables from .env file
      load_dotenv()

      client = Perplexity(
          api_key=os.getenv("PERPLEXITY_API_KEY"),
          max_retries=int(os.getenv("PERPLEXITY_MAX_RETRIES", "3"))
      )
      ```

      ```typescript TypeScript/JavaScript theme={null}
      import dotenv from 'dotenv';
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Load environment variables from .env file
      dotenv.config();

      const client = new Perplexity({
          apiKey: process.env.PERPLEXITY_API_KEY,
          maxRetries: parseInt(process.env.PERPLEXITY_MAX_RETRIES || '3')
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Validate environment variables">
    Check for required environment variables at startup.

    <CodeGroup>
      ```python Python theme={null}
      import os
      import sys
      from perplexity import Perplexity

      def create_client():
          api_key = os.getenv("PERPLEXITY_API_KEY")
          if not api_key:
              print("Error: PERPLEXITY_API_KEY environment variable is required")
              sys.exit(1)
          
          return Perplexity(api_key=api_key)

      client = create_client()
      ```

      ```typescript TypeScript/JavaScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      function createClient(): Perplexity {
          const apiKey = process.env.PERPLEXITY_API_KEY;
          if (!apiKey) {
              console.error("Error: PERPLEXITY_API_KEY environment variable is required");
              process.exit(1);
          }
          
          return new Perplexity({ apiKey });
      }

      const client = createClient();
      ```
    </CodeGroup>
  </Step>
</Steps>

### API Key Rotation

Implement secure API key rotation:

<CodeGroup>
  ```python Python theme={null}
  import os
  import logging
  from perplexity import Perplexity
  from typing import Optional

  class SecurePerplexityClient:
      def __init__(self, primary_key: Optional[str] = None, fallback_key: Optional[str] = None):
          self.primary_key = primary_key or os.getenv("PERPLEXITY_API_KEY")
          self.fallback_key = fallback_key or os.getenv("PERPLEXITY_API_KEY_FALLBACK")
          self.current_client = Perplexity(api_key=self.primary_key)
          self.logger = logging.getLogger(__name__)
      
      def _switch_to_fallback(self):
          """Switch to fallback API key if available"""
          if self.fallback_key:
              self.logger.warning("Switching to fallback API key")
              self.current_client = Perplexity(api_key=self.fallback_key)
              return True
          return False
      
      def search(self, query: str, **kwargs):
          try:
              return self.current_client.search.create(query=query, **kwargs)
          except Exception as e:
              if "authentication" in str(e).lower() and self._switch_to_fallback():
                  return self.current_client.search.create(query=query, **kwargs)
              raise e

  # Usage
  client = SecurePerplexityClient()
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class SecurePerplexityClient {
      private primaryKey: string;
      private fallbackKey?: string;
      private currentClient: Perplexity;
      
      constructor(primaryKey?: string, fallbackKey?: string) {
          this.primaryKey = primaryKey || process.env.PERPLEXITY_API_KEY!;
          this.fallbackKey = fallbackKey || process.env.PERPLEXITY_API_KEY_FALLBACK;
          this.currentClient = new Perplexity({ apiKey: this.primaryKey });
      }
      
      private switchToFallback(): boolean {
          if (this.fallbackKey) {
              console.warn("Switching to fallback API key");
              this.currentClient = new Perplexity({ apiKey: this.fallbackKey });
              return true;
          }
          return false;
      }
      
      async search(query: string, options?: any) {
          try {
              return await this.currentClient.search.create({ query, ...options });
          } catch (error: any) {
              if (error.message.toLowerCase().includes('authentication') && this.switchToFallback()) {
                  return await this.currentClient.search.create({ query, ...options });
              }
              throw error;
          }
      }
  }

  // Usage
  const client = new SecurePerplexityClient();
  ```
</CodeGroup>

## Rate Limiting and Efficiency

### Intelligent Rate Limiting

Implement exponential backoff with jitter:

<CodeGroup>
  ```python Python theme={null}
  import time
  import random
  import asyncio
  from typing import TypeVar, Callable, Any
  import perplexity
  from perplexity import Perplexity

  T = TypeVar('T')

  class RateLimitedClient:
      def __init__(self, client: Perplexity, max_retries: int = 5):
          self.client = client
          self.max_retries = max_retries
      
      def _calculate_delay(self, attempt: int) -> float:
          """Calculate delay with exponential backoff and jitter"""
          base_delay = 2 ** attempt
          jitter = random.uniform(0.1, 0.5)
          return min(base_delay + jitter, 60.0)  # Cap at 60 seconds
      
      def with_retry(self, func: Callable[[], T]) -> T:
          """Execute function with intelligent retry logic"""
          last_exception = None
          
          for attempt in range(self.max_retries):
              try:
                  return func()
              except perplexity.RateLimitError as e:
                  last_exception = e
                  if attempt < self.max_retries - 1:
                      delay = self._calculate_delay(attempt)
                      print(f"Rate limited. Retrying in {delay:.2f}s (attempt {attempt + 1})")
                      time.sleep(delay)
                      continue
                  raise e
              except perplexity.APIConnectionError as e:
                  last_exception = e
                  if attempt < self.max_retries - 1:
                      delay = min(2 ** attempt, 10.0)  # Shorter delay for connection errors
                      print(f"Connection error. Retrying in {delay:.2f}s")
                      time.sleep(delay)
                      continue
                  raise e
          
          raise last_exception
      
      def search(self, query: str, **kwargs):
          return self.with_retry(
              lambda: self.client.search.create(query=query, **kwargs)
          )

  # Usage
  client = RateLimitedClient(Perplexity())
  result = client.search("artificial intelligence")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class RateLimitedClient {
      private client: Perplexity;
      private maxRetries: number;
      
      constructor(client: Perplexity, maxRetries: number = 5) {
          this.client = client;
          this.maxRetries = maxRetries;
      }
      
      private calculateDelay(attempt: number): number {
          const baseDelay = 2 ** attempt * 1000; // Convert to milliseconds
          const jitter = Math.random() * 500; // 0-500ms jitter
          return Math.min(baseDelay + jitter, 60000); // Cap at 60 seconds
      }
      
      async withRetry<T>(func: () => Promise<T>): Promise<T> {
          let lastError: any;
          
          for (let attempt = 0; attempt < this.maxRetries; attempt++) {
              try {
                  return await func();
              } catch (error: any) {
                  lastError = error;
                  
                  if (error.constructor.name === 'RateLimitError') {
                      if (attempt < this.maxRetries - 1) {
                          const delay = this.calculateDelay(attempt);
                          console.log(`Rate limited. Retrying in ${delay}ms (attempt ${attempt + 1})`);
                          await new Promise(resolve => setTimeout(resolve, delay));
                          continue;
                      }
                  } else if (error.constructor.name === 'APIConnectionError') {
                      if (attempt < this.maxRetries - 1) {
                          const delay = Math.min(2 ** attempt * 1000, 10000);
                          console.log(`Connection error. Retrying in ${delay}ms`);
                          await new Promise(resolve => setTimeout(resolve, delay));
                          continue;
                      }
                  }
                  
                  throw error;
              }
          }
          
          throw lastError;
      }
      
      async search(query: string, options?: any) {
          return this.withRetry(() => 
              this.client.search.create({ query, ...options })
          );
      }
  }

  // Usage
  const client = new RateLimitedClient(new Perplexity());
  const result = await client.search("artificial intelligence");
  ```
</CodeGroup>

### Request Batching

Efficiently batch multiple requests:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from typing import List, TypeVar, Generic
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  T = TypeVar('T')

  class BatchProcessor(Generic[T]):
      def __init__(self, batch_size: int = 5, delay_between_batches: float = 1.0):
          self.batch_size = batch_size
          self.delay_between_batches = delay_between_batches
      
      async def process_batch(
          self, 
          items: List[str], 
          process_func: Callable[[str], Awaitable[T]]
      ) -> List[T]:
          """Process items in batches with rate limiting"""
          results = []
          
          for i in range(0, len(items), self.batch_size):
              batch = items[i:i + self.batch_size]
              
              # Process batch concurrently
              tasks = [process_func(item) for item in batch]
              batch_results = await asyncio.gather(*tasks, return_exceptions=True)
              
              # Filter out exceptions and collect results
              for result in batch_results:
                  if not isinstance(result, Exception):
                      results.append(result)
              
              # Delay between batches
              if i + self.batch_size < len(items):
                  await asyncio.sleep(self.delay_between_batches)
          
          return results

  # Usage
  async def main():
      processor = BatchProcessor(batch_size=3, delay_between_batches=0.5)
      
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          
          async def search_query(query: str):
              return await client.search.create(query=query)
          
          queries = ["AI", "ML", "DL", "NLP", "CV"]
          results = await processor.process_batch(queries, search_query)
          
          print(f"Processed {len(results)} successful queries")

  asyncio.run(main())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class BatchProcessor<T> {
      constructor(
          private batchSize: number = 5,
          private delayBetweenBatches: number = 1000
      ) {}
      
      async processBatch<R>(
          items: T[],
          processFunc: (item: T) => Promise<R>
      ): Promise<R[]> {
          const results: R[] = [];
          
          for (let i = 0; i < items.length; i += this.batchSize) {
              const batch = items.slice(i, i + this.batchSize);
              
              // Process batch concurrently
              const tasks = batch.map(item => 
                  processFunc(item).catch(error => error)
              );
              const batchResults = await Promise.all(tasks);
              
              // Filter out exceptions and collect results
              for (const result of batchResults) {
                  if (!(result instanceof Error)) {
                      results.push(result);
                  }
              }
              
              // Delay between batches
              if (i + this.batchSize < items.length) {
                  await new Promise(resolve => 
                      setTimeout(resolve, this.delayBetweenBatches)
                  );
              }
          }
          
          return results;
      }
  }

  // Usage
  async function main() {
      const processor = new BatchProcessor<string>(3, 500);
      const client = new Perplexity();
      
      const searchQuery = (query: string) => 
          client.search.create({ query });
      
      const queries = ["AI", "ML", "DL", "NLP", "CV"];
      const results = await processor.processBatch(queries, searchQuery);
      
      console.log(`Processed ${results.length} successful queries`);
  }

  main();
  ```
</CodeGroup>

## Production Configuration

### Configuration Management

Use environment-based configuration for different deployment stages:

<CodeGroup>
  ```python Python theme={null}
  import os
  from dataclasses import dataclass
  from typing import Optional
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  @dataclass
  class PerplexityConfig:
      api_key: str
      max_retries: int = 3
      timeout_seconds: float = 30.0
      max_connections: int = 100
      max_keepalive: int = 20
      environment: str = "production"
      
      @classmethod
      def from_env(cls) -> "PerplexityConfig":
          """Load configuration from environment variables"""
          api_key = os.getenv("PERPLEXITY_API_KEY")
          if not api_key:
              raise ValueError("PERPLEXITY_API_KEY environment variable is required")
          
          return cls(
              api_key=api_key,
              max_retries=int(os.getenv("PERPLEXITY_MAX_RETRIES", "3")),
              timeout_seconds=float(os.getenv("PERPLEXITY_TIMEOUT", "30.0")),
              max_connections=int(os.getenv("PERPLEXITY_MAX_CONNECTIONS", "100")),
              max_keepalive=int(os.getenv("PERPLEXITY_MAX_KEEPALIVE", "20")),
              environment=os.getenv("ENVIRONMENT", "production")
          )
      
      def create_client(self) -> Perplexity:
          """Create optimized client based on configuration"""
          timeout = httpx.Timeout(
              connect=5.0,
              read=self.timeout_seconds,
              write=10.0,
              pool=10.0
          )
          
          limits = httpx.Limits(
              max_keepalive_connections=self.max_keepalive,
              max_connections=self.max_connections,
              keepalive_expiry=60.0 if self.environment == "production" else 30.0
          )
          
          return Perplexity(
              api_key=self.api_key,
              max_retries=self.max_retries,
              timeout=timeout,
              http_client=DefaultHttpxClient(limits=limits)
          )

  # Usage
  config = PerplexityConfig.from_env()
  client = config.create_client()
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  interface PerplexityConfig {
      apiKey: string;
      maxRetries: number;
      timeoutMs: number;
      maxConnections: number;
      maxKeepalive: number;
      environment: string;
  }

  class ConfigManager {
      static fromEnv(): PerplexityConfig {
          const apiKey = process.env.PERPLEXITY_API_KEY;
          if (!apiKey) {
              throw new Error("PERPLEXITY_API_KEY environment variable is required");
          }
          
          return {
              apiKey,
              maxRetries: parseInt(process.env.PERPLEXITY_MAX_RETRIES || '3'),
              timeoutMs: parseInt(process.env.PERPLEXITY_TIMEOUT || '30000'),
              maxConnections: parseInt(process.env.PERPLEXITY_MAX_CONNECTIONS || '100'),
              maxKeepalive: parseInt(process.env.PERPLEXITY_MAX_KEEPALIVE || '20'),
              environment: process.env.NODE_ENV || 'production'
          };
      }
      
      static createClient(config: PerplexityConfig): Perplexity {
          const httpsAgent = new https.Agent({
              keepAlive: true,
              keepAliveMsecs: config.environment === 'production' ? 60000 : 30000,
              maxSockets: config.maxConnections,
              maxFreeSockets: config.maxKeepalive,
              timeout: config.timeoutMs
          });
          
          return new Perplexity({
              apiKey: config.apiKey,
              maxRetries: config.maxRetries,
              timeout: config.timeoutMs,
              httpAgent: httpsAgent
          });
      }
  }

  // Usage
  const config = ConfigManager.fromEnv();
  const client = ConfigManager.createClient(config);
  ```
</CodeGroup>

### Monitoring and Logging

Implement comprehensive monitoring:

<CodeGroup>
  ```python Python theme={null}
  import logging
  import time
  import functools
  from typing import Any, Callable
  from perplexity import Perplexity
  import perplexity

  # Configure logging
  logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  )
  logger = logging.getLogger(__name__)

  class MonitoredPerplexityClient:
      def __init__(self, client: Perplexity):
          self.client = client
          self.request_count = 0
          self.error_count = 0
          self.total_response_time = 0.0
      
      def _log_request(self, method: str, **kwargs):
          """Log request details"""
          self.request_count += 1
          logger.info(f"Making {method} request #{self.request_count}")
          logger.debug(f"Request parameters: {kwargs}")
      
      def _log_response(self, method: str, duration: float, success: bool = True):
          """Log response details"""
          self.total_response_time += duration
          avg_response_time = self.total_response_time / self.request_count
          
          if success:
              logger.info(f"{method} completed in {duration:.2f}s (avg: {avg_response_time:.2f}s)")
          else:
              self.error_count += 1
              logger.error(f"{method} failed after {duration:.2f}s (errors: {self.error_count})")
      
      def search(self, query: str, **kwargs):
          self._log_request("search", query=query, **kwargs)
          start_time = time.time()
          
          try:
              result = self.client.search.create(query=query, **kwargs)
              duration = time.time() - start_time
              self._log_response("search", duration, success=True)
              return result
          except Exception as e:
              duration = time.time() - start_time
              self._log_response("search", duration, success=False)
              logger.error(f"Search error: {type(e).__name__}: {e}")
              raise
      
      def get_stats(self):
          """Get client statistics"""
          return {
              "total_requests": self.request_count,
              "error_count": self.error_count,
              "success_rate": (self.request_count - self.error_count) / max(self.request_count, 1),
              "avg_response_time": self.total_response_time / max(self.request_count, 1)
          }

  # Usage
  client = MonitoredPerplexityClient(Perplexity())
  result = client.search("machine learning")
  print(client.get_stats())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  interface ClientStats {
      totalRequests: number;
      errorCount: number;
      successRate: number;
      avgResponseTime: number;
  }

  class MonitoredPerplexityClient {
      private client: Perplexity;
      private requestCount: number = 0;
      private errorCount: number = 0;
      private totalResponseTime: number = 0;
      
      constructor(client: Perplexity) {
          this.client = client;
      }
      
      private logRequest(method: string, params: any): void {
          this.requestCount++;
          console.log(`Making ${method} request #${this.requestCount}`);
          console.debug(`Request parameters:`, params);
      }
      
      private logResponse(method: string, duration: number, success: boolean = true): void {
          this.totalResponseTime += duration;
          const avgResponseTime = this.totalResponseTime / this.requestCount;
          
          if (success) {
              console.log(`${method} completed in ${duration.toFixed(2)}ms (avg: ${avgResponseTime.toFixed(2)}ms)`);
          } else {
              this.errorCount++;
              console.error(`${method} failed after ${duration.toFixed(2)}ms (errors: ${this.errorCount})`);
          }
      }
      
      async search(query: string, options?: any) {
          this.logRequest("search", { query, ...options });
          const startTime = performance.now();
          
          try {
              const result = await this.client.search.create({ query, ...options });
              const duration = performance.now() - startTime;
              this.logResponse("search", duration, true);
              return result;
          } catch (error) {
              const duration = performance.now() - startTime;
              this.logResponse("search", duration, false);
              console.error(`Search error: ${error}`);
              throw error;
          }
      }
      
      getStats(): ClientStats {
          return {
              totalRequests: this.requestCount,
              errorCount: this.errorCount,
              successRate: (this.requestCount - this.errorCount) / Math.max(this.requestCount, 1),
              avgResponseTime: this.totalResponseTime / Math.max(this.requestCount, 1)
          };
      }
  }

  // Usage
  const client = new MonitoredPerplexityClient(new Perplexity());
  const result = await client.search("machine learning");
  console.log(client.getStats());
  ```
</CodeGroup>

## Error Handling Best Practices

### Graceful Degradation

Implement fallback strategies for different error types:

<CodeGroup>
  ```python Python theme={null}
  from typing import Optional, Dict, Any
  import perplexity
  from perplexity import Perplexity

  class ResilientPerplexityClient:
      def __init__(self, client: Perplexity):
          self.client = client
          self.circuit_breaker_threshold = 5
          self.circuit_breaker_count = 0
          self.circuit_breaker_open = False
      
      def _should_circuit_break(self) -> bool:
          """Check if circuit breaker should be triggered"""
          return self.circuit_breaker_count >= self.circuit_breaker_threshold
      
      def _record_failure(self):
          """Record a failure for circuit breaker"""
          self.circuit_breaker_count += 1
          if self._should_circuit_break():
              self.circuit_breaker_open = True
              print("Circuit breaker activated - temporarily disabling API calls")
      
      def _record_success(self):
          """Record a success - reset circuit breaker"""
          self.circuit_breaker_count = 0
          self.circuit_breaker_open = False
      
      def search_with_fallback(
          self, 
          query: str, 
          fallback_response: Optional[Dict[str, Any]] = None
      ):
          """Search with graceful degradation"""
          if self.circuit_breaker_open:
              print("Circuit breaker open - returning fallback response")
              return fallback_response or {
                  "query": query,
                  "results": [],
                  "status": "service_unavailable"
              }
          
          try:
              result = self.client.search.create(query=query)
              self._record_success()
              return result
              
          except perplexity.RateLimitError:
              print("Rate limited - implementing backoff strategy")
              # Could implement intelligent backoff here
              raise
              
          except perplexity.APIConnectionError as e:
              print(f"Connection error: {e}")
              self._record_failure()
              return fallback_response or {
                  "query": query,
                  "results": [],
                  "status": "connection_error"
              }
              
          except Exception as e:
              print(f"Unexpected error: {e}")
              self._record_failure()
              return fallback_response or {
                  "query": query,
                  "results": [],
                  "status": "error"
              }

  # Usage
  client = ResilientPerplexityClient(Perplexity())
  result = client.search_with_fallback("machine learning")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  interface FallbackResponse {
      query: string;
      results: any[];
      status: string;
  }

  class ResilientPerplexityClient {
      private client: Perplexity;
      private circuitBreakerThreshold: number = 5;
      private circuitBreakerCount: number = 0;
      private circuitBreakerOpen: boolean = false;
      
      constructor(client: Perplexity) {
          this.client = client;
      }
      
      private shouldCircuitBreak(): boolean {
          return this.circuitBreakerCount >= this.circuitBreakerThreshold;
      }
      
      private recordFailure(): void {
          this.circuitBreakerCount++;
          if (this.shouldCircuitBreak()) {
              this.circuitBreakerOpen = true;
              console.log("Circuit breaker activated - temporarily disabling API calls");
          }
      }
      
      private recordSuccess(): void {
          this.circuitBreakerCount = 0;
          this.circuitBreakerOpen = false;
      }
      
      async searchWithFallback(
          query: string,
          fallbackResponse?: FallbackResponse
      ): Promise<any> {
          if (this.circuitBreakerOpen) {
              console.log("Circuit breaker open - returning fallback response");
              return fallbackResponse || {
                  query,
                  results: [],
                  status: "service_unavailable"
              };
          }
          
          try {
              const result = await this.client.search.create({ query });
              this.recordSuccess();
              return result;
              
          } catch (error: any) {
              if (error.constructor.name === 'RateLimitError') {
                  console.log("Rate limited - implementing backoff strategy");
                  throw error;
              } else if (error.constructor.name === 'APIConnectionError') {
                  console.log(`Connection error: ${error.message}`);
                  this.recordFailure();
                  return fallbackResponse || {
                      query,
                      results: [],
                      status: "connection_error"
                  };
              } else {
                  console.log(`Unexpected error: ${error.message}`);
                  this.recordFailure();
                  return fallbackResponse || {
                      query,
                      results: [],
                      status: "error"
                  };
              }
          }
      }
  }

  // Usage
  const client = new ResilientPerplexityClient(new Perplexity());
  const result = await client.searchWithFallback("machine learning");
  ```
</CodeGroup>

## Testing Best Practices

### Unit Testing with Mocking

Create testable code with proper mocking:

<CodeGroup>
  ```python Python theme={null}
  import unittest
  from unittest.mock import Mock, patch
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse, SearchResult

  class TestPerplexityIntegration(unittest.TestCase):
      def setUp(self):
          self.mock_client = Mock(spec=Perplexity)
          
      def test_search_success(self):
          # Mock successful response
          mock_result = SearchResult(
              title="Test Result",
              url="https://example.com",
              snippet="Test snippet"
          )
          
          mock_response = SearchCreateResponse(
              query="test query",
              results=[mock_result]
          )
          
          self.mock_client.search.create.return_value = mock_response
          
          # Test your application logic
          result = self.mock_client.search.create(query="test query")
          
          self.assertEqual(result.query, "test query")
          self.assertEqual(len(result.results), 1)
          self.assertEqual(result.results[0].title, "Test Result")
      
      @patch('perplexity.Perplexity')
      def test_rate_limit_handling(self, mock_perplexity_class):
          # Mock rate limit error
          mock_client = Mock()
          mock_perplexity_class.return_value = mock_client
          mock_client.search.create.side_effect = perplexity.RateLimitError("Rate limited")
          
          # Test your error handling logic here
          with self.assertRaises(perplexity.RateLimitError):
              mock_client.search.create(query="test")

  if __name__ == '__main__':
      unittest.main()
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import { jest } from '@jest/globals';
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import type { SearchCreateResponse, SearchResult } from '@perplexity-ai/perplexity_ai';

  // Mock the Perplexity client
  jest.mock('@perplexity-ai/perplexity_ai');

  describe('Perplexity Integration', () => {
      let mockClient: jest.Mocked<Perplexity>;
      
      beforeEach(() => {
          mockClient = new Perplexity() as jest.Mocked<Perplexity>;
      });
      
      test('should handle successful search', async () => {
          const mockResult: SearchResult = {
              title: "Test Result",
              url: "https://example.com",
              snippet: "Test snippet"
          };
          
          const mockResponse: SearchCreateResponse = {
              query: "test query",
              results: [mockResult]
          };
          
          (mockClient.search.create as jest.Mock).mockResolvedValue(mockResponse);
          
          const result = await mockClient.search.create({ query: "test query" });
          
          expect(result.query).toBe("test query");
          expect(result.results).toHaveLength(1);
          expect(result.results[0].title).toBe("Test Result");
      });
      
      test('should handle rate limit errors', async () => {
          const rateLimitError = new Error('Rate limited');
          rateLimitError.constructor.name = 'RateLimitError';
          
          (mockClient.search.create as jest.Mock).mockRejectedValue(rateLimitError);
          
          await expect(mockClient.search.create({ query: "test" })).rejects.toThrow('Rate limited');
      });
  });
  ```
</CodeGroup>

## Performance Best Practices Summary

<Steps>
  <Step title="Use environment variables for configuration">
    Never hardcode API keys or configuration values.
  </Step>

  <Step title="Implement intelligent rate limiting">
    Use exponential backoff with jitter for retry strategies.
  </Step>

  <Step title="Configure connection pooling">
    Optimize HTTP client settings for your use case.
  </Step>

  <Step title="Monitor and log appropriately">
    Track performance metrics and error rates.
  </Step>

  <Step title="Implement graceful degradation">
    Provide fallback responses when APIs are unavailable.
  </Step>

  <Step title="Write testable code">
    Use dependency injection and mocking for unit tests.
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Error Handling" icon="triangle-exclamation" href="/docs/sdk/error-handling">
    Comprehensive error handling strategies
  </Card>

  <Card title="Performance" icon="bolt" href="/docs/sdk/performance">
    Async operations and optimization techniques
  </Card>

  <Card title="Configuration" icon="gear" href="/docs/sdk/configuration">
    Production-ready configuration patterns
  </Card>

  <Card title="Type Safety" icon="shield-check" href="/docs/sdk/type-safety">
    Leveraging types for safer code
  </Card>
</CardGroup>


# Configuration
Source: https://docs.perplexity.ai/docs/sdk/configuration

Learn how to configure the Perplexity SDKs for retries, timeouts, proxies, and advanced HTTP client customization.

## Overview

The Perplexity SDKs provide extensive configuration options to customize client behavior for different environments and use cases. This guide covers retry configuration, timeout settings, and custom HTTP client setup.

## Retries and Timeouts

### Basic Retry Configuration

Configure how the SDK handles failed requests:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  import httpx

  client = Perplexity(
      max_retries=3,  # Default is 2
      timeout=httpx.Timeout(30.0, read=10.0, write=5.0, connect=2.0)
  )

  # Per-request configuration
  search = client.with_options(max_retries=5).search.create(
      query="example"
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity({
      maxRetries: 3, // Default is 2
      timeout: 30000, // 30 seconds in milliseconds
  });

  // Per-request configuration
  const search = await client.withOptions({ maxRetries: 5 }).search.create({
      query: "example"
  });
  ```
</CodeGroup>

### Advanced Timeout Configuration

Set granular timeout controls for different phases of the request:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity

  # Detailed timeout configuration
  timeout_config = httpx.Timeout(
      connect=5.0,    # Time to establish connection
      read=30.0,      # Time to read response
      write=10.0,     # Time to send request
      pool=10.0       # Time to get connection from pool
  )

  client = Perplexity(timeout=timeout_config)

  # For long-running operations
  long_timeout = httpx.Timeout(
      connect=5.0,
      read=120.0,  # 2 minutes for complex queries
      write=10.0,
      pool=10.0
  )

  client_long = Perplexity(timeout=long_timeout)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Basic timeout (applies to entire request)
  const client = new Perplexity({
      timeout: 30000  // 30 seconds
  });

  // For long-running operations
  const clientLong = new Perplexity({
      timeout: 120000  // 2 minutes for complex queries
  });

  // Per-request timeout override
  const result = await client.withOptions({ 
      timeout: 60000  // 1 minute for this specific request
  }).chat.completions.create({
      model: "llama-3.1-sonar-large-128k-online",
      messages: [{ role: "user", content: "Complex research query..." }]
  });
  ```
</CodeGroup>

## Custom HTTP Client

### Proxy Configuration

Configure the SDK to work with corporate proxies:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # HTTP Proxy
  client = Perplexity(
      http_client=DefaultHttpxClient(
          proxy="http://proxy.company.com:8080"
      )
  )

  # HTTPS Proxy with authentication
  client_auth = Perplexity(
      http_client=DefaultHttpxClient(
          proxy="http://username:password@proxy.company.com:8080"
      )
  )

  # SOCKS proxy
  client_socks = Perplexity(
      http_client=DefaultHttpxClient(
          proxy="socks5://proxy.company.com:1080"
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import { HttpsProxyAgent } from 'https-proxy-agent';
  import { SocksProxyAgent } from 'socks-proxy-agent';

  // HTTP/HTTPS Proxy
  const client = new Perplexity({
      httpAgent: new HttpsProxyAgent('http://proxy.company.com:8080')
  });

  // Proxy with authentication
  const clientAuth = new Perplexity({
      httpAgent: new HttpsProxyAgent('http://username:password@proxy.company.com:8080')
  });

  // SOCKS proxy
  const clientSocks = new Perplexity({
      httpAgent: new SocksProxyAgent('socks5://proxy.company.com:1080')
  });
  ```
</CodeGroup>

### Custom Headers and User Agent

Add custom headers to all requests:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # Custom headers
  headers = {
      "User-Agent": "MyApp/1.0",
      "X-Custom-Header": "custom-value"
  }

  client = Perplexity(
      http_client=DefaultHttpxClient(
          headers=headers
      )
  )

  # Advanced HTTP client configuration
  transport = httpx.HTTPTransport(
      local_address="0.0.0.0",  # Bind to specific interface
      verify=True,              # SSL verification
      cert=None,                # Client certificate
      http2=True               # Enable HTTP/2
  )

  client_advanced = Perplexity(
      http_client=DefaultHttpxClient(
          transport=transport,
          headers=headers
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Custom headers
  const client = new Perplexity({
      defaultHeaders: {
          "User-Agent": "MyApp/1.0",
          "X-Custom-Header": "custom-value"
      }
  });

  // Advanced fetch configuration
  const clientAdvanced = new Perplexity({
      fetch: (url, options) => {
          return fetch(url, {
              ...options,
              headers: {
                  ...options?.headers,
                  "User-Agent": "MyApp/1.0",
                  "X-Custom-Header": "custom-value"
              }
          });
      }
  });
  ```
</CodeGroup>

### SSL/TLS Configuration

Configure SSL verification and certificates:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  import ssl
  from perplexity import Perplexity, DefaultHttpxClient

  # Disable SSL verification (not recommended for production)
  client_no_ssl = Perplexity(
      http_client=DefaultHttpxClient(
          verify=False
      )
  )

  # Custom SSL context
  ssl_context = ssl.create_default_context()
  ssl_context.check_hostname = False
  ssl_context.verify_mode = ssl.CERT_NONE

  client_custom_ssl = Perplexity(
      http_client=DefaultHttpxClient(
          verify=ssl_context
      )
  )

  # Client certificate authentication
  client_cert = Perplexity(
      http_client=DefaultHttpxClient(
          cert=("client.crt", "client.key")
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  // Custom HTTPS agent with SSL options
  const httpsAgent = new https.Agent({
      rejectUnauthorized: false, // Disable SSL verification (not recommended)
      keepAlive: true,
      maxSockets: 50
  });

  const client = new Perplexity({
      httpAgent: httpsAgent
  });

  // For Node.js environments with custom CA certificates
  const httpsAgentCA = new https.Agent({
      ca: [/* your CA certificates */],
      cert: /* client certificate */,
      key: /* client private key */
  });

  const clientCert = new Perplexity({
      httpAgent: httpsAgentCA
  });
  ```
</CodeGroup>

## Connection Pooling

Optimize performance with connection pooling:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # Configure connection limits
  limits = httpx.Limits(
      max_keepalive_connections=20,  # Keep-alive connections
      max_connections=100,           # Total connections
      keepalive_expiry=30.0         # Keep-alive timeout
  )

  client = Perplexity(
      http_client=DefaultHttpxClient(
          limits=limits
      )
  )

  # For high-throughput applications
  high_throughput_limits = httpx.Limits(
      max_keepalive_connections=100,
      max_connections=500,
      keepalive_expiry=60.0
  )

  client_high_throughput = Perplexity(
      http_client=DefaultHttpxClient(
          limits=high_throughput_limits
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  // Configure agent pool settings
  const httpsAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 30000,  // 30 seconds
      maxSockets: 50,         // Max connections per host
      maxFreeSockets: 10,     // Max idle connections per host
      timeout: 60000          // Socket timeout
  });

  const client = new Perplexity({
      httpAgent: httpsAgent
  });

  // For high-throughput applications
  const highThroughputAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 60000,
      maxSockets: 200,
      maxFreeSockets: 50,
      timeout: 120000
  });

  const clientHighThroughput = new Perplexity({
      httpAgent: highThroughputAgent
  });
  ```
</CodeGroup>

## Environment-Specific Configuration

### Development Configuration

Settings optimized for development and debugging:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # Development configuration
  dev_client = Perplexity(
      max_retries=1,           # Fail fast in development
      timeout=httpx.Timeout(10.0),  # Short timeout
      http_client=DefaultHttpxClient(
          # Enable detailed logging
          event_hooks={
              'request': [lambda request: print(f"Request: {request.method} {request.url}")],
              'response': [lambda response: print(f"Response: {response.status_code}")]
          }
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Development configuration
  const devClient = new Perplexity({
      maxRetries: 1,     // Fail fast in development
      timeout: 10000,    // 10 second timeout
      
      // Custom fetch with logging
      fetch: (url, options) => {
          console.log(`Request: ${options?.method || 'GET'} ${url}`);
          return fetch(url, options).then(response => {
              console.log(`Response: ${response.status}`);
              return response;
          });
      }
  });
  ```
</CodeGroup>

### Production Configuration

Settings optimized for production environments:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # Production configuration
  prod_limits = httpx.Limits(
      max_keepalive_connections=50,
      max_connections=200,
      keepalive_expiry=60.0
  )

  prod_timeout = httpx.Timeout(
      connect=5.0,
      read=60.0,
      write=10.0,
      pool=10.0
  )

  prod_client = Perplexity(
      max_retries=3,
      timeout=prod_timeout,
      http_client=DefaultHttpxClient(
          limits=prod_limits,
          verify=True,  # Always verify SSL in production
          http2=True    # Enable HTTP/2 for better performance
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  // Production configuration
  const prodAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 60000,
      maxSockets: 100,
      maxFreeSockets: 20,
      timeout: 60000
  });

  const prodClient = new Perplexity({
      maxRetries: 3,
      timeout: 60000,
      httpAgent: prodAgent
  });
  ```
</CodeGroup>

## Configuration Patterns

### Environment-Based Configuration

Use environment variables to configure the client:

<CodeGroup>
  ```python Python theme={null}
  import os
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  def create_client():
      # Base configuration
      timeout = httpx.Timeout(
          connect=float(os.getenv('PERPLEXITY_CONNECT_TIMEOUT', '5.0')),
          read=float(os.getenv('PERPLEXITY_READ_TIMEOUT', '30.0')),
          write=float(os.getenv('PERPLEXITY_WRITE_TIMEOUT', '10.0'))
      )
      
      max_retries = int(os.getenv('PERPLEXITY_MAX_RETRIES', '3'))
      
      # Optional proxy configuration
      proxy = os.getenv('PERPLEXITY_PROXY')
      http_client_kwargs = {}
      if proxy:
          http_client_kwargs['proxy'] = proxy
      
      return Perplexity(
          max_retries=max_retries,
          timeout=timeout,
          http_client=DefaultHttpxClient(**http_client_kwargs)
      )

  client = create_client()
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import { HttpsProxyAgent } from 'https-proxy-agent';

  function createClient(): Perplexity {
      const maxRetries = parseInt(process.env.PERPLEXITY_MAX_RETRIES || '3');
      const timeout = parseInt(process.env.PERPLEXITY_TIMEOUT || '30000');
      
      const config: any = {
          maxRetries,
          timeout
      };
      
      // Optional proxy configuration
      if (process.env.PERPLEXITY_PROXY) {
          config.httpAgent = new HttpsProxyAgent(process.env.PERPLEXITY_PROXY);
      }
      
      return new Perplexity(config);
  }

  const client = createClient();
  ```
</CodeGroup>

### Configuration Factory

Create reusable configuration patterns:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  class PerplexityClientFactory:
      @staticmethod
      def development():
          return Perplexity(
              max_retries=1,
              timeout=httpx.Timeout(10.0)
          )
      
      @staticmethod
      def production():
          return Perplexity(
              max_retries=3,
              timeout=httpx.Timeout(connect=5.0, read=60.0, write=10.0),
              http_client=DefaultHttpxClient(
                  limits=httpx.Limits(
                      max_keepalive_connections=50,
                      max_connections=200
                  )
              )
          )
      
      @staticmethod
      def high_throughput():
          return Perplexity(
              max_retries=2,
              timeout=httpx.Timeout(connect=2.0, read=30.0, write=5.0),
              http_client=DefaultHttpxClient(
                  limits=httpx.Limits(
                      max_keepalive_connections=100,
                      max_connections=500
                  )
              )
          )

  # Usage
  client = PerplexityClientFactory.production()
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  class PerplexityClientFactory {
      static development(): Perplexity {
          return new Perplexity({
              maxRetries: 1,
              timeout: 10000
          });
      }
      
      static production(): Perplexity {
          const agent = new https.Agent({
              keepAlive: true,
              maxSockets: 100,
              timeout: 60000
          });
          
          return new Perplexity({
              maxRetries: 3,
              timeout: 60000,
              httpAgent: agent
          });
      }
      
      static highThroughput(): Perplexity {
          const agent = new https.Agent({
              keepAlive: true,
              maxSockets: 500,
              maxFreeSockets: 100,
              timeout: 30000
          });
          
          return new Perplexity({
              maxRetries: 2,
              timeout: 30000,
              httpAgent: agent
          });
      }
  }

  // Usage
  const client = PerplexityClientFactory.production();
  ```
</CodeGroup>

## Related Resources

<CardGroup>
  <Card title="Error Handling" icon="triangle-exclamation" href="/docs/sdk/error-handling">
    Handle timeouts and connection errors
  </Card>

  <Card title="Performance" icon="bolt" href="/docs/sdk/performance">
    Optimize async operations and connection pooling
  </Card>
</CardGroup>


# Error Handling
Source: https://docs.perplexity.ai/docs/sdk/error-handling

Learn how to handle API errors gracefully with the Perplexity SDKs for Python and TypeScript/JavaScript.

## Overview

The Perplexity SDKs provide robust error handling with specific exception types for different error scenarios. This guide covers how to catch and handle common API errors gracefully.

## Common Error Types

The SDKs provide specific exception types for different error scenarios:

* **APIConnectionError** - Network connection issues
* **RateLimitError** - API rate limit exceeded
* **APIStatusError** - HTTP status errors (4xx, 5xx)
* **AuthenticationError** - Invalid API key or authentication issues
* **ValidationError** - Invalid request parameters

## Basic Error Handling

Handle common API errors with try-catch blocks:

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  client = Perplexity()

  try:
      search = client.search.create(query="machine learning")
      print(search.results)
  except perplexity.APIConnectionError as e:
      print("Network connection failed")
      print(e.__cause__)
  except perplexity.RateLimitError as e:
      print("Rate limit exceeded, please retry later")
  except perplexity.APIStatusError as e:
      print(f"API error: {e.status_code}")
      print(e.response)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  try {
      const search = await client.search.create({ query: "machine learning" });
      console.log(search.results);
  } catch (error) {
      if (error.constructor.name === 'APIConnectionError') {
          console.log("Network connection failed");
          console.log(error.cause);
      } else if (error.constructor.name === 'RateLimitError') {
          console.log("Rate limit exceeded, please retry later");
      } else if (error.constructor.name === 'APIStatusError') {
          console.log(`API error: ${error.status}`);
          console.log(error.response);
      }
  }
  ```
</CodeGroup>

<Info>
  Common HTTP status codes: 400 (Bad Request), 401 (Authentication), 403 (Permission Denied), 404 (Not Found), 429 (Rate Limit), 500+ (Server Error).
</Info>

## Advanced Error Handling

### Exponential Backoff for Rate Limits

Implement intelligent retry logic for rate limit errors:

<CodeGroup>
  ```python Python theme={null}
  import time
  import random
  import perplexity
  from perplexity import Perplexity

  def search_with_retry(client, query, max_retries=3):
      for attempt in range(max_retries):
          try:
              return client.search.create(query=query)
          except perplexity.RateLimitError:
              if attempt == max_retries - 1:
                  raise  # Re-raise on final attempt
              
              # Exponential backoff with jitter
              delay = (2 ** attempt) + random.uniform(0, 1)
              print(f"Rate limited. Retrying in {delay:.2f} seconds...")
              time.sleep(delay)
          except perplexity.APIConnectionError:
              if attempt == max_retries - 1:
                  raise
              
              # Shorter delay for connection errors
              delay = 1 + random.uniform(0, 1)
              print(f"Connection error. Retrying in {delay:.2f} seconds...")
              time.sleep(delay)

  # Usage
  client = Perplexity()
  result = search_with_retry(client, "artificial intelligence")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function searchWithRetry(
      client: Perplexity, 
      query: string, 
      maxRetries: number = 3
  ) {
      for (let attempt = 0; attempt < maxRetries; attempt++) {
          try {
              return await client.search.create({ query });
          } catch (error) {
              if (attempt === maxRetries - 1) {
                  throw error; // Re-throw on final attempt
              }
              
              if (error.constructor.name === 'RateLimitError') {
                  // Exponential backoff with jitter
                  const delay = (2 ** attempt + Math.random()) * 1000;
                  console.log(`Rate limited. Retrying in ${delay}ms...`);
                  await new Promise(resolve => setTimeout(resolve, delay));
              } else if (error.constructor.name === 'APIConnectionError') {
                  // Shorter delay for connection errors
                  const delay = (1 + Math.random()) * 1000;
                  console.log(`Connection error. Retrying in ${delay}ms...`);
                  await new Promise(resolve => setTimeout(resolve, delay));
              } else {
                  throw error; // Don't retry other errors
              }
          }
      }
  }

  // Usage
  const client = new Perplexity();
  const result = await searchWithRetry(client, "artificial intelligence");
  ```
</CodeGroup>

### Error Context and Debugging

Extract detailed error information for debugging:

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  client = Perplexity()

  try:
      chat = client.chat.completions.create(
          model="sonar-pro",
          messages=[{"role": "user", "content": "What's the weather?"}]
      )
  except perplexity.APIStatusError as e:
      print(f"Status Code: {e.status_code}")
      print(f"Error Type: {e.type}")
      print(f"Error Message: {e.message}")
      
      # Access raw response for detailed debugging
      if hasattr(e, 'response'):
          print(f"Raw Response: {e.response.text}")
          print(f"Request ID: {e.response.headers.get('X-Request-ID')}")
          
  except perplexity.ValidationError as e:
      print(f"Validation Error: {e}")
      # Handle parameter validation errors
      
  except Exception as e:
      print(f"Unexpected error: {type(e).__name__}: {e}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  try {
      const chat = await client.chat.completions.create({
          model: "sonar-pro",
          messages: [{ role: "user", content: "What's the weather?" }]
      });
  } catch (error: any) {
      if (error.constructor.name === 'APIStatusError') {
          console.log(`Status Code: ${error.status}`);
          console.log(`Error Type: ${error.type}`);
          console.log(`Error Message: ${error.message}`);
          
          // Access raw response for detailed debugging
          if (error.response) {
              console.log(`Raw Response: ${await error.response.text()}`);
              console.log(`Request ID: ${error.response.headers.get('X-Request-ID')}`);
          }
      } else if (error.constructor.name === 'ValidationError') {
          console.log(`Validation Error: ${error.message}`);
          // Handle parameter validation errors
      } else {
          console.log(`Unexpected error: ${error.constructor.name}: ${error.message}`);
      }
  }
  ```
</CodeGroup>

## Error Recovery Strategies

### Graceful Degradation

Implement fallback mechanisms when API calls fail:

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  def get_ai_response(query, fallback_response="I'm sorry, I'm temporarily unavailable."):
      client = Perplexity()
      
      try:
          # Primary: Try online model
          response = client.chat.completions.create(
              model="sonar-pro",
              messages=[{"role": "user", "content": query}]
          )
          return response.choices[0].message.content
          
      except perplexity.RateLimitError:
          try:
              # Fallback: Try offline model if rate limited
              response = client.chat.completions.create(
                  model="llama-3.1-8b-instruct",
                  messages=[{"role": "user", "content": query}]
              )
              return response.choices[0].message.content
          except Exception:
              return fallback_response
              
      except perplexity.APIConnectionError:
          # Network issues - return cached response or fallback
          return fallback_response
          
      except Exception as e:
          print(f"Unexpected error: {e}")
          return fallback_response

  # Usage
  response = get_ai_response("What is machine learning?")
  print(response)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function getAIResponse(
      query: string, 
      fallbackResponse: string = "I'm sorry, I'm temporarily unavailable."
  ): Promise<string> {
      const client = new Perplexity();
      
      try {
          // Primary: Try online model
          const response = await client.chat.completions.create({
              model: "sonar-pro",
              messages: [{ role: "user", content: query }]
          });
          return response.choices[0].message.content || "";
          
      } catch (error: any) {
          if (error.constructor.name === 'RateLimitError') {
              try {
                  // Fallback: Try offline model if rate limited
                  const response = await client.chat.completions.create({
                      model: "llama-3.1-8b-instruct",
                      messages: [{ role: "user", content: query }]
                  });
                  return response.choices[0].message.content || "";
              } catch {
                  return fallbackResponse;
              }
          } else if (error.constructor.name === 'APIConnectionError') {
              // Network issues - return cached response or fallback
              return fallbackResponse;
          } else {
              console.log(`Unexpected error: ${error.message}`);
              return fallbackResponse;
          }
      }
  }

  // Usage
  const response = await getAIResponse("What is machine learning?");
  console.log(response);
  ```
</CodeGroup>

## Best Practices

<Steps>
  <Step title="Always handle rate limits">
    Rate limiting is common with API usage. Always implement retry logic with exponential backoff.

    <Warning>
      Don't implement aggressive retry loops without delays - this can worsen rate limiting.
    </Warning>
  </Step>

  <Step title="Log errors for monitoring">
    Include proper logging to track error patterns and API health.

    <CodeGroup>
      ```python Python theme={null}
      import logging
      import perplexity

      logging.basicConfig(level=logging.INFO)
      logger = logging.getLogger(__name__)

      try:
          result = client.search.create(query="example")
      except perplexity.APIStatusError as e:
          logger.error(f"API Error {e.status_code}: {e.message}", 
                      extra={'request_id': e.response.headers.get('X-Request-ID')})
      ```

      ```typescript TypeScript/JavaScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      try {
          const result = await client.search.create({ query: "example" });
      } catch (error: any) {
          console.error(`API Error ${error.status}: ${error.message}`, {
              requestId: error.response?.headers.get('X-Request-ID')
          });
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Set appropriate timeouts">
    Configure timeouts to prevent hanging requests.

    <CodeGroup>
      ```python Python theme={null}
      import httpx
      from perplexity import Perplexity

      client = Perplexity(
          timeout=httpx.Timeout(connect=5.0, read=30.0, write=5.0, pool=10.0)
      )
      ```

      ```typescript TypeScript/JavaScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity({
          timeout: 30000 // 30 seconds
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Handle authentication errors">
    Check for invalid API keys and provide helpful error messages.

    <CodeGroup>
      ```python Python theme={null}
      try:
          result = client.search.create(query="test")
      except perplexity.AuthenticationError:
          print("Invalid API key. Please check your PERPLEXITY_API_KEY environment variable.")
      ```

      ```typescript TypeScript/JavaScript theme={null}
      try {
          const result = await client.search.create({ query: "test" });
      } catch (error: any) {
          if (error.constructor.name === 'AuthenticationError') {
              console.log("Invalid API key. Please check your PERPLEXITY_API_KEY environment variable.");
          }
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Configuration" icon="gear" href="/docs/sdk/configuration">
    Configure timeouts and retries
  </Card>

  <Card title="Best Practices" icon="star" href="/docs/sdk/best-practices">
    Environment variables and rate limiting
  </Card>
</CardGroup>


# Quickstart
Source: https://docs.perplexity.ai/docs/sdk/overview

Learn how to use the official Perplexity SDKs for Python and TypeScript/JavaScript to access the Perplexity APIs with type safety and async support.

## Overview

The official Perplexity SDKs provide convenient access to the Perplexity APIs from Python 3.8+ and Node.js applications. Both SDKs include type definitions for all request parameters and response fields, with both synchronous and asynchronous clients.

Access three core APIs: **Chat Completions** for web-grounded AI responses, **Agentic Research** for third-party models with web search tools and presets, and **Search** for ranked web search results.

## Available APIs

<CardGroup>
  <Card title="Chat Completions" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    AI responses with web-grounded knowledge, conversation context, and streaming support.
  </Card>

  <Card title="Agentic Research" icon="code" href="/docs/grounded-llm/responses/quickstart">
    Third-party models from OpenAI, Anthropic, Google, and more with presets and web search tools.
  </Card>

  <Card title="Search" icon="magnifying-glass" href="/docs/search/quickstart">
    Ranked web search results with filtering, multi-query support, and domain controls.
  </Card>
</CardGroup>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript/JavaScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```
</CodeGroup>

## Authentication

<Card title="Get your Perplexity API Key" icon="key" href="https://perplexity.ai/account/api">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

After generating the key, set it as an environment variable in your terminal:

<Tabs>
  <Tab title="Windows">
    ```bash theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>

  <Tab title="MacOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>
</Tabs>

### Using Environment Variables

You can use the environment variable directly:

<CodeGroup>
  ```python Python theme={null}
  import os
  from perplexity import Perplexity

  client = Perplexity() # Automatically uses PERPLEXITY_API_KEY
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity({
    apiKey: process.env['PERPLEXITY_API_KEY'], // This is the default and can be omitted
  });
  ```
</CodeGroup>

Or use [python-dotenv](https://pypi.org/project/python-dotenv/) (Python) or [dotenv](https://www.npmjs.com/package/dotenv) (Node.js) to load the environment variable from a `.env` file:

<CodeGroup>
  ```python Python theme={null}
  import os
  from dotenv import load_dotenv
  from perplexity import Perplexity

  load_dotenv()

  client = Perplexity() # Uses PERPLEXITY_API_KEY from .env file
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import dotenv from 'dotenv';

  dotenv.config();

  const client = new Perplexity(); // Uses PERPLEXITY_API_KEY from .env file
  ```
</CodeGroup>

<Tip>
  Now you're ready to start using the Perplexity APIs! Choose your API below for step-by-step usage guides.
</Tip>

<CardGroup>
  <Card title="Chat Completions" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Get started with AI responses
  </Card>

  <Card title="Agentic Research" icon="code" href="/docs/grounded-llm/responses/quickstart">
    Get started with third-party models
  </Card>

  <Card title="Search" icon="magnifying-glass" href="/docs/search/quickstart">
    Get started with web search
  </Card>
</CardGroup>

## Resources

<CardGroup>
  <Card title="Python Package" icon="cube" href="https://pypi.org/project/perplexityai/">
    Install from PyPI with pip
  </Card>

  <Card title="Node.js Package" icon="cube" href="https://www.npmjs.com/package/@perplexity-ai/perplexity_ai">
    Install from npm registry
  </Card>
</CardGroup>


# Performance Optimization
Source: https://docs.perplexity.ai/docs/sdk/performance

Learn how to optimize the Perplexity SDKs for high-throughput applications with async support, connection pooling, and raw response access.

## Overview

The Perplexity SDKs provide several features to optimize performance for high-throughput applications. This guide covers async operations, connection pooling, raw response access, and other performance optimization techniques.

## Async Support

### Basic Async Usage

For applications that need to handle multiple requests concurrently:

<CodeGroup>
  ```bash Python Installation theme={null}
  pip install perplexityai[aiohttp]
  ```

  ```bash TypeScript/JavaScript Installation theme={null}
  npm install @perplexity-ai/perplexity_ai
  # Async support is built-in with TypeScript/JavaScript
  ```
</CodeGroup>

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def main():
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          # Single async request
          search = await client.search.create(query="machine learning")
          print(search.results)

  asyncio.run(main())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function main() {
      const client = new Perplexity();
      
      // Async is built-in for TypeScript/JavaScript
      const search = await client.search.create({ query: "machine learning" });
      console.log(search.results);
  }

  main();
  ```
</CodeGroup>

### Concurrent Requests

Process multiple requests simultaneously for better throughput:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def concurrent_searches():
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          # Concurrent requests
          queries = ["AI", "machine learning", "deep learning", "neural networks"]
          tasks = [
              client.search.create(query=query)
              for query in queries
          ]
          
          results = await asyncio.gather(*tasks)
          
          for i, result in enumerate(results):
              print(f"Query '{queries[i]}': {len(result.results)} results")

  asyncio.run(concurrent_searches())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function concurrentSearches() {
      const client = new Perplexity();
      
      // Concurrent requests
      const queries = ["AI", "machine learning", "deep learning", "neural networks"];
      const tasks = queries.map(query => 
          client.search.create({ query })
      );
      
      const results = await Promise.all(tasks);
      
      results.forEach((result, i) => {
          console.log(`Query '${queries[i]}': ${result.results.length} results`);
      });
  }

  concurrentSearches();
  ```
</CodeGroup>

### Batch Processing with Rate Limiting

Process large numbers of requests while respecting rate limits:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def batch_process_with_limit(queries, batch_size=5, delay=1.0):
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          results = []
          
          for i in range(0, len(queries), batch_size):
              batch = queries[i:i + batch_size]
              
              # Process batch concurrently
              tasks = [
                  client.search.create(query=query)
                  for query in batch
              ]
              
              batch_results = await asyncio.gather(*tasks, return_exceptions=True)
              results.extend(batch_results)
              
              # Delay between batches to respect rate limits
              if i + batch_size < len(queries):
                  await asyncio.sleep(delay)
          
          return results

  # Usage
  queries = [f"query {i}" for i in range(20)]
  results = asyncio.run(batch_process_with_limit(queries))
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function batchProcessWithLimit(
      queries: string[], 
      batchSize: number = 5, 
      delay: number = 1000
  ) {
      const client = new Perplexity();
      const results = [];
      
      for (let i = 0; i < queries.length; i += batchSize) {
          const batch = queries.slice(i, i + batchSize);
          
          // Process batch concurrently
          const tasks = batch.map(query => 
              client.search.create({ query }).catch(error => error)
          );
          
          const batchResults = await Promise.all(tasks);
          results.push(...batchResults);
          
          // Delay between batches to respect rate limits
          if (i + batchSize < queries.length) {
              await new Promise(resolve => setTimeout(resolve, delay));
          }
      }
      
      return results;
  }

  // Usage
  const queries = Array.from({ length: 20 }, (_, i) => `query ${i}`);
  const results = await batchProcessWithLimit(queries);
  ```
</CodeGroup>

## Raw Response Access

Access headers, status codes, and raw response data for advanced use cases:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Get raw response with headers
  response = client.search.with_raw_response.create(
      query="machine learning"
  )

  print(f"Status Code: {response.status_code}")
  print(f"Request ID: {response.headers.get('X-Request-ID')}")
  print(f"Rate Limit Remaining: {response.headers.get('X-RateLimit-Remaining')}")
  print(f"Rate Limit Reset: {response.headers.get('X-RateLimit-Reset')}")

  # Parse the actual search results
  search = response.parse()
  print(f"Found {len(search.results)} results")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Get raw response with headers
  const response = await client.search.withRawResponse.create({
      query: "machine learning"
  });

  console.log(`Status Code: ${response.response.status}`);
  console.log(`Request ID: ${response.response.headers.get('X-Request-ID')}`);
  console.log(`Rate Limit Remaining: ${response.response.headers.get('X-RateLimit-Remaining')}`);
  console.log(`Rate Limit Reset: ${response.response.headers.get('X-RateLimit-Reset')}`);

  // Parse the actual search results
  const search = response.parse();
  console.log(`Found ${search.results.length} results`);
  ```
</CodeGroup>

### Response Streaming

For chat completions, use streaming to get partial results as they arrive:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Stream chat completion responses
  stream = client.chat.completions.create(
      model="llama-3.1-sonar-large-128k-online",
      messages=[{"role": "user", "content": "Explain quantum computing"}],
      stream=True
  )

  for chunk in stream:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="", flush=True)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Stream chat completion responses
  const stream = await client.chat.completions.create({
      model: "llama-3.1-sonar-large-128k-online",
      messages: [{ role: "user", content: "Explain quantum computing" }],
      stream: true
  });

  for await (const chunk of stream) {
      if (chunk.choices[0]?.delta?.content) {
          process.stdout.write(chunk.choices[0].delta.content);
      }
  }
  ```
</CodeGroup>

## Connection Pooling

### Optimized Connection Settings

Configure connection pooling for better performance:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient, AsyncPerplexity, DefaultAioHttpClient

  # Sync client with optimized connection pooling
  limits = httpx.Limits(
      max_keepalive_connections=50,  # Keep connections alive
      max_connections=100,           # Total connection pool size
      keepalive_expiry=30.0         # Keep-alive timeout
  )

  sync_client = Perplexity(
      http_client=DefaultHttpxClient(limits=limits)
  )

  # Async client with optimized connection pooling
  async_limits = httpx.Limits(
      max_keepalive_connections=100,
      max_connections=200,
      keepalive_expiry=60.0
  )

  async def create_async_client():
      return AsyncPerplexity(
          http_client=DefaultAioHttpClient(limits=async_limits)
      )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  // Optimized HTTPS agent for connection pooling
  const optimizedAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 30000,  // 30 seconds
      maxSockets: 50,         // Max connections per host
      maxFreeSockets: 10,     // Max idle connections per host
      timeout: 60000          // Socket timeout
  });

  const client = new Perplexity({
      httpAgent: optimizedAgent
  });

  // For high-throughput applications
  const highThroughputAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 60000,
      maxSockets: 200,
      maxFreeSockets: 50,
      timeout: 120000
  });

  const clientHighThroughput = new Perplexity({
      httpAgent: highThroughputAgent
  });
  ```
</CodeGroup>

## Performance Monitoring

### Request Timing and Metrics

Monitor performance metrics to identify bottlenecks:

<CodeGroup>
  ```python Python theme={null}
  import time
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  class PerformanceMonitor:
      def __init__(self):
          self.request_times = []
          self.error_count = 0
          
      async def timed_request(self, client, query):
          start_time = time.time()
          try:
              result = await client.search.create(query=query)
              duration = time.time() - start_time
              self.request_times.append(duration)
              return result
          except Exception as e:
              self.error_count += 1
              raise e
      
      def get_stats(self):
          if not self.request_times:
              return {"error": "No successful requests"}
          
          return {
              "total_requests": len(self.request_times),
              "error_count": self.error_count,
              "avg_response_time": sum(self.request_times) / len(self.request_times),
              "min_response_time": min(self.request_times),
              "max_response_time": max(self.request_times)
          }

  async def run_performance_test():
      monitor = PerformanceMonitor()
      
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          queries = [f"test query {i}" for i in range(10)]
          
          tasks = [
              monitor.timed_request(client, query)
              for query in queries
          ]
          
          await asyncio.gather(*tasks, return_exceptions=True)
          
      print(monitor.get_stats())

  asyncio.run(run_performance_test())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class PerformanceMonitor {
      private requestTimes: number[] = [];
      private errorCount: number = 0;
      
      async timedRequest(client: Perplexity, query: string) {
          const startTime = performance.now();
          try {
              const result = await client.search.create({ query });
              const duration = performance.now() - startTime;
              this.requestTimes.push(duration);
              return result;
          } catch (error) {
              this.errorCount++;
              throw error;
          }
      }
      
      getStats() {
          if (this.requestTimes.length === 0) {
              return { error: "No successful requests" };
          }
          
          return {
              totalRequests: this.requestTimes.length,
              errorCount: this.errorCount,
              avgResponseTime: this.requestTimes.reduce((a, b) => a + b, 0) / this.requestTimes.length,
              minResponseTime: Math.min(...this.requestTimes),
              maxResponseTime: Math.max(...this.requestTimes)
          };
      }
  }

  async function runPerformanceTest() {
      const monitor = new PerformanceMonitor();
      const client = new Perplexity();
      
      const queries = Array.from({ length: 10 }, (_, i) => `test query ${i}`);
      
      const tasks = queries.map(query => 
          monitor.timedRequest(client, query).catch(error => error)
      );
      
      await Promise.all(tasks);
      
      console.log(monitor.getStats());
  }

  runPerformanceTest();
  ```
</CodeGroup>

## Memory Optimization

### Efficient Data Processing

Process large datasets efficiently with streaming and pagination:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def process_large_dataset(queries, process_fn):
      """Process queries in batches to manage memory usage"""
      
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          
          async def process_single(query):
              try:
                  result = await client.search.create(query=query)
                  # Process immediately to avoid storing in memory
                  processed = process_fn(result)
                  # Clear the original result from memory
                  del result
                  return processed
              except Exception as e:
                  return f"Error processing {query}: {e}"
          
          # Process in small batches
          batch_size = 5
          for i in range(0, len(queries), batch_size):
              batch = queries[i:i + batch_size]
              
              # Process batch
              tasks = [process_single(query) for query in batch]
              batch_results = await asyncio.gather(*tasks)
              
              # Yield results instead of accumulating
              for result in batch_results:
                  yield result
              
              # Optional: Small delay to prevent overwhelming the API
              await asyncio.sleep(0.1)

  # Usage
  async def summarize_result(search_result):
      """Process function that extracts only what we need"""
      return {
          "query": search_result.query,
          "result_count": len(search_result.results),
          "top_title": search_result.results[0].title if search_result.results else None
      }

  async def main():
      queries = [f"query {i}" for i in range(100)]
      
      async for processed_result in process_large_dataset(queries, summarize_result):
          print(processed_result)

  asyncio.run(main())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function* processLargeDataset<T>(
      queries: string[], 
      processFn: (result: any) => T
  ): AsyncGenerator<T | string> {
      const client = new Perplexity();
      
      async function processSingle(query: string): Promise<T | string> {
          try {
              const result = await client.search.create({ query });
              // Process immediately to avoid storing in memory
              const processed = processFn(result);
              return processed;
          } catch (error) {
              return `Error processing ${query}: ${error}`;
          }
      }
      
      // Process in small batches
      const batchSize = 5;
      for (let i = 0; i < queries.length; i += batchSize) {
          const batch = queries.slice(i, i + batchSize);
          
          // Process batch
          const tasks = batch.map(query => processSingle(query));
          const batchResults = await Promise.all(tasks);
          
          // Yield results instead of accumulating
          for (const result of batchResults) {
              yield result;
          }
          
          // Optional: Small delay to prevent overwhelming the API
          await new Promise(resolve => setTimeout(resolve, 100));
      }
  }

  // Usage
  function summarizeResult(searchResult: any) {
      return {
          query: searchResult.query,
          resultCount: searchResult.results.length,
          topTitle: searchResult.results[0]?.title || null
      };
  }

  async function main() {
      const queries = Array.from({ length: 100 }, (_, i) => `query ${i}`);
      
      for await (const processedResult of processLargeDataset(queries, summarizeResult)) {
          console.log(processedResult);
      }
  }

  main();
  ```
</CodeGroup>

## Best Practices

<Steps>
  <Step title="Use async for concurrent operations">
    Always use async clients when you need to process multiple requests simultaneously.

    <Tip>
      For CPU-bound processing after API calls, consider using worker threads or processes.
    </Tip>
  </Step>

  <Step title="Implement connection pooling">
    Configure appropriate connection limits based on your application's needs.

    <CodeGroup>
      ```python Python theme={null}
      # Good: Optimized for your use case
      limits = httpx.Limits(
          max_keepalive_connections=20,  # Based on expected concurrency
          max_connections=50,
          keepalive_expiry=30.0
      )
      ```

      ```typescript TypeScript/JavaScript theme={null}
      // Good: Optimized for your use case
      const agent = new https.Agent({
          keepAlive: true,
          maxSockets: 20,  // Based on expected concurrency
          keepAliveMsecs: 30000
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Monitor and tune performance">
    Use metrics to identify bottlenecks and optimize accordingly.

    <Warning>
      Don't optimize prematurely - measure first, then optimize based on actual performance data.
    </Warning>
  </Step>

  <Step title="Handle backpressure">
    Implement proper rate limiting and backpressure handling for high-throughput applications.

    <CodeGroup>
      ```python Python theme={null}
      # Use semaphores to limit concurrent requests
      semaphore = asyncio.Semaphore(10)  # Max 10 concurrent requests

      async def rate_limited_request(client, query):
          async with semaphore:
              return await client.search.create(query=query)
      ```

      ```typescript TypeScript/JavaScript theme={null}
      // Use a queue or throttling library
      import pLimit from 'p-limit';

      const limit = pLimit(10);  // Max 10 concurrent requests

      const rateLimitedRequest = (client: Perplexity, query: string) =>
          limit(() => client.search.create({ query }));
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Configuration" icon="gear" href="/docs/sdk/configuration">
    Optimize connection pooling and timeouts
  </Card>

  <Card title="Error Handling" icon="triangle-exclamation" href="/docs/sdk/error-handling">
    Handle errors in async operations
  </Card>
</CardGroup>


# Type Safety
Source: https://docs.perplexity.ai/docs/sdk/type-safety

Learn how to leverage full TypeScript definitions and Python type hints with the Perplexity SDKs for better development experience and code safety.

## Overview

Both Perplexity SDKs provide comprehensive type definitions to help you catch errors at development time and provide better IDE support. This guide covers type annotations, generic types, and advanced typing patterns.

## Basic Type Usage

### Type Imports and Annotations

Use type imports for better IDE support and type checking:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  from perplexity.types import (
      SearchCreateResponse,
      ChatCompletionCreateResponse,
      SearchResult,
      ChatCompletionMessage
  )

  client = Perplexity()

  # Type hints for better IDE support
  search_response: SearchCreateResponse = client.search.create(
      query="artificial intelligence"
  )

  # Access typed properties
  result: SearchResult = search_response.results[0]
  print(f"Title: {result.title}")
  print(f"URL: {result.url}")
  print(f"Snippet: {result.snippet}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // TypeScript provides full intellisense and type checking
  const searchResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({
      query: "artificial intelligence"
  });

  // Access typed properties with intellisense
  const result = searchResponse.results[0];
  console.log(`Title: ${result.title}`);
  console.log(`URL: ${result.url}`);
  console.log(`Snippet: ${result.snippet}`);
  ```
</CodeGroup>

### Runtime Type Validation

Python SDK uses Pydantic for runtime type validation:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse

  client = Perplexity()

  # Runtime validation ensures type safety
  try:
      search_response = client.search.create(
          query="machine learning",
          max_results=10
      )
      
      # Pydantic model methods for serialization
      json_data = search_response.to_json()
      dict_data = search_response.to_dict()
      
      # Type validation on field access
      first_result = search_response.results[0]
      print(f"Result type: {type(first_result)}")
      
  except ValueError as e:
      print(f"Type validation error: {e}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // TypeScript compile-time type checking
  const searchResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({
      query: "machine learning",
      max_results: 10  // TypeScript ensures correct property names
  });

  // Serialization (already plain objects)
  const jsonData = JSON.stringify(searchResponse);
  const objectData = searchResponse; // Already a plain object

  // Type safety at compile time
  const firstResult = searchResponse.results[0];
  console.log(`Result type available in IDE: ${typeof firstResult}`);
  ```
</CodeGroup>

## Advanced Type Patterns

### Generic Type Helpers

Create reusable typed functions:

<CodeGroup>
  ```python Python theme={null}
  from typing import TypeVar, Generic, List, Optional, Callable
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse, ChatCompletionCreateResponse

  T = TypeVar('T')
  R = TypeVar('R')

  class TypedPerplexityClient:
      def __init__(self, client: Perplexity):
          self.client = client
      
      def search_with_transform(
          self, 
          query: str, 
          transform: Callable[[SearchCreateResponse], T]
      ) -> T:
          """Perform search and transform the result with type safety"""
          response = self.client.search.create(query=query)
          return transform(response)
      
      def batch_search(
          self, 
          queries: List[str]
      ) -> List[SearchCreateResponse]:
          """Perform multiple searches with proper typing"""
          results = []
          for query in queries:
              response = self.client.search.create(query=query)
              results.append(response)
          return results

  # Usage with type safety
  client = TypedPerplexityClient(Perplexity())

  def extract_titles(response: SearchCreateResponse) -> List[str]:
      return [result.title for result in response.results]

  # Typed function call
  titles: List[str] = client.search_with_transform("AI research", extract_titles)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class TypedPerplexityClient {
      constructor(private client: Perplexity) {}
      
      async searchWithTransform<T>(
          query: string,
          transform: (response: Perplexity.Search.SearchCreateResponse) => T
      ): Promise<T> {
          const response = await this.client.search.create({ query });
          return transform(response);
      }
      
      async batchSearch(queries: string[]): Promise<Perplexity.Search.SearchCreateResponse[]> {
          const tasks = queries.map(query => 
              this.client.search.create({ query })
          );
          return Promise.all(tasks);
      }
  }

  // Usage with type safety
  const client = new TypedPerplexityClient(new Perplexity());

  function extractTitles(response: Perplexity.Search.SearchCreateResponse): string[] {
      return response.results.map(result => result.title);
  }

  // Typed function call with full intellisense
  const titles: string[] = await client.searchWithTransform("AI research", extractTitles);
  ```
</CodeGroup>

### Custom Type Guards

Create type guards for safer type checking:

<CodeGroup>
  ```python Python theme={null}
  from typing import Union, TypeGuard
  from perplexity.types import (
      SearchCreateResponse, 
      ChatCompletionCreateResponse,
      SearchResult
  )

  def is_search_response(
      response: Union[SearchCreateResponse, ChatCompletionCreateResponse]
  ) -> TypeGuard[SearchCreateResponse]:
      """Type guard to check if response is a search response"""
      return hasattr(response, 'results')

  def is_valid_search_result(result: SearchResult) -> TypeGuard[SearchResult]:
      """Type guard to validate search result structure"""
      return (
          hasattr(result, 'title') and 
          hasattr(result, 'url') and 
          hasattr(result, 'snippet') and
          result.title is not None and
          result.url is not None
      )

  # Usage
  def process_response(
      response: Union[SearchCreateResponse, ChatCompletionCreateResponse]
  ) -> None:
      if is_search_response(response):
          # TypeScript now knows this is SearchCreateResponse
          for result in response.results:
              if is_valid_search_result(result):
                  print(f"Valid result: {result.title}")
              else:
                  print("Invalid result format")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  function isSearchResponse(
      response: Perplexity.Search.SearchCreateResponse | Perplexity.StreamChunk
  ): response is Perplexity.Search.SearchCreateResponse {
      return 'results' in response;
  }

  function isValidSearchResult(result: { title: string; url: string; snippet: string }): boolean {
      return (
          typeof result.title === 'string' &&
          typeof result.url === 'string' &&
          typeof result.snippet === 'string' &&
          result.title.length > 0 &&
          result.url.length > 0
      );
  }

  // Usage
  function processResponse(
      response: Perplexity.Search.SearchCreateResponse | Perplexity.StreamChunk
  ): void {
      if (isSearchResponse(response)) {
          // TypeScript now knows this is SearchCreateResponse
          response.results.forEach(result => {
              if (isValidSearchResult(result)) {
                  console.log(`Valid result: ${result.title}`);
              } else {
                  console.log("Invalid result format");
              }
          });
      }
  }
  ```
</CodeGroup>

## Response Type Utilities

### Extracting Nested Types

Work with nested response structures safely:

<CodeGroup>
  ```python Python theme={null}
  from typing import List, Optional
  from perplexity import Perplexity
  from perplexity.types import (
      SearchCreateResponse,
      SearchResult,
      ChatCompletionCreateResponse,
      ChatCompletionChoice
  )

  class ResponseUtils:
      @staticmethod
      def extract_search_titles(response: SearchCreateResponse) -> List[str]:
          """Extract all search result titles with type safety"""
          return [result.title for result in response.results if result.title]
      
      @staticmethod
      def extract_search_urls(response: SearchCreateResponse) -> List[str]:
          """Extract all search result URLs with type safety"""
          return [result.url for result in response.results if result.url]
      
      @staticmethod
      def get_first_search_result(
          response: SearchCreateResponse
      ) -> Optional[SearchResult]:
          """Get first search result safely"""
          return response.results[0] if response.results else None
      
      @staticmethod
      def extract_chat_content(
          response: ChatCompletionCreateResponse
      ) -> Optional[str]:
          """Extract chat completion content safely"""
          if response.choices and response.choices[0].message:
              return response.choices[0].message.content
          return None

  # Usage
  client = Perplexity()
  search_response = client.search.create(query="Python programming")

  titles = ResponseUtils.extract_search_titles(search_response)
  urls = ResponseUtils.extract_search_urls(search_response)
  first_result = ResponseUtils.get_first_search_result(search_response)

  print(f"Found {len(titles)} results")
  if first_result:
      print(f"First result: {first_result.title}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class ResponseUtils {
      static extractSearchTitles(response: Perplexity.Search.SearchCreateResponse): string[] {
          return response.results
              .filter(result => result.title)
              .map(result => result.title);
      }
      
      static extractSearchUrls(response: Perplexity.Search.SearchCreateResponse): string[] {
          return response.results
              .filter(result => result.url)
              .map(result => result.url);
      }
      
      static getFirstSearchResult(
          response: Perplexity.Search.SearchCreateResponse
      ) {
          return response.results[0];
      }
      
      static extractChatContent(
          response: Perplexity.StreamChunk
      ): string | undefined {
          const content = response.choices[0]?.message?.content;
          // Handle content which can be string, array of chunks, or null
          if (typeof content === 'string') {
              return content;
          }
          if (Array.isArray(content)) {
              // Extract text from content chunks
              return content
                  .filter(chunk => chunk.type === 'text' && 'text' in chunk)
                  .map(chunk => (chunk as { text: string }).text)
                  .join('');
          }
          return undefined;
      }
  }

  // Usage
  const client = new Perplexity();
  const searchResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({ 
      query: "Python programming" 
  });

  const titles = ResponseUtils.extractSearchTitles(searchResponse);
  const urls = ResponseUtils.extractSearchUrls(searchResponse);
  const firstResult = ResponseUtils.getFirstSearchResult(searchResponse);

  console.log(`Found ${titles.length} results`);
  if (firstResult) {
      console.log(`First result: ${firstResult.title}`);
  }
  ```
</CodeGroup>

### Custom Response Mappers

Create typed mappers for domain-specific data structures:

<CodeGroup>
  ```python Python theme={null}
  from typing import List, Optional, Dict, Any
  from dataclasses import dataclass
  from perplexity.types import SearchCreateResponse, SearchResult

  @dataclass
  class SimplifiedSearchResult:
      title: str
      url: str
      snippet: str
      domain: str

  @dataclass
  class SearchSummary:
      query: str
      total_results: int
      results: List[SimplifiedSearchResult]
      domains: List[str]

  class SearchResponseMapper:
      @staticmethod
      def to_simplified(response: SearchCreateResponse) -> SearchSummary:
          """Convert API response to simplified domain model"""
          simplified_results = []
          domains = set()
          
          for result in response.results:
              if result.title and result.url and result.snippet:
                  # Extract domain from URL
                  try:
                      from urllib.parse import urlparse
                      domain = urlparse(result.url).netloc
                      domains.add(domain)
                      
                      simplified_results.append(SimplifiedSearchResult(
                          title=result.title,
                          url=result.url,
                          snippet=result.snippet,
                          domain=domain
                      ))
                  except Exception:
                      # Skip invalid URLs
                      continue
          
          return SearchSummary(
              query=response.query,
              total_results=len(simplified_results),
              results=simplified_results,
              domains=list(domains)
          )

  # Usage with type safety
  client = Perplexity()
  api_response = client.search.create(query="machine learning frameworks")
  summary: SearchSummary = SearchResponseMapper.to_simplified(api_response)

  print(f"Query: {summary.query}")
  print(f"Results: {summary.total_results}")
  print(f"Unique domains: {len(summary.domains)}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  interface SimplifiedSearchResult {
      title: string;
      url: string;
      snippet: string;
      domain: string;
  }

  interface SearchSummary {
      query: string;
      totalResults: number;
      results: SimplifiedSearchResult[];
      domains: string[];
  }

  class SearchResponseMapper {
      static toSimplified(response: Perplexity.Search.SearchCreateResponse): SearchSummary {
          const simplifiedResults: SimplifiedSearchResult[] = [];
          const domains = new Set<string>();
          
          for (const result of response.results) {
              if (result.title && result.url && result.snippet) {
                  try {
                      const domain = new URL(result.url).hostname;
                      domains.add(domain);
                      
                      simplifiedResults.push({
                          title: result.title,
                          url: result.url,
                          snippet: result.snippet,
                          domain
                      });
                  } catch {
                      // Skip invalid URLs
                      continue;
                  }
              }
          }
          
          return {
              query: response.id, // response.id contains the search identifier
              totalResults: simplifiedResults.length,
              results: simplifiedResults,
              domains: Array.from(domains)
          };
      }
  }

  // Usage with type safety
  const client = new Perplexity();
  const apiResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({ 
      query: "machine learning frameworks" 
  });
  const summary: SearchSummary = SearchResponseMapper.toSimplified(apiResponse);

  console.log(`ID: ${summary.query}`);
  console.log(`Results: ${summary.totalResults}`);
  console.log(`Unique domains: ${summary.domains.length}`);
  ```
</CodeGroup>

## IDE Integration

### Enhanced Development Experience

Maximize IDE support with proper type usage:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse
  from typing import TYPE_CHECKING

  if TYPE_CHECKING:
      # Import types only for type checking (no runtime cost)
      from perplexity.types import ChatCompletionCreateResponse

  class EnhancedClient:
      def __init__(self):
          self.client = Perplexity()
      
      def search(self, query: str, **kwargs) -> SearchCreateResponse:
          """
          Perform search with full type hints
          
          Args:
              query: Search query string
              **kwargs: Additional search parameters
              
          Returns:
              SearchCreateResponse: Typed search results
          """
          return self.client.search.create(query=query, **kwargs)
      
      def chat(self, message: str, model: str = "sonar-pro") -> "ChatCompletionCreateResponse":
          """
          Chat completion with type hints
          
          Args:
              message: User message
              model: Model to use for completion
              
          Returns:
              ChatCompletionCreateResponse: Typed chat response
          """
          return self.client.chat.completions.create(
              model=model,
              messages=[{"role": "user", "content": message}]
          )

  # Usage with full IDE support
  enhanced_client = EnhancedClient()

  # IDE provides full autocomplete and type checking
  search_result = enhanced_client.search("Python tutorials")
  print(search_result.results[0].title)  # Full intellisense available

  chat_result = enhanced_client.chat("Explain decorators")
  # Access content safely (can be string, list, or None)
  content = chat_result.choices[0].message.content
  if isinstance(content, str):
      print(content)  # Type-safe access
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class EnhancedClient {
      private client: Perplexity;
      
      constructor() {
          this.client = new Perplexity();
      }
      
      /**
       * Perform search with full type hints
       */
      async search(
          query: string, 
          options?: Partial<Perplexity.Search.SearchCreateParams>
      ): Promise<Perplexity.Search.SearchCreateResponse> {
          return this.client.search.create({ 
              query, 
              ...options 
          });
      }
      
      /**
       * Chat completion with type hints
       */
      async chat(
          message: string, 
          model: string = "sonar"
      ): Promise<Perplexity.StreamChunk> {
          return this.client.chat.completions.create({
              model,
              messages: [{ role: "user", content: message }]
          });
      }
  }

  // Usage with full IDE support
  const enhancedClient = new EnhancedClient();

  // IDE provides full autocomplete and type checking
  const searchResult = await enhancedClient.search("Python tutorials");
  console.log(searchResult.results[0].title); // Full intellisense available

  const chatResult = await enhancedClient.chat("Explain decorators");
  // Content can be string, array of chunks, or null - handle appropriately
  const content = chatResult.choices[0]?.message?.content;
  if (typeof content === 'string') {
      console.log(content); // Type-safe access
  }
  ```
</CodeGroup>

## Type Safety Best Practices

<Steps>
  <Step title="Always use type imports">
    Import and use specific types for better IDE support and error catching.

    <CodeGroup>
      ```python Python theme={null}
      # Good: Specific type imports
      from perplexity.types import SearchCreateResponse, SearchResult

      def process_search(response: SearchCreateResponse) -> List[str]:
          return [result.title for result in response.results]
      ```

      ```typescript TypeScript/JavaScript theme={null}
      // Good: Use namespace types for type safety
      import Perplexity from '@perplexity-ai/perplexity_ai';

      function processSearch(response: Perplexity.Search.SearchCreateResponse): string[] {
          return response.results.map(result => result.title);
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Use type guards for runtime safety">
    Implement proper type checking for dynamic data.

    <Warning>
      TypeScript types are compile-time only. Use type guards for runtime validation.
    </Warning>
  </Step>

  <Step title="Leverage generic types">
    Create reusable typed functions and classes for common patterns.

    <Tip>
      Generic types help maintain type safety while providing flexibility.
    </Tip>
  </Step>

  <Step title="Document with types">
    Use type annotations as documentation for better code maintainability.

    <CodeGroup>
      ```python Python theme={null}
      def analyze_search_results(
          response: SearchCreateResponse,
          min_score: float = 0.5
      ) -> Dict[str, Any]:
          """
          Analyze search results with scoring
          
          Args:
              response: Search API response
              min_score: Minimum quality score threshold
              
          Returns:
              Analysis results with scores and recommendations
          """
          # Implementation with type safety
      ```

      ```typescript TypeScript/JavaScript theme={null}
      /**
       * Analyze search results with scoring
       */
      function analyzeSearchResults(
          response: Perplexity.Search.SearchCreateResponse,
          minScore: number = 0.5
      ): { scores: number[]; recommendations: string[] } {
          // Implementation with type safety
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Error Handling" icon="triangle-exclamation" href="/docs/sdk/error-handling">
    Type-safe error handling patterns
  </Card>

  <Card title="Best Practices" icon="star" href="/docs/sdk/best-practices">
    Type safety in production code
  </Card>
</CardGroup>


# Best Practices
Source: https://docs.perplexity.ai/docs/search/best-practices

Learn best practices for optimizing search queries and implementing efficient async patterns with Perplexity's Search API.

## Overview

This guide covers essential best practices for getting the most out of Perplexity's Search API, including query optimization techniques and efficient async usage patterns for high-performance applications.

## Query Optimization

<Steps>
  <Step title="Write specific queries">
    Use highly specific queries for more targeted results. For example, instead of searching for "AI", use a detailed query like "artificial intelligence machine learning healthcare applications 2024".

    <CodeGroup>
      ```python Python theme={null}
      # Better: Specific query
      search = client.search.create(
          query="artificial intelligence medical diagnosis accuracy 2024",
          max_results=10
      )

      # Avoid: Vague query
      search = client.search.create(
          query="AI medical",
          max_results=10
      )
      ```

      ```typescript TypeScript theme={null}
      // Better: Specific query
      const search = await client.search.create({
          query: "artificial intelligence medical diagnosis accuracy 2024",
          maxResults: 10
      });

      // Avoid: Vague query
      const search = await client.search.create({
          query: "AI medical",
          maxResults: 10
      });
      ```
    </CodeGroup>

    <Tip>
      Specific queries with context, time frames, and precise terminology yield more relevant and actionable results.
    </Tip>
  </Step>

  <Step title="Use multi-query for comprehensive research">
    Break your main topic into related sub-queries to cover all aspects of your research. Use the multi-query search feature to run multiple related queries in a single request for more comprehensive and relevant information.

    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      # Comprehensive research with related queries
      search = client.search.create(
          query=[
              "artificial intelligence medical diagnosis accuracy 2024",
              "machine learning healthcare applications FDA approval",
              "AI medical imaging radiology deployment hospitals"
          ],
          max_results=5
      )

      # Access results for each query
      for i, query_results in enumerate(search.results):
          print(f"Results for query {i+1}:")
          for result in query_results:
              print(f"  {result.title}: {result.url}")
          print("---")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      // Comprehensive research with related queries
      const search = await client.search.create({
          query: [
              "artificial intelligence medical diagnosis accuracy 2024",
              "machine learning healthcare applications FDA approval",
              "AI medical imaging radiology deployment hospitals"
          ],
          maxResults: 5
      });

      // Access results for each query
      search.results.forEach((queryResults, i) => {
          console.log(`Results for query ${i+1}:`);
          queryResults.forEach(result => {
              console.log(`  ${result.title}: ${result.url}`);
          });
          console.log("---");
      });
      ```
    </CodeGroup>

    <Info>
      You can include up to 5 queries in a single multi-query request for efficient batch processing.
    </Info>
  </Step>

  <Step title="Handle rate limits efficiently">
    Implement exponential backoff for rate limit errors and use appropriate batching strategies.

    <CodeGroup>
      ```python Python theme={null}
      import time
      import random
      from perplexity import RateLimitError

      def search_with_retry(client, query, max_retries=3):
          for attempt in range(max_retries):
              try:
                  return client.search.create(query=query)
              except RateLimitError:
                  if attempt < max_retries - 1:
                      # Exponential backoff with jitter
                      delay = (2 ** attempt) + random.uniform(0, 1)
                      time.sleep(delay)
                  else:
                      raise

      # Usage
      try:
          search = search_with_retry(client, "AI developments")
          for result in search.results:
              print(f"{result.title}: {result.url}")
      except RateLimitError:
          print("Maximum retries exceeded for search")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      async function searchWithRetry(
          client: Perplexity, 
          query: string, 
          maxRetries: number = 3
      ) {
          for (let attempt = 0; attempt < maxRetries; attempt++) {
              try {
                  return await client.search.create({ query });
              } catch (error) {
                  if (error instanceof Perplexity.RateLimitError && attempt < maxRetries - 1) {
                      // Exponential backoff with jitter
                      const delay = (2 ** attempt) + Math.random();
                      await new Promise(resolve => setTimeout(resolve, delay * 1000));
                  } else {
                      throw error;
                  }
              }
          }
          throw new Error("Max retries exceeded");
      }

      // Usage
      try {
          const search = await searchWithRetry(client, "AI developments");
          search.results.forEach(result => {
              console.log(`${result.title}: ${result.url}`);
          });
      } catch (error) {
          console.log("Maximum retries exceeded for search");
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Process concurrent searches efficiently">
    Use async for concurrent requests while respecting rate limits.

    <CodeGroup>
      ```python Python theme={null}
      import asyncio
      from perplexity import AsyncPerplexity

      async def batch_search(queries, batch_size=3, delay_ms=1000):
          async with AsyncPerplexity() as client:
              results = []
              
              for i in range(0, len(queries), batch_size):
                  batch = queries[i:i + batch_size]
                  
                  batch_tasks = [
                      client.search.create(query=query, max_results=5)
                      for query in batch
                  ]
                  
                  batch_results = await asyncio.gather(*batch_tasks)
                  results.extend(batch_results)
                  
                  # Add delay between batches
                  if i + batch_size < len(queries):
                      await asyncio.sleep(delay_ms / 1000)
              
              return results

      # Usage
      queries = ["AI developments", "climate change", "space exploration"]
      results = asyncio.run(batch_search(queries))
      print(f"Processed {len(results)} searches")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      async function batchSearch(
          queries: string[],
          batchSize: number = 3,
          delayMs: number = 1000
      ) {
          const client = new Perplexity();
          const results = [];
          
          for (let i = 0; i < queries.length; i += batchSize) {
              const batch = queries.slice(i, i + batchSize);
              
              const batchPromises = batch.map(query =>
                  client.search.create({
                      query,
                      maxResults: 5
                  })
              );
              
              const batchResults = await Promise.all(batchPromises);
              results.push(...batchResults);
              
              // Add delay between batches
              if (i + batchSize < queries.length) {
                  await new Promise(resolve => setTimeout(resolve, delayMs));
              }
          }
          
          return results;
      }

      // Usage
      const queries = ["AI developments", "climate change", "space exploration"];
      const results = await batchSearch(queries);
      console.log(`Processed ${results.length} searches`);
      ```
    </CodeGroup>
  </Step>
</Steps>

## Async Usage

For high-performance applications requiring concurrent requests, use the async client:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity

  async def main():
      async with AsyncPerplexity() as client:
          # Concurrent searches for better performance
          tasks = [
              client.search.create(
                  query="artificial intelligence trends 2024",
                  max_results=5
              ),
              client.search.create(
                  query="machine learning breakthroughs",
                  max_results=5
              ),
              client.search.create(
                  query="deep learning applications",
                  max_results=5
              )
          ]
          
          results = await asyncio.gather(*tasks)
          
          for i, search in enumerate(results):
              print(f"Query {i+1} results:")
              for result in search.results:
                  print(f"  {result.title}: {result.url}")
              print("---")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  async function main() {
      // Concurrent searches for better performance
      const tasks = [
          client.search.create({
              query: "artificial intelligence trends 2024",
              maxResults: 5
          }),
          client.search.create({
              query: "machine learning breakthroughs",
              maxResults: 5
          }),
          client.search.create({
              query: "deep learning applications",
              maxResults: 5
          })
      ];
      
      const results = await Promise.all(tasks);
      
      results.forEach((search, i) => {
          console.log(`Query ${i+1} results:`);
          search.results.forEach(result => {
              console.log(`  ${result.title}: ${result.url}`);
          });
          console.log("---");
      });
  }

  main();
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  const client = new Perplexity();

  async function main() {
      // Concurrent searches for better performance
      const tasks = [
          client.search.create({
              query: "artificial intelligence trends 2024",
              maxResults: 5
          }),
          client.search.create({
              query: "machine learning breakthroughs",
              maxResults: 5
          }),
          client.search.create({
              query: "deep learning applications",
              maxResults: 5
          })
      ];
      
      const results = await Promise.all(tasks);
      
      results.forEach((search, i) => {
          console.log(`Query ${i+1} results:`);
          search.results.forEach(result => {
              console.log(`  ${result.title}: ${result.url}`);
          });
          console.log("---");
      });
  }

  main();
  ```
</CodeGroup>

### Advanced Async Patterns

#### Rate-Limited Concurrent Processing

For large-scale applications, implement controlled concurrency with rate limiting:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity

  class SearchManager:
      def __init__(self, max_concurrent=5, delay_between_batches=1.0):
          self.max_concurrent = max_concurrent
          self.delay_between_batches = delay_between_batches
          self.semaphore = asyncio.Semaphore(max_concurrent)
      
      async def search_single(self, client, query):
          async with self.semaphore:
              return await client.search.create(query=query, max_results=5)
      
      async def search_many(self, queries):
          async with AsyncPerplexity() as client:
              tasks = [
                  self.search_single(client, query) 
                  for query in queries
              ]
              
              results = await asyncio.gather(*tasks, return_exceptions=True)
              
              # Filter out exceptions and return successful results
              successful_results = [
                  result for result in results 
                  if not isinstance(result, Exception)
              ]
              
              return successful_results

  # Usage
  async def main():
      manager = SearchManager(max_concurrent=3)
      queries = [
          "AI research 2024",
          "quantum computing advances",
          "renewable energy innovations",
          "biotechnology breakthroughs",
          "space exploration updates"
      ]
      
      results = await manager.search_many(queries)
      print(f"Successfully processed {len(results)} out of {len(queries)} searches")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class SearchManager {
      private maxConcurrent: number;
      private delayBetweenBatches: number;
      
      constructor(maxConcurrent: number = 5, delayBetweenBatches: number = 1000) {
          this.maxConcurrent = maxConcurrent;
          this.delayBetweenBatches = delayBetweenBatches;
      }
      
      async searchMany(queries: string[]) {
          const client = new Perplexity();
          const results = [];
          
          // Process in batches to respect rate limits
          for (let i = 0; i < queries.length; i += this.maxConcurrent) {
              const batch = queries.slice(i, i + this.maxConcurrent);
              
              const batchPromises = batch.map(query =>
                  client.search.create({ query, maxResults: 5 })
                      .catch(error => ({ error, query }))
              );
              
              const batchResults = await Promise.all(batchPromises);
              
              // Filter out errors and collect successful results
              const successfulResults = batchResults.filter(
                  result => !('error' in result)
              );
              
              results.push(...successfulResults);
              
              // Add delay between batches
              if (i + this.maxConcurrent < queries.length) {
                  await new Promise(resolve => 
                      setTimeout(resolve, this.delayBetweenBatches)
                  );
              }
          }
          
          return results;
      }
  }

  // Usage
  async function main() {
      const manager = new SearchManager(3, 1000);
      const queries = [
          "AI research 2024",
          "quantum computing advances", 
          "renewable energy innovations",
          "biotechnology breakthroughs",
          "space exploration updates"
      ];
      
      const results = await manager.searchMany(queries);
      console.log(`Successfully processed ${results.length} out of ${queries.length} searches`);
  }

  main();
  ```
</CodeGroup>

#### Error Handling in Async Operations

Implement robust error handling for async search operations:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import logging
  from perplexity import AsyncPerplexity, APIStatusError, RateLimitError

  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger(__name__)

  async def resilient_search(client, query, max_retries=3):
      for attempt in range(max_retries):
          try:
              result = await client.search.create(query=query, max_results=5)
              logger.info(f"Search successful for: {query}")
              return result
              
          except RateLimitError as e:
              if attempt < max_retries - 1:
                  delay = 2 ** attempt
                  logger.warning(f"Rate limited for '{query}', retrying in {delay}s")
                  await asyncio.sleep(delay)
              else:
                  logger.error(f"Max retries exceeded for: {query}")
                  return None
                  
          except APIStatusError as e:
              logger.error(f"API error for '{query}': {e}")
              return None
              
          except Exception as e:
              logger.error(f"Unexpected error for '{query}': {e}")
              return None

  async def main():
      async with AsyncPerplexity() as client:
          queries = ["AI developments", "invalid query", "tech trends"]
          
          tasks = [resilient_search(client, query) for query in queries]
          results = await asyncio.gather(*tasks)
          
          successful_results = [r for r in results if r is not None]
          print(f"Successful searches: {len(successful_results)}/{len(queries)}")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function resilientSearch(
      client: Perplexity, 
      query: string, 
      maxRetries: number = 3
  ) {
      for (let attempt = 0; attempt < maxRetries; attempt++) {
          try {
              const result = await client.search.create({ query, maxResults: 5 });
              console.log(`Search successful for: ${query}`);
              return result;
              
          } catch (error: any) {
              if (error.constructor.name === 'RateLimitError') {
                  if (attempt < maxRetries - 1) {
                      const delay = 2 ** attempt * 1000;
                      console.warn(`Rate limited for '${query}', retrying in ${delay}ms`);
                      await new Promise(resolve => setTimeout(resolve, delay));
                  } else {
                      console.error(`Max retries exceeded for: ${query}`);
                      return null;
                  }
              } else {
                  console.error(`Error for '${query}':`, error.message);
                  return null;
              }
          }
      }
      
      return null;
  }

  async function main() {
      const client = new Perplexity();
      const queries = ["AI developments", "invalid query", "tech trends"];
      
      const tasks = queries.map(query => resilientSearch(client, query));
      const results = await Promise.all(tasks);
      
      const successfulResults = results.filter(r => r !== null);
      console.log(`Successful searches: ${successfulResults.length}/${queries.length}`);
  }

  main();
  ```
</CodeGroup>

## Performance Optimization Tips

<Steps>
  <Step title="Optimize result count">
    Request only the number of results you actually need. More results = longer response times.

    ```python theme={null}
    # Good: Request only what you need
    search = client.search.create(query="tech news", max_results=5)

    # Avoid: Over-requesting results
    search = client.search.create(query="tech news", max_results=50)
    ```
  </Step>

  <Step title="Cache frequently used searches">
    Implement caching for queries that don't need real-time results.

    <CodeGroup>
      ```python Python theme={null}
      import time
      from typing import Dict, Tuple, Optional

      class SearchCache:
          def __init__(self, ttl_seconds=3600):  # 1 hour default
              self.cache: Dict[str, Tuple[any, float]] = {}
              self.ttl = ttl_seconds
          
          def get(self, query: str) -> Optional[any]:
              if query in self.cache:
                  result, timestamp = self.cache[query]
                  if time.time() - timestamp < self.ttl:
                      return result
                  else:
                      del self.cache[query]
              return None
          
          def set(self, query: str, result: any):
              self.cache[query] = (result, time.time())

      # Usage
      cache = SearchCache(ttl_seconds=1800)  # 30 minutes

      def cached_search(client, query):
          cached_result = cache.get(query)
          if cached_result:
              return cached_result
          
          result = client.search.create(query=query)
          cache.set(query, result)
          return result
      ```

      ```typescript TypeScript theme={null}
      class SearchCache {
          private cache: Map<string, { result: any; timestamp: number }> = new Map();
          private ttl: number;
          
          constructor(ttlSeconds: number = 3600) {  // 1 hour default
              this.ttl = ttlSeconds * 1000;  // Convert to milliseconds
          }
          
          get(query: string): any | null {
              const cached = this.cache.get(query);
              if (cached) {
                  if (Date.now() - cached.timestamp < this.ttl) {
                      return cached.result;
                  } else {
                      this.cache.delete(query);
                  }
              }
              return null;
          }
          
          set(query: string, result: any): void {
              this.cache.set(query, { result, timestamp: Date.now() });
          }
      }

      // Usage
      const cache = new SearchCache(1800);  // 30 minutes

      async function cachedSearch(client: Perplexity, query: string) {
          const cachedResult = cache.get(query);
          if (cachedResult) {
              return cachedResult;
          }
          
          const result = await client.search.create({ query });
          cache.set(query, result);
          return result;
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/search/quickstart">
    Get started with basic search functionality
  </Card>

  <Card title="Perplexity SDK" icon="code" href="/docs/sdk/overview">
    Explore the full SDK capabilities for enhanced performance
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/search-post">
    Complete Search API documentation
  </Card>
</CardGroup>


# Search Date and Time Filters
Source: https://docs.perplexity.ai/docs/search/filters/date-time-filters



<Note>
  The `search_after_date_filter` and `search_before_date_filter` parameters allow you to restrict search results to a specific publication date range. Only results with publication dates falling between these dates will be returned.

  The `last_updated_after_filter` and `last_updated_before_filter` parameters allow you to filter by when content was last modified or updated, rather than when it was originally published.

  The `search_recency_filter` parameter provides a convenient way to filter results by predefined time periods (e.g., "day", "week", "month", "year") relative to the current date.
</Note>

<Info>
  Specific date filters must be provided in the "%m/%d/%Y" format (e.g., "3/1/2025"). Recency filters use predefined values like "day", "week", "month", or "year". All filters are optional—you may supply either specific dates or recency filters as needed.
</Info>

## Overview

Date and time filters for the Search API allow you to control which search results are returned by limiting them to specific time periods. There are three types of date and time filters available:

### Publication Date Filters

The `search_after_date_filter` and `search_before_date_filter` parameters filter results based on when content was **originally created or published**. This is useful when you need to:

* Find content published within a specific timeframe
* Exclude outdated or overly recent publications
* Focus on content from a particular publication period

### Last Updated Date Filters

The `last_updated_after_filter` and `last_updated_before_filter` parameters filter results based on when content was **last modified or updated**. This is useful when you need to:

* Find recently updated or maintained content
* Exclude stale content that hasn't been updated recently
* Focus on content that has been refreshed within a specific period

### Search Recency Filter

The `search_recency_filter` parameter provides a simple way to filter results by predefined time periods relative to the current date. This is useful when you need to:

* Find content from the past day, week, month, or year
* Get recent results without specifying exact dates
* Quickly filter for timely information

**Available values:**

* `"day"` - Content from the past 24 hours
* `"week"` - Content from the past 7 days
* `"month"` - Content from the past 30 days
* `"year"` - Content from the past 365 days

**Important:** Publication filters use the original creation/publication date, last updated filters use the modification date, while recency filters use a relative time period from the current date.

To constrain search results by publication date:

```bash theme={null}
"search_after_date_filter": "3/1/2025",
"search_before_date_filter": "3/5/2025"
```

To constrain search results by last updated date:

```bash theme={null}
"last_updated_after_filter": "07/01/2025",
"last_updated_before_filter": "12/30/2025"
```

To constrain search results by recency:

```bash theme={null}
"search_recency_filter": "week"
```

These filters will be applied in addition to any other search parameters.

## Examples

**1. Limiting Results by Publication Date Range**

This example limits search results to content published between March 1, 2025, and March 5, 2025.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search(
      query="latest AI developments",
      max_results=10,
      search_after_date_filter="3/1/2025",
      search_before_date_filter="3/5/2025"
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search({
    query: "latest AI developments",
    max_results: 10,
    search_after_date_filter: "3/1/2025",
    search_before_date_filter: "3/5/2025"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "latest AI developments",
      "max_results": 10,
      "search_after_date_filter": "3/1/2025",
      "search_before_date_filter": "3/5/2025"
    }' | jq
  ```
</CodeGroup>

**2. Filtering with a Single Publication Date Parameter**

If you only wish to restrict the results to those published on or after a specific date, include just the `search_after_date_filter`:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search(
      query="tech news published after March 1, 2025",
      max_results=10,
      search_after_date_filter="3/1/2025"
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search({
    query: "tech news published after March 1, 2025",
    max_results: 10,
    search_after_date_filter: "3/1/2025"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "tech news published after March 1, 2025",
      "max_results": 10,
      "search_after_date_filter": "3/1/2025"
    }' | jq
  ```
</CodeGroup>

**3. Filtering by Last Updated Date Range**

This example limits search results to content that was last updated between July 1, 2025, and December 30, 2025. This is useful for finding recently maintained or refreshed content.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search(
      query="recently updated tech articles",
      max_results=10,
      last_updated_after_filter="07/01/2025",
      last_updated_before_filter="12/30/2025"
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search({
    query: "recently updated tech articles",
    max_results: 10,
    last_updated_after_filter: "07/01/2025",
    last_updated_before_filter: "12/30/2025"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "recently updated tech articles",
      "max_results": 10,
      "last_updated_after_filter": "07/01/2025",
      "last_updated_before_filter": "12/30/2025"
    }' | jq
  ```
</CodeGroup>

**4. Using Search Recency Filter**

The `search_recency_filter` provides a convenient way to filter results by predefined time periods without specifying exact dates:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search(
      query="latest AI developments",
      max_results=10,
      search_recency_filter="week"
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search({
    query: "latest AI developments",
    max_results: 10,
    search_recency_filter: "week"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "latest AI developments",
      "max_results": 10,
      "search_recency_filter": "week"
    }' | jq
  ```
</CodeGroup>

This example will return only content from the past 7 days, automatically calculated from the current date.

**5. Different Recency Filter Options**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Get content from the past day
  day_response = client.search(
      query="breaking tech news",
      max_results=5,
      search_recency_filter="day"
  )

  # Get content from the past month
  month_response = client.search(
      query="AI research developments",
      max_results=10,
      search_recency_filter="month"
  )

  # Get content from the past year
  year_response = client.search(
      query="major tech trends",
      max_results=15,
      search_recency_filter="year"
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Get content from the past day
  const dayResponse = await client.search({
    query: "breaking tech news",
    max_results: 5,
    search_recency_filter: "day"
  });

  // Get content from the past month
  const monthResponse = await client.search({
    query: "AI research developments",
    max_results: 10,
    search_recency_filter: "month"
  });

  // Get content from the past year
  const yearResponse = await client.search({
    query: "major tech trends",
    max_results: 15,
    search_recency_filter: "year"
  });
  ```

  ```bash cURL theme={null}
  # Get content from the past day
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "breaking tech news",
      "max_results": 5,
      "search_recency_filter": "day"
    }' | jq

  # Get content from the past month
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "AI research developments",
      "max_results": 10,
      "search_recency_filter": "month"
    }' | jq
  ```
</CodeGroup>

## Parameter Reference

### `search_after_date_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "3/1/2025")
* **Description**: Filters search results to only include content published after this date
* **Optional**: Yes
* **Example**: `"search_after_date_filter": "1/1/2025"`

### `search_before_date_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "3/1/2025")
* **Description**: Filters search results to only include content published before this date
* **Optional**: Yes
* **Example**: `"search_before_date_filter": "12/31/2025"`

### `last_updated_after_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "07/01/2025")
* **Description**: Filters search results to only include content last updated after this date
* **Optional**: Yes
* **Example**: `"last_updated_after_filter": "07/01/2025"`

### `last_updated_before_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "12/30/2025")
* **Description**: Filters search results to only include content last updated before this date
* **Optional**: Yes
* **Example**: `"last_updated_before_filter": "12/30/2025"`

### `search_recency_filter`

* **Type**: String
* **Allowed Values**: "day", "week", "month", "year"
* **Description**: Filters search results to content from the specified time period relative to the current date
* **Optional**: Yes
* **Example**: `"search_recency_filter": "week"`

## Best Practices

**Date Format**

* Strict Format: Dates must match the "%m/%d/%Y" format exactly. For example, "3/1/2025" or "03/01/2025" is acceptable.
* Consistency: Use one or both date filters consistently based on your search needs. Combining both provides a clear range.

**Filter Selection**

* Choose the Right Filter Type: Use publication date filters (`search_after_date_filter`/`search_before_date_filter`) when you care about when content was originally created. Use last updated filters (`last_updated_after_filter`/`last_updated_before_filter`) when you need recently maintained content. Use recency filters (`search_recency_filter`) for quick, relative time filtering.
* Recency vs. Exact Dates: Use `search_recency_filter` for convenience when you want recent content (e.g., "past week"). Use specific date filters when you need precise control over the time range.
* Combining Filters: You can use both publication and last updated filters together to find content that meets both criteria (e.g., published in 2024 but updated recently). Note that `search_recency_filter` cannot be combined with specific date filters (`search_after_date_filter`/`search_before_date_filter` or `last_updated_after_filter`/`last_updated_before_filter`).

**Client-Side Validation**

* Regex Check: Validate date strings on the client side using a regex such as:

<CodeGroup>
  ```bash theme={null}
  date_regex='^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/[0-9]{4}$'
  ```

  ```python theme={null}
  date_regex = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/\d{4}$'
  ```
</CodeGroup>

This ensures that dates conform to the required format before sending the request.

**Performance Considerations**

* Narrowing the Search: Applying date range filters typically reduces the number of results, which may improve response times and result relevance.
* Avoid Over-Restriction: Ensure that the date range is neither too narrow (limiting useful results) nor too broad (defeating the purpose of the filter).

## Advanced Usage Patterns

**Finding Breaking News**

Use the `search_recency_filter` with "day" to find the most recent breaking news:

```python theme={null}
response = client.search(
    query="breaking news technology",
    max_results=5,
    search_recency_filter="day"
)
```

**Historical Research**

Use specific date ranges to research historical events or trends:

```python theme={null}
response = client.search(
    query="AI developments",
    max_results=20,
    search_after_date_filter="1/1/2023",
    search_before_date_filter="12/31/2023"
)
```

**Finding Recently Maintained Content**

Use last updated filters to find content that has been refreshed or maintained recently:

```python theme={null}
response = client.search(
    query="React best practices",
    max_results=10,
    last_updated_after_filter="07/01/2025"
)
```

**Trend Analysis**

Compare different time periods by making multiple searches:

```python theme={null}
# Recent trends
recent = client.search(
    query="machine learning trends",
    search_recency_filter="month"
)

# Older trends for comparison
older = client.search(
    query="machine learning trends",
    search_after_date_filter="1/1/2023",
    search_before_date_filter="1/31/2023"
)
```

## Error Handling

When using date filters, ensure proper error handling for invalid date formats:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  import re

  def validate_date_format(date_string):
      pattern = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/\d{4}$'
      return bool(re.match(pattern, date_string))

  def search_with_date_filter(query, after_date=None, before_date=None):
      client = Perplexity()
      
      # Validate date formats
      if after_date and not validate_date_format(after_date):
          raise ValueError(f"Invalid date format: {after_date}")
      if before_date and not validate_date_format(before_date):
          raise ValueError(f"Invalid date format: {before_date}")
      
      try:
          response = client.search(
              query=query,
              search_after_date_filter=after_date,
              search_before_date_filter=before_date
          )
          return response
      except Exception as e:
          print(f"Search failed: {e}")
          return None
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  function validateDateFormat(dateString: string): boolean {
    const pattern = /^(0?[1-9]|1[0-2])\/(0?[1-9]|[12]\d|3[01])\/\d{4}$/;
    return pattern.test(dateString);
  }

  async function searchWithDateFilter(
    query: string, 
    afterDate?: string, 
    beforeDate?: string
  ) {
    const client = new Perplexity();
    
    // Validate date formats
    if (afterDate && !validateDateFormat(afterDate)) {
      throw new Error(`Invalid date format: ${afterDate}`);
    }
    if (beforeDate && !validateDateFormat(beforeDate)) {
      throw new Error(`Invalid date format: ${beforeDate}`);
    }
    
    try {
      const response = await client.search({
        query,
        search_after_date_filter: afterDate,
        search_before_date_filter: beforeDate
      });
      return response;
    } catch (error) {
      console.error('Search failed:', error);
      return null;
    }
  }
  ```
</CodeGroup>


# Search Domain Filter
Source: https://docs.perplexity.ai/docs/search/filters/domain-filter



<Note>
  The `search_domain_filter` parameter allows you to limit search results to specific domains or exclude certain domains from search results. This supports domain-level filtering for precise content control.
</Note>

<Warning>
  You can add a maximum of 20 domains to the `search_domain_filter` list. The filter works in either allowlist mode (include only) or denylist mode (exclude), but not both simultaneously.
</Warning>

<Info>
  Domain filters allow you to specify which domains to include or exclude in search results. You can filter by specific domains, top-level domains (TLDs), or domain parts. You can specify up to 20 domains per request. Domains should be provided without the protocol (e.g., "nature.com" not "[https://nature.com](https://nature.com)").
</Info>

## Overview

The domain filter for the Search API allows you to control which sources appear in your search results by limiting them to specific domains or excluding certain domains. This is particularly useful when you need to:

* Focus research on authoritative or trusted sources
* Filter out specific domains from search results
* Search within specific publication networks or organizations
* Build domain-specific search applications
* Conduct competitive research within specific industry domains

The `search_domain_filter` parameter accepts an array of domain strings. The filter operates in two modes:

* **Allowlist mode**: Include only the specified domains (no `-` prefix)
* **Denylist mode**: Exclude the specified domains (use `-` prefix)

```bash theme={null}
# Allowlist: Only search these domains
"search_domain_filter": ["nature.com", "science.org", "cell.com"]

# Denylist: Exclude these domains
"search_domain_filter": ["-reddit.com", "-pinterest.com", "-quora.com"]
```

## Filtering Capabilities

Domain filters support flexible matching across different domain components:

### Root Domain Filtering

Specify a root domain to match all content from that domain and its subdomains:

```bash theme={null}
"search_domain_filter": ["wikipedia.org"]
```

This will match:

* `en.wikipedia.org`
* `fr.wikipedia.org`
* `de.wikipedia.org`
* Any other Wikipedia language subdomain

### Top-Level Domain (TLD) Filtering

Filter by top-level domain to target specific categories of sites:

```bash theme={null}
"search_domain_filter": [".gov"]
```

This will match all government domains:

* `nasa.gov`
* `cdc.gov`
* `irs.gov`
* Any other `.gov` domain

<Tip>
  TLD filtering is particularly useful for targeting specific types of organizations, such as `.gov` for government sites, `.edu` for educational institutions, or country-specific TLDs like `.uk` or `.ca`.
</Tip>

### Domain Part Filtering

Any part of a domain can be used as a filter. The system will match domains containing that component.

## Examples

**1. Allowlist Specific Domains**

This example limits search results to authoritative academic publishers:

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="climate change research",
      max_results=10,
      search_domain_filter=[
          "nature.com",
          "science.org",
          "cell.com"
      ]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "climate change research",
    maxResults: 10,
    searchDomainFilter: [
      "nature.com",
      "science.org",
      "cell.com"
    ]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "climate change research",
      "max_results": 10,
      "search_domain_filter": [
        "nature.com",
        "science.org",
        "cell.com"
      ]
    }' | jq
  ```
</CodeGroup>

**2. Tech News Sources**

Search across major technology news websites:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="latest tech trends 2025",
      max_results=10,
      search_domain_filter=[
          "techcrunch.com",
          "theverge.com",
          "arstechnica.com",
          "wired.com"
      ]
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"Source: {result.url}")
      print(f"Date: {result.date}")
      print("---")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "latest tech trends 2025",
    maxResults: 10,
    searchDomainFilter: [
      "techcrunch.com",
      "theverge.com",
      "arstechnica.com",
      "wired.com"
    ]
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`Source: ${result.url}`);
    console.log(`Date: ${result.date}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "latest tech trends 2025",
      "max_results": 10,
      "search_domain_filter": [
        "techcrunch.com",
        "theverge.com",
        "arstechnica.com",
        "wired.com"
      ]
    }' | jq
  ```
</CodeGroup>

**3. Government and Educational Sources (TLD Filtering)**

Use top-level domain filtering to search across all government or educational institutions:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search all .gov and .edu domains
  response = client.search.create(
      query="climate change policy research",
      max_results=15,
      search_domain_filter=[
          ".gov",
          ".edu"
      ]
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"Source: {result.url}")
      print("---")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search all .gov and .edu domains
  const response = await client.search.create({
    query: "climate change policy research",
    maxResults: 15,
    searchDomainFilter: [
      ".gov",
      ".edu"
    ]
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`Source: ${result.url}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "climate change policy research",
      "max_results": 15,
      "search_domain_filter": [
        ".gov",
        ".edu"
      ]
    }' | jq
  ```
</CodeGroup>

**4. Wikipedia Across Languages (Subdomain Matching)**

Search across all Wikipedia language editions by specifying the root domain:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Matches en.wikipedia.org, fr.wikipedia.org, de.wikipedia.org, etc.
  response = client.search.create(
      query="quantum mechanics",
      max_results=10,
      search_domain_filter=["wikipedia.org"]
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"URL: {result.url}")
      print("---")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Matches en.wikipedia.org, fr.wikipedia.org, de.wikipedia.org, etc.
  const response = await client.search.create({
    query: "quantum mechanics",
    maxResults: 10,
    searchDomainFilter: ["wikipedia.org"]
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`URL: ${result.url}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "quantum mechanics",
      "max_results": 10,
      "search_domain_filter": ["wikipedia.org"]
    }' | jq
  ```
</CodeGroup>

**5. Denylist Specific Domains**

This example shows how to exclude specific domains from search results by prefixing the domain name with a minus sign (`-`):

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Exclude social media and Q&A sites from search results
  response = client.search.create(
      query="latest advancements in renewable energy",
      max_results=10,
      search_domain_filter=[
          "-pinterest.com",
          "-reddit.com",
          "-quora.com"
      ]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Exclude social media and Q&A sites from search results
  const response = await client.search.create({
    query: "latest advancements in renewable energy",
    maxResults: 10,
    searchDomainFilter: [
      "-pinterest.com",
      "-reddit.com",
      "-quora.com"
    ]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "latest advancements in renewable energy",
      "max_results": 10,
      "search_domain_filter": [
        "-pinterest.com",
        "-reddit.com",
        "-quora.com"
      ]
    }' | jq
  ```
</CodeGroup>

**6. Combining Domain Filter with Other Filters**

Domain filters work seamlessly with other search parameters for precise control:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Combine domain filter with date and language filters
  response = client.search.create(
      query="quantum computing breakthroughs",
      max_results=20,
      search_domain_filter=[
          "nature.com",
          "science.org",
          "arxiv.org"
      ],
      search_recency_filter="month",
      search_language_filter=["en"]
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"URL: {result.url}")
      print(f"Date: {result.date}")
      print("---")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Combine domain filter with date and language filters
  const response = await client.search.create({
    query: "quantum computing breakthroughs",
    maxResults: 20,
    searchDomainFilter: [
      "nature.com",
      "science.org",
      "arxiv.org"
    ],
    searchRecencyFilter: "month",
    searchLanguageFilter: ["en"]
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`URL: ${result.url}`);
    console.log(`Date: ${result.date}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "quantum computing breakthroughs",
      "max_results": 20,
      "search_domain_filter": [
        "nature.com",
        "science.org",
        "arxiv.org"
      ],
      "search_recency_filter": "month",
      "search_language_filter": ["en"]
    }' | jq
  ```
</CodeGroup>

## Parameter Reference

### `search_domain_filter`

* **Type**: Array of strings
* **Format**:
  * Domain names without protocol (e.g., "example.com")
  * Prefix with `-` for denylisting (e.g., "-reddit.com")
* **Description**: Filters search results to include or exclude content from specified domains
* **Optional**: Yes
* **Maximum**: 20 domains per request
* **Modes**:
  * Allowlist mode: Include only specified domains (no `-` prefix)
  * Denylist mode: Exclude specified domains (use `-` prefix)
* **Example**:
  * Allowlist: `"search_domain_filter": ["nature.com", "science.org"]`
  * Denylist: `"search_domain_filter": ["-reddit.com", "-pinterest.com"]`

## Domain Format Guidelines

**Correct Domain Formats:**

* `"nature.com"` - Root domain (matches nature.com and all subdomains)
* `"blog.example.com"` - Specific subdomain
* `"arxiv.org"` - Root domain (matches all subdomains)
* `".gov"` - Top-level domain (matches all .gov sites)
* `".edu"` - Top-level domain (matches all .edu sites)
* `".uk"` - Country-code TLD (matches all .uk sites)
* `"wikipedia.org"` - Matches en.wikipedia.org, fr.wikipedia.org, etc.
* `"-reddit.com"` - Exclude entire domain and all subdomains
* `"-pinterest.com"` - Exclude domain
* `"-.gov"` - Exclude all .gov domains

**Incorrect Domain Formats:**

* ❌ `"https://nature.com"` - Don't include protocol
* ❌ `"nature.com/"` - Don't include trailing slash
* ❌ `"nature.com/articles"` - Don't include path (path filtering coming soon)
* ❌ `"www.nature.com"` - Avoid www prefix (use root domain)

## Best Practices

### Domain Selection Strategy

* **Use Root Domains for Broad Coverage**: Specify root domains (e.g., "wikipedia.org") to match all subdomains automatically, including different language versions and regional sites.
* **Use TLDs for Categorical Filtering**: Target specific organization types with TLD filters like `.gov` for government, `.edu` for education, or `.org` for non-profits.
* **Be Specific When Needed**: Choose specific domains that are directly relevant to your search query to ensure high-quality results.
* **Quality Over Quantity**: Using fewer, highly relevant domains often produces better results than maximizing the 20-domain limit.
* **Consider Domain Authority**: Prioritize authoritative sources in your field for more reliable information.
* **Choose Your Mode**: Use either allowlist mode (include only) OR denylist mode (exclude), but not both in the same request. Denylisting is useful when you want broad search coverage but need to exclude specific low-quality or irrelevant sources.

### Locale and Regional Targeting

While domain filters don't directly filter by user location, you can target specific locales using:

* **Country-code TLDs**: Use filters like `.uk`, `.ca`, `.de`, `.jp` to target country-specific domains
* **Subdomain matching**: Specify regional subdomains when available (e.g., "uk.domain.com")
* **Combined approach**: Mix country TLDs with specific trusted domains for precise regional filtering

<Tip>
  For international research, combine TLD filtering with the `search_language_filter` parameter to refine results by both location and language.
</Tip>

### Domain Selection

* **Use Trusted Sources**: Select a specific set of trusted sources you want to search within (e.g., academic research, official documentation).
* **Leverage TLD Filtering**: When researching topics that span many sites of the same type, use TLD filters to cast a wider net (e.g., `.gov` for policy research).
* **Focus on Quality**: Choose authoritative domains that consistently provide reliable information relevant to your queries.

### Client-Side Validation

Validate domain formats on the client side before sending requests:

<CodeGroup>
  ```python Python theme={null}
  import re

  def validate_domain(domain):
      """Validate domain format including TLD filters."""
      # TLD filter (e.g., .gov, .edu)
      if domain.startswith('.'):
          tld_pattern = r'^\.[a-zA-Z]{2,}$'
          return bool(re.match(tld_pattern, domain))
      
      # Standard domain validation pattern
      pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
      return bool(re.match(pattern, domain))

  def validate_domain_filter(domains):
      """Validate domain filter array."""
      if len(domains) > 20:
          raise ValueError("Maximum 20 domains allowed")

      for domain in domains:
          if not validate_domain(domain):
              raise ValueError(f"Invalid domain format: {domain}")

      return True

  # Usage examples
  try:
      # Mix of regular domains and TLD filters
      domains = ["nature.com", "science.org", ".gov", ".edu"]
      validate_domain_filter(domains)

      response = client.search.create(
          query="research topic",
          search_domain_filter=domains
      )
  except ValueError as e:
      print(f"Validation error: {e}")
  ```

  ```typescript TypeScript theme={null}
  function validateDomain(domain: string): boolean {
    // TLD filter (e.g., .gov, .edu)
    if (domain.startsWith('.')) {
      const tldPattern = /^\.[a-zA-Z]{2,}$/;
      return tldPattern.test(domain);
    }
    
    // Standard domain validation pattern
    const pattern = /^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
    return pattern.test(domain);
  }

  function validateDomainFilter(domains: string[]): void {
    if (domains.length > 20) {
      throw new Error("Maximum 20 domains allowed");
    }

    for (const domain of domains) {
      if (!validateDomain(domain)) {
        throw new Error(`Invalid domain format: ${domain}`);
      }
    }
  }

  // Usage examples
  try {
    // Mix of regular domains and TLD filters
    const domains = ["nature.com", "science.org", ".gov", ".edu"];
    validateDomainFilter(domains);

    const response = await client.search.create({
      query: "research topic",
      searchDomainFilter: domains
    });
  } catch (error) {
    console.error("Validation error:", error.message);
  }
  ```
</CodeGroup>

### Performance Considerations

* **Result Availability**: Narrowing to specific domains may reduce the number of available results. Be prepared to handle cases where fewer results are returned than requested.
* **Domain Coverage**: Ensure the domains you specify actually contain content relevant to your query. Overly restrictive filters may return zero results.
* **Combination Effects**: Domain filters combined with other restrictive filters (date, language) can significantly reduce result counts.

<Tip>
  For best results, combine domain filtering with other filters like `search_recency_filter` or `search_language_filter` to narrow down your search to highly relevant, timely content from your target sources. Use TLD filters like `.gov` or `.edu` when you need broad coverage across an entire category of authoritative sites.
</Tip>


# Search Language Filter
Source: https://docs.perplexity.ai/docs/search/filters/language-filter



<Note>
  The `search_language_filter` parameter allows you to filter search results by language using ISO 639-1 language codes. Only results in the specified languages will be returned.
</Note>

<Info>
  Language codes must be valid 2-letter ISO 639-1 codes (e.g., "en", "ru", "fr"). You can filter by up to 10 languages per request.
</Info>

## Overview

The language filter for the Search API allows you to control which search results are returned by limiting them to specific languages. This is particularly useful when you need to:

* Search for content in specific languages
* Conduct multilingual research across multiple languages
* Focus on regional content in local languages
* Build language-specific applications or features

The `search_language_filter` parameter accepts an array of ISO 639-1 language codes and returns only results that match those languages.

To filter search results by language:

```bash theme={null}
"search_language_filter": ["en", "fr", "de"]
```

This filter will be applied in addition to any other search parameters.

## Examples

**1. Single Language Filter**

This example limits search results to English language content only.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="artificial intelligence",
      max_results=10,
      search_language_filter=["en"]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "artificial intelligence",
    maxResults: 10,
    searchLanguageFilter: ["en"]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "artificial intelligence",
      "max_results": 10,
      "search_language_filter": ["en"]
    }' | jq
  ```
</CodeGroup>

**2. Multiple Language Filter**

Search across multiple languages to gather diverse perspectives or multilingual content:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for content in English, French, and German
  response = client.search.create(
      query="renewable energy innovations",
      max_results=15,
      search_language_filter=["en", "fr", "de"]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for content in English, French, and German
  const response = await client.search.create({
    query: "renewable energy innovations",
    maxResults: 15,
    searchLanguageFilter: ["en", "fr", "de"]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "renewable energy innovations",
      "max_results": 15,
      "search_language_filter": ["en", "fr", "de"]
    }' | jq
  ```
</CodeGroup>

**3. Regional Language Search**

Focus on content from specific regions by using their local languages:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for Asian market news in Chinese, Japanese, and Korean
  response = client.search.create(
      query="technology market trends",
      max_results=10,
      search_language_filter=["zh", "ja", "ko"]
  )

  # Search for European tech news in multiple European languages
  eu_response = client.search.create(
      query="tech startups",
      max_results=10,
      search_language_filter=["en", "de", "fr", "es", "it"]
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for Asian market news in Chinese, Japanese, and Korean
  const response = await client.search.create({
    query: "technology market trends",
    maxResults: 10,
    searchLanguageFilter: ["zh", "ja", "ko"]
  });

  // Search for European tech news in multiple European languages
  const euResponse = await client.search.create({
    query: "tech startups",
    maxResults: 10,
    searchLanguageFilter: ["en", "de", "fr", "es", "it"]
  });
  ```

  ```bash cURL theme={null}
  # Search for Asian market news
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "technology market trends",
      "max_results": 10,
      "search_language_filter": ["zh", "ja", "ko"]
    }' | jq
  ```
</CodeGroup>

**4. Combining with Other Filters**

Language filters work seamlessly with other search parameters for precise control:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Combine language filter with date and domain filters
  response = client.search.create(
      query="climate change research",
      max_results=20,
      search_language_filter=["en", "de"],
      search_domain_filter=["nature.com", "science.org"],
      search_recency_filter="month"
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"URL: {result.url}")
      print(f"Date: {result.date}")
      print("---")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Combine language filter with date and domain filters
  const response = await client.search.create({
    query: "climate change research",
    maxResults: 20,
    searchLanguageFilter: ["en", "de"],
    searchDomainFilter: ["nature.com", "science.org"],
    searchRecencyFilter: "month"
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`URL: ${result.url}`);
    console.log(`Date: ${result.date}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "climate change research",
      "max_results": 20,
      "search_language_filter": ["en", "de"],
      "search_domain_filter": ["nature.com", "science.org"],
      "search_recency_filter": "month"
    }' | jq
  ```
</CodeGroup>

## Parameter Reference

### `search_language_filter`

* **Type**: Array of strings
* **Format**: ISO 639-1 language codes (2 lowercase letters)
* **Description**: Filters search results to only include content in the specified languages
* **Optional**: Yes
* **Maximum**: 10 language codes per request
* **Example**: `"search_language_filter": ["en", "fr", "de"]`

## Common Language Codes

Here's a comprehensive list of frequently used ISO 639-1 language codes:

| Language   | Code | Language   | Code |
| ---------- | ---- | ---------- | ---- |
| English    | `en` | Portuguese | `pt` |
| Spanish    | `es` | Dutch      | `nl` |
| French     | `fr` | Polish     | `pl` |
| German     | `de` | Swedish    | `sv` |
| Italian    | `it` | Norwegian  | `no` |
| Russian    | `ru` | Danish     | `da` |
| Chinese    | `zh` | Finnish    | `fi` |
| Japanese   | `ja` | Czech      | `cs` |
| Korean     | `ko` | Hungarian  | `hu` |
| Arabic     | `ar` | Greek      | `el` |
| Hindi      | `hi` | Turkish    | `tr` |
| Bengali    | `bn` | Hebrew     | `he` |
| Indonesian | `id` | Thai       | `th` |
| Vietnamese | `vi` | Ukrainian  | `uk` |

<Tip>
  For a complete list of ISO 639-1 language codes, see the [ISO 639-1 standard](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
</Tip>

## Best Practices

### Language Code Validation

* **Use Valid Codes**: Always use valid 2-letter ISO 639-1 codes. Invalid codes will result in an API error.
* **Lowercase Only**: Language codes must be lowercase (e.g., "en" not "EN").
* **Client-Side Validation**: Validate language codes on the client side using a regex pattern:

<CodeGroup>
  ```python Python theme={null}
  import re

  def validate_language_code(code):
      pattern = r'^[a-z]{2}$'
      return bool(re.match(pattern, code))

  def validate_language_filters(codes):
      if len(codes) > 10:
          raise ValueError("Maximum 10 language codes allowed")
      
      for code in codes:
          if not validate_language_code(code):
              raise ValueError(f"Invalid language code: {code}")
      
      return True

  # Usage
  try:
      codes = ["en", "fr", "de"]
      validate_language_filters(codes)
      
      response = client.search.create(
          query="technology news",
          search_language_filter=codes
      )
  except ValueError as e:
      print(f"Validation error: {e}")
  ```

  ```typescript TypeScript theme={null}
  function validateLanguageCode(code: string): boolean {
    const pattern = /^[a-z]{2}$/;
    return pattern.test(code);
  }

  function validateLanguageFilters(codes: string[]): void {
    if (codes.length > 10) {
      throw new Error("Maximum 10 language codes allowed");
    }
    
    for (const code of codes) {
      if (!validateLanguageCode(code)) {
        throw new Error(`Invalid language code: ${code}`);
      }
    }
  }

  // Usage
  try {
    const codes = ["en", "fr", "de"];
    validateLanguageFilters(codes);
    
    const response = await client.search.create({
      query: "technology news",
      searchLanguageFilter: codes
    });
  } catch (error) {
    console.error("Validation error:", error.message);
  }
  ```
</CodeGroup>

### Strategic Language Selection

* **Be Specific**: Choose languages that are most relevant to your research or application needs.
* **Consider Your Audience**: Select languages that match your target audience's preferences.
* **Regional Relevance**: Combine language filters with geographic filters (`country` parameter) for better regional targeting.
* **Content Availability**: Some topics may have limited content in certain languages. Start broad and narrow down as needed.

### Performance Considerations

* **Filter Size**: While you can specify up to 10 languages, using fewer languages may improve response times.
* **Result Quality**: More languages mean a broader search scope, which can dilute result relevance. Be strategic about which languages to include.
* **Combination Effects**: Language filters combined with other restrictive filters (domain, date) may significantly reduce the number of results.

## Advanced Usage Patterns

### Multilingual Research

Conduct comprehensive research by searching across multiple languages:

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Research a global topic in multiple languages
languages = [
    ["en"],           # English-speaking countries
    ["zh", "ja"],     # East Asia
    ["es", "pt"],     # Latin America and Iberia
    ["fr", "de", "it"] # Western Europe
]

results_by_region = {}

for lang_group in languages:
    response = client.search.create(
        query="sustainable development goals progress",
        max_results=10,
        search_language_filter=lang_group
    )
    results_by_region[", ".join(lang_group)] = response.results

# Analyze results by language/region
for region, results in results_by_region.items():
    print(f"Results in {region}: {len(results)} found")
```

### Content Localization Research

Find examples and references in target languages for localization projects:

```python theme={null}
# Find product reviews in target markets
target_languages = ["ja", "ko", "zh"]  # Asian markets

response = client.search.create(
    query="smartphone reviews 2024",
    max_results=15,
    search_language_filter=target_languages,
    search_recency_filter="month"
)
```

### Academic Research Across Languages

Access scholarly content in different languages:

```python theme={null}
# Search for research papers in multiple languages
response = client.search.create(
    query="quantum computing algorithms",
    max_results=20,
    search_language_filter=["en", "de", "fr", "ru"],
    search_domain_filter=["arxiv.org", "nature.com", "science.org"]
)
```

### News Monitoring by Language

Track news stories across different language regions:

```python theme={null}
# Monitor breaking news in different languages
news_queries = {
    "English": ["en"],
    "Chinese": ["zh"],
    "Spanish": ["es"],
    "Arabic": ["ar"]
}

for region, langs in news_queries.items():
    response = client.search.create(
        query="breaking news technology",
        max_results=5,
        search_language_filter=langs,
        search_recency_filter="day"
    )
    print(f"{region} News: {len(response.results)} articles")
```

## Error Handling

When using language filters, implement proper error handling for validation issues:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity, BadRequestError

  client = Perplexity()

  def safe_language_search(query, languages):
      """
      Perform a language-filtered search with error handling.
      """
      try:
          # Validate language codes
          if not isinstance(languages, list):
              raise ValueError("Languages must be provided as a list")
          
          if len(languages) > 10:
              raise ValueError("Maximum 10 language codes allowed")
          
          # Validate each code format
          for lang in languages:
              if not isinstance(lang, str) or len(lang) != 2 or not lang.islower():
                  raise ValueError(f"Invalid language code format: {lang}")
          
          # Perform search
          response = client.search.create(
              query=query,
              search_language_filter=languages,
              max_results=10
          )
          
          return response
          
      except ValueError as e:
          print(f"Validation error: {e}")
          return None
      except BadRequestError as e:
          print(f"API error: {e.message}")
          return None
      except Exception as e:
          print(f"Unexpected error: {e}")
          return None

  # Usage
  results = safe_language_search(
      "artificial intelligence",
      ["en", "fr", "de"]
  )

  if results:
      print(f"Found {len(results.results)} results")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  async function safeLanguageSearch(
    query: string,
    languages: string[]
  ): Promise<any | null> {
    try {
      // Validate language codes
      if (!Array.isArray(languages)) {
        throw new Error("Languages must be provided as an array");
      }
      
      if (languages.length > 10) {
        throw new Error("Maximum 10 language codes allowed");
      }
      
      // Validate each code format
      for (const lang of languages) {
        if (typeof lang !== 'string' || 
            lang.length !== 2 || 
            lang !== lang.toLowerCase()) {
          throw new Error(`Invalid language code format: ${lang}`);
        }
      }
      
      // Perform search
      const response = await client.search.create({
        query,
        searchLanguageFilter: languages,
        maxResults: 10
      });
      
      return response;
      
    } catch (error) {
      if (error instanceof Perplexity.BadRequestError) {
        console.error("API error:", error.message);
      } else if (error instanceof Error) {
        console.error("Error:", error.message);
      }
      return null;
    }
  }

  // Usage
  const results = await safeLanguageSearch(
    "artificial intelligence",
    ["en", "fr", "de"]
  );

  if (results) {
    console.log(`Found ${results.results.length} results`);
  }
  ```
</CodeGroup>

<Tip>
  For best results, combine language filtering with other filters like `search_domain_filter` or `search_recency_filter` to narrow down your search to highly relevant, timely content in your target languages.
</Tip>


# Perplexity Search API
Source: https://docs.perplexity.ai/docs/search/quickstart

Access real-time web search results with Perplexity's Search API. Get ranked results, domain filtering, multi-query search, and content extraction for developers.

## Overview

<Card title="Try Our New Interactive Playground" href="https://perplexity.ai/account/api/playground/search">
  Test search queries and parameters in real time, **no API key required**.
</Card>

Perplexity's Search API provides developers with real-time access to ranked web search results from a continuously refreshed index. Unlike traditional search APIs, Perplexity returns structured results with advanced filtering by domain, language, and region.

Use the Search API when you need raw, ranked web results with control over sources, regions, and extracted content. For LLM-generated summaries, use our [Chat Completions API](/docs/grounded-llm/chat-completions/quickstart) or [Agentic Research API](/docs/grounded-llm/responses/quickstart).

<Info>
  We recommend using our [official SDKs](/docs/sdk/overview) for a more convenient and type-safe way to interact with the Search API.
</Info>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript/JavaScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```
</CodeGroup>

## Authentication

Set your API key as an environment variable. The SDK will automatically read it:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

Or use a `.env` file in your project:

```bash .env theme={null}
PERPLEXITY_API_KEY=your_api_key_here
```

<Info>
  All SDK examples below automatically use the `PERPLEXITY_API_KEY` environment variable. You can also pass the key explicitly if needed.
</Info>

## Basic Usage

Start with a basic search query to get relevant web results. See the [API Reference](/api-reference/search-post) for complete parameter documentation.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  search = client.search.create(
      query="latest AI developments 2024",
      max_results=5,
      max_tokens_per_page=2048
  )

  for result in search.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const search = await client.search.create({
      query: "latest AI developments 2024",
      maxResults: 5,
      maxTokensPerPage: 2048
  });

  for (const result of search.results) {
      console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  const client = new Perplexity();

  async function main() {
      const search = await client.search.create({
          query: "latest AI developments 2024",
          maxResults: 5,
          maxTokensPerPage: 2048
      });

      for (const result of search.results) {
          console.log(`${result.title}: ${result.url}`);
      }
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "latest AI developments 2024",
      "max_results": 5,
      "max_tokens_per_page": 2048
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "results": [
      {
        "title": "2024: A year of extraordinary progress and advancement in AI - Google Blog",
        "url": "https://blog.google/technology/ai/2024-ai-extraordinary-progress-advancement/",
        "snippet": "## Relentless innovation in models, products and technologies\n\n2024 was a year of experimenting, fast shipping, and putting our latest technologies in the hands of developers.\n\nIn December 2024, we released the first models in our Gemini 2.0 experimental series — AI models designed for the agentic era. First out of the gate was Gemini 2.0 Flash, our workhorse model, followed by prototypes from the frontiers of our agentic research including: an updated Project Astra, which explores the capabilities of a universal AI assistant; Project Mariner, an early prototype capable of taking actions in Chrome as an experimental extension; and Jules, an AI-powered code agent. We're looking forward to bringing Gemini 2.0’s powerful capabilities to our flagship products — in Search, we've already started testing in AI Overviews, which are now used by over a billion people to ask new types of questions.\n\nWe also released Deep Research, a new agentic feature in Gemini Advanced that saves people hours of research work by creating and executing multi-step plans for finding answers to complicated questions; and introduced Gemini 2.0 Flash Thinking Experimental, an experimental model that explicitly shows its thoughts.\n\nThese advances followed swift progress earlier in the year, from incorporating Gemini's capabilities into more Google products to the release of Gemini 1.5 Pro and Gemini 1.5 Flash — a model optimized for speed and efficiency. 1.5 Flash's compact size made it more cost-efficient to serve, and in 2024 it became our most popular model for developers.... ## The architecture of intelligence: advances in robotics, hardware and computing\n\nAs our multimodal models become more capable and gain a better understanding of the world and its physics, they are making possible incredible new advances in robotics and bringing us closer to our goal of ever-more capable and helpful robots.\n\nWith ALOHA Unleashed, our robot learned to tie a shoelace, hang a shirt, repair another robot, insert a gear and even clean a kitchen.\n\nAt the beginning of the year, we introduced AutoRT, SARA-RT and RT-Trajectory, extensions of our Robotics Transformers work intended to help robots better understand and navigate their environments, and make decisions faster. We also published ALOHA Unleashed, a breakthrough in teaching robots on how to use two robotic arms in coordination, and DemoStart, which uses a reinforcement learning algorithm to improve real-world performance on a multi-fingered robotic hand by using simulations.\n\nRobotic Transformer 2 (RT-2) is a novel vision-language-action model that learns from both web and robotics data.\n\nBeyond robotics, our AlphaChip reinforcement learning method for accelerating and improving chip floorplanning is transforming the design process for chips found in data centers, smartphones and more. To accelerate adoption of these techniques, we released a pre-trained checkpoint to enable external parties to more easily make use of the AlphaChip open source release for their own chip designs. And we made Trillium, our sixth-generation and most performant TPU to date, generally available to Google Cloud customers. Advances in computer chips have accelerated AI. And now, AI can return the favor.... We are exploring how machine learning can help medical fields struggling with access to imaging expertise, such as radiology, dermatology and pathology. In the past year, we released two research tools, Derm Foundation and Path Foundation, that can help develop models for diagnostic tasks, image indexing and curation and biomarker discovery and validation. We collaborated with physicians at Stanford Medicine on an open-access, inclusive Skin Condition Image Network (SCIN) dataset. And we unveiled CT Foundation, a medical imaging embedding tool used for rapidly training models for research.\n\nWith regard to learning, we explored new generative AI tools to support educators and learners. We introduced LearnLM, our new family of models fine-tuned for learning and used it to enhance learning experiences in products like Search, YouTube and Gemini; a recent report showed LearnLM outperformed other leading AI models. We also made it available to developers as an experimental model in AI Studio. Our new conversational learning companion, LearnAbout, uses AI to help you dive deeper into any topic you're curious about, while Illuminate lets you turn content into engaging AI-generated audio discussions.\n\nIn the fields of disaster forecasting and preparedness, we announced several breakthroughs. We introduced GenCast, our new high-resolution AI ensemble model, which improves day-to-day weather and extreme events forecasting across all possible weather trajectories. We also introduced our NeuralGCM model, able to simulate over 70,000 days of the atmosphere in the time it would take a physics-based model to simulate only 19 days. And GraphCast won the 2024 MacRobert Award for engineering innovation.",
        "date": "2025-01-23",
        "last_updated": "2025-09-25"
      },
      {
        "title": "The 2025 AI Index Report | Stanford HAI",
        "url": "https://hai.stanford.edu/ai-index/2025-ai-index-report",
        "snippet": "Read the translation\n\nIn 2023, researchers introduced new benchmarks—MMMU, GPQA, and SWE-bench—to test the limits of advanced AI systems. Just a year later, performance sharply increased: scores rose by 18.8, 48.9, and 67.3 percentage points on MMMU, GPQA, and SWE-bench, respectively. Beyond benchmarks, AI systems made major strides in generating high-quality video, and in some settings, language model agents even outperformed humans in programming tasks with limited time budgets.\n\nFrom healthcare to transportation, AI is rapidly moving from the lab to daily life. In 2023, the FDA approved 223 AI-enabled medical devices, up from just six in 2015. On the roads, self-driving cars are no longer experimental: Waymo, one of the largest U.S. operators, provides over 150,000 autonomous rides each week, while Baidu's affordable Apollo Go robotaxi fleet now serves numerous cities across China.\n\nIn 2024, U.S. private AI investment grew to $109.1 billion—nearly 12 times China's $9.3 billion and 24 times the U.K.'s $4.5 billion. Generative AI saw particularly strong momentum, attracting $33.9 billion globally in private investment—an 18.7% increase from 2023. AI business usage is also accelerating: 78% of organizations reported using AI in 2024, up from 55% the year before. Meanwhile, a growing body of research confirms that AI boosts productivity and, in most cases, helps narrow skill gaps across the workforce.... In 2024, U.S.-based institutions produced 40 notable AI models, significantly outpacing China's 15 and Europe's three. While the U.S. maintains its lead in quantity, Chinese models have rapidly closed the quality gap: performance differences on major benchmarks such as MMLU and HumanEval shrank from double digits in 2023 to near parity in 2024. Meanwhile, China continues to lead in AI publications and patents. At the same time, model development is increasingly global, with notable launches from regions such as the Middle East, Latin America, and Southeast Asia.\n\nAI-related incidents are rising sharply, yet standardized RAI evaluations remain rare among major industrial model developers. However, new benchmarks like HELM Safety, AIR-Bench, and FACTS offer promising tools for assessing factuality and safety. Among companies, a gap persists between recognizing RAI risks and taking meaningful action. In contrast, governments are showing increased urgency: In 2024, global cooperation on AI governance intensified, with organizations including the OECD, EU, U.N., and African Union releasing frameworks focused on transparency, trustworthiness, and other core responsible AI principles.\n\nIn countries like China (83%), Indonesia (80%), and Thailand (77%), strong majorities see AI products and services as more beneficial than harmful. In contrast, optimism remains far lower in places like Canada (40%), the United States (39%), and the Netherlands (36%). Still, sentiment is shifting: since 2022, optimism has grown significantly in several previously skeptical countries—including Germany (+10%), France (+10%), Canada (+8%), Great Britain (+8%), and the United States (+4%).... Driven by increasingly capable small models, the inference cost for a system performing at the level of GPT-3.5 dropped over 280-fold between November 2022 and October 2024. At the hardware level, costs have declined by 30% annually, while energy efficiency has improved by 40% each year. Open-weight models are also closing the gap with closed models, reducing the performance difference from 8% to just 1.7% on some benchmarks in a single year. Together, these trends are rapidly lowering the barriers to advanced AI.\n\nIn 2024, U.S. federal agencies introduced 59 AI-related regulations—more than double the number in 2023—and issued by twice as many agencies. Globally, legislative mentions of AI rose 21.3% across 75 countries since 2023, marking a ninefold increase since 2016. Alongside growing attention, governments are investing at scale: Canada pledged $2.4 billion, China launched a $47.5 billion semiconductor fund, France committed €109 billion, India pledged $1.25 billion, and Saudi Arabia's Project Transcendence represents a $100 billion initiative.\n\nTwo-thirds of countries now offer or plan to offer K–12 CS education—twice as many as in 2019—with Africa and Latin America making the most progress. In the U.S., the number of graduates with bachelor's degrees in computing has increased 22% over the last 10 years. Yet access remains limited in many African countries due to basic infrastructure gaps like electricity. In the U.S., 81% of K–12 CS teachers say AI should be part of foundational CS education, but less than half feel equipped to teach it.",
        "date": "2024-09-10",
        "last_updated": "2025-09-25"
      }
    ],
    "id": "e38104d5-6bd7-4d82-bc4e-0a21179d1f77"
  }
  ```
</Accordion>

<Info>
  The `max_results` parameter accepts values from 1 to 20, with a default maximum of 10 results per search. See [pricing](/docs/getting-started/pricing) for details on search costs.
</Info>

## Regional Web Search

You can refine your search results by specifying a country to get more geographically relevant results:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for results from a specific country
  search = client.search.create(
      query="government policies on renewable energy",
      country="US",  # ISO country code
      max_results=5
  )

  for result in search.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for results from a specific country
  const search = await client.search.create({
      query: "government policies on renewable energy",
      country: "US", // ISO country code
      maxResults: 5
  });

  for (const result of search.results) {
      console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "government policies on renewable energy",
      "country": "US",
      "max_results": 5
    }' | jq
  ```
</CodeGroup>

<Tip>
  Use ISO 3166-1 alpha-2 country codes (e.g., "US", "GB", "DE", "JP") to target specific regions. This is particularly useful for queries about local news, regulations, or region-specific information.
</Tip>

## Multi-Query Web Search

Execute multiple related queries in a single request for comprehensive research:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  search = client.search.create(
      query=[
          "artificial intelligence trends 2024",
          "machine learning breakthroughs recent",
          "AI applications in healthcare"
      ],
      max_results=5
  )

  # Access results for each query
  for i, query_results in enumerate(search.results):
      print(f"Results for query {i+1}:")
      for result in query_results:
          print(f"  {result.title}: {result.url}")
      print("---")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const search = await client.search.create({
      query: [
          "artificial intelligence trends 2024",
          "machine learning breakthroughs recent", 
          "AI applications in healthcare"
      ],
      maxResults: 5
  });

  // Access results for each query
  search.results.forEach((queryResults, i) => {
      console.log(`Results for query ${i+1}:`);
      queryResults.forEach(result => {
          console.log(`  ${result.title}: ${result.url}`);
      });
      console.log("---");
  });
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": [
        "artificial intelligence trends 2024",
        "machine learning breakthroughs recent",
        "AI applications in healthcare"
      ],
      "max_results": 5
    }' | jq
  ```
</CodeGroup>

<Tip>
  Multi-query search is ideal for research tasks where you need to explore different angles of a topic. Each query is processed independently, giving you comprehensive coverage.
</Tip>

<Info>
  For single queries, `search.results` is a flat list. For multi-query requests, results are grouped per query in the same order.
</Info>

<Info>
  You can include up to 5 queries in a single multi-query request for efficient batch processing.
</Info>

## Domain Filtering for Search Results

The `search_domain_filter` parameter allows you to limit search results to specific domains (allowlist) or exclude certain domains (denylist) for focused research. The filter works in two modes:

* **Allowlist mode**: Include only specified domains (no `-` prefix)
* **Denylist mode**: Exclude specified domains (use `-` prefix)

**Note**: You can use either allowlist or denylist mode, but not both simultaneously in the same request.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  search = client.search.create(
      query="climate change research",
      search_domain_filter=[
          "science.org",
          "pnas.org",
          "cell.com"
      ],
      max_results=10
  )

  for result in search.results:
      print(f"{result.title}: {result.url}")
      print(f"Published: {result.date}")
      print("---")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const search = await client.search.create({
      query: "climate change research",
      searchDomainFilter: [
          "science.org",
          "pnas.org",
          "cell.com"
      ],
      maxResults: 10
  });

  for (const result of search.results) {
      console.log(`${result.title}: ${result.url}`);
      console.log(`Published: ${result.date}`);
      console.log("---");
  }
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  const client = new Perplexity();

  async function main() {
      const search = await client.search.create({
          query: "climate change research",
          searchDomainFilter: [
              "science.org",
              "pnas.org",
              "cell.com"
          ],
          maxResults: 10
      });

      for (const result of search.results) {
          console.log(`${result.title}: ${result.url}`);
          console.log(`Published: ${result.date}`);
          console.log("---");
      }
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "climate change research",
      "search_domain_filter": [
        "science.org",
        "pnas.org",
        "cell.com"
      ],
      "max_results": 10
    }' | jq
  ```
</CodeGroup>

<Warning>
  You can add a maximum of 20 domains to the `search_domain_filter` list. The filter works in either allowlist mode (include only) or denylist mode (exclude), but not both simultaneously. See the [domain filter guide](/docs/search/filters/domain-filter) for advanced usage patterns.
</Warning>

### Denylisting Example

You can also exclude specific domains from search results:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Exclude social media sites from search results
  search = client.search.create(
      query="renewable energy innovations",
      search_domain_filter=[
          "-pinterest.com",
          "-reddit.com",
          "-quora.com"
      ],
      max_results=10
  )

  for result in search.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Exclude social media sites from search results
  const search = await client.search.create({
      query: "renewable energy innovations",
      searchDomainFilter: [
          "-pinterest.com",
          "-reddit.com",
          "-quora.com"
      ],
      maxResults: 10
  });

  for (const result of search.results) {
      console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "renewable energy innovations",
      "search_domain_filter": [
        "-pinterest.com",
        "-reddit.com",
        "-quora.com"
      ],
      "max_results": 10
    }' | jq
  ```
</CodeGroup>

## Language Filtering for Web Search

The `search_language_filter` parameter allows you to filter search results by language using ISO 639-1 language codes:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for English, French, and German language results
  search = client.search.create(
      query="latest AI news",
      search_language_filter=["en", "fr", "de"],
      max_results=10
  )

  for result in search.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for English, French, and German language results
  const search = await client.search.create({
      query: "latest AI news",
      searchLanguageFilter: ["en", "fr", "de"],
      maxResults: 10
  });

  for (const result of search.results) {
      console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  const client = new Perplexity();

  async function main() {
      // Search for English, French, and German language results
      const search = await client.search.create({
          query: "latest AI news",
          searchLanguageFilter: ["en", "fr", "de"],
          maxResults: 10
      });

      for (const result of search.results) {
          console.log(`${result.title}: ${result.url}`);
      }
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "latest AI news",
      "search_language_filter": ["en", "fr", "de"],
      "max_results": 10
    }' | jq
  ```
</CodeGroup>

<Warning>
  Language codes must be valid 2-letter ISO 639-1 codes (e.g., "en", "ru", "fr"). You can add a maximum of 10 language codes per request. See the [language filter guide](/docs/search/filters/language-filter) for the complete list of supported codes.
</Warning>

## Content Extraction Control

The `max_tokens_per_page` parameter controls how much content is extracted from each webpage during search processing. This allows you to balance between comprehensive content coverage and processing efficiency.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Extract more content for comprehensive analysis
  detailed_search = client.search.create(
      query="artificial intelligence research methodology",
      max_results=5,
      max_tokens_per_page=2048
  )

  # Use default extraction for faster processing
  quick_search = client.search.create(
      query="AI news headlines",
      max_results=10,
      max_tokens_per_page=512
  )

  for result in detailed_search.results:
      print(f"{result.title}: {result.snippet[:100]}...")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Extract more content for comprehensive analysis
  const detailedSearch = await client.search.create({
      query: "artificial intelligence research methodology",
      maxResults: 5,
      maxTokensPerPage: 2048
  });

  // Use default extraction for faster processing
  const quickSearch = await client.search.create({
      query: "AI news headlines",
      maxResults: 3,
      maxTokensPerPage: 512
  });

  for (const result of detailedSearch.results) {
      console.log(`${result.title}: ${result.snippet.substring(0, 100)}...`);
  }
  ```

  ```bash cURL theme={null}
  # Comprehensive content extraction
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "artificial intelligence research methodology",
      "max_results": 5,
      "max_tokens_per_page": 2048
    }' | jq

  # Lighter content extraction
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "AI news headlines",
      "max_results": 3,
      "max_tokens_per_page": 512
    }' | jq
  ```
</CodeGroup>

<Info>
  The `max_tokens_per_page` parameter defaults to 2048 tokens. Higher values provide more comprehensive content extraction but may increase processing time. Lower values enable faster processing with more focused content.
</Info>

<Tip>
  Use lower `max_tokens_per_page` values (256-512) for quick information retrieval or when processing large result sets.
</Tip>

## Total Content Budget Control

The `max_tokens` parameter sets the maximum total tokens of webpage content returned across all search results. This controls how much content appears in the `snippet` fields. Use it together with `max_tokens_per_page` to control content distribution across results.
The `max_tokens` parameter defaults to 25,000 tokens. The maximum allowed value is 1,000,000 tokens.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Higher token budget = more content in snippets
  detailed_search = client.search.create(
      query="renewable energy technologies",
      max_results=10,
      max_tokens=50000,  # Total content budget across all results
      max_tokens_per_page=2048  # Per-result limit
  )

  # Lower token budget = shorter snippets
  brief_search = client.search.create(
      query="latest stock market news",
      max_results=5,
      max_tokens=5000
  )

  for result in detailed_search.results:
      print(f"{result.title}: {len(result.snippet)} chars")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Higher token budget = more content in snippets
  const detailedSearch = await client.search.create({
      query: "renewable energy technologies",
      maxResults: 10,
      maxTokens: 50000,  // Total content budget across all results
      maxTokensPerPage: 2048  // Per-result limit
  });

  // Lower token budget = shorter snippets
  const briefSearch = await client.search.create({
      query: "latest stock market news",
      maxResults: 5,
      maxTokens: 5000
  });

  for (const result of detailedSearch.results) {
      console.log(`${result.title}: ${result.snippet.length} chars`);
  }
  ```

  ```bash cURL theme={null}
  # Higher token budget for detailed content
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "renewable energy technologies",
      "max_results": 10,
      "max_tokens": 50000,
      "max_tokens_per_page": 2048
    }' | jq

  # Lower token budget for brief snippets
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "latest stock market news",
      "max_results": 5,
      "max_tokens": 5000
    }' | jq
  ```
</CodeGroup>

<Info>
  Search API charges per request only, with no additional token-based pricing.
</Info>

<Tip>
  **When to adjust each parameter:**

  * `max_tokens` controls the total content returned across all results—increase for longer snippets
  * `max_tokens_per_page` controls content per individual result—increase to get more from each page
  * Both parameters work together: `max_tokens` is the total budget, `max_tokens_per_page` is the per-result cap
</Tip>

## Next Steps

<Card title="Best Practices" icon="star" href="/docs/search/best-practices">
  Optimize your queries and implement async patterns
</Card>

## Explore More

<CardGroup>
  <Card title="API Reference" icon="book" href="/docs/api-reference/search-post">
    Complete API documentation for the Perplexity Search API
  </Card>

  <Card title="Perplexity SDK" icon="code" href="/docs/sdk/overview">
    Type-safe SDK for Python and TypeScript
  </Card>

  <Card title="Date & Time Filters" icon="calendar" href="/docs/search/filters/date-time-filters">
    Filter search results by recency and date ranges
  </Card>

  <Card title="Domain Filtering Guide" icon="globe" href="/docs/search/filters/domain-filter">
    Advanced domain allowlist and denylist patterns
  </Card>

  <Card title="Chat Completions API" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Get AI-generated summaries with built-in search capabilities.
  </Card>

  <Card title="Agentic Research API" icon="code" href="/docs/grounded-llm/responses/quickstart">
    Third-party models from OpenAI, Anthropic, Google, and more with presets and web search tools.
  </Card>
</CardGroup>


