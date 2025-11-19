# Source: https://docs.pinecone.io/guides/production/connect-to-aws-privatelink.md

# Configure Private Endpoints for AWS PrivateLink

> Secure Pinecone with private VPC endpoints.

This page describes how to create and use [Private Endpoints](/guides/production/security-overview#private-endpoints-for-aws-privatelink) to connect AWS PrivateLink to Pinecone while keeping your VPC private from the public internet.

## Use Private Endpoints to connect to PrivateLink

### Before you begin

The following steps assume you have:

* Access to the [AWS console](https://console.aws.amazon.com/console/home).

* [Created an Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-and-other-resources) in the same AWS [region](/guides/index-data/create-an-index#cloud-regions) as the index you want to connect to. You can optionally enable DNS hostnames and resolution, if you want your VPC to automatically discover the DNS CNAME for your PrivateLink and do not want configure a CNAME.

  * To [configure the routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html) yourself, use one of Pinecone's DNS entry for the corresponding region:

  | Index region              | Pinecone DNS entry                     |
  | ------------------------- | -------------------------------------- |
  | `us-east-1` (N. Virginia) | `*.private.aped-4627-b74a.pinecone.io` |
  | `us-west-2` (Oregon)      | `*.private.apw5-4e34-81fa.pinecone.io` |
  | `eu-west-1` (Ireland)     | `*.private.apu-57e2-42f6.pinecone.io`  |

* A [Pinecone Enterprise plan](https://www.pinecone.io/pricing/).

* [Created a serverless index](/guides/index-data/create-an-index#create-a-serverless-index) in the same AWS [region](/guides/index-data/create-an-index#cloud-regions) as your Amazon VPC.

<Note>
  Private Endpoints are configured at the project-level and you can add up to 10 endpoints per project. If you have multiple projects in your organization, Private Endpoints need to be set up separately for each.
</Note>

### 1. Create an Amazon VPC endpoint

In the [AWS console](https://console.aws.amazon.com/console/home):

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).

2. In the navigation pane, click **Endpoint**.

3. Click **Create endpoint**.

4. For **Service category**, select **Other endpoint services**.

5. In **Service settings**, enter the **Service name**, based on the region your Pinecone index is in:
   | Index region              | Service name                                              |
   | ------------------------- | --------------------------------------------------------- |
   | `us-east-1` (N. Virginia) | `com.amazonaws.vpce.us-east-1.vpce-svc-05ef6f1f0b9130b54` |
   | `us-west-2` (Oregon)      | `com.amazonaws.vpce.us-west-2.vpce-svc-04ecb9a0e0d5aab01` |
   | `eu-west-1` (Ireland)     | `com.amazonaws.vpce.eu-west-1.vpce-svc-03c6b7e17ff02a70f` |

6. Click **Verify service**.

7. Select the **VPC** to host the endpoint.

8. (Optional) In **Additional settings**, **Enable DNS name**.
   The enables you to access our service with the DNS name we configure. An additional CNAME record is needed if you disable this option.

9. Select the **Subnets** and **Subnet ID** for the endpoint.

10. Select the **Security groups** to apply to the endpoint.

11. Click **Create endpoint**.

12. Copy the **VPC endpoint ID** (e.g., `vpce-XXXXXXX`).
    This will be used to [add a Private Endpoint in Pinecone](#2-add-a-private-endpoint-in-pinecone).

### 2. Add a Private Endpoint in Pinecone

To add a Private Endpoint using the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to **Manage > Network**.
3. Click **Add a connection**.
4. Select your VPC region.
   Only indexes in the selected region in this project will be affected.
5. Click **Next**.
6. Enter the AWS VPC endpoint ID you copied in the [section above](#create-an-amazon-vpc-endpoint).
7. Click **Next**.
8. (optional) To **enable VPC endpoint access only**, turn the toggle on.
   This can also be enabled later. For more information, see [Manage internet access to your project](#optional-manage-internet-access-to-your-project).
9. Click **Finish setup**.

<Note>
  Private Endpoints only affect [data plane](/reference/api/latest/data-plane) access. [Control plane](/reference/api/latest/control-plane) access will continue over the public internet.
</Note>

## Read and write data

Once your private endpoint is configured, you can run data operations against an index as usual, but you must target the index using its private endpoint URL. The only difference in the URL is that `.svc.` is changed to `.svc.private.`.

You can get the private endpoint URL for an index from the Pinecone console or API.

<Tabs>
  <Tab title="Console">
    To get the private endpoint URL for an index from the Pinecone console:

    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select the project containing the index.
    3. Select the index.
    4. Copy the URL under **PRIVATE ENDPOINT**.
  </Tab>

  <Tab title="API">
    To get the private endpoint URL for an index from the API, use the [`describe_index`](/reference/api/latest/control-plane/describe_index) operation, which returns the private endpoint URL as the `private_host` value:

    <CodeGroup>
      ```JavaScript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone';

      const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

      await pc.describeIndex('docs-example');
      ```

      ```go Go theme={null}
      package main

      import (
          "context"
          "encoding/json"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
      )

      func prettifyStruct(obj interface{}) string {
          bytes, _ := json.MarshalIndent(obj, "", "  ")
          return string(bytes)
      }

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          idx, err := pc.DescribeIndex(ctx, "docs-example")
          if err != nil {
              log.Fatalf("Failed to describe index \"%v\": %v", idx.Name, err)
          } else {
              fmt.Printf("index: %v\n", prettifyStruct(idx))
          }
      }
      ```

      ```bash curl theme={null}
      PINECONE_API_KEY="YOUR_API_KEY"

      curl -i -X GET "https://api.pinecone.io/indexes/docs-example" \
          -H "Api-Key: YOUR_API_KEY" \
          -H "X-Pinecone-API-Version: 2025-04"
      ```
    </CodeGroup>

    The response includes the private endpoint URL as the `private_host` value:

    <CodeGroup>
      ```json JavaScript {6} theme={null}
      {
        name: 'docs-example',
        dimension: 1536,
        metric: 'cosine',
        host: 'docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io',
        privateHost: 'docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io',
        deletionProtection: 'disabled',
        tags: { environment: 'production' },
        embed: undefined,
        spec: {
          byoc: undefined,
          pod: undefined,
          serverless: { cloud: 'aws', region: 'us-east-1' }
        },
        status: { ready: true, state: 'Ready' },
        vectorType: 'dense'
      }
      ```

      ```go Go {5} theme={null}
      index: {
        "name": "docs-example",
        "dimension": 1536,
        "host": "docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io",
        "private_host": "docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io",
        "metric": "cosine",
        "deletion_protection": "disabled",
        "spec": {
          "serverless": {
            "cloud": "aws",
            "region": "us-east-1"
          }
        },
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "tags": {
          "environment": "production"
        }
      }
      ```

      ```json curl {12} theme={null}
      {
        "id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
        "vector_type": "dense",
        "name": "docs-example",
        "metric": "cosine",
        "dimension": 1536,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io",
        "private_host": "docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io",
        "spec": {
          "serverless": {
            "region": "us-east-1",
            "cloud": "aws"
          }
        },
        "deletion_protection": "disabled",
        "tags": {
          "environment": "production"
        }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Note>
  If you run data operations against an index from outside the Private Endpoint, you will get an `Unauthorized` response.
</Note>

## Manage internet access to your project

Once your Private Endpoint is configured, you can turn off internet access to your project. To enable VPC endpoint access only:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select your project.
3. Go to **Network > Access**.
4. Turn the **VPC endpoint access only** toggle on.
   This will turn off internet access to the project. This can be turned off at any point.

   <Warning>
     This access control is set at the *project-level* and can unintentionally affect Pinecone indexes that communicate via the internet in the same project. Only indexes communicating through Private Endpoints will continue to work.
   </Warning>

## Manage Private Endpoints

In addition to [creating Private Endpoints](#2-add-a-private-endpoint-in-pinecone), you can also:

* [View Private Endpoints](#view-private-endpoints)
* [Delete a Private Endpoint](#delete-a-private-endpoint)

### View Private Endpoints

To view Private Endpoints using the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to **Manage > Network**.
   A list of Private Endpoints displays with the associated **VPC ID** and **Cloud** provider.

### Delete a Private Endpoint

To delete a Private Endpoint using the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to **Manage > Network**.
3. For the Private Endpoint you want to delete, click the *...* (Actions) icon.
4. Click **Delete**.
5. Enter the endpoint name.
6. Click **Delete Endpoint**.
