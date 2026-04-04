# Source: https://planetscale.com/docs/vitess/managed/gcp/private-service-connect.md

# Set up GCP Private Service Connect with PlanetScale Managed

> PlanetScale Managed can connect you to your databases via [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect).

## Overview

The following guide describes how PlanetScale Managed with GCP Private Service Connect works and how to set it up.

<Note>
  If you are on a Scaler Pro plan and would like to set up GCP Private Service Connect endpoint, see our [Private connections documentation](/docs/vitess/connecting/private-connections-gcp).
</Note>

## How PlanetScale Managed and GCP Private Service Connect work

Private Service Connect (PSC) allows a service producer (PlanetScale) offer services to a service consumer without the consumer being a member of the service producer's organization.

The service producer is the Google Cloud project controlled by PlanetScale, and the service consumer is the project(s) where your applications operate. Your applications connect to a private IP you allocate in your project, which is routed to your PlanetScale databases in the project that PlanetScale controls.

GCP PSC requires multiple components:

* A Private Service Connect [Service Attachment](https://cloud.google.com/vpc/docs/private-service-connect#service-attachments) (also known as a Published Service) deployed in the project that PlanetScale controls on your behalf.
* A Private Service Connect [Endpoint](https://cloud.google.com/vpc/docs/private-service-connect#endpoints) deployed in the project(s) that your applications operate in.

Once all components are operating correctly, the applications in the project with the endpoint configured will connect to the service attachment using private IP addresses instead of the publicly accessible endpoint.

## Step 1: Initiating the setup process

If you would like to initiate the process, please contact your Solutions Engineer and let them know the Google Cloud project ID(s) in which you intend to create Private Service Connect endpoints. If you need to add additional projects to the allowlist, please get in touch with your Solutions Engineer.

<Warning>
  Google Cloud project IDs cannot be changed after initial setup. Please be sure to choose an ID that you will continue to use.
</Warning>

Once they receive your project IDs and forward them to the team responsible for provisioning your deployment, the team will provide them (and ultimately you) with the Private Service Connect Service Attachment URI, which will be in the form `projects/PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`.

<Warning>
  If you use VPC Service Controls in your VPC, you must ensure that the policy allows access to the PlanetScale-controlled project.
</Warning>

Your Solutions Engineer will provide you the following information when the setup is complete:

* `Target Service` (example: `projects/PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`)

You will use these values when configuring the Private Service Connect in your application projects.

If you have databases in multiple regions, each region will have a unique `Target Service`, and you will need to configure consumer endpoints for each region.

## Step 2: Establishing Private Service Connect

<Warning>
  Only proceed to the next steps once a PlanetScale Solutions Engineer has provided the `Target Service`.
</Warning>

Refer to Google Cloud's [Access published services through endpoints](https://cloud.google.com/vpc/docs/configure-private-service-connect-services) document for more information on connecting to services via Private Service Connect. This document covers additional details not covered here, including the IAM roles required to perform the configuration process.

### Using the GCP console

The following steps are an example of establishing a Private Service Connect endpoint in the [GCP Console](https://console.cloud.google.com/).

<Steps>
  <Step>
    Obtain the Private Service Connect Attachment URI (`Target Service`) from your Solutions Engineer. It will be in the format: `projects/PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`.
  </Step>

  <Step>
    Create a Private Service Connect Endpoint. In the GCP console, go to ["Network Service > Private Service Connect"](https://console.cloud.google.com/net-services/psc) page, select the "**Connected endpoints**" tab, and select the "**+ Connect endpoint**" button.
  </Step>

  <Step>
    Add a Private Service Connect Endpoint with the following details:

    * **Target**: Published Service.
    * **Target Service**: Paste the `Target Service` attachment URI provided by your Solutions Engineer in step 1.
    * **Name**: Pick any `Endpoint Name`. The examples in this document use `"edge"`.
    * **Network and subnet**: Select the network (VPC) to create the endpoint in. The endpoint will reserve a static IP address in the subnet. The VPC and subnet must be reachable by the applications you intend to connect to your PlanetScale databases from.
    * **Create an IP Address**: Create a reserved IP address. This is the address your applications will use to access your PlanetScale databases.
    * **Enable Global Access**: PlanetScale recommends enabling this option. When enabled, this allows applications in other regions of your VPC to reach the PSC endpoint.

    Finally, click **Add Endpoint** to start the process. Setup will take approximately 1-2 minutes.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/connect_endpoint_details.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=3a628afc3368f200ef7a5e041beb99ba" alt="connect_endpoint_details" data-og-width="825" width="825" data-og-height="892" height="892" data-path="docs/images/assets/docs/managed/gcp/private-service-connect/connect_endpoint_details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/connect_endpoint_details.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=cf9ff0d935370188b95fe2a8b0b24453 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/connect_endpoint_details.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=766dd3780f3307b1ae0f93b25486d10e 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/connect_endpoint_details.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=9a3844e39979f16172a784fcb3b1622f 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/connect_endpoint_details.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=05e8194f73732bef3604ddc579443881 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/connect_endpoint_details.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f234b0063fc305a18c31e25fdd0a499e 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/connect_endpoint_details.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=59e63a64a90bbfe33400b7fe925e8f6c 2500w" />
    </Frame>
  </Step>

  <Step>
    The endpoint creation process will take a minute or two. When finished, select the endpoint and verify the status is **Accepted**:

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/endpoint_status.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=28bfb2a2c7528b4392751a850fdf9dbe" alt="Showing endpoint status as &#x22;Accepted&#x22;" data-og-width="1098" width="1098" data-og-height="432" height="432" data-path="docs/images/assets/docs/managed/gcp/private-service-connect/endpoint_status.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/endpoint_status.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=186d95e6b201bddda1edbe17af98d1aa 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/endpoint_status.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=706ec8e1f8bf805a4587b6557a56c903 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/endpoint_status.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=5706d2ab1fc7bcb1ed4056d19c954560 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/endpoint_status.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=8b477ef93fd6b79777ffb26a743241c1 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/endpoint_status.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=af7dd63e330a3efac285f81c96286ed8 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/endpoint_status.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=e13749a236a5ed9cd7babb731b9182aa 2500w" />
    </Frame>

    <Note>
      You must provide the list of projects you wish to connect from to your Solutions Engineer. Your endpoint will only function once they have been added to the allowlist in the published service.
    </Note>

    Repeat steps 2-4 to create an endpoint in **each project** you wish to connect to the Private Service Connect Attachment.
  </Step>
</Steps>

## Step 3: Verifying Connectivity

## DNS

<Note>
  Private Service Connect services created after **May 8, 2024** automatically create private Cloud DNS records in the project where the PSC consumer endpoints are created.

  PSC services published before **May 8, 2024** may need to create a private Cloud DNS zone and configure records pointing to the PSC endpoint IP's manually if you wish to use DNS names to connect to your PlanetScale databases.

  Google maintains additional documentation covering DNS and Private Service Connect here:

  * [Automatic DNS configuration for Service Consumers](https://cloud.google.com/vpc/docs/dns-vpc-hosted-services#auto-dns-consumer)
  * [Other ways to configure DNS for Service Consumers](https://cloud.google.com/vpc/docs/configure-private-service-connect-services#other-dns)
</Note>

Private Service Connect endpoints automatically create a private DNS records in the project where the PSC consumer endpoints are created that resolve to the endpoint's reserved IP.

The domain name used varies by region. You can view the domain name by clicking on `Network Services > Cloud DNS`. If Google was able to set up automatic DNS, you will see a new private DNS zone labeled by `DNS Name`:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/cloud_dns.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=ce3038a503038fdaa93c940e207824f5" alt="cloud dns zone list" data-og-width="1098" width="1098" data-og-height="373" height="373" data-path="docs/images/assets/docs/managed/gcp/private-service-connect/cloud_dns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/cloud_dns.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=625d33992c50f7454fa855c07d7c6fa7 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/cloud_dns.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=a0ff32536b71e10f7aed0ffa7aa83d6d 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/cloud_dns.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=a6c51f4efed2501f6fce0861a91fcb0d 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/cloud_dns.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=22a4e9fca6b1ac2fc9ccff305eca6b82 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/cloud_dns.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=1a9a8be9c084ee54805c2b334ec7682a 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/managed/gcp/private-service-connect/cloud_dns.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=42b72b52352f466ef45d59547399c3e3 2500w" />
</Frame>

Your consumer endpoints will be available via DNS records visible only within your VPC using the format:

* `<Endpoint-Name>.<Domain-Name>`

If your endpoint was created with automatic DNS or your created your own DNS records manually, you can verify resolution with `dig`. In this example, the endpoint was created with the name `edge` and the service's domain name was `izkpm55j334u-uscentral1.private-connect.psdb.cloud`:

```shell  theme={null}
$ dig +short edge.izkpm55j334u-uscentral1.private-connect.psdb.cloud
10.128.0.14
```

## Test connectivity

Run `curl https://<Endpoint-Name>.<Domain-Name>` to verify your connectivity. A successful response will yield `Welcome to PlanetScale`.

```shell  theme={null}
curl https://edge.izkpm55j334u-uscentral1.private-connect.psdb.cloud
Welcome to PlanetScale.
```

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt