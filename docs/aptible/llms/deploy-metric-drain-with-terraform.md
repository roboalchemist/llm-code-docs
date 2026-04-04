# Source: https://www.aptible.com/docs/how-to-guides/app-guides/deploy-metric-drain-with-terraform.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Metric Drain with Terraform

Deploying [Metric Drains](/core-concepts/observability/metrics/metrics-drains/overview) with [Aptible's Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest) is relativley straight-forward, with some minor configuration exceptions. Aptible's Terraform Provider uses the Aptible CLI for authorization and authentication, so please run `aptible login` before we get started.

## Prerequisites

1. [Terraform](https://developer.hashicorp.com/terraform/install?ajs_aid=c5fc0f0b-590f-4dee-bf72-6f6ed1017286\&product_intent=terraform)
2. The [Aptible CLI](/reference/aptible-cli/cli-commands/overview)

You also need to be logged in to Aptible.

```
$ aptible login
```

## Getting Started

First, lets set up your Terraform directory to work with Aptible. Create a directory with a `main.tf` file and then run `terraform init` in the root of the directory.

Next, you will define where you want your metric drain to capture metrics. Whether this is a new environment or an exisiting one. If you are placing this in an exisiting environment you can skip this step, just make sure you have your [environment ID](https://github.com/aptible/terraform-provider-aptible/blob/master/docs/index.md#determining-the-environment-id).

```js  theme={null}
data "aptible_stack" "test-stack" {
    name = "test-stack"
}

resource "aptible_environment" "test-env" {
    stack_id = data.aptible_stack.test-stack.stack_id
    // if you use a shared stack above, you will have to manually grab your org_id
    org_id = data.aptible_stack.test-stack.org_id
    handle = "test-env"
}
```

Next, we will actually create the metric drain resource in Terraform, please select the drain type you wish to use from below.

<Tabs>
  <Tab title="Datadog">
    ```js  theme={null}
    resource "aptible_metric_drain" "datadog_drain" {
    env_id     = data.aptible_environment.example.env_id
    drain_type = "datadog"
    api_key    = "xxxxx-xxxxx-xxxxx"
    }
    ```
  </Tab>

  <Tab title="Aptible InfluxDB Database">
    ```js  theme={null}
    resource "aptible_metric_drain" "influxdb_database_drain" {
    env_id      = data.aptible_environment.example.env_id
    database_id = aptible_database.example.database_id
    drain_type  = "influxdb_database"
    handle      = "aptible-hosted-metric-drain"
    }
    ```
  </Tab>

  <Tab title="InfluxDB">
    ```js  theme={null}
    resource "aptible_metric_drain" "influxdb_drain" {
    env_id     = data.aptible_environment.example.env_id
    drain_type = "influxdb"
    handle     = "influxdb-metric-drain"
    url        = "https://influx.example.com:443"
    username   = "example_user"
    password   = "example_password"
    database   = "metrics"
    }
    ```
  </Tab>
</Tabs>

To check to make sure your changes are valid (in case of any changes not mentioned), run `terraform validate`

To deploy the above changes, run `terraform apply`

## Troubleshooting

## App configuration issues with Datadog

> Some users have reported issues with applications not sending logs to Datadog, applications will need additional configuration set. Below is an example.

```js  theme={null}
    resource "aptible_app" "load-test-datadog" {
        env_id = data.aptible_environment.example_environment.env_id
        handle = "example-app"
        config = {
            "APTIBLE_DOCKER_IMAGE" : "docker.io/datadog/agent:latest",
            "DD_APM_NON_LOCAL_TRAFFIC" : true,
            "DD_BIND_HOST" : "0.0.0.0",
            "DD_API_KEY" :"xxxxx-xxxxx-xxxxx",
            "DD_HOSTNAME_TRUST_UTS_NAMESPACE" : true,
            "DD_ENV" : "your environment",
            "DD_HOSTNAME" : "dd-hostname" # this does not have to match the hostname
        }
        service {
            process_type = "cmd"
            container_count = 1
            container_memory_limit = 1024
        }
    }
```

As a final note, if you have any questions about the Terraform provider please reach out to support or checkout our public [Terraform Provider Repository](https://github.com/aptible/terraform-provider-aptible) for more information!
