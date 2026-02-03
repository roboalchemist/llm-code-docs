# Source: https://braintrust.dev/docs/admin/self-hosting/advanced.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced self-hosting topics

This guide covers advanced topics related to self-hosting.

## Enable or disable telemetry

Braintrust can send the following types of telemetry from your self-hosted data plane to Braintrust's control plane:

| Type      | Description                                                                                        |
| --------- | -------------------------------------------------------------------------------------------------- |
| `status`  | Health check information (enabled by default)                                                      |
| `metrics` | System metrics (CPU/memory) and Braintrust-specific metrics like indexing lag (enabled by default) |
| `usage`   | Billing usage telemetry for aggregate usage metrics (enabled by default)                           |
| `memprof` | Memory profiling statistics and heap usage patterns                                                |
| `logs`    | Application logs                                                                                   |
| `traces`  | Distributed tracing data                                                                           |

By default, `status`, `metrics`, and `usage` are enabled. You can change the defaults as follows:

<Tabs>
  <Tab title="AWS">
    Add the `monitoring_telemetry` variable to your `variables.tf` file, and include the types of telemetry you want to send in the validation condition as a comma-separated list:

    ```bash {19} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    variable "monitoring_telemetry" {
      description = <<-EOT
        The telemetry to send to Braintrust's control plane to monitor your deployment. Should be in the form of comma-separated values.

        Available options:
        - status: Health check information (default)
        - metrics: System metrics (CPU/memory) and Braintrust-specific metrics like indexing lag (default)
        - usage: Billing usage telemetry for aggregate usage metrics
        - memprof: Memory profiling statistics and heap usage patterns
        - logs: Application logs
        - traces: Distributed tracing data
      EOT
      type        = string
      default     = "status,metrics,usage"

      validation {
        condition = var.monitoring_telemetry == "" || alltrue([
          for item in split(",", var.monitoring_telemetry) :
          contains(["metrics", "logs", "traces", "status", "memprof", "usage"], trimspace(item))
        ])
        error_message = "The monitoring_telemetry value must be a comma-separated list containing only: metrics, logs, traces, status, memprof, usage."
      }
    }
    ```
  </Tab>

  <Tab title="GCP / Azure">
    Update the `controlPlaneTelemetry` setting in your Helm `values.yaml` file to include the types of telemetry you want to send:

    ```bash {10} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    # Global configs
    global:
      orgName: "<your org name on Braintrust>"
      # When createNamespace is true, the namespace will be created and resources will be in global.namespace
      # When createNamespace is false, resources will use .Release.Namespace (the namespace specified during helm install/upgrade)
      createNamespace: false
      namespace: "braintrust"
      namespaceAnnotations: {}
      labels: {}
      controlPlaneTelemetry: "status,metrics,usage,logs,traces,memprof"
    ```
  </Tab>
</Tabs>

Braintrust also has access to endpoints reporting metrics about the backfill and compaction status of Brainstore segments. This is metadata only, no customer data. To disable these endpoints, set the `DISABLE_SYSADMIN_TELEMETRY` environment variable to `true`.

## Secure sensitive customer data

Braintrust's servers and employees *do not* require access to your data plane for it to operate successfully. That means that you can
protect it behind a firewall/VPN and physically isolate it from access. When you use the Braintrust web application, it communicates
directly with the data plane (via CORS), and the data does not flow through any intermediate systems (the control plane, or otherwise)
before reaching your browser. While the data plane does send metrics and status telemetry to the control plane, it does not send logs, traces, or customer data. Because of this
architecture, our self-hosted customers do not generally list us as a subprocessor.

Like any third-party software, it is important that you establish the appropriate controls to ensure that your deployment is secure, and we're
very happy to help you do so. Ultimately, the goal of the control plane and data plane split is to provide you with the highest levels of security
and compliance.

## Customize the webapp URL

The SDKs guide users to `https://www.braintrust.dev` (or the `BRAINTRUST_APP_URL` variable) to view their experiments. However,
in certain advanced configurations, you may want to reverse proxy traffic to the `BRAINTRUST_APP_URL` from the SDKs while pointing users
to a different URL.

To do this, you can set the `BRAINTRUST_APP_PUBLIC_URL` environment variable to the URL of your webapp. By default, this variable is set to
the value of `BRAINTRUST_APP_URL`, but you can customize it as you wish. This variable is *only* used to display information, so even its destination
does not need to be accessible from the SDK.

## Constrain SDKs to the data plane

If you're self-hosting the data plane, it may also be advantageous to constrain the SDKs to only communicate with your data plane. Normally, they
communicate with the control plane to:

