# Source: https://docs.anyscale.com/secrets/google-cloud.md

# Source: https://docs.anyscale.com/iam/google-cloud.md

# Manage Google Cloud service accounts for Anyscale clusters

[View Markdown](/iam/google-cloud.md)

# Manage Google Cloud service accounts for Anyscale clusters

This page describes how to use and manage service accounts for Anyscale clouds deployed on Google Cloud.

When you deploy an Anyscale cluster, the nodes in the cluster have a service account attached. The permissions in this service account grant access to required resources for workspace, jobs, and services.

## What service accounts does Anyscale use?[​](#what-accounts "Direct link to What service accounts does Anyscale use?")

The following table defines the service accounts used by Anyscale on Google Cloud:

| Term                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Control plane role (control plane service account) | Anyscale uses the term *control plane role* to describe the set of permissions granted by the customer to the Anyscale control plane.Anyscale on Google Cloud uses a model where admins configure a control plane service account that the Anyscale control plane accesses using Workload Identity Federation.                                                                                                                                                          |
| Anyscale cluster service accounts                  | When you deploy an Anyscale cluster, all virtual machines in the cluster assume a service account. This provides the nodes in your cluster direct access to resources in your cloud provider, such as your Cloud Storage bucket.You configure a default service account for clusters when you deploy your Anyscale cloud. You can add additional service accounts and define rules with cloud IAM mapping. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md). |

## Minimum privileges for Anyscale cluster service accounts[​](#minimum "Direct link to Minimum privileges for Anyscale cluster service accounts")

You can configure your Anyscale clusters to deploy with any service account. To use a service account on Anyscale, the service account must have the following minimum permissions:

* The service account needs read, write, and list access on the default storage bucket configured for your cloud. You can use the `Storage Admin` role to set these privileges.
* The control plane service account must have access to the target service account.

note

By default when you use `anyscale cloud setup`, Anyscale deploys a control plane service account with the `Owner` role.

This role grants access to all service accounts in your Google Cloud project, by default.

The [Compute Engine Service Agent](https://cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account) should have the `compute.serviceAgent` role on the your service account by default.

To create a service account, see the [Google Cloud docs on creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating).

## Common service account privileges[​](#common "Direct link to Common service account privileges")

To use a service account to interact with other Google Cloud services, you must add permissions. Follow the Google Cloud documentation for configuring IAM permissions for the following common services:

* [Google Secret Manager](https://cloud.google.com/secret-manager/docs/access-secret-version#required-roles)
* [Google Artifact Registry](https://cloud.google.com/artifact-registry/docs/access-control)
* [Google Cloud Key Management Service](https://cloud.google.com/kms/docs/iam)
* [BigQuery](https://cloud.google.com/bigquery/docs/control-access-to-resources-iam)

## Determine the service account used by an Anyscale cluster[​](#determine "Direct link to Determine the service account used by an Anyscale cluster")

Anyscale base images include the Google Python SDKs such as the `google.auth` library. Run the following Python code to get the identity of the service account attached to your cluster:

```
import google.auth.transport.requests

credentials, project = google.auth.default()
credentials.refresh(google.auth.transport.requests.Request())
print(credentials.service_account_email)
```

## Default service account for Anyscale clusters[​](#default "Direct link to Default service account for Anyscale clusters")

When you deploy an Anyscale cloud on Google Cloud, Anyscale configures a default service account that it attaches to each node in your Ray cluster. The name of the default service account has the following format:

```
cld-<anyscale-cloud-id>@<project-id>.iam.gserviceaccount.com
```

For Anyscale clouds configured to use virtual machines, the project ID is the Google Cloud project associated with your Anyscale cloud deployment.

## Edit the default service account[​](#edit "Direct link to Edit the default service account")

Google Cloud allows you to add permissions to a service account using any of the following patterns:

* Add the service account as a principal on the target infrastructure.
* Add a role to your service account that grants privileges on a collection of resources.
* Change the trust relationship between target infrastructure and a role in use by your service account.
* Create a custom role with the desired permissions and associate it with your service account.

note

When you add permissions to the default service account, these permissions pass to all users and clusters in your Anyscale cloud.

Use cloud IAM mapping to provide more granular permissions to Anyscale users. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).

## Configure a service account in another Google Cloud project[​](#cross-project "Direct link to Configure a service account in another Google Cloud project")

To use a service account in a separate Google Cloud project, you must complete the following additional steps:

1. Disable the [`iam.disableCrossProjectServiceAccountUsage`](https://cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project) boolean constraint in the project containing the service account.

2. Locate the [`Compute Engine Service Agent`](https://cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account) service account in the project containing your Anyscale cloud deployment. Grant the `compute.serviceAgent` role on the desired service account.

3. Grant the service account used by the Anyscale control plane the `roles/iam.serviceAccountUser` role on the desired service account. This is necessary for the Anyscale control plane to attach your service account to an instance.

4. Ensure the service account that you are configuring has read, write, and list access to the Google Storage bucket associated with your Anyscale cloud.

note

The Google Cloud project returned by [Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc#attached-sa) is the Anyscale cloud project, not the service account project.

## Specify a service account for an Anyscale cluster[​](#specify-a-service-account-for-an-anyscale-cluster "Direct link to Specify a service account for an Anyscale cluster")

To start a cluster with a service account,

note

Each cluster runs with a single service account. Specifying a service account overrides the default service for the cluster.

1. Locate the email address for your desired service account.
2. Create or modify a compute config. See [Create or version a compute config](/configuration/compute/create.md).
3. Add the service account email in the **Advanced settings > Instance config** field.
4. Use the compute config when configuring a workspace, job, or service.

The following JSON is an example configuration that specifies a service account and [access scope](https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam). Replace the `<service-account-email>` placeholder with the email address identifying your service account:

```
{
  "instance_properties": {
    "service_accounts": [
      {
        "email": "<service-account-email>",
        "scopes": [
          "https://www.googleapis.com/auth/cloud-platform"
        ]
      }
    ]
  }
}
```
