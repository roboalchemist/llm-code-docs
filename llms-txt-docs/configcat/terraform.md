# Source: https://configcat.com/docs/integrations/terraform.md

# Terraform - Manage feature flags from HCL scripts

[ConfigCat Feature Flags Provider](https://registry.terraform.io/providers/configcat/configcat) allows you to configure and access ConfigCat resources via ConfigCat Public Management API with [Terraform.](https://www.terraform.io/)

## Installation[​](#installation "Direct link to Installation")

Please refer to the [official documentation](https://registry.terraform.io/providers/configcat/configcat/latest/docs).

## Sample usage[​](#sample-usage "Direct link to Sample usage")

```
terraform {
  required_providers {
    configcat = {
      source  = "configcat/configcat"
      version = "~> 5.0"
    }
  }
}

provider "configcat" {
  // Get your ConfigCat Public API credentials at https://app.configcat.com/my-account/public-api-credentials
  basic_auth_username = var.configcat_basic_auth_username
  basic_auth_password = var.configcat_basic_auth_password
}

# Retrieve your Product
data "configcat_products" "my_products" {
  name_filter_regex = "ConfigCat's product"
}

# Retrieve your Config
data "configcat_configs" "my_configs" {
  product_id        = data.configcat_products.my_products.products[0].product_id
  name_filter_regex = "Main Config"
}

# Retrieve your Environment
data "configcat_environments" "my_environments" {
  product_id        = data.configcat_products.my_products.products[0].product_id
  name_filter_regex = "Test"
}

# Create a Feature Flag/Setting
resource "configcat_setting" "setting" {
  config_id    = data.configcat_configs.my_configs.configs[0].config_id
  key          = "isAwesomeFeatureEnabled"
  name         = "My awesome feature flag"
  hint         = "This is the hint for my awesome feature flag"
  setting_type = "boolean"
  order        = 0
}

# Initialize the Feature Flag/Setting's value
resource "configcat_setting_value" "setting_value" {
  environment_id = data.configcat_environments.my_environments.environments[0].environment_id
  setting_id     = configcat_setting.setting.id
  value          = "false"
}
```

## Useful Resources[​](#useful-resources "Direct link to Useful Resources")

* [Automating ConfigCat Resources with Terraform - Blog Post](https://configcat.com/blog/2023/06/02/infrastructure-as-code-terraform-integration/)
