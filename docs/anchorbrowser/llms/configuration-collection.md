# Source: https://docs.anchorbrowser.io/examples/configuration-collection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration Collection

The following example shows how to collect configuration data that is not exposed through an API from a SaaS service (Grafana) configuration page.

<CodeGroup>
  ```tsx node.js theme={null}
  const result = await anchorClient.agent.task(
    'Collect the node names and their CPU average %, return in JSON array',
    {
      taskOptions: {
        url: 'https://play.grafana.org/a/grafana-k8s-app/navigation/nodes',
      }
    }
  )
  console.log(result);
  ```

  ```python python theme={null}
  result = anchor_client.agent.task(
    'Collect the node names and their CPU average %, return in JSON array',
    task_options={
      'url': 'https://play.grafana.org/a/grafana-k8s-app/navigation/nodes',
    }
  )
  print(result)
  ```
</CodeGroup>
