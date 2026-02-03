# Source: https://docs.crewai.com/en/enterprise/features/flow-hitl-management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Flow HITL Management

> Enterprise-grade human review for Flows with email-first notifications, routing rules, and auto-response capabilities

<Note>
  Flow HITL Management features require the `@human_feedback` decorator, available in **CrewAI version 1.8.0 or higher**. These features apply specifically to **Flows**, not Crews.
</Note>

CrewAI Enterprise provides a comprehensive Human-in-the-Loop (HITL) management system for Flows that transforms AI workflows into collaborative human-AI processes. The platform uses an **email-first architecture** that enables anyone with an email address to respond to review requests—no platform account required.

## Overview

<CardGroup cols={3}>
  <Card title="Email-First Design" icon="envelope">
    Responders can reply directly to notification emails to provide feedback
  </Card>

  <Card title="Flexible Routing" icon="route">
    Route requests to specific emails based on method patterns or flow state
  </Card>

  <Card title="Auto-Response" icon="clock">
    Configure automatic fallback responses when no human replies in time
  </Card>
</CardGroup>

### Key Benefits

* **Simple mental model**: Email addresses are universal; no need to manage platform users or roles
* **External responders**: Anyone with an email can respond, even non-platform users
* **Dynamic assignment**: Pull assignee email directly from flow state (e.g., `sales_rep_email`)
* **Reduced configuration**: Fewer settings to configure, faster time to value
* **Email as primary channel**: Most users prefer responding via email over logging into a dashboard

## Setting Up Human Review Points in Flows

Configure human review checkpoints within your Flows using the `@human_feedback` decorator. When execution reaches a review point, the system pauses, notifies the assignee via email, and waits for a response.

```python  theme={null}
from crewai.flow.flow import Flow, start, listen
from crewai.flow.human_feedback import human_feedback, HumanFeedbackResult

class ContentApprovalFlow(Flow):
    @start()
    def generate_content(self):
        # AI generates content
        return "Generated marketing copy for Q1 campaign..."

    @listen(generate_content)
    @human_feedback(
        message="Please review this content for brand compliance:",
        emit=["approved", "rejected", "needs_revision"],
    )
    def review_content(self, content):
        return content

    @listen("approved")
    def publish_content(self, result: HumanFeedbackResult):
        print(f"Publishing approved content. Reviewer notes: {result.feedback}")

    @listen("rejected")
    def archive_content(self, result: HumanFeedbackResult):
        print(f"Content rejected. Reason: {result.feedback}")

    @listen("needs_revision")
    def revise_content(self, result: HumanFeedbackResult):
        print(f"Revision requested: {result.feedback}")
```

For complete implementation details, see the [Human Feedback in Flows](/en/learn/human-feedback-in-flows) guide.

### Decorator Parameters

| Parameter | Type        | Description                                         |
| --------- | ----------- | --------------------------------------------------- |
| `message` | `str`       | The message displayed to the human reviewer         |
| `emit`    | `list[str]` | Valid response options (displayed as buttons in UI) |

## Platform Configuration

Access HITL configuration from: **Deployment → Settings → Human in the Loop Configuration**

<Frame>
  <img src="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-overview.png?fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=e5d32c64d5f617edd4bef2ffc4791d0a" alt="HITL Configuration Settings" data-og-width="2324" width="2324" data-og-height="1630" height="1630" data-path="images/enterprise/hitl-settings-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-overview.png?w=280&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=154386d5b87d940882039275d39dfaf3 280w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-overview.png?w=560&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=e54c4950a751052a0550d165ccc2ee3b 560w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-overview.png?w=840&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=58f5bda9f4b34e74fb15ed922bd30972 840w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-overview.png?w=1100&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=cd206e8893f57a5b92f9bc3576de42f4 1100w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-overview.png?w=1650&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=e50180b5cefb79630735acc38e7507e2 1650w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-overview.png?w=2500&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=2d8eda2a818460b10dd16e9018c4a8d8 2500w" />
</Frame>

### Email Notifications

Toggle to enable or disable email notifications for HITL requests.

| Setting             | Default | Description                            |
| ------------------- | ------- | -------------------------------------- |
| Email Notifications | Enabled | Send emails when feedback is requested |

<Note>
  When disabled, responders must use the dashboard UI or you must configure webhooks for custom notification systems.
</Note>

### SLA Target

Set a target response time for tracking and metrics purposes.

| Setting              | Description                                                       |
| -------------------- | ----------------------------------------------------------------- |
| SLA Target (minutes) | Target response time. Used for dashboard metrics and SLA tracking |

Leave empty to disable SLA tracking.

## Email Notifications & Responses

The HITL system uses an email-first architecture where responders can reply directly to notification emails.

### How Email Responses Work

<Steps>
  <Step title="Notification Sent">
    When a HITL request is created, an email is sent to the assigned responder with the review content and context.
  </Step>

  <Step title="Reply-To Address">
    The email includes a special reply-to address with a signed token for authentication.
  </Step>

  <Step title="User Replies">
    The responder simply replies to the email with their feedback—no login required.
  </Step>

  <Step title="Token Validation">
    The platform receives the reply, verifies the signed token, and matches the sender email.
  </Step>

  <Step title="Flow Resumes">
    The feedback is recorded and the flow continues with the human's input.
  </Step>
</Steps>

### Response Format

Responders can reply with:

* **Emit option**: If the reply matches an `emit` option (e.g., "approved"), it's used directly
* **Free-form text**: Any text response is passed to the flow as feedback
* **Plain text**: The first line of the reply body is used as feedback

### Confirmation Emails

After processing a reply, the responder receives a confirmation email indicating whether the feedback was successfully submitted or if an error occurred.

### Email Token Security

* Tokens are cryptographically signed for security
* Tokens expire after 7 days
* Sender email must match the token's authorized email
* Confirmation/error emails are sent after processing

## Routing Rules

Route HITL requests to specific email addresses based on method patterns.

<Frame>
  <img src="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-routing-rules.png?fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=238a2ceff47325f3c462c20d209d4494" alt="HITL Routing Rules Configuration" data-og-width="1362" width="1362" data-og-height="1284" height="1284" data-path="images/enterprise/hitl-settings-routing-rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-routing-rules.png?w=280&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=d24fe99074deede0acc9ba7492cb4c30 280w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-routing-rules.png?w=560&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=46ff958cb36d3f6eb7fe96be3fe73385 560w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-routing-rules.png?w=840&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=6c9df86ac90cea2ad78cad310b59f4fc 840w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-routing-rules.png?w=1100&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=16f08ee69c2b75f0219c39699a1a71bc 1100w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-routing-rules.png?w=1650&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=f4ade63fb2e60fa68660e4a23d4a14dc 1650w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-routing-rules.png?w=2500&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=4f0362a553838ac122b6480d85fe4ce1 2500w" />
</Frame>

### Rule Structure

```json  theme={null}
{
  "name": "Approvals to Finance",
  "match": {
    "method_name": "approve_*"
  },
  "assign_to_email": "finance@company.com",
  "assign_from_input": "manager_email"
}
```

### Matching Patterns

| Pattern            | Description          | Example Match                       |
| ------------------ | -------------------- | ----------------------------------- |
| `approve_*`        | Wildcard (any chars) | `approve_payment`, `approve_vendor` |
| `review_?`         | Single char          | `review_a`, `review_1`              |
| `validate_payment` | Exact match          | `validate_payment` only             |

### Assignment Priority

1. **Dynamic assignment** (`assign_from_input`): If configured, pulls email from flow state
2. **Static email** (`assign_to_email`): Falls back to configured email
3. **Deployment creator**: If no rule matches, the deployment creator's email is used

### Dynamic Assignment Example

If your flow state contains `{"sales_rep_email": "alice@company.com"}`, configure:

```json  theme={null}
{
  "name": "Route to Sales Rep",
  "match": {
    "method_name": "review_*"
  },
  "assign_from_input": "sales_rep_email"
}
```

The request will be assigned to `alice@company.com` automatically.

<Tip>
  **Use Case**: Pull the assignee from your CRM, database, or previous flow step to dynamically route reviews to the right person.
</Tip>

## Auto-Response

Automatically respond to HITL requests if no human responds within a timeout. This ensures flows don't hang indefinitely.

### Configuration

| Setting           | Description                                      |
| ----------------- | ------------------------------------------------ |
| Enabled           | Toggle to enable auto-response                   |
| Timeout (minutes) | Time to wait before auto-responding              |
| Default Outcome   | The response value (must match an `emit` option) |

