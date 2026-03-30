# Source: https://docs.anyscale.com/ci-cd/github-actions.md

# GitHub Actions

[View Markdown](/ci-cd/github-actions.md)

# GitHub Actions

tip

View the comprehensive [MadeWithML](https://madewithml.com/courses/mlops/cicd/) example for a complete tutorial of CI/CD with Anyscale jobs and services.

GitHub Actions allow you to define CI/CD workflows triggered by specific events like pull requests or pushes. Define these workflows in the `.github/workflows` directory in your repository.

Follow these steps to trigger an Anyscale workload:

1. Create a workflow file in your repository at `.github/workflows/NAME.yaml`.

2. Set up the [Anyscale authentication](/get-started.md#setup-env) and your cloud service provider credentials so the processes can access the right resources and store results.

3. Set up dependencies to use during execution.

4. Use Anyscale CLI commands in the steps of your workflow to submit jobs or deploy services:

   <!-- -->

   ```
   anyscale job submit -f deploy/jobs/workloads.yaml --wait
   ```

   ```
   anyscale service deploy --service-config-file deploy/services/serve_model.yaml
   ```

### Submit an Anyscale job[​](#submit-job "Direct link to Submit an Anyscale job")

The following is a snippet from a sample workflow demonstrating how to submit an Anyscale job. See the complete `workloads.yaml` [on GitHub](https://github.com/GokuMohandas/Made-With-ML/blob/main/.github/workflows/workloads.yaml).

```
# Run workloads
- name: Workloads
  run: |
    export ANYSCALE_CLI_TOKEN=${{ secrets.ANYSCALE_CLI_TOKEN }}
    anyscale job submit -f deploy/jobs/workloads.yaml --wait
```

### Deploy an Anyscale service[​](#deploy-service "Direct link to Deploy an Anyscale service")

The following is a snippet from a sample workflow demonstrating how to roll out an Anyscale service. See the complete `serve.yaml` [on GitHub](https://github.com/GokuMohandas/Made-With-ML/blob/main/.github/workflows/serve.yaml).

```
# Serve model
- name: Serve model
  run: |
    export ANYSCALE_CLI_TOKEN=${{ secrets.ANYSCALE_CLI_TOKEN }}
    anyscale service deploy --service-config-file deploy/services/serve_model.yaml
```
