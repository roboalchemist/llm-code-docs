# Source: https://docs.datadoghq.com/agent/guide/gcp-private-service-connect.md

---
title: Connect to Datadog over Google Cloud Private Service Connect
description: >-
  Configure Google Cloud Private Service Connect endpoints and DNS zones to send
  telemetry to Datadog privately without using the public internet.
breadcrumbs: >-
  Docs > Agent > Agent Guides > Connect to Datadog over Google Cloud Private
  Service Connect
source_url: https://docs.datadoghq.com/guide/gcp-private-service-connect/index.html
---

# Connect to Datadog over Google Cloud Private Service Connect

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, us3.datadoghq.com, app.ddog-gov.com, ap1.datadoghq.com, ap2.datadoghq.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: us5.datadoghq.com

[Google Cloud Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) (PSC) allows you to send telemetry to Datadog without using the public internet.

Datadog exposes some of its data intake services in Google Cloud as Private Service Connect [*published services*](https://cloud.google.com/vpc/docs/private-service-connect#published-services), as seen in the table of published services.

You can configure a PSC endpoint to expose a private IP address for each Datadog intake service. This IP address routes traffic to the Datadog backend. You can then configure a Google Cloud [*Private DNS Zone*](https://cloud.google.com/dns/docs/zones/zones-overview) to override the DNS names corresponding to the products for each endpoint that is consumed.

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/psc/gcp-psc-overview-1.0c49964df7607fa3d427c36bc8b61902.png?auto=format"
   alt="Google Cloud Private Service Connect schema. On the left, a 'Customer VPC' box contains Datadog Agents sending data to a PSC endpoint. On the right, a 'Datadog VPC' box contains a service attachment in communication with Datadog services. The endpoint in the 'Customer VPC' box connects to the service attachment in the 'Datadog VPC' box through the Google Cloud backbone. " /%}

## Setup{% #setup %}

### Connect an endpoint{% #connect-an-endpoint %}

1. In your Google Cloud console, navigate to **Network services** > **Private Service Connect**.

1. Go to the **Endpoints** section. Click on **Connect endpoint**.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/psc/connect-endpoint1.7dd014b31eefcd0df8b182c414f00c95.png?auto=format"
      alt="Screenshot of a 'Connect endpoint' page in the Google Cloud console" /%}

   - Under **Target**, select *Published service*.
   - For **Target service**, enter the *PSC target name* that corresponds to the Datadog intake service that you want to use. You can find your PSC target name in the table of published services.
   - For **Endpoint name**, enter a unique identifier to use for this endpoint. You can use `datadog-<SERVICE>`. For example: `datadog-api`.
   - For **Network** and **Subnetwork**, choose the network and subnetwork where you want to publish your endpoint.
   - For **IP address**, click the dropdown and select *Create IP address* to create an internal IP from your subnet dedicated to the endpoint. Select this IP.
   - Check **Enable global access** if you intend to connect the endpoint to virtual machines outside of the `us-central1` region.

**Note**: Datadog exposes PSC producer endpoints from the `us-central1` region. These endpoints support global access, allowing services to connect from any region. However, the forwarding rule must be created in the `us-central1` region.

1. Click **Add endpoint**. Verify that your status is *Accepted*. Take note of the IP address, as this is used in the next section.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/psc/connect-endpoint-success1.9beec2ce7afef40d1914557e73e8d7ff.png?auto=format"
      alt="Screenshot of a success message after adding an endpoint in the Google Cloud console. Includes an IP address" /%}

### Create a DNS zone{% #create-a-dns-zone %}

1. In your Google Cloud console, navigate to **Network services** > **Cloud DNS**.

1. Click on **Create zone**.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/psc/create-a-dns-zone1.5a6cdd7143cfe02a842d32bb4cdbf208.png?auto=format"
      alt="Screenshot of a 'Create a DNS zone' page in the Google Cloud console" /%}

   - Under **Zone type**, select *Private*.
   - For **Zone name**, enter a descriptive name for your zone.
   - For **DNS name**, enter the *private DNS name* that corresponds to the Datadog intake service that you want to use. You can find your DNS name in the table of published services.

1. Next, create an `A` record that points to the endpoint IP. On the *Zone details* page of the zone you created, click on **Add record set**.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/psc/create-record1.2735ceaeb91d4e2b828fa6c7ac9b1973.png?auto=format"
      alt="Screenshot of the 'Create record set' page in the Google Cloud console." /%}

   - For **DNS name**, leave the field unmodified.
   - For **Resource record type**, select `A`.
   - Under **IPv4 Address**, enter the IP address that was displayed at the end of the previous section.

### Additional required steps for metrics and traces{% #additional-required-steps-for-metrics-and-traces %}

There are two Datadog Intake Services that are subdomains of the (`agent.`) domain. Because of this, the Private Hosted Zone is slightly different from other intakes.

