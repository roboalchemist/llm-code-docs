# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/integrate-the-ai-code-review-agent-into-the-ci-cd-pipeline.md

# Integrate the AI Code Review Agent into the CI/CD pipeline

[**Bito Cloud**](https://alpha.bito.ai/) lets you integrate the [**AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview) into your CI/CD pipeline for automated code reviews. This document provides a step-by-step guide to help you configure and run the script successfully.

## Installation and Configuration Steps

1. [**Select the appropriate Git provider guide from this link**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/..#connect-bito-to-your-git-provider) based on your Git provider, and follow the step-by-step instructions to install the **AI Code Review Agent** using **Bito Cloud**. Be sure to review the prerequisites and the installation/configuration steps provided in the documentation.
2. [**Download the bito-action-script folder from GitHub**](https://github.com/gitbito/CodeReviewAgent/tree/main/bito-action-script), which includes a shell script (`bito-actions.sh`) and a configuration file (`bito_action.properties`).
3. You can integrate the AI Code Review Agent into your CI/CD pipeline in two ways, depending on your preference:

* **Option 1: Using the** `bito_action.properties` **File**
  * Configure the following properties in the `bito_action.properties` file located in the downloaded **bito-action-script** folder.

<table><thead><tr><th width="261" align="center">Property Name</th><th>Description</th></tr></thead><tbody><tr><td align="center"><strong>agent_instance_url</strong></td><td>The URL of the Agent instance provided after configuring the AI Code Review Agent with Bito Cloud.</td></tr><tr><td align="center"><strong>agent_instance_secret</strong></td><td>The secret key for the Agent instance obtained after configuring the AI Code Review Agent with Bito Cloud.</td></tr><tr><td align="center"><strong>pr_url</strong></td><td>URL of your pull request on GitLab, GitHub, or BitBucket.</td></tr></tbody></table>

* Run the following command:
  * `./bito_actions.sh bito_action.properties`
  * **Note:** When using the properties file, make sure to provide all the three parameters in `.properties` file

* #### **Option 2: Using Runtime Values** <a href="#option-2-using-runtime-values" id="option-2-using-runtime-values"></a>
  * Provide all necessary values directly on the command line:
    * `./bito_actions.sh agent_instance_url=<agent_instance_url> agent_instance_secret=<secret> pr_url=<pr_url>`
    * Replace `<agent_instance_url>`, `<secret>`, and `<pr_url>` with your specific values.
  * **Note:** You can also override the values given in the `.properties` file or provide values that are not included in the file. For example, you can configure `agent_instance_url` and `agent_instance_secret` in the `bito_action.properties` file, and only pass `pr_url` on the command line during runtime.
    * `./bito_actions.sh bito_action.properties pr_url=<pr_url>`
    * Replace `<pr_url>` with your specific values.

4. Incorporate the AI Code Review Agent into your CI/CD pipeline by adding the appropriate commands to your build or deployment scripts. This integration will automatically trigger code reviews as part of the pipeline, enhancing your development workflow by enforcing code quality checks with every change.
