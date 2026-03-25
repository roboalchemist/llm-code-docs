# Source: https://docs.drip.re/developer/errors.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Handling

> Complete guide to API errors, status codes, and troubleshooting

This guide covers all aspects of error handling when working with the DRIP API, including common error scenarios, proper error handling techniques, and troubleshooting steps.

## Error Response Format

All DRIP API errors follow a consistent format:

```json  theme={"dark"}
{
  "error": "ValidationError",
  "message": "Invalid request parameters",
  "details": {
    "field": "tokens",
    "issue": "Must be a positive integer"
  },
  "requestId": "req_1234567890abcdef",
  "timestamp": "2024-01-20T15:30:00Z"
}
```

### Error Response Fields

| Field       | Description                               |
| ----------- | ----------------------------------------- |
| `error`     | Error type identifier                     |
| `message`   | Human-readable error description          |
| `details`   | Additional error context (when available) |
| `requestId` | Unique request identifier for support     |
| `timestamp` | When the error occurred                   |

## HTTP Status Codes

The DRIP API uses standard HTTP status codes:

### 2xx Success

* **200 OK**: Request successful
* **201 Created**: Resource created successfully
* **204 No Content**: Request successful, no response body

### 4xx Client Errors

* **400 Bad Request**: Invalid request format or parameters
* **401 Unauthorized**: Missing or invalid authentication
* **403 Forbidden**: Valid authentication but insufficient permissions
* **404 Not Found**: Requested resource doesn't exist
* **409 Conflict**: Request conflicts with current resource state
* **422 Unprocessable Entity**: Valid format but business logic error
* **429 Too Many Requests**: Rate limit exceeded

### 5xx Server Errors

* **500 Internal Server Error**: Unexpected server error
* **502 Bad Gateway**: Upstream service error
* **503 Service Unavailable**: Temporary service outage
* **504 Gateway Timeout**: Upstream service timeout

## Common Error Types

### Authentication Errors

<AccordionGroup>
  <Accordion title="401 Unauthorized - Invalid API Key">
    ```json  theme={"dark"}
    {
      "error": "Unauthorized",
      "message": "Invalid API key provided"
    }
    ```

    **Causes:**

    * API key is incorrect or malformed
    * API key has been revoked
    * Missing Authorization header

    **Solutions:**

    * Verify your API key is correct
    * Generate a new API key if needed
    * Ensure proper header format: `Authorization: Bearer YOUR_KEY`
  </Accordion>

  <Accordion title="403 Forbidden - Insufficient Permissions">
    ```json  theme={"dark"}
    {
      "error": "Forbidden",
      "message": "Insufficient permissions to access this resource"
    }
    ```

    **Causes:**

    * API key lacks required permissions
    * Trying to access another realm's resources
    * Account permissions have been changed

    **Solutions:**

    * Check your account permissions in the dashboard
    * Ensure you're using the correct realm ID
    * Contact an admin to update permissions
  </Accordion>
</AccordionGroup>

### Validation Errors

<AccordionGroup>
  <Accordion title="400 Bad Request - Invalid Parameters">
    ```json  theme={"dark"}
    {
      "error": "ValidationError",
      "message": "Invalid request parameters",
      "details": {
        "tokens": "Must be a number between -1000000 and 1000000",
        "realmPointId": "Must be a valid ObjectId"
      }
    }
    ```

    **Common Issues:**

    * Invalid data types (string instead of number)
    * Missing required fields
    * Values outside allowed ranges
    * Malformed IDs

    **Solutions:**

    * Validate input data before sending requests
    * Check API documentation for required fields and formats
    * Use proper data types in your requests
  </Accordion>

  <Accordion title="422 Unprocessable Entity - Business Logic Error">
    ```json  theme={"dark"}
    {
      "error": "InsufficientBalance",
      "message": "Member does not have enough points for this operation",
      "details": {
        "currentBalance": 50,
        "requestedAmount": 100,
        "memberId": "507f1f77bcf86cd799439013"
      }
    }
    ```

    **Common Scenarios:**

    * Insufficient point balance for transfers
    * Duplicate resource creation
    * Quest already completed
    * Store item out of stock

    **Solutions:**

    * Check resource state before operations
    * Implement proper business logic validation
    * Handle edge cases gracefully
  </Accordion>
