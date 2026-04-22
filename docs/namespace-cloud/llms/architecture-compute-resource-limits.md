<!-- Source: https://namespace.so/docs/architecture/compute/resource-limits -->

# Resource Limits

Learn what resource limits exist at Namespace, how concurrency limits work, and what concurrency limits are included in the different plans.

## Concurrency limits per platform

Concurrency limits are set per platform for each contract.
Namespace automatically manages environments so that only active workloads
(e.g. handling requests or with interactive workloads) consume concurrent capacity.

There are no restrictions on the number of instances that can run in parallel as long as they fit within the concurrency limit.
Each platform limit is independent and resources are not shared between platforms.

|  | Developer | Team | Business | Custom |
| --- | --- | --- | --- | --- |
| Linux | 32 vCPU,  64 GB RAM | 64 vCPU,  128 GB RAM | 160 vCPU,  320 GB RAM | Custom |
| MacOS | 12 vCPU,  28 GB RAM | 24 vCPU,  56 GB RAM | 48 vCPU,  112 GB RAM | Custom |
| Windows | N/A | 32 vCPU,  64 GB RAM | 80 vCPU,  160 GB RAM | Custom |

For example, in a Team plan for Linux, the concurrency limit is 64 vCPU, 128 GB RAM which can be used as:

- 4 instances with the shape of 16 vCPU, 32 GB RAM
- 8 instances of 8 vCPU, 16 GB RAM
- 32 instances of 2 vCPU, 4 GB RAM
- or any other combination with a total of 64 vCPU, 128 GB RAM.

For higher concurrency limit needs, reach out to our [Sales Team](mailto:sales@namespace.so) for custom plans
that scale up to thousands of vCPUs and TBs of RAM.

## Prioritizing and protecting concurrency limits

For larger organizations or multiple teams running different workflows,
it might be important to prioritize workflows, profiles, or teams so that the concurrency limits are not starved.

There are multiple solutions that allow you to handle this:

### Maximum number of concurrent instances per Runner Profile.

You can set the maximum number of concurrent instances per Runner Profile to restrict certain profiles that shouldn’t consume too many resources.
This can be set up by our team - reach out to [support@namespace.so](mailto:support@namespace.so) to try it out.

### Multi-tenant account

A multi-tenant account connects multiple workspaces to a global account.
In this case, concurrency limits can be set globally as well as per workspace.
You can, for example, set a lower limit for workspace A and allocate the remaining overall account limit to workspace B.

For example, if:

- Your account has an overall limit of 1,600 vCPU and 3,200 GB RAM
- Workspace A has a limit of 640 vCPU, 1,280 GB RAM
- Workspace B doesn't have a specific limit

Then whenever workspace A runs instances using all of their resources (640 vCPU, 1,280 GB RAM),
workspace B can still run instances with the remaining 960 vCPU and 1,920 GB RAM.

If workspace A doesn’t use any resources, workspace B can use the full concurrency of 1,600 vCPU and 3,200 GB RAM.

## API Error Details

When an instance creation request exceeds the workspace limits, the API returns an error with
structured error details that your code can inspect programmatically:

- **`ResourceLimitsError`**: Returned when the request exceeds concurrency limits. Includes the
  `requested`, `used`, and `limits` resource counts (vCPU, memory, instance count). The `kind` field
  indicates whether the limit is `CPU_MEMORY_LIMIT` or `INSTANCE_COUNT_LIMIT`.
- **`UsageLimitsError`**: Returned when the workspace has exhausted its usage quota for the billing
  period. Includes the `used` and `limits` values for `compute_unit_minutes` and `compute_wall_seconds`.
- **`PlatformNotAllowedError`**: Returned when the requested platform (e.g. `linux/arm64`) is not
  enabled for the workspace. Includes the `requested_platform` and the list of `allowed_platforms`.

See the [API reference](https://buf.build/namespace/cloud/docs/main:namespace.cloud.compute.v1beta) for details.

Last updated March 20, 2026