<Frame>
  <img src="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-auto-respond.png?fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=4dbc036a080750ef6cd2a60d29ccdef5" alt="HITL Auto-Response Configuration" data-og-width="1374" width="1374" data-og-height="386" height="386" data-path="images/enterprise/hitl-settings-auto-respond.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-auto-respond.png?w=280&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=a96e16ce9a8e1ef32dcb153081fee493 280w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-auto-respond.png?w=560&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=9843d3fff431796cb8aaaaa4f7c1d325 560w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-auto-respond.png?w=840&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=6f6dd82da89eaf5e96aa4ca5b9dccf4c 840w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-auto-respond.png?w=1100&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=918645d34c9c87b5909dd83d931f172b 1100w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-auto-respond.png?w=1650&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=2150efcf3d9cf5d366119fa0ec4c0406 1650w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-auto-respond.png?w=2500&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=67d805d98957c6f811438b1902fc2cdb 2500w" />
</Frame>

### Use Cases

* **SLA compliance**: Ensure flows don't hang indefinitely
* **Default approval**: Auto-approve low-risk requests after timeout
* **Graceful degradation**: Continue with a safe default when reviewers are unavailable

<Warning>
  Use auto-response carefully. Only enable it for non-critical reviews where a default response is acceptable.
</Warning>

## Review Process

### Dashboard Interface

The HITL review interface provides a clean, focused experience for reviewers:

* **Markdown Rendering**: Rich formatting for review content with syntax highlighting
* **Context Panel**: View flow state, execution history, and related information
* **Feedback Input**: Provide detailed feedback and comments with your decision
* **Quick Actions**: One-click emit option buttons with optional comments

<Frame>
  <img src="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-list-pending-feedbacks.png?fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=0076724f318c88a466599a3637f7afd2" alt="HITL Pending Requests List" data-og-width="2498" width="2498" data-og-height="942" height="942" data-path="images/enterprise/hitl-list-pending-feedbacks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-list-pending-feedbacks.png?w=280&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=f99e06ea9666c69101c72a5ab75ac3b3 280w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-list-pending-feedbacks.png?w=560&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=19b4c6b7265443cd789483c214281365 560w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-list-pending-feedbacks.png?w=840&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=09fad5b3f46d18edaeb528d03e837b47 840w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-list-pending-feedbacks.png?w=1100&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=805787ecef7c6de1fcc58cf57687a2a0 1100w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-list-pending-feedbacks.png?w=1650&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=bffa5222e3f8037f77bbe3f1ef18d92d 1650w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-list-pending-feedbacks.png?w=2500&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=c167597550ef9c5d9c0a422616a3514a 2500w" />
</Frame>

### Response Methods

Reviewers can respond via three channels:

| Method          | Description                              |
| --------------- | ---------------------------------------- |
| **Email Reply** | Reply directly to the notification email |
| **Dashboard**   | Use the Enterprise dashboard UI          |
| **API/Webhook** | Programmatic response via API            |

### History & Audit Trail

Every HITL interaction is tracked with a complete timeline:

* Decision history (approve/reject/revise)
* Reviewer identity and timestamp
* Feedback and comments provided
* Response method (email/dashboard/API)
* Response time metrics

## Analytics & Monitoring

Track HITL performance with comprehensive analytics.

### Performance Dashboard

<Frame>
  <img src="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-metrics.png?fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=0c303db20aa3bf1707c194c36dfc44e4" alt="HITL Metrics Dashboard" data-og-width="2472" width="2472" data-og-height="1450" height="1450" data-path="images/enterprise/hitl-metrics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-metrics.png?w=280&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=ee8d6c204e52714742f43fb9e4be5b77 280w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-metrics.png?w=560&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=30cec352564d949f8bc6bbf4aef0d8eb 560w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-metrics.png?w=840&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=6ae227019601cac4c02077b36462d4d3 840w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-metrics.png?w=1100&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=66120f1439e1d3c31d1a1c59eea2e9ba 1100w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-metrics.png?w=1650&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=d2624cc5863cba8a6584cfbdbd3b14d5 1650w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-metrics.png?w=2500&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=511cbb7c79b6b79e7b58c862233d62d4 2500w" />
</Frame>

<CardGroup cols={2}>
  <Card title="Response Times" icon="stopwatch">
    Monitor average and median response times by reviewer or flow.
  </Card>

  <Card title="Volume Trends" icon="chart-bar">
    Analyze review volume patterns to optimize team capacity.
  </Card>

  <Card title="Decision Distribution" icon="chart-pie">
    View approval/rejection rates across different review types.
  </Card>

  <Card title="SLA Tracking" icon="chart-line">
    Track percentage of reviews completed within SLA targets.
  </Card>
