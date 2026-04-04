# Source: https://planetscale.com/docs/vitess/connecting/private-connections-gcp.md

# Connecting to PlanetScale privately on GCP

## Connecting to PlanetScale privately via GCP Private Service Connect

When your compliance mandates that your connections do not route through the public Internet, PlanetScale provides private connection endpoints to GCP regions via [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect). GCP Private Service Connect is a form of *VPC peering* that keeps your traffic within Google Cloud. Private connections are included on Scaler Pro plans. There is no additional charge on PlanetScale's end, but this may impact your GCP bill.

Below is a list of instructions to set up your VPC network to utilize a Private Service Connect endpoint when communicating with PlanetScale databases.

## Establishing a Private Service Connect Endpoint

<Steps>
  <Step>
    Identify the GCP region that your VPC lives in, which we will refer to as `<gcp-region>` for the rest of this document.
  </Step>

  <Step>
    In the GCP console, go to ["Network Service > Private Service Connect"](https://console.cloud.google.com/net-services/psc) page, select the "**Connected endpoints**" tab, and select the "**+ Connect endpoint**" button.
  </Step>

  <Step>
    Add a Private Service Connect Endpoint with the following details:

    * **Target**: Published Service.
    * **Target Service**: Select the target service from the table below for the region you want to establish an endpoint in.
    * **Name**: Pick any endpoint name. The examples in this document use `"edge"`.
    * **Network and subnet**: Select the network (VPC) to create the endpoint in. The endpoint will reserve a static IP address in the subnet. The VPC and subnet must be reachable by the applications you intend to connect to your PlanetScale databases from.
    * **Create an IP Address**: Create a reserved IP address for the endpoint. This is the address your applications will use to access your PlanetScale databases.
    * **Enable Global Access**: PlanetScale recommends enabling this option. When enabled, this allows applications in other regions of your VPC to reach the PSC endpoint.
    * Finally, click **Add Endpoint** to start the process. Setup will take approximately 1-2 minutes.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/connect_endpoint_details.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=4c5a06499d0e6700029f4c4c693d6778" alt="Setup endpoint details" data-og-width="825" width="825" data-og-height="892" height="892" data-path="docs/images/assets/docs/multi/gcp/private-service-connect/connect_endpoint_details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/connect_endpoint_details.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=661660327bd31b9f39de96cf74adb06a 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/connect_endpoint_details.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=0e3b52977a8d6eea944d0604d31b6f87 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/connect_endpoint_details.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=ec2f13018a0ec2f418c76828baff1a7e 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/connect_endpoint_details.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=434f024cff833835162d1d64fd191879 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/connect_endpoint_details.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=5334ef996c6e408c69d6660e94c2252d 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/connect_endpoint_details.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=03750181ffa1c4d5e70d93e87a7250dd 2500w" />
    </Frame>

    | GCP Region              | Target Service                                                                                                                | Domain Name                                            |
    | :---------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
    | asia-northeast3         | `projects/planetscale-production/regions/asia-northeast3/serviceAttachments/edge-gateway-gcp-asia-northeast3`                 | gcp-asia-northeast3.private-connect.psdb.cloud         |
    | europe-west1            | `projects/planetscale-production/regions/europe-west1/serviceAttachments/edge-gateway-gcp-europe-west1`                       | gcp-europe-west1.private-connect.psdb.cloud            |
    | northamerica-northeast1 | `projects/planetscale-production/regions/northamerica-northeast1/serviceAttachments/edge-gateway-gcp-northamerica-northeast1` | gcp-northamerica-northeast1.private-connect.psdb.cloud |
    | us-central1             | `projects/planetscale-production/regions/us-central1/serviceAttachments/edge-gateway-gcp-us-central1`                         | gcp-us-central1.private-connect.psdb.cloud             |
    | us-east4                | `projects/planetscale-production/regions/us-east4/serviceAttachments/edge-gateway-gcp-us-east4`                               | gcp-us-east4.private-connect.psdb.cloud                |
  </Step>

  <Step>
    The endpoint creation process will take a minute or two. When finished, select the endpoint and verify the status is **Accepted**:

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/endpoint_status.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=a49e348b96a865b131b575fd8d125f33" alt="Showing endpoint status as 'Accepted'" data-og-width="1115" width="1115" data-og-height="433" height="433" data-path="docs/images/assets/docs/multi/gcp/private-service-connect/endpoint_status.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/endpoint_status.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f18e3a36bd630ae16f29eb24f1f4ed29 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/endpoint_status.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=958a90fc5720a9f985bfef8f366c9cf5 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/endpoint_status.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=70970e7b1b8648bf93de9dc072af02e9 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/endpoint_status.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=3e98e88bd496f411c69c07b6d7f17b39 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/endpoint_status.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=d2bc6ebf7c80b04b683a5b01a3dbdba3 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/multi/gcp/private-service-connect/endpoint_status.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=c7d3d2acc05a2c0a02b6ed8ac1cfebfe 2500w" />
    </Frame>
  </Step>
</Steps>

## Verifying the connectivity of your Private Service Connect endpoint

GCP will automatically create a private Cloud DNS zone in the project where the PSC consumer endpoints are created.

The domain name depends on the region the consumer endpoint was created in. Refer to the table above. The format of the domain name will be:

* `<Endpoint-Name>.<Domain-Name>`

For example, if you chose `edge` as the endpoint name in the `us-central1` region, the domain name for the endpoint would be:

* `edge.gcp-us-central1.private-connect.psdb.cloud`

<Steps>
  <Step>
    Log into any VM instance in the configured VPC and run `dig +short <Endpoint-Name>.<Domain-Name>` to confirm that DNS resolution resolves to the static IP address reserved during endpoint creation.

    ```
    $ dig +short edge.gcp-us-central1.private-connect.psdb.cloud
    10.128.0.17
    ```
  </Step>

  <Step>
    Run `curl https://<Endpoint-Name>.<Domain-Name>` to verify your connectivity. A successful response will yield `Welcome to PlanetScale`.

    ```
    curl https://edge.gcp-us-central1.private-connect.psdb.cloud
    Welcome to PlanetScale.
    ```
  </Step>
</Steps>

## Modifying your Connection Strings to utilize your Private Service Connect endpoint

By default, PlanetScale provides connection strings based on the `connect.psdb.cloud` domain name. To access your databases over the private endpoint change your connection string to match the `<Endpoint-Name>.<Domain-Name>` pattern.

For example, a connection string such as `gcp-us-central1.connect.psdb.cloud` would be changed to `edge.gcp-us-central1.private-connect.psdb.cloud` assuming `edge` was the Endpoint Name chosen during creation of the endpoint.

With this configured, you can leverage VPC peering to communicate between your GCP account and PlanetScale.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt