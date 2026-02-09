# Source: https://docs.pinecone.io/guides/production/bring-your-own-cloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Bring your own cloud

> Deploy Pinecone in your AWS or GCP account

Bring your own cloud (BYOC) lets you deploy Pinecone Database in your own AWS or GCP account to ensure data sovereignty and compliance, with Pinecone handling provisioning, operations, and maintenance.

<Note>
  BYOC is in [public preview](/release-notes/feature-availability) on AWS and GCP. To learn more about the offering, [contact Pinecone](https://www.pinecone.io/contact/?contact_form_inquiry_type=Product+Information).
</Note>

## Use cases

Pinecone BYOC is designed for organizations with high security and compliance requirements, for example:

* **Data sovereignty**: If your organization has strict data governance policies, Pinecone BYOC can help ensure that all data is stored and processed locally and does not leave your security perimeter.
* **Data residency**: The standard Pinecone managed service can be deployed in several [AWS or GCP cloud regions](/guides/index-data/create-an-index#cloud-regions). If your organization has specific data residency or latency constraints that require you to deploy in regions that Pinecone does not yet support, Pinecone BYOC gives you that flexibility.

## Architecture

<img className="block max-w-full dark:hidden" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=01b34857159d1eb8849f4250aa79ed00" data-og-width="2040" width="2040" data-og-height="1240" height="1240" data-path="images/byoc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e925a3467600c20f1c37e68e49d38acb 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c2c1b4077bf7f8dc593553a399e5fff6 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6688be4f64b0b4db4fe2ef90e04d6c44 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=4aa2923e28afc6a167bd8dfb28662c58 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c5c4c539a148f31e977c39c2ca813733 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8669a2c64a678822e7f2abe7dde6fdf0 2500w" />

<img className="hidden max-w-full dark:block" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=a27381222b26d1f31bc7d52b09f3ace0" data-og-width="2040" width="2040" data-og-height="1240" height="1240" data-path="images/byoc-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=f18f81d0f2a9387d2fd10231a4952284 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=7be91ffb937303f692dac9f4c7a812b6 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=06ec40f990b9795d42cd670c1f80e603 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6cc520e19003068137c960d9064648fc 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=902b44ca748163f9b199f128c5c7f543 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/byoc-dark.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6d1fc020dbfb7fc4d144012711c10a2a 2500w" />

The BYOC architecture employs a split model:

* **Data plane**: The data plane is responsible for storing and processing your records, executing queries, and interacting with object storage for index data. In a BYOC deployment, the data plane is hosted in your own AWS or GCP account within a dedicated VPC, ensuring that all data is stored and processed locally and does not leave your organizational boundaries. You use a [private endpoint](#configure-a-private-endpoint) (AWS PrivateLink or GCP Private Service Connect) as an additional measure to secure requests to your indexes.
* **Control plane**: The control plane is responsible for managing the index lifecycle as well as region-agnostic services such as user management, authentication, and billing. The control plane does not hold or process any records. In a BYOC deployment, the control plane is managed by Pinecone and hosted globally. Communication between the data plane and control plane is encrypted using TLS and employs role-based access control (RBAC) with minimal IAM permissions.

## Onboarding

The onboarding process for BYOC in AWS or GCP involves the following general stages:

<Steps>
  <Step title="Set up AWS or GCP account">
    If you don't already have an AWS or GCP account where you want to deploy Pinecone, you create one for this purpose.
  </Step>

  <Step title="Execute Terraform template">
    You download and run a Terraform template provided by Pinecone. This template creates essential resources, including an IAM role with scoped-down permissions and a trust relationship with Pinecone's AWS or GCP account.
  </Step>

  <Step title="Create environment">
    Pinecone deploys a data plane cluster within a dedicated VPC in your AWS or GCP account, and you [configure a private endpoint](#configure-a-private-endpoint) for securely connecting to your indexes via AWS PrivateLink or GCP Private Service Connect.
  </Step>

  <Step title="Validate">
    Once the environment is operational, Pinecone performs validation tests to ensure proper functionality.
  </Step>
</Steps>

## Configure a private endpoint

You use a [private endpoint](#configure-a-private-endpoint) to securely connect to your BYOC indexes. On AWS, you use the [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) service; on GCP, you use the [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) service.

<Tabs>
  <Tab title="AWS">
    Follow the instructions in the AWS documentation to [create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) for connecting to your indexes via AWS PrivateLink.

    * For **Resource configurations**, select the relevant resource for your Pinecone BYOC deployment.

    * For **Network settings**, select the VPC for your BYOC deployment.

    * In **Additional settings**, select **Enable DNS name** to allow you to access your indexes using a DNS name.
  </Tab>

  <Tab title="GCP">
    <Steps>
      <Step title="Create a private endpoint">
        Follow the instructions in the GCP documentation to [create a private endpoint](https://cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) for connecting to your indexes via GCP Private Service Connect.

        * Set the **Target service** to the following:

          ```
          projects/<YOUR-BYOC-PROJECT>/regions/<YOUR-BYOC-REGION>/serviceAttachments/pinecone-psc
          ```
        * Copy the IP address of the private endpoint. You'll need it later.
      </Step>

      <Step title="Create a private DNS zone">
        Follow the instructions in the GCP documentation to [create a private DNS zone](https://cloud.google.com/dns/docs/zones#create-private-zone).

        * Set the **DNS name** to the following:

          ```
          private.<YOUR-BYOC-ENVIRONMENT>.pinecone.io
          ```
        * Select the same VPC network as the private endpoint.
      </Step>

      <Step title="Add a resource record set">
        Follow the instructions in the GCP documentation to [add a resource record set](https://cloud.google.com/dns/docs/records#add-rrset).

        * Set the **DNS name** to **\***.

        * Set the **Resource record type** to **A**.

        * Set the **Ipv4 Address** to the IP address of the private endpoint.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Create an index

Once your BYOC environment is ready, you can create a BYOC index in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes) or via Pinecone API or [Python SDK](/reference/sdks/python/overview).

To create a BYOC index, set the `spec` parameter to the environment name provided to you during onboarding, for example:

<CodeGroup>
  ```python Python {9-11} theme={null}
  from pinecone import Pinecone, ByocSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
      name="example-byoc-index", 
      dimension=1536, 
      metric="cosine", 
      spec=ByocSpec(
          environment="aws-us-east-1-b921"
      ),
      deletion_protection="disabled",
      tags={
          "example": "tag"
      }
  )
  ```

  ```shell curl {11-15} theme={null}
  curl -s "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
          "name": "example-byoc-index",
          "vector_type": "dense",
          "dimension": 1536,
          "metric": "cosine",
          "spec": {
              "byoc": {
                  "environment": "aws-us-east-1-b921"
              }
          },
          "tags": {
              "example": "tag"
          },
          "deletion_protection": "disabled"
        }'
  ```
</CodeGroup>

## Read and write data

<Note>
  BYOC does not support reading and writing data from the index browser in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/-/browser).
</Note>

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
          -H "X-Pinecone-Api-Version: 2025-10"
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

## Monitoring

Pinecone engineers monitor the state of your BYOC deployment and manage incidents if they arise. In addition, you can [monitor performance metrics](/guides/production/monitoring) for your BYOC indexes in the Pinecone Console or with Prometheus or Datadog.

<Note>
  To use Prometheus, your monitoring tool must have access to your VPC.
</Note>

## Limitations

BYOC does not support the following:

* [Integrated embedding](/guides/index-data/indexing-overview#integrated-embedding), which relies on models hosted by Pinecone that are outsite of your AWS or GCP account.

* Reading and writing data from the index browser in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/-/browser). You must use the Pinecone API or SDKs instead.

* Using [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek) to secure data within a Pinecone project.

Also, to [monitor performance metrics with Prometheus](/guides/production/monitoring#monitor-with-prometheus), you must configure Prometheus within your VPC.

## FAQs

<AccordionGroup>
  <Accordion title="What is the difference between BYOC and Pinecone's standard service?">
    In the standard service, Pinecone manages all cloud resources and includes their cost in the service fee. In BYOC, customers provision and pay for cloud resources directly through their AWS or GCP account, providing greater control and data sovereignty as well as access to available AWS or GCP credits or discounts.

    Also, BYOC does not support certain features. See [Limitations](#limitations) for details.
  </Accordion>

  <Accordion title="How is data secured in BYOC?">
    Data is stored and processed exclusively within the customer's AWS or GCP account, with encryption applied at rest and in transit. Communication between the data plane and control plane is encrypted using TLS, and access is controlled via RBAC and scoped IAM permissions. AWS PrivateLink or GCP Private Service Connect is used for secure data plane API calls.
  </Accordion>

  <Accordion title="Is BYOC available in other cloud providers?">
    Currently, BYOC is available in AWS and GCP. Support for Azure is planned for future releases.
  </Accordion>
</AccordionGroup>
