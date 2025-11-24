# Source: https://docs.anchorbrowser.io/advanced/mfa.md

# MFA

> Real-time event signaling and coordination between external systems and browser instances

# Event Coordination

Event coordination allows you to send real-time messages between external systems and active browser instances. This is particularly useful for **multi-factor authentication (MFA)** where you need to inject authentication codes during browser automation.

## Overview

The system provides two operations:

* **Signal Event**: Send data to an event channel
* **Wait for Event**: Listen for data on an event channel with timeout

Events are user-scoped and work across multiple browser instances.

<Expandable title="API Endpoints">
  ## API Endpoints

  ### Signal an Event

  ```http  theme={null}
  POST https://api.anchorbrowser.io/api/v1/events/{eventName}
  ```

  ### Wait for an Event

  ```http  theme={null}
  POST https://api.anchorbrowser.io/api/v1/events/{eventName}/wait
  ```

  Both endpoints require `anchor-api-key` header and accept JSON payloads.

  ####
</Expandable>

## MFA Use Case

Handle MFA codes during automated login flows:

```javascript  theme={null}
// In your browser automation script
async function handleMFAFlow() {
  await page.fill('#username', 'user@example.com');
  await page.fill('#password', 'password');
  await page.click('#login-button');
  
  // Wait for MFA code from external system
  const mfaEvent = await waitForEvent('mfa_code', 30000);
  
  if (mfaEvent?.data?.code) {
    await page.fill('#mfa-code', mfaEvent.data.code);
    await page.click('#verify-button');
  }
}
```

```javascript  theme={null}
// In your external system (mobile app, webhook, etc.)
async function sendMFACode(code) {
  await signalEvent('mfa_code', { code });
}
```

## Implementation

### Helper Functions

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  async function signalEvent(eventName, data) {
    try {
      const response = await anchor_client.events.signal(eventName, { data: data || {} });
      return response;
    } catch (error) {
      throw new Error(`Failed to signal event: ${error.message}`);
    }
  }

  async function waitForEvent(eventName, timeoutMs = 60000) {
    try {
      const response = await anchor_client.events.waitFor(eventName, { timeoutMs });
      return response;
    } catch (error) {
      if (error.message.includes("408")) return null; // Timeout
      throw new Error(`Failed to wait for event: ${error.message}`);
    }
  }
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  def signal_event(event_name, data):
      try:
          response = anchor_client.events.signal(event_name, data=data or {})
          return response
      except Exception as error:
          raise Exception(f"Failed to signal event: {error}")

  def wait_for_event(event_name, timeout_ms=60000):
      try:
          response = anchor_client.events.wait_for(event_name, timeout_ms=timeout_ms)
          return response
      except Exception as error:
          if "408" in str(error):
              return None  # Timeout
          raise Exception(f"Failed to wait for event: {error}")
  ```
</CodeGroup>

## Event Flow Patterns

**Signal First, Wait Later** (immediate consumption):

```javascript  theme={null}
await signalEvent("data", { value: "preloaded" });
const data = await waitForEvent("data", 1000); // Short timeout
```

**Wait First, Signal Later** (typical MFA flow):

```javascript  theme={null}
const waitPromise = waitForEvent("mfa_code", 60000);
// ... other operations ...
const mfaData = await waitPromise;
```

## Best Practices

* Use descriptive event names: `mfa_code_login`, `mfa_code_transfer`
* Always set appropriate timeouts
* Validate received event data
* Handle timeout scenarios gracefully
