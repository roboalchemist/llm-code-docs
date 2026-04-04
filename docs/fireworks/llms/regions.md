# Source: https://docs.fireworks.ai/deployments/regions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Regions

> Fireworks runs a global fleet of hardware on which you can deploy your models.

## Availability

Current region availability:

| **Region**           | **Quota availability** | **Hardware availability**              |
| -------------------- | ---------------------- | -------------------------------------- |
| `US_IOWA_1`          | Available by default   | `NVIDIA_H100_80GB`                     |
| `US_TEXAS_2`         | Available by default   | `NVIDIA_H100_80GB`                     |
| `REGION_UNSPECIFIED` | Available by default   | `ANY OF THE ABOVE/BELOW`               |
| `US_ARIZONA_1`       | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_CALIFORNIA_1`    | Must be requested      | `NVIDIA_H200_141GB`                    |
| `US_GEORGIA_2`       | Must be requested      | `NVIDIA_B200_180GB`                    |
| `US_ILLINOIS_1`      | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_ILLINOIS_2`      | Must be requested      | `NVIDIA_A100_80GB`                     |
| `US_UTAH_1`          | Must be requested      | `NVIDIA_B200_180GB`                    |
| `US_VIRGINIA_1`      | Must be requested      | `NVIDIA_H100_80GB` `NVIDIA_H200_141GB` |
| `US_WASHINGTON_1`    | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_WASHINGTON_2`    | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_WASHINGTON_3`    | Must be requested      | `NVIDIA_B200_180GB`                    |
| `EU_FRANKFURT_1`     | Must be requested      | `NVIDIA_H100_80GB`                     |
| `EU_ICELAND_1`       | Must be requested      | `NVIDIA_H200_141GB`                    |
| `EU_ICELAND_2`       | Must be requested      | `NVIDIA_H200_141GB`                    |
| `AP_TOKYO_1`         | Must be requested      | `NVIDIA_H100_80GB`                     |
| `AP_TOKYO_2`         | Must be requested      | `NVIDIA_H200_141GB`                    |

<Tip>
  If you hit a quota limit when requesting a specific region, try launching the deployment without specifying a region. This taps into your global account quota, which is more flexible.
  Deployments may still be placed in `Must be requested` regions when region is not specified, but region-level quota must be enabled to explicitly specify that region when creating
  a deployment.
</Tip>

## Using a region

When creating a deployment, you can pass the `--region` flag:

```
firectl deployment create accounts/fireworks/models/llama-v3p1-8b-instruct \
    --region US_IOWA_1
```

## Changing regions

Updating a region for a deployment in-place is currently not supported. To move a deployment between regions, please
create a new deployment in the new region, then delete the old deployment.

## Quotas

Each region has it's own separate quota for each hardware type. To view your current quotas, run

```
firectl quota list
```

If you need deployments in a non-GA region, please contact our team at [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai).
