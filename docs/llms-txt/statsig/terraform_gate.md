# Source: https://docs.statsig.com/integrations/terraform/terraform_gate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Gates With Terraform

You can create a .tf file (Terraform File) to configure your Statsig feature gates. All features of [console/v1/gates](/console-api/gates) are supported. The layout is very similar to the JSON body of a /gates request.

Requiring the Statsig provider. (You will need to change the version).

```go  theme={null}
terraform {
  required_providers {
    statsig = {
      version = "x.x.x"
      source  = "statsig-io/statsig"
    }
  }
}
```

## Basic Example

Creating a basic gate resource

```go  theme={null}
resource "statsig_gate" "my_gate" {
  name        = "my_gate"
  description = "A short description of what this Gate is used for."
  is_enabled  = true
  id_type     = "userID"
  rules {
    name            = "Public"
    pass_percentage = 100
    conditions {
      type = "public"
    }
  }
}
```

## Conditions

All Console API conditions are supported but the syntax needs a little tweaking.

* **type** | string | The [type](/console-api/rules#all-conditions) of condition it is.
* **operator** | string | What form of evaluation should be run against the **target\_value**.
* **target\_value** | \[string] | The value or values you wish to evaluate. Note: This must be an array, and elements should be of string type. (You can put quotes on numbers. 31 -> "31")
* **field** | string | Only for custom\_field condition type. The name of the field you wish to pull for evaluation from the "custom" object on a user.

```go  theme={null}
conditions {
  type         = "custom_field"
  target_value = ["31"]
  operator     = "gt"
  field        = "age"
}
```

See the full list of conditions [here](/console-api/rules#all-conditions).

A full gate example is included in the open source Github repo [https://github.com/statsig-io/terraform-provider-statsig/blob/main/examples/resources/statsig\_gate/resource.tf](https://github.com/statsig-io/terraform-provider-statsig/blob/main/examples/resources/statsig_gate/resource.tf)


Built with [Mintlify](https://mintlify.com).