* Get your data plane's URL
* Register and retrieve metadata (e.g. about experiments)
* Print URLs to the webapp

The data plane can proxy the endpoints that the SDKs use to communicate with the control plane, allowing your SDKs to only communicate with the data plane
directly. Set the `BRAINTRUST_APP_URL` environment variable to the URL of your data plane and `BRAINTRUST_APP_PUBLIC_URL` to "[https://www.braintrust.dev](https://www.braintrust.dev)"
(or the URL of your webapp).

## Restrict URLs

In some cases, you may want to restrict the URLs that the SDKs or API server can communicate with. If so, you should
include the following URLs:

```
www.braintrust.dev
braintrust.dev
```

## Configure rate limits

By default, the Braintrust API server imposes rate limits against any external
domains it reaches out to, such as the `BRAINTRUST_APP_URL`. The purpose of
rate-limiting is to prevent unintentionally overloading any external domains,
which may block the API server IP in response.

By default, the rate limit is 100 requests per minute per user auth token. The
API server exposes the following variables to configure the rate limits:

* `OUTBOUND_RATE_LIMIT_MAX_REQUESTS`: Configure the number of requests per time
  window. This can be set to 0 to disable rate limiting.
* `OUTBOUND_RATE_LIMIT_WINDOW_MINUTES`: Configure the time window in minutes
  before the rate limit resets.

## Enable audit headers

When integrating with Braintrust,
especially in environments where actions need to be attributed
to specific users or for compliance purposes,
you might want to enable audit headers.
These headers provide additional metadata about the request and the resources it touched.

To enable audit headers, include the `x-bt-enable-audit: true` header in your API request.
When this header is present, the API response will include the following additional headers:

* `x-bt-audit-user-id`: The ID of the user who made the request
  (based on the provided API key or impersonation).
* `x-bt-audit-user-email`: The email of the user who made the request.
* `x-bt-audit-normalized-url`: A normalized representation of the API endpoint path that was called.
  Path parameters like object IDs are replaced with placeholders (for example, `/v1/project/[id]`).
* `x-bt-audit-resources`: A JSON-encoded, gzipped, and base64-encoded string
  containing a list of Braintrust resources (like projects, experiments, datasets, etc.)
  that were accessed or modified by the request.
  Each resource object includes its `type`, `id`, and `name`.

The `x-bt-audit-resources` header requires specific parsing due to its encoding.
Here's an example of how to parse it using the Python SDK:

```py  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os

import braintrust
import requests

API_URL = "https://api.braintrust.dev/v1"
# Ensure BRAINTRUST_API_KEY is set in your environment.
headers = {
    "Authorization": "Bearer " + os.environ["BRAINTRUST_API_KEY"],
    "x-bt-enable-audit": "true",  # Enable audit headers
}

# Example: Create a project.
response = requests.post(f"{API_URL}/project", headers=headers, json={"name": "audit-test-project"})
response.raise_for_status()

project_data = response.json()
print(f"Project created: {project_data['name']} (ID: {project_data['id']})")

# Access and parse audit headers.
user_id = response.headers.get("x-bt-audit-user-id")
user_email = response.headers.get("x-bt-audit-user-email")
normalized_url = response.headers.get("x-bt-audit-normalized-url")
resources_header = response.headers.get("x-bt-audit-resources")

print(f"Audit User ID: {user_id}")
print(f"Audit User Email: {user_email}")
print(f"Normalized URL: {normalized_url}")

if resources_header:
    try:
        # Use the provided utility to parse the resources header.
        resources = braintrust.parse_audit_resources(resources_header)
        print("Accessed/Modified Resources:")
        for resource in resources:
            print(f"  - Type: {resource['type']}, ID: {resource['id']}, Name: {resource['name']}")
    except Exception as e:
        print(f"Error parsing resources header: {e}")
else:
    print("No resources header found.")
```

This feature is useful for building audit logs or understanding resource usage patterns within your applications that interact with the Braintrust API.

## Control data retention

For features like [data retention](/admin/automations/data-management#data-retention), the data plane needs a [service token](/admin/access-control#service-accounts-and-service-tokens) with read-only permissions on projects to query object metadata and look up rentention policies configured in your organization.

Braintrust automatically provisions this service token when you configure your self-hosted data plane URL in [organization settings](/admin/organizations#configure-api-urls-self-hosted). The token is created with read-only permissions on projects and is securely stored in your data plane.

To verify the status or refresh the data plane service token, go to <Icon icon="settings-2" /> **Settings** > **Service tokens**. If the token doesn't exist, you can **Create** it. If it already exists, you can **Refresh** it at any time, and the data plane will automatically start using the new token.
