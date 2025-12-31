# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/cli-vs-webhooks-service.md

# CLI vs webhooks service

On your machine or in a Private Cloud, you can run the AI Code Review Agent via either CLI or webhooks service. This guide will teach you about the key differences between CLI and webhooks service and when to use each mode.

## Difference Between CLI and webhooks service

The main difference between CLI and webhooks service lies in their operational approach and purpose. In CLI, the docker container is used for a one-time code review. This mode is ideal for isolated, single-instance analyses where a quick, direct review of the code is needed.

On the other hand, webhooks service is designed for continuous operation. When set in webhooks service mode, the AI Code Review Agent remains online and active at a specified URL. This continuous operation allows it to respond automatically whenever a pull request is opened in a repository. In this scenario, the git provider notifies the server, triggering the AI Code Review Agent to analyze the pull request and post its review as a comment directly on it.

## When to Use CLI and When to Use webhooks service

Selecting the appropriate mode for code review with the AI Code Review Agent depends largely on the nature and frequency of your code review needs.

### CLI: Ideal for Specific, One-Time Reviews

CLI mode is best suited for scenarios requiring immediate, one-time code reviews. It's particularly effective for:

* Conducting quick assessments of specific pull requests.
* Performing periodic, scheduled code analyses.
* Reviewing code in environments with limited or no continuous integration support.
* Integrating with batch processing scripts for ad-hoc analysis.
* Using in educational settings to demonstrate code review practices.
* Experimenting with different code review configurations.
* Reviewing code on local setups or for personal projects.
* Performing a final check before pushing code to a repository.

CLI mode stands out for its simplicity and is perfect for standalone tasks where a single, direct execution of the code review process is all that's needed.

### Webhooks service: For Continuous, Automated Reviews

Webhooks service, on the other hand, is the go-to choice for continuous code review processes. It excels in:

* Continuously monitoring all pull requests in a repository.
* Providing instant feedback in collaborative projects.
* Seamlessly integrating with CI/CD pipelines for automated reviews.
* Performing automated code quality checks in team environments.
* Conducting real-time security scans on new pull requests.
* Ensuring adherence to coding standards in every pull request.
* Streamlining the code review process in large-scale projects.
* Maintaining consistency in code review across multiple projects.
* Enhancing workflows in remote or distributed development teams.
* Offering prompt feedback in agile development settings.

Webhooks service is indispensable in active development environments where consistent monitoring and immediate feedback are critical. It automates the code review process, integrating seamlessly into the workflow and eliminating the need for manual initiation of code reviews.
