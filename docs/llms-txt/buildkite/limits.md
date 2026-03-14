# Source: https://buildkite.com/docs/apis/graphql/portals/limits.md

# Source: https://buildkite.com/docs/apis/rest-api/limits.md

# Source: https://buildkite.com/docs/platform/limits.md

# Limits

This page outlines usage limits designed to protect your builds from unintentional resource issues and ensure reliable service for all customers. Limits vary by subscription tier:

- Personal plan
- Trial plan
- Pro plan
- Enterprise plan

You can find out more about the available plans and what is included in them in [Pricing](https://buildkite.com/pricing/).

The [**Usage** page](https://buildkite.com/organizations/~/usage) is available on every Buildkite plan and shows a breakdown of usage metrics across the Buildkite platform and all products for your Buildkite organization.

## Viewing your organization's service quotas

Buildkite organization administrators can view the service quotas that apply to their organization on the **Service Quotas** page in **Organization Settings**.

To access your organization's service quotas:

1. Select **Settings** in the global navigation to access the [**Organization Settings**](https://buildkite.com/organizations/~/settings) page.

1. Select **Quotas** to open the **Service Quotas** page.

    <div style="max-width: 581px"><div class="responsive-image-container"><img alt="The Service Quotas page in Organization Settings, showing quota limits grouped by product area with name, description, and limit value for each quota" src="/docs/assets/service-quotas-CMBZIFLl.png" /></div></div>

    The **Service Quotas** page displays your organization's current limits grouped by product area. Each quota shows the limit that applies to your organization, which may differ from the defaults listed on this page.

    A **Custom** badge next to a quota indicates that your organization has a limit that differs from the default for your plan. An **Exceeded in last 24h** badge indicates that your organization reached this limit within the past 24 hours.

> 📘 Adjusting limits
> Some organization-level limits can be increased on request depending on your plan. Contact Buildkite support at support@buildkite.com with details about your use case, or contact your Technical Account Manager if you have one.

## Platform and organization-level limits

Platform and organization-level limits apply to all Buildkite products. These limits protect your organization from unintentional resource exhaustion and ensure reliable service for all customers. These limits are scoped to your organization.

<table>
  <thead>
    <tr>
      <th style="width:25%">Service limit type</th>
      <th style="width:75%">Description and default limit</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td>
          <strong>Organizations per day</strong>
         </td>
        <td>
          <p>The maximum number of organizations a user can create per day.</p>
          Default: <strong>4 organizations</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Organizations per user</strong>
         </td>
        <td>
          <p>The maximum total number of organizations a user can create.</p>
          Default: <strong>20 organizations</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Unverified emails per user</strong>
         </td>
        <td>
          <p>The maximum number of unverified emails per user.</p>
          Default: <strong>5 emails</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Invitations per organization</strong>
         </td>
        <td>
          <p>The maximum number of pending invitations for an organization.</p>
          Default: <strong>20 invitations</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Teams per organization</strong>
         </td>
        <td>
          <p>The maximum number of teams that an organization can have.</p>
          Default: <strong>250 teams</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>REST API rate limit per organization</strong>
         </td>
        <td>
          <p>The number of requests an organization can make to Organization endpoints on the REST API, per minute.</p>
          Default: <strong>200 requests per minute</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>GraphQL API rate limit per organization</strong>
         </td>
        <td>
          <p>The number of requests an organization can make to Organization endpoints on the GraphQL API, per minute.</p>
          Default: <strong>20,000 requests per minute</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Portal API rate limit per organization</strong>
         </td>
        <td>
          <p>The number of requests an organization can make to Organization endpoints on the Portal API, per minute.</p>
          Default: <strong>200 requests per minute</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>GraphQL query complexity</strong>
         </td>
        <td>
          <p>The maximum complexity score for GraphQL queries.</p>
          Default: <strong>50,000</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>GraphQL query depth</strong>
         </td>
        <td>
          <p>The maximum nesting depth for GraphQL queries.</p>
          Default: <strong>15 levels</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Audit search terms</strong>
         </td>
        <td>
          <p>The maximum number of search terms for audit logs.</p>
          Default: <strong>3 terms</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>IP addresses per token</strong>
         </td>
        <td>
          <p>The maximum number of IP allowlist entries per token.</p>
          Default: <strong>24 addresses</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Maximum OIDC lifetime</strong>
         </td>
        <td>
          <p>The default maximum lifetime for OIDC.</p>
          Default: <strong>2 hours</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Linear services per organization</strong>
         </td>
        <td>
          <p>The maximum number of Linear integrations that can be added to an organization.</p>
          Default: <strong>1 service</strong>
        </td>
      </tr>
    
  </tbody>
</table>

## Pipelines limits

The following table lists the default service limits for [Pipelines](/docs/pipelines).

<table>
  <thead>
    <tr>
      <th style="width:25%">Service limit type</th>
      <th style="width:75%">Description and default limit</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td>
          <strong>Jobs per build</strong>
         </td>
        <td>
          <p>The maximum number of jobs that can be created in a single pipeline build (including job retries).</p>
          Default: <strong>4,000 jobs</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Jobs created per pipeline upload</strong>
         </td>
        <td>
          <p>The maximum number of jobs that can be created in a single pipeline upload.</p>
          Default: <strong>500 jobs</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Job timeout</strong>
         </td>
        <td>
          <p>The maximum time before a running job will time out.</p>
          Default: <strong>4 hours on the Personal plan. Unlimited on Pro and Enterprise plans</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Pipeline uploads per build</strong>
         </td>
        <td>
          <p>The maximum number of pipeline uploads that can be performed in a single build.</p>
          Default: <strong>500 pipeline uploads</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Triggers per pipeline</strong>
         </td>
        <td>
          <p>The maximum number of webhook triggers per pipeline.</p>
          Default: <strong>10</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Trigger build depth per pipeline</strong>
         </td>
        <td>
          <p>The maximum depth of a chain of trigger builds.</p>
          Default: <strong>10 builds</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Triggered builds per build</strong>
         </td>
        <td>
          <p>The maximum number of triggered builds per single build.</p>
          Default: <strong>250 builds</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Concurrency key length</strong>
         </td>
        <td>
          <p>The maximum length for concurrency group keys.</p>
          Default: <strong>200 characters</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Build retention</strong>
         </td>
        <td>
          <p>The time period builds are stored in Buildkite after running.</p>
          Default: <strong>90 days on the Personal and Pro plans, 365 days on the Enterprise plan</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Teams per block step</strong>
         </td>
        <td>
          <p>The maximum number of allowed teams for manual unlock steps.</p>
          Default: <strong>100 teams</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Matrix jobs per step</strong>
         </td>
        <td>
          <p>The maximum number of matrix jobs in a pipeline step.</p>
          Default: <strong>50 jobs</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Annotation replacements</strong>
         </td>
        <td>
          <p>The maximum number of image or link replacements per annotation.</p>
          Default: <strong>10 replacements</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Artifacts per job</strong>
         </td>
        <td>
          <p>The maximum number of artifacts that can be uploaded to Buildkite per job.</p>
          Default: <strong>5000 artifacts</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Artifact file size</strong>
         </td>
        <td>
          <p>The maximum size of an artifact that can be uploaded to Buildkite from an agent.</p>
          Default: <strong>10 GiB</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Artifact batch total file size</strong>
         </td>
        <td>
          <p>The maximum cumulative size of artifacts that can be uploaded to Buildkite from an agent in a single job using the <code>buildkite-agent artifact upload</code> command.</p>
          Default: <strong>50 GiB</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Multipart upload artifacts</strong>
         </td>
        <td>
          <p>The maximum number of artifacts per upload batch.</p>
          Default: <strong>30 artifacts</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Artifact retention</strong>
         </td>
        <td>
          <p>The maximum number of days artifacts are stored.</p>
          Default: <strong>180 days</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Log size per job</strong>
         </td>
        <td>
          <p>The maximum file-size of a job's log.</p>
          Default: <strong>1,024 MiB</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Number of clusters</strong>
         </td>
        <td>
          <p>The maximum number of clusters that can be created in a Buildkite organization.</p>
          Default: <strong>1 on the Personal plan, unlimited on Pro and Enterprise plans</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Number of queues per cluster</strong>
         </td>
        <td>
          <p>The default number of queues that can be created on a single cluster.</p>
          Default: <strong>50</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Portal secrets</strong>
         </td>
        <td>
          <p>The maximum number of secrets per portal.</p>
          Default: <strong>2 secrets</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Number of stacks per organization</strong>
         </td>
        <td>
          <p>The default number of stacks that can be created per organization.</p>
          Default: <strong>30</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Cache size for hosted agents</strong>
         </td>
        <td>
          <p>The maximum cache size for hosted agents.</p>
          Default: <strong>128 GB</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Artifact Create/Update API calls</strong>
         </td>
        <td>
          <p>The number of Create or Update requests for artifacts per minute per organization.</p>
          Default: <strong>600</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Slack services per organization</strong>
         </td>
        <td>
          <p>The maximum number of Slack services that can be added to an organization.</p>
          Default: <strong>50 services</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Webhook services per organization</strong>
         </td>
        <td>
          <p>The maximum number of Webhook services that can be added to an organization.</p>
          Default: <strong>15 services</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Event Log API services per organization</strong>
         </td>
        <td>
          <p>The maximum number of Event Log API services that can be added to an organization.</p>
          Default: <strong>15 services</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>OpenTelemetry Tracing services per organization</strong>
         </td>
        <td>
          <p>The maximum number of OpenTelemetry Tracing services that can be added to an organization.</p>
          Default: <strong>5 services</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Datadog Pipeline Visibility services per organization</strong>
         </td>
        <td>
          <p>The maximum number of Datadog Pipeline Visibility services that can be added to an organization.</p>
          Default: <strong>5 services</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>AWS EventBridge services per organization</strong>
         </td>
        <td>
          <p>The maximum number of AWS EventBridge services that can be added to an organization.</p>
          Default: <strong>1 service</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Anthropic spend</strong>
         </td>
        <td>
          <p>Model provider spend limits for Anthropic, per month in USD.</p>
          Default: <strong>$50 on Trial plan, $1,000 on Pro and Enterprise</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>OpenAI spend</strong>
         </td>
        <td>
          <p>Model provider spend limits for OpenAI, per month in USD.</p>
          Default: <strong>$50 on Trial plan, $1,000 on Pro and Enterprise</strong>
        </td>
      </tr>
    
  </tbody>
</table>

### Hosted agents limits

The following limits apply to the [Buildkite hosted agents](/docs/agent/buildkite-hosted) used in Buildkite Pipelines.

| Limit type | Trial | Personal | Pro | Enterprise |
| --- | --- | --- | --- | --- |
| **Linux concurrency** | 10 | 3 | 20 | Custom |
| **macOS concurrency** | 3 | - | 5 | Custom |
| **Linux minutes, per month** | 2,000 | 550 | usage-based | usage-based |
| **macOS minutes, per month** | 3,000 | not available | usage-based | usage-based |
| **Container cache volume** | 50 GB | 50 GB | 50 GB | 50 GB |
| **Git mirror volume** | 5 GB | 5 GB | 5 GB | 5 GB |

## Test Engine limits

The following table lists the default service limits for [Test Engine](/docs/test-engine).

<table>
  <thead>
    <tr>
      <th style="width:25%">Service limit type</th>
      <th style="width:75%">Description and default limit</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td>
          <strong>Test Engine workflows per suite</strong>
         </td>
        <td>
          <p>The maximum number of Test Engine workflows per suite.</p>
          Default: <strong>1 workflow on the Personal plan, 3 workflows on the Pro and Enterprise plans</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Test Engine workflow events per minute</strong>
         </td>
        <td>
          <p>The maximum number of Test Engine workflow events per minute.</p>
          Default: <strong>500 events</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Test Splitting API rate limit</strong>
         </td>
        <td>
          <p>The number of requests that can be made to the Test Splitting API.</p>
          Default: <strong>10,000 requests per minute</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Test ownership file size</strong>
         </td>
        <td>
          <p>The maximum size for CODEOWNERS files.</p>
          Default: <strong>1 MB</strong>
        </td>
      </tr>
    
  </tbody>
</table>

## Package Registries limits

The following table lists the default service limits for [Package Registries](/docs/package-registries). The limits in Package Registries are based on the [subscription tier](https://buildkite.com/pricing/):

<table>
  <thead>
    <tr>
      <th style="width:25%">Service limit type</th>
      <th style="width:75%">Description and default limit</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td>
          <strong>Personal plan</strong>
         </td>
        <td>
          <p>Allocated storage and bandwidth volume (combined).</p>
          Default: <strong>1 GB per month (hard limit)</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Pro plan</strong>
         </td>
        <td>
          <p>Allocated storage and bandwidth volume (combined).</p>
          Default: <strong>20 GB included per organization per month, then usage-based billing</strong>
        </td>
      </tr>
    
      <tr>
        <td>
          <strong>Enterprise plan</strong>
         </td>
        <td>
          <p>Allocated storage and bandwidth volume (combined).</p>
          Default: <strong>Custom allocation with volume pricing</strong>
        </td>
      </tr>
    
  </tbody>
</table>
