# Source: https://novita.ai/docs/guides/sandbox-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sandbox Metrics

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

The sandbox metrics allows you to get information about the sandbox's CPU and memory usage.

<SandboxConfigHint />

## Getting sandbox metrics

Getting the metrics of a sandbox returns an array of timestamped metrics containing CPU and memory usage information.
The metrics are collected at the start of the sandbox, then every 2 seconds, and finally right before the sandbox is deleted.

### Getting sandbox metrics using the SDKs

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()
  console.log('Sandbox created', sandbox.sandboxId)

  let metrics = await sandbox.getMetrics()

  // You can also get the metrics by sandbox ID:
  // const metrics = await Sandbox.getMetrics(sbx.sandboxId)

  while (metrics && metrics.length <= 1) {
      console.log('Waiting for metrics...')
      await new Promise(resolve => setTimeout(resolve, 1000))
      metrics = await sandbox.getMetrics()
  }

  console.log('Sandbox metrics:', metrics)

  // Example output:
  // Sandbox metrics: [
  //   {
  //     cpuCount: 2,
  //     cpuUsedPct: 17.85,
  //     memTotalMiB: 987,
  //     memUsedMiB: 245,
  //     timestamp: '2025-06-30T06:49:15.243Z'
  //   },
  //   {
  //     cpuCount: 2,
  //     cpuUsedPct: 0.4,
  //     memTotalMiB: 987,
  //     memUsedMiB: 246,
  //     timestamp: '2025-06-30T06:49:20.237Z'
  //   }
  // ]

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox
  import time

  sandbox = Sandbox.create()
  print('Sandbox created', sandbox.sandbox_id)

  metrics = sandbox.get_metrics()

  # You can also get the metrics by sandbox ID:
  # metrics = Sandbox.get_metrics(sbx.sandbox_id)

  while len(metrics) <= 1:
      print('Waiting for metrics...')
      time.sleep(1)
      metrics = sandbox.get_metrics()

  print('Sandbox metrics', metrics)

  # Example output:
  # Sandbox metrics [SandboxMetrics(timestamp=datetime.datetime(2025, 6, 30, 6, 51, 13, 169230, tzinfo=tzutc()), cpu_used_pct=17.87, cpu_count=2, mem_used_mib=245, mem_total_mib=987), SandboxMetrics(timestamp=datetime.datetime(2025, 6, 30, 6, 51, 18, 165258, tzinfo=tzutc()), cpu_used_pct=0.4, cpu_count=2, mem_used_mib=246, mem_total_mib=987)]

  sandbox.kill()
  ```
</CodeGroup>

### Getting sandbox metrics using the CLI

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli sandbox metrics <sandbox_id>
```

## Limitations

* It may take a second or more to get the metrics after the sandbox is created. Until the logs are collected from the sandbox, you will get an empty array.


Built with [Mintlify](https://mintlify.com).