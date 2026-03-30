# Source: https://novita.ai/docs/guides/error.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Common Error Codes

This document summarizes the most common error codes returned by the Novita API platform, along with definitions, causes, and recommended solutions to help users troubleshoot efficiently.

***

## Error Code 400

**Description**: Invalid request parameters.\
**Solution**:\
Review the error message details and check whether the parameter formats, field names, or value ranges comply with the API documentation.

***

## Error Code 401

**Description**: API Key is missing or incorrect.\
**Solution**:

* Ensure the API Key is provided in the request;
* Verify that the API Key is correct and has not expired;
* If using environment variables or config files, confirm they are being read correctly during execution.

***

## Error Code 403

**Description**: Access denied due to insufficient permissions.\
**Solution**:

* Verify that your account associated with the API Key has permission to access the requested model;
* Some models require identity verification to access:
  * Log in to the console and check your account’s verification status;
  * If not verified, complete identity verification first;
  * Alternatively, use an API Key from an already verified account.

***

## Error Code 429

**Description**: Rate limit exceeded (Too Many Requests).\
**Solution**:

* Check if the limit is due to **TPM** (tokens per minute) or **RPM** (requests per minute);
* Refer to the official Rate Limits documentation;
* To raise your rate limit, contact support or use a verified account.

***

## Error Code 503 / 504

**Description**: Backend timeout or service unavailable, often caused by high system load or throttling.

### Possible Causes:

* GPU or CPU overload on model service nodes;
* Long generation time on non-streaming requests exceeds gateway timeout;
* Failures in downstream services (e.g., Redis, model engine);
* Traffic shaping module activated surge protection and returned 503.

### Recommended Solutions:

**For API Users**:

* **Enable retry mechanism**: Use exponential backoff to prevent repeated overload;
* **Switch to streaming mode**: Streaming responses return tokens as they’re generated, lowering latency and timeout risk;
* **Optimize client settings**: Ensure `client_timeout` and `proxy_timeout` exceed 60 seconds;
* **Avoid peak periods**: For high concurrency scenarios, retry during off-peak hours.

**For Platform Ops**:

* Enhance monitoring and auto-scaling of model services;
* Adjust gateway-level `proxy_read_timeout` appropriately;
* Implement fine-grained throttling rules (e.g., priority queues, core-business prioritization);
* Use Prometheus + Alertmanager to trigger alerts on 503/504 spikes.

***

## Error Code 500

**Description**: Internal server error—typically caused by backend exceptions or model engine crashes.\
**Solution**:

* These issues usually require platform-side resolution. Contact support to investigate logs and system resources;
* Optionally, try switching models or falling back to a less resource-intensive configuration.

***

## Other Errors

For undefined or undocumented errors:

* First, refer to the `message` field in the API response;
* Next, check request logs or console traces;
* Finally, contact Novita support or submit a ticket for further assistance.


Built with [Mintlify](https://mintlify.com).