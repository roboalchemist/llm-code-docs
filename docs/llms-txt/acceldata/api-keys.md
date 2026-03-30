# Source: https://docs.acceldata.io/documentation/api-keys.md

# API Keys

In ADOC, API keys provide a secure way to perform operations directly through REST API calls, while ensuring that every request is authenticated and traceable.

Instead of using personal login credentials, ADOC uses a key pair, accessKey and secretKey, to authorize API requests. These credentials are included in the request headers and validate that the caller has permission to perform the requested action.

Example use cases in ADOC:

- **Automated Rule Execution**
Instead of logging into the Rules UI, teams can trigger **rule executions** programmatically. For example, a nightly data pipeline can automatically validate data quality rules before publishing reports, ensuring bad data never reaches downstream systems.
- **Metadata Crawling**
External schedulers (like Airflow) can call ADOC APIs to **start crawlers** on demand. This enables organizations to keep metadata fresh in near real-time, without waiting for scheduled jobs in the UI.
- **Asset Profiling at Scale**
Profiling can be triggered for large data assets directly through APIs. For instance, when a new dataset lands in a data lake, an API call can immediately kick off profiling, so the dataset is fully analyzed and ready for use without manual steps.
- **Integration with External Systems**
Monitoring or CI/CD systems can interact with ADOC via APIs to enforce governance checkpoints. For example, a deployment pipeline could call ADOC to validate data reliability before pushing updates to production.

This method is particularly useful for system-to-system integrations or automation pipelines that need to interact with ADOC without manual intervention.

## Accessing API Keys

1. In the left navigation pane, click  **Settings -&gt; User Management & Access**.
2. Select **API Keys**.
3. The page displays all existing API keys along with their metadata (name, creation date, validity).

## Generating a New API Key

1. Click **Generate API Key**.
2. Provide:
    1. **Display Name**: A descriptive label for identifying the key’s purpose (e.g., ETL Integration, Pipeline Monitor Automation).
    2. **Validity Date**: The expiration date after which the key becomes invalid.
    3. Click **Generate Key**.

3. Download the key pair:
    1. **accessKey**: Public identifier for the request.
    2. **secretKey**: Private authentication token.

Note The secret key is only shown once, store it securely.

## Example: Running a Rule Execution via API

Request Format

```bash
POST http://<ADOC_HOST>:8888/api/webhook/rules/executions/:id
Headers:
  accessKey: <your_access_key>
  secretKey: <your_secret_key>
Path Params:
  id – The Rule ID (must be enabled in ADOC)
```



Example Request

```bash
curl -X POST "http://localhost:8888/api/webhook/rules/executions/24" \
-H "accessKey: K2E32HK3A9NY" \
-H "secretKey: 8bXFZMtPizehms0AryHvFuBuwk5ZAR"
```



Successful Response (truncated)

```json
{
  "execution": {
    "executionMode": "API",
    "executionStatus": "RUNNING",
    "ruleName": "example_fb_policy",
    "ruleType": "DATA_QUALITY",
    "startedAt": "2021-01-31T20:59:33.610+05:30"
  }
}
```



Unauthorized Response

```json
{
  "errors": [
    {
      "message": "Unauthorised:: Authorisation through API Keys failed",
      "status": 401
    }
  ]
}
```



## Best Practices for API Key Usage

- **Use separate keys for separate integrations**. This makes it easier to revoke access without affecting other systems.
- **Rotate keys periodically**. Helps minimize security risks.
- **Set appropriate expiry dates**. Avoid indefinite validity unless absolutely necessary.
- **Store secrets securely**. Never commit them to code repositories.