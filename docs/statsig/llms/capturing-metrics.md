# Source: https://docs.statsig.com/integrations/azureai/capturing-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Capturing Metrics

Azure AI SDK automatically captures relevant invocation and usage metrics from each API call and logs them to Statsig.  You can see these events streaming in real-time in the console at: [https://console.statsig.com/metrics/events](https://console.statsig.com/metrics/events).

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/azureai/capturing-metrics/cb4136eb-6ae9-4ffa-b560-333f332eaa75.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=d1b08629c8d9fc342219d0175e73c8a1" alt="Statsig console events streaming interface" width="1404" height="574" data-path="images/integrations/azureai/capturing-metrics/cb4136eb-6ae9-4ffa-b560-333f332eaa75.png" />
</Frame>

### Metrics captured

Completion invocations capture the following metrics automatically: completion token length, prompt token length, latency, model name, total token length.

For example, a completion API call results in a usage log that looks like this:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/azureai/capturing-metrics/d9c150cc-eded-4607-aec8-d1631af77cec.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=45963354f06398bd1c530a7a2875d953" alt="Azure AI completion API usage log example" width="797" height="774" data-path="images/integrations/azureai/capturing-metrics/d9c150cc-eded-4607-aec8-d1631af77cec.png" />
</Frame>

These could be used to compare multiple deployments with each other, and also to run experiments against different sets of parameters, aiding in optimization of cost, responsiveness, user experience, etc.


Built with [Mintlify](https://mintlify.com).