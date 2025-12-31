# Source: https://smartcar.com/docs/connect/re-auth/oem-migrations.md

# OEM Migrations and Re-authentication

> Understanding when and why vehicle owners need to re-authenticate due to OEM infrastructure changes and migrations.

## Overview

As automakers evolve their connected services infrastructure, Smartcar occasionally needs to migrate integrations to newer OEM APIs or authentication systems. These migrations ensure your application maintains access to the latest features, improved reliability, and continued compatibility with OEM platforms. Smartcar does this work on your behalf to minimize disruption.

**Important**: Some OEM migrations will require vehicle owners to re-authenticate through Smartcar Connect. This is a necessary step to maintain secure access to vehicle data.

<Warning>
  Re-authentication requirements are an inevitable part of working with automotive APIs. Ensuring your application can gracefully manage [re-atuthentication](/connect/re-auth/redirect-to-connect) will help minimize disruption to your users.
</Warning>

## When Re-authentication Is Required

Vehicle owners may need to re-authenticate in several scenarios:

### Common Scenarios

Re-authentication may be required when:

* Vehicle owners change their OEM account credentials
* Connected services subscriptions are renewed or modified
* Vehicle owners revoke and re-grant access through OEM portals

### OEM Infrastructure Changes

When an automaker upgrades their API infrastructure or releases a new connected services platform, existing connections may need to be re-established. Examples include:

* **New APIs**: When OEMs annouce a new API platform for third-parties requiring all connected vehicles to re-authenticate
* **OEM Platform Updates**: When OEMs periodically update their authentication systems invalidating existing tokens forcing re-authentication
* **OEM Migrations**: When accounts or platforms are migrated between regions or systems deprecating legacy platforms

## Migration Communication

When a migration requiring re-authentication is necessary, Smartcar will:

1. **Notify you in advance** via email and your dedicated Slack channel
2. **Provide migration timelines** so you can plan communications with your users
3. **Offer technical support** throughout the migration process
4. **Provide documentation** outlining required actions (if any)

## Implementation Best Practices

### Plan for Re-authentication

Build your application with the expectation that re-authentication will be needed:

```javascript  theme={null}
// Example: Handle authentication errors gracefully
try {
  const response = await vehicle.odometer();
} catch (error) {
  if (error.type === 'AUTHENTICATION' || 
      error.statusCode === 'CONNECTED_SERVICES_ACCOUNT:AUTHENTICATION_FAILED') {
    // Prompt user to re-authenticate
    const reauthUrl = error.resolution?.url;
    redirectToReauth(reauthUrl);
  }
}
```

### Monitor for Authentication Errors

Watch for authentication-related errors in your API responses:

* `AUTHENTICATION_FAILED`: Indicates credentials are invalid or expired
* `PERMISSION` errors: May require permission updates through re-authentication
* API errors with `resolution.url`: Often include a pre-built re-authentication URL

See our [error documentation](/errors/api-errors/connected-services-account-errors) for complete details.

### Use Webhooks for Proactive Detection

Subscribe to [webhooks](/integrations/webhooks/overview) to detect authentication issues before users report them:

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
        "type": "CONNECTED_SERVICES_ACCOUNT",
        "code": "AUTHENTICATION_FAILED",
        "description": "Smartcar was unable to authenticate with the user’s connected services account. Please prompt the user to re-authenticate using Smartcar Connect.",
        "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#authentication-failed",
        "statusCode": 400,
        "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
        "resolution": {
          "type": "REAUTHENTICATE",
          "url": "https://connect.smartcar.com/oauth/reauthenticate?response_type=vehicle_id&client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07&vehicle_id=sc4a1b01e5-0497-417c-a30e-6df6ba33ba46"
        },
        "suggestedUserMessage": "Your car got disconnected from <app name>. Please use this link to re-connect your car: <link to Smartcar Connect>."
      }
    ]
  },
  "meta": {
    "version": "4.0",
    "deliveryId": "48b25f8f-9fea-42e1-9085-81043682cbb8",
    "deliveredAt": 1761896351529,
    "webhookId": "123e4567-e89b-12d3-a456-426614174000",
    "webhookName": "Your Webhook's Name",
    "mode": "LIVE"
  }
}
```

### Implement Streamlined Re-authentication

Use Smartcar's [re-authentication flow](/connect/re-auth/redirect-to-connect) to make the process seamless:

* Pre-populate the vehicle ID to skip vehicle selection
* Use the error's `resolution.url` field when available
* Provide clear messaging about why re-authentication is needed

### Communicate Proactively

When a migration is announced:

1. **Email users ahead of time** explaining the need and benefits
2. **Show in-app notifications** with clear calls-to-action
3. **Provide support resources** for users who have questions
4. **Track re-authentication completion** to follow up with users who haven't completed the process

### Example User Communication

<Accordion title="Sample email template">
  **Subject**: Action Required: Reconnect Your \[Vehicle Make] to \[Your App Name]

  Hi \[User Name],

  \[Your App Name] lost connection to your \[Vehicle Make]. Your action is needed to continue receiving \[Your app's benefits].

  **Why is this needed?**
  Connections to \[Vehicle Make] may expire from time to time. To maintain secure access to your vehicle data, you need to reconnect your vehicle.

  **What you need to do:**

  1. Click the button below to reconnect your vehicle
  2. Log in with your \[Vehicle Make] account credentials
  3. Approve the connection

  \[Reconnect My Vehicle Button]

  This process takes less than a minute. Your vehicle data and preferences will not be affected.

  If you have questions, reply to this email or contact our support team.

  Thank you,
  The \[Your App Name] Team
</Accordion>

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Will all OEM migrations require re-authentication?">
    No. Smartcar handles many OEM updates transparently without requiring user action. Re-authentication is only required when the changes are not compatible with the current integration. Smartcar does its best to minimize re-authentication related to OEM platform changes.
  </Accordion>

  <Accordion title="How much notice will we receive for migrations?">
    Smartcar provides advance notice for planned migrations, typically several weeks to months depending on the scope. In rare cases where OEMs make unexpected changes, we'll communicate as soon as possible.
  </Accordion>

  <Accordion title="What happens if users don't re-authenticate?">
    API requests will continue to fail with authentication errors until re-authentication is completed. The vehicle connection will remain in your system, but no data can be retrieved.
  </Accordion>

  <Accordion title="Can we force re-authentication for all users at once?">
    Yes. The sooner re-authentication occurs, the sooner you and your users can leverage new features or resolve downtime.
  </Accordion>

  <Accordion title="Will access tokens and refresh tokens change?">
    This depends on the migration. In some cases, existing connections will remain valid. In other cases, existing tokens will expire and re-authentication is required to resolve re-establish a connection. Smartcar will specify this in migration communication.
  </Accordion>
</AccordionGroup>

## Need Help?

If you have questions about an upcoming migration or need assistance implementing re-authentication flows:

* Contact [support@smartcar.com](mailto:support@smartcar.com)
* Visit our [Support Center](/help/accessing-support-center)
* Check the [Changelog](/changelog/latest) for migration announcements

<Note>
  For enterprise customers, coordinate Tesla tenant setup and other OEM-specific configurations with your Solutions Architect before going live with customer-facing vehicles.
</Note>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://smartcar.com/docs/llms.txt