# Source: https://checklyhq.com/docs/integrations/iac/terraform/maintenance-windows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Service maintenance windows in Terraform

> Schedule planned maintenance windows to prevent checks from running during specific times

With [maintenance windows](/maintenance-windows/) you can schedule planned maintenance for whatever you are monitoring in order to prevent your checks from running at specific times. Maintenance windows have their own resource:

```terraform  theme={null}
resource "checkly_maintenance_windows" "maintenance-monthly" {
  name            = "Monthly maintenance"       // The name of the maintenance window
  starts_at       = "2022-08-24T00:00:00.000Z"  // The start date of the maintenance window
  ends_at         = "2022-08-25T00:00:00.000Z"  // The end date of the maintenance window
  repeat_unit     = "MONTH"                     // The repeat strategy for the maintenance window
  tags = [                                      // The tags of the checks and groups maintenance window should apply to
    "auto"
  ]
}
```

You can see all the configuration options for maintenance windows, as well as more examples, on the official Terraform registry [documentation page](https://registry.terraform.io/providers/checkly/checkly/latest/docs/resources/maintenance_windows).


Built with [Mintlify](https://mintlify.com).