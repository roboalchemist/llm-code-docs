# Source: https://docs.datafold.com/integrations/orchestrators/custom-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Integrations

> Integrate Datafold with your custom orchestration using the Datafold SDK and REST API.

<Info>
  To use the Datafold REST API, you should first create a Datafold API key in Settings > Account.
</Info>

## Install

Then, create your virtual environment for Python:

```
> python3 -m venv venv
> source venv/bin/activate
> pip install --upgrade pip setuptools wheel
```

Now, you're ready to install the Datafold SDK:

```
> pip install datafold-sdk
```

## Configure

Navigate in the Datafold UI to Settings > Integrations > CI. After selecting `datafold-sdk` from the available options, complete configuration with the following information:

| Field Name                               | Description                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Repository                               | Select the repository that generates the webhooks and where pull / merge requests will be raised.                                                                                                                                                                  |
| Data Connection                          | Select the data connection where the code that is changed in the repository will run.                                                                                                                                                                              |
| Name                                     | An identifier used in Datafold to identify this CI configuration.                                                                                                                                                                                                  |
| Files to ignore                          | If defined, the files matching the pattern will be ignored in the PRs. The pattern uses the syntax of .gitignore. Excluded files can be re-included by using the negation; re-included files can be later re-excluded again to narrow down the filter.             |
| Mark the CI check as failed on errors    | If the checkbox is disabled, the errors in the CI runs will be reported back to GitHub/GitLab as successes, to keep the check "green" and not block the PR/MR. By default (enabled), the errors are reported as failures and may prevent PR/MRs from being merged. |
| Require the `datafold` label to start CI | When this is selected, the Datafold CI process will only run when the 'datafold' label has been applied. This label needs to be created manually in GitHub or GitLab and the title or name must match 'datafold' exactly.                                          |
| Sampling tolerance                       | The tolerance to apply in sampling for all data diffs.                                                                                                                                                                                                             |
| Sampling confidence                      | The confidence to apply when sampling.                                                                                                                                                                                                                             |
| Sampling Threshold                       | Sampling will be disabled automatically if tables are smaller than specified threshold. If unspecified, default values will be used depending on the Data Connection type.                                                                                         |

## Add commands to your custom orchestration

```bash  theme={null}
export DATAFOLD_API_KEY=XXXXXXXXX

# only needed if your Datafold app url is not app.datafold.com
export DATAFOLD_HOST=<CUSTOM_DATAFOLD_APP_DOMAIN>
```

To submit diffs for a CI run, replace `ci_config_id`, `pr_num`, and `diffs_file` with the appropriate values for your CI configuration ID, pull request number, and the path to your diffs `JSON` file.

#### CLI

```bash  theme={null}
datafold ci submit \
  --ci-config-id <ci_config_id> \
  --pr-num <pr_num> \
  --diffs <diffs_file> \
```

#### Python

```python  theme={null}
import os

from datafold_sdk.sdk.ci import run_diff

api_key = os.environ.get('DATAFOLD_API_KEY')

# Only needed if your Datafold app URL is not app.datafold.com
host = os.environ.get("DATAFOLD_HOST")

run_diff(host=host,
         api_key=api_key,
         ci_config_id=<ci_config_id>,
         pr_num=<pr_num>,
         diffs='<diffs_file>')
```

##### Example JSON format for diffs file

The `JSON` file should define the production and pull request tables to compare, along with any primary keys and columns to include or exclude in the comparison.

```json  theme={null}
[
  {
    "prod": "YOUR_PROJECT.PRODUCTION_TABLE_A",
    "pr": "YOUR_PROJECT.PR_TABLE_NUM",
    "pk": ["ID"],
    "include_columns": ["Column1", "Column2"],
    "exclude_columns": ["Column3"]
  },
  {
    "prod": "YOUR_PROJECT.PRODUCTION_TABLE_B",
    "pr": "YOUR_PROJECT.PR_TABLE_NUM",
    "pk": ["ID"],
    "include_columns": ["Column1"],
    "exclude_columns": []
  }
]
```
