# Source: https://grafbase.com/docs/platform/schema-checks/breaking-change-approvals.md

# Breaking change approvals

By default, [Operation Checks](https://grafbase.com/docs/platform/schema-checks.md) prevent breaking changes based on usage. You define thresholds and exclusion rules, and any breaking change that affects a part of the schema that is considered as used will trigger an operation check error.

However, in some scenarios, the analytics data to detect usage will not be available, for example in multi-tenant setups. The breaking change approvals feature is designed for these use cases.

It consists of two settings inside the operation checks section of Graph settings:

- "Ignore usage data for operation checks" makes operation checks consider all schema changes that are theoretically breaking as breaking, without relying on usage data.
- "Allow breaking changes that are part of an approved schema proposal" makes operation checks filter out the breaking changes that are part of an approved schema proposal.

Here is what the settings look like:

![UI screenshot for the two settings](/images/docs/schema-checks/breaking-change-approvals-configuration.png)

With these settings enabled, the workflow becomes the following:

- Create a schema proposal for the changes you want to make. Here, only the breaking changes will be relevant.
- Get that schema proposal reviewed and approved.
- That's it. Next time you run schema checks, any breaking change that is part of an approved schema proposal will be ignored.