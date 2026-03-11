# Source: https://www.courier.com/docs/tools/courier-skills.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Skills

> Agent skill packs that teach AI coding assistants Courier notification best practices.

Courier Skills is a public repository of structured guidance that AI coding agents use when building notifications. Install it once and your agent gets channel-specific rules, compliance constraints, reliability patterns, and code examples for the full Courier platform.

Works with Cursor, Claude Code, Windsurf, Cline, and any AI tool that supports agent skills.

## Installation

<Tabs>
  <Tab title="Cursor (global)">
    Available in all projects:

    ```bash  theme={null}
    git clone https://github.com/trycourier/courier-skills.git ~/.cursor/skills/courier-skills
    ```
  </Tab>

  <Tab title="Cursor (project)">
    Available in one project only:

    ```bash  theme={null}
    git clone https://github.com/trycourier/courier-skills.git .cursor/skills/courier-skills
    ```
  </Tab>

  <Tab title="Claude Code">
    ```bash  theme={null}
    git clone https://github.com/trycourier/courier-skills.git ~/.claude/skills/courier-skills
    ```

    Claude Code discovers skills from `~/.claude/skills/` automatically via `SKILL.md` frontmatter.
  </Tab>

  <Tab title="Other">
    Clone the repo into whatever skills directory your AI assistant supports, or point it at the `SKILL.md` file manually.

    ```bash  theme={null}
    git clone https://github.com/trycourier/courier-skills.git
    ```
  </Tab>
</Tabs>

## What Your Agent Learns

| Category                    | Coverage                                                                                                                                       |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **7 Channels**              | Email, SMS, push, in-app inbox, Slack, Microsoft Teams, WhatsApp; each with deliverability rules, compliance requirements, and code examples   |
| **5 Transactional Types**   | Authentication (OTP, password reset), orders, billing, appointments, account notifications; timing requirements, security rules, and templates |
| **6 Growth Types**          | Onboarding, adoption, engagement, re-engagement, referral, campaigns; consent requirements, frequency limits, and exit conditions              |
| **10 Cross-Cutting Guides** | Multi-channel routing, preferences, compliance (GDPR/TCPA/CAN-SPAM), reliability, batching, throttling, CLI usage, and reusable patterns       |

## How It Works

The skill is organized around a routing file (`SKILL.md`) that agents read first. Based on the task at hand, it directs the agent to read only the 1-2 files relevant to that task.

Each resource file follows a consistent structure:

1. **Quick Reference** at the top with hard rules, common mistakes, and copy-paste templates
2. **Detailed guidance** with explanations, examples, and edge cases
3. **Related links** to other relevant files

This means agents read the minimum necessary context rather than loading the entire skill.

### Example: agent building an OTP flow

1. Agent reads `SKILL.md`, finds the routing table
2. Routing table says: OTP/2FA -> read `authentication.md` + `sms.md`
3. Agent reads those two files, gets: 6-digit codes, 5-10 min expiry, SMS primary with email fallback, TCPA rules, idempotency key pattern, rate limits
4. Agent generates code that follows all constraints

## Code Examples

The skill includes TypeScript, Python, CLI, and curl examples for key patterns:

```bash  theme={null}
# Send with idempotency (CLI)
courier send message \
  --message.to.user_id "user-123" \
  --message.template "ORDER_CONFIRMATION" \
  --message.data '{"orderId": "12345"}'
```

```typescript  theme={null}
// Send with idempotency (TypeScript)
await courier.send({
  message: {
    to: { user_id: "user-123" },
    template: "ORDER_CONFIRMATION",
    data: { orderId: "12345" }
  }
}, {
  idempotencyKey: "order-confirmation-12345"
});
```

```python  theme={null}
# Send with idempotency (Python)
client.send(
    message={
        "to": {"user_id": "user-123"},
        "template": "ORDER_CONFIRMATION",
        "data": {"orderId": "12345"},
    },
    idempotency_key="order-confirmation-12345",
)
```

## Universal Rules

The skill enforces these constraints across all generated code:

* Never send promotional content in transactional notifications
* Never batch or delay OTP, password reset, or security alerts
* Never send SMS without TCPA-compliant consent records
* Always use idempotency keys for transactional sends
* Always respect quiet hours (10pm-8am local) unless critical
* Always use `method: "single"` unless the notification warrants all channels

## What's Next

<CardGroup cols={2}>
  <Card title="Build with AI" icon="microchip-ai" href="/tools/ai-onboarding">
    See all AI integration options: CLI, MCP, Skills, and llms.txt.
  </Card>

  <Card title="GitHub" icon="github" href="https://github.com/trycourier/courier-skills">
    Source code and full file listing.
  </Card>
</CardGroup>
