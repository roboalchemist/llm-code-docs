# Source: https://www.traceloop.com/docs/openllmetry/integrations/dynatrace.md

# LLM Observability with Dynatrace and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/svnZvSYnNXkA6fDZ/img/integrations/dynatrace.png?fit=max&auto=format&n=svnZvSYnNXkA6fDZ&q=85&s=552c3d2dc162abc28dd2c47759e5a06a" data-og-width="1874" width="1874" data-og-height="1117" height="1117" data-path="img/integrations/dynatrace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/svnZvSYnNXkA6fDZ/img/integrations/dynatrace.png?w=280&fit=max&auto=format&n=svnZvSYnNXkA6fDZ&q=85&s=5a573f99e2805e0807239123c343cbaa 280w, https://mintcdn.com/enrolla/svnZvSYnNXkA6fDZ/img/integrations/dynatrace.png?w=560&fit=max&auto=format&n=svnZvSYnNXkA6fDZ&q=85&s=872087acf0157c93522a2809eb36825f 560w, https://mintcdn.com/enrolla/svnZvSYnNXkA6fDZ/img/integrations/dynatrace.png?w=840&fit=max&auto=format&n=svnZvSYnNXkA6fDZ&q=85&s=c2d62dd60a08489099c99c86d9859926 840w, https://mintcdn.com/enrolla/svnZvSYnNXkA6fDZ/img/integrations/dynatrace.png?w=1100&fit=max&auto=format&n=svnZvSYnNXkA6fDZ&q=85&s=b656a85b9f736c79a82ade36468db205 1100w, https://mintcdn.com/enrolla/svnZvSYnNXkA6fDZ/img/integrations/dynatrace.png?w=1650&fit=max&auto=format&n=svnZvSYnNXkA6fDZ&q=85&s=85988430c38adec6555cfa244f4fb34a 1650w, https://mintcdn.com/enrolla/svnZvSYnNXkA6fDZ/img/integrations/dynatrace.png?w=2500&fit=max&auto=format&n=svnZvSYnNXkA6fDZ&q=85&s=03304260bfbe09dc3df4515ae014aafa 2500w" />
</Frame>

Analyze all collected LLM traces and logs within Dynatrace by using the native OpenTelemetry ingest endpoint of your Dynatrace environment.

Go to your Dynatrace environment and create a new access token under **Manage Access Tokens**.\
The access token needs the following permission scopes that allow the ingest of OpenTelemetry spans, metrics and logs
(openTelemetryTrace.ingest, metrics.ingest, logs.ingest).

Set `TRACELOOP_BASE_URL` environment variable to the URL of your Dynatrace OpenTelemetry ingest endpoint

```bash  theme={null}
TRACELOOP_BASE_URL=https://<YOUR_ENV>.live.dynatrace.com\api\v2\otlp
```

Set the `TRACELOOP_HEADERS` environment variable to include your previously created access token

```bash  theme={null}
TRACELOOP_HEADERS=Authorization=Api-Token%20<YOUR_ACCESS_TOKEN>
```

Done! All exported spans, along with their span attributes, will appear within the [Dynatrace trace view](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.genai.observability).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt