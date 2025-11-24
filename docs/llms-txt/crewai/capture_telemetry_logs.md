# Source: https://docs.crewai.com/en/enterprise/guides/capture_telemetry_logs.md

# Open Telemetry Logs

> Understand how to capture telemetry logs from your CrewAI AMP deployments

CrewAI AMP provides a powerful way to capture telemetry logs from your deployments. This allows you to monitor the performance of your agents and workflows, and to debug issues that may arise.

## Prerequisites

<CardGroup cols={2}>
  <Card title="ENTERPRISE OTEL SETUP enabled" icon="users">
    Your organization should have ENTERPRISE OTEL SETUP enabled
  </Card>

  <Card title="OTEL collector setup" icon="server">
    Your organization should have an OTEL collector setup or a provider like Datadog log intake setup
  </Card>
</CardGroup>

## How to capture telemetry logs

1. Go to settings/organization tab
2. Configure your OTEL collector setup
3. Save

Example to setup OTEL log collection capture to Datadog.

<Frame>
    <img src="https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=5bb359765661a61f7012824fe35b0978" alt="Capture Telemetry Logs" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/crewai-otel-export.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=280&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=2bee9ddb6077fca900cc42e98c1c1c77 280w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=560&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=ceae34948ba9b7daeff1a277d78f8991 560w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=840&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=3e86994eb05fe4c9005a8a62f272b618 840w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=1100&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=3b498ed5c28cb90d415721f636e16ac3 1100w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=1650&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=35463fcfaa322eacbb1e862ce638a093 1650w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=2500&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=fa9f64fe474823fedc93cfdf66d36b4b 2500w" />
</Frame>
