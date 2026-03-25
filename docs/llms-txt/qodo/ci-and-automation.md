# Source: https://docs.qodo.ai/qodo-documentation/qodo-command/features/ci-and-automation.md

# CI and Automation

### Autonomous CI Mode

Run Qodo in CI environments with the `--ci` flag:

```bash
qodo <command> --ci
```

The output logs from Qodo CLI tool will be simplified and fit for CI environments and build pipelines.

This mode runs Qodo in an autonomous mode that doesn't require the user to provide any answers to the agent.

### Webhook Mode

Run Qodo as an HTTP server to receive POST requests for each command.

```bash
qodo --webhook
```

This flag will make Qodo:

* Expose each of your configured agents as a separate POST endpoint.
* Open a server.
* Listen to POST requests that come in through the URLs.

The POST requests are validated according to the arguments available in the configured agent, and return the same return value that's set in the agent.

#### POST Example:

```bash
POST http://localhost:4000/webhook/explain
```

Returns results at end of execution.

#### SSE Mode (Live Streaming Logs)

If you add the parameter `sse=true` to the URL, a session ID will be returned. That enables you to run a GET request with the session ID.

Running a configured agent like so, you can see all the actions the agent is running behind the scenes, not just the return value.

```bash
POST http://localhost:4000/webhook/explain?sse=true

-> returns sessionId

GET http://localhost:4000/webhook/sse/explain?sessionId=<ID>
```

### Run Agent in MCP Mode

When you run Qodo CLI tool in MCP mode using the `--mcp` flag, it transforms into a server that exposes all configured agents (only those with a description) as callable tools.

```bash
qodo --mcp
```

Each of the configured agents becomes accessible through a streamable HTTP URL, allowing external systems to trigger them easily.

As the server processes a request, it can send real-time progress notifications and eventually returns the final result of the execution.

This allows you to seamlessly integrate your agents with other tools or platforms without the need to share API keys, as all execution and access are handled securely through the Qodo CLI tool server itself.

### GitHub Action

You can utilize [Qodo CLI tool's GitHub Action](https://github.com/qodo-ai/qodo-gen-cli/blob/main/action.yml) for your CI needs.