</AccordionGroup>

### Resource Errors

<AccordionGroup>
  <Accordion title="404 Not Found - Resource Missing">
    ```json  theme={"dark"}
    {
      "error": "NotFound",
      "message": "Realm member not found",
      "details": {
        "realmId": "507f1f77bcf86cd799439011",
        "memberId": "507f1f77bcf86cd799439013"
      }
    }
    ```

    **Common Causes:**

    * Incorrect resource IDs
    * Resource has been deleted
    * Member hasn't joined the realm
    * Typos in endpoint URLs

    **Solutions:**

    * Verify resource IDs are correct
    * Check if resources exist before operations
    * Handle missing resources gracefully
  </Accordion>

  <Accordion title="409 Conflict - Resource State Conflict">
    ```json  theme={"dark"}
    {
      "error": "ConflictError",
      "message": "Quest is already completed and cannot be modified",
      "details": {
        "questId": "507f1f77bcf86cd799439015",
        "currentStatus": "completed"
      }
    }
    ```

    **Common Scenarios:**

    * Modifying completed quests
    * Creating duplicate resources
    * Concurrent modification conflicts

    **Solutions:**

    * Check resource state before modifications
    * Implement proper concurrency handling
    * Use appropriate HTTP methods (PUT vs PATCH)
  </Accordion>
</AccordionGroup>

### Rate Limiting Errors

<AccordionGroup>
  <Accordion title="429 Too Many Requests">
    ```json  theme={"dark"}
    {
      "error": "RateLimitExceeded",
      "message": "Too many requests. Try again in 60 seconds.",
      "details": {
        "limit": 100,
        "window": 60,
        "retryAfter": 60
      }
    }
    ```

    **Solutions:**

    * Implement exponential backoff
    * Respect the Retry-After header
    * Use batch operations when possible
    * See the [Rate Limits guide](/developer/rate-limits) for details
  </Accordion>
</AccordionGroup>

## Error Handling Implementation

### JavaScript/Node.js

<CodeGroup>
  ```javascript Comprehensive Error Handler theme={"dark"}
  class DripAPIError extends Error {
    constructor(status, error, message, details, requestId) {
      super(message);
      this.name = 'DripAPIError';
      this.status = status;
      this.error = error;
      this.details = details;
      this.requestId = requestId;
    }
  }

  class DripClient {
    async request(method, endpoint, data = null) {
      try {
        const response = await fetch(`${this.baseUrl}${endpoint}`, {
          method,
          headers: {
            'Authorization': `Bearer ${this.apiKey}`,
            'Content-Type': 'application/json'
          },
          body: data ? JSON.stringify(data) : null
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new DripAPIError(
            response.status,
            errorData.error,
            errorData.message,
            errorData.details,
            errorData.requestId
          );
        }

        return response.json();
      } catch (error) {
        if (error instanceof DripAPIError) {
          throw error;
        }
        
        // Handle network errors, JSON parsing errors, etc.
        throw new Error(`Network error: ${error.message}`);
      }
    }

    async safeRequest(method, endpoint, data = null, options = {}) {
      const { retries = 3, retryDelay = 1000 } = options;
      
      for (let attempt = 0; attempt <= retries; attempt++) {
        try {
          return await this.request(method, endpoint, data);
        } catch (error) {
          if (error instanceof DripAPIError) {
            // Don't retry client errors (4xx) except rate limits
            if (error.status >= 400 && error.status < 500 && error.status !== 429) {
              throw error;
            }
            
            // Handle rate limits
            if (error.status === 429) {
              const retryAfter = error.details?.retryAfter || 60;
              if (attempt < retries) {
                await this.sleep(retryAfter * 1000);
                continue;
              }
            }
            
            // Retry server errors (5xx)
            if (error.status >= 500 && attempt < retries) {
              await this.sleep(retryDelay * Math.pow(2, attempt));
              continue;
            }
          }
          
          // Final attempt or non-retryable error
          if (attempt === retries) {
            throw error;
          }
        }
      }
    }

    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }
  }

  ```

  ```javascript Usage Example theme={"dark"}
  const client = new DripClient(apiKey, realmId);

  async function updateMemberSafely(memberId, tokens) {
    try {
      const result = await client.safeRequest(
        'PATCH',
        `/realm/${client.realmId}/members/${memberId}/point-balance`,
        { tokens }
      );
      
      console.log('Balance updated successfully:', result);
      return { success: true, data: result };
      
    } catch (error) {
      if (error instanceof DripAPIError) {
        console.error(`API Error [${error.status}]:`, error.message);
        
        switch (error.error) {
          case 'NotFound':
            return { success: false, error: 'Member not found' };
          case 'InsufficientBalance':
            return { success: false, error: 'Not enough points' };
          case 'ValidationError':
            return { success: false, error: 'Invalid input data' };
          default:
            return { success: false, error: 'API error occurred' };
        }
      } else {
        console.error('Network error:', error.message);
        return { success: false, error: 'Network error' };
      }
    }
  }
  ```

