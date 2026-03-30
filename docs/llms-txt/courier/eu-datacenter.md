# Source: https://www.courier.com/docs/platform/workspaces/eu-datacenter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# EU Datacenter

> Use Courier's European datacenter for data residency compliance, GDPR requirements, and optimized performance for EU customers.

## Overview

Courier operates a dedicated European datacenter in AWS EU West 1 (Ireland) to ensure data residency compliance for European customers. You can access the same Courier workspace from both US and EU regions - the difference is where your notification data is stored and processed. EU region operations ensure all customer data remains within European borders for GDPR and regulatory compliance.

<Note>
  EU Datacenter is available for Enterprise customers. Contact [Courier Support](mailto:support@courier.com) for access or [request a demo](https://www.courier.com/request-demo) to learn more.
</Note>

## Key Features

Courier's EU datacenter provides data residency compliance while maintaining full platform functionality:

* **Data Residency Compliance** - All notification data stored and processed within EU borders
* **GDPR Compliant** - Built-in data protection controls and audit capabilities
* **Same Workspace Access** - Use your existing workspace with EU data residency
* **Reduced Latency** - Optimized performance for European users and services
* **Full Feature Parity** - Complete Courier API functionality available in EU region
* **Easy Migration** - Move existing data to EU region without workspace changes

## EU-Specific Endpoints

Access Courier services through dedicated EU endpoints:

* **API Endpoint**: `https://api.eu.courier.com`
* **Dashboard**: `https://app.eu.courier.com`
* **Data Center**: AWS EU-West 1 (Ireland)

EU region data access uses the same authentication with region-specific endpoints:

* **Same API Keys** - Your existing workspace API keys work with both US and EU endpoints
* **Region-Specific Data** - Keys access different data stores depending on the endpoint used
* **Same Key Format** - No changes needed to existing key formats (`pk_prod_*`, `pk_test_*`, etc.)
* **Single Workspace** - Same workspace accessed via different regional endpoints

<Note>
  **Data Separation**: EU and US endpoints route to different data storage locations. Use EU endpoints to ensure your data remains within European borders.
</Note>

## Getting Started

### New EU Customers

<Steps>
  <Step title="Create Courier Account">
    Sign up at [app.courier.com](https://app.courier.com) or [app.eu.courier.com](https://app.eu.courier.com) to create your workspace.
  </Step>

  <Step title="Enable EU Region">
    Contact [Courier Support](mailto:support@courier.com) to enable EU datacenter access for your workspace.
  </Step>

  <Step title="Configure API Integration">
    Use EU endpoints with your workspace API keys for data residency compliance.

    ```bash  theme={null}
    # Use EU-specific endpoint
    curl https://api.eu.courier.com/send \
      -H "Authorization: Bearer YOUR_API_KEY"
    ```
  </Step>

  <Step title="Test Integration">
    Verify your integration works correctly with EU endpoints before deploying to production.
  </Step>
</Steps>

### Migrating from US to EU Region

For existing Courier customers moving to the EU region:

<Steps>
  <Step title="Initiate Data Migration">
    Contact [Courier Support](mailto:support@courier.com) to begin migrating your data to the EU region. Our team will replicate your existing data to EU-West 1.
  </Step>

  <Step title="Update API Endpoints">
    Update your integration to use EU-specific endpoints with your existing API keys:

    ```javascript  theme={null}
    // Before (US region)
    const courier = new CourierClient({
      authorizationToken: "YOUR_API_KEY"
    });

    // After (EU region)  
    const courier = new CourierClient({
      authorizationToken: "YOUR_API_KEY", // Same key
      baseUrl: "https://api.eu.courier.com"
    });
    ```
  </Step>

  <Step title="Test EU Region Access">
    Verify your integration works correctly with EU endpoints using your existing API keys before switching production traffic.
  </Step>

  <Step title="Update Custom Domains">
    If using custom domains, update DNS/CNAME records to point to EU region endpoints.
  </Step>
</Steps>

## Code Examples

### SDK Configuration

Update your SDK configuration to use EU endpoints:

<CodeGroup>
  ```javascript Node.js theme={null}
  import { CourierClient } from "@trycourier/courier";

  const courier = new CourierClient({
    authorizationToken: process.env.COURIER_API_KEY, // Same key as US region
    baseUrl: "https://api.eu.courier.com"
  });

  // Send notification through EU region
  const { requestId } = await courier.send({
    message: {
      to: { email: "user@example.com" },
      template: "my-template",
      data: { name: "John Doe" }
    }
  });
  ```

  ```python Python theme={null}
  from trycourier import Courier

  client = Courier(
      auth_token=os.environ["COURIER_API_KEY"], # Same key as US region
      base_url="https://api.eu.courier.com"
  )

  # Send notification through EU region
  response = client.send_message(
      message={
          "to": {"email": "user@example.com"},
          "template": "my-template", 
          "data": {"name": "John Doe"}
      }
  )
  ```

  ```bash cURL theme={null}
  # EU region API call
  curl -X POST https://api.eu.courier.com/send \
    -H "Authorization: Bearer $COURIER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {"email": "user@example.com"},
        "template": "my-template",
        "data": {"name": "John Doe"}
      }
    }'
  ```
</CodeGroup>

### Environment Configuration

Set up environment variables for EU region:

```bash .env theme={null}
# Same API key works for both regions
COURIER_API_KEY=pk_prod_your_api_key_here

# EU region configuration
COURIER_EU_BASE_URL=https://api.eu.courier.com

# US region configuration (for comparison)
COURIER_US_BASE_URL=https://api.courier.com
```

## Implementation Requirements

### Data Residency Configuration

When using the EU region, ensure your integration properly handles data locality:

```javascript  theme={null}
// Verify EU region configuration
const courier = new CourierClient({
  authorizationToken: process.env.COURIER_API_KEY, // Same key
  baseUrl: "https://api.eu.courier.com" // Required for EU data residency
});

// All API calls now route to EU infrastructure
const response = await courier.send({...});
```

### GDPR Compliance Implementation

#### User Data Deletion

Handle GDPR deletion requests using the EU region API:

```bash  theme={null}
# Delete user profile and all associated data
curl -X DELETE https://api.eu.courier.com/profiles/{user_id} \
  -H "Authorization: Bearer $COURIER_API_KEY"
```

#### Data Export for Subject Access Requests

Export user data for GDPR access requests:

```bash  theme={null}
# Get complete user profile data
curl https://api.eu.courier.com/profiles/{user_id} \
  -H "Authorization: Bearer $COURIER_API_KEY"

# Get user's message history
curl https://api.eu.courier.com/profiles/{user_id}/lists \
  -H "Authorization: Bearer $COURIER_API_KEY"
```

#### Audit Log Access

Access compliance audit logs through your EU workspace:

1. Navigate to [app.eu.courier.com/logs](https://app.eu.courier.com/logs)
2. Filter by user ID or time range for compliance reporting
3. Export logs as needed for regulatory audits

<Warning>
  Enterprise customers should review compliance documentation at [security.courier.com](https://security.courier.com/) before handling personal data.
</Warning>

## Troubleshooting

### Common Issues

#### Authentication Errors

If experiencing authentication failures:

1. **Verify API Key** - Ensure you're using valid workspace API keys
2. **Check Endpoint URL** - Confirm requests target `api.eu.courier.com`
3. **Test Key Format** - Verify key format matches expected pattern

#### 404 Not Found Errors

When receiving 404 errors:

1. **Confirm Data Migration** - Verify your data has been migrated to EU region
2. **Check API Endpoints** - Ensure all URLs point to EU region
3. **Review Resource IDs** - Some resources may exist only in US region if migration is incomplete

#### CORS Configuration

For browser-based applications:

1. **Allowlist EU Origins** - Ensure `https://app.eu.courier.com` is allowlisted
2. **Update CORS Settings** - Configure CORS for EU-specific domains
3. **Check Preflight Requests** - Verify OPTIONS requests work with EU endpoints

### Performance Monitoring

Monitor EU region performance:

* **Status Page** - Check [status.courier.com](https://status.courier.com) for EU-specific incidents
* **Regional Health** - Monitor EU region service health and latency
* **API Response Times** - Compare performance between regions if needed

## Service Level Agreement

### EU Region SLA

* **Uptime Guarantee** - 99.9% uptime SLA for EU region services
* **Incident Response** - 24/7 monitoring and response team
* **Regional Failover** - Automated failover capabilities within EU region
* **Performance Standards** - Sub-200ms response times for EU-based requests

## Next Steps

<CardGroup cols={2}>
  <Card title="Contact Support" href="mailto:support@courier.com" icon="headset">
    Get expert assistance with EU region setup and migration
  </Card>

  <Card title="API Reference" href="/reference/get-started" icon="code">
    Complete API documentation for EU region integration
  </Card>

  <Card title="Workspace Settings" href="/platform/workspaces/environments-api-keys" icon="gear">
    Configure API keys and environment settings for EU region
  </Card>

  <Card title="Compliance Documentation" href="https://security.courier.com/" icon="shield">
    GDPR compliance and data processing agreements
  </Card>
</CardGroup>
