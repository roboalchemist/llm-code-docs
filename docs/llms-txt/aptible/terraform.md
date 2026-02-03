# Source: https://www.aptible.com/docs/reference/terraform.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Terraform

> Learn to manage Aptible resources directly from Terraform

<Card title="Aptible Terraform Provider" icon={<svg fill="#E09600" width="30px" height="30px"  viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="none">  <g fill="#E09600">  <path d="M1 0v5.05l4.349 2.527V2.526L1 0zM10.175 5.344l-4.35-2.525v5.05l4.35 2.527V5.344zM10.651 10.396V5.344L15 2.819v5.05l-4.349 2.527zM10.174 16l-4.349-2.526v-5.05l4.349 2.525V16z"/>  </g>  </svg>} href="https://registry.terraform.io/providers/aptible/aptible/latest/docs" />

## Overview

The [Aptible Terraform provider](https://registry.terraform.io/providers/aptible/aptible) allows you to manage your Aptible resources directly from Terraform - enabling infrastructure as code (IaC) instead of manually initiating Operations from the Aptible Dashboard of Aptible CLI. You can use the Aptible Terraform to automate the process of setting up new Environments, including:

* Creating, scaling, modifying, and deprovisioning Apps and Databases

* Creating and deprovisioning Log Drains and Metric Drains (including the [Aptible Terraform Metrics Module](https://registry.terraform.io/modules/aptible/metrics/aptible/latest), which provisions built Grafana dashboards with alerting)

* Creating, modifying, and provisioning App Endpoints and Database Endpoints

For an overview of what actions the Aptible Terraform Provider supports, see the [Feature Support Matrix](/reference/interface-feature#feature-support-matrix).

## Using the Aptible Terraform Provider

### Environment definition

The Environment resource is used to create and manage [Environments](https://www.aptible.com/docs/core-concepts/architecture/environments) running on Aptible Deploy.

```perl  theme={null}
data "aptible_stack" "example" {
    name = "example-stack"
}

resource "aptible_environment" "example" {
  stack_id = data.aptible_stack.example.stack_id
  org_id   = data.aptible_stack.example.org_id
  handle   = "example-env"
}
```

### Deployment and managing Docker images

[Direct Docker Image Deployment](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) is currently the only deployment method supported with Terraform. If you'd like to use Terraform to deploy your Apps and you're currently using [Dockerfile Deployment](/how-to-guides/app-guides/deploy-from-git) you'll need to switch. See [Migrating from Dockerfile Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) for tips on how to do so.

If you’re already using Direct Docker Image Deployment, managing this is pretty easy. Set your Docker repo, registry username, and registry password as the configuration variables `APTIBLE_DOCKER_IMAGE`, `APTIBLE_PRIVATE_REGISTRY_USERNAME`, and `APTIBLE_PRIVATE_REGISTRY_PASSWORD`.

```perl  theme={null}
resource "aptible_app" "example-app" {
    env_id         = data.aptible_environment.example.env_id
    handle         = "example-app"
    config = {
        "APTIBLE_DOCKER_IMAGE": "",
        "APTIBLE_PRIVATE_REGISTRY_USERNAME": "",
        "APTIBLE_PRIVATE_REGISTRY_PASSWORD": "",
    }
}
```

<Warning> Please ensure you have the correct image, username, and password set every time you run `terraform apply`. If you are deploying outside of Terraform, you will also need to keep your Terraform configuration up to date. See [Terraform's refresh Terraform configuration documentation](https://developer.hashicorp.com/terraform/cli/commands/refresh) for more information.</Warning>

<Tip> For a step-by-step tutorial in deploying a metric drain with Terraform, please visit our [Terraform Metric Drain Deployment Guide](/how-to-guides/app-guides/deploy-metric-drain-with-terraform)</Tip>

## Managing Services

### Managing Services

The service `process_type` should match what's contained in your Procfile. Otherwise, service container sizes and container counts cannot be defined and managed individually. The process\_type maps directly to the Service name used in the Procfile. If you are not using a Procfile, you will have a single Service with the process\_type of cmd.

```perl  theme={null}
resource "aptible_app" "example-app" {
  env_id         = data.aptible_environment.example.env_id
  handle         = "exmaple-app"
  config = {
    "APTIBLE_DOCKER_IMAGE": "",
    "APTIBLE_PRIVATE_REGISTRY_USERNAME": "",
    "APTIBLE_PRIVATE_REGISTRY_PASSWORD": "",
  }
  service {
    process_type           = "sidekiq"
    container_count        = 1
    container_memory_limit = 1024
  }
  service {
    process_type           = "web"
    container_count        = 2
    container_memory_limit = 4096
  }
}
```

### Referencing Resources in Configurations

Resources can easily be referenced in configurations when using Terraform. Here is an example of an App configuration that references Databases:

```perl  theme={null}
resource "aptible_app" "example-app" {
    env_id = data.aptible_environment.example.env_id
    handle = "example-app"
    config = {
        "REDIS_URL": aptible_database.example-redis-db.default_connection_url,
        "DATABASE_URL": aptible_database.example-pg-db.default_connection_url,
    }
    service {
        process_type           = "cmd"
        container_count        = 1
        container_memory_limit = 1024
    }
}

resource "aptible_database" "example-redis-b" {
  env_id         = data.aptible_environment.example.env_id
  handle         = "example-redis-db"
  database_type  = "redis"
  container_size = 512
  disk_size      = 10
  version        = "5.0"
}

resource "aptible_database" "example-pg-db" {
  env_id         = data.aptible_environment.example.env_id
  handle         = "example-pg-db"
  database_type  = "postgresql"
  container_size = 1024
  disk_size      = 10
  version        = "12"
}
```

Some apps use the port, hostname, username, and password broken apart rather than as a standalone connection URL. Terraform can break those apart, or you can add some logic in your app or container entry point to achieve this. This also works with endpoints. For example:

```perl  theme={null}
resource "aptible_app" "example-app" {
  env_id = data.aptible_environment.example.env_id
  handle = "example-app"
  config = {
    "ANOTHER_APP_URL": aptible_endpoint.example-endpoint.virtual_domain,
  }
  service {
    process_type = "cmd"
    container_count = 1
    container_memory_limit = 1024
  }
}

resource "aptible_app" "another-app" {
  env_id = data.aptible_environment.example.env_id
  handle = "another-app"
  config = {}
  service {
    process_type = "cmd"
    container_count = 1
    container_memory_limit = 1024
  }
}

resource "aptible_endpoint" "example-endpoint" {
  env_id         = data.aptible_environment.example.env_id
  default_domain = true
  internal       = true
  platform       = "alb"
  process_type   = "cmd"
  endpoint_type  = "https"
  resource_id    = aptible_app.another-app.app_id
  resource_type  = "app"
  ip_filtering   = []
}
```

The value `aptible_endpoint.example-endpoint.virtual_domain` will be the domain used to access the Endpoint (so `app-0000.on-aptible.com` or [`www.example.com`).](https://www.example.com\).)

<Note> If your Endpoint uses a wildcard certificate/domain, `virtual_domain` would be something like `*.example.com` which is not a valid domain name. Therefore, when using a wildcard domain, you should provide the subdomain you want your application to use to access the Endpoint, like `www.example.com`, rather than relying solely on the Endpoint's `virtual_domain`.</Note>

## Circular Dependencies

One potential risk of relying on URLs to be set in App configurations is circular dependencies. This happens when your App uses the Endpoint URL in its configuration, but the Endpoint cannot be created until the App exists. Terraform does not have a graceful way of handling circular dependencies. While this approach won't work for default domains, the easiest option is to define a variable that can be referenced in both the Endpoint resource and the App configuration:

```perl  theme={null}
variable "example_domain" {
  description = "The domain name"
  type        = string
  default     = "www.example.com"
}

resource "aptible_app" "example-app" {
  env_id = data.aptible_environment.example.env_id
  handle = "example-app"
  config = {
    "ANOTHER_APP_URL": var.example_domain,
  }
  service {
    process_type = "cmd"
    container_count = 1
    container_memory_limit = 1024
  }
}

resource "aptible_endpoint" "example-endpoint" {
  env_id         = data.aptible_environment.example.env_id
  endpoint_type  = "https"
  internal       = false
  managed        = true
  platform       = "alb"
  process_type   = "cmd"
  resource_id    = aptible_app.example-app.app_id
  resource_type  = "app"
  domain         = var.example_domain
  ip_filtering   = []
}
```

## Managing DNS

While Aptible does not directly manage your DNS, we do provide you the information you need to manage DNS. For example, if you are using Cloudflare for your DNS, and you have an endpoint called `example-endpoint`, you would be able to create the record:

```perl  theme={null}
resource "cloudflare_record" "example_app_dns" {
  zone_id = cloudflare_zone.example.id
  name    = "www.example"
  type    = "CNAME"
  value   = aptible_endpoint.example-endpoint.id
  ttl     = 60
}
```

And for the Managed HTTPS [dns-01](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls#dns-01) verification record:

```perl  theme={null}
resource "cloudflare_record" "example_app_acme" {
  zone_id = cloudflare_zone.example.id
  name    = "_acme-challange.www.example"
  type    = "CNAME"
  value   = "acme.${aptible_endpoint.example-endpoint.id}"
  ttl     = 60
}
```

## Secure/Sensitive Values

You can use Terraform to mark values as secure. These values are redacted in the output of `terraform plan` and `terraform apply`.

```perl  theme={null}

variable "shhh" {
  description = "A sensitive value"
  type        = string
  sensitive   = true
}

resource "aptible_app" "example-app" {
  env_id = data.aptible_environment.example.env_id
  handle = "example-app"
  config = {
    "SHHH": var.shhh,
  }
  service {
    process_type = "cmd"
    container_count = 1
    container_memory_limit = 1024
  }
}
```

When you run `terraform state show` these values will also be marked as sensitive. For example:

```perl  theme={null}
resource "aptible_app" "example-app" {
    app_id   = 000000
    config   = {
        "SHHH" = (sensitive)
    }
    env_id   = 4749
    git_repo = "git@beta.aptible.com:terraform-example-environment/example-app.git"
    handle   = "example-app"
    id       = "000000"

    service {
        container_count        = 1
        container_memory_limit = 1024
        process_type           = "cmd"
    }
}
```

## Spinning down Terraform Resources

Resources created using Terraform should not be deleted through the Dashboard or CLI. Deleting through the Dashboard or CLI does not update the Terraform state which will result in errors the next time you run terraform plan or terraform apply. Instead, use terraform plan -destroy to see which resources will be destroyed and then use terraform destroy to destroy those resources.

If a Terraform-created resource is deleted through the Dashboard or CLI, use the terraform state rm [command](https://developer.hashicorp.com/terraform/cli/commands/state/rm) to remove the deleted resource from the Terraform state file. The next time you run terraform apply, the resource will be recreated to reflect the configuration.
