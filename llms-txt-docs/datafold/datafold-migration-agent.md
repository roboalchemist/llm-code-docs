# Source: https://docs.datafold.com/data-migration-automation/datafold-migration-agent.md

# Datafold Migration Agent

> Automatically migrate data environments of any scale and complexity with Datafold's Migration Agent.

Datafold provides a full-cycle migration automation solution for data teams, which includes code translation and cross-database reconciliation.

## How does DMA work?

Datafold performs complete SQL codebase translation and validation using an AI-powered architecture. This approach leverages a large language model (LLM) with a feedback loop optimized for achieving full parity between the migration source and target. DMA analyzes metadata, including schema, data types, and relationships, to ensure accuracy in translation.

<img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4472535367a2544e0fc7bce54d43b9e6" alt="datafold migration agent architecture" data-og-width="1561" width="1561" data-og-height="974" height="974" data-path="images/data-migration/datafold_migration_agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a4f2f90cfea623e5d276e4befb1375a2 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=33e9c4d42a7721007c3a036a27afb7a4 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6c11775d4c737d0dd5dc6ef2f4b9e1ab 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=603b1e80b7b5cfa35ed59651729e0b65 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f38f8488278f57d2b976e5c6e517356a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-migration/datafold_migration_agent.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=567ee1b4c54d471dd0dacaed97c15233 2500w" />

Datafold provides a comprehensive report at the end of the migration. This report includes links to data diffs validating parity and highlighting any discrepancies at the dataset, column, and row levels between the source and target databases.

## Why migrate with DMA?

Unlike traditional deterministic transpilers, DMA offers several distinct benefits:

* **Full parity between source and target:** DMA ensures not just code that compiles, but code that delivers the same results in your new database, complete with explicit validation.
* **Flexible dialect handling:** DMA can adapt to any arbitrary input/output dialect without requiring a full grammar definition, which is especially valuable for legacy systems.
* **Self-correction capabilities:** The AI-driven DMA can account for and correct mistakes based on both compilation errors and data discrepancies.
* **Modernizing code structure:** DMA can convert complex stored procedures into clean, modern formats such as dbt projects, following best practices.

## Getting started with DMA

<Note>
  **Want to learn more?**

  If you're interested in diving deeper, please take a moment to [fill out our intake form](https://nw1wdkq3rlx.typeform.com/to/VC2TbEbz) to connect with the Datafold team.
</Note>

1. Connect your source and target data sources to Datafold.
2. Provide Datafold access to your codebase, typically by installing the Datafold GitHub/GitLab/ADO app or via system catalog access for stored procedures.

Once you connect your source and target systems and Datafold ingests the codebase, DMA's translation process is supervised by the Datafold team. In most cases, no additional input is required from the customer.

The migration process timeline depends on the technologies, scale, and complexity of the migration. After setup, migrations typically take several days to several weeks.

## Security

Datafold is SOC 2 Type II, GDPR, and HIPAA-compliant. We offer flexible deployment options, including in-VPC setups in AWS, GCP, or Azure. The LLM infrastructure is local, ensuring no data is exposed to external subprocessors beyond the cloud provider. For VPC deployments, data stays entirely within the customer’s private network.

## FAQ

For more information, please see our extensive [FAQ section](../faq/data-migration-automation).
