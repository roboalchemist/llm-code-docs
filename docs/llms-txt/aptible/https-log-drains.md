# Source: https://www.aptible.com/docs/core-concepts/observability/logs/log-drains/https-log-drains.md

# HTTPS Log Drains

# Overview

Aptible can deliver your logs via HTTPS.

The logs are delivered via HTTPS POST, using a JSON `Content-Type`.

# Payload

The payload is structured as follows. New keys may be added over time, and logs from [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions) include additional keys.

```json  theme={null}
{
  "@timestamp": "2017-01-11T11:11:11.111111111Z",
  "log": "some log line from your app",
  "stream": "stdout",
  "time": "2017-01-11T11:11:11.111111111Z",
  "@version": "1",
  "type": "json",
  "file": "/tmp/dockerlogs/containerId/containerId-json.log",
  "host": "containerId",
  "offset": "123",
  "layer": "app",
  "service": "app-web",
  "app": "app",
  "app_id": "456",
  "source": "app",
  "container": "containerId"
}
```

# Specific Metadata

Both [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions) and [Endpoint Logs](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs) contain additional metadata; see the appropriate documentation for further details.

# Get Started

<Card title="Setting up a HTTP Log Drain on Aptible" icon="books" iconType="duotone" href="https://www.aptible.com/docs/self-hosted-https-log-drain">
  Step-by-step instructions on setting up logging to an HTTP Log Drain on Aptible
</Card>
