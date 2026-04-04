# Source: https://docs.vespa.ai/en/operations/private-endpoints.html.md

# Private endpoints

 

Vespa Cloud lets you set up private endpoint services on your application clusters, for exclusive access from your own, co-located VPCs with the same cloud provider. This is supported for AWS deployments through AWS's [PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), and for GCP deployments through GCP's [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect). This guide takes you through the necessary configuration steps for either [AWS PrivateLink](#aws-private-link) or for [GCP Private Service Connect](#gcp-private-service-connect).

Private endpoints are only supported in zones in the [prod environment](environments.html#prod).

 **Note:** Private endpoints use mTLS authentication by default, and token-based authentication must be explicitly enabled. See [configuring private endpoint authentication method](#authentication-methods).

## AWS PrivateLink

Required information:

| Item | Description |
| --- | --- |
| **Your IAM account number** | The numeric identifier for your AWS account. |
| **VPC ID** | The identifier of your AWS VPC where you wish to connect to the service endpoints from. |
| **AWS region name** | The name of the AWS region to connect from. Note that you can only connect to a service in the same region, or, if public endpoints are disabled, in the same AWS availability zone. |

Procedure:

1. **Configure a private endpoint service on your Vespa Cloud Container cluster**

2. **Find the service ID of your endpoint services**

3. **Create the VPC interface endpoint**

4. **Verify the VPC endpoint is connected to the Vespa cluster**

5. **Verify your Vespa cluster is reachable from within your VPC**

 **Note:** Enclave users may set up high-availability PrivateLink endpoints connected across multiple AZs. Contact[Vespa support](https://vespa.ai/support/) for guidance.

## GCP Private Service Connect

Prerequisites:

| Item | Description |
| --- | --- |
| **Enabled GCP APIs** | The _Compute Engine_, _Service Directory_ and _Cloud DNS_ APIs must all be enabled in your GCP account:
```
$ gcloud services enable compute.googleapis.com
$ gcloud services enable dns.googleapis.com
$ gcloud services enable servicedirectory.googleapis.com
```
 |
| **Your GCP project name** | The string identifier for your GCP account, like _resonant-diode-123456_ |
| **VPC network and subnetwork names** | The name of the network and subnetwork to create your consumer endpoint in. |

Procedure:

1. **Configure a private endpoint service on your Vespa Cloud Container cluster**

2. **Find the service ID of your endpoint services**

3. **Create the service consumer endpoint**

4. **Verify the VPC endpoint is connected to the Vespa cluster**

5. **Verify your Vespa cluster is reachable from within your VPC**

6. **Generated endpoints with Private Service Connect**

## Configuring Private Endpoint Authentication

You can configure private endpoints to use either mTLS or token-based authentication with the optional `auth-method` attribute. If the attribute is not set, mTLS will be used by default. The attribute is only allowed with `private` type endpoints and must be either `mtls` or `token`.

 **Note:** Only one authentication method can be enabled at the same time. Enabling token authentication will disable mTLS authentication for the private endpoint, and vice versa.

#### Example with token-based authentication

```
```
<deployment version="1.0">
    <prod>
        <region>region-1</region>
        <region>region-2</region>
    </prod>
    <endpoints>
        <endpoint type="private" auth-method='token'>
            <allow with="aws-private-link" arn="arn:aws:iam::123123123123:root" />
        </endpoint>
    </endpoints>
</deployment>
```
```

#### Changing authentication method for an existing deployment

If you have an existing deployment with a private endpoint, you must remove any connections and redeploy with a[validation override](../reference/applications/validation-overrides.html)to modify the authentication method:

1. Remove the VPC interface endpoint (AWS) or service consumer endpoint (GCP) configured above 
2. Change the authentication method for the endpoint in `deployment.xml`
3. Deploy with the `zone-endpoint-change` validation override: 

```
```
<validation-overrides>
    <allow until="2023-04-31" comment="Change private endpoint authentication">
        zone-endpoint-change
    </allow>
</validation-overrides>
```
```

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [AWS PrivateLink](#aws-private-link)
- [GCP Private Service Connect](#gcp-private-service-connect)
- [Configuring Private Endpoint Authentication](#authentication-methods)

