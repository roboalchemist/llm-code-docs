# Source: https://buildkite.com/docs/apis/webhooks/pipelines/agent-events.md

# Agent webhook events

## Events

<table>
  <thead>
    <tr><th>Event</th><th>Description</th></tr>
  </thead>
  <tbody>
    <p></p><tr>
    <th><code>agent.connected</code></th>
    <td>An agent has connected to the API</td>
  </tr>
  <tr>
    <th><code>agent.lost</code></th>
    <td>An agent has been marked as lost. This happens when Buildkite stops receiving pings from the agent</td>
  </tr>
  <tr>
    <th><code>agent.disconnected</code></th>
    <td>An agent has disconnected. This happens when the agent shuts down and disconnects from the API</td>
  </tr>
  <tr>
    <th><code>agent.stopping</code></th>
    <td>An agent is stopping. This happens when an agent is instructed to stop from the API. It first transitions to stopping and finishes any current jobs</td>
  </tr>
  <tr>
    <th><code>agent.stopped</code></th>
    <td>An agent has stopped. This happens when an agent is instructed to stop from the API. It can be graceful or forceful</td>
  </tr>
  <tr>
    <th><code>agent.blocked</code></th>
    <td>An agent has been blocked. This happens when an agent's IP address is no longer included in the agent token's <a href="/docs/pipelines/security/clusters/manage#restrict-an-agent-tokens-access-by-ip-address">allowed IP addresses</a>
</td>
  </tr>

  </tbody>
</table>

## Common event data

The following properties are sent by all events.

<table>
  <thead>
    <tr><th>Property</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>agent</code></td>
      <td><a href="/docs/apis/rest-api/agents">Agent</a></td>
      <td>The agent this notification relates to</td></tr>
    <tr>
      <td><code>sender</code></td>
      <td>String</td>
      <td>The user who created the webhook</td>
    </tr>
  </tbody>
</table>

Example request body:

```json
{
  "event": "agent.connected",
  "agent": {
    "...": "..."
  },
  "sender": {
    "id": "8a7693f8-dbae-4783-9137-84090fce9045",
    "name": "Some Person"
  }
}
```

## Agent blocked event data

The following properties are sent by the `agent.blocked` event.

<table>
  <thead>
    <tr><th>Property</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>blocked_ip</code></td>
      <td>String</td>
      <td>The blocked request IP address</td>
    </tr>
    <tr>
      <td><code>agent</code></td>
      <td><a href="/docs/apis/rest-api/agents">Agent</a></td>
      <td>The agent this notification relates to</td>
    </tr>
    <tr>
      <td><code>cluster_token</code></td>
      <td><a href="/docs/apis/rest-api/clusters/agent-tokens#token-data-model">Agent token</a></td>
      <td>The agent token used in the registration attempt</td>
    </tr>
    <tr>
      <td><code>sender</code></td>
      <td>String</td>
      <td>The user who created the webhook</td></tr>
  </tbody>
</table>

Example request body:

```json
{
  "event": "agent.blocked",
  "blocked_ip": "202.188.43.20",
  "agent": {
    "...": "..."
  },
  "cluster_token": {
    "...": "..."
  },
  "sender": {
    "id": "8a7693f8-dbae-4783-9137-84090fce9045",
    "name": "Some Person"
  }
}
```
