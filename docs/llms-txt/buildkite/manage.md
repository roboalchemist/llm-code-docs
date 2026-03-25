# Source: https://buildkite.com/docs/package-registries/registries/manage.md

# Source: https://buildkite.com/docs/pipelines/security/clusters/rules/manage.md

# Source: https://buildkite.com/docs/pipelines/security/clusters/manage.md

# Manage clusters

This page provides details on how to manage [clusters](/docs/pipelines/glossary#cluster) within your Buildkite organization.

Learn more about on how to set up queues within a cluster in [Manage queues](/docs/agent/queues/managing).

## Setting up clusters

When a new Buildkite organization is created, a single default cluster (initially named **Default cluster**) is also created.

For smaller organizations, working on smaller projects, this default cluster may be sufficient. However, it's usually more convenient for large organizations to manage projects in separate clusters, when these projects require different:

- Source code visibility, such as open-source versus closed-source code projects.
- Expertise and ownership, such as Android developers, macOS developers, Windows developers, Machine Learning expert etc.
- Multiple projects, for example, different product lines.

Once your clusters are set up, you can set up one or more [queues](/docs/agent/queues/managing) within each cluster.

## Create a cluster

New clusters can be created by a [_Buildkite organization administrator_](/docs/pipelines/security/permissions#manage-teams-and-permissions-organization-level-permissions) using the [**Clusters** page](#create-a-cluster-using-the-buildkite-interface), as well as Buildkite's [REST API](#create-a-cluster-using-the-rest-api) or [GraphQL API](#create-a-cluster-using-the-graphql-api).

Once the cluster has been created, a Buildkite organization administrator can then make other members of their Buildkite organization a [_maintainer_](#manage-maintainers-on-a-cluster) of the cluster. These people can then administer the cluster on behalf of the Buildkite organization administrator.

### Using the Buildkite interface

To create a new cluster using the Buildkite interface:

1. Select **Agents** in the global navigation to access the **Clusters** page.
1. Select **Create a Cluster**.
1. On the **New Cluster** page, enter the mandatory **Name** for the new cluster.
1. Enter an optional **Description** for the cluster. This description appears under the name of the cluster in its tile on the **Clusters** page.
1. Enter an optional **Emoji** and **Color** using the recommended syntax. This emoji appears next to the cluster's name and the color (in hex code syntax, for example, `#FFE0F1`) provides the background color for this emoji.
1. Select **Create Cluster**.

    The new cluster's page is displayed on its **Queues** page, indicating the cluster's name and its default queue, named **queue**. From this page, you can set up one or more additional [queues](/docs/agent/queues/managing) within this cluster.

### Using the REST API

To [create a new cluster](/docs/apis/rest-api/clusters#clusters-create-a-cluster) using the [REST API](/docs/apis/rest-api), run the following example `curl` command:

```bash
curl -H "Authorization: Bearer $TOKEN" \
  -X POST "https://api.buildkite.com/v2/organizations/{org.slug}/clusters" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Open Source",
    "description": "A place for safely running our open source builds",
    "emoji": "\:technologist\:",
    "color": "#FFE0F1"
  }'
```

where:

<ul>
<li>
<code>$TOKEN</code> is an <a href="https://buildkite.com/user/api-access-tokens">API access token</a> scoped to the relevant <strong>Organization</strong> and <strong>REST API Scopes</strong> that your request needs access to in Buildkite.</li>
</ul>

<ul>
<li>
<p><code>{org.slug}</code> can be obtained:</p>

<ul>
<li>From the end of your Buildkite URL, after accessing <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
<li>
<p>By running the <a href="/docs/apis/rest-api/organizations#list-organizations">List organizations</a> REST API query to obtain this value from <code>slug</code> in the response. For example:</p>
<div class="highlight"><pre class="highlight shell"><code>curl <span class="nt">-H</span> <span class="s2">"Authorization: Bearer </span><span class="nv">$TOKEN</span><span class="s2">"</span> <span class="se">\</span>
  <span class="nt">-X</span> GET <span class="s2">"https://api.buildkite.com/v2/organizations"</span>
</code></pre></div>
</li>
</ul>
</li>
</ul>

<ul>
<li><p><code>name</code> (required) is the name for the new cluster.</p></li>
<li><p><code>description</code> (optional) is the description that appears under the name of cluster in its tile on the <strong>Clusters</strong> page.</p></li>
<li><p><code>emoji</code> (optional) is the emoji that appears next to the cluster's name in the Buildkite interface and uses the example syntax above.</p></li>
<li><p><code>color</code> (optional) provides the background color for this emoji and uses hex code syntax (for example, <code>#FFE0F1</code>).</p></li>
</ul>

<section class="callout callout--info">
  <p class="callout__title"><a class="callout__anchor" href="#a-default-queue-is-not-automatically-created" id="a-default-queue-is-not-automatically-created"> A default queue is not automatically created</a></p>
  <p>Unlike creating a new cluster through the <a href="#create-a-cluster-using-the-buildkite-interface">Buildkite interface</a>, a default queue is not automatically created using this API call. To create a new/default queue for any new cluster created through an API call, you need to manually <a href="/docs/agent/queues/managing#create-a-self-hosted-queue">create a new queue</a>.</p>
</section>

### Using the GraphQL API

To [create a new cluster](/docs/apis/graphql/schemas/mutation/clustercreate) using the [GraphQL API](/docs/apis/graphql-api), run the following example mutation:

```graphql
mutation {
  clusterCreate(
    input: {
      organizationId: "organization-id"
      name: "Open Source"
      description: "A place for safely running our open source builds"
      emoji: "\:technologist\:"
      color: "#FFE0F1"
    }
  ) {
    cluster {
      id
      uuid
      name
      description
      emoji
      color
      defaultQueue {
        id
      }
      createdBy {
        id
        uuid
        name
        email
        avatar {
          url
        }
      }
    }
  }
}
```

where:

<ul>
<li>
<p><code>organizationId</code> (required) can be obtained:</p>

<ul>
<li>From the <strong>GraphQL API Integration</strong> section of your <strong>Organization Settings</strong> page, accessed by selecting <strong>Settings</strong> in the global navigation of your organization in Buildkite.</li>
<li>
<p>By running a <code>getCurrentUsersOrgs</code> GraphQL API query to obtain the organization slugs for the current user's accessible organizations, followed by a <a href="/docs/apis/graphql/schemas/query/organization">getOrgId</a> query, to obtain the organization's <code>id</code> using the organization's slug. For example:</p>

<p>Step 1. Run <code>getCurrentUsersOrgs</code> to obtain the organization slug values in the response for the current user's accessible organizations:</p>
<div class="highlight"><pre class="highlight graphql"><code><span class="k">query</span><span class="w"> </span><span class="n">getCurrentUsersOrgs</span><span class="w"> </span><span class="p">{</span><span class="w">
  </span><span class="n">viewer</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="n">organizations</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="n">edges</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="n">node</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="n">name</span><span class="w">
          </span><span class="n">slug</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div>
<p>Step 2. Run <code>getOrgId</code> with the appropriate slug value above to obtain this organization's <code>id</code> in the response:</p>
<div class="highlight"><pre class="highlight graphql"><code><span class="k">query</span><span class="w"> </span><span class="n">getOrgId</span><span class="w"> </span><span class="p">{</span><span class="w">
  </span><span class="n">organization</span><span class="p">(</span><span class="n">slug</span><span class="p">:</span><span class="w"> </span><span class="s2">"organization-slug"</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="n">id</span><span class="w">
    </span><span class="n">uuid</span><span class="w">
    </span><span class="n">slug</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div>
<p><strong>Note:</strong> The <code>organization-slug</code> value can also be obtained from the end of your Buildkite URL, by selecting <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</p>
</li>
</ul>
</li>
</ul>

<ul>
<li><p><code>name</code> (required) is the name for the new cluster.</p></li>
<li><p><code>description</code> (optional) is the description that appears under the name of cluster in its tile on the <strong>Clusters</strong> page.</p></li>
<li><p><code>emoji</code> (optional) is the emoji that appears next to the cluster's name in the Buildkite interface and uses the example syntax above.</p></li>
<li><p><code>color</code> (optional) provides the background color for this emoji and uses hex code syntax (for example, <code>#FFE0F1</code>).</p></li>
</ul>

<section class="callout callout--info">
  <p class="callout__title"><a class="callout__anchor" href="#a-default-queue-is-not-automatically-created" id="a-default-queue-is-not-automatically-created"> A default queue is not automatically created</a></p>
  <p>Unlike creating a new cluster through the <a href="#create-a-cluster-using-the-buildkite-interface">Buildkite interface</a>, a default queue is not automatically created using this API call. To create a new/default queue for any new cluster created through an API call, you need to manually <a href="/docs/agent/queues/managing#create-a-self-hosted-queue">create a new queue</a>.</p>
</section>

## Connect agents to a cluster

Agents are associated with a cluster through the cluster's agent tokens. Learn more about this in [Agent tokens](/docs/agent/self-hosted/tokens).

Once you have [created your required agent token/s](/docs/agent/self-hosted/tokens#create-a-token), [use them](/docs/agent/self-hosted/tokens#using-and-storing-tokens) with the relevant agents, along with an optional [tag representing the relevant queue in your cluster](/docs/agent/queues#assigning-a-self-hosted-agent-to-a-queue).

You can also create, edit, and revoke other agent tokens from the cluster’s **Agent tokens**.

## Migrate unclustered agents to a cluster

Unclustered agents are agents associated with the **Unclustered** area of the **Clusters** page in a Buildkite organization. Learn more about unclustered agents in [Working with unclustered agent tokens](/docs/agent/self-hosted/tokens#working-with-unclustered-agent-tokens).

Migrating unclustered agents to a cluster allows those agents to use [agent tokens](/docs/agent/self-hosted/tokens) that connect to Buildkite via a cluster, which can be managed by users with [cluster maintainer](/docs/pipelines/security/clusters/manage#manage-maintainers-on-a-cluster) privileges.

> 📘 Buildkite organizations created after February 26, 2024
> Buildkite organizations created after this date will not have an **Unclustered** area. Therefore, this process is not required for these newer Buildkite organizations.

Learn more about this entire process from the detailed [Migrate from unclustered to clustered agents](/docs/pipelines/security/clusters/migrate-from-unclustered-to-clustered-agents) guide, which guides you through the individual processes of:

1. [Assessing your current environment](/docs/pipelines/security/clusters/migrate-from-unclustered-to-clustered-agents#assessing-your-current-environment).
1. Deciding on an [agent migration strategy](/docs/pipelines/security/clusters/migrate-from-unclustered-to-clustered-agents#migration-strategies), noting that an initial [single-cluster migration strategy](/docs/pipelines/security/clusters/migrate-from-unclustered-to-clustered-agents#single-cluster-migration-overview) may likely provide the least friction.
1. Understanding the [technical considerations](/docs/pipelines/security/clusters/migrate-from-unclustered-to-clustered-agents#technical-considerations) of the agent migration process.
1. The [agent migration process](/docs/pipelines/security/clusters/migrate-from-unclustered-to-clustered-agents#agent-migration-process) itself.

## Restrict an agent token's access by IP address

As a security measure, each agent token has an optional **Allowed IP Addresses** setting that can be used to lock down access to the token. When this option is set on an agent token, only agents with an IP address that matches one this agent token's setting can use this token to connect to your Buildkite organization (through your cluster).

An agent token's **Allowed IP Addresses** setting can be set [when the token is created](/docs/agent/self-hosted/tokens#create-a-token), or this setting can be added to or modified on existing agent tokens by a [cluster maintainer](#manage-maintainers-on-a-cluster) or Buildkite organization administrator, using the [**Agent Tokens** page of a cluster](#restrict-an-agent-tokens-access-by-ip-address-using-the-buildkite-interface), as well as Buildkite's [REST API](#restrict-an-agent-tokens-access-by-ip-address-using-the-rest-api) or [GraphQL API](#restrict-an-agent-tokens-access-by-ip-address-using-the-graphql-api).

For these API requests, the _cluster ID_ value submitted in the request is the target cluster the token is associated with.

> 🚧 Changing the **Allowed IP Addresses** setting
> Modifying an agent token's **Allowed IP Addresses** setting forcefully disconnects any existing agents (using this token) with an IP address that no longer matches one of the values of this updated setting. This will prevent the completion of any jobs in progress on those agents.

To remove this IP address restriction from an agent's token, explicitly set its **Allowed IP Addresses** value to its default value of `0.0.0.0/0`.

Be aware that an agent token's **Allowed IP Addresses** setting also has the following limitations:

- Access to the [Metrics API](/docs/apis/agent-api/metrics) for this agent token is not restricted.
- There is a maximum of 24 CIDR blocks per agent token.
- IPv6 is currently not supported.

### Using the Buildkite interface

To restrict an existing agent token's access by IP address (via the token's **Allowed IP Addresses** setting) using the Buildkite interface:

1. Select **Agents** in the global navigation to access the **Clusters** page.
1. Select the cluster associated with the agent token.
1. Select **Agent Tokens** and expand the agent token whose **Allowed IP Addresses** setting is to be added or modified.
1. Select **Edit**.
1. Update the **Allowed IP Addresses** setting, using space-separated [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) to the IP addresses which agents must be accessible through.
1. Select **Save Token**.

### Using the REST API

To restrict an existing agent token's access by IP address using the REST API, run the following example `curl` command to [update this agent token](/docs/apis/rest-api/clusters/agent-tokens#update-a-token):

```bash
curl -H "Authorization: Bearer $TOKEN" \
  -X PUT "https://api.buildkite.com/v2/organizations/{org.slug}/clusters/{cluster.id}/tokens/{id}" \
  -H "Content-Type: application/json" \
  -d '{ "allowed_ip_addresses": "192.0.2.0/24 198.51.100.12" }'
```

where:

<ul>
<li>
<code>$TOKEN</code> is an <a href="https://buildkite.com/user/api-access-tokens">API access token</a> scoped to the relevant <strong>Organization</strong> and <strong>REST API Scopes</strong> that your request needs access to in Buildkite.</li>
</ul>

<ul>
<li>
<p><code>{org.slug}</code> can be obtained:</p>

<ul>
<li>From the end of your Buildkite URL, after accessing <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
<li>
<p>By running the <a href="/docs/apis/rest-api/organizations#list-organizations">List organizations</a> REST API query to obtain this value from <code>slug</code> in the response. For example:</p>
<div class="highlight"><pre class="highlight shell"><code>curl <span class="nt">-H</span> <span class="s2">"Authorization: Bearer </span><span class="nv">$TOKEN</span><span class="s2">"</span> <span class="se">\</span>
  <span class="nt">-X</span> GET <span class="s2">"https://api.buildkite.com/v2/organizations"</span>
</code></pre></div>
</li>
</ul>
</li>
</ul>

<ul>
<li>
<p><code>{cluster.id}</code> can be obtained:</p>

<ul>
<li>From the <strong>Cluster Settings</strong> page of your target cluster. To do this:

<ol>
<li>Select <strong>Agents</strong> (in the global navigation) &gt; the specific cluster &gt; <strong>Settings</strong>.</li>
<li>Once on the <strong>Cluster Settings</strong> page, copy the <code>id</code> parameter value from the <strong>GraphQL API Integration</strong> section, which is the <code>{cluster.id}</code> value.</li>
</ol>
</li>
<li>
<p>By running the <a href="/docs/apis/rest-api/clusters#clusters-list-clusters">List clusters</a> REST API query and obtain this value from the <code>id</code> in the response associated with the name of your target cluster (specified by the <code>name</code> value in the response). For example:</p>
<div class="highlight"><pre class="highlight shell"><code>curl <span class="nt">-H</span> <span class="s2">"Authorization: Bearer </span><span class="nv">$TOKEN</span><span class="s2">"</span> <span class="se">\</span>
  <span class="nt">-X</span> GET <span class="s2">"https://api.buildkite.com/v2/organizations/<span class="o">{org.slug}</span>/clusters"</span>
</code></pre></div>
</li>
</ul>
</li>
</ul>

<ul>
<li>
<p><code>{id}</code> is that of the agent token, whose value can be obtained:</p>

<ul>
<li>
<p>From the Buildkite URL path when editing the agent token. To do this:</p>

<ul>
<li>Select <strong>Agents</strong> (in the global navigation) &gt; the specific cluster &gt; <strong>Agent Tokens</strong> &gt; expand the agent token &gt; <strong>Edit</strong>.</li>
<li>Copy the ID value between <code>/tokens/</code> and <code>/edit</code> in the URL.</li>
</ul>
</li>
<li>
<p>By running the <a href="/docs/apis/rest-api/clusters/agent-tokens#list-tokens">List tokens</a> REST API query and obtain this value from the <code>id</code> in the response associated with the description of your token (specified by the <code>description</code> value in the response). For example:</p>
<div class="highlight"><pre class="highlight shell"><code>curl <span class="nt">-H</span> <span class="s2">"Authorization: Bearer </span><span class="nv">$TOKEN</span><span class="s2">"</span> <span class="se">\\</span>
  <span class="nt">-X</span> GET <span class="s2">"https://api.buildkite.com/v2/organizations/<span class="o">{org.slug}</span>/clusters/<span class="o">{cluster.id}</span>/tokens"</span>
</code></pre></div>
</li>
</ul>
</li>
</ul>

- `allowed_ip_addresses` is/are the IP addresses which agents must be accessible through to access this agent token and be able to connect to Buildkite via your cluster. Use space-separated [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) to enter IP addresses for this field value.

### Using the GraphQL API

To restrict an existing agent token's access by IP address using the [GraphQL API](/docs/apis/graphql-api), run the following example mutation to [update this agent token](/docs/apis/graphql/schemas/mutation/clusteragenttokenupdate):

```graphql
mutation {
  clusterAgentTokenUpdate(
    input: {
      organizationId: "organization-id"
      id: "token-id"
      description: "A description"
      allowedIpAddresses: "202.144.0.0/24 198.51.100.12"
    }
  ) {
    clusterAgentToken {
      id
      uuid
      description
      allowedIpAddresses
      cluster {
        id
        uuid
        organization {
          id
          uuid
        }
      }
      createdBy {
        id
        uuid
        email
      }
    }
  }
}
```

where:

<ul>
<li>
<p><code>organizationId</code> (required) can be obtained:</p>

<ul>
<li>From the <strong>GraphQL API Integration</strong> section of your <strong>Organization Settings</strong> page, accessed by selecting <strong>Settings</strong> in the global navigation of your organization in Buildkite.</li>
<li>
<p>By running a <code>getCurrentUsersOrgs</code> GraphQL API query to obtain the organization slugs for the current user's accessible organizations, followed by a <a href="/docs/apis/graphql/schemas/query/organization">getOrgId</a> query, to obtain the organization's <code>id</code> using the organization's slug. For example:</p>

<p>Step 1. Run <code>getCurrentUsersOrgs</code> to obtain the organization slug values in the response for the current user's accessible organizations:</p>
<div class="highlight"><pre class="highlight graphql"><code><span class="k">query</span><span class="w"> </span><span class="n">getCurrentUsersOrgs</span><span class="w"> </span><span class="p">{</span><span class="w">
  </span><span class="n">viewer</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="n">organizations</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="n">edges</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="n">node</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="n">name</span><span class="w">
          </span><span class="n">slug</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div>
<p>Step 2. Run <code>getOrgId</code> with the appropriate slug value above to obtain this organization's <code>id</code> in the response:</p>
<div class="highlight"><pre class="highlight graphql"><code><span class="k">query</span><span class="w"> </span><span class="n">getOrgId</span><span class="w"> </span><span class="p">{</span><span class="w">
  </span><span class="n">organization</span><span class="p">(</span><span class="n">slug</span><span class="p">:</span><span class="w"> </span><span class="s2">"organization-slug"</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="n">id</span><span class="w">
    </span><span class="n">uuid</span><span class="w">
    </span><span class="n">slug</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div>
<p><strong>Note:</strong> The <code>organization-slug</code> value can also be obtained from the end of your Buildkite URL, by selecting <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</p>
</li>
</ul>
</li>
</ul>

<ul>
<li>
<p><code>id</code> (required) is that of the agent token, whose value can only be obtained using the APIs, by running a <a href="/docs/apis/graphql/schemas/query/organization">getClustersAgentTokenIds</a> query, to obtain the organization's clusters and each of their agent tokens' <code>id</code> values in the response. For example:</p>
<div class="highlight"><pre class="highlight graphql"><code><span class="w">  </span><span class="k">query</span><span class="w"> </span><span class="n">getClustersAgentTokenIds</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="n">organization</span><span class="p">(</span><span class="n">slug</span><span class="p">:</span><span class="w"> </span><span class="s2">"organization-slug"</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="n">clusters</span><span class="p">(</span><span class="n">first</span><span class="p">:</span><span class="w"> </span><span class="mi">10</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="n">edges</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="n">node</span><span class="w"> </span><span class="p">{</span><span class="w">
            </span><span class="n">name</span><span class="w">
            </span><span class="n">id</span><span class="w">
            </span><span class="n">agentTokens</span><span class="p">(</span><span class="n">first</span><span class="p">:</span><span class="w"> </span><span class="mi">10</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w">
              </span><span class="n">edges</span><span class="w"> </span><span class="p">{</span><span class="w">
                </span><span class="n">node</span><span class="w"> </span><span class="p">{</span><span class="w">
                  </span><span class="n">description</span><span class="w">
                  </span><span class="n">id</span><span class="w">
                </span><span class="p">}</span><span class="w">
              </span><span class="p">}</span><span class="w">
            </span><span class="p">}</span><span class="w">
          </span><span class="p">}</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span></code></pre></div>
</li>
</ul>

- <p><code>description</code> (required) should clearly identify the environment the token is intended to be used for (for example, <code>Read-only token for static site generator</code>), as it is listed on the <strong>Agent tokens</strong> page of your specific cluster the agent connects to. To access this page, select <strong>Agents</strong> (in the global navigation) &gt; the specific cluster &gt; <strong>Agent Tokens</strong>.</p>

    If you do not need to change the existing `description` value, specify the existing field value in the request.

- `allowedIpAddresses` is/are the IP addresses which agents must be accessible through to access this agent token and be able to connect to Buildkite via your cluster. Use space-separated [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) to enter IP addresses for this field value.

## Manage maintainers on a cluster

A user who is a [_Buildkite organization administrator_](/docs/pipelines/security/permissions#manage-teams-and-permissions-organization-level-permissions) can [create clusters](#create-a-cluster). As a Buildkite organization administrator, you can add and manage other users or teams in your Buildkite organization as _maintainers_ of a cluster in the organization.

A cluster maintainer can:

- Update or delete the cluster.
- Manage [agent tokens](/docs/agent/self-hosted/tokens) associated with the cluster.
- Manage [queues](/docs/agent/queues/managing) within the cluster.
- Add pipelines to or remove them from the cluster.
- Stop, pause and resume agents belonging to a queue within the cluster.
- Manage [Buildkite secrets](/docs/pipelines/security/secrets/buildkite-secrets) associated with the cluster.

> 📘
> Learn more about Buildkite organization administrators and user permissions in Buildkite from [User and team permissions](/docs/platform/team-management/permissions).

To add a maintainer to a cluster:

1. Select **Agents** in the global navigation to access the **Clusters** page.
1. Select the cluster whose user or team is to be added as a maintainer of this cluster.
1. Select **Maintainers** > **Add Maintainer**.
1. Select if the maintainer will either be a specific **User** or **Team** of users.
1. Select the specific user or team from the dropdown list.
1. Select **Add Maintainer** and the user or team is listed on the **Maintainers** page.

To remove a maintainer from a cluster:

1. From the cluster's **Maintainers** page, select **Remove** from the user or team to be removed as a maintainer.
1. Select **OK** to confirm this action.

## Move a pipeline to a specific cluster

Move a pipeline to a specific cluster to ensure the pipeline's builds run only on agents connected to that cluster.

> 📘 Associating pipelines with cluster
> A pipeline can only be associated with one cluster at a time. It is not possible to associate a pipeline with two or more clusters simultaneously.

A pipeline can be moved to a cluster by a [cluster maintainer](#manage-maintainers-on-a-cluster) or Buildkite organization administrator via the pipeline's [**General** settings page](#move-a-pipeline-to-a-specific-cluster-using-the-buildkite-interface), as well as Buildkite's [REST API](#move-a-pipeline-to-a-specific-cluster-using-the-rest-api) or [GraphQL API](#move-a-pipeline-to-a-specific-cluster-using-the-graphql-api).

For these API requests, the _cluster ID_ value submitted in the request is the target cluster the pipeline is being moved to.

### Using the Buildkite interface

To move a pipeline to a specific cluster using the Buildkite interface:

1. Select **Pipelines** in the global navigation to access your organization's list of accessible pipelines.
1. Select the pipeline to be moved to a specific cluster.
1. Select **Settings** to open the pipeline's **General** settings page.
1. On this page, select **Change Cluster** in the **Cluster** section of this page.
1. Select the specific target cluster in the dialog and select **Change**.

    The pipeline's **General** settings page indicates the current cluster the pipeline is associated with. The pipeline will also be visible and accessible from the cluster's **Pipelines** page.

### Using the REST API

To [move a pipeline to a specific cluster](/docs/apis/rest-api/pipelines#update-a-pipeline) using the [REST API](/docs/apis/rest-api), run the following `curl` command:

```bash
curl -H "Authorization: Bearer $TOKEN" \
  -X PATCH "https://api.buildkite.com/v2/organizations/{org.slug}/pipelines/{slug}" \
  -H "Content-Type: application/json" \
  -d '{ "cluster_id": "xxx" }'
```

where:

<ul>
<li>
<code>$TOKEN</code> is an <a href="https://buildkite.com/user/api-access-tokens">API access token</a> scoped to the relevant <strong>Organization</strong> and <strong>REST API Scopes</strong> that your request needs access to in Buildkite.</li>
</ul>

<ul>
<li>
<p><code>{org.slug}</code> can be obtained:</p>

<ul>
<li>From the end of your Buildkite URL, after accessing <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
<li>
<p>By running the <a href="/docs/apis/rest-api/organizations#list-organizations">List organizations</a> REST API query to obtain this value from <code>slug</code> in the response. For example:</p>
<div class="highlight"><pre class="highlight shell"><code>curl <span class="nt">-H</span> <span class="s2">"Authorization: Bearer </span><span class="nv">$TOKEN</span><span class="s2">"</span> <span class="se">\</span>
  <span class="nt">-X</span> GET <span class="s2">"https://api.buildkite.com/v2/organizations"</span>
</code></pre></div>
</li>
</ul>
</li>
</ul>

- `{slug}` can be obtained:

  - From the end of your Buildkite URL, after accessing **Pipelines** in the global navigation of your organization in Buildkite, then accessing the specific pipeline to be moved to the cluster.

  - By running the [List pipelines](/docs/apis/rest-api/pipelines#list-pipelines) REST API query to obtain this value from `slug` in the response from the specific pipeline. For example:

        ```bash
        curl -H "Authorization: Bearer $TOKEN" \
          -X GET "https://api.buildkite.com/v2/organizations/{org.slug}/pipelines"
        ```

<ul>
<li>
<p><code>cluster_id</code> can be obtained:</p>

<ul>
<li>From the <strong>Cluster Settings</strong> page of your target cluster. To do this:

<ol>
<li>Select <strong>Agents</strong> (in the global navigation) &gt; the specific cluster &gt; <strong>Settings</strong>.</li>
<li>Once on the <strong>Cluster Settings</strong> page, copy the <code>id</code> parameter value from the <strong>GraphQL API Integration</strong> section, which is the <code>cluster_id</code> value.</li>
</ol>
</li>
<li>
<p>By running the <a href="/docs/apis/rest-api/clusters#clusters-list-clusters">List clusters</a> REST API query and obtain this value from the <code>id</code> in the response associated with the name of your target cluster (specified by the <code>name</code> value in the response). For example:</p>
<div class="highlight"><pre class="highlight shell"><code>curl <span class="nt">-H</span> <span class="s2">"Authorization: Bearer </span><span class="nv">$TOKEN</span><span class="s2">"</span> <span class="se">\</span>
  <span class="nt">-X</span> GET <span class="s2">"https://api.buildkite.com/v2/organizations/<span class="o">{org.slug}</span>/clusters"</span>
</code></pre></div>
</li>
</ul>
</li>
</ul>

### Using the GraphQL API

To [move a pipeline to a specific cluster](/docs/apis/graphql/schemas/mutation/pipelineupdate) using the [GraphQL API](/docs/apis/graphql-api), run the following mutation:

```curl
mutation {
  pipelineUpdate(
    input: {
      id: "pipeline-id"
      clusterId: "cluster-id"
    }
  ) {
    pipeline {
      id
      uuid
      name
      description
      slug
      createdAt
      cluster {
        id
        uuid
        name
        description
      }
    }
  }
}
```

where:

- `id` (required) is that of the pipeline to be moved, whose value can be obtained:

  - From the pipeline's **General** settings page. To do this:
        1. Select **Pipelines** in the global navigation > the specific pipeline to be moved to the cluster > **Settings**.
        1. Copy the **ID** shown in the **GraphQL API Integration** section of this page, which is this `id` value.

  - By running the `getCurrentUsersOrgs` GraphQL API query to obtain the organization slugs for the current user's accessible organizations, then [getOrgPipelines](/docs/apis/graphql/schemas/query/organization) query to obtain the pipeline's `id` in the response. For example:

        Step 1. Run `getCurrentUsersOrgs` to obtain the organization slug values in the response for the current user's accessible organizations:

        ```graphql
        query getCurrentUsersOrgs {
          viewer {
            organization {
              edges {
                node {
                  name
                  slug
                }
              }
            }
          }
        }
        ```

        Step 2. Run `getOrgPipelines` with the appropriate slug value above to obtain this organization's `id` in the response:

        ```graphql
        query getOrgPipelines {
          organization(slug: "organization-slug") {
            pipelines(first: 100) {
              edges {
                node {
                  id
                  uuid
                  name
                }
              }
            }
          }
        }
        ```

<ul>
<li>
<p><code>clusterId</code> (required) can be obtained:</p>

<ul>
<li>From the <strong>Cluster Settings</strong> page of your target cluster. To do this:

<ol>
<li>Select <strong>Agents</strong> (in the global navigation) &gt; the specific cluster &gt; <strong>Settings</strong>.</li>
<li>Once on the <strong>Cluster Settings</strong> page, copy the <code>cluster</code> parameter value from the <strong>GraphQL API Integration</strong> section, which is the <code>cluster.id</code> value.</li>
</ol>
</li>
<li>
<p>By running the <a href="/docs/apis/graphql/cookbooks/clusters#list-clusters">List clusters</a> GraphQL API query and obtain this value from the <code>id</code> in the response associated with the name of your target cluster (specified by the <code>name</code> value in the response). For example:</p>
<div class="highlight"><pre class="highlight graphql"><code><span class="k">query</span><span class="w"> </span><span class="n">getClusters</span><span class="w"> </span><span class="p">{</span><span class="w">
  </span><span class="n">organization</span><span class="p">(</span><span class="n">slug</span><span class="p">:</span><span class="w"> </span><span class="s2">"organization-slug"</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="n">clusters</span><span class="p">(</span><span class="n">first</span><span class="p">:</span><span class="w"> </span><span class="mi">10</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="n">edges</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="n">node</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="n">id</span><span class="w">
          </span><span class="n">name</span><span class="w">
          </span><span class="n">uuid</span><span class="w">
          </span><span class="n">color</span><span class="w">
          </span><span class="n">description</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div>
</li>
</ul>
</li>
</ul>

## Cluster insights

The cluster insights page provides an overview on the overall health of your cluster and agent set-up. Learn more in [Cluster insights](/docs/pipelines/insights/clusters).