</CodeGroup>

### Python

<CodeGroup>
  ```python Error Handling Class theme={"dark"}
  import requests
  import time
  from typing import Optional, Dict, Any

  class DripAPIError(Exception):
      def **init**(self, status: int, error: str, message: str, details: Optional[Dict] = None, request_id: Optional[str] = None):
          super().**init**(message)
          self.status = status
          self.error = error
          self.message = message
          self.details = details or {}
          self.request_id = request_id

  class DripClient:
      def **init**(self, api_key: str, realm_id: str):
          self.api_key = api_key
          self.realm_id = realm_id
          self.base_url = 'https://api.drip.re/api/v1'
          self.session = requests.Session()
          self.session.headers.update({
              'Authorization': f'Bearer {api_key}',
              'Content-Type': 'application/json'
          })

      def request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict[Any, Any]:
          try:
              response = self.session.request(method, f"{self.base_url}{endpoint}", json=data)
              
              if not response.ok:
                  try:
                      error_data = response.json()
                  except ValueError:
                      error_data = {'error': 'UnknownError', 'message': 'Unknown error occurred'}
                  
                  raise DripAPIError(
                      status=response.status_code,
                      error=error_data.get('error', 'UnknownError'),
                      message=error_data.get('message', 'Unknown error'),
                      details=error_data.get('details'),
                      request_id=error_data.get('requestId')
                  )
              
              return response.json()
              
          except requests.exceptions.RequestException as e:
              raise Exception(f"Network error: {str(e)}")

      def safe_request(self, method: str, endpoint: str, data: Optional[Dict] = None, retries: int = 3, retry_delay: int = 1) -> Dict[Any, Any]:
          for attempt in range(retries + 1):
              try:
                  return self.request(method, endpoint, data)
                  
              except DripAPIError as e:
                  # Don't retry client errors except rate limits
                  if 400 <= e.status < 500 and e.status != 429:
                      raise e
                  
                  # Handle rate limits
                  if e.status == 429:
                      retry_after = e.details.get('retryAfter', 60)
                      if attempt < retries:
                          time.sleep(retry_after)
                          continue
                  
                  # Retry server errors
                  if e.status >= 500 and attempt < retries:
                      time.sleep(retry_delay * (2 ** attempt))
                      continue
                  
                  # Final attempt
                  if attempt == retries:
                      raise e
                      
              except Exception as e:
                  if attempt == retries:
                      raise e
                  time.sleep(retry_delay * (2 ** attempt))

  ```

  ```python Usage Example theme={"dark"}
  def update_member_safely(client: DripClient, member_id: str, tokens: int) -> Dict[str, Any]:
      try:
          result = client.safe_request(
              'PATCH',
              f'/realm/{client.realm_id}/members/{member_id}/point-balance',
              {'tokens': tokens}
          )
          
          print('Balance updated successfully:', result)
          return {'success': True, 'data': result}
          
      except DripAPIError as e:
          print(f"API Error [{e.status}]: {e.message}")
          
          error_mapping = {
              'NotFound': 'Member not found',
              'InsufficientBalance': 'Not enough points',
              'ValidationError': 'Invalid input data'
          }
          
          error_message = error_mapping.get(e.error, 'API error occurred')
          return {'success': False, 'error': error_message}
          
      except Exception as e:
          print('Network error:', str(e))
          return {'success': False, 'error': 'Network error'}
  ```

</CodeGroup>

## Debugging and Troubleshooting

### Request ID Tracking

Always log the `requestId` from error responses for support:

```javascript  theme={"dark"}
function logError(error) {
  if (error instanceof DripAPIError) {
    console.error(`[${error.requestId}] ${error.error}: ${error.message}`);
    if (error.details) {
      console.error('Details:', JSON.stringify(error.details, null, 2));
    }
  }
}
```

### Common Debugging Steps

<Steps>
  <Step title="Verify API Key">
    Test your API key with a simple request:

    ```bash  theme={"dark"}
    curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID" \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -w "\nStatus: %{http_code}\n"
    ```
  </Step>

  <Step title="Check Request Format">
    Ensure your request matches the API documentation:

    * Correct HTTP method
    * Proper JSON format
    * Required headers included
    * Valid parameter types
  </Step>

  <Step title="Validate Resource IDs">
    Confirm that all IDs in your request are valid:

    * Realm ID exists and you have access
    * Member ID exists in the realm
    * Point type ID is correct
  </Step>

  <Step title="Test with cURL">
    Replicate the failing request with cURL to isolate the issue:

    ```bash  theme={"dark"}
    curl -X PATCH "https://api.drip.re/api/v1/realm/REALM_ID/members/MEMBER_ID/point-balance" \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"tokens": 100}' \
      -v
    ```
  </Step>
</Steps>

### Error Monitoring

Set up monitoring to track error patterns:

```javascript  theme={"dark"}
class ErrorMonitor {
  constructor() {
    this.errors = [];
  }

  recordError(error, context = {}) {
    this.errors.push({
      timestamp: new Date().toISOString(),
      status: error.status,
      error: error.error,
      message: error.message,
      requestId: error.requestId,
      context
    });

    // Alert on high error rates
    this.checkErrorRate();
  }

  checkErrorRate() {
    const recentErrors = this.errors.filter(
      e => Date.now() - new Date(e.timestamp).getTime() < 300000 // Last 5 minutes
    );

    if (recentErrors.length > 10) {
      console.warn('High error rate detected:', recentErrors.length, 'errors in 5 minutes');
      // Send alert to monitoring system
    }
  }

  getErrorStats() {
    const last24h = this.errors.filter(
      e => Date.now() - new Date(e.timestamp).getTime() < 86400000
    );

    const errorCounts = last24h.reduce((acc, error) => {
      acc[error.error] = (acc[error.error] || 0) + 1;
      return acc;
    }, {});

    return {
      total: last24h.length,
      byType: errorCounts,
      recent: last24h.slice(-10)
    };
  }
}
```

## Best Practices

<CardGroup cols={2}>
  <Card title="Graceful Degradation" icon="shield-check">
    * Always handle errors gracefully
    * Provide meaningful user feedback
    * Implement fallback behaviors
    * Log errors for debugging
  </Card>

  <Card title="Retry Logic" icon="arrows-rotate">
    * Implement exponential backoff
    * Don't retry client errors (4xx)
    * Respect rate limit headers
    * Set maximum retry limits
  </Card>

  <Card title="Error Logging" icon="file-text">
    * Log all API errors with context
    * Include request IDs for support
    * Monitor error patterns
    * Set up alerting for high error rates
  </Card>

  <Card title="User Experience" icon="heart">
    * Show user-friendly error messages
    * Provide actionable next steps
    * Handle loading and error states
    * Implement proper error boundaries
  </Card>
</CardGroup>

## Getting Help

When contacting support about API errors:

1. **Include the Request ID** from the error response
2. **Provide the full error response** with status code
3. **Share your request details** (without sensitive data)
4. **Describe the expected behavior** vs what happened
5. **Include relevant logs** and timestamps

<CardGroup cols={2}>
  <Card title="Discord Support" icon="discord" href="https://discord.gg/dripchain">
    Join our community for help and discussions
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Check the complete API documentation
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
