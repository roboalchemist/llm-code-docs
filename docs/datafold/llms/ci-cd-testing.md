# Source: https://docs.datafold.com/faq/ci-cd-testing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CI/CD Testing

<AccordionGroup>
  <Accordion title="What if my staging/dev environment contains only a subset of data from production?">
    You can use [SQL filters](/deployment-testing/configuration/model-specific-ci/sql-filters) to ensure that Datafold compares equivalent subsets of data between your staging/dev and production environments, allowing for accurate data quality checks despite the difference in data volume.
  </Accordion>

  <Accordion title="Can I use Datafold in development?">
    Yes, you can use Datafold in development. It helps catch data quality issues early by comparing data changes in your development environment before they reach production. This proactive approach ensures that errors and inconsistencies are identified and resolved during the development process, enhancing overall data reliability and preventing potential issues in production. Data teams can leverage the Datafold SDK to run data diffs from the command line while developing and testing data models.
  </Accordion>

  <Accordion title="How does Datafold handle data drift?">
    Data drift in CI occurs when the two data transformation builds that are compared by Datafold in CI have differing data outputs due to the upstream data changing over time.

    We have a few recommended strategies for dealing with data drift [in our docs here](/deployment-testing/best-practices/handling-data-drift).
  </Accordion>

  <Accordion title="Can I run Data Diffs before opening a PR?">
    Some teams want to show Data Diff results in their tickets *before* creating a pull request. This speeds up code reviews as developers can QA code changes before requesting a PR review.

    If you use dbt, we explain [how you can automate this workflow here](/faq/datafold-with-dbt#can-i-run-data-diffs-before-opening-a-pr).
  </Accordion>
</AccordionGroup>
