# Source: https://docs.datafold.com/deployment-testing/getting-started/universal/api.md

# API

> Learn how to set up and configure Datafold's API for CI/CD testing.

## 1. Create a repository integration

Integrate your code repository using the appropriate [integration](/integrations/code-repositories).

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=45fd70946a2add757d79098af039b429" data-og-width="2084" width="2084" data-og-height="742" height="742" data-path="images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a69e88590a390b61e72569c53a496d24 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd0d01e133d73d97290b898e2f53623b 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3cc0312866dc746c1654834ce3d07382 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=2ada31061cc7d4abc5d4939d4e8d80c3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=cf99b0fd987b5dbc15bc46d84fc7d927 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b4ab64b5e13ef955ff4aab55f4d16879 2500w" />
</Frame>

## 2. Create an API integration

In the Datafold app, create an API integration.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7be3befc9aa261a2f155ee155143944f" data-og-width="2072" width="2072" data-og-height="1094" height="1094" data-path="images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5d13b05cc2d3dd048ad48377bb57949f 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e86d492621fd5f2659d3cb40a837dbd 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=50a25d67b9a037262eb9b655aff8fa47 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e1e685b014a75fc3fb1c2089c72618a 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=128ba338ad334a2fe0d45e75905ded8a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4a47c0ba9c62d731a7da05666aac7cd5 2500w" />
</Frame>

## 3. Set up the API integration

Complete the configuration by specifying the following fields:

### Basic settings

| Field Name         | Description                                               |
| ------------------ | --------------------------------------------------------- |
| Configuration name | Choose a name for your for your Datafold dbt integration. |
| Repository         | Select the repository you configured in step 1.           |
| Data Source        | Select the data source your repository writes to.         |

### Advanced settings: Configuration

| Field Name                     | Description                                                                                                                                                                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Diff Hightouch Models          | Run data diffs for Hightouch models affected by your PR.                                                                                                                                                                                                                   |
| CI fails on primary key issues | If null or duplicate primary keys exist, CI will fail.                                                                                                                                                                                                                     |
| Pull Request Label             | When this is selected, the Datafold CI process will only run when the 'datafold' label has been applied.                                                                                                                                                                   |
| CI Diff Threshold              | Data Diffs will only be run automatically for given CI Run if the number of diffs doesn't exceed this threshold.                                                                                                                                                           |
| Custom base branch             | If defined, the Datafold CI process will only run on pull requests with the specified base branch.                                                                                                                                                                         |
| Files to ignore                | Datafold CI diffs all changed models in the PR if at least one modified file doesn’t match the ignore pattern. Datafold CI doesn’t run in the PR if all modified files should be ignored. ([Additional details.](/deployment-testing/configuration/datafold-ci/on-demand)) |

### Advanced settings: Sampling

| Field Name          | Description                                                                                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enable sampling     | Enable sampling for data diffs to optimize analyzing large datasets.                                                                                                   |
| Sampling tolerance  | The tolerance to apply in sampling for all data diffs.                                                                                                                 |
| Sampling confidence | The confidence to apply when sampling.                                                                                                                                 |
| Sampling threshold  | Sampling will be disabled automatically if tables are smaller than specified threshold. If unspecified, default values will be used depending on the Data Source type. |

## 4. Obtain a Datafold API Key and CI config ID

Generate a new Datafold API Key and obtain the CI config ID from the CI API integration settings page:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e65dd3975cef3b16ad203a0e6dfc1e7c" data-og-width="2310" width="2310" data-og-height="972" height="972" data-path="images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2e0e7022637f64e95d0f4c01e6f09db1 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4fc016fc32528e5f1f08b4f9edc88cc7 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b570523c1b5d58809b253754f6fbe82f 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cc99d5527fc2951e3c3919f784b15955 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=23aaa8a8a35b8d3bfe814868517fca80 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/api_key_and_config_id-634de74aeb5f3904e366c412b4c61ba1.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8d376a542ad6683d9418572183ba8542 2500w" />
</Frame>

You will need these values later on when setting up the CI Jobs.

## 5. Install Datafold SDK into your Python environment

```Bash  theme={null}
pip install datafold-sdk
```

## 6. Configure your CI script(s) with the Datafold SDK

Using the Datafold SDK, configure your CI script(s) to use the Datafold SDK `ci submit` command. The example below should be adapted to match your specific use-case.

```Bash  theme={null}
datafold ci submit --ci-config-id <datafold_ci_config_id> --pr-num <pr_num> --diffs ./diffs.json
```

Since Datafold cannot infer which tables have changed, you'll need to manually provide this information in a specific `json` file format. Datafold can then determine which models to diff in a CI run based on the `diffs.json` you pass in to the Datafold SDK `ci submit` command.

```Bash  theme={null}
[
  {
    "prod": "MY.PROD.TABLE", // Production table to compare PR changes against
    "pr": "MY.PR.TABLE", // Changed table containing data modifications in the PR
    "pk": ["MY", "PK", "LIST"], // Primary key; can be an empty array
    // These fields are not required and can be omitted from the JSON file:
    "include_columns": ["COLUMNS", "TO", "INCLUDE"],
    "exclude_columns": ["COLUMNS", "TO", "EXCLUDE"]
  }
]
```

Note: The `JSON` file is optional and you can also achieve the same effect by using standard input (stdin) as shown here. However, for brevity, we'll use the `JSON` file approach in this example:

```Bash  theme={null}
datafold ci submit \
    --ci-config-id <datafold_ci_config_id> \
    --pr-num <pr_num> <<- EOF
[{
        "prod": "MY.PROD.TABLE",
        "pr": "MY.PR.TABLE",
        "pk": ["MY", "PK", "LIST"]
}]
```

