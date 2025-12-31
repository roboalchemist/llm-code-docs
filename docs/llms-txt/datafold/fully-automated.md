# Source: https://docs.datafold.com/deployment-testing/getting-started/universal/fully-automated.md

# Fully-Automated

> Automatically diff tables modified in a pull request with Datafold's Fully-Automated CI integration.

Our Fully-Automated CI integration enables you to automatically diff tables modified in a pull request so you know exactly how your data will change before going to production.

We do this by analyzing the SQL in any changed files, extracting the relevant table names, and diffing those tables between your staging and production environments. We then post the results of those diffs—including any downstream impact—to your pull request for all to see. All without manual intervention.

## Prerequisites

* Your code must be hosted in one of our supported version control integrations
* Your tables/views must be defined in SQL
* Your schema names must be parameterized ([see below](#4-parameterize-schema-names))
* You must be automatically generating staging data ([more info](/deployment-testing/how-it-works))

## Get Started

Get started in just a few easy steps.

### 1. Generate a Datafold API key

If you haven't already generated an API key (you only need one), visit Settings > Account and select **Create API Key**. Save the key somewhere safe like a password manager, as you won't be able to view it later.

### 2. Set up a version control integration

Open the Datafold app and navigate to Settings > Integrations > Repositories to connect the repository that contains the code you'd like to automatically diff.

### 3. Add a step to your CI workflow

<Note>This example assumes you're using GitHub actions, but the approach generalizes to any version control tool we support including GitLab, Bitbucket, etc.</Note>

Either [create a new GitHub Action](https://docs.github.com/en/actions/writing-workflows/quickstart) or add the following steps to an existing one:

```yaml  theme={null}
- name: Install datafold-sdk
  run: pip install -q datafold-sdk

- name: Trigger Datafold CI
  run: |
    datafold ci auto trigger --ci-config-id $CI_CONF_ID --pr-num $PR_NUM 
    --base-sha $BASE_SHA --pr-sha $PR_SHA --reference-params "$REFERENCE_PARAMS" 
    --pr-params "$PR_PARAMS"
  env:
    DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
    CI_CONF_ID: 436
    PR_NUM:  "${{ steps.findPr.outputs.pr }}"
    PR_SHA: "${{ github.event.pull_request.head.sha }}"
    BASE_SHA: ${{ github.event.pull_request.base.sha }}
    REFERENCE_PARAMS: '{ "target_schema": "nc_default" }'
    PR_PARAMS: "{ \"target_schema\": \"${{ env.TARGET_SCHEMA }}\" }"
```

### 4. Parameterize schema names

If it's not already the case, you'll need to parameterize the schema for any table paths you'd like Datafold to diff. For example, let's say you have a file called `dim_orgs.sql` that defines a table called `DIM_ORGS` in your warehouse. Your SQL should look something like this:

```sql  theme={null}
-- datafold: pk=org_id
CREATE OR REPLACE TABLE analytics.${target_schema}.dim_orgs AS (
  SELECT
    org_id,
    org_name,
    employee_count,
    created_at
  FROM analytics.${target_schema}.org_created
);
```

### 5. Provide primary keys (optional)

<Note>While this step is technically optional, we strongly recommend providing primary keys for any tables you'd like Datafold to diff.</Note>

In order for Datafold to perform full value-level comparisons between staging and production tables, Datafold needs to know the primary keys. To provide this information, place a comment above each query using the `-- datafold: pk=<your_pk>` syntax shown below:

```sql  theme={null}
-- datafold: pk=org_id
CREATE OR REPLACE TABLE analytics.${target_schema}.dim_orgs AS (
  SELECT
    org_id,
...
```

### 6. Create a pull request

When you create a pull request, Datafold will automatically detect it, attempt to diff any tables modified in the code, and post a summary as a comment in the PR. You can click through on the comment to view a more complete analysis of the changes in the Datafold app. Happy diffing!

## Need help?

If you have any questions about Fully-Automated CI, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
