# Source: https://render.com/docs/terraform-provider.md

# Render Terraform Provider — Manage Render resources alongside your other infrastructure.

You can use Render's official [Terraform provider](https://registry.terraform.io/providers/render-oss/render/latest) to incorporate your Render resources into your existing Terraform configuration. This enables you to manage Render services alongside the rest of your infrastructure.

*See an example resource declaration*

```hcl
# Basic example web service configuration
resource "render_web_service" "web" {
  name               = "terraform-web-service"
  plan               = "starter"
  region             = "oregon"
  start_command      = "npm start"

  runtime_source = {
    native_runtime = {
      auto_deploy   = true
      branch        = "main"
      build_command = "npm install"
      repo_url = "https://github.com/render-examples/express-hello-world"
      runtime  = "node"
    }
  }
}
```

Documentation for the provider is available in the Terraform Registry:

## Terraform or Blueprints?

We recommend using [Blueprints](infrastructure-as-code) (Render's IaC model) where possible.

If you don't need to include any non-Render infrastructure in your configuration, it's quicker to get started with Blueprints, and they're tightly integrated with the Render platform.

If you _do_ need to manage your Render services alongside other infrastructure, use the Render Terraform provider.