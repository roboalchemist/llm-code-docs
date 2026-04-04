# Source: https://www.traceloop.com/docs/openllmetry/integrations/bmc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with BMC and OpenLLMetry

BMC Helix provides the capability to export observability data directly using the OpenTelemetry Collector. This requires deploying an OpenTelemetry Collector in your cluster.

See also [BMC Helix documentation](https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Operations-Management/BMC-Helix-AIOps/aiops244/Administering/Enabling-BMC-Helix-applications-to-collect-service-traces-from-OpenTelemetry/).

Exporting Data to an OpenTelemetry Collector

```yaml  theme={null}
otlp:
  receiver:
    protocols:
      http:
        enabled: true
```

Then, set this env var, and you're done!

```bash  theme={null}
TRACELOOP_BASE_URL=http://<tenantURL>
```
