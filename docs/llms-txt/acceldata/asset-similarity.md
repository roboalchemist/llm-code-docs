# Source: https://docs.acceldata.io/documentation/asset-similarity.md

# Find Similar Assets

Asset Similarity helps you discover tables across your data landscape that share similar structures and characteristics. When you open an asset and navigate to its details page, you can access the Asset Similarity tab to view assets that are similar to the one you are currently viewing.

## Overview

Asset Similarity automatically analyzes your assets and identifies similar ones, enabling you to:

- Discover related tables across environments 
- Reuse existing Data Quality and Reconciliation rules instead of recreating them
- Identify overlaps or duplicates in your catalog
- Validate that source and destination systems remain synchronized over time

## Benefits

**Faster monitoring setup**
 Reuse rules from one asset on another similar asset, instead of configuring everything from scratch.

**Safer migrations**
 Confirm that migrated tables in a new environment closely match their original source.

**Better visibility**
 See which tables in your environment are related to a given asset.

**Stronger governance**
 Apply consistent checks and policies to groups of similar assets, such as customer-related tables.

## How it works

ADOC determines asset similarity through the following process:

1. **Profiles your assets**: When profiling is enabled, ADOC computes statistics and summaries for each column in a table, including distinct counts, distributions, and uniqueness.
2. **Compares assets**: ADOC uses a combination of schema details (names, types, structure) and data profile metrics (distributions, uniqueness) to estimate similarity between columns and tables.
3. **Assigns similarity scores**: ADOC calculates column similarity scores and overall table similarity scores based on the combined similarity of matching columns.
4. **Surfaces relevant matches**: Only assets with sufficiently high similarity scores appear in the Asset Similarity view.

You do not need to configure algorithms or parameters. Your main responsibility is to ensure profiling is configured for the assets you want to compare.

## Prerequisites

Before using Asset Similarity, ensure the following:

- **Assets are discovered**: The tables you want to compare must be registered and visible in ADOC under **Discover Assets**.
- **Profiling is enabled**: Run profile jobs for your key assets. Similarity is most effective when sufficient profile data exists for each column.
- **Both assets contain data**: For ADOC to find a match, both the reference asset and candidate assets should have at least basic profiling completed and contain a reasonable amount of data. Empty or extremely small tables provide weaker signals.
- **For reconciliation use cases**: Ensure profiling can infer uniqueness or key-like behavior for important columns. This helps ADOC suggest or support rules that rely on unique keys.

## Accessing Asset Similarity

To access Asset Similarity:

1. Navigate to **Discover Assets**.
2. Search for and select the table you want to analyze.
3. On the **Asset Details** page, click the **Asset Similarity** tab.

ADOC displays a list of assets that are similar to the current asset, including:

- Asset name
- Data source, database, and schema
- Similarity indicator (score or rank)
- Brief information about matching columns or attributes (optional)

## Using Asset Similarity

### Viewing similar assets

To view assets similar to your current asset:

1. Open the asset in **Asset Detail**s page.
2. Click the **Asset Similarity** tab to see the list of similar assets.
3. Review the similarity scores and matching information for each result.

### Analyzing a similar asset

To examine a similar asset in detail:

1. Click on the similar asset from the list.
2. Review its Asset 360° view, including profile, lineage, policies, and reliability metrics.
3. Compare it to your reference asset to understand similarities and differences.

### Reusing Data Quality rules

To reuse Data Quality rules based on Asset Similarity:

1. Identify assets with well-configured Data Quality rules.
2. Use Asset Similarity to find other tables that behave similarly.
3. Adapt or copy existing rules to the similar assets.

**Example**: A rule enforcing valid email format on `customer_email` can be copied to a similar column in another customer table.

### Setting up Reconciliation policies

To configure Reconciliation policies using Asset Similarity:

1. Use Asset Similarity to identify pairs of tables that represent the same logical entity in different systems.
2. Verify that the tables share similar key columns and distributions.
3. Configure Reconciliation policies to compare row counts, aggregated measures, and key-based equality between source and target.

Asset Similarity helps you confidently select the right asset pairs and columns for reconciliation policies, but does not automatically create these policies.

## Use cases

### Cloud migration validation

**Scenario**: You migrate tables from an on-premises warehouse to a cloud data platform and need to ensure the migrated tables match their originals.

**Solution**:

1. Open the source table in Asset 360°.
2. Use Asset Similarity to find the corresponding cloud table.
3. Confirm high similarity between the tables.
4. Reuse Data Quality rules and set up reconciliation policies between the two tables.

### Harmonizing Data Quality across domains

**Scenario**: Multiple teams maintain customer-like tables in different systems, each with their own rules, but you want a consistent baseline.

**Solution**:

1. Start with your most trusted customer table.
2. Use Asset Similarity to find other similar customer tables.
3. Apply a standard set of Data Quality checks (for example, mandatory fields, key uniqueness, value ranges) across similar assets.

### Identifying potential duplicates

**Scenario**: Your catalog contains hundreds or thousands of tables, and you suspect duplication or overlapping datasets.

**Solution**:

1. Select a representative asset (for example, a fact table or critical dimension).
2. Use Asset Similarity to identify other highly similar tables.
3. Use this insight to consolidate redundant datasets, align ownership, and avoid conflicting definitions.

## Troubleshooting

### No similar assets appear for a table

If you do not see any similar assets for a table, check the following:

**Profiling status**

- Verify that profiling has run for the asset you are viewing.
- Verify that other relevant assets have also been profiled.

**Scope**

- Ensure you are looking in the correct domain or environment.
- If your catalog is small or newly onboarded, there may be no strong matches yet.

**True dissimilarity**

- Tables that appear similar by name may actually differ significantly in structure or data.
- In such cases, Asset Similarity correctly does not surface them as similar.

### Similarity results are outdated

Similarity is based on profiled data. If the underlying data changes significantly but profiles are not refreshed, similarity may not reflect recent changes.

**Solution**:

- Configure regular profile schedules for your key assets.
- Re-run profiles after major schema or data changes (for example, large migrations or model refactors).

### Asset Similarity tab is not visible

If you do not see the Asset Similarity section:

1. Verify with your ADOC administrator that:
    - You have the required user role and permissions.
    - Asset Similarity is enabled for your deployment.

2. If needed, contact Acceldata Support with:
    - Your tenant URL
    - Affected assets
    - A brief description of the expected behavior

## Best practices

Follow these best practices when using Asset Similarity:

- **Profile your most important domains first** – Start with critical tables (for example, finance, customer, regulatory data) so similarity is most useful where it matters most.
- **Standardize naming and metadata** – Consistent naming conventions and metatags make it easier to interpret similarity results and apply policies.
- **Use similarity as a guide** – Always validate key matches before applying strict reconciliation or compliance rules.
- **Combine with other ADOC features** – Use Asset Similarity together with lineage, reliability scores, and existing policies to make informed decisions.
- **Maintain up-to-date profiles** – Schedule regular profiling jobs to ensure similarity results reflect your current data landscape.