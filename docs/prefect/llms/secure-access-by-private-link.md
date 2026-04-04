# Source: https://docs.prefect.io/v3/how-to-guides/cloud/manage-users/secure-access-by-private-link.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to secure access over PrivateLink

> Manage network access to Prefect Cloud accounts over PrivateLink.

PrivateLink is an available upgrade to certain Enterprise plans.\
[PrivateLink](https://aws.amazon.com/privatelink/) enables account administrators to restrict access to Prefect Cloud APIs and the UI at the network level, by routing all network traffic through AWS and GCP.\
Traffic between your network and Prefect Cloud is encrypted, and does not traverse the public internet.

To learn more, please contact your account manager or the Prefect team at [sales@prefect.io](mailto:sales@prefect.io).

Your Prefect team will provide the service endpoint to register.
Provide the following information for the registered endpoint so that Prefect can accept the connection:

* AWS Account Number
* AWS VPC IDs
* Source Region for each VPC (for example, `us-east-1`, `us-east-2`, etc.)
* VPC Endpoint ID

Prefect will match your pending connection to the information provided, and accept the connection once approved.

Once accepted, customers should enable "Modify Private DNS" to ensure the VPCs can resolve the Prefect service endpoint.

With Private DNS and the accepted connection, connectivity can be validated through curl:

```bash  theme={null}
curl -i https://api-internal.private.prefect.cloud/api/health
```

To configure Prefect clients and workers to use the endpoint, `PREFECT_API_URL` and `PREFECT_CLOUD_API_URL` should be set to the endpoint provided by Prefect.

```bash  theme={null}
prefect config set PREFECT_API_URL=https://api-internal.private.prefect.cloud/api/accounts/<ACCOUNT_ID>/workspaces/<WORKSPACE_ID>
prefect config set PREFECT_CLOUD_API_URL=https://api-internal.private.prefect.cloud/api
```


Built with [Mintlify](https://mintlify.com).