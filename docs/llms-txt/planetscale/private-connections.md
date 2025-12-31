# Source: https://planetscale.com/docs/vitess/connecting/private-connections.md

# Connecting to PlanetScale privately on AWS

## Connecting to PlanetScale privately via AWS PrivateLink

When your compliance mandates that your connections do not route through the public Internet, PlanetScale provides private connection endpoints to AWS regions via [AWS PrivateLink](https://aws.amazon.com/privatelink/). AWS PrivateLink is a form of *VPC peering* that does not send your traffic over the public internet. Private connections are included on Scaler Pro plans. There is no additional charge on PlanetScale's end, but this may impact your AWS bill.

Below is a list of instructions to set up your Virtual Private Cloud (VPC) to utilize a VPC endpoint when communicating with PlanetScale databases.

## Establishing a VPC endpoint

<Steps>
  <Step>
    Identify the AWS region that your VPC lives in, which we will refer to as `<aws-region>` for the rest of this document.
  </Step>

  <Step>
    Navigate to the "Endpoints" section on the VPC page and select "**Create Endpoint**."

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/create-new-endpoint.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=5aa9d629a8171ed0a24924aa9bdfe3f9" alt="Create a new endpoint" data-og-width="3260" width="3260" data-og-height="1416" height="1416" data-path="docs/images/private-connections/create-new-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/create-new-endpoint.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=04cccfae2d06bb554b93ddb72d526739 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/create-new-endpoint.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=d87e4b4df0a620e92e0cfba108de5db3 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/create-new-endpoint.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=708cc295c15f88c77b011fc840cecf68 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/create-new-endpoint.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=90822113c5b31ef85fea041e0fea54ee 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/create-new-endpoint.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=4dd17b94ddf4c59a7ff5ec11e4c008cf 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/create-new-endpoint.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=5e07d735eae86bf4bea5cf1ba87ac4d6 2500w" />
    </Frame>
  </Step>

  <Step>
    Select "Endpoint services that use NLBs and GWLBs"

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/type-of-endpoint.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=240ffb56c6adc56c8291a756636ef4f1" alt="Menu to select endpoint type" data-og-width="3134" width="3134" data-og-height="2080" height="2080" data-path="docs/images/private-connections/type-of-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/type-of-endpoint.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=8e3ce9478f9ad1cb414d3dc89920bed1 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/type-of-endpoint.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=af7d46ce33a13620c7d373c3c7276a23 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/type-of-endpoint.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=1a361dfe9358990e754ad9daefadce48 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/type-of-endpoint.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=c694a8505444fe795ad387e13999191b 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/type-of-endpoint.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=61b5a769dcec93c68ed9415e94ad8624 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/type-of-endpoint.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=7eb27018ed8001cd46275bb5cd8f6743 2500w" />
    </Frame>

    | AWS Region Name           | AWS Region     | VPC Endpoint Service Name                                      |
    | :------------------------ | :------------- | :------------------------------------------------------------- |
    | US East (Ohio)            | us-east-2      | `com.amazonaws.vpce.us-east-2.vpce-svc-069f88c102c1a7fba`      |
    | US East (N. Virginia)     | us-east-1      | `com.amazonaws.vpce.us-east-1.vpce-svc-02fef31be60d3fd35`      |
    | US West (Oregon)          | us-west-2      | `com.amazonaws.vpce.us-west-2.vpce-svc-0f63a383cb2d41919`      |
    | Asia Pacific (Mumbai)     | ap-south-1     | `com.amazonaws.vpce.ap-south-1.vpce-svc-06556ed2371c5fdd2`     |
    | Asia Pacific (Singapore)  | ap-southeast-1 | `com.amazonaws.vpce.ap-southeast-1.vpce-svc-046d8feae38660302` |
    | Asia Pacific (Sydney)     | ap-southeast-2 | `com.amazonaws.vpce.ap-southeast-2.vpce-svc-03e5578eeaf446c90` |
    | Asia Pacific (Tokyo)      | ap-northeast-1 | `com.amazonaws.vpce.ap-northeast-1.vpce-svc-099c246fa320e54d1` |
    | Europe (Frankfurt)        | eu-central-1   | `com.amazonaws.vpce.eu-central-1.vpce-svc-091260498e58d4dc3`   |
    | Europe (Ireland)          | eu-west-1      | `com.amazonaws.vpce.eu-west-1.vpce-svc-049577caa775e8648`      |
    | Europe (London)           | eu-west-2      | `com.amazonaws.vpce.eu-west-2.vpce-svc-0f69e183c9a555f03`      |
    | South America (São Paulo) | sa-east-1      | `com.amazonaws.vpce.sa-east-1.vpce-svc-09b11604d399b5c58`      |
    | Canada (Montreal)         | ca-central-1   | `com.amazonaws.vpce.ca-central-1.vpce-svc-0617a00ea4e327520`   |

    * Canada (Central) |
  </Step>

  <Step>
    Fill the "Service name" text box according to which region you want to establish AWS PrivateLink for. Once you have filled in the Service Name text box, click "Verify service".

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/service-name-and-verification.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=4b1d3bb6215941d86393a8a9619d8785" alt="Endpoint service name and verification" data-og-width="3772" width="3772" data-og-height="1276" height="1276" data-path="docs/images/private-connections/service-name-and-verification.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/service-name-and-verification.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=9b2b153ed5ae25f9b6667d06a091b5e7 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/service-name-and-verification.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=660e249f5da6c677e2c85e3bce95e2be 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/service-name-and-verification.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=bd9fb24799b1b029b9221f1183265cd5 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/service-name-and-verification.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=06c35eefe97f1f35dfc783d373cf7041 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/service-name-and-verification.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=608a6b83f64188e5d258f9f9a35f2c89 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/private-connections/service-name-and-verification.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=e6ddf72865e0abeca07d46676ec2a26d 2500w" />
    </Frame>
  </Step>

  <Step>
    Choose the VPC and subnets that should be peered with the PlanetScale service endpoint.
  </Step>

  <Step>
    Click the "Additional settings" dropdown arrow to reveal the "DNS name" configuration, and select the "Enable DNS name" checkbox.
  </Step>

  <Step>
    Choose the security group of your choice to control what can send traffic to the PlanetScale service endpoint.
  </Step>

  <Step>
    Click "Create endpoint" and verify that the VPC endpoint's status reports "Available" after a few minutes.
  </Step>
</Steps>

## Verifying the connectivity of your VPC endpoint

<Steps>
  <Step>
    In the AWS UI, confirm that the endpoint has successfully been created by verifying that the Status section of the endpoint reads "Available".

    <Warning>
      Some PlanetScale regions are named differently than AWS Provider regions. We will refer to the PlanetScale region as `<planetscale-region>` for the rest of this document.
    </Warning>
  </Step>

  <Step>
    Confirm that the Private DNS Names reads: `<planetscale-region>.private-connect.psdb.cloud`.
  </Step>

  <Step>
    Log into any EC2 instance in the configured VPC and run `dig +short <planetscale-region>.private-connect.psdb.cloud` to confirm that DNS resolution is producing IP Addresses in the range of your VPC's CIDR.

    ```bash  theme={null}
    dig +short us-east.private-connect.psdb.cloud
    172.31.16.197
    172.31.13.7
    ```
  </Step>

  <Step>
    Run `curl https://<planetscale-region>.private-connect.psdb.cloud` to verify your connectivity. A successful response will yield `Welcome to PlanetScale`.

    ```
    curl https://us-east.private-connect.psdb.cloud
    Welcome to PlanetScale.
    ```
  </Step>
</Steps>

## Modifying your Connection Strings to utilize your VPC endpoint.

By default, PlanetScale provides users with a connection string that reads `<planetscale-region>.connect.psdb.cloud`.

To utilize your newly configured VPC endpoint, prepend `private-` to the `connect` subdomain as shown above, yielding a connection string that reads `<planetscale-region>.private-connect.psdb.cloud`.

With this configured, you can leverage VPC peering to communicate between your AWS account and PlanetScale.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt