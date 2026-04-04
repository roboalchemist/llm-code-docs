# Source: https://docs.datafold.com/deployment-testing/configuration/datafold-ci/on-demand.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running Data Diff for Specific PRs/MRs

> By default, Datafold CI runs on every new pull/merge request and commits to existing ones.

To **only** run Datafold CI when the user explicitly requests it, you can set **Run only when tagged** option in the Datafold app [CI settings](https://app.datafold.com/settings/integrations/ci) which will only allow Datafold CI to run if a `datafold` tag/label is assigned to the pull/merge request.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a1872bbe27be3779fa79908ecff53ba1" data-og-width="1980" width="1980" data-og-height="1030" height="1030" data-path="images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c04d7824efb2d2943058fabfd4bd3740 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=667677d57e58e9acae205bf7fdf1cc1d 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=59f3ccbc8e78e3b696090910cce116af 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9368ce4d5832ca5f77f1b38cfad40328 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a8819937fa20899398b770f344d1c92f 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/datafold_label_in_pr-81dfcfe40ff4c9c43bb14fde407894d5.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a978e793c77796292c89145d197df739 2500w" />
</Frame>

## Running data diff on specific file changes

By default, Datafold CI will run on any file change in the repo. To skip Datafold CI runs for certain modified files (e.g., if the dbt code is placed in the same repo with non-dbt code), you can specify files to ignore. The pattern uses the syntax of .gitignore. Excluded files can be re-included by using the negation.

### Example

Let's say the dbt project is a folder in a repo that contains other code (e.g., Airflow). We want to run Datafold CI for changes to dbt models but skip it for other files. For that, we exclude all files in the repo except those the /dbt folder. We also want to filter out `.md` files in the /dbt folder:

```Bash  theme={null}
*!dbt/*dbt/*.md
```

<Tip>
  **SKIPPING SPECIFIC DBT MODELS**

  To skip diffing individual dbt models in CI, use the [never\_diff](/deployment-testing/configuration/model-specific-ci/excluding-models) option in the Datafold dbt yaml config.
</Tip>
