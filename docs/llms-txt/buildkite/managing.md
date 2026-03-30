# Source: https://buildkite.com/docs/pipelines/security/secrets/managing.md

# Source: https://buildkite.com/docs/agent/queues/managing.md

# Managing queues

This page provides details on how to manage queues within a [cluster](/docs/pipelines/security/clusters/manage) of your Buildkite organization.

## Setting up queues

A [_queue_](/docs/pipelines/glossary#queue) defines and manages [Buildkite agents](/docs/agent) within a cluster. When a new Buildkite organization is created, along with the automatically created [default cluster](/docs/pipelines/security/clusters/manage#setting-up-clusters) (named **Default cluster**), a default queue (named **default-queue**) within this cluster is also created.

A cluster can be configured with multiple queues. Each queue can be used for workload routing to specific combinations of your [build/agent infrastructure](#agent-infrastructure), based on:

- Architecture (x86-64, arm64, Apple silicon, etc.)
- Size of agents (small, medium, large, extra large)
- Type of machine (macOS, Linux, Windows, etc.)

For example, you can set up dedicated queues for `linux_medium_x86`, `mac_large_silicon`, etc.

Breaking down your infrastructure into individual queues like this makes it easier to scale groups of similar agents and get meaningful metrics from Buildkite.

## Agent infrastructure

Buildkite provides support for managing [Buildkite agents](/docs/agent) either in your own self-hosted infrastructure, or [Buildkite's own hosted infrastructure](/docs/agent/buildkite-hosted).

When setting up a queue, you can choose between configuring it with Buildkite agents running in either of these types of infrastructure.

Learn more about how to set up and create a queue using either self-hosted agents (known as a [self-hosted queue](#create-a-self-hosted-queue)) or Buildkite hosted agents (known as a [Buildkite hosted queue](#create-a-buildkite-hosted-queue)).

Be aware that it is not possible to create a queue that uses a mix of self-hosted and Buildkite hosted agents. If you do need to use a combination of these different agent types for your pipeline builds, create separate self-hosted and Buildkite hosted queues for these agents and use [agent or queue tags](/docs/agent/queues#assigning-a-self-hosted-agent-to-a-queue), or a combination of both, to target the appropriate queues.

Furthermore, once a queue has been created, it is not possible to change its type from a self-hosted to a Buildkite hosted queue, or vice versa. If you do need to change your type of agent infrastructure, use a queue with the appropriate hosted queue type, or create a new queue to suit your new agent infrastructure.

## Create a self-hosted queue

Self-hosted queues use [Buildkite agents installed in your own infrastructure](/docs/agent/self-hosted/install) to run your pipeline builds. New self-hosted queues can be created by a [cluster maintainer](/docs/pipelines/security/clusters/manage#manage-maintainers-on-a-cluster) or Buildkite organization administrator using the [Buildkite interface](#create-a-self-hosted-queue-using-the-buildkite-interface), as well as Buildkite's [REST API](#create-a-self-hosted-queue-using-the-rest-api) or [GraphQL API](#create-a-self-hosted-queue-using-the-graphql-api).

For these API requests, the _cluster ID_ value submitted in the request is the target cluster the queue will be created in.

When you [create a new cluster](/docs/pipelines/security/clusters/manage#create-a-cluster) through the [Buildkite interface](/docs/pipelines/security/clusters/manage#create-a-cluster-using-the-buildkite-interface), this cluster automatically has an initial **default** queue.

Multiple self-hosted agents can connect to your self-hosted queue by ensuring that the agent is configured to use both of the following:

- The [cluster's agent token](/docs/agent/self-hosted/tokens#using-and-storing-tokens)
- The [agent tag](/docs/agent/queues#assigning-a-self-hosted-agent-to-a-queue) targeting your self-hosted queue

### Using the Buildkite interface

To create a new self-hosted agent queue using the Buildkite interface:

1. Select **Agents** in the global navigation to access the **Clusters** page.
1. Select the cluster in which to create the new queue.
1. On the **Queues** page, select **New Queue** to open the **Create a new Queue** page.
1. In the **Create a key** field, enter a unique _key_ for the queue, which can only contain letters, numbers, hyphens, and underscores, as valid characters.
1. Select the **Add description** checkbox to enter an optional longer description for the queue. This description appears under the queue's key, which is listed on the **Queues** page, as well as when viewing the queue's details.
1. In the **Select your agent infrastructure** section, select **Self hosted** for your agent infrastructure.

    **Note:** In the **Retry Agent Affinity** section, leave the default **Prefer Warmest Agent** setting unchanged. To learn more about this setting, see [Retry agent affinity](/docs/agent/self-hosted/prioritization#retry-agent-affinity). You can always change this setting later through your self-hosted queue's **Settings** tab.

1. Select **Create Queue**.

    The new queue's details are displayed, indicating the queue's key and its description (if configured) underneath this key. Select **Queues** on the interface again to list all configured queues in your cluster.

> 📘
> A `key` can have a maximum length of 100 characters.

### Using the REST API

To [create a new self-hosted agent queue](/docs/apis/rest-api/clusters/queues#create-a-self-hosted-queue) using the [REST API](/docs/apis/rest-api), run the following example `curl` command:

```curl
curl -H "Authorization: Bearer $TOKEN" \
  -X POST "https://api.buildkite.com/v2/organizations/{org.slug}/clusters/{cluster.id}/queues" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "linux_small_amd",
    "description": "A small self-hosted AMD64 Linux agent."
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
<li><p><code>key</code> (required) is displayed on the cluster's <strong>Queues</strong> pages, and this value can only contain letters, numbers, hyphens, and underscores, as valid characters.</p></li>
<li><p><code>description</code> (optional) is a longer description for the queue, which appears under the queue's key, when listed on the <strong>Queues</strong> page, as well as when viewing the queue's details.</p></li>
</ul>

### Using the GraphQL API

To [create a new self-hosted agent queue](/docs/apis/graphql/cookbooks/clusters#create-a-self-hosted-queue) using the [GraphQL API](/docs/apis/graphql-api), run the following example mutation:

```graphql
mutation {
  clusterQueueCreate(
    input: {
      organizationId: "organization-id"
      clusterId: "cluster-id"
      key: "linux_small_amd"
      description: "A small self-hosted AMD64 Linux agent."
    }
  ) {
    clusterQueue {
      id
      uuid
      key
      description
      dispatchPaused
      hosted
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

<ul>
<li><p><code>key</code> (required) is displayed on the cluster's <strong>Queues</strong> pages, and this value can only contain letters, numbers, hyphens, and underscores, as valid characters.</p></li>
<li><p><code>description</code> (optional) is a longer description for the queue, which appears under the queue's key, when listed on the <strong>Queues</strong> page, as well as when viewing the queue's details.</p></li>
</ul>

## Create a Buildkite hosted queue

Buildkite hosted queues use [Buildkite's hosted agent infrastructure](/docs/agent/buildkite-hosted) to run your pipeline builds. New Buildkite hosted queues can be created by a [cluster maintainer](/docs/pipelines/security/clusters/manage#manage-maintainers-on-a-cluster) or Buildkite organization administrator using the [Buildkite interface](#create-a-buildkite-hosted-queue-using-the-buildkite-interface), as well as Buildkite's [REST API](#create-a-buildkite-hosted-queue-using-the-rest-api) or [GraphQL API](#create-a-buildkite-hosted-queue-using-the-graphql-api).

When you create a Buildkite hosted queue, you can choose the machine type (Linux or macOS) and the capacity (small, medium, large, or extra large), known as the _instance shape_, of the Buildkite hosted agents that will run your builds.

Only one instance shape can be configured on a Buildkite hosted queue. However, depending on your pipeline's requirements, multiple Buildkite hosted agents of the queue's configured instance shape can be spawned automatically by Buildkite.

### Using the Buildkite interface

To create a new Buildkite hosted queue using the Buildkite interface:

1. Select **Agents** in the global navigation to access the **Clusters** page.
1. Select the cluster in which to create the new queue.
1. On the **Queues** page, select **New Queue** to open the **Create a new Queue** page.
1. In the **Create a key** field, enter a unique _key_ for the queue, which can only contain letters, numbers, hyphens, and underscores, as valid characters.
1. Select the **Add description** checkbox to enter an optional longer description for the queue. This description appears under the queue's key, which is listed on the **Queues** page, as well as when viewing the queue's details.
1. In the **Select your agent infrastructure** section, select **Hosted** for your agent infrastructure.
1. In the new **Configure your hosted agent infrastructure** section, select your **Machine type** ([**Linux**](/docs/agent/buildkite-hosted/linux) or [**macOS**](/docs/agent/buildkite-hosted/macos)).
1. If you selected **Linux**, within **Architecture**, you can choose between **AMD64** (the default and recommended) or **ARM64** architectures for the Linux machines running as hosted agents. To switch to **ARM64**, select **Change**, followed by **ARM64 (AArch64)**.
1. Select the appropriate **Capacity** for your hosted agent machine type (**Small**, **Medium** or **Large**). Take note of the additional information provided in the new **Hosted agents trial** section, which changes based on your selected **Capacity**.
1. Select **Create Queue**.

    The new queue's details are displayed, indicating the queue's key and its description (if configured) underneath this key. Select **Queues** on the interface again to list all configured queues in your cluster.

### Using the REST API

To [create a new Buildkite hosted queue](/docs/apis/rest-api/clusters/queues#create-a-buildkite-hosted-queue) using the [REST API](/docs/apis/rest-api), run the following example `curl` command:

```curl
curl -H "Authorization: Bearer $TOKEN" \
  -X POST "https://api.buildkite.com/v2/organizations/{org.slug}/clusters/{cluster.id}/queues" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "mac_silicon",
    "description": "macOS agents running on Apple silicon architecture.",
    "hostedAgents": {
      "instanceShape": "MACOS_ARM64_M4_6X28"
    }
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
<li><p><code>key</code> (required) is displayed on the cluster's <strong>Queues</strong> pages, and this value can only contain letters, numbers, hyphens, and underscores, as valid characters.</p></li>
<li><p><code>description</code> (optional) is a longer description for the queue, which appears under the queue's key, when listed on the <strong>Queues</strong> page, as well as when viewing the queue's details.</p></li>
</ul>

- `hostedAgents` (required) an object that configures this queue to use [Buildkite hosted agents](/docs/agent/buildkite-hosted), which makes this a _Buildkite hosted queue_, and defines the instance shape (within its `instanceShape` parameter) for this queue's [Linux-](#create-a-buildkite-hosted-queue-instance-shape-values-for-linux) or [macOS-](#create-a-buildkite-hosted-queue-instance-shape-values-for-macos)based Buildkite hosted agent. For example:

    ```json
    "hostedAgents": {
      "instanceShape": "LINUX_AMD64_2X4"
    }
    ```

### Using the GraphQL API

To [create a new Buildkite hosted queue](/docs/apis/graphql/cookbooks/hosted-agents#create-a-buildkite-hosted-queue) using the [GraphQL API](/docs/apis/graphql-api), run the following example mutation:

```graphql
mutation {
  clusterQueueCreate(
    input: {
      organizationId: "organization-id"
      clusterId: "cluster-id"
      key: "mac_silicon"
      description: "macOS agents running on Apple silicon architecture."
      hostedAgents: {
        instanceShape: MACOS_ARM64_M4_6X28
      }
    }
  ) {
    clusterQueue {
      id
      uuid
      key
      description
      dispatchPaused
      hosted
      hostedAgents {
        instanceShape {
          name
          size
          vcpu
          memory
        }
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

<ul>
<li><p><code>key</code> (required) is displayed on the cluster's <strong>Queues</strong> pages, and this value can only contain letters, numbers, hyphens, and underscores, as valid characters.</p></li>
<li><p><code>description</code> (optional) is a longer description for the queue, which appears under the queue's key, when listed on the <strong>Queues</strong> page, as well as when viewing the queue's details.</p></li>
</ul>

- `hostedAgents` (required) an object that configures this queue to use [Buildkite hosted agents](/docs/agent/buildkite-hosted), which makes this a _Buildkite hosted queue_, and defines the instance shape (within its `instanceShape` field) for this queue's [Linux-](#create-a-buildkite-hosted-queue-instance-shape-values-for-linux) or [macOS-](#create-a-buildkite-hosted-queue-instance-shape-values-for-macos) based Buildkite hosted agent. For example:

    ```graphql
    hostedAgents: {
      instanceShape: LINUX_AMD64_2X4
    }
    ```

### Instance shape values for Linux

Specify the appropriate **Instance shape** for the `instanceShape` value in your API call.

<table class="responsive-table">
  <thead>
    <th>Instance shape</th>
    <th>Size</th>
    <th>Architecture</th>
    <th>vCPU</th>
    <th>Memory</th>
    <th>Disk space</th>
  </thead>
  <tbody>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>LINUX_AMD64_2X4</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Small</td>
      <th aria-hidden class="responsive-table__faux-th">Architecture</th>
<td>AMD64</td>
      <th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>2</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>4 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>47 GB</td>
    </tr>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>LINUX_AMD64_4X16</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Medium</td>
      <th aria-hidden class="responsive-table__faux-th">Architecture</th>
<td>AMD64</td>
      <th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>4</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>16 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>95 GB</td>
    </tr>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>LINUX_AMD64_8X32</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Large</td>
      <th aria-hidden class="responsive-table__faux-th">Architecture</th>
<td>AMD64</td>
      <th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>8</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>32 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>158 GB</td>
    </tr>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>LINUX_AMD64_16X64</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Extra Large</td>
      <th aria-hidden class="responsive-table__faux-th">Architecture</th>
<td>AMD64</td>
      <th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>16</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>64 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>284 GB</td>
    </tr>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>LINUX_ARM64_2X4</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Small</td>
      <th aria-hidden class="responsive-table__faux-th">Architecture</th>
<td>ARM64</td>
<th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>2</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>4 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>47 GB</td>
    </tr>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>LINUX_ARM64_4X16</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Medium</td>
      <th aria-hidden class="responsive-table__faux-th">Architecture</th>
<td>ARM64</td>
      <th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>4</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>16 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>95 GB</td>
    </tr>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>LINUX_ARM64_8X32</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Large</td>
      <th aria-hidden class="responsive-table__faux-th">Architecture</th>
<td>ARM64</td>
      <th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>8</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>32 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>158 GB</td>
    </tr>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>LINUX_ARM64_16X64</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Extra Large</td>
      <th aria-hidden class="responsive-table__faux-th">Architecture</th>
<td>ARM64</td>
      <th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>16</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>64 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>284 GB</td>
    </tr>
  </tbody>
</table>

### Instance shape values for macOS

Specify the appropriate **Instance shape** for the `instanceShape` value in your API call.

<table class="responsive-table">
  <thead>
    <th>Instance shape</th>
    <th>Size</th>
    <th>vCPU</th>
    <th>Memory</th>
    <th>Disk space</th>
  </thead>
  <tbody>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>MACOS_ARM64_M4_6X28</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Medium</td>
      <th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>6</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>28 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>182 GB</td>
    </tr>
    <tr>
      <th aria-hidden class="responsive-table__faux-th">Instance shape</th>
<td>
        <code>MACOS_ARM64_M4_12X56</code>
      </td>
      <th aria-hidden class="responsive-table__faux-th">Size</th>
<td>Large</td>
      <th aria-hidden class="responsive-table__faux-th">vCPU</th>
<td>12</td>
      <th aria-hidden class="responsive-table__faux-th">Memory</th>
<td>56 GB</td>
      <th aria-hidden class="responsive-table__faux-th">Disk space</th>
<td>294 GB</td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong> Shapes <code>MACOS_M2_4X7</code>, <code>MACOS_M2_6X14</code>, <code>MACOS_M2_12X28</code>, <code>MACOS_M4_12X56</code> were deprecated and removed on July 1, 2025.</p>

## Pause and resume a queue

You can pause a queue to prevent any jobs of the cluster's pipelines from being dispatched to agents associated with this queue.

To pause a queue:

1. Select **Agents** in the global navigation to access the **Clusters** page.
1. Select the cluster with the queue to pause.
1. On the **Queues** page, select the queue to pause.
1. On the queue's details page, select **Pause Queue**.
1. Enter an optional note in the confirmation dialog, and select **Pause Queue** to pause the queue.

    **Note:** Use this note to explain why you're pausing the queue. The note will be displayed on the queue's details page and on any affected builds.

Jobs _already_ dispatched to agents in the queue before pausing will continue to run. New jobs that target the paused queue will wait until the queue is resumed.

Since [trigger steps](/docs/pipelines/configure/step-types/trigger-step) do not rely on agents, these steps will run, unless they have dependencies waiting on the paused queue. The behavior of the triggered jobs depends on their configuration:

- If a triggered job targets a paused queue, the job will wait until the queue is resumed.
- If a triggered job does not target the paused queue, the job will run as usual.

To resume a queue:

1. Select **Agents** in the global navigation to access the **Clusters** page.
1. Select the cluster with the queue to resume.
1. On the **Queues** page, select the queue to resume.
1. On the queue's details page, select **Resume Queue**.

    Jobs will resume being dispatched to the resumed queue as usual, including any jobs waiting to run.

### Pause and resume an individual agent

You can also pause an agent to prevent any jobs of the cluster's pipelines from being dispatched to that particular agent. Learn more in [Pausing and resuming an agent](/docs/agent/self-hosted/pausing-and-resuming).

## Queue connection status

Self-hosted queues served by a [stack](/docs/apis/agent-api/stacks) — an orchestration system such as the [Buildkite Agent Stack for Kubernetes](/docs/agent/self-hosted/agent-stack-k8s) or the [Buildkite Elastic CI Stack for AWS](/docs/agent/self-hosted/aws/elastic-ci-stack) — display a **Connected** or **Disconnected** status badge in the Buildkite Pipelines interface.

- **Connected**: The stack serving this queue is running and actively communicating with Buildkite.
- **Disconnected**: The stack has stopped reporting in. This can occur if the stack has been shut down, has lost connectivity to Buildkite, or has encountered an error.

If no badge is displayed, the queue has no stack registered against it. This is the case when agents are started manually rather than through a stack-based orchestration system.

## Queue metrics

Clusters provides additional, easy to access queue metrics that are available only for queues within a cluster. Learn more in [Queue metrics in clusters](/docs/pipelines/insights/queue-metrics).
