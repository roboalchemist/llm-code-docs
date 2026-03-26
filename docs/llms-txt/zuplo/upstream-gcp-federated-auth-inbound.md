# Source: https://www.zuplo.com/docs/policies/upstream-gcp-federated-auth-inbound.md

# Upstream GCP Federated Auth Policy

This policy allows you to delegate authentication and authorization to your
gateway without writing any code on your origin service by adding an
authentication token to outgoing header allowing the service to be secured with
GCP IAM.

The tokens are issued using Zuplo's internal OAuth services and exchanged with
GCP using
[Workflow Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation).
This allows you to authenticate your Zuplo API to your origin without saving any
secrets in Zuplo.

This is a useful means of securing your origin server so that only your Zuplo
gateway can make requests against it.

This policy works with
[GCP Identity Aware Proxy](https://zuplo.com/docs/articles/gke-with-upstream-auth-policy)
or services like [Cloud Run](https://cloud.google.com/iap/docs/managing-access)
that natively support IAM authorization.

For information on how Google's service based auth works see
[Authenticating for invocation](https://cloud.google.com/functions/docs/securing/authenticating)

:::caution{title="Beta"}

This policy is in beta. You can use it today, but it may change in non-backward compatible ways before the final release.

:::

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-upstream-gcp-federated-auth-inbound-policy",
  "policyType": "upstream-gcp-federated-auth-inbound",
  "handler": {
    "export": "UpstreamGcpFederatedAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "audience": "https://hello-k7meruiynq-uc.a.run.app",
      "serviceAccountEmail": "zup-api@my-project.iam.gserviceaccount.com",
      "workloadIdentityProvider": "projects/932049231233/locations/global/workloadIdentityPools/my-pool/providers/my-provider"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `upstream-gcp-federated-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `UpstreamGcpFederatedAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `audience` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The audience for the minted JWT. This is typically the URL of your service. See the document [AuthRequirement](https://cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.AuthRequirement) for details.
- `serviceAccountEmail` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Google Service Account email address.
- `workloadIdentityProvider` **(required)** <code className="text-green-600">&lt;string&gt;</code> - No description available.
- `tokenLifetime` <code className="text-green-600">&lt;number&gt;</code> - The lifetime in seconds of the issued token. Defaults to `3600`.
- `tokenRetries` <code className="text-green-600">&lt;number&gt;</code> - The number of times to retry fetching the token in the event of a failure. Defaults to `3`.
- `expirationOffsetSeconds` <code className="text-green-600">&lt;number&gt;</code> - The number of seconds less than the token expiration to cache the token. Defaults to `300`.
- `useMemoryCacheOnly` <code className="text-green-600">&lt;boolean&gt;</code> - This is an advanced option that should only be used if you do not want to persist information in ZoneCache.

## Using the Policy

Before you can use this policy, you will need to have configured the following:

- Setup Workload Identity Federation in your GCP project
- Create a GCP service account with the appropriate permissions.

### Setup GCP Workload Identity Federation

Setting up Workload Identity Federation for Zuplo follows the instructions for
setting up a standard OIDC Identity Provider. Refer to
[Google's Documentation for additional details](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#configure).

To begin, navigate to the
[Workload Identity page of Google Cloud Console](https://console.cloud.google.com/iam-admin/workload-identity-pools).
You will find this in the **IAM** section on the menu.

If you don't already have one, create a new Workload Identity Pool. Then create
a new provider and select **OpenID Connect** as the provider type.

Complete the following values in the form:

- **Provider name**: Any Value
- **Provider ID**: Any Value
- **Issuer (URL)**:
  `https://dev.zuplo.com/v1/client-auth/auth_o8PUdhKxSTOiB794GWPwLQCD`
- **JWK File**: Do not set this value, GCP will perform automatic discovery of
  the OAuth configuration.
- **Audiences**: Select "Default Audience"

Copy the URL value for the **Default Audience** and record it for later use.

Click **Continue** and set the follow provider attribute mappings.

- `google.subject` =>
  `"zuplo::" + assertion.account + "::" + assertion.project + "::" + assertion.deployment`
- `attributes.account` => `assertion.account`
- `attributes.project` => `assertion.project`
- `attributes.deployment` => `assertion.deployment`

You can read about all the claims in the
[Zuplo Identity Token](https://zuplo.com/docs/articles/zuplo-id-token)
documentation.

Set **Attribute Conditions**

:::caution{title="Important Security Step"}

It is critical that you set at minimum the `attribute.account == "my-account"`
attribute condition. Without this restriction ANY Zuplo API would be able to
call your resources.

:::

Set the attribute conditions you want to use to restrict access to this Workload
Identity Pool. Generally, you only need to set this to restrict the account. You
will use IAM bindings to grant specific permissions in later steps.

To set the account condition set the following value.

```
attribute.account == "my-account"
```

If you want to set further conditions, you can do so as desired, for example to
restrict access to all environments in a project set the following.

```txt
attribute.account == "my-account" && attribute.project == "my-project"
```

### Create a Service Account

You Zuplo Identity Token will be granted access to act as if it where a service
account in your Google project. As such, you will need to create a service
account.

You can do so in the Google console or using the Google CLI:

```shell
gcloud iam service-accounts create zuplo-api \
  –-description="zuplo api sa"  \
  –-display-name="zuplo-api"
```

Next you need to create role binding for the Zuplo principal to impersonate the
service account:

- `SERVICE_ACCOUNT_EMAIL` is the email address of the service account.
- `PROJECT_NUMBER` is your numeric Google project number.
- `POOL_ID` is the id of the Workload Identity Pool you created earlier, for
  example `zuplo-pool`.
- `SUBJECT` is the same the concatenated value we set to the value of
  `google.subject` earlier. For example,
  `zuplo::my-account::my-project::my-deployment-1235`

```shell
gcloud iam service-accounts add-iam-policy-binding $SERVICE_ACCOUNT_EMAIL \
    --role roles/iam.workloadIdentityUser \
    --member "principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$POOL_ID/subject/$SUBJECT
```

Finally, grant your service account the permissions desired. For example, to
invoke Cloud Run services grant the `roles/run.invoker`

- `SERVICE_ACCOUNT_EMAIL` is the email address of the service account.
- `SERVICE_NAME` is the name of your Cloud Run service.

```shell
gcloud run services add-iam-policy-binding $SERVICE_NAME
  --member-"serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
  --role="roles/run.invoker"
```

### Set the Policy Options

With GCP Workload Federation setup, you can add the policy to your Zuplo API.

- `audience`: Set this to the resource you are planning to call, for example,
  the Cloud Run URL.
- `serviceAccountEmail` - Set this value to the email address of the service
  account previously created.
- `workloadIdentityProvider` - Set this to the value that was copied when
  setting up your Workload Identity Pool (called **Default Audience**). Remove
  the beginning `https://iam.googleapis.com/` part of the string.

```json
{
  "name": "gcp-federated-auth",
  "policyType": "upstream-gcp-federated-auth-inbound-policy",
  "handler": {
    "module": "$import(@zuplo/runtime)",
    "export": "UpstreamGcpFederatedAuthInboundPolicy",
    "options": {
      "audience": "https://test-basic-vhpkl3cvtq-uc.a.run.app",
      "serviceAccountEmail": "zup-api@my-project.iam.gserviceaccount.com",
      "workloadIdentityProvider": "projects/932049231233/locations/global/workloadIdentityPools/my-pool/providers/my-provider"
    }
  }
}
```

Read more about [how policies work](/articles/policies)
