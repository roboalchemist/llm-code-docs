# Source: https://docs.jit.io/docs/jit-on-github-self-hosted-runners.md

# Self-hosted GitHub Actions Set Up

## Overview

* **Jit on GitHub Self-hosted-runners**, automates configuring Jit to run on a [GitHub self-hosted runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners). This is especially useful for [Scanning Your Web Application for Vulnerabilities (DAST)](https://docs.jit.io/docs/run-a-web-application-scanner) if the web app is protected (no public IP / WAF).

## Requirements

* Python 3.x
* Git
* Make

## Installing and cloning the GitHub repository

```Text Mac
brew install git make
git clone https://github.com/jitsecurity/jit-customer-scripts.git
cd jit-customer-scripts
```
```Text Ubuntu
sudo apt update
sudo apt install -y git make
git clone https://github.com/jitsecurity/jit-customer-scripts.git
cd jit-customer-scripts
```
```Text Amazon Linux
sudo yum install -y git make
git clone https://github.com/jitsecurity/jit-customer-scripts.git
cd jit-customer-scripts
```

If you haven't cloned the repo recently, make sure to update it.

```
git pull https://github.com/jitsecurity/jit-customer-scripts.git
```

To see all available scripts, use the `make help` command.

The Jit self-hosted runner customer script automates the configuration process for running Jit on GitHub self-hosted runners. The advantages of using self-hosted runners include:

* Cost, reducing expenses using your own hardware.
* Scale, not being limited to the GitHub infrastructure for runners.
* Access, accessing repos using whitelist IPs or accessing internal resources like a web app on a staging environment. Self-hosted runners are also very useful for running [Scanning Your Web Application for Vulnerabilities (DAST)](https://docs.jit.io/docs/run-a-web-application-scanner) on a protected app without a public IP or with WAF.

For more information see [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners).

The Jit self-hosted runner customer script and its sub-commands can be used to configure GitHub self-hosted runners on the following OS:

* Amazon Linux.
* Ubuntu.

## Configuring self-hosted runners

1. Make sure you have installed the prerequisites and cloned the repo.
   ```Text Amazon Linux
   sudo yum install -y git make
   git clone https://github.com/jitsecurity/jit-customer-scripts.git
   cd jit-customer-scripts
   ```
   ```Text Ubuntu
   sudo apt update
   sudo apt install -y git make
   git clone https://github.com/jitsecurity/jit-customer-scripts.git
   cd jit-customer-scripts
   ```
2. If you haven't cloned the repo recently, make sure to update it.
   ```
   git pull https://github.com/jitsecurity/jit-customer-scripts.git
   ```
3. Get the **[GitHub self-hosted runner token](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners)**
4. Get the **GitHub organization name** for your organization.
5. Use the following scripts to automate the process:

   ```Text Amazon Linux
   make self-hosted-runner amazon runner_token=<runner-token> github_org=<github-organization>
   ```
   ```Text Ubuntu
   make self-hosted-runner ubuntu runner_token=<runner-token> github_org=<github-organization>
   ```

   * Answer the questions about the self-hosted runner configurations.
   * Restart the EC2 machine. The self-hosted runner automatically initiates after the machine reboots.
   * Enter the  <**runner-token**> and <**github-organization**> values.