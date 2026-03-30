# Source: https://novita.ai/docs/guides/gpu-instance-pricing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GPU Instance Pricing

## On-Demand Pricing

### Introduction

On-Demand Pricing is designed to offer users the flexibility to access computational resources without any long-term commitments or upfront costs. This pricing model is ideal for users who require compute power on an as-needed basis, whether for short-term projects, variable workloads, or unpredictable processing demands.

### Billing Structure of On-Demand Pricing

Includes "computing resources" and "storage resources", you can view the billing details on the <a href="https://novita.ai/gpu-instance/console/billing" target="_blank">Billing Explore</a>.

#### 1. Computing Resources

**<u>Cost = Instance Unit Price × Billing Duration × Number of Cards</u>**

<Tip>
  * Billing duration is accurate to the second and settled hourly;

  * You can view the unit prices of various instance specifications on the <a href="https://novita.ai/gpu-instance/console" target="_blank">GPU Instance Explore</a>;

  * The billing start time is when the instance is successfully created and enters the **pulling** state, and the billing stop time is when the instance is stopped.
</Tip>

#### 2. Storage Resources

| **Billing Item** | **Billing Method** | **Explanation**                                                                            | **Billing Logic**                                      |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| Container Disk   | Pay-as-you-go      | Supports **60GB** free quota, charges for the excess based on capacity and usage duration. | Unit price for the excess capacity: **\$0.005/GB/day** |
| Volume Disk      | Pay-as-you-go      | Charges based on capacity and usage duration.                                              | Unit price: **\$0.005/GB/day**                         |
| Network Volume   | Pay-as-you-go      | Charges based on capacity and usage duration.                                              | Unit price: **\$0.002/GB/day**                         |

### Advantages of On-Demand Pricing for Different Scenarios

* **Short-Term Projects**: For projects with a limited duration, On-Demand Pricing allows you to align your compute costs with the project timeline.

* **Variable Workloads**: If your workloads fluctuate, On-Demand Pricing provides the flexibility to scale up or down as needed without incurring fixed costs.

* **Testing and Development**: For testing new applications or developing code, On-Demand Pricing offers a cost-effective way to access necessary compute resources without long-term financial commitments.


Built with [Mintlify](https://mintlify.com).