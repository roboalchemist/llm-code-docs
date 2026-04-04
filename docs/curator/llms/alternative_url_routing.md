# Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/alternative_url_routing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Alternative URL Routing

> Configure URL routing for Tableau Server connections when using reverse proxies or alternative network configurations.

Curator connects to Tableau Server to verify a user's access and permissions.

Sometimes, Tableau Server is configured to live behind a "Reverse Proxy".
There are many reasons why this configuration may be preferable.

Often, though, Reverse Proxy setups with Tableau are misconfigured.
This can lead to trusted ticket whitelisting issues.

Since the Tableau Server whitelisting for issuing a trusted ticket is based on an IP address, when proxies are
misconfigured, Tableau Server sees the proxy/load balancer, instead of Curator and rejects the ticket request.

Tableau Server requires
[tsm configuration options, gateway whitelisting and several headers](https://help.tableau.com/current/server/en-us/proxy.htm#configure-the-reverse-proxy-server)
for these API calls to work correctly.

## Working Around Reverse Proxy Setups

Usually, instead of fixing Tableau Server Reverse Proxy setups, routing Curator around them is quicker and easier.

Of course, end users should continue to be routed over the reverse proxy/load balancer.

**To configure alternative routing:**

* Go to **Integrations** > **Connections** and click on your Tableau Server connection.
* Place the *internal route* to Tableau Server in *Tableau Server URL*.
* Place the user-facing route to Tableau Server in *Alternate Tableau Server URL*.

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/reverse_proxy_alt_url.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=710819aeec5943d08539cf4c7413889f" alt="Reverse Proxy Alt URL" data-og-width="2088" width="2088" data-og-height="948" height="948" data-path="assets/images/creating_integrations/tableau_connection/reverse_proxy_alt_url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/reverse_proxy_alt_url.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=9d103e7ed129172f273ac53475448785 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/reverse_proxy_alt_url.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=183876d03a3061f8241557772a5e2c5c 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/reverse_proxy_alt_url.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=e7874138adad90a55650526f0e886672 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/reverse_proxy_alt_url.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=f5a7f2bfe2afab05a6c57080a217340d 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/reverse_proxy_alt_url.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4d5ff840d7639e123e347e1d44b66af9 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/reverse_proxy_alt_url.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=a9afda1a4405ab9893c9311006c1dc0a 2500w" />