</CardGroup>

### Audit & Compliance

Enterprise-ready audit capabilities for regulatory requirements:

* Complete decision history with timestamps
* Reviewer identity verification
* Immutable audit logs
* Export capabilities for compliance reporting

## Common Use Cases

<AccordionGroup>
  <Accordion title="Security Reviews" icon="shield-halved">
    **Use Case**: Internal security questionnaire automation with human validation

    * AI generates responses to security questionnaires
    * Security team reviews and validates accuracy via email
    * Approved responses are compiled into final submission
    * Full audit trail for compliance
  </Accordion>

  <Accordion title="Content Approval" icon="file-lines">
    **Use Case**: Marketing content requiring legal/brand review

    * AI generates marketing copy or social media content
    * Route to brand team email for voice/tone review
    * Automatic publishing upon approval
  </Accordion>

  <Accordion title="Financial Approvals" icon="money-bill">
    **Use Case**: Expense reports, contract terms, budget allocations

    * AI pre-processes and categorizes financial requests
    * Route based on amount thresholds using dynamic assignment
    * Maintain complete audit trail for financial compliance
  </Accordion>

  <Accordion title="Dynamic Assignment from CRM" icon="database">
    **Use Case**: Route reviews to account owners from your CRM

    * Flow fetches account owner email from CRM
    * Store email in flow state (e.g., `account_owner_email`)
    * Use `assign_from_input` to route to the right person automatically
  </Accordion>

  <Accordion title="Quality Assurance" icon="magnifying-glass">
    **Use Case**: AI output validation before customer delivery

    * AI generates customer-facing content or responses
    * QA team reviews via email notification
    * Feedback loops improve AI performance over time
  </Accordion>
</AccordionGroup>

## Webhooks API

When your Flows pause for human feedback, you can configure webhooks to send request data to your own application. This enables:

* Building custom approval UIs
* Integrating with internal tools (Jira, ServiceNow, custom dashboards)
* Routing approvals to third-party systems
* Mobile app notifications
* Automated decision systems

<Frame>
  <img src="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-webhook.png?fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=3301018dbd6a4cb01d352b09c18e674a" alt="HITL Webhook Configuration" data-og-width="1382" width="1382" data-og-height="556" height="556" data-path="images/enterprise/hitl-settings-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-webhook.png?w=280&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=f629be280edd240a458bf1917c8542a8 280w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-webhook.png?w=560&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=f8a6614eaa9af58d0d55d628fde0706b 560w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-webhook.png?w=840&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=45e643cd5a1d62baddd49c87511c4519 840w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-webhook.png?w=1100&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=8f834a562c6dfe712a39ea8aca99a56a 1100w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-webhook.png?w=1650&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=34fe08cd3cda1fd5ec7e9cffbf4f57a2 1650w, https://mintcdn.com/crewai/w39BrkMXZUwGQ32u/images/enterprise/hitl-settings-webhook.png?w=2500&fit=max&auto=format&n=w39BrkMXZUwGQ32u&q=85&s=4c5f8509f11d3ecdf862da8aa5532ffe 2500w" />
</Frame>

### Configuring Webhooks

<Steps>
  <Step title="Navigate to Settings">
    Go to your **Deployment** → **Settings** → **Human in the Loop**
  </Step>

  <Step title="Expand Webhooks Section">
    Click to expand the **Webhooks** configuration
  </Step>

  <Step title="Add Your Webhook URL">
    Enter your webhook URL (must be HTTPS in production)
  </Step>

  <Step title="Save Configuration">
    Click **Save Configuration** to activate
  </Step>
</Steps>

You can configure multiple webhooks. Each active webhook receives all HITL events.

### Webhook Events

Your endpoint will receive HTTP POST requests for these events:

| Event Type    | When Triggered                            |
| ------------- | ----------------------------------------- |
| `new_request` | A flow pauses and requests human feedback |

### Webhook Payload

All webhooks receive a JSON payload with this structure:

```json  theme={null}
{
  "event": "new_request",
  "request": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "flow_id": "flow_abc123",
    "method_name": "review_article",
    "message": "Please review this article for publication.",
    "emit_options": ["approved", "rejected", "request_changes"],
    "state": {
      "article_id": 12345,
      "author": "john@example.com",
      "category": "technology"
    },
    "metadata": {},
    "created_at": "2026-01-14T12:00:00Z"
  },
  "deployment": {
    "id": 456,
    "name": "Content Review Flow",
    "organization_id": 789
  },
  "callback_url": "https://api.crewai.com/...",
  "assigned_to_email": "reviewer@company.com"
}
```

### Responding to Requests

To submit feedback, **POST to the `callback_url`** included in the webhook payload.

```http  theme={null}
POST {callback_url}
Content-Type: application/json

{
  "feedback": "Approved. Great article!",
  "source": "my_custom_app"
}
```

### Security

<Info>
  All webhook requests are cryptographically signed using HMAC-SHA256 to ensure authenticity and prevent tampering.
</Info>

#### Webhook Security

* **HMAC-SHA256 signatures**: Every webhook includes a cryptographic signature
* **Per-webhook secrets**: Each webhook has its own unique signing secret
* **Encrypted at rest**: Signing secrets are encrypted in our database
* **Timestamp verification**: Prevents replay attacks

#### Signature Headers

Each webhook request includes these headers:

| Header        | Description                                  |
| ------------- | -------------------------------------------- |
| `X-Signature` | HMAC-SHA256 signature: `sha256=<hex_digest>` |
| `X-Timestamp` | Unix timestamp when the request was signed   |

#### Verification

Verify by computing:

```python  theme={null}
import hmac
import hashlib

expected = hmac.new(
    signing_secret.encode(),
    f"{timestamp}.{payload}".encode(),
    hashlib.sha256
).hexdigest()

if hmac.compare_digest(expected, signature):
    # Valid signature
```

### Error Handling

Your webhook endpoint should return a 2xx status code to acknowledge receipt:

| Your Response | Our Behavior                   |
| ------------- | ------------------------------ |
| 2xx           | Webhook delivered successfully |
| 4xx/5xx       | Logged as failed, no retry     |
| Timeout (30s) | Logged as failed, no retry     |

## Security & RBAC

### Dashboard Access

HITL access is controlled at the deployment level:

| Permission                  | Capability                                  |
| --------------------------- | ------------------------------------------- |
| `manage_human_feedback`     | Configure HITL settings, view all requests  |
| `respond_to_human_feedback` | Respond to requests, view assigned requests |

### Email Response Authorization

For email replies:

1. The reply-to token encodes the authorized email
2. Sender email must match the token's email
3. Token must not be expired (7-day default)
4. Request must still be pending

### Audit Trail

All HITL actions are logged:

* Request creation
* Assignment changes
* Response submission (with source: dashboard/email/API)
* Flow resume status

## Troubleshooting

### Emails Not Sending

1. Check "Email Notifications" is enabled in configuration
2. Verify routing rules match the method name
3. Verify assignee email is valid
4. Check deployment creator fallback if no routing rules match

### Email Replies Not Processing

1. Check token hasn't expired (7-day default)
2. Verify sender email matches assigned email
3. Ensure request is still pending (not already responded)

### Flow Not Resuming

1. Check request status in dashboard
2. Verify callback URL is accessible
3. Ensure deployment is still running

## Best Practices

<Tip>
  **Start Simple**: Begin with email notifications to deployment creator, then add routing rules as your workflows mature.
</Tip>

1. **Use Dynamic Assignment**: Pull assignee emails from your flow state for flexible routing.

2. **Configure Auto-Response**: Set up a fallback for non-critical reviews to prevent flows from hanging.

3. **Monitor Response Times**: Use analytics to identify bottlenecks and optimize your review process.

4. **Keep Review Messages Clear**: Write clear, actionable messages in the `@human_feedback` decorator.

5. **Test Email Flow**: Send test requests to verify email delivery before going to production.

## Related Resources

<CardGroup cols={2}>
  <Card title="Human Feedback in Flows" icon="code" href="/en/learn/human-feedback-in-flows">
    Implementation guide for the `@human_feedback` decorator
  </Card>

  <Card title="Flow HITL Workflow Guide" icon="route" href="/en/enterprise/guides/human-in-the-loop">
    Step-by-step guide for setting up HITL workflows
  </Card>

  <Card title="RBAC Configuration" icon="shield-check" href="/en/enterprise/features/rbac">
    Configure role-based access control for your organization
  </Card>

  <Card title="Webhook Streaming" icon="bolt" href="/en/enterprise/features/webhook-streaming">
    Set up real-time event notifications
  </Card>
</CardGroup>
