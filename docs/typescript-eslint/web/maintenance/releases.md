# Source: https://typescript-eslint.io/maintenance/releases

On this page# Releases[Users > Releases](/users/releases) describes how our automatic releases are done.
There is generally no maintenance activity we need to take for the weekly releases.
However, there are two kinds of releases we infrequently go through that each require manual effort.
## Major Releases[​](#major-releases)
Per [Users > Releases > Major Releases](/users/releases#major-releases), we infrequently release major versions with accumulated breaking changes.
### 1. Pre-Release Preparation[​](#1-pre-release-preparation)
- Create a milestone by the name of the release [example: [Milestone 6.0.0](https://github.com/typescript-eslint/typescript-eslint/milestone/8)].
- If an issue for changes to recommended rule configs doesn&#x27;t yet exist, create one [example: [Changes to the `recommended` sets for 5.0.0](https://github.com/typescript-eslint/typescript-eslint/issues/5900)].
- Add any breaking changes intended for the release to that milestone.
- Search for source code comments (excluding `CHANGELOG.md` files) that mention deprecated code and/or a todo for the new major version, and create corresponding issues in that milestone.
For example, for a new major version 8, searches might include:
`/deprecated|todo/i`
- `/v8/i`
- `/todo.*v?8/i`
- Create an issue to raise the minimum versions of dependencies [example: [Enhancement: Raise minimum versions of dependencies for v8](https://github.com/typescript-eslint/typescript-eslint/issues/8929)]
- Create two new branches off `main` in the project repository (not a personal fork):
`v${major}`
- `v${major}-canary-auto-release`
- Raise a PR from `v${major}-canary-auto-release` to `main` modifying [`ci.yml` workflow](https://github.com/typescript-eslint/typescript-eslint/blob/main/.github/workflows/ci.yml) and README.md [example: [chore: add auto-canary release for v6](https://github.com/typescript-eslint/typescript-eslint/pull/5883)]:
`ci.yml`:
Under `push:` > `branches:` at the beginning of the file, add a `- v${major}` list item.
- Add a `publish_canary_version_v${major}` step the same as `publish_canary_version` except:
Change the `if` condition&#x27;s branch check to: `if: github.ref == &#x27;refs/heads/v${major}&#x27;`.
- Its publish command should be `npx nx release publish --tag rc-v${major} --verbose`.
- `README.md`:
Add a link to a `v${major}--typescript-eslint.netlify.app` preview deploy environment on Netlify that you create for the branch.
- `docusaurus.config.mts`: updating the `supportedMajorVersion` variable
- Merge this into `main` once reviewed and rebase the `v${major}` branch.
- Configure the [https://github.com/ldez/gha-mjolnir](https://github.com/ldez/gha-mjolnir) action to auto-close issues when PRs are merged to the `v${major}` branch (GitHub doesn&#x27;t by default): see [`close-v8-issues.yml`](https://github.com/auvred/typescript-eslint/blob/b77e94dbd8ac7fd59c92527e13d241d6b26908b1/.github/workflows/close-v8-issues.yml) for reference
#### 1a. Shared Config Changes[​](#1a-shared-config-changes)
Major versions are our only real chance to change the values in our stable `recommended*` and `stylistic*` configs.
In parallel to the general PR flow of the major version:
- Create a `v${major}` channel on the typescript-eslint Discord
- Create a discussion with a table summarizing any proposed rule changes [example: [Changes to configurations for 6.0.0](https://github.com/typescript-eslint/typescript-eslint/discussions/6014)]
- Post that discussion on the typescript-eslint Discord and on social media
- Once the greater of (1 month) and (discussion settling down) has passed, file an issue and send a corresponding PR to the `v${major}` branch making the corresponding changes [example: [Configs: Apply changes to config presets for v6](https://github.com/typescript-eslint/typescript-eslint/issues/6759)]
#### 1b. Voluntary Community Testing[​](#1b-voluntary-community-testing)
In parallel to the shared config changes work, make sure to test out the beta version on popular community projects willing to try it out.
- Create a pinned issue offering to try out the new version&#x27;s beta for end users (example: [Try out v8 beta on various influential community repos](https://github.com/typescript-eslint/typescript-eslint/issues/9141))
Ask each community repo if they&#x27;d be interested in trying out the new version, such as in their Discord or on their issue tracker.
- Each community project that&#x27;s indicated willingness to receive a PR should have one.
- Create a pinned issue offering to try the new version&#x27;s beta for downstream plugins (example: [Try out v8 beta on various influential plugins](https://github.com/typescript-eslint/typescript-eslint/issues/9501))
These PRs can be sent without asking, as a friendly courtesy.
- Once the proposed *Shared Config Changes* are merged into the `v${major}` branch, send a draft PR to each project with the new beta version.
#### 1c. Tracking Issue for Support[​](#1c-tracking-issue-for-support)
If there are behavioral breaking changes in the new major version, consider also creating a tracking issue showing support across popular plugins.
To do this:
- Create a pinned issue (example: [📈 Tracking: typescript-eslint v8 support](https://github.com/typescript-eslint/typescript-eslint/issues/9720))
- For each plugin you&#x27;re familiar with, try sending a draft PR to them with a description of what you&#x27;re doing (example: [chore: bump typescript-eslint to v8](https://github.com/vitest-dev/eslint-plugin-vitest/pull/479))
- Make sure you&#x27;re subscribed to notifications on that issue and any PRs, and update the table regularly
#### 1d. Post Community Testing Config Touchups[​](#1d-post-community-testing-config-touchups)
There may be additional changes to preset configs discovered as part of the community testing.
If that&#x27;s the case:
- Create a discussion describing the suggested changes [example: [Configs: Last round of "final" changes to configs for v6](https://github.com/typescript-eslint/typescript-eslint/discussions/7130)].
- Post this new discussion in the previous config changes one, in the typescript-eslint Discord, and on social media.
- Once the greater of (2 weeks) and (discussion settling down) has passed
If possible, we prefer to avoid making a second round of config changes.
These should only be done for feedback that consistently comes up in community testing.
### 2. Merging Breaking Changes[​](#2-merging-breaking-changes)
- Send a PR from `v${major}` to `main` [example: [v6.0.0](https://github.com/typescript-eslint/typescript-eslint/pull/5886)].
- Change all [breaking change PRs](https://github.com/typescript-eslint/typescript-eslint/issues?q=is%3Aissue+is%3Aopen+label%3A%22breaking+change%22) to target the `v${major}` branch.
To signify these changes as breaking, the first line of the PR description must read as `BREAKING CHANGE:`, and second line should briefly summarize the changes.
- It is important to note that when merged the commit message must also include `BREAKING CHANGE:` as the first line in order for `nx release` to recognize it as a breaking change in the release notes. If you miss this it just means more manual work when writing the release documentation.
- Write and share out a blog post announcing the new beta [example: [Docs: Blog post describing changes & migration strategy for v5->v6](https://github.com/typescript-eslint/typescript-eslint/issues/6466)].
Keep this post up-to-date as changes land in the `v${major}` branch.
- Send a PR to the `v${major}` branch that adds the old major version to [Users > Releases > Old Release Documentation](/users/releases#old-release-documentation)
- Wait until all required PRs have been merged
- Write a blog post announcing the new release [example: [Docs: Release blog post for v6](https://github.com/typescript-eslint/typescript-eslint/issues/7153)], and land it in the `v${major}` branch.
- Let the release wait for **at least 1 week** to allow time for early adopters to help test it and discuss the changes.
Promote it on social media to get some additional attention.
- Once discussions have settled, traditional merge commit the PR on top of `main` by temporarily enabling that merge setting for the repo.
note*Non*-breaking changes can be merged to `main` or the major branch.
They don&#x27;t need any special treatment.
### 3. Releasing the Version[​](#3-releasing-the-version)
- Discuss with the maintainers to be ready for an [out-of-band](#out-of-band-releases) release. Doing this manually helps ensure someone is on-hand to action any issues that might arise from the major release.
- Prepare the release notes. `nx release` will automatically generate the release notes on GitHub, however this will be disorganized and unhelpful for users. We need to reorganize the release notes so that breaking changes are placed at the top to make them most visible. If any migrations are required, we must list the steps to make it easy for users.
Example release notes: [`v6.0.0`](https://github.com/typescript-eslint/typescript-eslint/releases/tag/v6.0.0), [`v5.0.0`](https://github.com/typescript-eslint/typescript-eslint/releases/tag/v5.0.0)
- Update Netlify deploys for old sites:
Update the `CURRENT_MAJOR_VERSION` environment variable to the new major version integer, such as `9`
- Re-deploy the `v${major}` branches listed in [Users > Releases > Old Release Documentation](/users/releases#old-release-documentation)
- Finally, post the release on social media with a link to the GitHub release. Make sure you include additional information about the highlights of the release!
## Out-of-Band Releases[​](#out-of-band-releases)
Per [Users > Releases > Out-of-Band Releases](/users/releases#out-of-band-releases), we may manually trigger a new release for a rare emergency such as a critical regression.
If that happens:
- Mention in any relevant issue(s) that you intend to release an out-of-band release
- Post in a private maintenance Discord channel that you&#x27;re working on it
- Send a pull request resolving the issue(s)
- Waiting up to a day (as reasonable) for approval before merging the PR
- Trigger the private release workflow to cause a new release
- Post back in those same issue(s) with a link to the newly released version(s)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/maintenance/Releases.mdx)- [Major Releases](#major-releases)[1. Pre-Release Preparation](#1-pre-release-preparation)[1a. Shared Config Changes](#1a-shared-config-changes)- [1b. Voluntary Community Testing](#1b-voluntary-community-testing)- [1c. Tracking Issue for Support](#1c-tracking-issue-for-support)- [1d. Post Community Testing Config Touchups](#1d-post-community-testing-config-touchups)- [2. Merging Breaking Changes](#2-merging-breaking-changes)- [3. Releasing the Version](#3-releasing-the-version)- [Out-of-Band Releases](#out-of-band-releases)