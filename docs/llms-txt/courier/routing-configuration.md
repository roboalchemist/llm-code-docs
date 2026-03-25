# Source: https://www.courier.com/docs/platform/content/template-designer/routing-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Routing Configuration

> Configure reusable routing configurations in Design Studio. Define channel priority, fallback logic, and delivery methods.

Routing determines how your notification is delivered across channels. In Design Studio, you can create named routing configurations that are reusable across templates.

<Note>
  This feature is available in Design Studio (Beta). In Classic Designer, routing is configured separately for each template.
</Note>

## Selecting a routing configuration

Click the routing dropdown in the template editor toolbar to select or create routing configurations.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-routing-selector.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=d4d9b4480c778d2bb42b41fdb4b9e53f" alt="Routing selector dropdown showing saved configurations" width="1498" height="636" data-path="assets/platform/content/designer-v2/designer-v2-routing-selector.png" />
</Frame>

From this dropdown you can:

* Select an existing routing configuration
* Click the pencil icon to edit a configuration
* Click **+ Add new routing** to create a new configuration

## Routing schemes

Each routing configuration has a **name** and a **scheme**. The scheme determines how channels are prioritized.

### Basic scheme

The Basic scheme sends notifications to all enabled channels simultaneously.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-basic-routing-modal.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=a0ec8519613189ad6af58950a46d0187" alt="Basic routing scheme with all channels enabled" width="1956" height="1704" data-path="assets/platform/content/designer-v2/designer-v2-basic-routing-modal.png" />
</Frame>

Toggle channels on or off to control which channels receive the notification. The flowchart on the right shows that all enabled channels receive the notification at the same time.

### Advanced scheme

The Advanced scheme provides cascading fallback logic. Notifications are sent to a required channel first, then fall back to other channels if delivery fails.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/kP89ont3skGKuAuV/assets/platform/content/designer-v2/designer-v2-advanced-routing-modal.png?fit=max&auto=format&n=kP89ont3skGKuAuV&q=85&s=f49757a1008d5f9bd167f12dd343ebb8" alt="Advanced routing scheme with fallback chain" width="1954" height="1702" data-path="assets/platform/content/designer-v2/designer-v2-advanced-routing-modal.png" />
</Frame>

The Advanced scheme has two sections:

| Section                              | Behavior                                                 |
| ------------------------------------ | -------------------------------------------------------- |
| **Always send to**                   | Required channel(s) that always receive the notification |
| **If the last above fails, send to** | Fallback channels tried in order until one succeeds      |

Drag channels to reorder priority. The flowchart visualizes the fallback chain.

## Reusing routing configurations

Unlike the classic designer where routing is configured per-template, v2 routing configurations are saved and reusable:

1. Create a routing configuration once (e.g., "Primary" with email + SMS fallback)
2. Apply it to multiple templates from the routing dropdown
3. Edit the configuration to update all templates using it

This makes it easier to maintain consistent delivery logic across your notification templates.

## Related

<CardGroup cols={2}>
  <Card title="Content Blocks" icon="cube" href="/platform/content/design-studio/design-studio-block-basics">
    Building notification content
  </Card>

  <Card title="Send API" icon="paper-plane" href="/reference/send/message">
    Sending notifications with routing
  </Card>
</CardGroup>
