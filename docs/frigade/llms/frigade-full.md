# Frigade Documentation

Source: https://docs.frigade.com/llms-full.txt

---

# API Authorization
Source: https://docs.frigade.com/api-reference/authorization



The Frigade API is secured using authorization tokens.
These api keys are used to authenticate your requests to the API. You can create and manage your api keys in the [Frigade Dashboard](https://app.frigade.com/developer).

Frigade provides two scopes of API keys: public and private. Below, we describe the differences between the two.

## Public API keys

This key can be exposed publicly (i.e. in your frontend code) and is used to access the public API endpoints.
These endpoints are prefixed with the `public` namespace in the API url (e.g. `https://api.frigade.com/v1/public/flows`).

## Private API keys

This key should be kept secret and is used to access the private API endpoints. It can be used to both access public and private API endpoints.

## Sample API request

The key should be passed in the `Authorization: Bearer <key>` header.
For example, to access the list of available flows in your account, you would make the following request:

```bash  theme={"system"}
curl -i -X GET \
   -H "Authorization:Bearer api_public_J3FNG3dJASDKLW98SN4KLOJHNTYUFGNVSK" \
 'https://api.frigade.com/v1/public/flows'
```


# Get User Flow State
Source: https://docs.frigade.com/api-reference/flows/flow-states-get

get /v1/public/flowStates
Get the state of a User in all Flows



# Update User Flow State
Source: https://docs.frigade.com/api-reference/flows/flow-states-post

post /v1/public/flowStates
Updates the user's state in a single Flow



# Delete Flow
Source: https://docs.frigade.com/api-reference/flows/flows-delete

delete /v1/flows/{numericFlowId}
Delete a Flow

Deleting a Flow will remove all the data associated with it, including the Flow itself, its responses, and any other related data. This operation is irreversible.

<Warning>Only call this endpoint from your backend code.</Warning>

### Obtaining the numeric ID of a Flow

To obtain the numeric ID of a Flow, you should make a [GET request](/api-reference/flows/flows-get) to get the Flow you are looking to change. The numeric ID is a number and is different from the slug (e.g. `flow_GzXC2fHz`). The reason for this is that different [versions](/platform/versioning) of the Flow share the same slug but have different numeric IDs to differentiate them.


# Get a Flow
Source: https://docs.frigade.com/api-reference/flows/flows-get

get /v1/public/flows/{slug}
Get a single Flow by its Flow ID/slug.



# Update Flow
Source: https://docs.frigade.com/api-reference/flows/flows-put

put /v1/flows/{numericFlowId}
Update a Flow's configuration and metadata

As this endpoint modifies data, you will need to use the [private API key](/api-reference/authorization).

<Warning>Only call this endpoint from your backend code.</Warning>

### Obtaining the numeric ID of a Flow

To obtain the numeric ID of a Flow, you should make a [GET request](/api-reference/flows/flows-get) to get the Flow you are looking to change. The numeric ID is a number and is different from the slug (e.g. `flow_GzXC2fHz`). The reason for this is that different [versions](/platform/versioning) of the Flow share the same slug but have different numeric IDs to differentiate them.


# Get all Flows
Source: https://docs.frigade.com/api-reference/flows/overview

get /v1/public/flows
Get all Flows for your organization.



# Delete a Group
Source: https://docs.frigade.com/api-reference/groups/groups-delete

delete /v1/groups



# Find a Group
Source: https://docs.frigade.com/api-reference/groups/groups-get

get /v1/groups
Find a group by ID



# Create a Group
Source: https://docs.frigade.com/api-reference/groups/overview

post /v1/public/groups

This endpoint allows you to upsert new or existing Groups. If the group already exists, it will be updated with the new data.
Any property left unchanged will not be modified. Changes to tracking events are append-only.


# Create or update a User
Source: https://docs.frigade.com/api-reference/users/overview

post /v1/public/users
Create a user, add properties, and tracking events

This endpoint allows you to upsert new or existing Users. If the user already exists, it will be updated with the new data.
Any property left unchanged will not be modified. Changes to tracking events are append-only.


# Delete a User
Source: https://docs.frigade.com/api-reference/users/users-delete

delete /v1/users



# Find a User
Source: https://docs.frigade.com/api-reference/users/users-get

get /v1/users
Find a user by ID



# Webhooks
Source: https://docs.frigade.com/api-reference/webhooks



Webhooks allow you to receive notifications from Frigade when certain events occur.
You can use webhooks to receive notifications about your users when they start a Flow and as they progress through it.

## Creating a webhook

To add a new webhook, open the **Developer** page from the left sidebar, pick the **Webhooks** tab and click the "New webhook" button.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/webhooks.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f8b3b7e5dbf1d0b133c3e0a0787309bc" data-og-width="1399" width="1399" data-og-height="835" height="835" data-path="images/platform/webhooks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/webhooks.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=38e3d45ef2decfaadf6f40a618f5ed46 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/webhooks.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=daf73ded7c324f9ce557f4debdb1f7aa 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/webhooks.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8b7811f8060afe7d32b07efc5fc9b5c6 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/webhooks.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a12a11b1e1a9250ad50daea4978f758d 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/webhooks.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b106460424f04cb8976ada82addcaff5 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/webhooks.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c1f68f6715a84281bc1953bce373c776 2500w" />
</Frame>

## Supported events

The following events are currently supported:

<ParamField body="flowResponse.startedFlow">When a user starts a Flow</ParamField>
<ParamField body="flowResponse.completedFlow">When a user completes a Flow</ParamField>
<ParamField body="flowResponse.skippedFlow">When a user dismisses/skips a Flow</ParamField>
<ParamField body="flowResponse.startedStep">When a user starts a Step in a Flow</ParamField>
<ParamField body="flowResponse.completedStep">When a user completes a Step in a Flow</ParamField>

## Webhook payload

The payload of the message includes the type of the event in the `type` property.

The data property contains the actual payload sent by Frigade.
The payload can be a different object depending on the event type.

### Schema

```typescript  theme={"system"}
{
  // Event type identifier
  type: string;  // e.g. "flowResponse.completedFlow"
  
  // Timestamp when the event occurred (ISO 8601)
  time: string;  // e.g. "2024-08-21T16:31:36.207Z"
  
  // Request timeout in milliseconds
  timeout: number;

  // User information
  user: {
    // The user id in your system. This will match the `foreignUserId` field in the data object.
    id: string;
    // The name of the user
    name: string;
    // The email of the user
    email: string | null;
  };

  // Flow information
  flow: {
    // Flow ID, for example: flow_8Lq7hAqA
    id: string;

    // Flow name, for example: "NPS Survey"
    name: string;
  };

  // Detailed response data
  data: {
    // Step-specific data, keyed by stepId
    [stepId: string]: {
      [fieldName: string]: any;
    };

    // Response ID
    id: string;

    // Flow ID
    flowId: string;

    // Flow slug
    flowSlug: string;

    // Numeric Frigade user ID
    userId: number;

    // Frigade user slug
    userSlug: string;

    // Action type: COMPLETED_FLOW, SKIPPED_FLOW, COMPLETED_STEP, SKIPPED_STEP
    actionType: string;

    // Step ID
    stepId: string;

    // ISO 8601 timestamp
    createdAt: string;

    // Foreign user ID. This will match your own internal user ID provided to Frigade.
    foreignUserId: string;

    // Whether the flow is blocked
    blocked: boolean;

    // Whether the flow is hidden
    hidden: boolean;

    // Additional data collected, such as form data in a stringified JSON object.
    data: string;
  };
}
```

The below example shows the payload for a `flowResponse.completedFlow` event for the [NPS Survey](/component/survey/nps) component with flattened data fields:

```json  theme={"system"}
{
  "timeout": 1000,
  "data__nps-feedback-page__nps-feedback-text": "I love the service!",
  "data__nps-score-page__nps-score": 10,
  "data__id": "flowResponse_uPzbTOayngU00Vzc",
  "data__flowId": "flow_8Lq7hAqA",
  "data__flowSlug": "flow_8Lq7hAqA",
  "data__userId": 53526,
  "data__userSlug": "user_qnsDyTeZxP2sl12Q",
  "data__actionType": "COMPLETED_FLOW",
  "data__data": "{}",
  "data__stepId": "nps-feedback-page",
  "data__blocked": false,
  "data__hidden": false,
  "user__name": "",
  "user__email": null,
  "user__id": "abcdefgh",
  "flow__id": "flow_8Lq7hAqA",
  "flow__name": "NPS Survey",
  "type": "flowResponse.completedFlow",
  "data": {
    "nps-feedback-page": {
      "nps-feedback-text": "I love the service!"
    },
    "nps-score-page": {
      "nps-score": 10
    },
    "id": "flowResponse_uPzbTOayngU00Vzc",
    "flowId": "flow_8Lq7hAqA",
    "flowSlug": "flow_8Lq7hAqA",
    "userId": 53526,
    "userSlug": "user_qnsDyTeZxP2sl12Q",
    "actionType": "COMPLETED_FLOW",
    "data": "{}",
    "stepId": "nps-feedback-page",
    "createdAt": "2024-08-21T16:31:36.187Z",
    "foreignUserId": "abcdefgh",
    "blocked": false,
    "hidden": false
  },
  "time": "2024-08-21T16:31:36.207Z",
  "user": {
    "name": "",
    "email": null,
    "id": "abcdefgh"
  },
  "flow": {
    "id": "flow_8Lq7hAqA",
    "name": "NPS Survey"
  }
}
```

## Verifying webhooks

When you create a webhook, Frigade will generate a secret key for you. You can use this key to verify that the webhook is coming from Frigade.

<Note>
  If you don't verify the request, your app will be susceptible to a number of attacks since your webhook endpoint is open to the public.
</Note>

To verify the request, you need to calculate the HMAC SHA256 digest of the JSON-encoded `data` field using the secret key as the key and compare it to the value in the `X-Webhook-Signature` header. The signature is base64 encoded.
Note that when JSON-encoding the `data` field it needs to match the order of the keys in the payload and not contain any whitespace between the keys and values.

For example, in Node.js, you can do it like this:

```ts  theme={"system"}
const crypto = require('crypto');

const payload = '{"type":"flowResponse.completedStep",....}}'
const secret = 'my-secret' // Find this in the webhook settings in the Frigade dashboard
function verifySignature(secret, payload) {
  const hmac = crypto.createHmac('sha256', secret);
  hmac.update(Buffer.from(payload, 'utf-8'));
  const digest = hmac.digest('base64');
  return digest;
}

const signature = verifySignature(secret, payload);

if (signature !== payload.signature) {
  throw new Error('Invalid signature');
}
```

## Verifying timestamps

The `time` field in the payload is the time when the event occurred. You can use this field to verify that the request is not a [replay attack](https://en.wikipedia.org/wiki/Replay_attack) by ignoring older events.

## Retrying failed requests

Frigade will retry failed requests up to 5 times with an exponential backoff strategy.

## Common fields

The following fields are available in all Frigade webhooks (shown in flattened format):

* `flow__id`: The ID of the Flow that triggered the webhook
* `flow__name`: The name of the Flow that triggered the webhook
* `user__id`: The ID of the user that triggered the webhook
* `user__name`: The name of the user that triggered the webhook (if available)
* `user__email`: The email of the user that triggered the webhook (if available)


# Announcement
Source: https://docs.frigade.com/component/announcement

Communicate information or drive action via modal-based announcements

<Frame className="h-96 items-center px-4">
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1feb6c3c3162ad5dcfb671cee05b2720"
    style={{
    width: "350px",
  }}
    data-og-width="470"
    width="470"
    data-og-height="533"
    height="533"
    data-path="images/components/announcement.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=fa0489f75065c31f350c1bae87fb694d 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9c312391ce3bead7af2a56d8091fba32 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=160d89e44ac348fcd7acda99c3c72fd1 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=aecd9e5384c9c04f4d4088a4e118c861 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1d46eb5279067aa5749f69eca67d26e7 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=d2621dab38c40ab54856d4019ca57730 2500w"
  />
</Frame>

## About this component

The `Announcement` component is a flexible communication tool that’s perfect for sharing important information or driving user action. They’re especially effective for getting the word out about new feature launches, upcoming webinars, or welcoming users to new areas of your product.

**When to Use Announcements:**

* **Key Communications:** Use announcements to highlight significant updates or events that need immediate user attention.
* **Transactional Flows:** They’re also great for welcoming users or guiding them to explore new features, like kicking off a product tour.

**Advantages of Announcements:**

* **Grab Attention:** Announcements often interrupt workflows in a way that demands attention, making sure users don’t miss out on important info.
* **Visual Impact:** You have ample space for visual assets (videos, images, GIF), which can help draw users in and keep the message engaging.

**Best Practices for Effective Announcements:**

* **Limit Frequency:** To avoid overwhelming users, try to keep announcements to once a session per user, and ideally once a week. This helps maintain their impact and prevents the dreaded “wack-a-mole” effect.
* **Be Concise:** Keep your messages short and to the point. The easier they are to digest, the more likely users will engage with them.
* **Target Your Audience:** Make sure your announcements are relevant and reach the right people by targeting on user properties, events and other signals.
* **Clear Calls to Action:** Use actionable phrases like “Learn more” and direct links over passive language like "Got it" or "Okay".
* **Utilize Collections:** Use Frigade Collections to manage in-app UI channels effectively, ensuring that only one announcement is displayed at a time.
* **Less Critical Info:** For non-essential information, consider launching announcements in the corner of the screen without background blurs for a subtler touchpoint.

## Resources

* [Launch announcements](/platform/collections#launch-with-collections) in minutes with no-code via Collections
* Target your announcement to specific users with [Targeting](/platform/targeting)

## Demo

* See announcements in action in our [live demo](https://demo.frigade.com/modals)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Announcement flowId="my-flow-id" />
      );
    };

    ```
  </Tab>

  <Tab title="No-code">
    Announcements can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```

      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Register the Flow as a modal to prevent popup collisions (only one modal Flow will render at a time).
    </ParamField>

    <ParamField body="onCloseAutoFocus" type="(event: Event) => void">
      Event handler called when auto-focusing on close.
      Can be prevented.
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onEscapeKeyDown" type="(event: KeyboardEvent) => void">
      Event handler called when the escape key is down.
      Can be prevented.
    </ParamField>

    <ParamField body="onInteractOutside" type="(event: PointerDownOutsideEvent , FocusOutsideEvent) => void">
      Event handler called when an interaction happens outside the `DismissableLayer`.
      Specifically, when a `pointerdown` event happens outside or focus moves outside of it.
      Can be prevented.
    </ParamField>

    <ParamField body="onOpenAutoFocus" type="(event: Event) => void">
      Event handler called when auto-focusing on open.
      Can be prevented.
    </ParamField>

    <ParamField body="onOpenChange" type="(open: boolean) => void" />

    <ParamField body="onPointerDownOutside" type="(event: PointerDownOutsideEvent) => void">
      Event handler called when the a `pointerdown` event happens outside of the `DismissableLayer`.
      Can be prevented.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="steps" type="array">
      The individual steps/pages of the announcement
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>
  </Tab>
</Tabs>


# Banner
Source: https://docs.frigade.com/component/banner

Communicate information or drive action via in-line banners

<Frame className="h-96 items-center px-4">
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=85007c7bf1c50af98cb76411ff1256e3"
    style={{
    height: "auto",
  }}
    data-og-width="1000"
    width="1000"
    data-og-height="100"
    height="100"
    data-path="images/components/banner.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=28087310105f6277a14b4ef167423363 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b02de011f0cd469ccf6a2eb7304f7f8f 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b77009cb787e78dfdaad5f49c0f31b21 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=691706e4786fb88c6539c6f2b734ce62 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=4e5781f625009647b9da7edfab7f40bc 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=01e0b610a723d20c9b46e130fe01da0e 2500w"
  />
</Frame>

## About this component

The `Banner` component is a versatile, persistent UI component that typically span the full width of a page or container, often at the top or bottom of the page. They serve as an unobtrusive way to communicate important information and promote additional offerings without disrupting the user’s workflow.

**When to use Banners:**

* **Alerts:** Ideal for notifying users about critical updates, such as free trial expirations or scheduled maintenance.
* **Lightweight Up-sells:** Effective for promoting related products or features, banners can be strategically targted and placed next to relevant content.

**Advantages of Banners:**

* **Non-Disruptive Communication:** Since banners remain visible without interrupting the user experience, they allow users to continue their tasks while still being informed.
* **Flexible Design Options:** Banners can be customized with full-bleed graphics and images, making them visually appealing and engaging. Frigade supports custom components including on-brand, eye-catching banners.

**Best Practices for Banners:**

* **Use Collections:** Leverage Collections to define reusable in-app UI channels, enabling teams to efficiently manage and launch banners across different pages, such as your product dashboard or a specific product pages.
* **Regulate Frequency:** Control the frequency of banner displays to ensure they remain relevant and engaging without overwhelming users.
* **Make Dismissible:** Most often, banners are easily dismissible for the best user expeirence. In select cases, banners may be non-dismissible to communicate a critical message for some time (e.g. product downtime).

## Resources

* Launch banners with no-code using custom [Collections](/platform/collections#inline-ui-components)
* Target your banner to specific users with [Targeting](/platform/targeting)
* See [industry examples](https://www.productonboarding.com/?type=banner) of banners

## Demo

* See banners in action in our [live demo](https://demo.frigade.com/cards)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Banner flowId="my-flow-id" />
      );
    };
    ```
  </Tab>

  <Tab title="No-code">
    Banners can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```
      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Register the Flow as a modal to prevent popup collisions (only one modal Flow will render at a time).
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="steps" type="array">
      The steps to show in the tooltip tour.
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>
  </Tab>
</Tabs>


# Carousel
Source: https://docs.frigade.com/component/checklist/carousel

A carousel checklist component to drive set up and activation

<Frame className="h-96 items-center">
  <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/carousel.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=2c69f824b91721872a6b30049c74a211" style={{ maxWidth: "500px" }} data-og-width="1120" width="1120" data-og-height="457" height="457" data-path="images/components/carousel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/carousel.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=8e2941d443ba516af0485df0dad35e50 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/carousel.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=2f131d0a29fdfac56ebba97bc391e40e 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/carousel.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=2764535aacc1e418dd889818b7b37e51 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/carousel.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=37dea889e948ffd22b663de455618f78 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/carousel.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=494a483dc72fabe5ca32888966c2d980 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/carousel.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b0662747758ba7d4e6d724f40e0e283b 2500w" />
</Frame>

## About this component

The `Checklist` component is one of Frigade’s most popular tools, especially for user onboarding and activation. They’re super handy for guiding users through their journey, whether it’s at the start of their experience or when they’re setting up a new product vertical or a complex feature.

**When to Use Checklists:**

* **Onboarding and Activation:** Checklists are perfect for helping users get started and ensuring they complete essential tasks. They provide a clear path forward and help users feel more confident as they navigate your product.

**Advantages of Announcements::**

* **Two Default Versions:** Frigade offers two out-of-the-box checklist formats—carousel and collapsible—so you can choose what fits best for your users. Plus, if you need something custom, you can easily build one using the Frigade SDK/API.
* **Deeply integrated:** The most effective checklists measure actual in-product results. Frigade makes it easy to connect checklist steps to automatically complete from actual in-product actions and milestones.

**Best Practices for Checklists:**

* **Limit the Number of Tasks:** Keep your checklists manageable. Too many tasks can overwhelm users, so aim for a concise list that’s easy to follow.
* **Pre-Complete Steps Where Applicable:** For example, marking “Set up account” complete after sign up can show users progress from the start and create a sense of momentum (like showing 20% done instead of 0%).
* **Avoid Basic “Mark Done” Steps:** Whenever possible, tie checklist steps to actual workflows and tasks. Deep linking users to complete actions is way more effective. It’s okay to have “Skip” or “Mark done” as secondary options for non-essential steps.
* **Include a CTA to Hide the Checklist:** Giving users the option to hide the checklist can help them feel more in control of their setup and UI.
* **Break Large Workflows into Smaller Segments:** If you have a hefty checklist (like 12 steps), consider phasing it and breaking it into smaller groups (like two groups of 6). This makes it feel less daunting.
* **Measure Completion Rates:** Keep track of how users are progressing through each step and the entire checklist. This data can help you identify areas for improvement for future iterations.

## Resources

* Target your checklist to specific users with [Targeting](/platform/targeting)
* [Dynamically mark a step complete](/sdk/advanced/completing-a-step#programmatically-marking-steps-complete)
* Create shared checklists using [Group Properties](/sdk/hooks/group) and [completion criteria](/sdk/advanced/completing-a-step#automatically-marking-steps-complete)
* See [industry examples](https://www.productonboarding.com/?type=checklist) of checklists

## Demo

* See checklists in action in our [live demo](https://demo.frigade.com/checklists)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Checklist.Carousel flowId="my-flow-id" />
      );
    };
    ```
  </Tab>

  <Tab title="No-code">
    Checklists can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```
      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Register the Flow as a modal to prevent popup collisions (only one modal Flow will render at a time).
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="sort" type="'completed-last' , 'default'">
      How to sort the default the completed steps of the carousel.

      * `completed-last` will sort the completed/skips steps to the end of the carousel.
      * `default` will keep the order of the steps as they are in the flow.
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="sequential" type="boolean">
      If true, all steps must be completed in order. This means that the next step will be disabled until the current step is completed. Default behavior is `false`.
    </ParamField>

    <ParamField body="steps" type="array">
      The steps to show in the checklist flow.
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>
  </Tab>
</Tabs>


# Collapsible
Source: https://docs.frigade.com/component/checklist/collapsible

A condensed checklist component that can be used inline or in a modal

<Frame className="h-120 items-center px-4">
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/collapsible.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=06f4d1092cd12b7d2c1d515c67a18562"
    style={{
    width: "350px",
  }}
    data-og-width="540"
    width="540"
    data-og-height="825"
    height="825"
    data-path="images/components/collapsible.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/collapsible.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=acf8c16ec6af5c259834016167f85680 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/collapsible.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1600ecd0eb31341dfe2ac87ed69be884 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/collapsible.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=e40640c171b27daa749085b0cef825e2 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/collapsible.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=60b2cb6f5848c4425646d62e80ae657e 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/collapsible.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=41ae7d2ace378d3721a587f4299db909 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/collapsible.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=94a1ea62d1af4114d43118ac00bddb74 2500w"
  />
</Frame>

## About this component

The `Checklist` component is one of Frigade’s most popular tools, especially for user onboarding and activation. They’re super handy for guiding users through their journey, whether it’s at the start of their experience or when they’re setting up a new product vertical or a complex feature.

**When to Use Checklists:**

* **Onboarding and Activation:** Checklists are perfect for helping users get started and ensuring they complete essential tasks. They provide a clear path forward and help users feel more confident as they navigate your product.

**Advantages of Announcements::**

* **Two Default Versions:** Frigade offers two out-of-the-box checklist formats—carousel and collapsible—so you can choose what fits best for your users. Plus, if you need something custom, you can easily build one using the Frigade SDK/API.
* **Deeply integrated:** The most effective checklists measure actual in-product results. Frigade makes it easy to connect checklist steps to automatically complete from actual in-product actions and milestones.

**Best Practices for Checklists:**

* **Limit the Number of Tasks:** Keep your checklists manageable. Too many tasks can overwhelm users, so aim for a concise list that’s easy to follow.
* **Pre-Complete Steps Where Applicable:** For example, marking “Set up account” complete after sign up can show users progress from the start and create a sense of momentum (like showing 20% done instead of 0%).
* **Avoid Basic “Mark Done” Steps:** Whenever possible, tie checklist steps to actual workflows and tasks. Deep linking users to complete actions is way more effective. It’s okay to have “Skip” or “Mark done” as secondary options for non-essential steps.
* **Include a CTA to Hide the Checklist:** Giving users the option to hide the checklist can help them feel more in control of their setup and UI.
* **Break Large Workflows into Smaller Segments:** If you have a hefty checklist (like 12 steps), consider phasing it and breaking it into smaller groups (like two groups of 6). This makes it feel less daunting.
* **Measure Completion Rates:** Keep track of how users are progressing through each step and the entire checklist. This data can help you identify areas for improvement for future iterations.

## Resources

* Target your checklist to specific users with [Targeting](/platform/targeting)
* [Dynamically mark a step complete](/sdk/advanced/completing-a-step#programmatically-marking-steps-complete)
* Create shared checklists using [Group Properties](/sdk/hooks/group) and [completion criteria](/sdk/advanced/completing-a-step#automatically-marking-steps-complete)
* See [industry examples](https://www.productonboarding.com/?type=checklist) of checklists

## Demo

* See checklists in action in our [live demo](https://demo.frigade.com/checklists)

## Code

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Checklist.Collapsible flowId="my-flow-id" />
      );
    };

    ```
  </Tab>

  <Tab title="No-code">
    Checklists can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```

      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Register the Flow as a modal to prevent popup collisions (only one modal Flow will render at a time).
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="stepTypes" type="StepTypes">
      Map of step types to their respective components.
      Use this to build custom step components. The `type` defined on the step in the Flow YAML config should match the key in this object.
      For instance, if you have a step with `type: 'custom'`, you should provide a component for it like so:

      ```
      <Checklist.Collapsible stepTypes={{ custom: CustomStepComponent }} />
      ```

      The corresponding YAML config would look like:

      ```
      steps:
       - id: custom-step
         type: custom
      ```
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="sequential" type="boolean">
      If true, all steps must be completed in order. This means that the next step will be disabled until the current step is completed. Default behavior is `false`.
    </ParamField>

    <ParamField body="steps" type="array">
      The steps to show in the checklist flow.
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>
  </Tab>
</Tabs>


# Form
Source: https://docs.frigade.com/component/form

Collect user information via forms in modals or embedded in your UI

<Frame>
  <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/forms-modal.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=c8f7d424a24f984f0aa6e582909a2f5d" style={{ width: "350px" }} data-og-width="888" width="888" data-og-height="1644" height="1644" data-path="images/forms-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/forms-modal.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=61d54441deeb533c44b1f2ed7fb4e2cc 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/forms-modal.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=709ba0bf8d422dc45a469e99adf3276f 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/forms-modal.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=0cb6bd6470bc35ec8ae7d3c5e67c44a4 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/forms-modal.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=8b1221dace25f39042c234fa99c3079d 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/forms-modal.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=fe36dd52abac76dc4eeb4f930be6161a 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/forms-modal.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=c89ee13767cd132c0da128f5cb915ee5 2500w" />
</Frame>

## About this component

The `Form` component is a super versatile tool that can fit right into your product UI or pop up in a modal for things like surveys. They can be used for wide range of use cases including registration flows, surveys, feedback forms, and more. The component supports form validation (client and server-side), conditional fields, branching logic, and multi-step Flows.

**When to Use Forms:**

* **Embedded in UI:** Forms work great for tasks like product registration, helping users get started smoothly without leaving the page.
* **Modal Surveys:** Use forms in modals for surveys or feedback, making it easy for users to share their thoughts without disrupting their experience.

**Why Forms Are Powerful:**

* **Conditional and Branching Logic:** Forms can adapt based on user responses, guiding them through a tailored experience that feels intuitive.
* **Custom React Steps:** You can embed custom React components to invite teammates or perform API lookups, adding a personal touch to your forms.
* **Customizable Input Types:** With a variety of built-in input types—like text fields, multiple-choice options, and dropdowns—you can design forms that suit your specific needs.

**Best Practices for Forms:**

* **Provide Progress Indicators:** Adding progress bars or step indicators (like "Step X of Y") can help users see how far they've come and what's left to do. This makes the process feel less daunting and more manageable.
* **Streamlined Data Collection:** Frigade makes it easy to create new forms quickly, allowing you to gather user data and send it wherever you need it in your system.

## Resources

* Create a form and [send events to Slack](/guides/form-video-demo)
* Launch pop-up forms and surveys with no-code using [Collections](/platform/collections#announcements-surveys-and-dialogs)
* Target your form to specific users with [Targeting](/platform/targeting)
* See [industry examples](https://www.productonboarding.com/?type=form) of forms

## Demo

* See forms in action in our [live demo](https://demo.frigade.com/forms)

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## Examples

The following section includes ready-made examples and code for various form use cases.

### Simple Modal Form

<Tabs>
  <Tab title="Component">
    <Frame>
      <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/simple-modal.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=4993d78d77987a0a956294a703c3cf82" style={{ width: "350px" }} data-og-width="920" width="920" data-og-height="1161" height="1161" data-path="images/components/forms/simple-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/simple-modal.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=32589ba7fd89c6a36f9e3dc633f331ae 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/simple-modal.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=bd888c96dae62fe618f0bb8158978f3b 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/simple-modal.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=04a522e73807dd65c8c56a6a5afeb9e5 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/simple-modal.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1d8d9db32f56ca8c49200a4084a06b86 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/simple-modal.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=941a3da5589c851c725660bb166ac349 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/simple-modal.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=8e3d10fb04d793bff83ed15f837f9fab 2500w" />
    </Frame>
  </Tab>

  <Tab title="Configuration and Code">
    <CodeGroup>
      ```Typescript App.tsx theme={"system"}
      import * as Frigade from '@frigade/react';

      const App = () => {
      return (

      <Frigade.Form
        flowId="my-flow-id"
        // Remove the line below to render the Form inline
        as={Frigade.Dialog}
        dismissible
      />
      ) }

      ```

      ```yaml Configuration theme={"system"}
      steps:
        - id: waitlist-page
          title: Join the waitlist
          subtitle: Get pumped! We are launching soon.
          primaryButton:
            title: Join the waitlist
          fields:
            - id: company-size
              type: radio
              label: Company size
              options:
                - label: 1-10
                  value: 1-10
                - label: 20-100
                  value: 20-100
                - label: 100+
                  value: 100
            - id: industry
              type: select
              label: Industry
              options:
                - label: Icecream making
                  value: icecream
                - label: Guitar riffing
                  value: guitar-riffing
            - id: name
              type: text
              label: Your name
              placeholder: John Doe
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Churn Survey

<Tabs>
  <Tab title="Component">
    <Frame>
      <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/churn-survey.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=2c3d2956ea15ea89dd052851a349a9ec" style={{ width: "350px" }} data-og-width="1321" width="1321" data-og-height="1781" height="1781" data-path="images/components/forms/churn-survey.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/churn-survey.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=87042547988472169d02b72bdaf74dc5 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/churn-survey.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=d96a9770574d7f60350b1b3bdb0564df 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/churn-survey.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=6f16948e473ed6e8cdad72f6ff2ac57d 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/churn-survey.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=0bcb9a578d722cd4b4aaeb1fb24471ac 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/churn-survey.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=318065b0ae87fb461292852facbe0c8a 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/churn-survey.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=ac10d4ed7c4762120dcf3347aa95afd7 2500w" />
    </Frame>
  </Tab>

  <Tab title="Configuration and Code">
    <CodeGroup>
      ```Typescript App.tsx theme={"system"}
      import * as Frigade from '@frigade/react';

      const App = () => {
      return (

      <Frigade.Form flowId="my-flow-id" as={Frigade.Dialog} dismissible />) }

      ```

      ```yaml Configuration theme={"system"}
      steps:
        - id: collect-intend
          title: We are sorry to see you go
          subtitle: We are sorry to see you go. Please help us improve by answering a few questions.
          primaryButton:
            title: Cancel my plan
          fields:
            - id: rating
              type: select
              multiple: true
              label: Why would you like to cancel your plan?
              options:
                - label: Too expensive
                  value: too-expensive
                - label: Not enough features
                  value: not-enough-features
                - label: Found a better alternative
                  value: better-alternative
                - label: Too many bugs
                  value: too-many-bugs
                - label: Other
                  value: other
            - id: feedback
              type: textarea
              label: What can we do better?
              placeholder: Your feedback here
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Dynamic Fields

<Tabs>
  <Tab title="Component">
    <Frame>
      <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/dynamic-fields.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=c1b0625e7cf356a709bccbac2f139bb5" style={{ width: "350px" }} data-og-width="919" width="919" data-og-height="782" height="782" data-path="images/components/forms/dynamic-fields.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/dynamic-fields.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=4106290d7004f7aea09a03a09f493760 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/dynamic-fields.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=dfde548b1a0019d2f82012614b129aa7 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/dynamic-fields.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=53bc6bb77dd6d59e7af1180f48eb12a2 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/dynamic-fields.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=612134eeacae6da1efb44d19d67c41b1 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/dynamic-fields.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=92eb1a281891c640dfe3a4551ec73c4f 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/dynamic-fields.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=8789b16bab688d0b12ddd760f4b5b502 2500w" />
    </Frame>

    Sometimes you may want to conditionally render a dynamic field based on the value of another field. The example above dynamically changes the second dropdown based on the value of the first dropdown.
  </Tab>

  <Tab title="Configuration and Code">
    This component requires a custom form field for dynamically changing the input. You can achieve this by using the `formContext` provided by react-hook-forms.
    In this case, we define a [custom field](/component/form#custom-field-types) type called `DynamicFollowUpBasedOnField` that renders a `SelectField` component.
    The options of the `follow-up` dropdown depends on the value of `food`. If the user selects `pizza`, the `follow-up` dropdown will show options for pizza toppings. If the user selects `pasta`, the `follow-up` dropdown will show options for pasta sauces.

    <CodeGroup>
      ```Typescript App.tsx theme={"system"}
      import { Form, type FormFieldProps, SelectField } from "@frigade/react";

      const App = () => {
      return (

      <Form
      flowId="my-flow-id"
      fieldTypes={{
      DynamicFollowUpBasedOnField: (props: FormFieldProps) => {
      const categoryValue = props.formContext.watch("food");
      const field = props.fieldData.props.mappings[categoryValue];

                if (!field) {
                  return null;
                }

                return (
                  <SelectField
                    {...props}
                    fieldData={{
                      ...props.fieldData,
                      ...field,
                    }}
                  />
                );
              },
            }}
          />

      )
      }

      ```

      ```yaml Configuration theme={"system"}
      steps:
        - id: collect-intend
          title: Tell us about your favorites
          subtitle: Help us understand your preferences and taste.
          fields:
            - id: food
              label: What is your favorite food?
              type: select
              required: true
              options:
                - value: pizza
                  label: Pizza
                - value: pasta
                  label: Pasta
            - id: follow-up
              type: DynamicFollowUpBasedOnField
              required: true
              props:
                mappings:
                  pizza:
                    label: What is your favorite topping?
                    required: true
                    options:
                      - value: pepperoni
                        label: Pepperoni
                      - value: mushrooms
                        label: Mushrooms
                  pasta:
                    label: What is your favorite sauce?
                    required: true
                    options:
                      - value: tomato
                        label: Tomato
                      - value: alfredo
                        label: Alfredo
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Branching Forms

<Tabs>
  <Tab title="Component">
    <Frame>
      <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/branching.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=d54d1420b56feb62de58e88697fccfe4" style={{ width: "350px" }} data-og-width="1319" width="1319" data-og-height="910" height="910" data-path="images/components/forms/branching.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/branching.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=0ef2b92f69f9b07c341a9c7b3146ab96 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/branching.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=d404e5bf75bfce969bd5a34f64ceae19 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/branching.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=166f40e8444babb6847fa81b7b2de55b 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/branching.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=cd1e9f35dfa0c1d8d578d11d84033708 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/branching.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=2eff11b0bc3bfca2748fc80b8d57432a 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/forms/branching.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=47500fba0fe6b050f587ae9296939c06 2500w" />
    </Frame>

    This example shows how to implement branching in a form based on the user's choice in the first step.
  </Tab>

  <Tab title="Configuration and Code">
    If you want a form to conditionally skip a step based on the result of a previous step, you can use the `visibilityCriteria` property in the step configuration.
    For instance, the example below will jump directly to page 3 if the user picks a specific option on the first page/step:

    <CodeGroup>
      ```Typescript App.tsx theme={"system"}
      import * as Frigade from '@frigade/react';

      const App = () => {
      return (

      <Frigade.Form flowId="my-flow-id" as={Frigade.Dialog} dismissible />
      ); }

      ```

      ```yaml Configuration theme={"system"}
      steps:
        - id: page-1
          title: This is page 1
          primaryButtonTitle: Next
          fields:
            - id: test-radio-1
              type: radio
              label: Which page do you want to go to?
              options:
                - label: Go to page 3
                  value: x
                - label: Continue to page 2
                  value: y
        - id: page-2
          title: This is page 2
          primaryButtonTitle: Next
          # Replace the flow ID below with your own
          visibilityCriteria: user.flowStepData("my-flow-id", "page-1", "test-radio-1") != "x"
          fields:
            - id: test-text
              type: text
              label: Text field
        - id: page-3
          title: This is page 3
          primaryButtonTitle: Finish
          fields:
            - id: test-radio-3
              type: radio
              label: Radio group
              options:
                - label: Radio 1
                  value: 1
                - label: Radio 2
                  value: 2
                - label: Radio 3
                  value: 3
      ```
    </CodeGroup>

    `visibilityCriteria` will work with both form data or any other [Targeting](/platform/targeting#examples) condition.
  </Tab>
</Tabs>

## Supported Field Types

The component supports the following builtin field types that correspond to their respective HTML input types:

* `select`

* `radio`

* `text`

* `textarea`

* `checkbox`

### Overriding Field Attributes

You can override or add any attribute for a field by using the `props` property in the field configuration.
For instance, this is useful if you want to use the `text` field type, but override the `type` to `email` or `tel`. It can also be used to add any attribute such as a css class, data, or styling.

```yaml  theme={"system"}
steps:
  - id: step-1
    title: This is page 1
    fields:
      - id: email
        type: text
        props:
          type: email
          className: "my-custom-class"
          data-attr: "my-custom-data-attr"
          style:
            color: "red"
```

### Custom Field Types

The Form SDK is built on top of [react-hook-form](https://react-hook-form.com/), which means you can use the majority of its features in your forms. You can define your own custom field types using the `fieldTypes` [prop](#fieldtypes).
For instance, you can implement a simple calendar datepicker field type as such:

```tsx  theme={"system"}
import { FormFieldProps } from "@frigade/react";
import * as Frigade from "@frigade/react";

function CalendarField({ field, submit }: FormFieldProps) {
  return (
    <div>
      <input type="date" onChange={field.onChange} value={field.value} />
    </div>
  );
}

// ...

<Frigade.Form flowId="my-flow-id" fieldTypes={{ calendar: CalendarField }} />;
```

It is also possible to conditionally render a field based on the value of another field by using the [formContext](https://react-hook-form.com/docs/useformcontext) provided by react-hook-form.
For instance, if you want a custom field called `company-size` to show up when a user selects `company` in the `customer-type` field:

```tsx  theme={"system"}
import { type FormFieldProps, SelectField } from "@frigade/react";
import * as Frigade from "@frigade/react";

<Frigade.Form
  flowId="myflowid"
  fieldTypes={{
    "company-size": (props: FormFieldProps) => {
      const customerTypeValue = props.formContext.watch("customer-type");

      if (customerTypeValue !== "company") {
        return null;
      }

      return <div>My custom conditional field</div>;
    },
  }}
/>;
```

## Form Validation

The component supports client-side and server-side validation out of the box. You can define validation rules for each field in the form configuration using the `pattern` property with a regular expression. The example below shows how to validate an email field:

```yaml  theme={"system"}
steps:
  - id: collect-intend
    fields:
      - id: email
        type: text
        required: true
        pattern:
          message: Please provide a valid email
          value: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

### Server-side Validation

You can perform server-side validation by returning a Promise from the `onPrimary` event handler. If the promise resolves to `false`, the current step in the form will not be marked as completed. The `onPrimary` event handler also contains all form data collected in the session, which allows you to send the data to your server for validation or storage.

```tsx  theme={"system"}
import { StepHandlerProp } from "@frigade/react";
import * as Frigade from "@frigade/react";

const App = () => {
  const handlePrimary: StepHandlerProp = async (step, event, properties) => {
    const response = await fetch("https://my-server.com/validate", {
      method: "POST",
      body: JSON.stringify(properties),
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (response.ok) {
      return true;
    }

    // The current step in the form will be marked as completed
    return false;
  };

  return <Frigade.Form flowId="my-flow-id" onPrimary={handlePrimary} />;
};
```

## Browser Navigation

You can implement browser navigation (back/forward) with your Frigade forms using the [useFlow](/sdk/hooks/flow) hook. This allows users to navigate through form steps using their browser's back and forward buttons.

Here's an example of how to implement this:

```jsx  theme={"system"}
import { useFlow } from '@frigade/react';
import { useEffect, useRef } from 'react';

export function FormWithBrowserNavigation() {
  const flowId = 'your-flow-id';
  const { flow } = useFlow(flowId);
  const flowRef = useRef(flow);

  // Update ref when flow changes
  useEffect(() => {
    flowRef.current = flow;
  }, [flow]);

  useEffect(() => {
    if (!flowRef.current) return;

    // Handle browser navigation events
    const handlePopState = () => {
      const currentStepIndex = flowRef.current.getCurrentStepIndex();
      const newStepIndex = parseInt(window.location.hash.replace('#step-', '')) || 0;
      
      if (newStepIndex < currentStepIndex) {
        // User clicked back - go to previous step
        flowRef.current.back();
      } else if (newStepIndex > currentStepIndex) {
        // User clicked forward - go to next step
        flowRef.current.forward();
      }
    };

    // Add event listener for browser navigation
    window.addEventListener('popstate', handlePopState);

    // Cleanup
    return () => {
      window.removeEventListener('popstate', handlePopState);
    };
  }, []); 

  return (
    <Frigade.Form 
      flowId={flowId}
    />
  );
}
```

This example:

1. Uses the `useFlow` hook to get access to the flow instance
2. Uses a ref to store the flow instance and prevent re-renders
3. Sets up an event listener for browser navigation (`popstate`)
4. Handles browser back/forward navigation by moving to the appropriate step using `flow.back()` or `flow.forward()`
5. Cleans up the event listener when the component unmounts

When users click the browser's back button, they'll be taken to the previous step in the form. Similarly, clicking forward will take them to the next step.

## Prefilling a form

Forms can be prefilled by using [Dynamic Variables](/platform/dynamic-variables) by linking the `value` of a `field` to the `variables` prop of the Form component. The example below shows how to prefill a form with the user's name:

<CodeGroup>
  ```Typescript App.tsx theme={"system"}
  import * as Frigade from '@frigade/react';

  const App = () => {
  return (

  <Frigade.Form
  flowId="my-flow-id"
  variables={{
    name: "John Doe",
  }}
  />
  ) }

  ```

  ```yaml Configuration theme={"system"}
  steps:
    - id: collect-intend
      fields:
        - id: name
          type: text
          label: Your name
          value: ${name}
  ```
</CodeGroup>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```
      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="fieldTypes" type="FieldTypes">
      Custom field types to be used in the Form.
      You can use this to build your own custom form fields in a `Form`.

      For example, if you want to use a custom field type called `calendar`:

      ```tsx  theme={"system"}
      import { Form, FormFieldProps } from '@frigade/react'

      function CalendarField({ field, submit }: FormFieldProps) {
        return (
         <div>
           <input type="date" onChange={field.onChange} value={field.value} />
         </div>
        )
      }

       // ...

       <Form flowId="my-flow-id" fieldTypes={{ calendar: CalendarField }} />

      ```
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Register the Flow as a modal to prevent popup collisions (only one modal Flow will render at a time).
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="steps" type="array">
      The individual steps/pages of the form
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>

    <ParamField body="steps[].fields" type="array">
      The data contained on the form step, typically text input boxes, multiple choice questions, etc.
    </ParamField>

    <ParamField body="steps[].fields[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].fields[].label" type="string">
      The label of the field
    </ParamField>

    <ParamField body="steps[].fields[].value" type="string">
      The default value of the field (used for prefilling). For checkboxes, use 'true' or 'false'.
    </ParamField>

    <ParamField body="steps[].fields[].multiple" type="boolean">
      Whether the field can accept multiple values. Only used for the `select` type field.
    </ParamField>

    <ParamField body="steps[].fields[].type" type="string">
      The type of the field. The built-in supported types are: `text`, `textarea`, `select`, `checkbox`, and `radio`. If you are using custom form field types, the name here should match it.
    </ParamField>

    <ParamField body="steps[].fields[].placeholder" type="string">
      The placeholder of the field
    </ParamField>

    <ParamField body="steps[].fields[].maxLength" type="integer">
      The maximum length of the field
    </ParamField>

    <ParamField body="steps[].fields[].required" type="any">
      Whether the field is required or not. Use a string here to show a custom error message.
    </ParamField>

    <ParamField body="steps[].fields[].options" type="array">
      The options for the field. Only used for select fields.
    </ParamField>

    <ParamField body="steps[].fields[].options[].label" type="string">
      The label of the option
    </ParamField>

    <ParamField body="steps[].fields[].options[].value" type="any">
      The value of the option
    </ParamField>

    <ParamField body="steps[].fields[].pattern" type="object">
      The validation rules for the field. See documentation for more information.
    </ParamField>

    <ParamField body="steps[].fields[].pattern.value" type="string">
      Regex pattern to match the field against
    </ParamField>

    <ParamField body="steps[].fields[].pattern.message" type="string">
      The error message to display if the pattern does not match
    </ParamField>

    <ParamField body="steps[].fields[].props" type="object">
      Optional additional properties for the field. These will be passed to the frontend component as HTML attributes and merged with the default props for the given field type.
    </ParamField>
  </Tab>
</Tabs>

```
```


# Hint
Source: https://docs.frigade.com/component/hint

Hints are a great way to subtly call attention to specific parts of your UI

<Frame>
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=2da7d591eb61dcb9cec7eb90e6b6a9a4"
    style={{
    width: "350px",
  }}
    data-og-width="390"
    width="390"
    data-og-height="440"
    height="440"
    data-path="images/components/hint.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=49177bd51b9a24bb32c8d707eac66332 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9b5c06a32647218ad936be59da8b6305 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=74b6f27baa0bfe0471addc1145af6f22 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=8afbb6903463f6587367da28e3e200a1 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=719ae4f59f847c0ed1a6d29f35c7451f 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=86626bebb6613e9f1f49fc0b98ea4577 2500w"
  />
</Frame>

## About this component

The `Hint` component provides users with contextual guidance without interrupting their workflow. Unlike tours, hints are not sequential and are closed by default, allowing users to engage with them at their own pace. This design choice minimizes disruption and enhances the user experience by offering assistance when needed.

**When to Use Hints:**

* **Contextual Assistance:** Provide users with relevant tips or information based on their current task or location within the app.
* **Feature Highlights:** Draw attention to new or underutilized features without overwhelming users with a full tour.
* **Error Prevention:** Offer guidance that helps users avoid common mistakes or pitfalls as they navigate the application.

**Best Practices for Hints:**

* **Visibility:** Ensure hints are easily noticeable but not obtrusive. Use subtle animations or colors to draw attention without being distracting.
* **Actionable Content:** Like tours, hints should provide actionable advice. For example, instead of stating “This is the settings page,” a hint could say, “Click here to adjust your notification preferences.”
* **Dismissible:** Hints should be easily dismissible. Users should feel in control and not forced to engage with hints if they choose not to.

## Demo

* See hints in action in our [live demo](https://demo.frigade.com/hints)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx App.tsx theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Tour
          flowId='flow_laJhda4sgJCdsCy6'
          sequential={false} // Show all Steps at once
          defaultOpen={false} // Only show Hint markers
        />
      );
    };
    ```
  </Tab>

  <Tab title="No-code">
    Hints can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

Hints are a specific configuration of Tours. Please refer to the [Tour](/component/tour#sdk-properties) documentation to see properties for Hints.


# Card
Source: https://docs.frigade.com/component/inline-card

Communicate information or drive action via in-line content cards

<Frame className="h-96 items-center">
  <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=abfab3323d2170b86b6ee639e15944dd" style={{ maxWidth: "300px" }} data-og-width="360" width="360" data-og-height="165" height="165" data-path="images/components/inline-card.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=6abc6d7c71151f904a656b78283f5616 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=92d84811248e1db170f274ede35174d4 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=f69788ea49c6d800fa5777dab22bb7ea 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9b4f485d6b364775deea9388f28772ca 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=a7ccd2699537edf8410ee3df11409dd0 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=4db6b8e14ca67696eefbbf9faa2e9d0b 2500w" />
</Frame>

## About this component

The `Card` component is a handy little UI element that’s great for showing off promotional materials and important info in a visually appealing way. While they share some similarities with banners, cards have their own unique vibe and offer flexibility in placement.

**When to Use Cards:**

* **Promotional Materials:** Think of cards as your go-to swiss-army knife for inline promotions. For instance, showcasing new features, nudging users with onboarding tips, or encouraging user referrals.

**Advantages of Cards:**

* **Inline Placement:** You’ll usually find cards sitting neatly within in the main UI, like in a sidebar or alongside other product elements. This makes them easy to spot without getting in the way of the user experience.
* **Visual Appeal:** Cards can be designed with eye-catching images, icons, and text, making them interesting and engaging for users.
* **Versatile Use:** Whether you’re promoting a feature or sharing a helpful resource, cards can handle a variety of content types, making them super flexible.

**Best Practices for Cards:**

* **Strategic Placement:** Think about where you put your cards. Positioning them where users can easily see them can boost engagement.
* **Keep It Consistent:** Stick to a consistent design and placement across all your cards. These patterns helps create a cohesive look and feel throughout your app, which increases engagement.
* **Clear Calls to Action:** Make sure each card has a clear call to action, like “Learn More” or “Request Demo.” This encourages users to take that next step.

## Resources

* Launch cards with no-code using custom [Collections](/platform/collections#inline-ui-components)
* Target your card to specific users with [Targeting](/platform/targeting)
* See [industry examples](https://www.productonboarding.com/?type=card) of cards

## Demo

* See cards in action in our [live demo](https://demo.frigade.com/cards)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Card flowId="my-flow-id" />
      );
    };
    ```
  </Tab>

  <Tab title="No-code">
    Cards can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="children" type="any" />

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```
      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Register the Flow as a modal to prevent popup collisions (only one modal Flow will render at a time).
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="steps" type="array">
      The steps to show in the tooltip tour.
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>
  </Tab>
</Tabs>


# Components Overview
Source: https://docs.frigade.com/component/overview

Beautiful UI components, best practices built-in

***

Frigade comes with a library of pixel-perfect React UI components so you don't have to reinvent the wheel. Get started with one click creation from the <a href="https://app.frigade.com/dev/components">Components</a> tab, and visit the [SDK](/sdk/overview) docs for advanced usage and [styling guides](/sdk/styling/theming).

### Resources

<CardGroup cols={2}>
  <Card title="Figma UI Kit" icon="figma" href="https://www.figma.com/community/file/1311771082704525565/frigade-product-onboarding-ui-components">
    Free Figma file with Frigade components
  </Card>

  <Card title="Frigade Demo" icon="sparkles" href="https://demo.frigade.com/">
    See Frigade components in action
  </Card>
</CardGroup>

### Components

<CardGroup cols={2}>
  <Card title="Announcement" icon="bullhorn" href="/component/announcement">
    Communicate major product updates
  </Card>

  <Card title="Banner" icon="circle-info" href="/component/banner">
    Display inline product communications
  </Card>

  <Card title="Card" icon="rectangle" href="/component/inline-card">
    Embed tips and house ads in your UI
  </Card>

  <Card title="Checklist" icon="square-check" href="/component/checklist/">
    Activate users and drive account setup
  </Card>

  <Card title="Form" icon="clipboard" href="/component/form">
    Build native forms inline or in modals
  </Card>

  <Card title="Hints" icon="circle-question" href="/component/hint">
    Guide users to important UI elements
  </Card>

  <Card title="NPS Survey" icon="gauge-high" href="/component/survey/">
    Collect user feedback and other info
  </Card>

  <Card title="Tour" icon="comment-dots" href="/component/tour">
    Launch interactive, guided tours
  </Card>

  <Card title="Custom component" icon="gear" href="/guides/custom">
    Build with the headless Frigade SDKs
  </Card>
</CardGroup>


# Progress Badge
Source: https://docs.frigade.com/component/progress-badge

Display a user's progress through a Flow

<Frame className="h-96 items-center">
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=268f826aae66c1096fecfe00d390a6b7"
    style={{
    width: "220px",
  }}
    data-og-width="220"
    width="220"
    data-og-height="67"
    height="67"
    data-path="images/components/progress-badge.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=acb64175dce30c206a90c60f5e01b08c 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9a2c2e23719d8b3c8a62bf37ede988e0 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=43dc825fb2c9d094734dfd26cd638e9c 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=16642606f3d70aa01c10705d125de11c 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=684d3caa16a43f910ab4be5fc7464b39 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=d573a6396b82c5c7e50f2c7e6b91e30c 2500w"
  />
</Frame>

## About this component

The Progress Badge component is unlike other components in that it doesn't have its own Flow. It exists to remind a user where they left off in an existing Flow (e.g. Checklist), and to help get them jump back in and complete it.

## Demo

* See progress badges in action in our [live demo](https://demo.frigade.com/checklists)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.ProgressBadge flowId="my-flow-id" />
      );
    };
    ```
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties


# NPS Survey
Source: https://docs.frigade.com/component/survey/nps

Collect structured and freeform feedback from your users

<Frame className="h-96 items-center px-4">
  <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/nps.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=06e1d731f5cbff52fc864cc189bf9aca" data-og-width="622" width="622" data-og-height="188" height="188" data-path="images/components/nps.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/nps.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=dac77d4284c82a7c6d27cb2f043e3f7d 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/nps.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=60dad2c62b5ca6d98251758dca56769e 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/nps.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=26b83e9eabceddf2360f25d7e6be0665 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/nps.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=c0d804bd6aa655b0aeab86302e462218 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/nps.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=29169f8264a873974fe2613729603348 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/nps.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=ebe3f53154d3f611ae2ce715950c459c 2500w" />
</Frame>

## About this component

The `Survey` component is a fantastic way to engage users right when it matters and gather valuable feedback or data. Whether you’re looking to measure satisfaction or collect insights, targeted in-app surveys can help you connect with users at key moments in their journey.

**When to Use Surveys:**

* **User Research:** Deploy surveys like NPS (Net Promoter Score) right after users complete specific actions. This is a great way to capture their feelings while the experience is fresh in their minds.
* **Data Collection:** Use surveys to collect additional data after user signups, helping you enrich your CRM and tailor your communications.

**Best Practices for Surveys:**

* **Flexible Display Options:** By default, NPS surveys typically float on the screen, ensuring they don’t take over the entire user experience. This keeps the process smooth and non-intrusive.
* **Full-Screen Takeovers:** For the highest engagement rates, for custom surveys or other input forms, they can be displayed inline within the page or as a full page modal. Just be sure to use these methods thoughtfully to avoid annoying users.

**Custom Surveys:**

* **Built on Forms:** Custom surveys utilize the same underlying components as Forms, which means you can refer to the Forms documentation for more details on how to create and implement them effectively.

## Resources

* Launch surveys with no-code using [Collections](/platform/collections#announcements-surveys-and-dialogs)
* Target your survey to specific users with [Targeting](/platform/targeting)
* See [industry examples](https://www.productonboarding.com/?type=survey) of surveys

## Demo

* See surveys in action in our [live demo](https://demo.frigade.com/modals)

## Alternative scales

The component comes with a default NPS scale of 0-10. You can also use a custom scale by passing the `options` property either directly in the React component or in the YAML config via the `props` property. For instance, in the example below, we're using an emoji scale:

<Tabs>
  <Tab title="Emoji Survey">
    <Frame style={{ paddingTop: "64px", paddingBottom: "64px" }}>
      <img
        src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/surveys/emoji.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=5547c82d295589ed2566ddb41cddb2f2"
        style={{
        width: "340px",
        height: "auto",
      }}
        data-og-width="1034"
        width="1034"
        data-og-height="517"
        height="517"
        data-path="images/components/surveys/emoji.png"
        data-optimize="true"
        data-opv="3"
        srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/surveys/emoji.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=47bbf71587c609176319b500027ca119 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/surveys/emoji.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=dba2cd173dce5976b02905b8d8e16b21 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/surveys/emoji.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b2a373b7efa8ed69cf7ebe7ed1e4077f 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/surveys/emoji.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=8bffb090eeccb7ae16b93c570951569c 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/surveys/emoji.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=7742054ee55a372f735cd0abd6cfde88 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/surveys/emoji.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=0a651c4968ddaa7d52a54005cabc0633 2500w"
      />
    </Frame>
  </Tab>

  <Tab title="Code">
    <CodeGroup>
      ```Typescript App.tsx theme={"system"}
        import * as Frigade from '@frigade/react';
        
        const App = () => {
          return (
            <Frigade.Survey.NPS
             flowId="my-flow-id"
             dismissible={true}
             alignSelf="flex-end"
             justifySelf="flex-end"
             positiveLabel="Very good"
             negativeLabel="Very bad"
             options={[
              { label: "😞", value: "0" },
              { label: "😕", value: "1" },
              { label: "😐", value: "2" },
              { label: "🙂", value: "3" },
              { label: "😍", value: "4" },
              ]}
            />
          );
        };
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Survey.NPS flowId="my-flow-id" dismissible={true} />
      );
    };
    ```
  </Tab>

  <Tab title="No-code">
    NPS Surveys can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```
      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="fieldTypes" type="FieldTypes">
      Custom field types to be used in the Form.
      You can use this to build your own custom form fields in a `Form`.

      For example, if you want to use a custom field type called `calendar`:

      ```tsx  theme={"system"}
      import { Form, FormFieldProps } from "@frigade/react";

      function CalendarField({ field, submit }: FormFieldProps) {
        return (
          <div>
            <input type="date" onChange={field.onChange} value={field.value} />
          </div>
        );
      }

      // ...

      <Form flowId="my-flow-id" fieldTypes={{ calendar: CalendarField }} />;
      ```
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Register the Flow as a modal to prevent popup collisions (only one modal Flow will render at a time).
    </ParamField>

    <ParamField body="negativeLabel" type="string">
      The label to display for the negative end of the NPS scale.
      If not provided, the default label "Not likely at all" will be used.
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="options" type="NPSOptions">
      The options to display in the NPS field.
      If not provided, the default NPS numbers from 0 to 10 will be used.
    </ParamField>

    <ParamField body="positiveLabel" type="string">
      The label to display for the positive end of the NPS scale.
      If not provided, the default label "Extremely likely" will be used.
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="steps" type="array">
      The individual steps/pages of the form
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>

    <ParamField body="steps[].fields" type="array">
      The data contained on the form step, typically text input boxes, multiple choice questions, etc.
    </ParamField>

    <ParamField body="steps[].fields[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].fields[].label" type="string">
      The label of the field
    </ParamField>

    <ParamField body="steps[].fields[].value" type="string">
      The default value of the field (used for prefilling). For checkboxes, use 'true' or 'false'.
    </ParamField>

    <ParamField body="steps[].fields[].multiple" type="boolean">
      Whether the field can accept multiple values. Only used for the `select` type field.
    </ParamField>

    <ParamField body="steps[].fields[].type" type="string">
      The type of the field. The built-in supported types are: `text`, `textarea`, `select`, `checkbox`, and `radio`. If you are using custom form field types, the name here should match it.
    </ParamField>

    <ParamField body="steps[].fields[].placeholder" type="string">
      The placeholder of the field
    </ParamField>

    <ParamField body="steps[].fields[].maxLength" type="integer">
      The maximum length of the field
    </ParamField>

    <ParamField body="steps[].fields[].required" type="any">
      Whether the field is required or not. Use a string here to show a custom error message.
    </ParamField>

    <ParamField body="steps[].fields[].options" type="array">
      The options for the field. Only used for select fields.
    </ParamField>

    <ParamField body="steps[].fields[].options[].label" type="string">
      The label of the option
    </ParamField>

    <ParamField body="steps[].fields[].options[].value" type="any">
      The value of the option
    </ParamField>

    <ParamField body="steps[].fields[].pattern" type="object">
      The validation rules for the field. See documentation for more information.
    </ParamField>

    <ParamField body="steps[].fields[].pattern.value" type="string">
      Regex pattern to match the field against
    </ParamField>

    <ParamField body="steps[].fields[].pattern.message" type="string">
      The error message to display if the pattern does not match
    </ParamField>

    <ParamField body="steps[].fields[].props" type="object">
      Optional additional properties for the field. These will be passed to the frontend component as HTML attributes and merged with the default props for the given field type.
    </ParamField>
  </Tab>
</Tabs>


# Tour
Source: https://docs.frigade.com/component/tour

Guide users through a specific product flow or feature

<Frame>
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/tour.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=0fddc17d2f8f39376b145d04b2fd5a65"
    style={{
    width: "350px",
  }}
    data-og-width="424"
    width="424"
    data-og-height="474"
    height="474"
    data-path="images/components/tour.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/tour.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=19698c121504d03cb0087d27569c094a 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/tour.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=10a84940d932fddb1d2057272c4ae76c 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/tour.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=55e95fb2d752d6577c57a9c4734ce3d7 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/tour.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=c34245df4477cf0e4b0bc42b233ff9b4 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/tour.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=5f4075c13d7a0859543ef464dc728a3c 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/tour.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1a0b7a870cde45e653cbc2fcfee27ef3 2500w"
  />
</Frame>

## About this component

The `Tour` component is a sequential walkthrough designed to guide users through in-app steps. While tours can be one of the most effective ways to onboard users, they can also be a bit controversial. A poorly designed tour can be frustrating, especially if it interrupts users when they have a task in mind. We’ve all been there—logging into an app only to be confronted by an intrusive tour that disrupts our focus. This often leads to users rushing to close or ignore the tour, resulting in a net negative experience.

**When to Use Tours:**

* **Product Onboarding:** Show new users around critical workflows to get started
* **Feature Launches:** Increase adoption of a new feature by showing users how it workflows
* **Ongoing Education:** Automatically trigger tours for users once they reach a certain usage threshold, or give users the ability to request a tour themselves if they get stuck

**Best Practices for Announcements:**

* **Opt-In Design:** Tours should ideally be opt-in. Asking users if they want guidance results in much higher engagement compared to forcing a tour upon them. Users can opt in from a checklist, announcement, inline card, or help hub.
* **Actionable Steps:** Avoid generic and obvious statements like “This is the X page.” Instead, make tours actionable by connecting them to actual user actions. For example, a step that completes only when a user enters specific input or successfully finishes a task.
* **Keep It Short:** Tours should be concise—avoid lengthy, 16-step tours that can overwhelm users.
* **Dismissible:** Generally, tours should be dismissible. Be cautious about creating a tour that cannot be closed.
* **Relaunch Hub:** If relevant, consider providing a hub where users can relaunch specific tours. This is helpful if they are not ready or don’t have time when prompted.

## Resources

* [Create your first product tour](/guides/tours) in just a few minutes
* See [industry examples](https://www.productonboarding.com/?type=tour) of tours

## Demo

* See tours in action in our [live demo](https://demo.frigade.com/tours)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from "@frigade/react";

    const App = () => {
      return <Frigade.Tour flowId="my-flow-id" />;
    };
    ```
  </Tab>

  <Tab title="No-code">
    Tours can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="align" type="AlignValue">
      The alignment of the tooltip relative to the anchor.
      Possible values: `after`, `before`, `center`, `end`, `start`.
    </ParamField>

    <ParamField body="alignOffset" type="number">
      The offset of the tooltip relative to the anchor along the alignment axis.
    </ParamField>

    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoScroll" type="boolean">
      Automatically scroll to the anchor element of the current Step
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="container" type="string , Element , DocumentFragment">
      Specify a container in the DOM render the Tour into.
      Use this to render the Tour into a different container/scrollable ancestor.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```
      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="defaultOpen" type="boolean">
      Whether the tooltip should be open by default.
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="lockScroll" type="boolean">
      Whether to lock the scroll of the container when the Spotlight is enabled.
      Defaults to `true`.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Whether to render a modal overlay behind the tooltip.
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onOpenChange" type="(open: boolean) => void">
      Callback function triggered when the open state of the tooltip changes.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="open" type="boolean">
      Controls the open state of the tooltip. Use this for controlled components.
    </ParamField>

    <ParamField body="sequential" type="boolean">
      Whether the Tour should be completed by the end-user in sequential order.
      If `false`, all steps will be rendered at once.
      Defaults to `true`, which means only one step will be rendered at a time in sequential order.
    </ParamField>

    <ParamField body="side" type="SideValue">
      The preferred side of the anchor to render the tooltip.
      Possible values: `top`, `right`, `bottom`, `left`.
    </ParamField>

    <ParamField body="sideOffset" type="number">
      The distance in pixels from the tooltip to the anchor element.
    </ParamField>

    <ParamField body="spotlight" type="boolean">
      Whether to highlight the anchor element with a spotlight/scrim effect.
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="steps" type="array">
      The steps to show in the tooltip tour.
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>

    <ParamField body="steps[].selector" type="string">
      CSS class or ID of the element to highlight in the step (e.g. .my-element or #my-element)
    </ParamField>
  </Tab>
</Tabs>


# Guide: Product Announcements
Source: https://docs.frigade.com/guides/announcements



<Frame className="h-96 items-center px-4">
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1feb6c3c3162ad5dcfb671cee05b2720"
    style={{
                                                    width: '350px',
                                                    }}
    data-og-width="470"
    width="470"
    data-og-height="533"
    height="533"
    data-path="images/components/announcement.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=fa0489f75065c31f350c1bae87fb694d 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9c312391ce3bead7af2a56d8091fba32 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=160d89e44ac348fcd7acda99c3c72fd1 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=aecd9e5384c9c04f4d4088a4e118c861 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1d46eb5279067aa5749f69eca67d26e7 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=d2621dab38c40ab54856d4019ca57730 2500w"
  />
</Frame>

## Targeting announcements

You can target [announcements](/component/announcement) to specific groups of users using the [Targeting](/platform/targeting) section on the flow detail page.
By default, an announcement will show up for all users once the flow code is live in production.

## Launching additional announcements without code changes

We recommend using the [Dialogs Collection](/platform/collections) to launch new announcements without updating your product codebase. The Dialogs Collection is built-in to the Frigade SDK and can be used to launch Frigade Announcements, Surveys, and other Dialog-based components.

## Launching another Flow from an Announcement

You may want to launch another Flow when a user clicks on the primary button of a different Flow. For example, you can launch a tour Flow when a user clicks on the primary button of an announcement. You can achieve this my modifying the [Targeting](/platform/targeting) of the tour Flow directly in the Frigade dashboard, locating the given announcement under **Flows** and selecting **Completed** (typically initiated by the primary button) or **Dismissed** (if the user clicks the X button in the announcement).

<Frame>
  <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=0ed035d90662d8aa9f2d1949d08c6fc3" data-og-width="1051" width="1051" data-og-height="610" height="610" data-path="images/guides/announcement/announcement-launch-tour.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=a5d00c1de983ab24674affc473944955 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=80735621f0800fe1958ef45b6c781a5f 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b06efb5a4f391087cc1b152062e3a93c 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=ffe1eb01da8245cd28bbc9e590bd1cbc 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=abe7033b8f1317666a7fc81de3c8a35b 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1b2e9fea09f8df95e1e59b3d446f1d73 2500w" />
</Frame>


# Guide: Cards and Banners
Source: https://docs.frigade.com/guides/cards-video-demo

In this video, we show you how to build a GitHub style embedded card.

<iframe width="100%" height="355" src="https://www.youtube.com/embed/RlwZDlY9XMY?si=wyoKzVhZRP84dTwR" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

## Resources

* *[Quickstart guide](/sdk/quickstart)*
* *[Styling components](/sdk/styling/css-overrides)*
* *[Component setup guides](/guides/)*


# Using Custom Components in Collections
Source: https://docs.frigade.com/guides/custom/collections



[Collections](/platform/collections) allow you to deploy [Flows](/platform/flows) without having to manually embed them in your app code, which is great! Who doesn't love no-code deploys? But you may be asking "How do I use Custom Components if I'm not rendering React components directly?" Great question, let's dig in to how to use Custom Components in Collections.

To start, let's get a Collection set up with a Custom Flow in it:

<Steps>
  <Step title="Create a &#x22;Macguffins&#x22; Collection">
    In the Frigade web app, [Create a Collection](/platform/collections#creating-a-collection) named "Macguffins".
  </Step>

  <Step title="Create a new Custom Flow">
    1. In the top nav bar, click the "Create" button and select "Custom" from the list of available Flow types.
    2. Use the three dot menu to rename your flow to "The Rug"
    3. In the Advanced Flow editor, replace the default YAML with the following:

    ```yaml  theme={"system"}
    type: macguffin
    title: The Rug
    subtitle: It really ties the room together.
    owner: The Dude
    ```
  </Step>

  <Step title="Add your Flow to the Macguffins Collection">
    1. Select "Collections" in the left nav bar
    2. Click "Macguffins" from the list of Collections
    3. Click "Add Flows" and select "The Rug"
    4. Click "Save Collection" (or press CMD+S)
  </Step>

  <Step title="Embed the Macguffins Collection in your app">
    1. Click "In-App Channel" to show the embed code for your Collection
    2. Paste the embed code into your app
  </Step>
</Steps>

Great! Excellent job so far, you should now have a Collection in your app that does absolutely nothing. But this is a good thing! You've defined a Flow with a `type: macguffin` that's unknown to Frigade -- we don't have a built-in Component in the SDK that matches that Flow type, so there's nothing to render yet.

Let's fix that by wiring up a new `<Macguffin>` Component and registering it with the Frigade `<Provider>` so that we know how to render Flows with `type: macguffin`.

<Steps>
  <Step title="Create a Macguffin Component">
    Paste the following code into `Macguffin.tsx`

    ```jsx  theme={"system"}
    import { Flow, type FlowProps } from '@frigade/react';

    export function Macguffin(props: FlowProps) {
      return (
        <Flow {...props}>
          {({ flow }) => {
            <h3>{flow.title}</h3>
            <p>{flow.subtitle}</p>
            <p>{flow.owner}</p>
          }}
        </Flow>
      )
    }
    ```
  </Step>

  <Step title="Pass your Component into the Provider">
    Add the `flowTypes` prop to `<Frigade.Provider>` to map your new `<Macguffin>` Component to the `macguffin` Flow type

    ```jsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    import { Macguffin } from 'Macguffin.tsx'

    export function App() {
     return (
       <Frigade.Provider apiKey="..." flowTypes={{
         macguffin: Macguffin
       }}>
         {/* ... */}
       </Frigade.Provider>
     )
    }
    ```
  </Step>
</Steps>

That's it, you're done. You should now see your `<Macguffin>` rendering the contents of your Flow. Now that you have it set up, you can deploy any Flow with `type: macguffin` to any Collection.


# Flow Component
Source: https://docs.frigade.com/guides/custom/flow-component



`<Flow>` is a generic wrapper that bootstraps all of the functionality of a Frigade Flow. We use it as the basis for building Flow-aware Components in our SDK, and we recommend it as the starting point when building your own custom components.

In this example, we will build a custom announcement component with an open source UI kit. We'll use `AnnouncementProps` and `Flow` from `@frigade/react` to get the data. We'll use [Sanity UI](https://www.sanity.io/ui) primarily to build the UI.

The final result looks like this:

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=29f4e0062593b174af3534d393efb510" style={{maxWidth: '700px'}} data-og-width="2716" width="2716" data-og-height="1527" height="1527" data-path="images/guides/custom/sanity-announcement.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e03a17d57d8f684842ac66b9b8fc8393 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b77bf00b5db29d4c85fd940aad744e25 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1b2cfd65376cb6331f7087b5a02eeb4f 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4415757676733008a0beecae3f61ba5f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5af6ae32caeb1b1e969f19942d927885 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a8ef2dd0b39d0d431cfbdbf94e36993f 2500w" />
</Frame>

<Steps>
  <Step title="Create a new Announcement Flow">
    In the Frigade dashboard, tap "Create Flow" from the top right corner and select "Announcement" as the Flow type.
  </Step>

  <Step title="Update the Flow YAML">
    Next, we can update the YAML to include our desired announcement content. Here's an example we can start with:

    ```yaml  theme={"system"}
    steps:
      - id: announcement-page-one
        title: First page title
        subtitle: A space to share more details with users about your product update or announcement.
        primaryButton:
          title: Click me
          uri: https://www.frigade.com
          target: _blank
        secondaryButton:
          title: Next
        imageUri: https://frigade.com/img/grey-box-two.svg
      - id: announcement-page-two
        title: Second page title
        subtitle: This is also a space to share more details with users about your product update or announcement.
        imageUri: https://frigade.com/img/grey-box-two.svg
        primaryButton:
          title: Learn more
          uri: https://www.frigade.com
          target: _blank
    ```
  </Step>

  <Step title="Create a React component">
    Now let's create a React component to render our announcement in the product.

    We will import some components from `@frigade/react` and `@sanity/ui` to build the UI. Here are our imports:

    ```jsx  theme={"system"}
    "use client";
    import { Button, Card, Dialog, Flex, ThemeProvider } from "@sanity/ui";
    import { buildTheme } from "@sanity/ui/theme";
    import { AnnouncementProps, Flow, Progress, Text } from "@frigade/react";
    ```

    Next we have the announcement component. We use `flowId` to connect the component to our Frigade Flow. Then we use the Announcement props such as `step.title`, `step.subtitle`, `step.imageUri`, `step.primaryButton.title`, and `step.secondaryButton.title` to render the content where we like.

    We are using the Sanity UI `Dialog`, `Button`, `Card`, and `Flex` components to build the UI. Sanity doesn't have a component for progress, so we can import the `Progress` component from `@frigade/react` to render optional progress indicators for the current page.
    \`

    ```jsx  theme={"system"}
    export function AnnouncementWithFrigade({
      flowId,
      ...props
    }: AnnouncementProps) {
      return (
        <ThemeProvider theme={buildTheme()}>
          <Flow as={null} flowId={flowId} {...props}>
            {({
              flow,
              handleDismiss,
              handlePrimary,
              handleSecondary,
              parentProps: { dismissible },
              step,
            }) => (
              <Dialog
                __unstable_autoFocus={false}
                header={step.title}
                id="dialog-example"
                onClose={
                  dismissible
                    ? () => {
                        // @ts-expect-error - handleDismiss expects an event to be passed to it
                        handleDismiss();
                      }
                    : undefined
                }
                zOffset={1000}
              >
                <Flex
                  direction="column"
                  gap={4}
                  paddingRight={4}
                  paddingLeft={4}
                  paddingBottom={4}
                >
                  {step.imageUri && (
                    <Card radius={4} overflow="hidden">
                      <img src={step.imageUri} />
                    </Card>
                  )}

                  <Text.Body2>{step.subtitle}</Text.Body2>

                  <Progress.Dots
                    current={flow.getCurrentStepIndex() + 1}
                    marginInline="auto"
                    total={flow.getNumberOfAvailableSteps()}
                  />

                  <Flex direction="row" gap={3}>
                    {step.primaryButton?.title && (
                      <Button
                        onClick={handlePrimary}
                        text={step.primaryButton.title}
                        tone="primary"
                        width="fill"
                      />
                    )}
                    {step.secondaryButton?.title && (
                      <Button
                        onClick={handleSecondary}
                        mode="ghost"
                        space={3}
                        text={step.secondaryButton.title}
                        width="fill"
                      />
                    )}
                  </Flex>
                </Flex>
              </Dialog>
            )}
          </Flow>
        </ThemeProvider>
      );
    }
    ```
  </Step>

  <Step title="Place the component in your product">
    Now, if you've already installed Frigade via the [quick start guide](/quickstart), you can simply place the `AnnouncementWithFrigade` component in your product where you'd like the announcement to appear with the `Flow ID` we generated in the first step. Here's an example of how you might do that:

    ```jsx  theme={"system"}
    "use client";
    import { AnnouncementWithFrigade } from "@/components/Sanity/Announcement";

    const ECommerce: React.FC = () => {
      return (
        <>

          <AnnouncementWithFrigade dismissible={true} flowId="flow_VEJdWA2M" />

          {/* Your application here */}

        </>
      );
    };

    export default ECommerce;
    ```
  </Step>

  <Step title="You're done!">
    That's it! You've built a custom announcement component using the Frigade Engage React SDK and Sanity UI. If you visit the page you should now see your announcement in the product.

    As you interact with the Flow, you will see a user profile generated in the Frigade dashboard. You can delete the user or reset this specific Flow in the user profile page in order to see it again after completing it.

    Of course, you can always use targeting as well to ensure your announcement only shows up after a certain action or to a specific audience.
  </Step>
</Steps>


# JavaScript SDK
Source: https://docs.frigade.com/guides/custom/js-sdk



You can build components entirely headless using the [Frigade JS SDK](/sdk/js). For instance, to build a simple Checklist component, you can use the `Flow` and `Step` classes to get the data and build the UI. Here's an example of how to do just that:

<CodeGroup>
  ```js app.js theme={"system"}
  import { Flow, Step } from '@frigade/js';

  const flowId = 'flow_RgilNasCrSBQmrVM'; // Replace this with the Flow ID found in the Frigade dashboard
  const frigade = new Frigade('FRIGADE_API_KEY');
  const flow = await frigade.getFlow(flowId);

  const checklist = document.getElementById('checklist');

  const steps = flow.getSteps();
  const stepsCompleted = flow.getNumberOfCompletedSteps();
  const totalSteps = flow.getNumberOfAvailableSteps();

  const progress = document.createElement('div');

  progress.innerHTML = `
    <div>
      <h2>Getting started</h2>
      <p>${stepsCompleted}/${totalSteps}</p>
    </div>
    <div>
      ${steps.map((step, index) => {
        const isCompleted = index < stepsCompleted;
        return `<div style="background-color: ${isCompleted ? 'blue' : 'grey'}; height: 9px; width: 100%;"></div>`;
      }).join('')}
    </div>
  `;

  checklist.appendChild(progress);

  const stepsList = document.createElement('ul');
  stepsList.innerHTML = steps.map((step, index) => {
    const isCompleted = index < stepsCompleted;
    let html = `<li style="color: ${isCompleted ? 'blue' : 'grey'};">`
    html += `<p>${step.name}</p>`;
    html += `<button id="step-${step.id}">Mark Complete</button>`;
    html += `</li>`;
  }).join('');

  checklist.appendChild(stepsList);

  steps.forEach((step, index) => {
    const isCompleted = index < stepsCompleted;
    const button = document.getElementById(`step-${step.id}`);
    button.addEventListener('click', () => {
      if (!isCompleted) {
        step.complete();
        button.style.color = 'blue';
      }
    });
  });
  ```

  ```html index.html theme={"system"}
  <div id="checklist"></div>
  ```
</CodeGroup>


# useFlow Hook
Source: https://docs.frigade.com/guides/custom/useflow-hook



The `useFlow` hook sits one layer deeper in the React SDK than the [Flow Component](/guides/custom/flow-component) and serves as the connection between our vanilla JS data layer and React Components.

In most cases, you'll want to use `<Flow>` over `useFlow`, but if you need a deeper level of control over the lifecycle and behavior of a Flow, or if you need access to a Flow outside of a Component, this hook is for you.

In this example, we'll build a Progress Badge using the [useFlow hook](/sdk/hooks/flow) for the data layer.
Additionally, we'll leverage a series of prebuilt Frigade component primitives such as `<Box>` to build the UI.

The final result looks like this:

<Frame caption="A custom built progress badge">
  <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/custom/custom-progress-badge.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9db56ca86dd2bd80c270248acceb3b6f" style={{maxWidth: '400px'}} data-og-width="700" width="700" data-og-height="350" height="350" data-path="images/guides/custom/custom-progress-badge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/custom/custom-progress-badge.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=a1c94bd4415bbad009f37e70ce372d4e 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/custom/custom-progress-badge.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=e39ecc540c1f4a3f7e2bec87d626e781 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/custom/custom-progress-badge.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=88811d8bf9c7224d4f69889fc4d54b2f 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/custom/custom-progress-badge.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=4e5b634471ad031429613b18b7d7ac7e 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/custom/custom-progress-badge.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b91842a120890f3a7f716c8aace60a02 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/custom/custom-progress-badge.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b1a7f358bd45ea049003447218d9efa2 2500w" />
</Frame>

First, create a new Flow in the Frigade Dashboard by navigating to the **Flows** tab and clicking **Create Flow**. Select **Custom Flow** as the Flow type.

You can use any code you wish for the YAML configuration, however, we recommend starting with the following example:

```yaml  theme={"system"}
steps:
    # Only the id field is required per step.
  - id: unique-step-id-1
    title: Some title
    # You can add any custom fields here.
    # They will automatically be available in the Flow object.
    foo: bar
  - id: unique-step-id-2
    title: Some title
  - id: unique-step-id-3
    title: Some title

```

We're now ready to wire in the frontend code. Start by simply importing the `useFlow` hook. We'll then use the hook to get the flow data and calculate the number of steps completed and the total number of steps:

```jsx  theme={"system"}
import { useFlow } from '@frigade/react';

export function ProgressBadge() {
  const flowId = 'flow_RgilNasCrSBQmrVM'; // Replace this with the Flow ID found in the Frigade dashboard
  const { flow } = useFlow(flowId);
  const stepsCompleted = flow?.getNumberOfCompletedSteps();
  const totalSteps = flow?.getNumberOfAvailableSteps();
}
```

To see the full list of methods and fields in the `flow` object, see the [Flow API Reference](/sdk/js/flow).

Now, all we have left to do is to build the UI. We'll use the `Box` and `Text` components from the Frigade Engage React SDK to build the UI. We'll also use the `IconRender` component to render the ChevronRight icon from the `lucide-react` package:

```jsx  theme={"system"}
import { Box, Text, useFlow } from '@frigade/react';
import { ChevronRight } from 'lucide-react';

export function ProgressBadge() {
  const flowId = 'flow_RgilNasCrSBQmrVM';
  const { flow } = useFlow(flowId);
  const stepsCompleted = flow?.getNumberOfCompletedSteps();
  const totalSteps = flow?.getNumberOfAvailableSteps();


  if (!flow) {
  return null;
  }

  // This flag is automatically set to false if the Flow is not visible to the user.
  // Flows will automatically be hidden if the user has already
  // finished the Flow or if they don't fit the audience.
  if (!flow.isVisible) {
  return null;
  }

  return (
      <Box
        display="flex"
        flexDirection="column"
        border="md"
        borderRadius="md"
        borderColor="neutral.border"
        py={2}
        px={3}
        gap={1}
      >
        <Box
          display="flex"
          flexDirection="row"
          justifyContent="space-between"
          alignItems="center"
        >
          <Box display="flex">
            <Text.Body2
              fontWeight="medium"
              color="--fr-colors-x-sub-header-text"
            >
              Getting started
            </Text.Body2>
          </Box>
          <Box display="flex">
            <ChevronRight />
          </Box>
        </Box>

        <Box
          display="flex"
          flexDirection="row"
          justifyContent="center"
          alignItems="center"
          gap={2}
        >
          <Box display="flex" alignItems="center">
            <Text.Caption
              fontWeight="medium"
            >
              {stepsCompleted}/{totalSteps}
            </Text.Caption>
          </Box>
          <Box
            display="flex"
            gap={1}
            justifyContent="space-between"
            alignItems="center"
            width="100%"
          >
            {Array.from({ length: totalSteps }, (_, i) => {
              const stepNumber = i + 1;
              const isCompleted = stepNumber <= stepsCompleted;
              return (
                <Box
                  key={i}
                  backgroundColor={
                    isCompleted
                      ? 'blue'
                      : 'grey'
                  }
                  borderRadius="md"
                  height="9px"
                  width="100%"
                  display="flex"
                />
              );
            })}
          </Box>
        </Box>
      </Box>
  );
}
```

That's it! You've built a custom component using the Frigade Engage React SDK.


# Guide: Building Slack-Integrated Forms
Source: https://docs.frigade.com/guides/form-video-demo

In this video, we show you how to build a Form with React, Frigade, and Next.js and how to send the form data to Slack.

<iframe width="100%" height="355" src="https://www.youtube.com/embed/RxWUXCg9kaQ?si=LaML4V080pSN8pPB" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

## Resources

* *[Quickstart guide](/sdk/quickstart)*
* *[Form component](/component/form)*
* *[Slack integration](/integrations/slack)*
* *[Styling components](/sdk/styling/css-overrides)*
* *[Component setup guides](/guides/)*


# Guide: Build a 'New' Badge
Source: https://docs.frigade.com/guides/new-badge-video-demo

In this video, we show you how to build a 'New' badge with React and Frigade.

<iframe width="100%" height="355" src="https://www.youtube.com/embed/NnvPux1vHPs" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

## Resources

* *[Quickstart guide](/sdk/quickstart)*
* *[Custom components](/guides/custom)*


# Guide: Targeting New Users
Source: https://docs.frigade.com/guides/only-target-new-users

Learn how to use Frigade's [targeting](/platform/targeting) feature to only show a Flow to new users

### Targeting a Flow to new users

When building product onboarding, the brand new user experience is often one of the first experiences teams focus on. In this guide, we'll show you how to set up your Flow so that your new user experience is only shown to new users.

There are several ways to approach this, but we'll cover one of the most straight forward and popular methods.

<Steps>
  <Step title="Write sign up dates to Frigade user properties">
    First, we'll want begin passing user signup or account created dates to Frigade. You can do this by sending the property to Frigade with the SDK. The documentation on [User Hook](/sdk/hooks/user) has more details, but below is a code snippet with an example.

    ```tsx  theme={"system"}
    import { useUser } from '@frigade/react';

    const { addProperties } = useUser();

    addProperties({
      // Pull this number from your database or auth provider
      createdAt: '2023-08-01T00:00:00.000Z',
    });
    ```

    Once a property is written to Frigade, it will begin to show up in the user properties section of the user detail page and you'll be able to access it for Frigade targeting and dynamic variables.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=70d3ab7238176d7b7bee44c2d47b4b9f" className="rounded-md" style={{border: '1px solid #E8EBF0',}} data-og-width="1262" width="1262" data-og-height="830" height="830" data-path="images/guides/targeting/user-properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=96b3ecb80b417e9a9b70c90edec0872e 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=dbafc7b4523c4b552e23bf4cdea360e3 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1f900f6cdfa0722484e3395d7724c830 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8dec08c9c7485d10493779b4c381e72f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d04228b21bf0e0ae0e84bbdcb8446d80 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7db1a9b33f4cecf8738daa91ee5f2de9 2500w" />
  </Step>

  <Step title="Add targeting to your Flow">
    Next, open the **Targeting** tab of the Flow detail page. Click `Add filter`, then choose `User property`, and then choose our `createdAt` field we just set for account creation date. Once selected, we can set the logic so only shows it to new users.

    By choosing `is greater than` we can tell Frigade to only show this Flow to users whose sign up date is on or after a specific day, such as the day we roll the experience out. We could also choose an option like `within the last X days` to show an experience to users within a relative time period.

    You can of course adjust and combine the properties and periods to further refine your targeting (e.g. isEnterprise, completedSetup, etc.).

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=18a1ba27a4a2c0648a809537554b071d" alt="User detail page" className="rounded-md" style={{border: '1px solid #E8EBF0',}} data-og-width="1380" width="1380" data-og-height="802" height="802" data-path="images/guides/targeting/audience-targeting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b07aa401a1bfe3c39fdf8982e01c21f6 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fb1fe0fc047edc93a9301790fcc082af 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=703e4eb660d9e672095c0a631dd3f319 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=bb8340884bca79dc515d54be9f1d0c90 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e2ae69dbc192a06ac17f8a11c5a03ed0 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=12d78458757e707a0ff69ff8ee00032a 2500w" />

    And that's it! Now your Flow will only be shown to users who signed up in the period you specified. If you already have audiences set up with another analytics tool, be sure to check out our [Integrations](/integrations) to connect and use them in Frigade.
  </Step>
</Steps>


# Guide: Product Tours & Hints
Source: https://docs.frigade.com/guides/tours



<Frame caption="An example of a <Frigade.Tour/>">
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f155b1d2d3b4965cd228c8a2c127c48a" className="h-96" data-og-width="1980" width="1980" data-og-height="2010" height="2010" data-path="images/tours-tooltip-basic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=77320f2da88bea5507059f72c476e6c8 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3f9c18d20127c192c926be55153a57e8 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5f0c74b38d9d16bd58e7e8887af25e8d 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=512cdff16492459bab879079990ffe43 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=ec95265aa1f3458ac8b90c81b2ad280e 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=aad9484870af39b58cfcca4b21881127 2500w" />
</Frame>

## In this guide

1. [Adding a Tour to your application](#adding-a-tour-to-your-application)
2. [Adding Hints to your application](#adding-hints-to-your-application)
3. [Tips and tricks](#tips-and-tricks)

## Adding a Tour to your application

<Steps>
  <Step title="Create a Tour">
    In the Frigade Dashboard, create a new [Tour](https://app.frigade.com/prod/components/tour).
  </Step>

  <Step title="Find your Step anchors">
    Pick out the elements in your application that you want to attach individual Steps to.

    <Info>Each Step in a Tour uses a [CSS Selector](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors) to attach itself to the element in your page that you want to highlight. We recommend adding a unique `id` to your element to ensure that Frigade can find it.</Info>

    ```tsx  theme={"system"}
    <span id="my-element">
      This is the element that we're going to attach a Tour Step to.
    </span>
    ```
  </Step>

  <Step title="Configure your Flow">
    In the Frigade Dashboard, use the `selector` property in each step of your Tour to highlight the desired element in your application:

    ```yaml  theme={"system"}
    steps:
      - title: "Welcome to Frigade!"
        description: "This is a tour of the Frigade platform."
        selector: "#my-element"
    ```
  </Step>

  <Step title="Embed the Tour Component">
    Add the [Tour](/component/tour) Component to your application with its corresponding Flow ID.

    ```tsx  theme={"system"}
    <Frigade.Tour flowId="flow_Bkh43aEjXcrna2lO" />
    ```
  </Step>
</Steps>

## Adding Hints to your application

<Steps>
  <Step title="Create some Hints">
    In the Frigade Dashboard, create new [Hints](https://app.frigade.com/prod/components/hints).
  </Step>

  <Step title="Find your Hint anchors">
    Pick out the elements in your application that you want to attach individual Steps to.

    <Info>Each Hint uses a [CSS Selector](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors) to attach itself to the element in your page that you want to highlight. We recommend adding a unique `id` to your element to ensure that Frigade can find it.</Info>

    ```tsx  theme={"system"}
    <span id="my-element">
      This is the element that we're going to attach a Hint to.
    </span>
    ```
  </Step>

  <Step title="Configure your Flow">
    In the Frigade Dashboard, use the `selector` property in each Hint to highlight the desired element in your application.

    ```yaml  theme={"system"}
    steps:
      - title: "Welcome to Frigade!"
        description: "This is a tour of the Frigade platform."
        selector: "#my-element"
    ```
  </Step>

  <Step title="Embed the Tour Component">
    No, that's not a typo, Hints are actually a specially configured `<Frigade.Tour>`!

    ```tsx  theme={"system"}
    <Frigade.Tour
      flowId='flow_Bkh43aEjXcrna2lO'
      sequential={false} // Show all Steps at once
      defaultOpen={false} // Only show Hint markers
    />
    ```
  </Step>
</Steps>

## Tips and tricks

### Seamless navigation between pages

One of the benefits of Frigade is that it can tap into your existing router to navigate users across pages without janky page refreshes. Check out our guide on [Navigation](/sdk/navigation) for setup.

### Debugging Steps

If a Step in a Tour is not appearing when you expect it to, you can enable debugging by enabling Verbose logging in your browser. To enable this in Chrome Devtools, simply click the three dot menu in the console as shown below:

<Frame caption="Enabling verbose logging in Chrome Devtools">
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2cb121c8d0f6d50b0ef13854c4e88cc5" className="h-96" data-og-width="747" width="747" data-og-height="518" height="518" data-path="images/guides/tours/debug.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=87a7d41c953e184c6a6516a3f5e885d6 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4abbb3951dc9331370a6f6b4b617277c 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3a0001bebc5a08f2775d501d9f74eafe 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=689d603f223b048760769c4add41fa1b 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4436c048e73e7919f760018e1ee60405 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5791ff4778ba19a1c93463807329259f 2500w" />
</Frame>

This will log if a selector is not found on the current page.

### Controlling the z-index of Steps

By default, Steps are rendered with a z-index of 9999. To change this, you can use the `zIndex` prop on a Tour:

```tsx  theme={"system"}
<Frigade.Tour flowId="my-flow-id" zIndex={100} />
```

Or alternatively, you can override the z-index for a specific Step directly in the YAML config using the `zIndex` property:

```yaml  theme={"system"}
steps:
  - id: my-tour-step
    title: My title
    subtitle: My subtitle
    primaryButton:
      title: Got it
    selector: "#my-tour-step-anchor"
    props:
      zIndex: 42
```

### Overriding position for a specific Step

If you want to force a specific Step to show up on the left or right side of the targeted element, you can use the `align` and `side` properties in Config YAML to override the default positioning.
It follows the same syntax as the [align and side props](/component/tour#align) on the `Tour` component.

```yaml  theme={"system"}
steps:
  - id: my-tour-step
    title: My title
    subtitle: This Step will show up on the left of the target element, after its trailing edge
    primaryButton:
      title: Got it
    selector: "#my-tour-step-anchor"
    props:
      align: after
      side: left
```

### Offset x and y positioning

You can add a custom offset to the x and y positioning of each Step in a Tour using the `sideOffset` and `alignOffset` properties (see [Tour component documentation](/component/tour)).
Alternatively, you can override the offset for a specific Step directly in the YAML config by leveraging the `props` field:

```yaml  theme={"system"}
steps:
  - id: my-tour-step
    title: My title
    subtitle: My subtitle
    primaryButton:
      title: Got it
    selector: "#my-tour-step-anchor"
    props:
      sideOffset: 10
      alignOffset: -10
```

### Hiding CTA buttons

Sometimes you may want to hide the CTA button on a single Step for a user to take an action in your application rather than simply continuing the tour on every button click. To do this, simply omit the `primaryButton.title` property in the YAML config:

```yaml  theme={"system"}
steps:
  - id: my-tour-step
    title: My title
    subtitle: My subtitle
    # Omitting primaryButton.title will hide the CTA button
    # primaryButton:
    #   title: Got it
    selector: "#my-tour-step-anchor"
```

### Programmatically completing a step

If you want too programmatically complete the step (e.g. an action in your app advances the Flow), see the documentation for automatically [advancing a Flow](/sdk/advanced/completing-a-step).


# Amplitude
Source: https://docs.frigade.com/integrations/amplitude



Frigade supports sending events to Amplitude. The following guide will help you set up this integration in just a few steps.

## Sending Frigade events to Amplitude

You can set up Frigade to send events to Amplitude when your users take actions in your Flows.
The event types and data schema is identical to the events sent in [Frigade Webhooks](/api-reference/webhooks).

<Steps>
  <Step title="Copy your Amplitude API Key">
    Log in to your Amplitude account, open the settings menu, and select **Organization settings**. Select the **Projects** tab and copy the API Key for the project you want to send events to. Do not copy the secret API key as only the public API key is required.

    <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=cb793dc1cd31739ad093c80fb904e809" className="rounded" data-og-width="1471" width="1471" data-og-height="1188" height="1188" data-path="images/amplitude-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=188cd96f97dbd480e37763dd769562ab 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=17dc33c9387d94ade461614082be54f0 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b84c99f6ca0a01c9088792c56ffd72ef 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=39b08cd005223ababfea581840b6a77f 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=5ea895c4dc166728929ee1074b36b937 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-1.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=af4c59c2c03eaaafc5b3fc297a180753 2500w" />
  </Step>

  <Step title="Add Amplitude as an integration in Frigade">
    Open the **Integrations** page in Frigade and select **Amplitude**. Paste the API key you copied in step 1 and click **Save**. If the integration is enabled, events will start streaming to Amplitude immediately.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=0bd8ef8b05ba31ea930921b461acd737" className="rounded" data-og-width="3248" width="3248" data-og-height="2124" height="2124" data-path="images/integrations/amplitude.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=daa2446ce8fa7ae54eff1bab412d5304 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e47eb5d33eb86b9eb65c94237a8a4a69 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=df9716537176a4e0baa4e23b9b197516 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8aaaff68c0189795afedf8b79ca03302 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f2b2788b9c828c5527f03739725979ca 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/amplitude.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2453f5c43d3171bebb49fa719978d261 2500w" />
  </Step>

  <Step title="See data in Amplitude">
    Open the dashboard for the project you selected in step 1 and take some action in any given Frigade Flow such as completing a step. You should see events starting to stream from Frigade in the **Realtime event stream** widget:

    <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=888e39d259276c646c97490422f590b3" className="rounded" data-og-width="1471" width="1471" data-og-height="1188" height="1188" data-path="images/amplitude-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=caa38c6fd57a33c77d59c2d615cbbab8 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=72d137ccaa11791b98b11c1efae15578 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=e386123d83186fa12d7b06b9cb3e6205 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=562d2795e3011a55c86a104b4b833ed0 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=55506b07f06caa7b300803e1019659f4 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/amplitude-2.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=5db397e5c09e318c73cc0b6abbaf357d 2500w" />
  </Step>
</Steps>

## Sending Amplitude data to Frigade

Bidirectional read/write to Amplitude is not yet available on all Frigade plans. If you're interested in this feature, please [get in touch](mailto:support@frigade.com).


# Heap
Source: https://docs.frigade.com/integrations/heap



Frigade supports bidirectional reads and writes from Heap. This guide shows you how to get started in a few minutes.

## Sending Frigade data to Heap

The following steps will help you send data from Frigade to Heap. For instance, when a user completes a Survey or a step in a Checklist, Frigade can send this data to Heap.

<Steps>
  <Step title="Get your Heap Environment ID">
    From the Heap dashboard, navigate to **Settings** and open **Projects**.
    Click the appropriate project and environment and copy the numeric **Environment ID**.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=c9aaf64c9e9d33f7ee678558d91ef958" className="rounded" data-og-width="1493" width="1493" data-og-height="875" height="875" data-path="images/integrations/heap/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9a8954b0fc9aceac40c834c4b694b02a 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=50b597f97779b8f87c156b3805901071 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fb36214f35cec377737735bca99c3721 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=19b91f54245e189366973a1d59f85c89 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6535c18c36c879714861e0d17ab09f5f 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/1.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a81aaffc595f4dc4e820d9f0ab641c0d 2500w" />
  </Step>

  <Step title="Add Heap in Frigade">
    Next, go to your Frigade dashboard and select **Integrations**. Click **Add Integration** and select **Heap**.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6bcc9086b2808f9d596ddaed04bb449d" className="rounded" data-og-width="1395" width="1395" data-og-height="825" height="825" data-path="images/integrations/heap/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7c05651a411f06d612188cc9541becfc 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=75aa5121e93c01f767dc8e1971062d93 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5eab8efc716d0cc25c1c3e9c868ad0d4 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=83eb8ed9df03c08be2fe24b218e8e04e 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=97165363154e329c233d6a314e5c2307 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/2.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1b4060a4e52646d0ec8f58b59edb48c5 2500w" />

    You will be asked to enter your Heap Environment ID. Click **Connect** to save and activate the integration. Shortly after, events will start streaming from Frigade in real-time.
  </Step>

  <Step title="See Frigade events in Heap">
    You should now see events from Frigade in your Heap dashboard. You can test the integration by completing a Flow and checking the **Live data feed** page in Heap:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ca238de01f7f28293ffb7f95c2a2edbb" className="rounded" data-og-width="1380" width="1380" data-og-height="812" height="812" data-path="images/integrations/heap/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6e2fded11031ee5879b1f029fb7264dc 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=df5336e86ec739e01384c3e2b66203be 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=cb616c9898e02d0f5fa57e0d64d638f8 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=45a3454dd05a44db6208e0821407d2a6 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3e5ab8a811fc3c7a13cd3828c7bc1386 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/heap/3.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3ddaeec8d7a8593b426dd9eac505f1f2 2500w" />
  </Step>
</Steps>

## Sending Heap segments to Frigade

<Note>This feature is in early preview. <a href="mailto:support@frigade.com">Reach out</a> to get early access.</Note>


# Hubspot
Source: https://docs.frigade.com/integrations/hubspot



Frigade supports writing data to Hubspot. When users take action in Flows, Frigade will send the data and any corresponding metadata to Hubspot.
For instance, when a User completes a Survey or a step in a Checklist, Frigade will send this data to Hubspot to the matching contact.

<Info>
  Frigade will only send data to Hubspot if the User has an email associated with them. To associate an email with a User, see the [useUser hook](/sdk/hooks/user) or the [User API](/api-reference/users).
</Info>

# Sending Frigade data to Hubspot

<Steps>
  <Step title="Create a Hubspot API Token">
    To get started, you will need to create a Hubspot API token by setting up a Private App in your Hubspot account.
    You can do this by navigating to the **Settings** > **Integrations** > **Private Apps** page as seen below:
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=07c6859475a52f65a4aaba50e3d524f6" alt="Hubspot Integrations" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a14c093d2560b7cca0f5981b2c6b6b4b 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f0a60c4dd4516841d083410c4f43f9ea 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=59da4914ec4e6f23f589528470bfe357 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2ddae539a7fbdfa5c6bf03bb6278b3a2 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4991712290c491780866e8714d9d9edf 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=bc21d89a19f90e1f3f30e69d51e23657 2500w" />
  </Step>

  <Step title="Create a new App">
    Click on the **Create a private app** button to create a new app. Type in "Frigade" as the app name. Leave description and logo blank.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ac5b0ddfda5ac87eb0ac98101296a5f5" alt="Create App" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/create-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1e8ec611475a7bb4eb371fa5bd32766e 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2099187dfb23755b91d7e9c1edfb9225 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=80e34c7758ae0938236807a07c853c4b 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e9fb817d41d7d7020f931600f72677b9 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9feb350d2f5beb0ae122f8f6a88dcd68 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8180baf64102155196a8b7995d302ba6 2500w" />
  </Step>

  <Step title="Set App Scopes">
    Click on the **Scopes** tab and select the scopes which you would like Frigade to have access to. As a minimum, `contact.objects.contacts` is required for reading and writing.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7b5069080bfdb2fd6e630a2ca16d4f52" alt="Set Permissions" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/app-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=49c79c73ec78f3139c19382e83cfda8f 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a888c8b5a705e780899895fb6a665d65 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4c5d7d8637a83041d757fe2892a534dd 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=90f16e1d83bc4da6298785badcb6672f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a7a5b2c007a0382a359c24f8e995f999 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7ee293d9d0ca455163c3ded2fb472741 2500w" />
    Once you have set the permissions, click on the **Create app** button.
  </Step>

  <Step title="Get API Key">
    Once the app is created, you will be presented with the API token. Copy this token.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=26c876e442236acda0a2d166d7a338bf" alt="Get API Key" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/app-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5f58a306e11dce0456e12fd1dcaab0c3 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e069bbafe0b693416224176b0db707ba 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3e81835fdbbde6cae21cc6205b56974a 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fc2f6b43733b1921e9421f800fe5367c 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=38834f97016fa8d68577e8746a2341cd 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2ca6a90b674afeb501599fa3e044cb30 2500w" />
  </Step>

  <Step title="Add Token to Frigade">
    In the Frigade dashboard, navigate to the **Integrations** page and click on the **Hubspot** integration. Paste the API token into the input field and click **Save**.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e2d8b5be62e2d4165a7124594f7792e9" alt="Add token to Frigade" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/frigade-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f6cae782b6e2d3e4f23ecc09b1b6e692 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=922147edc2a3e268954eceb54c762f0f 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=69c745af7cf68921665aa9d5341a65c7 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ac2b4f5ef314e7bb771d7da59b862ac6 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3b5858a379089e8a444bfe24a7658ec9 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=61957cc28373f41479b708a3ff28241f 2500w" />

    <Info>
      As soon as you save the token, Frigade will start sending data to Hubspot.
    </Info>
  </Step>

  <Step title="Verify Data in Hubspot">
    That's it! Data from Frigade will now start streaming to Hubspot in real time.

    You can test the integration by completing a Flow and checking the data in Hubspot for the corresponding contact.
    All data is added as Notes to the contact in Hubspot as seen below:
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=791aacea8840297353cee31e88ee30dd" alt="Hubspot Data" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/frigade-hubspot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=00c4a78f802cc61bf5ffd85188a5a458 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ff2053c258b9dcb14fb532572bd11ff0 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7e9b6893ebbc88c1bcc6125ed8b9f29f 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=223089f75ea333e28691df278a7061ee 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5afcad78da5a9eb79a5897e934d2e6bc 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=64d7477b3eab0803105bcfb4dd577576 2500w" />
  </Step>
</Steps>


# Mixpanel
Source: https://docs.frigade.com/integrations/mixpanel



Frigade supports ingesting Mixpanel data and using this data to [Target flows](/platform/targeting) to users.

There are two ways to integrate Mixpanel with Frigade: real-time sync (via Mixpanel Webhooks) or a daily sync (via the Mixpanel API). Both options can also be used together.

Depending on your use case, we recommend using the Webhook integration for real-time data and the API integration for historical data as well as syncing non-standard user properties.

## Mixpanel Webhooks (Webhook sync)

Sending Mixpanel data via Webhooks allows you to send real-time data to Frigade as your users enter and leave cohorts. The setup process is as follows:

<Steps>
  <Step title="Create a Webhook in Mixpanel">
    Following the [Mixpanel documentation](https://docs.mixpanel.com/docs/cohort-sync/webhooks), create a new Webhook on the Mixpanel **Integrations** page.
    You should use the following parameters when creating the webhook:

    * **Connector name:** `Frigade`
    * **URL:** `https://api.frigade.com/v1/thirdParty/cdp/mixpanel`
    * **Username:** `frigade`
    * **Password:** Your <i>private</i> Frigade API key (found on the **Developer** page in the Frigade dashboard)

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ed5a954894da7024871e313c1913e57e" className="rounded" data-og-width="2800" width="2800" data-og-height="1996" height="1996" data-path="images/integrations/mixpanel/webhook-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d039dac8383c04c7c36350afb464b488 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6096cf4e27e69943eb36f24703e6b1e6 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2cde3c53e0925cc016d48a21114f1604 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=eff3d9d445606dfdb0aa99a6e2d25bd2 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3f98671eaa9d60343fa362b2e7af17fc 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-1.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=02a3f106b94f7bddba9f8a7731a2acac 2500w" />
  </Step>

  <Step title="View cohort data in Frigade">
    After setting up the Webhook, you will see the cohort data in the Frigade dashboard. Note that it may take up to 30 minutes the first time before all data is synced.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=c5718e6927779a1f29f4591fd46697b7" className="rounded" data-og-width="2902" width="2902" data-og-height="1992" height="1992" data-path="images/integrations/mixpanel/webhook-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=96afcbd6c22fac3f4370f1c9b1fbba34 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=26a2e749fa11e3084c0751e8c7666e16 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=063d8c3308f11e1dfe7daaa2da72c3e9 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4e9dd8c8d7dc108cbcaf615524870bff 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=cbe69ca912b4eb3da56806e25536ae8b 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/mixpanel/webhook-2.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d05a4a45a6ababb48804fc8d72f4d8ca 2500w" />
  </Step>
</Steps>

## Mixpanel Cohorts in Frigade (API sync)

To send your Cohorts to Frigade, you will need to create a service account in Mixpanel and add the keys to Frigade. Frigade will then automatically sync your cohorts from Mixpanel.

<Steps>
  <Step title=" Create a Mixpanel Service Account for Frigade">
    To create a service account for Frigade, open your Mixpanel project, then click **Project Settings** and select the **Service Accounts** tab. Then click **Add Service Account** and select **Analyst** as the role.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7604297781f5dc49f0550957fb74ecc3" className="rounded" data-og-width="1540" width="1540" data-og-height="1121" height="1121" data-path="images/mixpanel-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=62e9cb7070d57bd1b87c1e58d04f36d6 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e821d9a42308858c3ccda2ecd127ead6 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7aa21e8b4c638c05620fb97adff42eb5 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=594a1d4969d572ce7bc7cb431d3eb83e 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8debd8b0001dc46d0af280fb143f205e 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-1.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=c0b1d5a4f544f1d77a302c6cf35aaafe 2500w" />
  </Step>

  <Step title="Add the Mixpanel Service Account keys to Frigade">
    Open the [Integrations](https://app.frigade.com/integrations) page in the Frigade dashboard and click the "Connect" button for Mixpanel. Then paste the two keys you copied in the previous step into the corresponding fields.

    Then, copy the **Project ID** from Mixpanel that you wish to sync cohorts from. You can find the Project ID on the Project Settings page in Mixpanel:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f471191ddfc81704dbfb891775d06136" className="rounded" data-og-width="1540" width="1540" data-og-height="1121" height="1121" data-path="images/mixpanel-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=750e18a1cbd6d06f85c99d5cc41eeb43 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2ae6650eaa4dcdc23b3069beb147f33a 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=0338d22c3080805e35322ee79d2324d0 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=788c855bfb471e13a925d84376b3b05e 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=0af007772aa3c6d76b5af8bb1503b8b4 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-2.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=dc11d8bfa29d9cfd4fecbc6d99280bba 2500w" />
  </Step>

  <Step title="See your Mixpanel Cohorts in Frigade">
    Your Mixpanel cohorts appear as properties on your users in Frigade. Each cohort is prefixed with `mixpanel_cohort_` and the name of the cohort. For example, if you have a cohort named `NewUsers`, you will see a property named `mixpanel_cohort_NewUsers` on your users in Frigade.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=58d6d81abb9bbf50c23d2bafcea6e24c" className="rounded" data-og-width="2980" width="2980" data-og-height="2136" height="2136" data-path="images/mixpanel-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=cdcfd968617f0cddad59d87863dc8dfa 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8b00d23a23f7f44d31a2c4f50f6d074e 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f8f03a7aed9fee357d8a23e3fe011707 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f585743a19993fa122481d15fee6b61f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8bc27427a16e6476af2f4cb0773425ab 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/mixpanel-3.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=61a9e7e6c76218673e7601942b324049 2500w" />
  </Step>
</Steps>

## Targeting Mixpanel Cohorts

You can target users based on these properties in the [Targeting](/platform/targeting) section of the Frigade dashboard. For instance, to target users in the `NewUsers` cohort, you can use the following targeting rule:

```js  theme={"system"}
user.property('mixpanel_cohort_NewUsers') == true
```


# Overview
Source: https://docs.frigade.com/integrations/overview

Connect your favorite tools to Frigade

<CardGroup cols={3}>
  <Card
    title="Amplitude"
    href="/integrations/amplitude"
    icon={
                                                         <svg className="h-7 w-7" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                         <path d="M15.5988 8.04494C15.4989 7.91714 15.3924 7.84668 15.2646 7.84668C15.1728 7.85323 15.0876 7.88273 15.009 7.93188C14.0635 8.67087 12.7773 11.8055 11.7188 15.9412L12.6576 15.9477C14.5059 15.969 16.4165 15.9903 18.3008 16.0182C17.8027 14.1273 17.3341 12.5068 16.9015 11.1926C16.2674 9.28205 15.8414 8.42181 15.5988 8.04494Z" fill="#1E61F0"/>
                                                         <path d="M17.6964 0.078125C7.92405 0.078125 0 8.00217 0 17.7745C0 27.5468 7.92405 35.4709 17.6964 35.4709C27.4687 35.4709 35.3928 27.5468 35.3928 17.7745C35.3928 8.00217 27.4687 0.078125 17.6964 0.078125ZM30.7589 17.5615C30.7098 17.7598 30.5885 17.9531 30.4181 18.094C30.3968 18.1088 30.3755 18.1219 30.3542 18.1366L30.3329 18.1514L30.2903 18.1792L30.2543 18.2005C30.1199 18.271 29.9692 18.307 29.8135 18.307H21.4274C21.4913 18.584 21.5699 18.9035 21.6469 19.2459C22.109 21.2286 23.3248 26.5014 24.6242 26.5014H24.652H24.6668H24.6946C25.704 26.5014 26.2234 25.0382 27.3606 21.8316L27.3753 21.7955C27.5605 21.2843 27.7669 20.701 27.9865 20.0832L28.0439 19.9276C28.1291 19.7211 28.3634 19.6146 28.5698 19.6998C28.7189 19.7572 28.8254 19.9063 28.8254 20.0701C28.8254 20.1127 28.8189 20.1488 28.8107 20.1832L28.7615 20.3388C28.6403 20.7223 28.5207 21.2417 28.3699 21.8463C27.6948 24.6466 26.6707 28.8757 24.0556 28.8757H24.0343C22.3433 28.861 21.334 26.1606 20.8998 25.0022C20.0903 22.8409 19.4791 20.5453 18.8893 18.3152H11.1864L9.58718 23.439L9.56588 23.4177C9.32501 23.7946 8.82034 23.9076 8.44347 23.6668C8.20916 23.5176 8.0666 23.262 8.0666 22.9851V22.9573L8.16655 22.3739C8.38612 21.0598 8.65648 19.6867 8.9547 18.3087H5.68578L5.67104 18.2939C5.00251 18.194 4.54043 17.5697 4.64039 16.9012C4.71904 16.3817 5.1172 15.9705 5.62843 15.8771C5.75624 15.8623 5.88405 15.8558 6.01186 15.8623H6.16752C7.19817 15.8771 8.29272 15.8984 9.50034 15.9115C11.1995 9.00333 13.1674 5.49191 15.3565 5.48535C17.7013 5.48535 19.4431 10.8221 20.8359 16.0458L20.8424 16.0671C23.7 16.1245 26.756 16.2097 29.7185 16.4227L29.8463 16.4374C29.8954 16.4374 29.938 16.444 29.9888 16.4522H30.0036L30.0183 16.4588H30.0249C30.5312 16.5587 30.8654 17.0568 30.7589 17.5615Z" fill="#1E61F0"/>
                                                         </svg>}
  />

  <Card
    title="Heap"
    href="/integrations/heap"
    icon={

  <svg
                                                                 className="h-8 w-8"
                                                                 width="50"
                                                                 height="30"
                                                                 viewBox="0 0 50 30"
                                                                 fill="none"
                                                                 xmlns="http://www.w3.org/2000/svg"
                                                               >
                                                                 <path d="M4.6,8.6H0v22.7h4.6V8.6z" fill="#000000"/>
    <path d="M14.7,0h-4.6v17.3h4.6V0z" fill="#000000"/>
    <path d="M14.7,22.7h-4.6V40h4.6V22.7z" fill="#31D891"/>
    <path d="M24.8,8.6h-4.6v22.7h4.6V8.6z" fill="#31D891"/>

                                                               </svg>
                                                             }
  />

  <Card
    title="Hubspot"
    href="/integrations/hubspot"
    icon={<svg
                                                                                                                              className="h-8 w-8"
                                                               width="27" height="28"
                                                                                                                              viewBox="0 0 27 28"
                                                                                                                              fill="none"
                                                                                                                              xmlns="http://www.w3.org/2000/svg"
                                                                                                                            >
                                                                                                                              <g id="MHE-Post-Launch-Updates" stroke="none" strokeWidth="1" fill="none" fillRule="evenodd">
                                                                  <path d="M19.614233,20.1771162 C17.5228041,20.1771162 15.8274241,18.4993457 15.8274241,16.4299995 C15.8274241,14.3602937 17.5228041,12.6825232 19.614233,12.6825232 C21.7056619,12.6825232 23.4010418,14.3602937 23.4010418,16.4299995 C23.4010418,18.4993457 21.7056619,20.1771162 19.614233,20.1771162 M20.7478775,9.21551429 L20.7478775,5.88190722 C21.6271788,5.47091457 22.243053,4.59067833 22.243053,3.56912967 L22.243053,3.49218091 C22.243053,2.08229273 21.0774338,0.928780545 19.6527478,0.928780545 L19.5753548,0.928780545 C18.1506688,0.928780545 16.9850496,2.08229273 16.9850496,3.49218091 L16.9850496,3.56912967 C16.9850496,4.59067833 17.6009238,5.47127414 18.4802251,5.88226679 L18.4802251,9.21551429 C17.1710836,9.4157968 15.9749432,9.95012321 14.9884545,10.7365107 L5.73944086,3.61659339 C5.80048326,3.3846684 5.84335828,3.14591151 5.84372163,2.89492912 C5.84517502,1.29842223 4.53930368,0.00215931486 2.92531356,1.87311107e-06 C1.31205014,-0.00179599501 0.00181863138,1.29087118 1.8932965e-06,2.88773765 C-0.00181484479,4.48460412 1.30405649,5.78086703 2.91804661,5.7826649 C3.44381061,5.78338405 3.93069642,5.63559929 4.35726652,5.39540411 L13.4551275,12.3995387 C12.6815604,13.5552084 12.2281026,14.9395668 12.2281026,16.4299995 C12.2281026,17.9901894 12.7262522,19.433518 13.5677653,20.6204705 L10.8012365,23.3586237 C10.5825013,23.2935408 10.3557723,23.2482346 10.1152362,23.2482346 C8.78938076,23.2482346 7.71423516,24.3118533 7.71423516,25.6239375 C7.71423516,26.9363812 8.78938076,28 10.1152362,28 C11.441455,28 12.5162373,26.9363812 12.5162373,25.6239375 C12.5162373,25.3866189 12.4704555,25.1618854 12.4046896,24.9454221 L15.1414238,22.2371135 C16.3837093,23.1752411 17.9308435,23.7390526 19.614233,23.7390526 C23.6935367,23.7390526 27,20.466573 27,16.4299995 C27,12.7756527 24.2872467,9.7566726 20.7478775,9.21551429" fill="#FF7A59">
                                                                  </path>
                                                                </g>

                                                                                                                            </svg>}
  />

  <Card
    title="Mixpanel"
    href="/integrations/mixpanel"
    icon={
      <svg
        className="h-8 w-8"
        style={{ fill: "#7856ff" }}
        viewBox="0 0 98 98"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path d="M24.2391 58.7912C29.877 58.7912 34.4475 54.2207 34.4475 48.5828C34.4475 42.9449 29.877 38.3745 24.2391 38.3745C18.6012 38.3745 14.0308 42.9449 14.0308 48.5828C14.0308 54.2207 18.6012 58.7912 24.2391 58.7912Z"></path>
        <path d="M54.7787 55.7046C58.7675 55.7046 62.0011 52.4716 62.0011 48.4834C62.0011 44.4952 58.7675 41.2622 54.7787 41.2622C50.7899 41.2622 47.5563 44.4952 47.5563 48.4834C47.5563 52.4716 50.7899 55.7046 54.7787 55.7046Z"></path>
        <path d="M78.6018 52.0652C80.547 52.0652 82.1239 50.4883 82.1239 48.5431C82.1239 46.5979 80.547 45.021 78.6018 45.021C76.6566 45.021 75.0798 46.5979 75.0798 48.5431C75.0798 50.4883 76.6566 52.0652 78.6018 52.0652Z"></path>
      </svg>
    }
  />

  <Card
    title="Posthog"
    href="/integrations/posthog"
    icon={
                                                               <svg
                                                                 className="h-8 w-8"
                                                                 width="50"
                                                                 height="30"
                                                                 viewBox="0 0 50 30"
                                                                 fill="none"
                                                                 xmlns="http://www.w3.org/2000/svg"
                                                               >
                                                                 <path
                                                                   d="M10.8914 17.2057c-.3685.7371-1.42031.7371-1.78884 0L8.2212 15.443c-.14077-.2815-.14077-.6129 0-.8944l.88136-1.7627c.36853-.7371 1.42034-.7371 1.78884 0l.8814 1.7627c.1407.2815.1407.6129 0 .8944l-.8814 1.7627zM10.8914 27.2028c-.3685.737-1.42031.737-1.78884 0L8.2212 25.44c-.14077-.2815-.14077-.6129 0-.8944l.88136-1.7627c.36853-.7371 1.42034-.7371 1.78884 0l.8814 1.7627c.1407.2815.1407.6129 0 .8944l-.8814 1.7628z"
                                                                   fill="#1D4AFF"
                                                                 />
                                                                 <path
                                                                   d="M0 23.4082c0-.8909 1.07714-1.3371 1.70711-.7071l4.58338 4.5834c.62997.63.1838 1.7071-.7071 1.7071H.999999c-.552284 0-.999999-.4477-.999999-1v-4.5834zm0-4.8278c0 .2652.105357.5196.292893.7071l9.411217 9.4112c.18753.1875.44189.2929.70709.2929h5.1692c.8909 0 1.3371-1.0771.7071-1.7071L1.70711 12.7041C1.07714 12.0741 0 12.5203 0 13.4112v5.1692zm0-9.99701c0 .26521.105357.51957.292893.7071L19.7011 28.6987c.1875.1875.4419.2929.7071.2929h5.1692c.8909 0 1.3371-1.0771.7071-1.7071L1.70711 2.70711C1.07715 2.07715 0 2.52331 0 3.41421v5.16918zm9.997 0c0 .26521.1054.51957.2929.7071l17.994 17.99401c.63.63 1.7071.1838 1.7071-.7071v-5.1692c0-.2652-.1054-.5196-.2929-.7071l-17.994-17.994c-.63-.62996-1.7071-.18379-1.7071.70711v5.16918zm11.7041-5.87628c-.63-.62997-1.7071-.1838-1.7071.7071v5.16918c0 .26521.1054.51957.2929.7071l7.997 7.99701c.63.63 1.7071.1838 1.7071-.7071v-5.1692c0-.2652-.1054-.5196-.2929-.7071l-7.997-7.99699z"
                                                                   fill="#F9BD2B"
                                                                 />
                                                                 <path
                                                                   d="M42.5248 23.5308l-9.4127-9.4127c-.63-.63-1.7071-.1838-1.7071.7071v13.1664c0 .5523.4477 1 1 1h14.5806c.5523 0 1-.4477 1-1v-1.199c0-.5523-.4496-.9934-.9973-1.0647-1.6807-.2188-3.2528-.9864-4.4635-2.1971zm-6.3213 2.2618c-.8829 0-1.5995-.7166-1.5995-1.5996 0-.8829.7166-1.5995 1.5995-1.5995.883 0 1.5996.7166 1.5996 1.5995 0 .883-.7166 1.5996-1.5996 1.5996z"
                                                                   fill="#000"
                                                                 />
                                                                 <path
                                                                   d="M0 27.9916c0 .5523.447715 1 1 1h4.58339c.8909 0 1.33707-1.0771.70711-1.7071l-4.58339-4.5834C1.07714 22.0711 0 22.5173 0 23.4082v4.5834zM9.997 10.997L1.70711 2.70711C1.07714 2.07714 0 2.52331 0 3.41421v5.16918c0 .26521.105357.51957.292893.7071L9.997 18.9946V10.997zM1.70711 12.7041C1.07714 12.0741 0 12.5203 0 13.4112v5.1692c0 .2652.105357.5196.292893.7071L9.997 28.9916V20.994l-8.28989-8.2899z"
                                                                   fill="#1D4AFF"
                                                                 />
                                                                 <path
                                                                   d="M19.994 11.4112c0-.2652-.1053-.5196-.2929-.7071l-7.997-7.99699c-.6299-.62997-1.70709-.1838-1.70709.7071v5.16918c0 .26521.10539.51957.29289.7071l9.7041 9.70411v-7.5834zM9.99701 28.9916h5.58339c.8909 0 1.3371-1.0771.7071-1.7071L9.99701 20.994v7.9976zM9.99701 10.997v7.5834c0 .2652.10539.5196.29289.7071l9.7041 9.7041v-7.5834c0-.2652-.1053-.5196-.2929-.7071L9.99701 10.997z"
                                                                   fill="#F54E00"
                                                                 />
                                                               </svg>
                                                             }
  />

  <Card
    title="Salesforce"
    href="/integrations/salesforce"
    icon={<svg width="800px" height="800px" className="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                                 <path d="M15.1823 12.0413C15.2625 11.9197 15.3033 11.7476 15.3033 11.5292C15.3033 11.3111 15.2625 11.1393 15.1826 11.019C15.103 10.8999 14.983 10.8419 14.8157 10.8419C14.648 10.8419 14.5286 10.8999 14.4506 11.019C14.3716 11.1393 14.3315 11.3111 14.3315 11.5292C14.3315 11.7476 14.3716 11.92 14.4506 12.0413C14.5286 12.1619 14.648 12.2202 14.8157 12.2202C14.983 12.2202 15.103 12.1616 15.1823 12.0413Z" fill="#479FDA"/>
                                                                 <path d="M19.5355 11.0191C19.4838 11.0977 19.4503 11.1987 19.4324 11.3199H20.3419C20.3328 11.2031 20.3099 11.0977 20.2573 11.0191C20.178 10.9 20.0674 10.8342 19.9 10.8342C19.7326 10.8342 19.6136 10.8997 19.5355 11.0191Z" fill="#479FDA"/>
                                                                 <path d="M9.32318 11.0191C9.27148 11.0977 9.23824 11.1987 9.22008 11.3199H10.1295C10.1204 11.2031 10.0975 11.0977 10.0452 11.0191C9.96563 10.9 9.85499 10.8342 9.68765 10.8342C9.5203 10.8342 9.40121 10.8997 9.32318 11.0191Z" fill="#479FDA"/>
                                                                 <path d="M6.39015 12.0794C6.40706 12.1051 6.41395 12.1151 6.46379 12.1549C6.46284 12.1546 6.57817 12.2452 6.83766 12.2295C7.02004 12.2185 7.18175 12.1837 7.18175 12.1837V11.604C7.18175 11.604 7.01848 11.577 6.83578 11.5745C6.57568 11.5711 6.46507 11.667 6.46599 11.6666C6.3892 11.7209 6.35223 11.8014 6.35223 11.9136C6.35223 11.9844 6.36506 12.0402 6.39015 12.0794Z" fill="#479FDA"/>
                                                                 <path fillRule="evenodd" clipRule="evenodd" d="M12.9449 4.78232C11.8524 4.78232 10.8646 5.24084 10.1551 5.98012C9.37442 4.9594 8.14311 4.30065 6.75761 4.30065C4.39778 4.30065 2.48453 6.21106 2.48453 8.56775C2.48453 9.17104 2.61021 9.74487 2.83615 10.2648C1.73866 10.9063 1 12.1053 1 13.4786C1 15.5279 2.64405 17.1888 4.672 17.1887C4.93087 17.1887 5.18315 17.1618 5.42665 17.1101C5.98385 18.6217 7.43547 19.6993 9.13874 19.6993C10.7743 19.6993 12.1777 18.706 12.78 17.2891C13.2382 17.5126 13.7528 17.6381 14.2969 17.6381C15.5965 17.6381 16.7288 16.922 17.3229 15.8622C17.6305 15.9243 17.9434 15.9555 18.2572 15.9553C20.8765 15.9553 23 13.8133 23 11.1708C23 8.52859 20.8765 6.38655 18.2572 6.38655C17.5743 6.38655 16.9253 6.5323 16.3389 6.79427C15.6642 5.59211 14.3971 4.78232 12.9449 4.78232ZM13.9857 9.69029C14.034 9.69937 14.071 9.70784 14.1117 9.72038C14.1205 9.7238 14.1453 9.73602 14.1352 9.76493L14.0378 10.0326C14.0296 10.0526 14.024 10.0648 13.9823 10.0523C13.9719 10.0491 13.9566 10.0448 13.9171 10.0363C13.8886 10.0303 13.8507 10.026 13.8124 10.026C13.762 10.026 13.7159 10.0322 13.6755 10.0454C13.636 10.0582 13.5999 10.0805 13.5686 10.1118C13.5369 10.1438 13.4993 10.1905 13.4793 10.2479C13.4395 10.363 13.4202 10.4843 13.414 10.5232L13.4119 10.5355H13.8196C13.8538 10.5355 13.8644 10.5512 13.8613 10.5766L13.8137 10.8417C13.8064 10.8802 13.771 10.879 13.771 10.879H13.3511L13.0637 12.5046C13.0336 12.6725 12.9957 12.8167 12.9515 12.9327C12.907 13.0502 12.8603 13.136 12.786 13.2182C12.7171 13.294 12.6394 13.3501 12.5504 13.3824C12.4617 13.4143 12.3545 13.4309 12.2373 13.4309C12.1812 13.4309 12.1214 13.43 12.0505 13.4134C11.9994 13.4012 11.9715 13.3924 11.9339 13.3792C11.918 13.3733 11.9054 13.3535 11.9142 13.3282C11.9233 13.3028 11.9985 13.0962 12.0089 13.069C12.022 13.0361 12.0549 13.0486 12.0549 13.0486C12.0778 13.0583 12.0938 13.0649 12.1239 13.0709C12.1543 13.0771 12.1953 13.0822 12.226 13.0822C12.2815 13.0822 12.3323 13.0753 12.3761 13.0605C12.4294 13.0427 12.4602 13.012 12.4927 12.9706C12.5266 12.9273 12.5538 12.8681 12.5817 12.7891C12.6103 12.7089 12.636 12.6033 12.6582 12.4748L12.944 10.879H12.6623C12.6285 10.879 12.6175 10.863 12.6209 10.8379L12.6682 10.5725C12.6758 10.5343 12.7109 10.5355 12.7109 10.5355H13.0004L13.0161 10.4493C13.0593 10.1933 13.1455 9.99866 13.2725 9.87078C13.4 9.7423 13.5818 9.67711 13.8125 9.67711C13.8786 9.67711 13.9368 9.68153 13.9857 9.69029ZM8.37841 12.5168C8.39973 12.5168 8.41508 12.4996 8.41508 12.4783V9.75672C8.41508 9.73544 8.39973 9.71819 8.37841 9.71819H8.04026C8.01895 9.71819 8.00391 9.73544 8.00391 9.75672V12.4783C8.00391 12.4996 8.01895 12.5168 8.04026 12.5168H8.37841ZM4.1927 12.3325C4.18612 12.3262 4.1752 12.3159 4.18661 12.2861L4.27569 12.0391C4.28978 11.9965 4.32207 12.0106 4.33491 12.0188C4.34531 12.025 4.35463 12.0311 4.36435 12.0374C4.37747 12.0459 4.3913 12.0548 4.40949 12.0654C4.6718 12.2312 4.91468 12.2328 4.99083 12.2328C5.18702 12.2328 5.30861 12.1288 5.30861 11.989V11.9815C5.30861 11.8287 5.12191 11.7713 4.90503 11.7046L4.85639 11.6897C4.55834 11.6045 4.24026 11.4822 4.24026 11.1052V11.0977C4.24026 10.7401 4.52857 10.4907 4.94161 10.4907L4.98673 10.4904C5.22928 10.4904 5.46371 10.5609 5.63325 10.664C5.6486 10.6734 5.66364 10.6909 5.65519 10.7148C5.64735 10.7367 5.57212 10.9391 5.56336 10.9617C5.54737 11.004 5.50381 10.9758 5.50381 10.9758C5.35527 10.8937 5.12461 10.8291 4.93031 10.8291C4.75544 10.8291 4.64262 10.9219 4.64262 11.0479V11.0557C4.64262 11.203 4.83544 11.2656 5.05905 11.3383L5.09797 11.3509C5.39476 11.4446 5.71095 11.5744 5.71095 11.9317V11.9392C5.71095 12.3256 5.43078 12.5656 4.97951 12.5656C4.75795 12.5656 4.54607 12.5309 4.32169 12.4118L4.2954 12.397C4.26199 12.3783 4.22879 12.3598 4.19601 12.3359C4.19526 12.3349 4.19407 12.3337 4.1927 12.3325ZM10.7992 12.3325C10.7927 12.3262 10.7817 12.3159 10.7932 12.2861L10.8822 12.0391C10.8953 11.9987 10.9336 12.0134 10.9417 12.0188L10.9568 12.0285C10.9744 12.04 10.9912 12.051 11.016 12.0654C11.2783 12.2312 11.5212 12.2328 11.5973 12.2328C11.7935 12.2328 11.9154 12.1288 11.9154 11.989V11.9815C11.9154 11.8288 11.7286 11.7714 11.5119 11.7048L11.4629 11.6897C11.1648 11.6045 10.8467 11.4822 10.8467 11.1052V11.0977C10.8467 10.7401 11.135 10.4907 11.5481 10.4907L11.5932 10.4904C11.8358 10.4904 12.0702 10.5609 12.2397 10.664C12.2551 10.6734 12.2702 10.6909 12.2617 10.7148C12.2538 10.7367 12.1786 10.9391 12.1698 10.9617C12.1539 11.004 12.1103 10.9758 12.1103 10.9758C11.9618 10.8937 11.7311 10.8291 11.5368 10.8291C11.3619 10.8291 11.2491 10.9219 11.2491 11.0479V11.0557C11.2491 11.2029 11.4419 11.2656 11.6653 11.3382L11.7045 11.3509C12.0013 11.4446 12.3175 11.5744 12.3175 11.9317V11.9392C12.3175 12.3256 12.0373 12.5656 11.586 12.5656C11.3645 12.5656 11.1526 12.5309 10.9282 12.4118L10.9018 12.3969C10.8685 12.3783 10.8353 12.3598 10.8026 12.3359C10.8021 12.3353 10.8015 12.3346 10.8008 12.3339C10.8003 12.3335 10.7998 12.333 10.7992 12.3325ZM15.5086 10.7971C15.5853 10.8889 15.643 10.9992 15.68 11.1243C15.7169 11.2487 15.7355 11.385 15.7355 11.5292C15.7355 11.6734 15.717 11.8097 15.68 11.9341C15.643 12.0591 15.5853 12.1695 15.5086 12.2613C15.4318 12.3534 15.3343 12.4271 15.2193 12.4794C15.104 12.5317 14.9683 12.5584 14.8157 12.5584C14.6627 12.5584 14.527 12.5317 14.4117 12.4794C14.2967 12.4271 14.1992 12.3534 14.1224 12.2613C14.0453 12.1692 13.988 12.0588 13.9507 11.9341C13.914 11.81 13.8955 11.6737 13.8955 11.5292C13.8955 11.3847 13.914 11.2487 13.9507 11.1243C13.988 10.9996 14.0457 10.8893 14.1221 10.7971C14.1992 10.705 14.2964 10.631 14.4117 10.5771C14.5267 10.5235 14.6627 10.4963 14.8157 10.4963C14.9683 10.4963 15.1043 10.5235 15.2193 10.5771C15.3346 10.631 15.4318 10.705 15.5086 10.7971ZM18.7254 12.139C18.7254 12.139 18.7608 12.1252 18.7733 12.1619L18.8658 12.4173C18.8777 12.449 18.8504 12.4621 18.8504 12.4621C18.7082 12.5182 18.5101 12.5574 18.3171 12.5574C17.9905 12.5574 17.7401 12.4631 17.5734 12.2775C17.407 12.0926 17.3227 11.84 17.3227 11.5276C17.3227 11.3831 17.3433 11.2465 17.3841 11.1221C17.4251 10.9973 17.4865 10.887 17.5674 10.7949C17.6482 10.7027 17.7504 10.6288 17.8708 10.5752C17.9914 10.5213 18.1324 10.4943 18.2907 10.4943C18.3966 10.4943 18.4919 10.5009 18.5734 10.5135C18.6605 10.5266 18.7758 10.5576 18.8247 10.5767C18.8335 10.5802 18.8579 10.5924 18.8479 10.6209C18.8244 10.6883 18.8056 10.7399 18.7859 10.7942L18.7554 10.8786C18.7413 10.9174 18.7116 10.9046 18.7116 10.9046C18.5875 10.8654 18.469 10.8475 18.3136 10.8475C18.1271 10.8475 17.9874 10.9099 17.8955 11.0315C17.8031 11.1537 17.7517 11.3142 17.751 11.5276C17.7504 11.762 17.8087 11.9353 17.9128 12.0425C18.0165 12.1497 18.1613 12.2039 18.3437 12.2039C18.4179 12.2039 18.4872 12.1989 18.5502 12.1892C18.6122 12.1795 18.6705 12.16 18.7254 12.139ZM20.5374 10.7549C20.5895 10.8107 20.6688 10.9326 20.7007 11.0532C20.7772 11.3219 20.7449 11.5563 20.7393 11.597L20.7386 11.6026C20.7351 11.6352 20.7016 11.6358 20.7016 11.6358L19.4265 11.6346C19.4346 11.8282 19.4807 11.9655 19.575 12.0589C19.6668 12.1501 19.8135 12.2084 20.0112 12.2087C20.2873 12.2093 20.4194 12.1587 20.5097 12.1241L20.5346 12.1147C20.5346 12.1147 20.5701 12.1018 20.5826 12.1366L20.6659 12.3701C20.6829 12.4096 20.6694 12.4234 20.6553 12.4312C20.5754 12.4754 20.3814 12.5575 20.0131 12.5587C19.8342 12.5591 19.6784 12.5334 19.5503 12.4838C19.4211 12.4341 19.3133 12.3626 19.2297 12.2714C19.1457 12.1808 19.0836 12.0715 19.0448 11.9473C19.0062 11.8242 18.9868 11.6872 18.9868 11.5402C18.9868 11.3958 19.0056 11.2588 19.0429 11.1332C19.0799 11.0069 19.1381 10.8956 19.2156 10.8022C19.293 10.7085 19.3917 10.6333 19.5092 10.5781C19.6264 10.523 19.7709 10.4963 19.9301 10.4963C20.0667 10.4963 20.1915 10.5258 20.2955 10.5703C20.3751 10.6048 20.4553 10.6665 20.5374 10.7549ZM10.3251 10.7549C10.3771 10.8107 10.4561 10.9326 10.488 11.0532C10.5645 11.3209 10.5328 11.5546 10.5271 11.5965L10.5263 11.6026C10.5229 11.6352 10.4893 11.6358 10.4893 11.6358L9.21415 11.6346C9.22232 11.8282 9.26837 11.9655 9.36271 12.0589C9.45454 12.1501 9.60121 12.2084 9.79864 12.2087C10.0751 12.2093 10.2071 12.1587 10.2974 12.1241L10.3223 12.1147C10.3223 12.1147 10.3577 12.1018 10.3706 12.1366L10.4536 12.3701C10.4705 12.4096 10.4571 12.4234 10.443 12.4312C10.363 12.4754 10.1691 12.5575 9.80082 12.5587C9.62187 12.5591 9.46613 12.5334 9.33794 12.4838C9.20882 12.4341 9.10103 12.3626 9.01734 12.2714C8.93337 12.1808 8.87132 12.0715 8.83245 11.9473C8.79389 11.8242 8.77446 11.6872 8.77446 11.5402C8.77446 11.3958 8.79358 11.2588 8.83055 11.1332C8.86753 11.0069 8.92582 10.8956 9.00323 10.8022C9.08063 10.7085 9.17936 10.6333 9.29687 10.5781C9.41407 10.523 9.55886 10.4963 9.71775 10.4963C9.8544 10.4963 9.97911 10.5258 10.0832 10.5703C10.1628 10.6048 10.243 10.6665 10.3251 10.7549ZM6.77214 11.253C6.85237 11.253 6.91944 11.2552 6.97115 11.2589C6.97115 11.2589 7.07175 11.268 7.18144 11.2837V11.2297C7.18144 11.0599 7.14603 10.9794 7.07646 10.9261C7.00502 10.8712 6.8991 10.8437 6.76119 10.8437C6.76119 10.8437 6.45095 10.8396 6.20556 10.9731C6.19426 10.9797 6.18455 10.9835 6.18455 10.9835C6.18455 10.9835 6.15414 10.9941 6.14286 10.9628L6.0526 10.7202C6.03881 10.6851 6.06387 10.6694 6.06387 10.6694C6.17858 10.5798 6.45718 10.5259 6.45718 10.5259C6.54932 10.5074 6.70319 10.4942 6.79879 10.4942C7.05356 10.4942 7.25068 10.5535 7.3845 10.6707C7.51895 10.7882 7.58726 10.9778 7.58726 11.2335L7.5879 12.3997C7.5879 12.3997 7.59041 12.4335 7.55874 12.4413C7.52908 12.4494 7.4993 12.457 7.46942 12.4642C7.42681 12.4739 7.27325 12.5049 7.14821 12.5263C7.02191 12.5479 6.89154 12.5585 6.76086 12.5585C6.63675 12.5585 6.52331 12.547 6.42333 12.5241C6.32181 12.5012 6.23436 12.4633 6.16354 12.4116C6.0921 12.3599 6.03601 12.2928 5.99714 12.2123C5.95827 12.132 5.93885 12.0339 5.93885 11.9211C5.93885 11.8102 5.96173 11.7111 6.00686 11.6271C6.0515 11.5438 6.11477 11.4718 6.19175 11.4168C6.26885 11.3617 6.35848 11.32 6.45813 11.2934C6.55716 11.2667 6.66278 11.253 6.77214 11.253ZM17.2369 10.5561C17.2454 10.5592 17.2657 10.573 17.256 10.6019C17.2441 10.6366 17.1821 10.8112 17.1601 10.8695C17.152 10.8917 17.1382 10.9068 17.1138 10.904C17.1138 10.904 17.0404 10.8868 16.9737 10.8868C16.9273 10.8868 16.8618 10.8927 16.8026 10.9109C16.7446 10.9287 16.6916 10.9604 16.6449 11.0055C16.5985 11.051 16.5609 11.1143 16.5334 11.1933C16.5052 11.2732 16.491 11.4004 16.491 11.5279V12.4781C16.4911 12.4884 16.487 12.4983 16.4798 12.5055C16.4726 12.5128 16.4628 12.517 16.4525 12.517H16.1175C16.0962 12.517 16.0786 12.4995 16.0786 12.4781V10.5762C16.0786 10.5545 16.094 10.5373 16.1153 10.5373H16.4421C16.4635 10.5373 16.4788 10.5545 16.4788 10.5762V10.7313C16.5277 10.6658 16.6155 10.6081 16.6944 10.5724C16.7741 10.5367 16.8631 10.5097 17.0232 10.5194C17.1069 10.5248 17.2153 10.5477 17.2369 10.5561Z" fill="#479FDA"/>
                                                                 </svg>}
  />

  <Card
    title="Segment"
    href="/integrations/segment"
    icon={<svg className="h-8 w-8"
                                                                       width="100"
                                                                       height="100"
                                                                       viewBox="0 0 90 90"
                                                                       fill="none"
                                                                       xmlns="http://www.w3.org/2000/svg">
                                                                  <g id="b2b0aac9-bfe7-47c1-8033-08dd00eeee5c" data-name="Layer 1">
                                                                   <rect className="b53154be-f3fc-4f62-a1f7-fe24ef3a9b96" x="32.8171" y="28.8538" width="52.2503" height="9.0638" rx="1.6853" fill="#52bd94">
                                                                   </rect>
                                                                   <rect className="b53154be-f3fc-4f62-a1f7-fe24ef3a9b96" x="0.4877" y="51.5052" width="52.2503" height="9.0638" rx="1.6853" fill="#52bd94">
                                                                   </rect>
                                                                   <path className="bd3fb54f-8d44-4644-ac64-7058d6d89eab" d="M6.7614,35.0584a1.6992,1.6992,0,0,0,2.0528-1.1545A35.6595,35.6595,0,0,1,50.482,9.9028,1.6712,1.6712,0,0,0,52.44,8.6873l1.4747-5.5039a1.6954,1.6954,0,0,0-1.2817-2.0879,44.7263,44.7263,0,0,0-52.56,30.39,1.6775,1.6775,0,0,0,1.1849,2.0978Z" fill="#52bd94">
                                                                   </path>
                                                                   <path className="bd3fb54f-8d44-4644-ac64-7058d6d89eab" d="M78.8125,54.3644A1.699,1.699,0,0,0,76.76,55.5188,35.659,35.659,0,0,1,35.0919,79.52a1.6714,1.6714,0,0,0-1.9576,1.2155L31.66,86.2394a1.6954,1.6954,0,0,0,1.2817,2.0879,44.7263,44.7263,0,0,0,52.56-30.39,1.6774,1.6774,0,0,0-1.1849-2.0978Z" fill="#52bd94">
                                                                   </path>
                                                                   <circle className="b53154be-f3fc-4f62-a1f7-fe24ef3a9b96" cx="68.613" cy="13.9321" r="4.9695" fill="#52bd94">
                                                                   </circle>
                                                                   <circle className="b53154be-f3fc-4f62-a1f7-fe24ef3a9b96" cx="16.9592" cy="75.4907" r="4.9695" fill="#52bd94">
                                                                   </circle>
                                                                  </g>
                                                                 </svg>}
  />

  <Card title="Slack" href="/integrations/slack" icon={<svg className="h-8 w-8" height="256" preserveAspectRatio="xMidYMid" viewBox="0 0 256 256" width="256" xmlns="http://www.w3.org/2000/svg"><path d="m53.8412698 161.320635c0 14.831746-11.9873015 26.819048-26.8190476 26.819048-14.831746 0-26.8190476-11.987302-26.8190476-26.819048s11.9873016-26.819048 26.8190476-26.819048h26.8190476zm13.4095239 0c0-14.831746 11.9873015-26.819048 26.8190476-26.819048 14.8317457 0 26.8190477 11.987302 26.8190477 26.819048v67.047619c0 14.831746-11.987302 26.819048-26.8190477 26.819048-14.8317461 0-26.8190476-11.987302-26.8190476-26.819048z" fill="#e01e5a"/><path d="m94.0698413 53.6380952c-14.8317461 0-26.8190476-11.9873015-26.8190476-26.8190476 0-14.831746 11.9873015-26.8190476 26.8190476-26.8190476 14.8317457 0 26.8190477 11.9873016 26.8190477 26.8190476v26.8190476zm0 13.6126985c14.8317457 0 26.8190477 11.9873015 26.8190477 26.8190476 0 14.8317457-11.987302 26.8190477-26.8190477 26.8190477h-67.2507937c-14.831746 0-26.8190476-11.987302-26.8190476-26.8190477 0-14.8317461 11.9873016-26.8190476 26.8190476-26.8190476z" fill="#36c5f0"/><path d="m201.549206 94.0698413c0-14.8317461 11.987302-26.8190476 26.819048-26.8190476s26.819048 11.9873015 26.819048 26.8190476c0 14.8317457-11.987302 26.8190477-26.819048 26.8190477h-26.819048zm-13.409523 0c0 14.8317457-11.987302 26.8190477-26.819048 26.8190477s-26.819048-11.987302-26.819048-26.8190477v-67.2507937c0-14.831746 11.987302-26.8190476 26.819048-26.8190476s26.819048 11.9873016 26.819048 26.8190476z" fill="#2eb67d"/><path d="m161.320635 201.549206c14.831746 0 26.819048 11.987302 26.819048 26.819048s-11.987302 26.819048-26.819048 26.819048-26.819048-11.987302-26.819048-26.819048v-26.819048zm0-13.409523c-14.831746 0-26.819048-11.987302-26.819048-26.819048s11.987302-26.819048 26.819048-26.819048h67.250794c14.831746 0 26.819047 11.987302 26.819047 26.819048s-11.987301 26.819048-26.819047 26.819048z" fill="#ecb22e"/></svg>} />
</CardGroup>

## Send data from Frigade

In addition to using the official integrations listed above, you can write Frigade events to any platform that supports ingesting webhooks. See the [Webhooks](/api-reference/webhooks) documentation for more information.


# Posthog
Source: https://docs.frigade.com/integrations/posthog



Frigade supports sending events to Posthog. The following guide will help you set up this integration in just a few steps.

## Sending events to Posthog

Frigade can read and write data to most modern analytics and CDP platforms. To connect Posthog to Frigade, open the [Integrations](https://app.frigade.com/integrations) page in the Frigade dashboard and click the "Connect" button.
You will need your Posthog API key, which you can find in your [Posthog settings](https://app.posthog.com/project/settings) as well as your Posthog instance URL.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9cfdcb084ead8cf77cb44421b03cfe38" data-og-width="3106" width="3106" data-og-height="1776" height="1776" data-path="images/integrations/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7ab1f96ac1e4c54dc18ae33bf8d0f88c 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=50be02071b773e204d8a6ea58a3b6e39 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4defa9a2e689018355b64671129b49cc 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3fffb24e60feff80877f0c7beae82304 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f63e2f3404243e8ef32d55a369d8a72e 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=63ae0fb4d2e02604ff6d7c923064f7b4 2500w" />
</Frame>


# Salesforce
Source: https://docs.frigade.com/integrations/salesforce



Frigade supports syncing data with Salesforce. For instance, when a User completes a Survey or a step in a Checklist, Frigade will send this data to Salesforce to the matching contact.

<Info>
  Frigade will only send data to Salesforce if the User has an email associated with them. To associate an email with a User, see the [useUser hook](/sdk/hooks/user) or the [User API](/api-reference/users).
</Info>

# Sending Frigade data to Salesforce

<Steps>
  <Step title="Connect Salesforce to Frigade">
    To get started, open teh Frigade Dashboard and navigate to the **Integrations**. Click **Connect** on the Salesforce integration.
    This will prompt you to connect your Salesforce account to Frigade using OAuth.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=64c4a27586506203b6660272f7d5bc02" alt="Salesforce Connect" data-og-width="1541" width="1541" data-og-height="1111" height="1111" data-path="images/integrations/salesforce/connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a9e1a7907b65616a490cb950366cbd97 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e8c031b93a3e23a4b93fdebbfe4c2c7e 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ac705328a2ad529d2bbc47ee51b17a02 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=73232bf2e64e514fb5186b2d565615a8 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9acdfde30d0ac9b4ba7ee3b347b7eb07 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e0c1e6629aaeb1a3fef86fb072174eed 2500w" />
  </Step>

  <Step title="Specify data to sync">
    After connecting Salesforce, you will have the option to specify which data you would like to sync to Salesforce.
    By default, Frigade will only send Step and Flow completion events to Salesforce along with the associated metadata. For example, when a User completes a Survey or a step in a Checklist, Frigade will send this data to Salesforce for the corresponding contact.
  </Step>

  <Step title="Test the integration">
    You can test the integration by completing a Flow or a Step in a Flow. Once the Flow is completed, you can check Salesforce to see if the data has been synced.
    In the example below, a contact completed and NPS Survey and the data was synced to Salesforce:
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=0169375f028c93cbe83de9dfc869f5c8" alt="Salesforce Data" data-og-width="1541" width="1541" data-og-height="1111" height="1111" data-path="images/integrations/salesforce/data.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b60ba677bd6e37eb6762fd6689fb8085 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6530779f7c9c6748b33272203e4e58a5 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7ad5e26ccad567ec298854a3ae997f49 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=eb8dac2c8bfe83b4d26b22bdb58f3f60 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=28cfdd7dd882fa0db300bf14e99d72b1 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5d852e6570bace6a27dfac1bd6a0a8ca 2500w" />
  </Step>
</Steps>


# Segment
Source: https://docs.frigade.com/integrations/segment



Frigade supports bidirectional reads and writes from Segment. This guide shows you how to get started in a few minutes.

## Sending Segment data to Frigade

You can set up Frigade as a destination for Segment identify, group, and track calls by using [Webhooks as a destination](https://segment.com/docs/connections/destinations/catalog/webhooks/).

<Steps>
  <Step title="Add webhook destination">
    Log in to your Segment account, open workspace, and select source. Click on **Add Destination** and search and select **Webhooks**.

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6c5d04e248ea13e47275a49a41d29b99" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1809bc76e0407eca23b3fc89d23f9bba 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e5cedf6f3d7a1fa47f679c768187ab11 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f92f058339b662308b2fc1eeae887477 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5e92d1218c6d1f7f7377063d32916b94 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a876572c6528a045de75b9e97d76ba77 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-1.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=fb053803703463dd26ebd6232369df61 2500w" />
  </Step>

  <Step title="Create mapping">
    Next after creating the destination, click the **Mappings** tab and add a new mapping:

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=37908f8bb79f582c9e09cf06ee257573" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=fdbe0c9849b0bb87c413ff69c2f7113c 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=140fc5f0d2a17cca32d2636a9f53eb61 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=79b87d5c14113ccfd3cbe2a0f1c514c0 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8b2d1b25ba3c476fb2e7e528de875422 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1f7e8a2a6f829efa815a8ba014e4982d 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-2.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=bb0c2606c3750e1215ccf9566ad1b790 2500w" />
  </Step>

  <Step title="Select event types to send to Frigade">
    Select the event types you want to send to Frigade. In this example we select identify, group, and track, but you can select any event type you want to send to Frigade.

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8f7a0d6cbeec26ee36566068af74cdcd" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=737ff2bc8a46d8b326f38aebf09eba03 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=091c97443415b8686caf731536872b8e 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=38e705746f29870c376ad8bbe0ceeea8 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b31e9bdc9e3bda73861deb8bae47f888 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7168293f36ca38d1b9597a8d2bed660a 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-3.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e6be6b484bf9752db845ac18c858d920 2500w" />
  </Step>

  <Step title="Add Frigade Webhook URL">
    Fill out the **Select mappings** as shown below using:

    * `https://api.frigade.com/v1/thirdParty/cdp/segment` as the URL
    * `POST` as **Method**
    * `100` as **Batch Size**. Note: if you send fewer than 500 events per day, it is recommended to set this to a lower value to avoid delays in sending events to Frigade.
    * Your secret Frigade API key (it will be the one prefixed with `api_private`). This key can be found in the dashboard under [API Keys](https://app.frigade.com/developer). Make sure to prefix it with `Bearer` as shown in the screenshot below.
    * `Authorization` as the key

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=dc4edba3b13ba6b5c78facb695706ac5" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=74c8ef7d60b93c3a77e2a8e72e57c768 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c752865c5f981c719b6fcd8358301150 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e355f97b587b1ee887105712ace02e36 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=313bfb747eccb7239f0a9b0ca324ffdb 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3731190ba1ab9fb5e5bef057d8fdbc16 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-4.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a328960feef324359131c4894139c1ba 2500w" />

    Finally, set **Enable Batching?** to **Yes**. Optionally, you can send a test event to verify that the webhook is working. Click **Save** to save the webhook.
  </Step>

  <Step title="Turn on the webhook">
    Finally, turn on the webhook by turning on the mapping you just created. Then, open the **Settings** tab and enable the Destination.

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1f8e9228b06b13d248042ad2d3064ca1" className="rounded" data-og-width="1684" width="1684" data-og-height="1255" height="1255" data-path="images/segment-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=4d4e3aded498252853a59f92ca437269 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9ef86f56b3385aaba37429d2615a5967 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=86604375a57fe8b11099a243ce1db124 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7c2c1e857ba5620c295b5c7549d6f29c 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6e8d62ed25f1d4c4800355861a6b40f2 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-5.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1a3151c991056b55895ae3dc409dab08 2500w" />

    Congratulations! You have successfully set up Frigade as a destination for Segment. You can now use Frigade's [Targeting](/platform/targeting) with your Segment data to create personalized experiences for your users.
  </Step>
</Steps>

## Sending Frigade data to Segment

Frigade also supports sending user and organization events from Frigade Flows to Segment.

<Steps>
  <Step title="Add your Segment write key">
    To send events to your Segment instance, select **Add Source** and then **HTTP API**. Then, copy your Segment write key.

    <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c6d0bb8874625bae5100bbbcd37596c7" className="rounded" data-og-width="3976" width="3976" data-og-height="2282" height="2282" data-path="images/segment-write.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=478cc2c4994e76c9879a4b2123c84e1f 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7124659f327b2de8af844101e1593afb 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e9a846fa67a615b34254c6cc6fc06912 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7ee00f7a5c677aabc22a60bf39be3681 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=73821ba39d63f4a511f571c3f6353ac4 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/segment-write.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=0a1b0fafef7df29475bfbd44efcd06a3 2500w" />
  </Step>

  <Step title="Add Segment in Frigade">
    Next, go to your Frigade dashboard and select **Integrations**. Click **Add Integration** and select **Segment**.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=15a5d94a542b9074e18bf200613df52c" data-og-width="3160" width="3160" data-og-height="2036" height="2036" data-path="images/integrations/segment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b372f84acf63933f73b99946fd5c60d1 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=60e74e8a80fbd827ec58e9522c5c3f45 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7e1ef4f3354da4f62617489b4585047e 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ac150e42e3b3a0361afb8d1829804b00 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6357afa214216430b3ef6c1b043f1d9c 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/segment.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3f1c04a320032462800ced06002a1bdd 2500w" />

    You will be asked to enter your Segment write key. Click **Connect** to save the integration. Shortly after, events will start streaming from Frigade in real-time.
  </Step>
</Steps>


# Slack
Source: https://docs.frigade.com/integrations/slack

Easily send messages to a Slack channel when users take actions in your Flows

<Steps>
  <Step title="Create a Slack Workflow">
    In Slack, open the Workflow page by searching for **Workflows** in the search bar and click the **Create a Workflow** button. Then, choose the **From a webhook** option:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=444b970032ad05b7f12e1732751e7b32" className="rounded" data-og-width="1527" width="1527" data-og-height="991" height="991" data-path="images/integrations/slack/slack-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d729bb593121dfc4f5a55df84be7d93b 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8e9d4a579e3395c0b040078ac68d3efb 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8529485aea7b994eae2c640c28620825 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=96aa4f3920c1668218f234ca8a2406ae 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b816132834b53d43cfc6819c70429699 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-1.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6922ad09e7f333019d753bacad64c946 2500w" />
  </Step>

  <Step title="Create a webhook in Frigade">
    Copy the **Webhook request URL** from Slack. Then press **X**.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4639bf93ecd7922928b3a16b12b2253e" className="rounded" data-og-width="1527" width="1527" data-og-height="991" height="991" data-path="images/integrations/slack/slack-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7907ecbe0ed61f88636102ee1edc9c29 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=dc33ab6d9e8bc512e98a5d7c0ecbd152 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=92512e6bb215e55069b284c266b4764d 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8225c4a03a425504a36cab67d76a5aa4 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=08dc5dfaab9b41f0a92c589537cb7b85 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-2.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=352505861be56530fddf553e586861d2 2500w" />

    In the Frigade dashboard, navigate to the **Developer** section and click on **Webhooks**. Click the **New webhook** button and fill in the details as shown below with your Flow of choice. In this example, we use a simple [Form Flow](/component/form):

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=764dd1db37fc89d5f4637c8d584d79de" className="rounded" data-og-width="1527" width="1527" data-og-height="989" height="989" data-path="images/integrations/slack/slack-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8363b342921a539056096f0faed479a3 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5e4feb5ce3796f9bc71038251e1ad162 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=859aa2f1d252e3c4140de770ac2bb920 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=54a3d0ae0dfb1c937a7c39d80bb157cb 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ec00b9b7b05f2e24fd9fca4a0c9c4489 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-3.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b3dd1a3b1df2d4b4b05a665d83ca7011 2500w" />

    <Tip>You can use a free service such as [Webhook.site](https://webhook.site/) to test your webhook.</Tip>
  </Step>

  <Step title="Set up data variables in Slack">
    In the Slack Workflow, click the **Starts with a webhook** card at the top and add the variables you'd like to send in your Slack message as seen below:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=98dec1e271f438a948e44e1fe2041430" className="rounded" data-og-width="1527" width="1527" data-og-height="991" height="991" data-path="images/integrations/slack/slack-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=88fc089d9017f45f8b962ef6e53687bc 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=80b4350bf3afaaf3843a38511f3029f5 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=293ee4c14eb31a124502fa91e3483fd6 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=54588c4adc5febd042221c99bdae923b 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=98b5ce32b4df544de7ff49310a18c1c2 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-4.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b78056f6181ad0292d848ecf04519d2b 2500w" />

    By default Frigade sends `user__email` and `user__name` for the given user if the data has been [provided in the SDK](/sdk/hooks/user). In this case, we also want to send the value of the `message` field from the Form Flow. To do this, we add a new variable `data__data__message` to map it to the field. You can target any field in a Frigade Form by prefixing the variable name with `data__data__`.
    <Tip>Select and radio form inputs will include both the label and the value in the webhook.  Therefore, if your field is named `industry` you should use `data__data__industry__label` to get the label or `data__data__industry__value` to get the value.</Tip>
  </Step>

  <Step title="Send a message to a Slack channel">
    Add a new step to the Slack Workflow by clicking the **Messages** link in the right menu. Then pick your channel of choice and add the variables you'd like to send in your Slack message as seen below:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=45412088fcf18852d58fd4db68a191f8" className="rounded" data-og-width="1395" width="1395" data-og-height="928" height="928" data-path="images/integrations/slack/slack-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f3bd76dc02e793a179e7b3ca73dbb15e 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3bb825b8427d71b0e2c370ea892f05f1 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4d57412dd190836ceb6395822386fe4b 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b4a4b3ef72c79f18509f0eebcf51d941 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=01cd392315bb5ce28b4a09793a2b6cf0 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-5.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e59a6a63c56900cc57608c534538dbfb 2500w" />

    Finally, hit the **Publish** button in the top right corner to make your Slack Workflow live.
  </Step>

  <Step title="Test your Slack integration">
    You're now all set to test your Slack integration. In your application, complete the Flow you've set up the webhook for. In this case, we'll submit the Form Flow:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e0321d0946bd2e98db4bdef6501e2ed7" className="rounded" data-og-width="1527" width="1527" data-og-height="989" height="989" data-path="images/integrations/slack/slack-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d01c65a5d3b5149f275eb00589041147 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3fe983e115c0ceca3a1b84b848078b70 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b2cc8317d0d3bf064b35131ce39cb309 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fd0fd635b1e95f4ae35b2d55cab88411 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6141cde5fca85748b9d071df692b8b14 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-6.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d51b2c9843f55174f84d2e4557760a12 2500w" />

    After completing a step in the Frigade Flow, you should now see the following show up in your Slack channel:

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=20a317d919e06793f1185fdbdc75ab55" className="rounded" data-og-width="1396" width="1396" data-og-height="926" height="926" data-path="images/integrations/slack/slack-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fcf51fb4276ec45379126976516003c9 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5ac7ae9f4b728a491a8930645e62d7a8 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=52238002dc08e042d3ea9aeadcbc34c5 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=636685666c2a5366d19a30f58cd3ab42 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4f4e2632fd2a35995ede4d949af19f13 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/slack/slack-7.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=650491572d525b4f85cf63cf75a14193 2500w" />
  </Step>
</Steps>

That's it! You've successfully integrated Slack with Frigade. Remember, Frigade webhooks are unique for the Development and Production environments, so make sure to create a new webhook for each environment you want to integrate with Slack.

# Example

If you want a new Slack message when a user provides an NPS score in a Frigade Form, you can set up a webhook in Frigade and a Slack Workflow as follows:

1. Create a new workflow in Slack and copy the Webhook URL.
2. Create a new webhook in Frigade and paste the Slack Webhook URL.
3. Pick **Flow completed** and **Flow dismissed**.
4. Add the variables `data__nps-score-page__nps-score` (for the NPS Score) and `data__nps-feedback-page__nps-feedback-text` (for the NPS Comment) to the Slack Workflow.
5. Craft a message and pick a channel to send the data to.


# Frigade Engage Documentation
Source: https://docs.frigade.com/overview

Product growth and onboarding for modern software companies

<Note>
  You're currently viewing the documentation for Frigade Engage. The documenatation for the Frigade Assistant is not yet publicly available. Head over to <a href="https://frigade.com" className="font-bold">frigade.com</a> to learn more.
</Note>

[Frigade Engage](https://frigade.com/engage) helps teams build better user onboarding experiences. Use Frigade to guide users through your product, educate them about its features, and drive them toward key actions.

<video autoPlay muted controls loop playsInline className="w-full aspect-video" src="https://cdn.frigade.com/59e1ae3b-54f6-430f-9dec-7ab0d308924b.mp4" />

## Why Frigade Engage?

***

* **Developer experience:** Best-in-class developer experience with a flexible API, thoughtful developer documentation, and an easy-to-use admin dashboard.
* **Native components:** High-quality UI components for checklists, tours, and more; supports building custom Flows and blends in seamlessly with your product and brand.
* **Platform:** A powerful platform with targeting, analytics, and state management built-in; leverage Frigade instead of building and maintaining your own onboarding infrastructure.
* **Collaboration:** Frigade offers both code and no-code based approaches for launching new Flows and a suite of tools for non-engineers to make updates from the web.

## Getting Started

***

<CardGroup cols={3}>
  <Card title="Quickstart Guide →" href="/quickstart" horizontal={true}>
    Add a Flow to your product in less than 5 minutes.
  </Card>

  <Card title="No-Code Guide →" href="/platform/collections" horizontal={true}>
    Use Collections to ship Flows without code.
  </Card>

  <Card title="Get in touch →" href="https://cal.com/team/frigade/frigade-demo" target="__blank" horizontal={true}>
    Question? We're here and happy to help.
  </Card>
</CardGroup>

## Overview

***

### Flows

[Flows](/platform/flows) are the main building blocks of Frigade Engage. Flows can power product announcements, set up guides, product tours, or even custom flows. Flows have built-in state management, versioning, analytics, and validation to make it easy to build and collaborate.

### Components

Flows power [components](/component/overview) inside your codebase. We offer high quality, pre-built UI components to ship faster e.g. `<Frigade.Announcement />`, `<Frigade.Tour />`.

Components are embedded in your product natively. You can style Frigade components with your design system, themes, or custom CSS. You can also build custom Frigade components.

### Admin Dashboard

The web [admin dashboard](/platform/overview) helps you manage your Flows and users. You can create, edit, and delete Flows, view analytics and user progress, and make updates to your in-app experiences.


# Analytics
Source: https://docs.frigade.com/platform/analytics

Frigade provides analytics and connects to external analytics platforms

## Built-in Analytics

***

Frigade provides built-in funnel analysis to help you understand the performance of your Flows. Frigade will automatically track how many users have interacted with a Flow and how many have completed it. You can also see how many users have dismissed or quit a Flow.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f632aa1260d214f0364db81a4566f739" alt="Analytics" data-og-width="3106" width="3106" data-og-height="1776" height="1776" data-path="images/platform/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=72d6dc8a6477300becc5350f3e5e7ce0 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=da579b6f77d2c7d1fd7f2811ff551df8 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fbd93eac453fa2084d86b9c93f7a0a46 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4566eb22a43927ab822444ce9880d93b 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8915b788cbdaa7d148e5968e2154f453 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=65a9008f491bdeb74916b03e2ca902cb 2500w" />
</Frame>

### Flow cohorts

Frigade analytics are based on user cohorts. Frigade will group users into daily cohorts based on the date they first interacted with the Flow.

You can see detailed breakdowns by hovering on any given day in the graph. Statuses include completing the Flow, dismissing or quitting the Flow, or not yet completing the Flow.

### Time windows

You can change the time range for the stats by clicking on the dropdown in the top right corner of the analytics page. You can choose between `Last 7 days`, `Last 30 days`, or `All time`. The metrics on the right side represent the totals for the selected time window, and the graph and step completion rates below will also adjust to the selected time window.

### Flow versions

Each time a new [version](/platform/versioning) of a Flow is published it will its own analytics. This allows you to review the performance of different versions of the same Flow over time.

## External Analytics

***

You can send Frigade tracking events to an external analytics platform for dashboards and reporting. Check out the [integrations](/integrations/) section to see our supported platforms.

Additionally, you can always connect Frigade to the analytics platform of your choice using webhooks. See the [webhooks](/api-reference/webhooks) documentation for more information.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9cfdcb084ead8cf77cb44421b03cfe38" alt="Groups" data-og-width="3106" width="3106" data-og-height="1776" height="1776" data-path="images/integrations/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7ab1f96ac1e4c54dc18ae33bf8d0f88c 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=50be02071b773e204d8a6ea58a3b6e39 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4defa9a2e689018355b64671129b49cc 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3fffb24e60feff80877f0c7beae82304 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f63e2f3404243e8ef32d55a369d8a72e 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=63ae0fb4d2e02604ff6d7c923064f7b4 2500w" />
</Frame>


# Collections
Source: https://docs.frigade.com/platform/collections

Launch Flows and set cool-offs without code

Collections are **reusable in-app UI channels** to launch Flows without code. Once embedded and styled, Collections can house and display new Flows without code updates. This is especially useful for product teams who want to templatize Flows and enable non-technical teammates to launch them (e.g. product announcements).

Collections also provide **governance and orchestration** through air traffic control functionality. This includes controls like limits, cool-offs, and priorities. For example, Collections can determine the frequency and timing of a group of Flows to avoid overwhelming users e.g. only show one announcement per day, space out an in-app upsell campaign.

## Launch with Collections

***

#### Announcements, Surveys, and Dialogs

Frigade comes with a default Collection called <strong>Dialogs</strong>. The Dialogs Collection is built-in to the Frigade SDK and can be used to launch Frigade Announcements, Surveys, and other Dialog-based components without updating your product codebase.

<Steps>
  <Step title="Install the Frigade SDK">
    To add a new dialog-based component to your product, first make sure the Frigade Provider is properly installed in your product. This is also where you can add custom CSS for your dialog components.

    ```jsx  theme={"system"}
    import * as Frigade from "@frigade/react";

    const FRIGADE_API_KEY = "api_public_abcd1234";

    export const App = () => {
      const userId = "...";

      return (
        <Frigade.Provider
            apiKey={FRIGADE_API_KEY}
            userId={userId}
            css={{
            '.fr-announcement': ANNOUNCEMENT_CSS,
            }}>
            {/* ... */}
        </Frigade.Provider>
      );
    };
    ```
  </Step>

  <Step title="Create a new Dialog Flow">
    Next, create a new dialog-based Flow (e.g. Announcement, NPS Survey, Tour) in Frigade. Customize this Flow with your content and targeting logic.
  </Step>

  <Step title="Add the Flow to the Dialog Collection">
    Finally, add the Flow you just created to the Collection via the <strong>Add Flows</strong> button in the Collection detail page. From here, you can also control the cool-off and priority of included Flows.

    <Frame>
      <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-detail.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3277ae76b92069f088827ce590f63160" alt="Collections" data-og-width="3456" width="3456" data-og-height="1996" height="1996" data-path="images/platform/collections-detail.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-detail.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1215ff0be09816f92104d8905983d57a 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-detail.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5a9563a2a781491765f2a81e94b6f910 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-detail.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7d6a899dc8627bf803c595234b20d968 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-detail.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7a64f6f5a8829b7fb7562c4cd1c7aa7a 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-detail.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=064139fe2c821ab63df81a9c2697f172 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-detail.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=95c2c42c7e6898efb5ba926af2a71906 2500w" />
    </Frame>

    <Note>A Flow can display for eligible users immediately after being added to a Collection in Production</Note>
  </Step>
</Steps>

#### Inline UI Components

You can also use Collections to launch new Flows that are embedded directly into your product UI with no-code.

<Steps>
  <Step title="Create a New Collection">
    To start, create a new Collection in the Frigade dashboard.
  </Step>

  <Step title="Restrict the Flow Types">
    Next, we recommend restricting the Flow types to only what you plan to support for this in-app channel e.g. Banners, Cards, etc. This prevents accidentally adding Flows to an embedded Collection that do not fit the intended space.
  </Step>

  <Step title="Embed and Style the Collection">
    Next, grab the install snippet for the Collection and place it in your product codebase where you want the in-app channel to live. You can also style the Collection with custom CSS.

    ```jsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Collection collectionId="collection_4jDCTYUm" css={NAV_CARD_CSS}/>
      );
    };
    ```
  </Step>

  <Step title="Create and Add a Flow to your Collection">
    Finally, create a Flow and add it to the Collection. Depending on the Flow targeting and Collection priority, the Flow will begin to go live to eligible users.
  </Step>
</Steps>

## Creating a Collection

To create a Collection, visit the Collections page in the Frigade dashboard and click on the **New Collection** button. You will be prompted to enter a name and description for the Collection. Once created, you can access the embed snippet, set the display logic, and add Flows to the Collection.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d58510929dba831e648753a6b5c46768" alt="Collections" data-og-width="3456" width="3456" data-og-height="1996" height="1996" data-path="images/platform/collections.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=be7a3307c6de574c26ef2c4430fe494e 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=0c23a69c27ec192e04971a0446f67a6c 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2592ec8ad58825b82627a6bb46f06ee9 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=92f637d84b18327f3fd26b13f6f35329 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3655309736ebc8c81e8706351530eeab 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d8ac77e143847a6b89dfe9ae90c5e5b9 2500w" />
</Frame>

## Ordering Flows

You can specify the priority of Flows within the Collection by dragging and dropping them in **Flow priority** section of the Collection detail page. This is useful for prioritizing content types (e.g. onboarding > upsells > research) or sequences (welcome > getting started > go deeper).

<Accordion title="Flow ordering in Collections">
  <Warning>
    <b>Note:</b> Collections do not guarantee Flows will be shown in that order.
  </Warning>

  Flows may still be shown out of order if they are triggered out of order. Collections
  are used to resolve priorities when multiple Flows are eligible to be shown at
  once. If you need to ensure an exact order, you can combine Collections with [Flow
  targeting](/platform/targeting) to ensure users have completed another Flow first
  or any other criteria.
</Accordion>

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-reorder.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=dbd7e8c7357ca7bcfa3aa330c22f3119" alt="Collections" data-og-width="3456" width="3456" data-og-height="1996" height="1996" data-path="images/platform/collections-reorder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-reorder.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=479be407899b2d7f64e810c57be8b208 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-reorder.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6a9a7a9f76188438fca817ab8f0b8039 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-reorder.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=80b074cf5ae284fbbdfc64a2c9290985 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-reorder.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9b2b24ed01f140f77fffa8ea1cbf42de 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-reorder.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f3ffd0f7e917e0661b754f96002d4552 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/collections-reorder.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=80004779930245c491caf3d6c116b7b8 2500w" />
</Frame>

## Ordering Collections

Collections themselves can also be ordered via drag and drop on the Collections overview page. Because Flows can belong to multiple Collections, this priority informs the order in which Frigade processes each Collection.

## Combining Collections and Targeting

Collections can and should be combined with [Flow targeting](/platform/targeting) to ensure the right Flows are shown to the right users at the right time.

You can think of Collections as content pools. By giving each individual Flow its own targeting, Collections can then personalize the product experience to each user by choosing the highest priority eligible Flow for them.

## Usecases

***

### Feature adoption

Let's say we have a few different educational in-app sequences to encourage further feature adoption and that a user may be eligible for multiple sequences. For each sequence, we can use Flow targeting to define

1. the eligible audience (e.g. enterprise, free trial, etc.) and
2. the exact order of the sequence (e.g. Flow 1 must be completed to see Flow 2).

If we have defined multiple sequences, we can create a Collection and add all the Flows to ensure that only a single Flow from any campaign can be shown within a desired time frame. This helps ensure that users are not overwhelmed and increases the likelihood that users will engage with the content.

### Product communications

SaaS products often use dialogs and floating UI to communicate and collect important information. For example, an [announcement](/component/announcement) or a [survey](/component/survey/nps). Oftentimes, product teams may accidentally show multiple competing experiences to the same user at the same time.

This can easily be avoided with Frigade. The default Collection called "Dialogs" can house all of our announcements and surveys to spread these experiences out with cool-offs. We can rank these Flows so that onboarding announcements take priority over product updates and user research (or whichever order makes sense for your product).

### Product Upsells

Let's say our product has a free trial experience and we want to nudge users toward upgrading to a paid plan. We can create a Collection called "Upsells" and add our entire catalog of upsell Flows to this Collection (announcements, cards, banners, etc.). We can then set a limit of one per day to ensure we're not overwhelming users with too many upsell messages.

We can define the audience for each Flow to ensure that only users who are actively in a free trial are eligible to be shown the messages. Once a user upgrades, the Flow audiences will prevent them from receiving any further promos in the sequence.

## Frequently Asked Questions

***

<AccordionGroup>
  <Accordion title="How do I get access to Collections?">
    Collections are part of our [Scale plan](https://frigade.com/pricing). You can try out Collections in the Development environment to see if they are a good fit for your product. If you're interested in upgrading to our Scale plan, please reach out to [our team](mailto:support@frigade.com).
  </Accordion>

  <Accordion title="What happened to Rules?">
    Collections are an evolution of what we set out to achieve with Rules and will directly replace them. Collections can still be used like Rules to orchestrate Flows and cool-offs, but they've been upgraded to add the ability to launch Flows with no-code, as well.
  </Accordion>
</AccordionGroup>

<Info>Available in `@frigade/react` version `2.4.17` and above.</Info>


# Dynamic Variables
Source: https://docs.frigade.com/platform/dynamic-variables



Sometimes you want to use a dynamic piece of content within your Flow such as an email address or a localized string for  [i18n](/platform/i18n). In these cases, you can use **dynamic variables** to personalize for each user.

### Setting Dynamic Variables

***

Flows support setting custom variables anywhere in the data defined from the Frigade dashboard with the `${variable}` pattern. For instance,
your Flow might look like this:

```yml  theme={"system"}
steps:
  - id: "announcement-page-1"
  - title: "Welcome to Acme, ${firstName}!"
```

Then using your React component of choice, you can set the `firstName` variable like so:

```tsx  theme={"system"}
<Frigade.Announcement
  ...
  variables={{
    firstName: 'Christian'
  }}
/>
```

Variables can also be added at the global level via the `<Frigade.Provider />`. This will make them accessible in all Flows and [Collections](/platform/collections).
To pass in variables globally, simply pass the `variables` object to the provider:

```tsx  theme={"system"}
<Frigade.Provider
  ...
  variables={{
    firstName: 'Christian'
  }}
/>
```

See the [Provider documentation](/sdk/provider#variables) for more details.


# Environments
Source: https://docs.frigade.com/platform/environments

Frigade supports development and production environments

## Changing environments

***

Frigade environments allow you to manage your Flows across **Development** and **Production**. You can access each environment from the dropdown in the top of the left sidebar.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/environments.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f14c54cdaac6dae0eac5f02b303a40ce" alt="Environments" className="rounded-md" style={{}} data-og-width="1948" width="1948" data-og-height="1146" height="1146" data-path="images/platform/environments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/environments.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f881bf64f226e8efacf3cfb51d160911 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/environments.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9799667369329a055882e8a60e7a5423 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/environments.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8cddac12f537d178e0d214de3a6d4e8d 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/environments.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=227251f64c402168824e8675987f6ae0 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/environments.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=89e07a8bb7e3a6937b1d3240666d4273 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/environments.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=806219d10f2bc79fd5737bb35eaabc00 2500w" />
</Frame>

## Manage Flow across environments

***

By default, Flow IDs are unique to each environment. However, if you want to use the same Flow ID across environments, you can use **Sync to Production** to link a Flow between Development and Production.

### Sync Flows to Production

When you are ready to move a Flow from Development to Production, you can simply **Sync to Production** from the overflow menu on the Flows page. This will create a new Production Flow with the same ID, content, targeting, and properties.

If the Flow ID already exists in Production, then **Sync to Production** will give you the choice to overwrite the Flow or create a new draft version with your changes.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/copy-to-production.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=45ed40403c8282d9fec457578984a053" alt="Environments" className="rounded-md" style={{}} data-og-width="1713" width="1713" data-og-height="962" height="962" data-path="images/platform/copy-to-production.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/copy-to-production.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7d31333fe606711b48f53f14cbd48413 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/copy-to-production.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b2f0d374f8b9a5be3c91bc51b9a6f931 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/copy-to-production.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=94b483b5f39333f93fc7371529559dff 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/copy-to-production.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3fb9dfc1129dfdc0876f1324cb99370c 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/copy-to-production.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=db8e9a53aa8bb1f24b2ebdff46808efd 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/copy-to-production.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e8d86da86c6a3efe441d13bf87993eab 2500w" />
</Frame>


# Flows
Source: https://docs.frigade.com/platform/flows



## What are Flows?

***

Flows are the main building blocks of Frigade. Flows are made up of one or more Steps that you want a user to take. A Flow can be a product tour, a checklist, a form, or any other onboarding experience you can imagine.

Flows comes with built-in content management, version control, and analytics to make it easier to build and collaborate on onboarding.

Users have their own state for each Flow (e.g. started, dismissed, completed), and it is automatically tracked by Frigade. Flows can also track Steps across groups of users, such as companies or teams.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=55e8bc703b8ab4b7eb2ab88744f0a7f6" data-og-width="3696" width="3696" data-og-height="2244" height="2244" data-path="images/platform/flow-detail-editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=2cabf0b9b2df7e673f82283d3f8a5438 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a6be6a39ea113270cefe299fc4939ff3 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7635b4aba7fd32d96fb07a50cee8b829 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=0e027ab9110a817c968646ec1eda944a 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f7beeb294fba262b914a894c934e3047 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=937924267315fd24fa96258d85494640 2500w" />
</Frame>

## User Lifecycle

Users can have state in Flows and in the Steps within a Flow. The lifecycle of a user's state in a Flow is as follows:

1. **Not started**: The user has not seen or engaged with the Flow.
2. **Started**: The user has seen the Flow and may have completed or skipped one or more Steps.
3. **Completed** or **Dismissed**: The user has completed or dismissed the Flow.

Once a Flow is completed or dismissed, it will remain in this state for the user unless the Flow is restarted via the SDK, API, or the **Reset in Flow** button in the Frigade Dashboard. This is true even if the Flow has new Steps added or a Step's state is reset.

## Frequently Asked Questions

***

<AccordionGroup>
  <Accordion title="How do I create a Flow?">
    You can create a Flow by tapping **Create Flow** from the navigation bar or from a component in the [component library](https://app.frigade.com/components/).
  </Accordion>

  <Accordion title="How do I edit a Flow?">
    Flows can be edited by clicking on the Flow name from the Flow overview page. From there, you can edit:

    * Version

    * Name and Description

    * Content (e.g. copy, assets, images)

    * Step logic (e.g. what actions mark a step complete)

    * Step order (e.g. what order content should be shown in)

    * User targeting logic (e.g. which users should see this Flow)

    * Status (e.g. whether the Flow is active or not)
  </Accordion>

  <Accordion title="How do I edit a Flow's YAML configuration?">
    You can edit a Flow's underlying YAML code by clicking the **Advanced Editor** toggle on the Flow detail page.

    <Note>The preview it will not reflect any custom styling you define in your own codebase.</Note>
  </Accordion>

  <Accordion title="How do I preview a Flow?">
    When using a Frigade pre-built UI, you can simply preview the Flow from the Editor tab of the Flow detail page. To see your Flow in your product, you can view your Flow in your staging or production environment.

    If you'd like, you can use targeting to only show it to teammates while building, and you can reset users in the **Users** tab to go through the Flow multiple times.

    <Frame caption="Preview your Flow in real-time in Frigade">
      <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=fc40523ed27e6c6ced0882293f0e7ecc" data-og-width="4598" width="4598" data-og-height="2410" height="2410" data-path="images/platform/editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e10b2892db864e36792081193d199be0 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7985c658200915d98ff903edbd812c34 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7bcbeebc8e05529ab0d9ebbf7e6ab55b 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8a02113fd5d1826db7f4f39444871c2b 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b8567865f7d8035a3d1b63fc83ffeffe 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=0884c324dc8a5a18b4d586b8fd93ebfc 2500w" />
    </Frame>

    <Note>The preview it will not reflect any custom styling you define in your own codebase.</Note>
  </Accordion>

  <Accordion title="What Flow types are there?">
    Frigade supports the following Flow types:

    * [Checklist](/component/checklist/carousel)
    * [Tour](/component/tour)
    * [Form](/component/form)
    * [Announcement](/component/announcement)
    * [Banner](/component/banner)
    * [Card](/component/inline-card)

    You can also build [custom Flows](/guides/custom) using the Frigade SDK.
  </Accordion>

  <Accordion title="Can a group share a Step of a Flow?">
    Yes. Sometimes you want any user in a group to complete a Step on behalf of all the other users in the group (e.g. add a credit card, install an SDK, etc.). This is supported in Frigade through [group properties](/sdk/hooks/group) and [completion criteria](/sdk/advanced/completing-a-step).
  </Accordion>
</AccordionGroup>


# Using HTML in Strings
Source: https://docs.frigade.com/platform/html-in-strings



You can use basic HTML tags to format strings in your YAML Flow definitions. The following tags and attributes are supported:

* `<b>`
* `<i>`
* `<u>`
* `<a href="..." target="...">`
* `<br>`
* `<p>`
* `<img src="..." alt="...">`
* `<div>`
* `<span>`

The `style` and `class` attributes can be used to style all of the above elements.

## Example

```yaml  theme={"system"}
title: This title is <b>really</b> important
```


# Internationalization
Source: https://docs.frigade.com/platform/i18n



Internationalization (i18n) is supported in Frigade through [dynamic variables](/platform/dynamic-variables). Dynamic variables allow you to pass in the string variable in the appropriate language based on the users' locale, settings, etc.


# Admin Overview
Source: https://docs.frigade.com/platform/overview

Easily manage your product onboarding from the admin dashboard

The admin dashboard is where you create and manage your organization's onboarding. It includes our UI component library, Flow management, and analytics on all onboarding activity. The following sections highlight some of the key functionality of the platform.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flows.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=ba9c75b4c2777312bc9fa396f3534523" data-og-width="3508" width="3508" data-og-height="2150" height="2150" data-path="images/platform/flows.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flows.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=bf791869795af435f205f57d87e1a42f 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flows.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a5c4fe312b5c268fd5c589adc3447ca9 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flows.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=838c6c4b13aeede92a1b6fe3900175a2 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flows.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b6792d3c68220579edb7b7d46e54ac8b 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flows.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=211bd01982e6202d4dc1937b79456da6 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flows.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a26f88a27d10bc4bde597301fae827da 2500w" />
</Frame>


# Targeting
Source: https://docs.frigade.com/platform/targeting



Use targeting to personalize Flows to different cohorts of users, seamlessly link multiple onboarding experiences together, and define completion criterias for a Step in a Flow.

## Flow targeting

***

You can optionally add targeting to every Flow you create. You can view and edit this targeting logic on the **Targeting** tab of the Flow detail page. The Flow targeting logic is used to determine who should see the Flow.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3ff629c1598a46737aad2579fcd342b1" alt="Flow Targeting" data-og-width="3456" width="3456" data-og-height="1926" height="1926" data-path="images/platform/flow-detail-audience.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6be15fee4c76d9da2cd14014ff762843 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=59a1aeb9087ce79ce5e731351740b43f 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6430d0069d4fb14ef1a4271bdee6c85f 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=25d1e7ec6bd9d9ffc8fd030b1a05a7f6 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5ad647ada4e6bf57add11f123df68e43 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=d05ba711ef7422ebb937b35ea9b75ad6 2500w" />
</Frame>

### Example use cases

Here are some common ways we see developers using Flow targeting:

* Only show a Flow to newly created accounts
* Show a Flow to users with a certain job function or user property
* Show a Flow to users who have taken a specific action in the product (e.g. an upsell once they use something 10 times)
* Show a Flow to users who have completed another Flow (e.g. a "next steps" Flow after a user completes an initial onboarding Flow)
* Show a Flow only after X days have passed since completing another Flow

<Note>Refer to the users [SDK](/sdk/hooks/user) and [API](/api-reference/users) for more info on using properties and events in targeting</Note>

## Step targeting

***

You can also leverage targeting logic within the Steps of a Flow by using the Advanced Editor.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=614526d567e2202cecc1458859c34581" alt="Step visibility" className="rounded-lg" style={{border: '1px solid #D3D3D3',}} data-og-width="1639" width="1639" data-og-height="596" height="596" data-path="images/platform/flow-detail-yaml-step-visibility.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7fffa9c7035df77c5c64670f32af26b9 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=22ae0823c1ba68267b53f43d5c40c23b 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9723d7b4190517b5666fca65fa66e056 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=081169fc1a9b8a70c4717383eaf3f50c 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1b8e6f3daa1da0d9742c54e19fd5a090 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f801f71c7bbdc48acaa50c03b59f96b0 2500w" />
</Frame>

### Example use cases

Here are some common ways we see developers using Step targeting:

* Mark a Step complete based on a condition [using steps\[\].completionCriteria](/sdk/advanced/completing-a-step#automatically-marking-steps-complete)
* Show or hide a Step based on a condition [using steps\[\].visibilityCriteria](/component/tour#flow-configuration)
* Mark a Step started based on a condition [using steps\[\].startCriteria](/component/tour#flow-configuration)

## User props

***

All data you've made available to Frigade can be used in your targeting logic, including the properties below supported on [users](/sdk/hooks/user). You can also sync with your [existing analytics platform](/integrations/) to leverage [user properties and events](/sdk/hooks/user) you're already tracking.

<ParamField body="user.flow('<flowId>')">User Flow state (e.g. `COMPLETED_FLOW`)</ParamField>
<ParamField body="user.flowStep('<flowId>', '<stepId>')">User Flow Step state (e.g. `COMPLETED_STEP`)</ParamField>
<ParamField body="user.flowStepData('<flowId>', '<stepId>', '<fieldId>')">Data collected from in a specific step (e.g. form data)</ParamField>
<ParamField body="user.event('<eventId>').count">User event count</ParamField>
<ParamField body="user.property('<property>')">User properties</ParamField>
<ParamField body="user.propertyContains('<property>', '<searchString>')">User properties partial match (<Tooltip tip="Not case-sensitive. Returns true or false.">more</Tooltip>). It supports searching in strings, objects, and arrays.</ParamField>
<ParamField body="user.currentUrl()">Current URL of the user</ParamField>

## Group props

***

All data you've made available to Frigade can be used in your targeting logic, including the properties below supported on [groups](/sdk/hooks/group). You can also sync with your [existing analytics platform](/integrations/) to leverage [group properties and events](/sdk/hooks/group) you're already tracking

<ParamField body="group.property('<property>')">Group properties</ParamField>
<ParamField body="group.event('<eventId>').count">Group event count</ParamField>

## Boolean logic and operators

***

Supported operators are: `&&`, `||`, `==`, `!=`, `>`, `<`, `>=`, `<=`, `contains`, `!contains`,  `endsWith`, `!endsWith`, `startsWith`, `!startsWith`, `within`, `!within`

## Examples

***

Here are some examples of some of the most popular targeting logic we see developers using.

#### Relative dates

You can use relative dates in your targeting logic similar to how this is handled in [plain Javascript](https://stackoverflow.com/questions/7763327/how-to-calculate-date-difference-in-javascript).
For example, you can target users who are younger than at least 30 days:

```javascript  theme={"system"}
user.property('accountCreatedDate') within 30d
```

Or target users who are older than 30 days:

```javascript  theme={"system"}
user.property('accountCreatedDate') !within 30d
```

This behavior also works for targeting users who have completed a Flow within as certain time frame:

```javascript  theme={"system"}
user.flow('flow_i6kH7DjcbE6tiaQd') !within 4w
```

#### Property matching

Target a Flow to a user who has connected their bank account:

```javascript  theme={"system"}
user.property('bankAccountConnected') == true
```

#### Check if a property is present

Target a Flow to a user who has a job title:

```javascript  theme={"system"}
user.property('jobTitle') != null
```

#### Absolute dates

Target a Flow only for users signed up after a certain date:

```javascript  theme={"system"}
user.property('accountCreatedDate') > '2023-03-01 00:00:00'
```

#### Flow state

Target a Flow to a user who has completed another onboarding Flow already and has connected a bank account:

```javascript  theme={"system"}
user.flow('flow_i6kH7DjcbE6tiaQd') == 'COMPLETED_FLOW' && user.property('bankAccountConnected') == true`
```

Target a Flow when a Step in another Flow is completed:

```javascript  theme={"system"}
user.flowStep('flow_i6kH7DjcbE6tiaQd', 'my-step-id') == 'COMPLETED_STEP'
```

Target the output of a previous step in the same Flow:

```javascript  theme={"system"}
user.flowStepData('flow_i6kH7DjcbE6tiaQd', 'my-step-id', 'my-field-id') == 'some-value'
```

#### Event counts

If the event properties do not matter and you simply wish to see if a user has triggered an event, you can use the following expression:

```javascript  theme={"system"}
user.event('pageView').count > 0
```

Automatically trigger when a group/organization sends a specific event:

```javascript  theme={"system"}
group.event('connectedBankAccount').count > 0
```

#### Current URL

Target based on the current URL contains a specific string:

```javascript  theme={"system"}
user.currentUrl() contains 'example.com'
```

Target based on the current URL ends with a specific string:

```javascript  theme={"system"}
user.currentUrl() endsWith '?myParam=123'
```


# Users and Groups
Source: https://docs.frigade.com/platform/users-and-groups

Easily manage users and groups as they engage with your Flows

## User Management

***

You can view all of the users interacting with your Flows on the <a href="https://app.frigade.com/users" target="_blank">users</a> page. Users will automatically appear in Frigade once they have been identified in your app (see [SDK](/sdk/hooks/user) or [API](/api-reference/users) docs for more info).

You can see all of the Flows that a user has engaged with and their status for each Flow on the user detail page. This can be especially useful for Customer Success teams to see which customers may be stuck and where.

If needed, you can also reset a user's status for a Flow to allow them to start over. This is an especially helpful feature when developing with Frigade to reset your own Flow status.

### Exporting User Data

You can export your users and their state in a given Flow by clicking the **Export** button on **Users** tab on a Flow detail page. This will download a CSV file with all of the user's data and state in the given Flow. Alternatively, you can use the [API](/api-reference/users/users-get) to fetch user data programmatically or use the [Webhooks](/api-reference/webhooks) whenever a user takes actions in your Flows.

### Standardized User Fields

When sending user properties to Frigade, the platform will automatically decorate the following fields on the user profile:

* `firstName`
* `lastName`
* `email`
* `organization`
* `profilePicture`

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7a218d9c17ffbcb2d6f67c0a842f6565" alt="Users" data-og-width="3456" width="3456" data-og-height="1994" height="1994" data-path="images/platform/users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=517ef6bc15d92776657a8953a4af2a66 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=97bde8fb87ea0c0082a6afea0d884a21 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=227aa3ff5152e2dc650dbc05dc53079e 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=773cdc62a48d84bb5b769ad63c2d6caa 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=efaf9617808beb2a0bce5e864157638e 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=400db77cda1008ae1662e33138f08fc8 2500w" />
</Frame>

## Group Management

***

You can view all of your groups and their associated data on the <a href="https://app.frigade.com/users" target="_blank">groups</a> page. Groups allows you to associate an individual user with a group (e.g. a company, organization, account, project, or team).
Groups will automatically show up in Frigade once they have been identified in your app (see [SDK](/sdk/hooks/group) or [API](/api-reference/groups) docs for more info).

The group detail page will show all of a group's members and where they are in your onboarding Flows. Groups are especially helpful if you have any tasks in your product that are shared across a group of users.

For example, you may want to implement a checklist with a Step that can be completed by any user in the group (e.g. connecting a third party API). You can use groups to ensure once that Step is completed by one user it will be completed for all users.

### Standardized Group Fields

When sending group properties to Frigade, the platform will automatically decorate the following fields on the group:

* `name`
* `imageUrl`
* `website`

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=957acdd5f519204940f3b7f198b4ea68" alt="Groups" data-og-width="3456" width="3456" data-og-height="1994" height="1994" data-path="images/platform/groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7a4fb43d40363ff5644375702bb6479f 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e0c1512862f2a766aa80652411ec2580 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=73f10d589c4c75568125a705875b2386 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=cec457cf4b9558359c3a44d8d2ee2054 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7e10e3ce61a5fc4a8f6b1c9eb11257b1 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c3faa8ccd79a8fd33e5ae8e8588ee008 2500w" />
</Frame>


# Version Control
Source: https://docs.frigade.com/platform/versioning

Manage the rollout of new Flow updates with built-in version control

## Creating a new version

***

To create a new version of your Flow, open the versions panel on the Flow detail page. Then, click the **New version** button.
The new version will remain a draft until you activate it. Frigade supports one draft version at a time. Tap **View** on a version to view and make changes.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1e70232b5fd3e693c31acfcc1b2eb902" alt="Versioning" data-og-width="3013" width="3013" data-og-height="1718" height="1718" data-path="images/platform/flow-detail-versions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=cd6a3874acbf230f0c4d0d328998165e 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=89387955b4eb9246e1f8e89d23819957 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8bf42358bf316a4fccb578e08ab09733 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=ba60cbb46bde545cb678cbb02779c108 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=355d0db45c96ab5b35ccc5da6220178d 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9ae2120c68617a60bbb9aae764a57656 2500w" />
</Frame>

## Activating a draft version

***

Once your draft version is ready to go live, click **Activate** to publish it. If there are existing users in your Flow, you will have a choice on how to transition users:

<AccordionGroup>
  <Accordion title="Restart in-progress users in new version">
    This option will restart all users currently in the Flow in the new version. Users who have already completed the Flow will not see the new version.
  </Accordion>

  <Accordion title="Exit in-progress users from the Flow">
    This option will exit all users currently in the Flow. Only new users who enter the Flow moving forward will see the new version.
  </Accordion>

  <Accordion title="Restart all users in new version">
    This option will restart all users in the Flow in the new version regardless of their state. This means that users who have already completed the Flow will also see the new version, too.
  </Accordion>
</AccordionGroup>

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=4fc4bcf053d618a4a9081b632eb6ff61" alt="Transitioning users" data-og-width="3008" width="3008" data-og-height="1720" height="1720" data-path="images/platform/flow-detail-versions-restart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=22dbfec271757a01f1a787d7776f654a 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=603451fb860f5c7c8390233e5ba664cc 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a4ecc2e2ea5a5e6f212eec48182a004c 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=edecfd836828cd03a0b5a28586c20e50 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=47b966a865868bf6060915c49a4e7b31 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=ea237dfc003622a5c43f759285069aa2 2500w" />
</Frame>

## Old versions

***

Once a draft has been activated, old versions of the Flow become read-only. Analytics for old versions will be preserved and can be viewed by clicking the **View** button on an old version.


# Frigade Engage Quickstart Guide
Source: https://docs.frigade.com/quickstart

Get set up with Frigade Engage in less than 15 minutes

<img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c09c3a4cb253ff4c9dcd772251ddb095" className="rounded pointer-events-none" data-og-width="2171" width="2171" data-og-height="944" height="944" data-path="images/welcome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5d7f6759b7f82b258948a7283b73e94c 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=37420c9445b969bbba94e12b262d6a92 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c48be5b63b0165f1023f2aa58d39abef 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f1515e30ee2abd4aacc10edfb9eac742 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f7827da35206c38e1ad7d9f85fb995ec 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=2c56365efaebc0a0e0f41c3ee548d632 2500w" />

<Steps>
  <Step title="Sign up and install">
    <AccordionGroup>
      <Accordion title="Get your API key">
        The first thing to do is sign up for a Frigade account at [frigade.com](https://app.frigade.com/sign-up). Then, locate your Frigade public API key in the [Developer](https://app.frigade.com/developer) tab of the dashboard.

        <Frame>
          <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5e6542db65e287c2a4be1e72267acfaa" data-og-width="1408" width="1408" data-og-height="526" height="526" data-path="images/platform/developer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=87c8f99108fb020261cb82887b94b02f 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=80566e99244aba45a6433d99d4f78e10 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3f5ef5a43f1507d88f4a988dff376c90 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=dbc6918b6d9a8056bcf95d850cf2691b 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1dd626800e1591de19efba8aa8476b86 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=911ce393220071c4f9640362a0b10327 2500w" />
        </Frame>
      </Accordion>

      <Accordion title="Install the React SDK">
        Install <a href="https://www.npmjs.com/package/@frigade/react" target="_blank" rel="noreferrer">@frigade/react</a> with your package manager.

        <CodeGroup>
          ```txt npm theme={"system"}
          npm install @frigade/react
          ```

          ```txt pnpm theme={"system"}
          pnpm install @frigade/react
          ```

          ```txt yarn theme={"system"}
          yarn add @frigade/react
          ```
        </CodeGroup>

        Next, add the Frigade `Provider` component to your app and plug in your public API key from earlier. We recommend wrapping your entire application to ensure that the SDK is available everywhere.
        Below are examples for how to install the Provider in popular React frameworks.

        <CodeGroup>
          ```tsx React theme={"system"}
          // Add this to your main application file, e.g., App.tsx or index.tsx
          import * as Frigade from "@frigade/react";

          // Replace this with your Frigade public API key
          const FRIGADE_API_KEY = "api_public_abcd1234";

          export const App: React.FC = () => {
            return (
              <Frigade.Provider 
                apiKey={FRIGADE_API_KEY}
                // Replace this with the ID of the signed in user
                userId="my-user-id"
                userProperties={{
                  email: "john@doe.com",
                  name: "John Doe"
                }}
              >
                {/* ... */}
              </Frigade.Provider>
            );
          };
          ```

          ```tsx Next.js (App router) theme={"system"}
          // frigade-provider-wrapper.tsx
          "use client";
          import * as Frigade from "@frigade/react";
          import { ReactNode } from 'react';

          // Replace this with your Frigade public API key
          const FRIGADE_API_KEY = "api_public_abcd1234";

          interface FrigadeProviderWrapperProps {
            children: ReactNode;
          }

          const FrigadeProviderWrapper: React.FC<FrigadeProviderWrapperProps> = ({ children }) => {
            return (
              <Frigade.Provider 
                apiKey={FRIGADE_API_KEY}
                // Replace this with the ID of the signed in user
                userId="my-user-id"
                userProperties={{
                  email: "john@doe.com",
                  name: "John Doe"
                }}
              >
                {children}
              </Frigade.Provider>
            );
          };

          // layout.tsx
          export default function Layout({ children }: { children: ReactNode }) {
            return (
              <FrigadeProviderWrapper>
                {children}
              </FrigadeProviderWrapper>
            );
          }
          ```

          ```tsx Next.js (Pages router) theme={"system"}
          // Add this to your _app.tsx file
          import * as Frigade from "@frigade/react";
          import { AppProps } from 'next/app';

          // Replace this with your Frigade public API key
          const FRIGADE_API_KEY = "api_public_abcd1234";

          function MyApp({ Component, pageProps }: AppProps) {
            return (
              <Frigade.Provider 
                apiKey={FRIGADE_API_KEY}
                // Replace this with the ID of the signed in user
                userId="my-user-id"
                userProperties={{
                  email: "john@doe.com",
                  name: "John Doe"
                }}
              >
                <Component {...pageProps} />
              </Frigade.Provider>
            );
          }

          export default MyApp;
          ```
        </CodeGroup>

        Great! Now you're ready to start building.
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Building and styling">
    <AccordionGroup>
      <Accordion title="Create a Flow">
        **Add a Flow to your application**

        For this example, let's add a `Banner` to our product.

        1. Click the **Create** button at the top of any page in the dashboard. Select the **Banner** component.
        2. On the Flow detail page, click the **Deploy** button. Copy the code snippet to your clipboard.
        3. Next, place the `<Frigade.Banner />` component in your application. Make sure to do this in a subcomponent of the `<Frigade.Provider />` component.

        ```tsx  theme={"system"}
        import * as Frigade from "@frigade/react";

        export const MyComponent = () => {
          return <Frigade.Banner flowId="flow_abcd1234" />;
        };
        ```

        **View the Flow**

        Tada! You should now see a shiny `Frigade Banner` where you placed it.

        <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1b065e68687f91cfec0edcd7a47f003f" data-og-width="1710" width="1710" data-og-height="401" height="401" data-path="images/platform/banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=23ebc8245b0210617488ac27208c526c 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6f9f99e204a5f18153d85e213e4f3a73 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d17c648c9aa128313e66a8ab75ba5ca1 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a61e06b1f39289419b29e83e6f19cd2f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7916813a184b39e22f03adb76b3d3ed2 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=72e736a9754a0f0a77da00d02777bf3c 2500w" />

        **See users in the Flow**

        Once you interact with the Flow in your application, you should see your user appear in the users tab of the Flow detail page. You can reset a user's progress in the Flow from here, which is especially useful for testing.

        <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=2f0eb06f64cfd58dcb5b9558e538b2f4" data-og-width="2987" width="2987" data-og-height="521" height="521" data-path="images/platform/reset-user.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6aa273b976f50bde5547e6c2cad6ee34 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=90f28649e5d111df07d360bfc39426d6 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7e1575f9fbe510e617578aefcc9c6027 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=27d5352ee8c1b2eef593d4f094e470b4 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=238e08f31e49911e3410a6e83a17f4ba 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=242c5e83883be71a665f3c7ca49a78ce 2500w" />
      </Accordion>

      <Accordion title="Updating Flows">
        Once a Flow is created, you can update it at any time from the dashboard.

        1. Navigate to the [Flows](https://app.frigade.com/flows) page and select a Flow
        2. In the Editor tab you can make changes with the basic or advanced editor
        3. Make changes and click **Save** and Frigade will update the Flow in real-time

        Check out the documentation for each component to see all the configuration options. Check out the [Banner](/component/banner) component for this quickstart demo.

        <Frame>
          <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=fc40523ed27e6c6ced0882293f0e7ecc" data-og-width="4598" width="4598" data-og-height="2410" height="2410" data-path="images/platform/editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e10b2892db864e36792081193d199be0 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7985c658200915d98ff903edbd812c34 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7bcbeebc8e05529ab0d9ebbf7e6ab55b 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8a02113fd5d1826db7f4f39444871c2b 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b8567865f7d8035a3d1b63fc83ffeffe 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=0884c324dc8a5a18b4d586b8fd93ebfc 2500w" />
        </Frame>

        <Note>If you plan to make major changes to a Flow, we recommend [version control](/platform/versioning).</Note>
      </Accordion>

      <Accordion title="User targeting">
        Sometimes you only want to show an experience to a specific user or group of users. Frigade makes this easy with [targeting](/platform/targeting).

        1. Navigate to the Flows page and select a Flow
        2. In the **Targeting** tab you can define the targeting for the Flow
        3. Frigade makes sure the Flow is only shown to users that match your criteria

        Check out [integrations](/integrations) to connect other platforms and import existing user segments for targeting.

        <Frame>
          <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3ff629c1598a46737aad2579fcd342b1" data-og-width="3456" width="3456" data-og-height="1926" height="1926" data-path="images/platform/flow-detail-audience.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6be15fee4c76d9da2cd14014ff762843 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=59a1aeb9087ce79ce5e731351740b43f 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6430d0069d4fb14ef1a4271bdee6c85f 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=25d1e7ec6bd9d9ffc8fd030b1a05a7f6 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5ad647ada4e6bf57add11f123df68e43 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=d05ba711ef7422ebb937b35ea9b75ad6 2500w" />
        </Frame>
      </Accordion>

      <Accordion title="Styling Flows">
        Frigade is fully customizable. You can style components to fit seamlessly within your application. Styling documentation is covered [here](/sdk/styling/). You can also see a live demo of the theming system at [demo.frigade.com](https://demo.frigade.com).

        <video autoPlay muted loop playsInline className="w-full aspect-video" src="https://app.frigade.com/images/marketing/img/themes-1.mp4" />
      </Accordion>

      <Accordion title="Custom components">
        When a pre-built Frigade UI component won't cut it, you can also build custom components with the Frigade SDK. See our custom component guide [here](/guides/custom).
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Nice work!">
    You've set up your first Frigade Flow. Our docs cover additional functionality like [analytics](/platform/analytics), [no-code deployments](/platform/collections), and [environments](/platform/environments).

    If you have questions or want to discuss your particular project, feel free to reach out to us at [support@frigade.com](mailto:support@frigade.com) or [book a demo](https://cal.com/team/frigade/frigade-demo).
  </Step>
</Steps>


# Dynamically Completing a Step
Source: https://docs.frigade.com/sdk/advanced/completing-a-step

Learn how to dynamically complete steps in Flows when your users take certain actions in your application.

For most components, steps in Flows are marked as completed when a user clicks the primary button. However, for components such as [Checklists](/component/checklist), you may want to complete or skip steps when your users take certain actions in your application rather than clicking the primary button. This can be achieved either marking a step completed via the SDK or API, or by defining a targeting query in the `completionCriteria` property on a step.

### Marking Steps completed via the SDK

Call the `complete` method from the [useFlow hook](/sdk/hooks/flow) in the [React SDK](/sdk/quickstart) or via the [JS SDK](/sdk/js/flow). In the example below, we're calling the `complete` method from the React SDK:

```javascript  theme={"system"}
import { useFlow } from '@frigade/react';

const { flow } = useFlow("my-flow-id");

await flow.steps.get('my-step-id').complete();
```

### Marking Steps complete via Targeting

Use the `completionCriteria` property on a step to automatically mark the step as completed when a user meets the criteria. See [Targeting](/platform/targeting) for more examples of how to write targeting queries.

```yaml  theme={"system"}
steps:
  - id: my-step-id
    ...
    completionCriteria: user.property('connectedBank') == true
```

### Preventing Steps from completing on primary button click

In built-in Flow components, a step is marked as complete when the primary button is clicked. To prevent this, select **No action** in the editor under the **Primary button** property:

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=37f4d1e7ccf0a41ffac913d6c8a01130" data-og-width="1842" width="1842" data-og-height="1027" height="1027" data-path="images/sdk/no-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7e941d97545749a9a679bf68e4e49848 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8e493b96aa2399a875646562bdcf85a7 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9173016be52c5144d283dae29d948243 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=96e27308262ae1777c0a22c7e62bd044 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=ef86e0b2b1d391ba67477c39d522de11 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e4d598be5d5b582fd2f62e78b3b97a73 2500w" />
</Frame>

## API Methods

You can also mark steps completed via the [flowStates](/api-reference/flows/flow-states-post) API endpoint.


# Merging a guest session with a authenticated user
Source: https://docs.frigade.com/sdk/advanced/linking-guest-users

Link a guest session's state to a user when they register or log in

Frigade will generate a guest user ID for you if you do not provide a user id. This ID is stored in the user's browser using `localStorage`.
This allows unauthenticated users to have state in Frigade Flows and to be able to continue their session when they return to your application.

Often it is useful to link a guest session to a user when they register or log in and transfer all state and data.

You can do this by calling the [Users API endpoint](/api-reference/users/overview) with a `linkGuestId` parameter. This will merge all state from the guest session to the user with the `userId` you provide. Note that this will only take affect if the given `userId` does not yet have any state in Frigade.

To do this in Javascript, you can use the `fetch` API:

```jsx  theme={"system"}
const options = {
  method: 'POST',
  headers: { Authorization: 'Bearer <FRIGADE_PUBLIC_API_KEY>',
            'Content-Type': 'application/json' },
  body: '{"userId":"<USER_ID>", "linkGuestId":"<GUEST_ID>"}'
};

fetch('https://api.frigade.com/v1/public/users', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```


# Reverse Proxy and Custom Domains
Source: https://docs.frigade.com/sdk/advanced/reverse-proxy



A reverse proxy allows you to use your own domain when sending data to and from Frigade. To set up a reverse proxy, you need to create a `CNAME` record in your DNS settings.
The `CNAME` record should point to `api.frigade.com` and override the host header to `api.frigade.com`.

For example, if you want to use `api.example.com` as your domain, you should create a `CNAME` record for `api.example.com` that points to `api.frigade.com` and override the Host header to `api.frigade.com`.
Then, when instantiating Frigade in your application with the `<Frigade.Provider />` component, you should set the `apiUrl` to `https://api.example.com`:

For a more in depth guide on how to set up a reverse proxy, check out [this guide](https://posthog.com/docs/advanced/proxy) from Posthog.

```jsx  theme={"system"}
import * as Frigade from '@frigade/react';

const App = () => (
  <Frigade.Provider apiUrl="https://api.example.com">
    <App />
  </Frigade.Provider>
);
```


# Automated Testing
Source: https://docs.frigade.com/sdk/advanced/testing

Learn how to run unit and integration tests with your Frigade Flows

***

Unlike no-code tools, Frigade allows you to easily write automated tests for your Flows. In this guide, we will show you how to write and run tests for your Flows using Playwright and Jest. The same principles can be applied to any testing framework.

<Steps>
  <Step title="Using a test user">
    When writing tests for your Flows, you should use a test user. This user should have the same permissions and properties as the users who will use your Flow.

    Before running your tests, you will likely want to reset this user in Frigade. This can be done by making the following API request using your private API key in the Developer environment (see [API docs](/api-reference/users/users-delete) for more information):

    ```javascript  theme={"system"}
    function resetTestUser() {
      fetch('https://api.frigade.com/v1/users?foreignId=my-test-user-id', {
        method: 'DELETE',
        headers: {
          'Authorization
          : `Bearer ${process.env.FRIGADE_PRIVATE_DEV_API_KEY}`,
        },
      });
    }
    ```

    With this in hand, you can add a `beforeAll` to reset the test user before and after running your tests.

    ```javascript  theme={"system"}
    beforeAll(() => {
      resetTestUser();
    });
    ```
  </Step>

  <Step title="Writing tests">
    To write tests for your Flows, you can use Playwright, Puppeteer, or any other testing framework.

    In this example, we will use Playwright. This test presses the primary button with the text "Got it" in a `Frigade.Announcement` and ensures that the modal is closed.

    ```javascript  theme={"system"}
    const { test, expect } = require('@playwright/test');

    test('close announcement', async ({ page }) => {
      await page.goto('http://localhost:3000/');
      await page.click('text=Got it');
      await page.waitForSelector('text=Got it', { state: 'detached' });
    });
    ```
  </Step>

  <Step title="Going further">
    For testing more complex scenarios (for instance, the chaining of Flows), you can leverage the underlying Vanilla JS SDK to simulate completing the first Flow and then starting the second Flow.

    Methods such as `flow.complete()` or `step.complete()` support an optional `createdAt` parameter that can simulate the time of completion, too.

    ```javascript  theme={"system"}
    import { Frigade } from '@frigade/js'

    test('Flow is visible after completing other Flow', async () => {
        const frigade = new Frigade(process.env.FRIGADE_PRIVATE_DEV_API_KEY, {
          userId: "my-test-user-id"
        })
        const flow = await frigade.getFlow("flow_abc")
        expect(flow.isVisible).toBeFalsy() // The Flow is not yet visible because `flow_def` has not been completed
        await frigade.getFlow("flow_def").complete({
            // Overrides the date of completion
            createdAt: "2022-01-01T00:00:00Z",
          })
        expect(flow.isVisible).toBeTruthy() // The Flow is now visible
      })
    ```
  </Step>
</Steps>


# V1 SDK Guide
Source: https://docs.frigade.com/sdk/advanced/v1



## Upgrading from V1 to V2

This guide outlines some of the biggest changes you need to make to upgrade from V1 to V2. Scroll down to the bottom for instructions on how to [use V1 and V2 at the same time](/sdk/advanced/v1#running-both-v1-and-v2-of-the-sdk).

### Provider theme

In V2, we have a [fully-fledged theming system](/sdk/styling/theming) that allows you to customize every token in our design system. If you used V1's theme colors, you can convert them to V2 like so:

```jsx  theme={"system"}
// V1
<FrigadeProvider
  config={{
    defaultAppearance: {
      theme: {
        colorText: '#3d3d3d',
        colorTextSecondary: '#494949',
        colorTextOnPrimaryBackground: '#fff',
        colorPrimary: '#2956B5',
        colorBorder: '#E2E2E2',
      }
    }
  }}
>

// V2
<Frigade.Provider
  theme={{
    colors: {
      neutral: {
        // Replaces colorBorder
        border: '#E2E2E2',

        // Replaces colorText
        foreground: '#3d3d3d'
      },
      primary: {
        // Replaces colorTextOnPrimaryBackground
        foreground: '#fff',

        // Replaces colorPrimary
        surface: '#2956B5'
      }
    }
  }}
>
```

Note that `colorTextSecondary` was deprecated and doesn't have a V2 equivalent.

### Global style overrides

We no longer wrap descendents of the Frigade Provider in a container element, as we found that for most users adding an extra wrapper to the DOM at (or near) the top was more disruptive than helpful.

As a result, we no longer support the `config.defaultAppearance.styleOverrides` property that existed on `FrigadeProvider` in V1.

We now recommend that you author global styles using your existing CSS workflow.

### Component style overrides

We use [Emotion's CSS prop](/sdk/styling/css-overrides) in V2, so you can write any CSS that Emotion supports directly on any component:

```jsx  theme={"system"}
// V1
<FrigadeAnnouncement
  appearance={{
    styleOverrides: {
      'button': {
        backgroundColor: 'fuchsia'
      }
    }
  }}
/>

// V2
<Frigade.Announcement
  css={{
    '.fr-button-primary': {
      backgroundColor: 'fuchsia',

      '&:hover': {
        backgroundColor: 'lilac'
      }
    },
  }}
/>
```

### Important difference between V1 `styleOverrides` and V2 `css` props:

The V2 `css` prop accepts a style object, which means that if you're using V1's `styleOverrides` prop to pass Tailwind classNames through to sub-components, you'll need to update your code to pass Tailwind's [arbitrary variants](https://tailwindcss.com/docs/hover-focus-and-other-states#using-arbitrary-variants), e.g.:

```jsx  theme={"system"}
// V1
<FrigadeAnnouncement
  appearance={{
    styleOverrides: {
      'button': 'w-full'
    }
  }}
/>

// V2
<Frigade.Announcement
  className="[&_button]:w-full"
/>
```

### Navigation

The `navigate` prop is now a top-level prop on Provider, it is no longer nested inside `config`:

```jsx  theme={"system"}
// V1
<FrigadeProvider
  config={{
    navigate: (url, target): void => {
      if (target === "_blank") {
        window.open(url, "_blank");
      } else {
        router.push(url);
      }
    },
  }}
>

// V2
<Frigade.Provider
  navigate={(url, target) => {
    if (target === "_blank") {
      window.open(url, "_blank");
    } else {
      router.push(url);
    }
  }}
>
```

### Event handlers

The catch-all `onButtonClick` prop has been replaced with individual handlers for `onPrimary`, `onSecondary`, `onDismiss`, and `onComplete`.

Full definitions of each handler are available in our [component docs](/component/announcement#oncomplete)

### Hooks

Our SDK hooks now expose objects from our [JS SDK](https://www.npmjs.com/package/@frigade/js) directly, for example [useFlow](/sdk/hooks/flow) returns an instance of [Flow](/sdk/js/flow), which you can operate directly on as you would in the JS SDK.

***

## Running V1 and V2 together

If you already have a V1 implementation and aren't ready to fully upgrade yet, you can use both V1 and V2 at the same time. This setup allows you to import V1 components from `@frigade/react` and V2 components from `@frigade/reactv2`.

### Instructions

<Steps>
  <Step title="First, install V2 using a package alias:">
    ```json  theme={"system"}
    "dependencies": [
    "@frigade/react": "1.x",
    "@frigade/reactv2": "npm:@frigade/react@2.x",
    ]
    ```
  </Step>

  <Step title="Then add the V2 `Provider` above the V1 `FrigadeProvider`:">
    ```tsx  theme={"system"}
    import { FrigadeProvider } from "@frigade/react";
    import * as Frigade from "@frigade/reactv2";

    const FRIGADE_API_KEY = "api_public_abcd1234";

    export const App = () => {
      const userId = "...";

      return (
        <Frigade.Provider apiKey={FRIGADE_API_KEY} userId={userId}>
          <FrigadeProvider publicApiKey={FRIGADE_API_KEY} userId={userId}>
            {/* ... */}
          </FrigadeProvider>
        </Frigade.Provider>
      );
    };
    ```
  </Step>
</Steps>

### Sharing state between V1 and V2

When using V1 and V2 together, state is not shared between the two providers. Be sure to call `frigade.reload()` from the [useFrigade() hook](/sdk/hooks/frigade) (V2) and/or `refresh()` from the `useFlows()` hook (V1).


# Common Issues and Solutions
Source: https://docs.frigade.com/sdk/common-issues

Find solutions to common issues with the Frigade SDK.

***

## Flows not showing up

If your Frigade components are not rendering in your product as expected, below are some of thhe most common issues and solutions to help you troubleshoot.

<AccordionGroup>
  <Accordion title="Developer console">
    Open the developer console in your browser and look for any error messages.
  </Accordion>

  <Accordion title="API key">
    Make sure you have the correct API key in your `<Frigade.Provider />` component. You can find your API key in the [Frigade dashboard](https://app.frigade.com/developer).
  </Accordion>

  <Accordion title="Flow status">
    Make sure your Flows are properly installed in your app and that they are active in the Frigade dashboard. If you have not published your Flows, or if you have turned them off, they will not be available in your app.
  </Accordion>

  <Accordion title="Flow targeting">
    Make sure any targeting you've set in the **Targeting** tab of your Flow is correct. If the targeting is too restrictive, your Flows may not show up for the intended users.
  </Accordion>

  <Accordion title="Environment">
    Make sure you are using the correct environment in your `<Frigade.Provider />` component. Each environment has its own API key and Flows. If you are using the wrong environment, your Flows will not show up in your app.
  </Accordion>

  <Accordion title="Debug mode">
    If you are still having issues, you can enable debug mode in Chrome Devtools ([see guide](/guides/tours#debugging-tooltips)).
  </Accordion>

  <Accordion title="Ensure zIndex is set correctly">
    If your Flows are not showing up, it may be because they are being rendered behind other elements on the page. You can fix this by setting the `zIndex` on components such as `Frigade.Tour` or `Frigade.Announcement` to a higher value.
  </Accordion>

  <Accordion title="Rules">
    If you've created a rule in the **Rules** tab of Frigade that includes the Flow then that could affect its visibility. Make sure you've configured the rule correctly and that your Flow is actually expected to show.
  </Accordion>
</AccordionGroup>

***

## Guest users in my dashboard

If a `userId` is not available when Frigade is initialized via the `<Frigade.Provider />` and/or the JS SDK, Frigade will automatically assign a guest user id to the user. This is to ensure that the user can still be tracked and that their data is not lost.

To prevent Frigade from automatically generating guest user IDs, you can pass a flag to the `<Frigade.Provider />` as shown below:

```jsx  theme={"system"}
<Frigade.Provider generateGuestId={false} />
```

## Import error

If you into an error such as `Can't import the named export 'Anchor' from non EcmaScript module (only default export is available)`, it is likely that you are using an older version of create-react-app.

There are two ways to fix this issue:

1. Upgrade to the latest version of create-react-app (you need to be on version 5.0.0 or higher of `react-scripts`).
2. Eject your app from create-react-app (if not already done) and manually configure your webpack to support ESM. Do this by adding the following to your webpack config:

```javascript  theme={"system"}
module.exports = {
  //...
  resolve: {
    extensions: ['.mjs', '.js', '.json'],
    mainFields: ['module', 'main'],
  },
  rules: [
    ///...
    { test: /\.mjs$/, include: /node_modules/, type: 'javascript/auto' }
  ],
  //...
};
```

***

## Something else?

If you are still having trouble with Frigade, [get in touch](mailto:support@frigade.com) and we'll be happy to help.


# useFlow
Source: https://docs.frigade.com/sdk/hooks/flow



The `useFlow(<flowId>)` hook makes it easy to build headless components or manipulate the state of a Flow for an existing component.
It exports a single field, `flow`, which contains the current state of the Flow, as well as a set of methods to manipulate the Flow.
[View the Flow class docs](../js/flow) to see the available fields and methods.

## About this hook

The `useFlow` hook is especially useful if you want to build a highly custom experience with your UI and/or components. You can find some example of how to build custom Flows in our [Custom Components guide](/guides/custom).

### Example use cases:

* Building a custom onboarding progress widget for your sidebar navigation
* Building a custom Kanban-style onboarding experience
* Building a highly custom onboarding checklist interface

### Example usage:

```tsx  theme={"system"}
import { useFlow } from "@frigade/react";

function MyComponent() {
  // Replace "myFlowId" with the ID of your Flow
  const { flow } = useFlow("myFlowId");

  return (
    <div>
      <h1>{flow.title}</h1>
      <p>{flow.subtitle}</p>
      <p>Currently on step {flow.getCurrentStep().id}</p>
      <button onClick={flow.next}>Next</button>
      <button onClick={flow.back}>Previous</button>
      <button onClick={flow.reset}>Reset</button>
    </div>
  );
}
```

<Tip>Make sure to call any Frigade hook within the context of `<Frigade.Provider />`</Tip>


# useFrigade
Source: https://docs.frigade.com/sdk/hooks/frigade



The `useFrigade()` hook exposes the underlying [Frigade JS SDK]() instance that powers the React SDK.
[View the Frigade class docs](../js/frigade) to see the available fields and methods.

## About this hook

The `useFrigade` hook can be used to access the underlying Frigade JS SDK instance and interact with it directly.
It should rarely be used as the provided [useFlow](./flow), [useUser](./user), and [useGroup](./group) hooks should be sufficient for most use cases.

### Example usage:

```tsx  theme={"system"}
import { useFrigade } from "@frigade/react";

function MyComponent() {
  const { frigade } = useFrigade();

  useEffect(() => {
  	const myHandler = (flow) => {
      console.log(`Detected change in ${flow.id}`);
    }
    frigade.onStateChange(myHandler);
    return () => {
      frigade.removeStateChangeHandler(myHandler);
    }
  }, []);
}
```

<Tip>Make sure to call any Frigade hook within the context of `<Frigade.Provider />`</Tip>


# useGroup
Source: https://docs.frigade.com/sdk/hooks/group



The `useGroup()` hook enables you to add properties and send tracking events to the current group.

## About this hook

The hook contains the following methods:
<ParamField body="track(eventName: string, properties?: Record<string, unknown>)">Promise that sends tracking events for the current group</ParamField>
<ParamField body="addProperties(properties: Record<string, unknown>)">Promise that adds properties to the current group</ParamField>
<ParamField body="setGroupId(groupId: string, properties?: Record<string, unknown>)">Promise that sets the current group ID. Using this hook can cause unexpected behaviors if also setting the group ID at the `<Frigade.Provider />` level.</ParamField>

### Example use cases:

* Tracking events and adding properties to the current group for using with [Targeting](/platform/targeting/)
* Wrapping the `track` method with your existing tracking/analytics methods

### Example usage:

```tsx  theme={"system"}
import { useGroup } from '@frigade/react';

function MyComponent() {
  const { addProperties } = useGroup();

  return (
    <button
      onClick={() => {
        addProperties({ orgHasConnectedBankAccount: true });
      }}
    >
      Connect Bank Account
    </button>
  );
}
```

<Tip>Make sure to call any Frigade hook within the context of `<Frigade.Provider />`</Tip>

## Standardized properties

The following standardized properties are automatically added to the group object if provided via `addProperties`:

* `name`: The name of the group/company/organiation
* `imageUrl`: The URL of the group/company/organiation's logo


# useUser
Source: https://docs.frigade.com/sdk/hooks/user



The `useUser()` hook enables you to add properties and send tracking events to the current user.

## About this hook

The hook contains the following methods:
<ParamField body="track(eventName: string, properties?: Record<string, unknown>)">Promise that sends tracking events for the current user</ParamField>
<ParamField body="addProperties(properties: Record<string, unknown>)">Promise that adds properties to the current user</ParamField>

<Info>Update the `userID` in the top-level `Frigade.Provider` component to change users</Info>

## Example use cases:

* Tracking events and adding properties to the current user for using with [Targeting](/platform/targeting/)
* Wrapping the `track` method with your existing tracking/analytics methods

### Tracking events example

```tsx  theme={"system"}
import { useUser } from "@frigade/react";

function MyComponent() {
  const { track } = useUser();

  useEffect(() => {
    track("MyComponent Viewed");
  }, []);

  return <div>My Component</div>;
}
```

### Adding properties example

```tsx  theme={"system"}
import { useUser } from "@frigade/react";

function MyComponent() {
  const { addProperties } = useUser();

  useEffect(() => {
    addProperties({
      email: "test@test.com",
      firstName: "John",
      lastName: "Doe",
      imageUrl: "https://example.com/image.png",
    });
  }, []);
}
```

Properties can also be added to the `userProperties` object via the `Frigade.Provider` component:

```tsx  theme={"system"}
<Frigade.Provider 
  apiKey="YOUR_API_KEY"
  userID="1234567890"
  userProperties={{ 
    email: "test@test.com", 
    firstName: "John", 
    lastName: "Doe", 
    imageUrl: "https://example.com/image.png" 
  }}
>
  <App />
</Frigade.Provider>
```

<Tip>Make sure to call any Frigade hook within the context of `<Frigade.Provider />`</Tip>

## Standardized properties

The following standardized properties are automatically added to the user object if provided via `addProperties`:

* `email` - The user's email address
* `name` - The user's full name
* `firstName` - The user's first name
* `lastName` - The user's last name
* `imageUrl` - The user's profile image URL


# Flow JS Type Definition
Source: https://docs.frigade.com/sdk/js/flow



All of Frigade's Javascript SDKs share the same Flow type definition which is defined in the [Frigade JS SDK](https://www.npmjs.com/package/@frigade/js).

The Flow object is the main object that models a Flow's static metadata (title, subtitle, steps, etc.) as well as the current user's state in this flow.

It contains all the data and methods needed to build custom components with Frigade and to interact with the Frigade API without writing a single custom network call.

# Properties

### Accessors

### config

**config**: `FrigadeConfig`

***

### id

**id**: `string`

The Flow's ID.

***

### isCompleted

**isCompleted**: `boolean`

Whether the Flow is completed or not.

***

### isSkipped

**isSkipped**: `boolean`

Whether the Flow has been skipped or not.

***

### isStarted

**isStarted**: `boolean`

Whether the Flow is started or not.

***

### rawData

**rawData**: `StatefulFlow`

The raw metadata of the Flow. Contains all properties defined in the Flow's YAML config as well as the current state of the Flow.
Generally this should only be used when building custom components to access custom high-level props on the Flow.

***

### steps

**steps**: `Map`\<`string`, `FlowStep`>

Ordered map of the Steps in the Flow.
See [Flow Step Definition](https://docs.frigade.com/v2/sdk/js/step) for more information.

***

### subtitle

`Optional` **subtitle**: `string`

The user-facing description of the Flow, if defined at the top level of the YAML config.

***

### title

`Optional` **title**: `string`

The user-facing title of the Flow, if defined at the top level of the YAML config.

***

### type

**type**: `FlowType`

The type of the Flow such as `TOUR` or `CHECKLIST`.

## Accessors

### isVisible

`get` **isVisible**(): `boolean`

Whether the Flow is visible to the user based on the current user/group's state.
This function will return `false` if the user has already completed or dismissed the Flow or if the user
does not match the Flow's targeting/audience.

`set` **isVisible**(`visible`): `void`

<b>Parameters</b>

| Name      | Type      |
| :-------- | :-------- |
| `visible` | `boolean` |

## Methods

### applyVariables

▸ **applyVariables**(`variables`): `void`

Apply variables to the flow. This will replace any `${variable}` in the title, subtitle, and step fields with the value of the variable.

<b>Parameters</b>

| Name        | Type                       | Description                                 |
| :---------- | :------------------------- | :------------------------------------------ |
| `variables` | `Record`\<`string`, `any`> | A record of variables to apply to the flow. |

***

### back

▸ **back**(`properties?`): `Promise`\<`void`>

Navigates the flow to the previous step if one exists. This will mark that step started, but will not complete the previous step.

<b>Parameters</b>

| Name          | Type              |
| :------------ | :---------------- |
| `properties?` | `PropertyPayload` |

***

### complete

▸ **complete**(`properties?`): `Promise`\<`void`>

Marks the flow completed

<b>Parameters</b>

| Name          | Type              |
| :------------ | :---------------- |
| `properties?` | `PropertyPayload` |

***

### forward

▸ **forward**(`properties?`): `Promise`\<`void`>

Navigates the flow to the next step if one exists. This will mark that step started, but will not complete the previous step.

<b>Parameters</b>

| Name          | Type              |
| :------------ | :---------------- |
| `properties?` | `PropertyPayload` |

***

### getCurrentStep

▸ **getCurrentStep**(): `FlowStep`

Gets current step. If the current step is not visible, it will return the first visible step after it.
If no steps are visible, it will return undefined.

***

### getCurrentStepIndex

▸ **getCurrentStepIndex**(): `number`

Get the index of the current step. Starts at 0

***

### getCurrentStepOrder

▸ **getCurrentStepOrder**(): `number`

Returns the current step's order based on the number of available steps.
Works similar to getCurrentStepIndex but takes into account hidden steps due to visibilityCriteria.

***

### getNumberOfAvailableSteps

▸ **getNumberOfAvailableSteps**(): `number`

Get the number of available steps for the current user in the current flow. This is the number of steps that are not hidden.

***

### getNumberOfCompletedSteps

▸ **getNumberOfCompletedSteps**(): `number`

Get the number of completed steps for the current user in the current flow

***

### getProgress

▸ **getProgress**(): `number`

Get the progress of the flow as a number between 0 and 1. Useful when rendering a progress bar.

***

### getStepByIndex

▸ **getStepByIndex**(`index`): `FlowStep`

Get a step by index

<b>Parameters</b>

| Name    | Type     |
| :------ | :------- |
| `index` | `number` |

***

### register

▸ **register**(`callback?`): `void`

<b>Parameters</b>

| Name        | Type                          |
| :---------- | :---------------------------- |
| `callback?` | `CollectionsRegistryCallback` |

***

### reload

▸ **reload**(): `void`

Reload the Flow data from the server

***

### restart

▸ **restart**(): `Promise`\<`void`>

Restarts the flow/marks it not started

***

### sendFlowStateToAPI

▸ **sendFlowStateToAPI**(`action`, `data?`, `stepId?`): `Promise`\<`void`>

<b>Parameters</b>

| Name      | Type              |
| :-------- | :---------------- |
| `action`  | `FlowActionType`  |
| `data?`   | `PropertyPayload` |
| `stepId?` | `string`          |

***

### skip

▸ **skip**(`properties?`): `Promise`\<`void`>

Marks the flow skipped

<b>Parameters</b>

| Name          | Type              |
| :------------ | :---------------- |
| `properties?` | `PropertyPayload` |

***

### start

▸ **start**(`properties?`): `Promise`\<`void`>

Marks the flow started

<b>Parameters</b>

| Name          | Type              |
| :------------ | :---------------- |
| `properties?` | `PropertyPayload` |

***

### unregister

▸ **unregister**(): `void`

[View definition](https://github.com/FrigadeHQ/frigade-react/blob/b8996ad7/packages/js-api/src/core/flow.ts#L696)


# Frigade JS Type Definition
Source: https://docs.frigade.com/sdk/js/frigade



The `Frigade` class is the main entry point for the Frigade JS SDK. It is used to create a new instance of the Frigade SDK and to interact with the Frigade API.

The Step type is a representation of a step in a Flow.

It contains all the data and methods needed to build custom components with Frigade and to interact with the Frigade API without writing a single custom network call.

# Properties

### getCollections

▸ **getCollections**(): `Promise`\<`CollectionsList`>

***

### getConfig

▸ **getConfig**(): `FrigadeConfig`

Gets the current configuration.
See  [FrigadeConfig](https://github.com/FrigadeHQ/javascript/blob/main/packages/js-api/src/core/types.ts#L240) for a list of available options.

***

### getFlow

▸ **getFlow**(`flowId`): `Promise`\<`Flow`>

Get a Flow by its ID.

<b>Parameters</b>

| Name     | Type     |
| :------- | :------- |
| `flowId` | `string` |

***

### getFlows

▸ **getFlows**(): `Promise`\<`Flow`\[]>

***

### group

▸ **group**(`groupId?`, `properties?`): `Promise`\<`void`>

Set the group for the current user.

<b>Parameters</b>

| Name          | Type              |
| :------------ | :---------------- |
| `groupId?`    | `string`          |
| `properties?` | `PropertyPayload` |

***

### hasFailedToLoad

▸ **hasFailedToLoad**(): `boolean`

Returns true if the JS SDK failed to connect to the Frigade API.

***

### identify

▸ **identify**(`userId`, `properties?`): `Promise`\<`void`>

Set the current user.

<b>Parameters</b>

| Name          | Type              |
| :------------ | :---------------- |
| `userId`      | `string`          |
| `properties?` | `PropertyPayload` |

***

### off

▸ **off**(`event`, `handler`): `Promise`\<`void`>

Removes the given handler.

<b>Parameters</b>

| Name      | Type                     | Description                                                                                                                                      |
| :-------- | :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| `event`   | `FlowChangeEvent`        | `flow.any` \| `flow.complete` \| `flow.restart` \| `flow.skip` \| `flow.start` \| `step.complete` \| `step.skip` \| `step.reset` \| `step.start` |
| `handler` | `FlowChangeEventHandler` |                                                                                                                                                  |

***

### on

▸ **on**(`event`, `handler`): `Promise`\<`void`>

Event handler that captures all changes that happen to the state of the Flows. Use `flow.any` to capture all events.

<b>Parameters</b>

| Name      | Type                     | Description                                                                                                                                      |
| :-------- | :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| `event`   | `FlowChangeEvent`        | `flow.any` \| `flow.complete` \| `flow.restart` \| `flow.skip` \| `flow.start` \| `step.complete` \| `step.skip` \| `step.reset` \| `step.start` |
| `handler` | `FlowChangeEventHandler` |                                                                                                                                                  |

***

### onStateChange

▸ **onStateChange**(`handler`): `Promise`\<`void`>

Event handler that captures all changes that happen to the state of the Flows.

<b>Parameters</b>

| Name      | Type                                                |
| :-------- | :-------------------------------------------------- |
| `handler` | (`flow`: `Flow`, `previousFlow?`: `Flow`) => `void` |

**Deprecated**

Use `frigade.on` instead.

***

### registerCollection

▸ **registerCollection**(`collectionId`): `Promise`\<`void`>

<b>Parameters</b>

| Name           | Type     |
| :------------- | :------- |
| `collectionId` | `string` |

***

### reload

▸ **reload**(`config?`): `Promise`\<`void`>

Reload the current state of the flows by calling the Frigade API.
This will trigger all event handlers.

<b>Parameters</b>

| Name      | Type            | Description                                                                            |
| :-------- | :-------------- | :------------------------------------------------------------------------------------- |
| `config?` | `FrigadeConfig` | optional config to use when reloading. If not passed, the current config will be used. |

***

### removeStateChangeHandler

▸ **removeStateChangeHandler**(`handler`): `Promise`\<`void`>

Removes the given handler from the list of event handlers.

<b>Parameters</b>

| Name      | Type                                                |
| :-------- | :-------------------------------------------------- |
| `handler` | (`flow`: `Flow`, `previousFlow?`: `Flow`) => `void` |

***

### resync

▸ **resync**(): `Promise`\<`void`>

***

### track

▸ **track**(`event`, `properties?`): `Promise`\<`void`>

Track an event for the current user (and group if set).

<b>Parameters</b>

| Name          | Type              |
| :------------ | :---------------- |
| `event`       | `string`          |
| `properties?` | `PropertyPayload` |

***

### triggerAllEventHandlers

▸ **triggerAllEventHandlers**(): `void`

[View definition](https://github.com/FrigadeHQ/frigade-react/blob/b8996ad7/packages/js-api/src/core/frigade.ts#L393)


# JS Quickstart
Source: https://docs.frigade.com/sdk/js/quickstart



The [Frigade JS SDK](https://www.npmjs.com/package/@frigade/js) is a lightweight library that allows you to easily integrate Frigade into any stack that runs Javascript.
Unlike the React SDK, it is completely headless and does not include any UI components. Instead, it provides a simple API that allows you to quickly build
your own components powered by Frigade with any Javascript framework or library.

<Steps>
  <Step title="Install the JS SDK">
    <CodeGroup>
      ```txt npm theme={"system"}
      npm install @frigade/js
      ```

      ```txt yarn theme={"system"}
      yarn add @frigade/js
      ```

      ```txt pnpm theme={"system"}
      pnpm install @frigade/js
      ```
    </CodeGroup>
  </Step>

  <Step title="Initialize the SDK">
    Simply `import { Frigade }  from '@frigade/js'` and initialize the SDK with your **public API key** from the **Developer** page of the dashboard.

    ```js  theme={"system"}
    import { Frigade } from '@frigade/js'

    const frigade = new Frigade('FRIGADE_API_KEY')

    await frigade.identify('USER_ID', {
      name: 'USER_NAME',
      email: 'USER_EMAIL',
      signed_up_at: 'USER_SIGNED_UP_AT' // ISO 8601 format
    })

    // Optional: send organization/group id
    await frigade.group('ORGANIZATION_ID', {
      name: 'COMPANY_NAME',
    })
    ```
  </Step>

  <Step title="Start building with Frigade">
    That's pretty much it! You can now use the Frigade JS SDK. Here's how to get a Flow:

    ```js  theme={"system"}
      const flow = await frigade.getFlow('FLOW_ID')
      console.log('Flow status:', flow.isCompleted)

      const currentStep = flow.getCurrentStep();

      /*
      * You'll usually want to ensure that the flow and current step are both
      * marked as "started" when a user sees them.
      */
      await flow.start();
      await currentStep.start();

      /*
      * Handling interaction is easy -- Flows and Steps have built-in methods
      * to update their state.
      */
      async function handleStepComplete() {
        await currentStep.complete();
      }
    ```

    We recommend taking a quick look at the [JS SDK API documentation](./frigade) to get a better understanding of the available methods and how to use them. Also, check out our guide on [building custom components](/guides/custom) for more information on how to build custom experiences with Frigade.
  </Step>
</Steps>


# Step JS Type Definition
Source: https://docs.frigade.com/sdk/js/step



All of Frigade's Javascript SDKs share the same Flow Step type definition which is defined in the [Frigade JS SDK](https://www.npmjs.com/package/@frigade/js).

The Step type is a representation of a step in a Flow.

It contains all the data and methods needed to build custom components with Frigade and to interact with the Frigade API without writing a single custom network call.

# Properties

### \$state

**\$state**: `Object`

The state of the step for the given user in the given Flow.
Example:

```
{
 completed: true,
 skipped: false,
 started: true,
 visible: true,
 blocked: false,
 lastActionAt: "2014-01-01T23:28:56.782Z"
}
```

***

### autoMarkCompleted

`Optional` **autoMarkCompleted**: `boolean`

Automatically mark the step as completed when the primary button is clicked. Default is false.

***

### backButtonTitle

`Optional` **backButtonTitle**: `string`

Text on button if a back button is present.

***

### complete

**complete**: (#propertypayload), `optimistic?`: `boolean`) => `Promise`\<`void`>

Marks the step completed.

**Param**

If true, the step will be marked as completed without waiting for the API and validation of any targeting rules.

**Parameters**

| Name          | Type                                  | Description                                                                                                      |
| :------------ | :------------------------------------ | :--------------------------------------------------------------------------------------------------------------- |
| `properties?` | [`PropertyPayload`](#propertypayload) | -                                                                                                                |
| `optimistic?` | `boolean`                             | If true, the step will be marked as completed without waiting for the API and validation of any targeting rules. |

**Returns**

`Promise`\<`void`>

***

### completionCriteria

`Optional` **completionCriteria**: `string`

Criteria that needs to be met for the step to complete.
Completion criteria uses Frigade's [Targeting Engine](https://docs.frigade.com/v2/platform/targeting) to determine if the step should be completed.

***

### dismissible

`Optional` **dismissible**: `boolean`

Whether the step is dismissible (for instance, tooltips or other non-essential steps).

***

### flow

**flow**: `Flow`

Reference to this step's parent Flow

***

### iconUri

`Optional` **iconUri**: `string`

Icon url to be shown for components supporting icons.

***

### id

**id**: `string`

***

### imageUri

`Optional` **imageUri**: `string`

Image url to be shown for components supporting image.

***

### onStateChange

**onStateChange**: (`callback`: (`step`: [`FlowStep`](FlowStep.md), `previousStep?`: [`FlowStep`](FlowStep.md)) => `void`) => `void`

Event handler called when this step's state changes.

**Deprecated**

Use `frigade.on('step.complete' | 'step.skip' | 'step.reset' | 'step.start', handler)` instead.

**Parameters**

| Name       | Type                                                                                      |
| :--------- | :---------------------------------------------------------------------------------------- |
| `callback` | (`step`: [`FlowStep`](FlowStep.md), `previousStep?`: [`FlowStep`](FlowStep.md)) => `void` |

**Returns**

`void`

**Deprecated**

Use `frigade.on('step.complete' | 'step.skip' | 'step.reset' | 'step.start', handler)` instead.

***

### order

**order**: `number`

Order of the step in the Flow.

***

### primaryButton

`Optional` **primaryButton**: `Object`

Config for the primary button in this step

\| `action?` | [`StepAction`](#stepaction) | Primary button action. (defaults to step.complete) |
\| `target?` | `string` | Primary button URI target (defaults to \_self). |
\| `title?` | `string` | Primary button title. If omitted, the primary button will not be shown. |
\| `uri?` | `string` | Primary button URI. |

***

### primaryButtonTitle

`Optional` **primaryButtonTitle**: `string`

**Deprecated**

Use primaryButton.title instead

**Description**

Primary button title. If omitted, the primary button will not be shown.

***

### primaryButtonUri

`Optional` **primaryButtonUri**: `string`

**Deprecated**

Use primaryButton.uri instead

**Description**

Primary button URI.

***

### primaryButtonUriTarget

`Optional` **primaryButtonUriTarget**: `string`

**Deprecated**

Use primaryButton.target instead

**Description**

Primary button URI target (defaults to \_self).

***

### progress

`Optional` **progress**: `number`

Progress if the step is tied to another Frigade Flow through completionCriteria.

***

### removeStateChangeHandler

**removeStateChangeHandler**: (`callback`: (`step`: [`FlowStep`](FlowStep.md), `previousStep?`: [`FlowStep`](FlowStep.md)) => `void`) => `void`

Removes the given callback from the list of event handlers.

**Parameters**

| Name       | Type                                                                                      |
| :--------- | :---------------------------------------------------------------------------------------- |
| `callback` | (`step`: [`FlowStep`](FlowStep.md), `previousStep?`: [`FlowStep`](FlowStep.md)) => `void` |

**Returns**

`void`

***

### reset

**reset**: () => `Promise`\<`void`>

Resets the step (useful for undoing a finished step).

**Returns**

`Promise`\<`void`>

***

### secondaryButton

`Optional` **secondaryButton**: `Object`

Config for the secondary button in this step

\| `action?` | [`StepAction`](#stepaction) | Secondary button action. (defaults to step.complete) |
\| `target?` | `string` | Secondary button URI target (defaults to \_self). |
\| `title?` | `string` | Secondary button title. If omitted, the secondary button will not be shown. |
\| `uri?` | `string` | Secondary button URI. |

***

### secondaryButtonTitle

`Optional` **secondaryButtonTitle**: `string`

**Deprecated**

Use secondaryButton.title instead

**Description**

Secondary button title. If omitted, the secondary button will not be shown.

***

### secondaryButtonUri

`Optional` **secondaryButtonUri**: `string`

**Deprecated**

Use secondaryButton.uri instead

**Description**

Secondary button URI.

***

### secondaryButtonUriTarget

`Optional` **secondaryButtonUriTarget**: `string`

**Deprecated**

Use secondaryButton.target instead

**Description**

Secondary button URI target (defaults to \_self)

***

### skip

**skip**: (#propertypayload), `optimistic?`: `boolean`) => `Promise`\<`void`>

Marks the step skipped. Works similar to step.complete()

**Parameters**

| Name          | Type                                  |
| :------------ | :------------------------------------ |
| `properties?` | [`PropertyPayload`](#propertypayload) |
| `optimistic?` | `boolean`                             |

**Returns**

`Promise`\<`void`>

***

### skippable

`Optional` **skippable**: `boolean`

If true, the step will be marked as completed when the secondary button is clicked.

***

### start

**start**: (#propertypayload)) => `Promise`\<`void`>

Marks the step started. This will move the current step index to the given step.

**Parameters**

| Name          | Type                                  |
| :------------ | :------------------------------------ |
| `properties?` | [`PropertyPayload`](#propertypayload) |

**Returns**

`Promise`\<`void`>

***

### startCriteria

`Optional` **startCriteria**: `string`

Criteria that needs to be met for the step to start.
Start criteria uses Frigade's [Targeting Engine](https://docs.frigade.com/v2/platform/targeting) to determine if the step should be started.

***

### stepName

`Optional` **stepName**: `string`

Name of the step when shown in a list view.

***

### subtitle

`Optional` **subtitle**: `string`

Subtitle of the step.

***

### title

`Optional` **title**: `string`

Title of the step.

***

### videoUri

`Optional` **videoUri**: `string`

Video url to be shown for components supporting video.

***

### visibilityCriteria

`Optional` **visibilityCriteria**: `string`

Criteria that needs to be met for the step to be visible.
Visibility criteria uses Frigade's [Targeting Engine](https://docs.frigade.com/v2/platform/targeting) to determine if the step should be visible.

[View definition](https://github.com/FrigadeHQ/frigade-react/blob/b8996ad7/packages/js-api/src/core/types.ts#L216)


# Navigation
Source: https://docs.frigade.com/sdk/navigation



Frigade supports the ability to route users to different pages in your application through the `primaryButtonUri` and `secondaryButtonUri` props defined in the [Flow configuration](/component/tour#flow-configuration).

By default, Frigade will use the `window.location` object to navigate to the specified URI. This works well for some use cases, but it causes a full page refresh which can be disruptive.

For optimal performance, we recommend overriding this behavior by providing a custom `navigate` function to the `Frigade.Provider` component where you can use your own router for a smoother experience.

# Examples

Overriding the default navigation handler is different depending on your React framework of choice. Below are examples for the most popular Routers:

## Next.js App and Pages Router

```jsx  theme={"system"}
import * as Frigade from '@frigade/react';
import { useRouter } from 'next/navigation'; // or 'next/router' if using Pages Router

const App = () => {
  const router = useRouter();

  return (
    <Frigade.Provider
      navigate={(url, target) => {
        if (target === "_blank") {
          window.open(url, "_blank");
        } else {
          router.push(url);
        }
      }}
    >
      {children}
    </Frigade.Provider>
  );
}
```

## React Router

```jsx  theme={"system"}
import * as Frigade from '@frigade/react';
import { useHistory } from 'react-router-dom';

const App = () => {
  const history = useHistory();

  return (
    <Frigade.Provider
      navigate={(url, target) => {
        if (target === "_blank") {
          window.open(url, "_blank");
        } else {
          history.push(url);
        }
      }}
    >
      {children}
    </Frigade.Provider>
  );
}
```


# React SDK Overview
Source: https://docs.frigade.com/sdk/overview

Frigade Engage React SDK and JavaScript SDK

<img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/npm.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=666c7b7a590df77cedc4d9f58547629d" data-og-width="2692" width="2692" data-og-height="1784" height="1784" data-path="images/sdk/npm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/npm.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=93aab391c0b1634687aec87dd3d809f2 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/npm.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e6c9803eaab4658e46ac04c828c5751f 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/npm.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=afe59d3d657684ca01984d41ea62b75f 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/npm.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=0038d260715b95ace14147a36a8604be 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/npm.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f8f4554ae3950fd78b3cab7607dc42a5 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/npm.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=450053346a75ab887c461e59b6ae83aa 2500w" />

## Getting Started

Check out the [SDK Quickstart](/sdk/quickstart) for instructions on installing the React SDK in your app.

## Components

The Frigade Engage React SDK includes a [library](/component/overview) of highly customizable onboarding components that you can use to build your app.

## JavaScript SDK

Our [JavaScript SDK](/sdk/js/quickstart) is a lightweight, headless library you can use to build custom experiences with Frigade. The SDK is vanilla and works for Node.js, React Native, and the browser.

## Typescript

All types used in the Javascript SDK are exported from the `@frigade/react` package under the `FrigadeJS` namespace. You can import them like so:

```javascript  theme={"system"}
import { FrigadeJS } from "@frigade/react";
```

## Angular, Vue, Svelte, etc.

We are mainly focused on React, but we plan to build SDKs for other frameworks. If you'd like to be notified about new SDKs, reach out and <a href="mailto:support@frigade.com">let us know</a> which framework you're using.


# Provider
Source: https://docs.frigade.com/sdk/provider



The `<Frigade.Provider />` component is the root component of the Frigade SDK. It initializes the SDK and keeps track of the user's session and state in all Frigade Flows.a

See the [Quickstart Guide](/sdk/quickstart) to see an example of how to use the Provider.

# Properties

### apiKey

**apiKey**: `string`

Your public API key from the Frigade dashboard. Do not ever use your private API key here.

***

### apiUrl

`Optional` **apiUrl**: `string`

The URL prefix of the API to use. By default, Frigade will use the production API: [https://api.frigade.com/v1/public](https://api.frigade.com/v1/public)

***

### children

`Optional` **children**: `ReactNode`

***

### css

`Optional` **css**: `Record`\<`string`, `unknown`>

Global CSS properties to attach to the :root element.

**See**

[https://emotion.sh/docs/css-prop#object-styles](https://emotion.sh/docs/css-prop#object-styles)

***

### defaultCollection

`Optional` **defaultCollection**: `boolean`

By default, Frigade.Provider will render a built-in Collection to allow no-code deploys of Announcements and other floating Components. Set this to `false` if you want to manually control the rendering of the default Collection.

***

### generateGuestId

`Optional` **generateGuestId**: `boolean`

Whether to generate a Guest ID and session if no userId is provided at render time.
If set to false, Frigade will not initialize or render any Flows until a userId is provided.
Defaults to true.

***

### groupId

`Optional` **groupId**: `string`

The group ID to use for this context (optional).

***

### groupProperties

`Optional` **groupProperties**: `PropertyPayload`

Optional group properties to attach to the groupId on initialization.

***

### navigate

`Optional` **navigate**: [`NavigateHandler`](#navigatehandler)

A function to handle navigation. By default, Frigade will use `window.open` if not provided.
[https://docs.frigade.com/v2/sdk/navigation](https://docs.frigade.com/v2/sdk/navigation)

***

### preloadImages

`Optional` **preloadImages**: `boolean`

Whether to preload images in Flows. Defaults to true.

***

### syncOnWindowUpdates

`Optional` **syncOnWindowUpdates**: `boolean`

Whether to sync state with Frigade on URL or focus change. Defaults to true.

***

### theme

`Optional` **theme**

The global theme to use across components. See docs on styling: [https://docs.frigade.com/v2/sdk/styling/theming](https://docs.frigade.com/v2/sdk/styling/theming)

***

### userId

`Optional` **userId**: `string`

The user ID of the user who is interacting with Frigade. If not provided, Frigade will generate a random guest ID and persist it in local storage.

***

### userProperties

`Optional` **userProperties**: `PropertyPayload`

Optional user properties to attach to the userId on initialization.

***

### variables

`Optional` **variables**: `Record`\<`string`, `unknown`>

Global variables to apply to all Flows, including Collections.
If the individual Collection or Flow has its own variables, the two objects will be merged, with the Flow/Collection having high priority.
Example:

```tsx  theme={"system"}
variables={{
  name: "Bobby Nerves",
  occupation: "Vocalist",
}}
```

This prop can conveniently be used to pass entire i18n objects as well, which will allow all Flows to access i18n strings as needed.

[View definition](https://github.com/FrigadeHQ/frigade-react/blob/b8996ad7/packages/react/src/components/Provider/Provider.tsx#L119)


# React SDK Quickstart
Source: https://docs.frigade.com/sdk/quickstart

How to set up Frigade in your React app

<Steps>
  <Step title="Install the React SDK">
    <CodeGroup>
      ```txt npm theme={"system"}
      npm install @frigade/react
      ```

      ```txt yarn theme={"system"}
      yarn add @frigade/react
      ```

      ```txt pnpm theme={"system"}
      pnpm install @frigade/react
      ```
    </CodeGroup>
  </Step>

  <Step title="Add the Provider">
    Add the Frigade `Provider` component to your app. Make sure to paste in your **public** API key and user ID.
    Optionally, you can pass in user properties like `firstName`, `lastName`, and `email` to decorate the user profile in Frigade.

    ```jsx  theme={"system"}
    import * as Frigade from "@frigade/react";

    const FRIGADE_API_KEY = "api_public_abcd1234";

    export const App = () => {
      const userId = "..."; // If no user id is provided, Frigade will generate a guest id

      return (
        <Frigade.Provider
          apiKey={FRIGADE_API_KEY}
          userId={userId}
          userProperties={{
            firstName: "John",
            lastName: "Doe",
            email: "john.doe@acme.com"
          }}
        >
          {/* ... */}
        </Frigade.Provider>
      );
    };
    ```

    For a full list of supported properties, see the [Provider documentation](/sdk/provider).
  </Step>

  <Step title="Use your first component">
    That's pretty much it! You can now use the SDK. Here's an example of how to use the `Announcement` component:

    ```tsx  theme={"system"}
    import * as Frigade from "@frigade/react";

    export const DemoComponent = () => {
        return <Frigade.Announcement flowId="flow_abcd1234" />;
    };
    ```

    Be sure to create an `Announcement` in Frigade web dashboard and link the FlowId to the component above. Check out our general [Quickstart](/quickstart) for more information.
  </Step>
</Steps>

## Next steps

Now that you have Frigade running in your application, you will likely want to style them to fit your brand.
See the [styling guide](/sdk/styling/theming) to get started.


# CSS Overrides
Source: https://docs.frigade.com/sdk/styling/css-overrides



## CSS Prop

We use [Emotion's css prop](https://emotion.sh/docs/css-prop#use-the-css-prop) under the hood in our components. You can pass a `css` object in at the top level of any of our components to create scoped styles for that specific instance of that component.

Since the `css` prop is scoped to each component, you can treat it as though it were a `style` prop with added functionality. For example:

```tsx  theme={"system"}
// This CSS will be compiled at runtime by Emotion and applied to
// the `.fr-card` wrapper at the top level of the Card component

<Frigade.Card
  css={{
    backgroundColor: "goldenrod",
  }}
/>
```

## Styling sub-components

We also assign stable class names to each internal part of each component, to make style overrides as easy as:

```tsx  theme={"system"}
<Frigade.Tour
  css={{
    ".fr-tooltip-content .fr-tooltip-close": {
      backgroundColor: "pink",
    },
    ".fr-button-primary": {
      backgroundColor: "fuchsia",
    },
  }}

  {...}
/>
```

To find the stable class names for any given component, you can either:

1. Inspect the component in your browser's dev tools and look for classes prefixed with `fr-`
2. [View the source](https://github.com/FrigadeHQ/javascript/tree/main/packages/react/src/components) for the component and use the value of the `part` prop (class name will always be `fr-${part}`)

## Global overrides

If you want to style every instance of a Frigade component (or write any other general CSS), the `<Frigade.Provider />` component also accepts a `css` prop. It writes global CSS into the document, so use it with caution.

Since every Frigade Component has its own stable classname, you can override every `<Button.Primary />` simply by writing CSS in object syntax:

```tsx  theme={"system"}
<Frigade.Provider
  css={{
    ".fr-button-primary": {
      backgroundColor: "aquamarine",

      "&:hover": {
        backgroundColor: "honeydew",
      },
    },
  }}

  {...}
/>
```

To override the styles for every Frigade Button, use a [wildcard attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors):

```tsx  theme={"system"}
<Frigade.Provider
  css={{
    "[class*='fr-button']": {
      backgroundColor: "maroon",

      "&:hover": {
        backgroundColor: "cornsilk",
      },
    },
  }}

  {...}
/>
```

## Overriding CSS from the Flow editor

You can override the `css` prop or any other attribute from the Flow editor by providing the `props` field in the Advanced YAML editor:

```yaml  theme={"system"}
props:
  css:
    backgroundColor: "blue"
    ".fr-button-primary":
      backgroundColor: "chartreuse"
steps: ...
```

You can also override the styling on specific Steps by providing the `props` field on the given Step. This will override the styling for that specific Step only:

```yaml  theme={"system"}
steps:
  - id: step-1
    props:
      css:
        ".fr-button-primary":
          backgroundColor: "chartreuse"
```

## External CSS

If you prefer to use your own CSS workflow, any old CSS will work. You can provide a top-level `className` prop to a component via a static stylesheet, CSS Modules, etc. then scope your styles to that:

```jsx  theme={"system"}
<Frigade.Tour className="my-scoped-component" {...} />
```

```css  theme={"system"}
.my-scoped-component {
  & .fr-button-primary {
    backgroundcolor: "chartreuse";
  }
}
```

Note: If you use external CSS to target `.fr-` classnames, your CSS must be source-ordered *after* Frigade's CSS in order to properly override the built-in Component styles.

If you don't have control over source-ordering in your app, you can increase the specificity of your selectors instead:

```css  theme={"system"}
body :is(.fr-title) {
  font-size: 42px;
}
```

## Tailwind

You can use Tailwind's [arbitrary variants](https://tailwindcss.com/docs/hover-focus-and-other-states#using-arbitrary-variants) to style the inner sub-components of a Frigade component:

```jsx  theme={"system"}
<Frigade.Banner className="[&_.fr-title]:text-fuchsia-500" {...} />
```


# Theming
Source: https://docs.frigade.com/sdk/styling/theming



The easiest way to get Frigade components integrated into your designs is by customizing the base theme that all of our components inherit from.

The base theme covers common style properties like colors, typography, spacing, and borders. If you need deeper customization, you can dig into CSS overrides or even custom components.

To override the base theme, pass the properties you want to change into the `theme` prop of the `Provider` component. In the example below we override the default blue primary color to be `#000000`:

```tsx  theme={"system"}
<Frigade.Provider
  apiKey="..."
  theme={{
    colors: {
      "primary": {
        "background": "#000000",
        "border": "#000000",
        "surface": "#000000",
      }
    }
  }}
/>
```

## Tailwind CSS and Shadcn

If you're using Tailwind CSS with Shadcn, you can use the `theme` mappings below to automatically match your existing theme.

```tsx  theme={"system"}
<Frigade.Provider
  apiKey="..."
  theme={{
    colors: {
      primary: {
        foreground: 'hsl(var(--primary-foreground))',
        background: 'hsl(var(--primary))',
        surface: 'hsl(var(--primary))',
        border: 'hsl(var(--primary))',
        hover: {
          background: 'hsl(var(--primary) / 0.9)',
          surface: 'hsl(var(--primary) / 0.9)',
          border: 'hsl(var(--primary) / 0.9)',
        },
      },
      secondary: {
        foreground: 'hsl(var(--secondary-foreground))',
        background: 'hsl(var(--secondary))',
        surface: 'hsl(var(--secondary))',
        border: 'hsl(var(--secondary))',
        hover: {
          background: 'hsl(var(--secondary) / 0.8)',
          surface: 'hsl(var(--secondary) / 0.8)',
          border: 'hsl(var(--secondary) / 0.8)',
        },
      },
      neutral: {
        background: 'hsl(var(--card))',
        foreground: 'hsl(var(--neutral-foreground))',
        border: 'hsl(var(--border))',
        '100': 'hsl(var(--neutral))',
        '200': 'hsl(var(--neutral))',
        '300': 'hsl(var(--neutral))',
        '400': 'hsl(var(--neutral))',
        '500': 'hsl(var(--accent))',
        '600': 'hsl(var(--accent))',
        '700': 'hsl(var(--accent))',
        '800': 'hsl(var(--accent))',
        '900': 'hsl(var(--accent))',
      },
    },
  }}
/>
```

If using a `<ThemeProvider />` to enable theming such as dark mode, make sure the `<Frigade.Provider />` is a child of the `<ThemeProvider />` component.

## CSS Variables

Our theme runs on a set of [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) that map 1:1 to the properties in the theme. For any part of the theme, you can override the related CSS var and any themed value in that CSS scope will be changed accordingly.

This is especially useful in conjunction with the `css` prop, as it allows you to create temporary sub-themes that apply only to one Component, e.g.:

```tsx  theme={"system"}
<Frigade.Tour
  css={{
    // Change primary elements (i.e. buttons) in this Tour to be black
    "--fr-color-primary-surface": "var(--fr-colors-black)",
  }}
/>
```

The full list of CSS variables used in our theme can be found [here](/sdk/styling/css-variables).

## Finding a specific theme variable

You can use your browser's developer tools to inspect the CSS properties of any Frigade component. For instance, to find the theme variable for the secondary text in the [Form](/component/form) component, you can inspect the element and look for the `color` property:

<img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=671d8130f0dbf45d51e3cd346e236b76" className="rounded-md" style={{border: '1px solid #E8EBF0',}} data-og-width="3470" width="3470" data-og-height="1820" height="1820" data-path="images/sdk/finding-colors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=93ac6afd9a803410844c5ae0a0cc79b8 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=229f456f304729452c5d8aaea0aa2879 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=bddcc50287f03dd21b7d7530668aa68e 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b19566c57594d7e99c6a262ecad618fe 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=d058e4558bc17d4efc054f2967442ea2 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9fd77f23cca4b81d9530d3cb922f7de3 2500w" />

In the above example, we see that the theme variable is `--fr-colors-neutral-400`, which also corresponds to `colors.neutral.400` in the theme object.


