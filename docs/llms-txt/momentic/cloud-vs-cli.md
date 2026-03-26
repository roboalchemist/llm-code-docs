# Source: https://momentic.ai/docs/cloud-vs-cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloud vs. CLI

> Compare Momentic's Cloud and CLI offerings to find the best fit for your team

Momentic offers two primary ways to build and run tests:
[Cloud](/quickstart/cloud) and [CLI](/quickstart/cli). Each has its own
strengths and is suited for different use cases.

## Comparison

Cloud is ideal for teams that want to get started quickly without worrying about
infrastructure. It allows you to build and run tests directly in your browser,
making it easy to monitor public-facing applications.

If you want to
[shift left](https://github.com/resources/articles/security/what-is-shift-left-testing)
and run tests as part of your development process, the CLI is the best choice.
It allows you to run tests locally, store them in version control, and integrate
them into your CI/CD pipelines seamlessly.

| Features                   | Cloud                                                | CLI                                         |
| -------------------------- | ---------------------------------------------------- | ------------------------------------------- |
| Version control            | No                                                   | Store tests in GitHub and other SCM systems |
| CI/CD integration          | Yes                                                  | Yes                                         |
| Public deployment testing  | Yes                                                  | Yes                                         |
| Private deployment testing | Yes with IP whitelist                                | Yes                                         |
| Local testing              | Yes with tunnel                                      | Yes                                         |
| Scheduled runs             | Yes                                                  | Orchestrate with CI/CD                      |
| Infrastructure             | Provisioned and managed by Momentic                  | Self-hosted or managed by your team         |
| Analytics                  | Yes                                                  | Yes                                         |
| Custom reporting           | No                                                   | JSON, JUnit, and Allure reports             |
| Notifications              | Slack, PagerDuty, Opsgenie, any webhook-based system | Orchestrate with CI/CD                      |

## Next steps

<Card title="CLI" icon="terminal" horizontal href="/quickstart/cli">
  For teams looking to store tests in source code management (SCM) and integrate
  into CI/CD
</Card>

<Card title="Cloud" icon="cloud" horizontal href="/quickstart/cloud">
  For teams looking to get started quickly and run tests without worrying about
  infrastructure
</Card>


Built with [Mintlify](https://mintlify.com).