Create a Private Zone for (`agent.`), as outlined in the Create a DNS Zone section. Then add the three records below.

| DNS name | Resource record type | IPv4 address                         |
| -------- | -------------------- | ------------------------------------ |
| `(apex)` | A                    | IP address for your metrics endpoint |
| `*`      | A                    | IP address for your metrics endpoint |
| `trace`  | A                    | IP address for your traces endpoint  |

**Note**: this zone requires a wildcard (`*`) record that points to the IP address for your metrics endpoint. This is because Datadog Agents submit telemetry using a versioned endpoint in the form (`<version>-app.agent.`).

### Validation{% #validation %}

To verify your configuration, SSH into one of your local nodes and run a `dig` command similar to the following:

*Verify that that the wildcard is routing to the metrics endpoint*

```shell
> dig +noall +answer 7-49-0-app.agent.us5.datadoghq.com
```

The response resembles:

```
7-49-0-app.agent.us5.datadoghq.com. 300 IN A        10.1.0.4
```

*Verify that the trace subdomain is routing to the traces endpoint*

```shell
> dig +noall +answer trace.agent.us5.datadoghq.com
```

The response resembles:

```
trace.agent.us5.datadoghq.com. 300 IN  A       10.1.0.9
```

Ensure that the IP address in the response matches the one associated with your PSC target.

## Published services{% #published-services %}

| Datadog intake service  | PSC target name                                                                              | Private DNS name                           |
| ----------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Logs (Agent)            | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-logs-agent-intake-psc` | `agent-http-intake.logs.us5.datadoghq.com` |
| Logs (User HTTP Intake) | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-logs-intake-psc`       | `http-intake.logs.us5.datadoghq.com`       |
| API                     | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-api-psc`               | `api.us5.datadoghq.com`                    |
| Metrics                 | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-metrics-agent-psc`     | `agent.us5.datadoghq.com`                  |
| Containers              | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-orchestrator-psc`      | `orchestrator.us5.datadoghq.com`           |
| Process                 | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-process-psc`           | `process.us5.datadoghq.com`                |
| Profiling               | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-logs-http-profile-psc` | `intake.profile.us5.datadoghq.com`         |
| Traces                  | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-trace-edge-psc`        | `agent.us5.datadoghq.com`                  |
| Database Monitoring     | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-dbm-metrics-psc`       | `dbm-metrics-intake.us5.datadoghq.com`     |
| Remote Configuration    | `projects/datadog-prod-us5/regions/us-central1/serviceAttachments/nlb-fleet-psc`             | `config.us5.datadoghq.com`                 |

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.eu

[Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) (PSC) allows you to send telemetry to Datadog without using the public internet.

Datadog exposes some of its data intake services in Google Cloud Platform as PSC [*published services*](https://cloud.google.com/vpc/docs/private-service-connect#published-services), as seen in the table of published services.

You can configure a PSC endpoint to expose a private IP address for each Datadog intake service. This IP address routes traffic to the Datadog backend. You can then configure a Google Cloud [*Private DNS Zone*](https://cloud.google.com/dns/docs/zones/zones-overview) to override the DNS names corresponding to the products for each endpoint that is consumed.

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/psc/gcp-psc-overview-1.0c49964df7607fa3d427c36bc8b61902.png?auto=format"
   alt="Google Cloud Private Service Connect schema. On the left, a 'Customer VPC' box contains Datadog Agents sending data to a PSC endpoint. On the right, a 'Datadog VPC' box contains a service attachment in communication with Datadog services. The PSC endpoint in the 'Customer VPC' box connects to the service attachment in the 'Datadog VPC' box through the Google Cloud backbone. " /%}

## Setup{% #setup-1 %}

### Connect an endpoint{% #connect-an-endpoint-1 %}

1. In your GCP console, navigate to **Network services** > **Private Service Connect**.

1. Go to the **Endpoints** section. Click on **Connect endpoint**.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/psc/connect-endpoint-eu1.3ae275e1a5e53e349332706912d1e99d.png?auto=format"
      alt="Screenshot of a 'Connect endpoint' page in the Google Cloud console" /%}

   - Under **Target**, select *Published service*.
   - For **Target service**, enter the *PSC target name* that corresponds to the Datadog intake service that you want to use. You can find your PSC target name in the table of published services.
   - For **Endpoint name**, enter a unique identifier to use for this endpoint. You can use `datadog-<SERVICE>`. For example: `datadog-metrics`.
   - For **Network** and **Subnetwork**, choose the network and subnetwork where you want to publish your endpoint.
   - For **IP address**, click the dropdown and select *Create IP address* to create an internal IP from your subnet dedicated to the endpoint. Select this IP.
   - Check **Enable global access** if you intend to connect the endpoint to virtual machines outside of the `europe-west3` region.

**Note**: Datadog exposes PSC producer endpoints from the `europe-west3` region. These endpoints support global access, allowing services to connect from any region. However, the forwarding rule must be created in the `europe-west3` region.

1. Click **Add endpoint**. Verify that your status is *Accepted*. Take note of the IP address, as this is used in the next section.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/psc/connect-endpoint-success-eu1.5e3f875a1deeec7f34719f4e28d422a8.png?auto=format"
      alt="Screenshot of a success message after adding an endpoint in the Google Cloud console. Includes an IP address" /%}

### Create a DNS zone{% #create-a-dns-zone-1 %}

1. In your Google Cloud console, navigate to **Network services** > **Cloud DNS**.

1. Click on **Create zone**.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/psc/create-a-dns-zone-eu1.6de90db06355acba64c586c1c6069ebb.png?auto=format"
      alt="Screenshot of a 'Create a DNS zone' page in the Google Cloud console" /%}

   - Under **Zone type**, select *Private*.
   - For **Zone name**, enter a descriptive name for your zone.
   - For **DNS name**, enter the *private DNS name* that corresponds to the Datadog intake service that you want to use. You can find your DNS name in the table of published services.

1. Next, create an `A` record that points to the endpoint IP. On the *Zone details* page of the zone you created, click on **Add record set**.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/psc/create-record-eu1.97e437beb70673e7f31e54ef64591a53.png?auto=format"
      alt="Screenshot of the 'Create record set' page in the Google Cloud console." /%}

   - For **DNS name**, leave the field unmodified.
   - For **Resource record type**, select `A`.
   - Under **IPv4 Address**, enter the IP address that was displayed at the end of the previous section.

### Additional required steps for metrics and traces{% #additional-required-steps-for-metrics-and-traces-1 %}

There are two Datadog Intake Services that are subdomains of the (`agent.`) domain. Because of this, the Private Hosted Zone is slightly different from other intakes.

Create a Private Zone for (`agent.`), as outlined in the Create a DNS Zone section. Then add the three records below.

| DNS name | Resource record type | IPv4 address                         |
| -------- | -------------------- | ------------------------------------ |
| `(apex)` | A                    | IP address for your metrics endpoint |
| `*`      | A                    | IP address for your metrics endpoint |
| `trace`  | A                    | IP address for your traces endpoint  |

**Note**: this zone requires a wildcard (`*`) record that points to the IP address for your metrics endpoint. This is because Datadog Agents submit telemetry using a versioned endpoint in the form (`<version>-app.agent.`).

### Validation{% #validation-1 %}

To verify your configuration, SSH into one of your local nodes and run a `dig` command similar to the following:

*Verify that that the wildcard is routing to the metrics endpoint*

```shell
> dig +noall +answer 7-49-0-app.agent.datadoghq.eu
```

The response resembles:

```
7-49-0-app.agent.datadoghq.eu. 300 IN A        10.1.0.4
```

*Verify that the trace subdomain is routing to the traces endpoint*

```shell
> dig +noall +answer trace.agent.datadoghq.eu
```

The response resembles:

```
trace.agent.datadoghq.eu. 300 IN  A       10.1.0.9
```

Ensure that the IP address in the response matches the one associated with your PSC target.

## Published services{% #published-services-1 %}

| Datadog intake service  | PSC target name                                                                           | Private DNS name                      |
| ----------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------- |
| Logs (Agent)            | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-logs-agent-intake-psc` | `agent-http-intake.logs.datadoghq.eu` |
| Logs (User HTTP Intake) | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-logs-intake-psc`       | `http-intake.logs.datadoghq.eu`       |
| API                     | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-api-psc`               | `api.datadoghq.eu`                    |
| Metrics                 | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-metrics-agent-psc`     | `agent.datadoghq.eu`                  |
| Containers              | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-orchestrator-psc`      | `orchestrator.datadoghq.eu`           |
| Process                 | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-process-psc`           | `process.datadoghq.eu`                |
| Profiling               | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-logs-http-profile-psc` | `intake.profile.datadoghq.eu`         |
| Traces                  | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-trace-edge-psc`        | `agent.datadoghq.eu`                  |
| Database Monitoring     | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-dbm-metrics-psc`       | `dbm-metrics-intake.datadoghq.eu`     |
| Remote Configuration    | `projects/datadog-prod/regions/europe-west3/serviceAttachments/nlb-fleet-psc`             | `config.datadoghq.eu`                 |

{% /callout %}

## Further reading{% #further-reading %}

- [Datadog-Google Cloud Platform Integration](https://docs.datadoghq.com/integrations/google_cloud_platform/)
- [Connect to Datadog over AWS PrivateLink](https://docs.datadoghq.com/agent/guide/private-link)
