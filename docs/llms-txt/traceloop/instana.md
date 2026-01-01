# Source: https://www.traceloop.com/docs/openllmetry/integrations/instana.md

# LLM Observability with Instana and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/instana.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=440da9f390600f83897496beb1ed360f" data-og-width="2984" width="2984" data-og-height="2224" height="2224" data-path="img/integrations/instana.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/instana.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c6c98fcd4c26e2e109ed0bff95c78e66 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/instana.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=a3340d048a575eb1b13127db3b3e9f68 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/instana.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=dd1e15f3395622ffdc6a546e403cf247 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/instana.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=ac5202ecc51f951b1ac0e60a63683db2 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/instana.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=2e7c211504cfb884fd2b6feba761f616 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/instana.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=568db42c876613f963211a2292782db8 2500w" />
</Frame>

With Instana, you can export directly to an Instana Agent in your cluster.

The Instana Agent will report back the tracing and metrics to the Instana Backend and display them on the Instana UI.

If you are running your Instana Agent on a VM or physical machine, do the following to config:

Edit the agent config file `configuration.yaml` under the `/opt/instana/agent/etc/instana` folder.

```
cd /opt/instana/agent/etc/instana
vi configuration.yaml
```

Add the following to the file:

```
com.instana.plugin.opentelemetry:
  enabled: true
  grpc:
    enabled: true
```

Restart the Instana agent:

```
systemctl restart instana-agent.service
```

If you are running Instana Agent on OpenShift or Kubernetes, do the following to config:

In Instana Configmap, add the following content:

```yaml  theme={null}
com.instana.plugin.opentelemetry:
  enabled: true
  grpc:
    enabled: true
```

For Instana Daemonset, add the following:

```yaml  theme={null}
- mountPath: /opt/instana/agent/etc/instana/configuration-opentelemetry.yaml
  name: configuration
  subPath: configuration-opentelemetry.yaml
```

The Instana agent should be ready for OpenTelemetry data at port 4317.

Then, set this env var, and you're done!

```bash  theme={null}
TRACELOOP_BASE_URL=<instana-agent-hostname>:4317
```

Instana now supports MCP Observability. The following span attributes are available for MCP traces :
mcp.method.name
mcp.request.argument
mcp.request.id
mcp.response.value
mcp.session.init\_options

Here is the MCP traces from Instana UI:

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/mcpTraces.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0da4830bf137b6a563e3e52cc93ee8c7" data-og-width="2898" width="2898" data-og-height="1662" height="1662" data-path="img/integrations/mcpTraces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/mcpTraces.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=2c2794b2280807e2e18a1f94d0af7d5d 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/mcpTraces.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=7d5939b5c91f97ae85ac8b93f41e8c30 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/mcpTraces.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0b0db2d45a7cfd26c6c13d70469dbe08 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/mcpTraces.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=f31477e9f656609636abf6440a1b5333 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/mcpTraces.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0cf17f24a43245da05d78b4add3a6595 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/mcpTraces.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e44c49fe2d1b41a8a46c4efbeb0627c5 2500w" />
</Frame>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt