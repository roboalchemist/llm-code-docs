# Source: https://smartcar.com/docs/api-reference/webhooks/events/vehicle-error.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# VEHICLE_ERROR Event

> Error notifications and resolution tracking for signal retrieval issues

Triggered when Smartcar encounters an error while attempting to retrieve signal data from a vehicle. This event helps you monitor data availability, understand missing or stale signal data and provide an event to trigger a user action to resolve the issue.

## When This Event Fires

The `VEHICLE_ERROR` event fires when:

* Smartcar detects an error while retrieving signal data
* The vehicle manufacturer's API returns an error
* The vehicle is offline or unreachable
* Authentication, permission, or compatibility errors occur

<Info>
  **Resolution notifications**: When an error condition is resolved (e.g., vehicle comes back online), Smartcar sends another `VEHICLE_ERROR` event with `state` set to `"RESOLVED"`. This enables automatic recovery workflows.
</Info>

***

## Error Categories

Errors are categorized by type and include specific error codes:

<AccordionGroup>
  <Accordion title="Connected Services Account Errors" icon="user-slash">
    Issues with the user's account with the vehicle manufacturer.

    | Type                         | Code                    | Description                                     |
    | ---------------------------- | ----------------------- | ----------------------------------------------- |
    | `CONNECTED_SERVICES_ACCOUNT` | `ACCOUNT_ISSUE`         | General account problem                         |
    | `CONNECTED_SERVICES_ACCOUNT` | `AUTHENTICATION_FAILED` | Authentication credentials are invalid          |
    | `CONNECTED_SERVICES_ACCOUNT` | `PERMISSION`            | User lacks necessary permissions                |
    | `CONNECTED_SERVICES_ACCOUNT` | `SUBSCRIPTION`          | Required subscription is inactive or expired    |
    | `CONNECTED_SERVICES_ACCOUNT` | `VIRTUAL_KEY_REQUIRED`  | Vehicle requires a virtual key to be configured |
  </Accordion>

  <Accordion title="Vehicle State Errors" icon="car-battery">
    Issues with the vehicle's connectivity or state.

    | Type            | Code                     | Description                              |
    | --------------- | ------------------------ | ---------------------------------------- |
    | `VEHICLE_STATE` | `REMOTE_ACCESS_DISABLED` | Remote access is disabled on the vehicle |
    | `VEHICLE_STATE` | `ASLEEP`                 | Vehicle is in sleep mode                 |
    | `VEHICLE_STATE` | `UNREACHABLE`            | Vehicle is not connected to the internet |
  </Accordion>

  <Accordion title="Compatibility Errors" icon="plug">
    Issues with signal availability for the specific vehicle.

    | Type            | Code                   | Description                                      |
    | --------------- | ---------------------- | ------------------------------------------------ |
    | `COMPATIBILITY` | `MAKE_NOT_COMPATIBLE`  | Vehicle manufacturer doesn't support this signal |
    | `COMPATIBILITY` | `SMARTCAR_NOT_CAPABLE` | Smartcar cannot retrieve this signal yet         |
    | `COMPATIBILITY` | `VEHICLE_NOT_CAPABLE`  | This specific vehicle doesn't support the signal |
  </Accordion>

  <Accordion title="Permission Errors" icon="lock">
    Issues with granted permissions.

    | Type         | Code   | Description                             |
    | ------------ | ------ | --------------------------------------- |
    | `PERMISSION` | `null` | Required permission not granted by user |
  </Accordion>
</AccordionGroup>

***

## Payload Structure

<ResponseField name="eventId" type="string" required>
  Unique identifier for this event. Use this for idempotency to prevent duplicate processing.
</ResponseField>

<ResponseField name="eventType" type="string" required>
  Always `"VEHICLE_ERROR"` for this event type.
</ResponseField>

<ResponseField name="vehicleId" type="string" required>
  Smartcar vehicle ID for the vehicle this event relates to.
</ResponseField>

<ResponseField name="data" type="object" required>
  Container for event data.

  <Expandable title="data object">
    <ResponseField name="user" type="object" required>
      Information about the user who connected the vehicle.

      <ResponseField name="id" type="string">
        Smartcar user ID
      </ResponseField>
    </ResponseField>

    <ResponseField name="vehicle" type="object" required>
      Vehicle information

      <ResponseField name="id" type="string">
        Smartcar vehicle ID
      </ResponseField>

      <ResponseField name="make" type="string">
        Vehicle manufacturer (e.g., `"TESLA"`, `"FORD"`, `"BMW"`)
      </ResponseField>

      <ResponseField name="model" type="string">
        Vehicle model (e.g., `"Model 3"`, `"Mustang Mach-E"`)
      </ResponseField>

      <ResponseField name="year" type="integer">
        Vehicle model year
      </ResponseField>
    </ResponseField>

    <ResponseField name="errors" type="array" required>
      Array of error objects. Multiple errors may occur simultaneously.

      <ResponseField name="type" type="string">
        Error category: `CONNECTED_SERVICES_ACCOUNT`, `VEHICLE_STATE`, `COMPATIBILITY`, or `PERMISSION`
      </ResponseField>

      <ResponseField name="code" type="string">
        Specific error code (see error categories above)
      </ResponseField>

      <ResponseField name="state" type="string">
        Error state: `"ERROR"` when error is active, `"RESOLVED"` when the issue has been fixed
      </ResponseField>

      <ResponseField name="description" type="string">
        Technical description of the error for logging and debugging
      </ResponseField>

      <ResponseField name="suggestedUserMessage" type="string">
        User-friendly error message suitable for display to end users. Use this in your application UI.
      </ResponseField>

      <ResponseField name="docURL" type="string">
        Link to detailed error documentation. Useful for linking users to troubleshooting guides.
      </ResponseField>

      <ResponseField name="resolution" type="object">
        Suggested resolution steps

        <ResponseField name="type" type="string">
          Resolution category: `RETRY_LATER`, `CONTACT_SUPPORT`, `USER_ACTION_REQUIRED`, etc.
        </ResponseField>
      </ResponseField>

      <ResponseField name="signals" type="array">
        Array of signal objects that were affected by this error.

        <ResponseField name="code" type="string">
          Kebab-case signal identifier (e.g., `"location-preciselocation"`)
        </ResponseField>

        <ResponseField name="name" type="string">
          Human-readable signal name (e.g., `"PreciseLocation"`)
        </ResponseField>

        <ResponseField name="group" type="string">
          Signal category (e.g., `"Location"`, `"TractionBattery"`)
        </ResponseField>
      </ResponseField>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="meta" type="object" required>
  Webhook delivery metadata. See [Event Reference Overview](/api-reference/webhooks/events/overview#common-fields) for complete `meta` object schema.
</ResponseField>

## Example Payloads

<Tabs>
  <Tab title="Error State">
    Delivered when an error occurs.

    ```json  theme={null}
    {
      "eventId": "5a537912-9ad3-424b-ba33-65a1704567e9",
      "eventType": "VEHICLE_ERROR",
      "vehicleId": "123e4567-e89b-12d3-a456-426614174000",
      "data": {
        "user": {
          "id": "93b3ea96-ca37-43a9-9073-f4334719iok7"
        },
        "vehicle": {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "make": "TESLA",
          "model": "Model 3",
          "year": 2020
        },
        "errors": [
          {
            "type": "COMPATIBILITY",
            "code": "VEHICLE_NOT_CAPABLE",
            "state": "ERROR",
            "description": "The vehicle is incapable of performing your request.",
            "suggestedUserMessage": "Your car is unable to perform this request.",
            "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#vehicle-not-capable",
            "resolution": {
              "type": "CONTACT_SUPPORT"
            },
            "signals": [
              {
                "code": "location-preciselocation",
                "name": "PreciseLocation",
                "group": "Location"
              },
              {
                "code": "tractionbattery-stateofcharge",
                "name": "StateOfCharge",
                "group": "TractionBattery"
              }
            ]
          }
        ]
      },
      "meta": {
        "version": "4.0",
        "deliveryId": "48b25f8f-9fea-42e1-9085-81043682cbb8",
        "deliveredAt": 1761896351529,
        "webhookId": "123e4567-e89b-12d3-a456-426614174000",
        "webhookName": "Battery Monitoring",
        "mode": "LIVE"
      }
    }
    ```
  </Tab>

  <Tab title="Resolved State">
    Delivered when an error condition is resolved.

    ```json  theme={null}
    {
      "eventId": "8d9e0f1a-2b3c-4d5e-6f7a-8b9c0d1e2f3a",
      "eventType": "VEHICLE_ERROR",
      "vehicleId": "123e4567-e89b-12d3-a456-426614174000",
      "data": {
        "user": {
          "id": "93b3ea96-ca37-43a9-9073-f4334719iok7"
        },
        "vehicle": {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "make": "TESLA",
          "model": "Model 3",
          "year": 2020
        },
        "errors": [
          {
            "type": "VEHICLE_STATE",
            "code": "UNREACHABLE",
            "state": "RESOLVED",
            "description": "The vehicle is now reachable.",
            "signals": [
              {
                "code": "location-preciselocation",
                "name": "PreciseLocation",
                "group": "Location"
              }
            ]
          }
        ]
      },
      "meta": {
        "version": "4.0",
        "deliveryId": "9f8e7d6c-5b4a-3c2b-1d0e-9f8e7d6c5b4a",
        "deliveredAt": 1761898351529,
        "webhookId": "123e4567-e89b-12d3-a456-426614174000",
        "webhookName": "Battery Monitoring",
        "mode": "LIVE"
      }
    }
    ```
  </Tab>
</Tabs>

***

## Common Error Scenarios

| Scenario                                | Type                         | Code                  | Recommended Action                              |
| --------------------------------------- | ---------------------------- | --------------------- | ----------------------------------------------- |
| Vehicle offline                         | `VEHICLE_STATE`              | `UNREACHABLE`         | Retry later; notify user if persistent          |
| User revoked permissions                | `CONNECTED_SERVICES_ACCOUNT` | `PERMISSION`          | Prompt user to re-authenticate                  |
| Connected services subscription expired | `CONNECTED_SERVICES_ACCOUNT` | `SUBSCRIPTION`        | Direct user to renew manufacturer subscription  |
| Signal not supported                    | `COMPATIBILITY`              | `VEHICLE_NOT_CAPABLE` | Remove signal from webhook or handle gracefully |
| Vehicle asleep                          | `VEHICLE_STATE`              | `ASLEEP`              | Retry later; avoid waking vehicle unnecessarily |

***

## Processing VEHICLE\_ERROR Events

### Basic Handler

```javascript  theme={null}
function handleVehicleError(payload) {
  const { vehicleId, data } = payload;
  const { errors } = data;
  
  errors.forEach(error => {
    if (error.state === 'ERROR') {
      // New error
      logError(vehicleId, error);
      notifyUser(vehicleId, error.suggestedUserMessage);
      
      // Take action based on error type
      if (error.resolution.type === 'RETRY_LATER') {
        scheduleRetry(vehicleId, error.signals);
      } else if (error.resolution.type === 'USER_ACTION_REQUIRED') {
        sendUserNotification(vehicleId, error);
      }
    } else if (error.state === 'RESOLVED') {
      // Error resolved
      logResolution(vehicleId, error);
      clearErrorState(vehicleId, error.code);
      notifyUser(vehicleId, 'Issue resolved, data is now available');
    }
  });
}
```

### Best Practices

<AccordionGroup>
  <Accordion title="Track error state changes" icon="chart-line">
    Monitor both `ERROR` and `RESOLVED` states to implement automatic recovery workflows.

    ```javascript  theme={null}
    async function trackErrorState(payload) {
      const { vehicleId, data } = payload;
      
      for (const error of data.errors) {
        if (error.state === 'ERROR') {
          await db.errors.insert({
            vehicleId,
            errorType: error.type,
            errorCode: error.code,
            affectedSignals: error.signals.map(s => s.code),
            detectedAt: new Date()
          });
        } else if (error.state === 'RESOLVED') {
          await db.errors.update(
            { vehicleId, errorCode: error.code },
            { resolvedAt: new Date(), status: 'resolved' }
          );
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Use suggestedUserMessage for notifications" icon="envelope">
    Display the user-friendly message to vehicle owners instead of technical error descriptions.

    ```javascript  theme={null}
    function notifyVehicleOwner(error, userId) {
      const message = error.suggestedUserMessage || 
        'We encountered an issue retrieving data from your vehicle.';
      
      sendNotification(userId, {
        title: 'Vehicle Data Unavailable',
        body: message,
        link: error.docURL // Link to troubleshooting docs
      });
    }
    ```
  </Accordion>

  <Accordion title="Implement retry logic for transient errors" icon="rotate">
    Some errors (ASLEEP, UNREACHABLE) are transient. Implement exponential backoff retries.

    ```javascript  theme={null}
    const TRANSIENT_ERROR_CODES = ['ASLEEP', 'UNREACHABLE'];

    function shouldRetry(error) {
      return TRANSIENT_ERROR_CODES.includes(error.code);
    }

    async function handleTransientError(vehicleId, error) {
      const retryDelays = [60000, 300000, 900000]; // 1m, 5m, 15m
      
      for (const delay of retryDelays) {
        await sleep(delay);
        
        try {
          // Attempt to fetch data again
          const data = await smartcar.fetchSignals(vehicleId, error.signals);
          return data; // Success
        } catch (err) {
          // Still failing, continue retrying
        }
      }
      
      // All retries failed
      notifyUser(vehicleId, 'Unable to reach vehicle after multiple attempts');
    }
    ```
  </Accordion>

  <Accordion title="Handle multiple simultaneous errors" icon="layer-group">
    A single `VEHICLE_ERROR` event can contain multiple errors affecting different signals.

    ```javascript  theme={null}
    function categorizeErrors(errors) {
      const categorized = {
        transient: [],
        userAction: [],
        permanent: []
      };
      
      errors.forEach(error => {
        if (['ASLEEP', 'UNREACHABLE'].includes(error.code)) {
          categorized.transient.push(error);
        } else if (error.resolution.type === 'USER_ACTION_REQUIRED') {
          categorized.userAction.push(error);
        } else {
          categorized.permanent.push(error);
        }
      });
      
      return categorized;
    }
    ```
  </Accordion>

  <Accordion title="Degrade gracefully in your UI" icon="shield-halved">
    When errors occur, show stale data with a clear indication that it's not current.

    ```javascript  theme={null}
    function displayVehicleData(vehicleId, hasActiveErrors) {
      const data = getLastKnownData(vehicleId);
      
      return {
        ...data,
        isStale: hasActiveErrors,
        staleSince: getLastSuccessfulFetch(vehicleId),
        errorMessage: 'Unable to retrieve current data. Showing last known values.'
      };
    }
    ```
  </Accordion>
</AccordionGroup>

***

## Error Resolution Tracking

When an error condition is resolved, Smartcar sends a `VEHICLE_ERROR` event with `state: "RESOLVED"`:

```javascript  theme={null}
function handleErrorResolution(payload) {
  const { vehicleId, data } = payload;
  
  data.errors.forEach(error => {
    if (error.state === 'RESOLVED') {
      console.log(`Error resolved for ${vehicleId}: ${error.code}`);
      
      // Clear error flags
      clearVehicleError(vehicleId, error.code);
      
      // Resume data collection
      resumeDataCollection(vehicleId, error.signals);
      
      // Notify user
      notifyUser(vehicleId, 'Your vehicle is now connected and data is available');
    }
  });
}
```

<Tip>
  **Automatic recovery**: Use `state: "RESOLVED"` events to automatically resume normal operations without manual intervention.
</Tip>

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Error Reference" icon="circle-exclamation" href="/errors/api-errors">
    Complete error code documentation
  </Card>

  <Card title="VEHICLE_STATE Event" icon="car" href="/api-reference/webhooks/events/vehicle-state">
    Learn about successful signal deliveries
  </Card>

  <Card title="Reliability Best Practices" icon="shield" href="/integrations/webhooks/best-practices/reliability">
    Implement idempotency and retry handling
  </Card>

  <Card title="Delivery Behavior" icon="truck-fast" href="/api-reference/webhooks/delivery-behavior">
    Understand retry policies
  </Card>
</CardGroup>
