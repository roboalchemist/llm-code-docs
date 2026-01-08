# Run local CLI scans

Source: https://semgrep.dev/docs/for-developers/cli

- [](/docs/)- [For developers](/docs/for-developers/overview)- Run scans- Run local CLI scans**On this page- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)Run local CLI scans
You can run local Semgrep CLI scans with the Semgrep command-line tool.

## Prerequisites[​](#prerequisites)

- An existing Semgrep org account.
- Semgrep CLI tool installed in your local machine.

## Best practices[​](#best-practices)
It&#x27;s best to run the following command for local scans:

`semgrep ci --dry-run`

- The command `semgrep ci` tells Semgrep to use your organization&#x27;s chosen analyses and rules for the scan.
- The `--dry-run` flag ensures that your scans are not uploaded to the Semgrep web app. This is recommended because your code could be a work in progress, subject to change, whereas code uploaded as a PR or MR usually indicates the code is ready for review.

When Semgrep performs a CLI or IDE scan, it presents findings from **all rules** that your AppSec team uses. For this reason, you may encounter **more false positive or low severity findings** that you can ignore.

## Common Semgrep commands[​](#common-semgrep-commands)
### `semgrep scan`[​](#semgrep-scan)
The following command runs a local scan with Semgrep&#x27;s open source Community Edition (CE) using pre-selected rules for a variety of languages:

`semgrep scan`

- `semgrep scan` does not take into account your organization&#x27;s settings.
- You do **not** need to be logged in to run a scan.
- It only runs lightweight SAST analyses.
- It does not run other Semgrep products, such as Secrets or Supply Chain.

caution
- `semgrep scan` does not run the same analyses as `semgrep ci` so you may have a higher rate of false positives.
- You can run `semgrep scan --pro` to run advanced SAST analyses with no other Semgrep products.

#### Test a custom rule[​](#test-a-custom-rule)
You can test a custom rule by creating a test file. See [Testing rules](/docs/writing-rules/testing-rules).

After you&#x27;ve tested your custom rule, you can try it on your codebase locally:

- Ensure that you&#x27;re signed in to Semgrep from the CLI by entering `semgrep login`. If you have successfully signed in, you should see **API token already exists** or a similar message.
- Enter the following command:
`semgrep scan --pro --config [CUSTOM_RULE].yaml`
Replace `CUSTOM_RULE.yaml` with the name of your custom rule.

### `semgrep ci`[​](#semgrep-ci)
The `semgrep ci` command, without any flags, sends the results of your scan to Semgrep AppSec Platform with the slug `local-scan/PROJECT_NAME`. When using this command in a team setting, ensure that you are aware of its risks and that your team members are aware that you&#x27;re uploading the results of local scans.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/for-developers/developer-local-scans.md)Last updated on **Jan 16, 2025**