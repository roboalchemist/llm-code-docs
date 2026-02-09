# Source: https://docs.datafold.com/deployment-testing/configuration/column-remapping.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Column Remapping

> Specify column renaming in your git commit message so Datafold can map renamed columns to their original counterparts in production for accurate comparison.

When your PR includes updates to column names, it's important to specify these updates in your git commit message using the following syntax. This allows Datafold to understand how renamed columns should be compared to the column in the production data with the original name.

## Example

By specifying column remapping in the commit message, instead of interpreting the change as a removing one column and adding another:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c492d769326e6c4c3a8882a3198332c8" data-og-width="2326" width="2326" data-og-height="602" height="602" data-path="images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=24e5cd73df50dc8ca97c3de3b0d4cdac 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=06f4da44a0f76e49812320b077d875c7 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=be2d7bd3cb7f9b1e8718568449b5f454 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9b2716806833b8d9967a3b4bf715b72b 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8edae7e8b4d940c119038abce698c45d 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_schema_difference_collapsed-f4fcb478c3a3e43b57f5b79b3f0bf15f.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=09cca214fdc5908a8d36c0e51df3dfd7 2500w" />
</Frame>

Datafold will recognize that the column has been renamed:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dac069059db9f6c994eac39bdfab09a6" data-og-width="2360" width="2360" data-og-height="884" height="884" data-path="images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4a51e513227eab1210b06b7fab9cc41f 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=bb90eca4fa0a7970ca1e3a953cfff443 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9c11cec9893cea6f21e0f2a2f56fc905 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=eb4351b13b52430ffb7aacab6e0ed05e 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0105a05b53050cad0cf531805a471769 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_no_schema_diff-d727e739b814160b72cde19f667ee7da.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5e30f215d3d1fe885b836247d5d2f228 2500w" />
</Frame>

## Syntax for column remapping

You can use any of the following syntax styles as a single line to a commit message to instruct Datafold in CI to remap a column from `oldcol` to `newcol`.

```Bash  theme={null}
# All models/tables in the PR:
datafold remap oldcol newcol
X-Datafold: rename oldcol newcol
/datafold renamed oldcol newcol
datafold: remapped oldcol newcol

# Filtered models/tables by shell-like glob:
datafold remap oldcol newcol model_NAME
X-Datafold: rename oldcol newcol TABLE
/datafold renamed oldcol newcol VIEW_*

```

## Chaining together column name updates

Commit messages can be chained together to reflect sequential changes. This means that a commit message does not lock you in to renaming a column.

For example, if your commit history looks like this:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2f980e14e0eee444c14eedb9b75f094c" data-og-width="1098" width="1098" data-og-height="254" height="254" data-path="images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=aebc576141e678c0ff75e3742df43e41 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=628675b62c028d16bfdf20c4be130b7b 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2ca1f2c9129c3fbd7c92011a02087cb4 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0689e2432d0ec94a4ae177b8b1cdc716 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=70e977b6cb99a56272f63f8221ccaec8 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/column_remapping_commit_messages-8ef04d36b80ee9f509fdb976d4dcb16e.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a2989342a14ba2047110a914b3a0234d 2500w" />
</Frame>

Datafold will understand that the production column `name` has been renamed to `first_name` in the PR branch.

## Handling column renaming in git commits and PR comments

### Git commits

Git commits track changes on a change-by-change basis and linearize history assuming merged branches introduce new changes on top of the base/current branch (1st parent).

### PR comments

PR comments apply changes to the entire changeset.

### When to use git commits or PR comments?

When handling chained renames:

* **Git commits:** Sequential renames (`col1 > col2 > col3`) result in the final rename (`col1 > col3`).
* **PR comments:** It's best to specify the final result directly (`col1 > col3`). Sequential renames (`col1 > col2 > col3`) can also work, but specifying the final state simplifies understanding during review.

| Aspect                    | Git Commits                                                                                                       | PR Comments                                                                                                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tracking Changes**      | Tracks changes on a change-by-change basis.                                                                       | Applies changes to the entire changeset.                                                                                                                                                    |
| **History Linearization** | Linearizes history assuming merged branches introduce new changes on top of the base/current branch (1st parent). | N/A                                                                                                                                                                                         |
| **Chained Renames**       | Sequential renames (col1 > col2 > col3) result in the final rename (col1 > col3).                                 | It's best to specify the final result directly (col1 > col3). Sequential renames (col1 > col2 > col3) can also work, but specifying the final state simplifies understanding during review. |
| **Precedence**            | Renames specified in git commits are applied in sequence unless overridden by subsequent commits.                 | PR comments take precedence over renames specified in git commits if applied during the review process.                                                                                     |

These guidelines ensure consistency and clarity when managing column renaming in collaborative development environments, leveraging Datafold's capabilities effectively.
