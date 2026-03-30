# Source: https://developers.make.com/mcp-server/connect-using-mcp-token/scenarios-as-tools-access-control.md

# Scenarios as tools access control

By default, the `mcp:use` scope of your MCP token allows AI systems to access all **active** and **on-demand** scenarios across all of your Make organizations. If you want to restrict access, append query parameters to the connection URL according to these levels:&#x20;

* Organization
* Team
* Scenario

Scenarios must be **active** with **on-demand** scheduling to be discoverable as MCP tools.&#x20;

{% hint style="warning" %}
The following applies only to scenario tools, and excludes management tools and other tool types.&#x20;
{% endhint %}

### **Organization level**

`https://<MAKE_ZONE>/mcp/u/<MCP_TOKEN>/stateless?organizationId=<id>`

The AI system can access all scenarios in any team within the specified organization.

### **Team level**

`https://<MAKE_ZONE>/mcp/u/<MCP_TOKEN>/stateless?teamId=<id>`&#x20;

The AI system can access all scenarios within the specified team.

### Scenario level

`https://<MAKE_ZONE>/mcp/u/<MCP_TOKEN>/stateless?scenarioId=<id>`&#x20;

The AI system can only access the specified scenario.

{% hint style="success" %}
If you experience connection issues, you can add  `/stream`  instead of `/stateless` in the connection URL. For SSE, add  `/sse`  instead.&#x20;
{% endhint %}

{% hint style="success" %}
&#x20;You can also specify multiple values for each of the entities above using the following syntax:\
&#x20;`?scenarioId[]=<id1>&scenarioId[]=<id2>`
{% endhint %}

{% hint style="warning" %}
You can't combine multiple levels, as levels are mutually exclusive.
{% endhint %}
