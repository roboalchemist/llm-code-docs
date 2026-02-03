# Source: https://www.aptible.com/docs/core-concepts/observability/sources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sources

# Overview

Sources allow you to relate your deployed Apps back to their source repositories, allowing you to use the Aptible Dashboard to answer the question "*what's deployed where?*"

# Configuring Sources

To connect your App with it's Source, you'll need to configure your deployment pipeline to send Source information along with your deployments. See [Linking Apps to Sources](/core-concepts/apps/deploying-apps/linking-apps-to-sources) for more details.

# The Sources List

The Sources list view displays a list of all of the Sources configured across your deployed Apps. This view is useful for finding groups of Apps that are running code from the same Source (e.g., ephemeral environments or multiple instances of a single-tenant application).

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-list.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=29499d83aef3092f29c70f273d637ca6" alt="" data-og-width="5120" width="5120" data-og-height="2560" height="2560" data-path="images/sources-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-list.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=436ac215494101cb4ded36f205c3c791 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-list.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f35d659346bb5eabad4398631354d527 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-list.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9cb592b500dd94aa38862a93ee9c1361 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-list.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=fcc3afd36832b3b5859cf6c685eee98b 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-list.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9b82fcfde539c28d73fedd4b3e0e474a 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-list.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a00be1ad957789acf920e6777be61d44 2500w" />

# Source Details

From the Source list page, you can click into a Source to see its details, including a list of Apps deployed from the Source and their current revision information

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-apps.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=917352be7d6f65ae8869ba55c3992644" alt="" data-og-width="5120" width="5120" data-og-height="2560" height="2560" data-path="images/sources-apps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-apps.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=c6d20d6030de82e209e0d800bb159ca7 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-apps.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=1221ff3e601f82dbc6e4cc277c02f87e 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-apps.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=fac1455d4e7543b765ff1cb772bc650b 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-apps.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=edef1db0ed1edd5d6dc351bde22397f9 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-apps.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=d88effdc45caff339874907486acead6 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-apps.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9cfee02abf3960dc45d95e4d48f1f750 2500w" />

You can also view the Deployments tab, which will display historical deployments and their revision information made from that Source across all of your Apps.

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-deployments.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5160d05058181de54cc4a8bb17b1e6e2" alt="" data-og-width="5120" width="5120" data-og-height="2560" height="2560" data-path="images/sources-deployments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-deployments.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9d5e225b35db71572c35bccd97509f79 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-deployments.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=34fe5fd394633cf0d6b8587774760a82 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-deployments.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=df2bf2c637a0b7399a89029ab53ec418 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-deployments.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7449a415e1573043332ececfbfcd4db3 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-deployments.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8c57b984e1b8ae09e1bf1a323e252613 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/sources-deployments.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=fb8675301d3022139a63dc5f4cb85a2d 2500w" />
