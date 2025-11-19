# Source: https://infisical.com/docs/documentation/platform/event-subscriptions.md

# Event Subscriptions

> Subscribe to events in Infisical for real-time updates

<Info>
  **Note:** Event Subscriptions is a paid feature. - **Infisical Cloud users:** Event Subscriptions is available under
  the **Enterprise Tier**. - **Self-Hosted Infisical:** Please contact [sales@infisical.com](mailto:sales@infisical.com)
  to purchase an enterprise license.
</Info>

Event Subscriptions in Infisical allow you to receive real-time notifications when specific actions occur within your account or organization. These notifications include changes to secrets, users, teams, and many more **coming soon**.

## How It Works

* Server receives message over pubsub connection indicating changes have occurred
* Server processes the change notification
* Updated data is synchronized across all connected Infisical instances
* Client applications receive real-time updates through [Server-Sent Events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
* All servers maintain consistent state without manual intervention

This ensures your infrastructure stays up-to-date automatically, without requiring restarts or manual synchronization.

<Note>
  Event Subscriptions are designed for real-time communication and do not include persistence or replay
  capabilities—events are delivered once and are not stored for future retrieval.
</Note>

## Supported Resources

You can currently subscribe to notifications for the following resources and event types:

* **Secrets**
  * `secret:created`: Triggered when a secret is created
  * `secret:updated`: Triggered when a secret is updated
  * `secret:deleted`: Triggered when a secret is deleted

## Permissions Setup

To receive events on a supported resource, the identity must have `Subscribe` action permission on that resource.

Follow these steps to set up the necessary permissions:

<Steps>
  <Step title="Select a project and copy the Project ID">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/select-project.png" alt="Select Project" />

    On your project page, open **Project Settings** from the sidebar.

    In the Project name section, click **Copy Project ID** to copy your Project ID, or extract it from the URL:
    `https://app.infisical.com/project/<your_project_id>/settings`
  </Step>

  <Step title="Navigate to Access Management and open Project Roles">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/project-detail.png" alt="Project Detail" /> <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/project-access.png" alt="Project
    Access" /> Navigate to **Access Management**, then select **Project Roles**.
  </Step>

  <Step title="Select an existing role or create a new one">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/project-role.png" alt="Project Role" /> You can either edit an existing role or create a new role
    for event subscriptions.
  </Step>

  <Step title="Assign policies to the role">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/role-detail.png" alt="Role Detail" /> Select the specific resources that the role should have access
    to. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/add-policy.png" alt="Add policy" />
  </Step>

  <Step title="Enable the Subscribe action in permissions">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/policy-setting.png" alt="Policy setting" />

    Ensure the **Subscribe** action is selected for the relevant resources and events.

    ## Conditions

    By default, the role will have access to all events for the selected resources in this project.

    <AccordionGroup>
      <Accordion title="Full Access">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/access-full.png" alt="Policy setting" />
      </Accordion>

      <Accordion title="Path Prefix">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/access-path.png" alt="Policy setting" />
      </Accordion>

      <Accordion title="Environment">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/access-dev.png" alt="Policy setting" />
      </Accordion>
    </AccordionGroup>
  </Step>
</Steps>

## Getting Started

Currently, events are only available via [API](/api-reference/endpoints/events) but will soon be available in our SDKs, Kubernetes Operator, and more.

### API Usage

You need an auth token to use this API. To get an authentication token, follow the authentication guide for one of our supported auth methods from the [machine identities documentation](/documentation/platform/identities/machine-identities#authentication-methods).

#### Creating a Subscription

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/postman-subscribe.png" alt="Postman Subscription" />

**Request Parameters:**

* `projectId`: Project whose events you want to subscribe to
* `register`: List of event filters
  * `conditions`: Conditions to filter events on
    * `environmentSlug`: Project environment
    * `secretPath`: Path of the secrets

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/events/postman-sse-response.png" alt="Postman Subscription Response" />

The subscribe endpoint responds with a `text/event-stream` content type to initiate SSE streaming.

For more specific details, please refer to our [API Reference](/api-reference/endpoints/events).
