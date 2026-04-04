# Source: https://typescript-eslint.io/maintenance/issues/rule-deprecations-and-deletions

On this page# Rule Deprecations, Renames, And DeletionsSometimes a rule that used to be 👍 does not age well and becomes 👎.
In the past, these cases have included:
- Overly opinionated and/or stylistic rules that don&#x27;t represent a universal best practice
- Renames
- Rules moved to an external plugin
In these cases, we aim to remove the old rule with minimal user disruption.
## Filing the Issue[​](#filing-the-issue)
Rule deprecations and renames can be filed as a [new issue bypassing templates](https://github.com/typescript-eslint/typescript-eslint/issues/new).
Provide it an `## Overview` containing:
- The rule name & link to its documentation page
- A clear explanation of why you believe it should be deprecated and/or renamed
- Whether it exists in popular configs such as `eslint-config-airbnb-typescript` and `eslint-config-standard-with-typescript`
- Sourcegraph queries showing how often it appears in user configs
See [#6036](https://github.com/typescript-eslint/typescript-eslint/issues/6036) for examples of those links and queries.
## Timeline[​](#timeline)
- In any minor/patch version, add [rule `meta` properties](https://eslint.org/docs/latest/developer-guide/working-with-rules#rule-basics):
`deprecated: true`
- `replacedBy`, if applicable
- Search through open issues and PRs, and update the name in them accordingly:
Deletions: close them with a link to the issue and deprecation PR
- Renames: update their title and explicitly mention in a comment that the rule has been renamed
- In the next major version, you may delete the deprecated rule
Leave a documentation page as a tombstone pointing to the new relevant rule or docs (see [`camelcase`](/rules/camelcase) as an example)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/maintenance/issues/Rule_Deprecations_And_Deletions.mdx)- [Filing the Issue](#filing-the-issue)- [Timeline](#timeline)