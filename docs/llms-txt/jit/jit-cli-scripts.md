# Source: https://docs.jit.io/docs/jit-cli-scripts.md

# Jit Scripts for extended usability

Jit user scripts enable you to perform actions using CLI to extend the usability of the Jit platform.

Currently, the following scripts are supported:

* **[Sync teams](https://docs.jit.io/docs/jit-teams-sync)**, when GitHub is not used for team management, this script syncs teams manually from other team management systems to [Jit teams](https://docs.jit.io/docs/teams).
* **[Jit on GitHub Self-hosted-runners](https://docs.jit.io/docs/jit-on-github-self-hosted-runners)**, automates configuring Jit to run on a [GitHub self-hosted runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners). This is especially useful for [Scaning Your Web Application for Vulnerabilities (DAST)](https://docs.jit.io/docs/run-a-web-application-scanner) if the web app is protected (no public IP / WAF).

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

If haven't cloned the repo recently, make sure to update it.

```
git pull https://github.com/jitsecurity/jit-customer-scripts.git
```

To see all available scripts, use the `make help` command.