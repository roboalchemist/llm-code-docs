# Source: https://www.courier.com/docs/help/glossary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

> Quick reference for Courier terminology and concepts.

## A

**[API Key](/platform/workspaces/environments-api-keys)** - A secret token used to authenticate requests to Courier's REST API. Each environment has its own API keys, and keys can be scoped to specific permissions.

**[Audience](/platform/users/audiences)** - A dynamic user collection that automatically updates based on filter rules. Unlike static lists, audiences automatically include or exclude users as their profile data changes.

**[Automation](/platform/automations/automations-overview)** - A multi-step workflow that orchestrates complex messaging sequences with conditional logic, delays, digests, and multiple notification steps.

## B

**[Batching](/platform/automations/batching)** - Grouping multiple automation triggers into a single consolidated action within an automation step.

**[Brand](/platform/content/brands/brands-overview)** - A visual template that applies consistent styling to email notifications, including logos, colors, and layout.

**[Bulk Send](/tutorials/sending/how-to-send-bulk-notifications)** - Sending the same notification to many recipients in a single API call using a job-based workflow.

## C

**[Channel](/external-integrations/integrations-overview)** - A communication method like email, SMS, push notifications, in-app inbox, or direct messaging (Slack, Discord, etc.).

**[Channel Priority](/platform/sending/channel-priority)** - The order in which different communication channels are attempted when delivering a notification.

**[Client Key](/platform/inbox/authentication)** - A publishable key used to authenticate client-side SDKs (Inbox, Toast, React components). Unlike API keys, client keys are safe to expose in frontend code.

**[Conditions](/platform/content/template-settings/send-conditions)** - Logic that enables or disables content blocks, channels, or entire notifications based on user data or other criteria.

**[Content Block](/platform/content/template-designer/template-designer-overview)** - A reusable, responsive content component (text, image, action button, etc.) used inside notification templates in the Template Designer.

**[Courier Create](/platform/create/create-overview)** - An embeddable notification designer that lets your users create and edit notification templates within your application.

## D

**[Delay](/platform/sending/delay)** - A pause step in automations that waits a specified duration or until a specific time before continuing.

**Delivery** - The final step where a message reaches the recipient through a provider.

**[Designer](/platform/content/template-designer/template-designer-overview)** - Courier's visual editor for creating and editing notification templates.

**Device Token** - A unique identifier for app-device combinations issued by Apple (APNs) or Google (FCM) push notification gateways. Stored in [user profiles](/platform/users/users).

**[Digest](/platform/automations/digest)** - A feature that batches multiple notifications into a single consolidated message, reducing notification fatigue.

**[Draft / Published](/platform/content/template-settings/general-settings)** - The two states of a notification template. Draft changes are only visible in the test environment until you publish them to production.

## E

**[Elemental](/platform/content/elemental/elemental-overview)** - A JSON-based syntax for describing notification content programmatically that works across all channels.

**[Environment](/platform/workspaces/environments-api-keys)** - Separate instances (test and production) within a workspace that allow safe development without affecting live notifications.