Implementation details will vary depending on [which CI tool](#ci-implementation-tools) you use. Please review the following instructions and examples for your organization's CI tool.

<Info>
  **NOTE**

  Populating the `diffs.json` file is specific to your use case and therefore out of scope for this guide. The only requirement is to adhere to the `JSON` schema structure explained above.
</Info>

## CI Implementation Tools

We've created guides and templates for three popular CI tools.

<Tip>
  **HAVING TROUBLE SETTING UP DATAFOLD IN CI?**

  <Icon icon="hand-wave" /> We're here to help! Please [reach out and chat with a Datafold Solutions Engineer](https://www.datafold.com/booktime). <Icon icon="phone-rotary" />
</Tip>

To add Datafold to your CI tool, add `datafold ci submit` step in your PR CI job.

<Tabs>
  <Tab title="GitHub Actions">
    ```Bash  theme={null}
    name: Datafold PR Job

    # Run this job when a commit is pushed to any branch except main
    on:
      pull_request:
      push:
        branches:
          - '!main'

    jobs:
      run:
        runs-on: ubuntu-20.04 # your image will vary

        steps:

          - name: Install Datafold SDK
            run: pip install -q datafold-sdk
        # ...
          - name: Upload what to diff to Datafold
            run: datafold ci submit --ci-config-id <datafold_ci_config_id> --pr-num ${PR_NUM} --diffs <path_to_diffs_json_file>
            env:
              # env variables used by Datafold SDK internally
              DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
              DATAFOLD_HOST: ${DATAFOLD_HOST}
              # For Dedicated Cloud/private deployments of Datafold,
              # Set the "https://custom.url.datafold.com" variable as the base URL as an environment variable, either as a string or a project variable
              # There are multiple ways to get the PR_NUM, this is just a simple example
              PR_NUM: ${{ github.event.number }}
    ```

    Be sure to replace `<datafold_ci_config_id>` with the [CI config ID](#4-obtain-a-datafold-api-key-and-ci-config-id) value.

    <Info>
      **NOTE**

      It is beyond the scope of this guide to provide guidance on generating the `<path_to_diffs_json_file>`, as it heavily depends on your specific use case. However, ensure that the generated file adheres to the required schema outlined above.
    </Info>

    Finally, store [your Datafold API Key](#4-obtain-a-datafold-api-key-and-ci-config-id) as a secret named `DATAFOLD_API_KEY` [in your GitHub repository settings](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

    Once you've completed these steps, Datafold will run data diffs between production and development data on the next GitHub Actions CI run.
  </Tab>

  <Tab title="CircleCI">
    ```Bash  theme={null}
    version: 2.1

    jobs:
      artifacts-job:
        filters:
          branches:
            only: main # or master, or the name of your default branch
        docker:
          - image: cimg/python:3.9 # your image will vary
              env:
                # env variables used by Datafold SDK internally
                DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
                DATAFOLD_HOST: ${DATAFOLD_HOST}
                # For Dedicated Cloud/private deployments of Datafold,
                # Set the "https://custom.url.datafold.com" variable as the base URL as an environment variable, either as a string or a project variable, per https://circleci.com/docs/set-environment-variable/
                # There are multiple ways to get the PR_NUM, this is just a simple example
                PR_NUM: ${{ github.event.number }}
        steps:
          - checkout
          - run:
              name: "Install Datafold SDK"
              command: pip install -q datafold-sdk

          - run:
              name: "Upload what to diff to Datafold"
              command: datafold ci submit --ci-config-id <datafold_ci_config_id> --pr-num ${CIRCLE_PULL_REQUEST} --diffs <path_to_diffs_json_file>
    ```

    Be sure to replace `<datafold_ci_config_id>` with the [CI config ID](#4-obtain-a-datafold-api-key-and-ci-config-id) value.

    <Info>
      **NOTE**

      It is beyond the scope of this guide to provide guidance on generating the `<path_to_diffs_json_file>`, as it heavily depends on your specific use case. However, ensure that the generated file adheres to the required schema outlined above.
    </Info>

    Then, enable [**Only build pull requests**](https://circleci.com/docs/oss#only-build-pull-requests) in CircleCI. This ensures that CI runs on pull requests and production, but not on pushes to other branches.

    Finally, store [your Datafold API Key](#4-obtain-a-datafold-api-key-and-ci-config-id) as a secret named `DATAFOLD_API_KEY` [your CircleCI project settings.](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

    Once you've completed these steps, Datafold will run data diffs between production and development data on the next CircleCI run.
  </Tab>

  <Tab title="GitLab CI">
    ```Bash  theme={null}

    image:
    name: ghcr.io/dbt-labs/dbt-core:1.x # your name will vary
    entrypoint: [ "" ]
    variables:
      # env variables used by Datafold SDK internally
      DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }}
      DATAFOLD_HOST: ${DATAFOLD_HOST}
      # For Dedicated Cloud/private deployments of Datafold,
      # Set the "https://custom.url.datafold.com" variable as the base URL as an environment variable, either as a string or a project variable
      # There are multiple ways to get the PR_NUM, this is just a simple example
      PR_NUM: ${{ github.event.number }}

    run_pipeline:
      stage: test
      before_script:
        - pip install -q datafold-sdk

      script:
        # Upload what to diff to Datafold
        - datafold ci submit --ci-config-id <datafold_ci_config_id> --pr-num $CI_MERGE_REQUEST_ID --diffs <path_to_diffs_json_file>
     rules:
        - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    ```

    Be sure to replace `<datafold_ci_config_id>` with the [CI config ID](#4-obtain-a-datafold-api-key-and-ci-config-id) value.

    <Info>
      **NOTE**

      It is beyond the scope of this guide to provide guidance on generating the `<path_to_diffs_json_file>`, as it heavily depends on your specific use case. However, ensure that the generated file adheres to the required schema outlined above.
    </Info>

    Finally, store [your Datafold API Key](#4-obtain-a-datafold-api-key-and-ci-config-id) as a secret named `DATAFOLD_API_KEY` [in your GitLab project's settings](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

    Once you've completed these steps, Datafold will run data diffs between production and development data on the next GitLab CI run.
  </Tab>
</Tabs>

## Optional CI Configurations and Strategies

### Skip Datafold in CI

To skip the Datafold step in CI, include the string `datafold-skip-ci` in the last commit message.
