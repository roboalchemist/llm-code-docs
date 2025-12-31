# Source: https://docs.datafold.com/faq/datafold-with-dbt.md

# Integrating Datafold with dbt

<AccordionGroup>
  <Accordion title="Why do I need Datafold if I already have dbt tests?">
    You need Datafold in addition to dbt tests because while dbt tests are effective for validating specific assertions about your data, they can't catch all issues, particularly unknown unknowns. Datafold identifies value-level differences between staging and production datasets, which dbt tests might miss.

    Unlike dbt tests, which require manual configuration and maintenance, Datafold automates this process, ensuring continuous and comprehensive data quality validation without additional overhead. This is all embedded within Datafold’s unified platform that offers end-to-end data quality testing with our [Column-level Lineage](/data-explorer/lineage) and [Data Monitors](/data-monitoring/monitor-types).

    Hence, we recommend combining dbt tests with Datafold to achieve complete test coverage that addresses both known and unknown data quality issues, providing a robust safeguard against potential data integrity problems in your CI pipeline.
  </Accordion>

  <Accordion title="What do I need to implement Datafold for dbt?">
    For dbt Core users, create an integration in Datafold, specify the necessary settings, obtain a Datafold API Key and CI config ID, and configure your CI scripts with the Datafold SDK to upload manifest.json files. Our detailed setup guide [can be found here](/integrations/orchestrators/dbt-core).

    For dbt Cloud users, set up dbt Cloud CI to run Pull Request jobs and create an Artifacts Job that generates production manifest.json on merges to main/master. Obtain your dbt Cloud access URL and a Service Token, then create a dbt Cloud integration in Datafold using these credentials. Configure the integration with your repository, data connection, primary key tag, and relevant jobs. Our detailed setup guide [can be found here](/integrations/orchestrators/dbt-cloud).
  </Accordion>

  <Accordion title="We currently have a dbt Cloud Slim CI job. Does Datafold work with the custom PR schema that dbt Cloud creates?">
    Yes, Datafold is fully compatible with the custom PR schema created by dbt Cloud for Slim CI jobs.
  </Accordion>

  <Accordion title="How can I optimize diff performance in dbt?">
    We outline effective strategies for efficient and scalable data diffing in our[performance and scalability guide](faq/performance-and-scalability#how-can-i-optimize-diff-performance-at-scale).

    For dbt-specific diff performance, you can exclude certain columns or tables from data diffs in your CI/CD pipeline by adjusting the **Advanced settings** in your Datafold CI/CD configuration. This helps reduce processing load by focusing diffs on only the most relevant columns.

        <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1a22a2d006506c4181030d7a6417daf4" alt="" data-og-width="2090" width="2090" data-og-height="1772" height="1772" data-path="images/faq/advanced_ci_columns_to_ignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=08c8c210035ff613a62d8453b70a3964 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d0766e0559b5093c0204882b7cd2896d 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6b1fe94bfdfa7eb27d6c26aac1f9bda1 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9b22e9e57064d8fba203c166040f83da 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=96cfef3957167e0b7d52269211c6c2a7 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/advanced_ci_columns_to_ignore.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4c4c4b4bcc81d2854b11bdaa31c4bb68 2500w" />
  </Accordion>

  <Accordion title="Can I run Data Diffs before opening a PR?">
    Some teams want to show Data Diff results in their tickets *before* creating a pull request. This speeds up code reviews as developers can QA code changes before requesting a PR review.

    You can trigger a Data Diff by first creating a **draft PR** and then running the following command via the CLI:

    ```bash  theme={null}
    dbt run && datafold diff dbt
    ```

    This command runs `dbt` locally and then triggers a Data Diff, allowing you to preview data changes without pushing to Git.

    To automate this process of kicking off a Data Diff before pushing code to git, we recommend creating a GitHub Actions job for draft PRs. For example:

    ```
    name: Data Diff on draft dbt PR

    on:
      pull_request:
        types: [opened, reopened, synchronize]
        branches:
          - '!main'

    jobs:
      run:
        if: github.event.pull_request.draft == true  # Run only on draft PRs
        runs-on: ubuntu-latest

        steps:
          - name: Checkout Code
            uses: actions/checkout@v2

          - name: Set Up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.8'

          - name: Install requirements
            run: pip install -r requirements.txt  

          - name: Install dbt dependencies
            run: dbt deps

          # Update with your S3 bucket details
          - name: Grab production manifest from S3
            run: |
              aws s3 cp s3://advanced-ci-manifest-demo/manifest.json ./manifest.json
            env:
              AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
              AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
              AWS_REGION: us-east-1

          - name: Run dbt and Data Diff
            env:
              DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
            run: |
              dbt run
              datafold diff dbt
              
          # Optional: Submit artifacts to Datafold for more analysis or logging
          - name: Submit artifacts to Datafold
            run: |
              set -ex
              datafold dbt upload --ci-config-id 350 --run-type pull_request --commit-sha ${GIT_SHA}
            env:
              DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
              GIT_SHA: "${{ github.event.pull_request.head.sha }}"

    ```
  </Accordion>
</AccordionGroup>