**Event** - A trigger identifier that initiates notifications. Can be a direct notification template ID or a custom event ID mapped to any template via [Event Mapping](/platform/content/template-settings/general-settings#event-mapping).

## F

**[Failover](/platform/sending/failover)** - Automatic switching to backup providers when a primary provider fails to deliver.

**[Feed](/platform/inbox/inbox-overview)** - A filtered stream of messages in the Inbox component. Feeds let you organize messages into categories like "Notifications" and "Comments" using tabs.

## G

**[Guardrails](/platform/sending/send-limits)** - Safety features like send limits that prevent accidental sends to large audiences or excessive notifications to individual users.

## H

**[Handlebars](/platform/content/template-designer/handlebars-designer)** - A templating language used in the Template Designer for dynamic content insertion, conditionals, and loops. See also [Handlebars Helpers](/platform/content/template-designer/handlebars-helpers).

## I

**[Idempotency Key](/reference/get-started#idempotency)** - A unique identifier sent with API requests to prevent duplicate processing. If the same key is sent twice, Courier returns the original response.

**[Inbox](/platform/inbox/inbox-overview)** - Courier's built-in in-app notification center component for web and mobile applications.

**Inline Content** - Notification content defined directly in the [Send API](/platform/sending/send-message) request body rather than referencing a stored template.

**[Integration](/external-integrations/integrations-overview)** - A connection between Courier and a notification provider (SendGrid, Twilio, etc.) that handles actual message delivery.

## J

**[Jsonnet](/platform/content/content-blocks/jsonnet-blocks)** - A data templating language used in content blocks and the [webhook designer](/platform/content/template-designer/jsonnet-webhook-designer) for advanced data transformation.

**[JWT (JSON Web Token)](/platform/inbox/authentication)** - A secure token used for client-side authentication, required for Inbox and other frontend SDK components.

## L

**[List](/platform/users/audiences)** - A static group of users that must be manually managed, unlike audiences which update automatically.

**[Locale](/platform/content/localization)** - A language or regional variant (e.g., `en-US`, `fr-FR`) used for localizing notification content.

**[Logs](/platform/analytics/message-logs)** - A timeline of sent messages with delivery status, provider responses, and rendered content.

## M

**[MCP (Model Context Protocol)](/tools/mcp)** - A protocol that lets AI agents interact with Courier programmatically.

**Message** - A single instance of a notification sent to a specific recipient.

**[Message Status](/platform/analytics/message-logs)** - The delivery state of a message as it moves through the pipeline: enqueued, sent, delivered, opened, clicked, or undeliverable.

## N

**Notification** - A message template that can be sent repeatedly through one or more channels, containing [variables](/platform/content/variables/inserting-variables) for personalization.

## O

**Override** - A way to modify the request body or configuration sent to a provider, useful for passing provider-specific options not exposed in the template designer.

**[Outbound Webhook](/platform/workspaces/outbound-webhooks)** - A webhook that Courier fires when specific events occur (message sent, delivered, etc.), allowing you to sync delivery data to external systems.

## P

**[Preferences](/platform/preferences/preferences-overview)** - User-controlled settings that determine which notifications they receive and through which channels.

**[Profile](/platform/users/users)** - A JSON object storing a user's contact information, device tokens, and custom attributes.

**[Provider](/external-integrations/integrations-overview)** - The downstream service (Twilio, SendGrid, etc.) that delivers notifications to recipients.

## R

**Recipient** - The end user who receives notifications, identified by their [profile](/platform/users/users).

**[Routing](/platform/sending/choosing-your-sending-strategy)** - The logic that determines which channels and providers are used to deliver notifications.

## S

**[Send Conditions](/platform/content/template-settings/send-conditions)** - Rules evaluated at send time that determine whether a notification should be delivered based on data or logic.

**[Send Limit](/platform/sending/send-limits)** - A cap on how many notifications can be sent to a user, topic, or tenant within a time period. Different from API rate limits.

**[Subscription Topic](/platform/preferences/preferences-overview)** - A category of notifications (e.g., "Marketing", "Order Updates") that users can opt in or out of through preferences. Configured in the [Preferences Editor](/platform/preferences/preferences-editor).

## T

**[Template](/platform/content/template-designer/template-designer-overview)** - A reusable message design created in the Template Designer that defines content structure and can be sent to multiple recipients.

**[Template Approval](/platform/content/template-approval-workflow)** - A workflow requiring review before templates can be published to production.

**[Tenant](/platform/tenants/tenants-overview)** - An organization or customer group in multi-tenant applications, allowing you to scope branding, preferences, and data to specific organizations.

**[Throttle](/platform/automations/throttle)** - An automation step that limits how frequently a notification can be triggered for a given scope (per-user, global, or dynamic key).

**[Toast](/platform/inbox/notify-with-toasts)** - A transient pop-up notification shown by the Inbox SDK components when a new message arrives.

**Trigger** - An action or event that starts an [automation](/platform/automations/automations-overview) or sends a notification.

## V

**[Variable](/platform/content/variables/inserting-variables)** - A placeholder in notification templates (like `{name}` or `{order_id}`) that gets replaced with actual data when sending.

## W

**[Workspace](/platform/workspaces/workspaces-overview)** - The top-level organizational unit containing all your Courier resources, environments, team members, and settings.
