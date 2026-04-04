# Source: https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted.md

# Install AI Architect (self-hosted)

This guide walks you through installing [**Bito's AI Architect**](https://docs.bito.ai/ai-architect/overview) as a self-hosted service in your own infrastructure. Self-hosting gives you complete control over where your code knowledge graph resides and how AI Architect accesses your repositories.

**Why choose self-hosted deployment?** Organizations with strict data governance requirements, air-gapped environments, or specific compliance needs benefit from running AI Architect within their own infrastructure. Your codebase analysis and knowledge graph stay entirely within your control, while still providing the same powerful context-aware capabilities to your AI coding tools.

**What you'll accomplish:** By the end of this guide, you'll have AI Architect running on your infrastructure, connected to your Git repositories, and ready to integrate with AI coding tools like Claude Code, Cursor, Windsurf, and GitHub Copilot through the Model Context Protocol (MCP).

### Deployment options

AI Architect can be deployed in three different configurations depending on your team size, infrastructure, and security requirements:

#### a. Personal use (with your LLM keys)

Set up AI Architect on your local machine for individual development work. You'll provide your own LLM API keys for indexing, giving you complete control over the AI models used and associated costs.

**Best for:** Individual developers who want codebase understanding on their personal machine.

#### b. Team / shared access (with your LLM keys)

Deploy AI Architect on a shared server within your infrastructure, allowing multiple team members to connect their AI coding tools to the same MCP server. Each team member can configure AI Architect with their preferred AI coding agent while sharing the same indexed codebase knowledge graph.

**Best for:** Development teams that want to share codebase intelligence across the team while managing their own LLM costs.

#### c. Enterprise deployment (requires Bito Enterprise Plan)

Deploy AI Architect on your infrastructure (local machine or shared server) with indexing managed by Bito. Instead of providing your own LLM keys, Bito handles the repository indexing process, simplifying setup and cost management.

**Best for:** Organizations that prefer managed indexing without handling individual LLM API keys and costs.

{% hint style="info" %}
**Note:** All deployment options are self-hosted on your infrastructure — your code and knowledge graph remain under your control.
{% endhint %}

## Prerequisites

### a. Required accounts and tokens

{% stepper %}
{% step %}

### Bito API Key (aka Bito Access Key)

You'll need a **Bito account** and a **Bito Access Key** to authenticate AI Architect. You can sign up for a Bito account at [**https://alpha.bito.ai**](https://alpha.bito.ai/), and create an access key from [**Settings -> Advanced Settings**](https://alpha.bito.ai/home/advanced)

* [**View Guide**](https://docs.bito.ai/help/account-and-settings/access-key)
  {% endstep %}

{% step %}

### Git provider

We support the following Git providers:

* GitHub
* GitLab
* Bitbucket

So, you'll need an account on one of these Git providers to index your repositories with AI Architect.
{% endstep %}

{% step %}

### Git Access Token

A personal access token from your chosen Git provider is required. You'll use this token to allow AI Architect to read and index your repositories.

1. **GitHub Personal Access Token (Classic):** To use GitHub repositories with AI Architect, ensure you have a CLASSIC personal access token with repo access. We do not support fine-grained tokens currently.
   * [**View Guide**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
2. **GitLab Personal Access Token:** To use GitLab repositories with AI Architect, a token with API access is required.
   * [**View Guide**](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)
3. **Bitbucket Access Token:** To use Bitbucket repositories with AI Architect, you need **API Token** or **HTTP Access Token** depending on your Bitbucket setup.
   1. **Bitbucket Cloud (`API Token`):** You must provide both your **token** and **email address**.
      * [**View Guide**](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/)
   2. **Bitbucket Self-Hosted (`HTTP Access Token`):** You must provide both your **token** and **username**.
      * [**View Guide**](https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html)
        {% endstep %}

{% step %}

### LLM API keys

Bito's AI Architect uses Large Language Models (LLMs) to build a knowledge graph of your codebase.

We suggest you provide API keys for both **Anthropic** and **Grok** LLMs, as that provides the best coverage and the best cost of indexing.

Bito will use **Claude Haiku** and **Grok Code Fast** together to index your codebase. It will cost you approximately USD $0.20 - $0.40 per MB of indexable code (we do not index binaries, TARs, zips, images, etc). If you provide only an Anthropic key without Grok, your indexing costs will be significantly higher, approximately USD $1.00 - $1.50 per MB of indexable code.&#x20;
{% endstep %}
{% endstepper %}

### b. System requirements

AI Architect can be installed on your local machine for individual use, or on a shared server that your entire team can connect to. When installed on a server, multiple developers can configure their AI coding tools (such as Claude Code, Cursor, Windsurf, etc.) to use the same MCP server, sharing access to the indexed codebase.

The AI Architect supports the following operating systems:

* **macOS**
* **Unix-based systems** (Ubuntu, Debian, RHEL, or similar distributions)
* **Windows (via WSL2)**

#### Shared servers (for team deployments)

* **On-premise physical servers** - Bare metal Linux servers in your data center
* **On-premise virtual machines** - VMware, Hyper-V, Proxmox, KVM, or other virtualization platforms
* **Cloud virtual machines** - AWS EC2, Google Cloud Compute Engine, Azure VMs, DigitalOcean Droplets, or similar cloud instances

{% stepper %}
{% step %}

### Hardware specifications

|          |                                                                                   Recommended                                                                                   |
| :------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|  **CPU** |                                                                                    6-8 cores                                                                                    |
|  **RAM** |                                                                                     8-12 GB                                                                                     |
| **Disk** | <p>SSD with adequate IOPS<br><br><strong>Note:</strong> Ensure sufficient disk space is available, as all configured repositories will be cloned to this disk during setup.</p> |

AI Architect automatically detects available system resources during setup and configures optimal resource allocation for its Docker containers. For most deployments, the automatic configuration provides good performance. However, you can manually adjust these settings to fine-tune performance or accommodate specific workload requirements.

You can customize resource limits by editing the `.env-bitoarch` file and run the command `./setup.sh --force-restart` to update the allocation. The following environment variables can be manually configured to control resource allocation.

```dotenv
CIS_PROVIDER_MEMORY_LIMIT=1g
CIS_MANAGER_MEMORY_LIMIT=2g
CIS_CONFIG_MEMORY_LIMIT=512m
MYSQL_MEMORY_LIMIT=2g
CIS_TRACKER_MEMORY_LIMIT=512m


CIS_PROVIDER_CPU_LIMIT=1.0
CIS_MANAGER_CPU_LIMIT=2.0
CIS_CONFIG_CPU_LIMIT=0.5
MYSQL_CPU_LIMIT=1.0
CIS_TRACKER_CPU_LIMIT=0.5
```

{% endstep %}

{% step %}

### **WSL2 is required for Windows users**

If you're running Windows, Windows Subsystem for Linux 2 (WSL2) must be installed before proceeding.

**To install WSL2:**

1. Open PowerShell or Command Prompt as Administrator
2. Run the following command:

```shellscript
wsl --install
```

3. Set up your Ubuntu username and password when prompted.
   {% endstep %}

{% step %}

### Docker Desktop / Docker Service (required)

**Docker Compose** is required to run AI Architect.

The easiest and recommended way to get Docker Compose is to install **Docker Desktop**.

Docker Desktop includes Docker Compose along with Docker Engine and Docker CLI which are Docker Compose prerequisites.

[**Install Docker Desktop**](https://docs.docker.com/compose/install)

**Configuration for Windows (WSL2):**

If you're using Windows with WSL2, you need to enable Docker integration with your WSL distribution:

1. Open **Docker Desktop**
2. Go to **Settings** > **Resources** > **WSL Integration**
3. Enable integration for your WSL distribution (e.g., Ubuntu)
4. Click **Apply**
   {% endstep %}

{% step %}

### Kubernetes cluster (required for Kubernetes based deployment method)

### For production environments:

During the setup process given below, if you choose [**Kubernetes**](https://kubernetes.io/docs/home/) as your deployment method, you must have an existing Kubernetes cluster set up and running.

Ensure your Kubernetes cluster have the following required tools:

* **kubectl** (Kubernetes command-line tool)
* **helm** (Kubernetes package manager)

### For testing and development:

For testing purposes, you can create a local Kubernetes cluster using KIND (Kubernetes in Docker). KIND allows you to run Kubernetes clusters in Docker containers.

**Install KIND:**

* **macOS:**

```shellscript
brew install kind kubectl helm
```

* **Linux:**

```shellscript
# KIND
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

{% hint style="info" %}
**Note:** Before creating a KIND cluster, verify Docker has sufficient resources:

```shellscript
docker info --format 'CPUs={{.NCPU}} Mem={{.MemTotal}}'
```

\
**Required:** Minimum 4 CPUs and 8GB RAM

If resources are insufficient, increase Docker Desktop resources (Preferences → Resources) and restart Docker.
{% endhint %}

#### Setting up a test cluster with KIND

Create a KIND cluster with proper port mappings for service access:

```shellscript
kind create cluster --name bito-ai-architect --config - <<EOF
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
  - containerPort: 443
    hostPort: 443
EOF
```

{% hint style="info" %}
**Note:** Services use ClusterIP for secure, internal-only access. External access is configured via Ingress Controller on ports 80/443.
{% endhint %}

#### Verify cluster

```shellscript
kubectl cluster-info --context kind-bito-ai-architect
kubectl get nodes
```

{% endstep %}
{% endstepper %}

## Installation guide

{% stepper %}
{% step %}

### Install AI Architect

Before proceeding with the installation, ensure **Docker Desktop / Docker Service** or **Kubernetes cluster** is running on your system. If it's not already running, launch it and wait for it to fully start before continuing.

Open your terminal:

* **Linux/macOS**: Use your standard terminal application
* **Windows (WSL2)**: Launch the **Ubuntu** application from the **Start menu**

Execute the installation command:

```bash
curl -fsSL https://aiarchitect.bito.ai/install.sh | bash
```

The installation script will:

* Download the latest Bito AI Architect package
* Extract it to your system
* Initialize the setup process

{% hint style="info" %}
**Installing dependencies:**

The AI Architect setup process will automatically check for required tools on your system. If any dependencies are missing (such as `jq`, which is needed for JSON processing), you'll be prompted to install them. Simply type `y` and press `Enter` to proceed with the installation.
{% endhint %}
{% endstep %}

{% step %}

### Configuration

Follow the on-screen prompts to configure your deployment. You'll provide the following information:

#### Select AI Architect deployment method:

Choose how you want to deploy Bito's AI Architect. We support two deployment methods:

1. **Docker Compose:** Deploys AI Architect using Docker Compose.
2. **Kubernetes:** Deploys AI Architect to an existing Kubernetes cluster. Choose this option if you have an existing Kubernetes cluster running and want to leverage Kubernetes for orchestration, scaling, and management.
   * **Note:** The setup script will automatically deploy AI Architect services to your Kubernetes cluster in the `bito-ai-architect` namespace.

{% hint style="info" %}
**If you have a Kubernetes cluster:**

1. Ensure it's running
2. Verify the current Kubernetes context: `kubectl config current-context`
3. Check connectivity: `kubectl cluster-info`

\
**If you don't have a Kubernetes cluster:**

1. Select Docker Compose (option 1)
   {% endhint %}

#### You'll need to provide the following details when prompted:

{% hint style="info" %}
**Note:** Refer to the [**Prerequisites section**](#prerequisites) for details on how to obtain these.
{% endhint %}

* **Bito API Key** (required) - Enter your Bito Access key and press Enter.
* **Git provider** (required):

  You'll be prompted to choose your Git provider:

  1. GitLab
  2. GitHub
  3. Bitbucket

  Enter the number corresponding to your Git provider and press Enter.
* **Is your Git provider self-hosted or cloud-based?**

  * Type `y` for enterprise/self-hosted instances (like `https://github.company.com`) and enter your custom domain URL
  * Type `n` for standard cloud providers (github.com, gitlab.com, bitbucket.org)

  Press Enter to continue.
* **Git Access Token** (required) - Enter personal access token for your Git provider and press Enter.
* **Configure LLM API keys** (required) - Choose which AI model provider(s) to configure:

  1. Anthropic
  2. Grok
  3. OpenAI

  Enter the number corresponding to your AI model provider, then provide your API key when prompted.

  We suggest you provide API keys for both **Anthropic** and **Grok** LLMs, as that provides the best coverage and the best cost of indexing.

  After adding a provider, you'll be asked: *"Do you want to configure another provider?"*

  * Type `y` to add additional providers (recommended for better coverage and fallback options).
  * Type `n` when you're done adding LLM providers.

  Press Enter to continue.
* **Generate a secure MCP access token?** - You'll be asked if you want Bito to create a secure token to prevent unauthorized access to your MCP server:

  * Type `y` to generate a secure access token (recommended)
  * Type `n` to skip token generation

  Press Enter to continue.
  {% endstep %}

{% step %}

### Add repositories

Once your Git account is connected successfully, Bito automatically detects your repositories and populates the `/usr/local/etc/bitoarch/.bitoarch-config.yaml` file with an initial list. Review this file to confirm which repositories you want to index — feel free to remove any that should be excluded or add others as needed. Once the list looks correct, save the file, and continue with the steps below.

{% hint style="info" %}
For versions older than 1.4.0, configuration file can be found in installation directory.
{% endhint %}

Below is an example of how the `.bitoarch-config.yaml` file is structured:

```yaml
repository:
  configured_repos:
    - namespace: your-org/repo-name-1
    - namespace: your-org/repo-name-2
    - namespace: your-org/repo-name-3
```

After updating the `.bitoarch-config.yaml` file, you have two options to proceed with adding your repositories for indexing:

1. **Auto Configure (recommended)**
   * Automatically saves the repositories and starts indexing
   * If needed, edit the repo list before selecting this option
2. **Manual Setup**
   * You have to manually update the configuration file and then start the indexing. Below we have provided complete details of the manual process.

Once you select an option, your **Bito MCP URL** and **Bito MCP Access Token** will be displayed. Make sure to store them in a safe place, you'll need them later when configuring MCP server in your AI coding agent (e.g., Claude Code, Cursor, Windsurf, GitHub Copilot (VS Code), etc.).

To manually apply the configuration, run this command:

```shellscript
bitoarch add-repos /usr/local/etc/bitoarch/.bitoarch-config.yaml
```

{% endstep %}

{% step %}

### Start indexing

Once your repositories are configured, AI Architect needs to analyze and index them to build the knowledge graph. This process scans your codebase structure, dependencies, and relationships to enable context-aware AI assistance.

Start the indexing process by running:

```shellscript
bitoarch index-repos
```

{% hint style="info" %}
**Note:** Indexing process will take approximately 3-10 minutes per repository. Smaller repos take less time.
{% endhint %}

Once the indexing is complete, you can configure AI Architect MCP server in any coding or chat agent that supports MCP.
{% endstep %}

{% step %}

### Check indexing status

Run this command to check the status of your indexing:

```shellscript
bitoarch index-status
```

{% hint style="info" %}
**Example output:**

```
Configured Repositories:
  Total: 3

Repository Index Status:
State: ⏳ running
  Progress: 0 / 1 completed
  In Progress: 1

Workspace Index Progress:
State: ⏳ running
  Progress: 1 / 2 completed
  In Progress: 1

Overall Status: in-progress
```

**What each section represents:**

* **Configured Repositories:** Shows how many repositories are added in your config file for indexing.
* **Repository Index Status:** Shows the indexing progress for each individual repository.
* **Workspace Index Progress:** Shows the status of indexes that combine and process information across multiple repositories.
* **Overall Status:** Provides a single summary indicating whether indexing is still running, completed successfully, or failed.
  {% endhint %}
  {% endstep %}

{% step %}

### Check MCP server details

To manually check the MCP server details (e.g. **Bito MCP URL** and **Bito MCP Access Token**), use the following command:

```shellscript
bitoarch mcp-info
```

If you need to update your **Bito MCP Access Token**, use the following command:

```shellscript
bitoarch rotate-mcp-token <new-token>
```

{% hint style="info" %}
Replace `<new-token>` with your new secure token value.

**Important:** After rotating the token, you'll need to update it in all AI coding agents (Claude Code, Cursor, Windsurf, etc.) where you've configured this MCP server.
{% endhint %}
{% endstep %}
{% endstepper %}

## Update repository list and re-index

Edit `/usr/local/etc/bitoarch/.bitoarch-config.yaml` file to add/remove repositories.

```shellscript
vim /usr/local/etc/bitoarch/.bitoarch-config.yaml
```

To apply the changes, run this command:

```shellscript
bitoarch update-repos /usr/local/etc/bitoarch/.bitoarch-config.yaml
```

Start the re-indexing process using this command:

```shellscript
bitoarch index-repos
```

## Accessing services (Kubernetes-based deployment)

Port-forwards are exposed on all network interfaces (0.0.0.0) and are accessible from any machine on the network.

#### Local access (from the Kubernetes host machine)

```shellscript
curl http://localhost:5001/health          # Provider
curl http://localhost:5002/health          # Manager
curl http://localhost:5003/health          # Config
```

#### Network access (from other machines on your network)

Get the host machine's IP address:

```shellscript
kubectl get nodes -o wide
# Or: hostname -I (Linux) / ifconfig (macOS)
```

From another machine on the network:

```shellscript
curl http://<host-ip>:5001/health          # Provider
curl http://<host-ip>:5002/health          # Manager
curl http://<host-ip>:5003/health          # Config
curl http://<host-ip>:5005/health          # Tracker
```

#### Security considerations

> **Important security notes:**
>
> * Port-forwards use HTTP (not HTTPS) - traffic is unencrypted
> * Services are accessible from any machine that can reach the host
>
> **For production internet-facing deployments:**
>
> * Use firewall rules to restrict access to trusted IPs
> * Consider using Kubernetes Ingress with TLS/SSL
> * Implement VPN for remote access
> * Use network policies to limit pod-to-pod traffic

#### Alternative: Kubernetes Ingress (production)

For production deployments, configure a Kubernetes Ingress Controller with TLS/SSL instead of using port-forwards. This provides secure HTTPS access with proper certificate management.

## Setting up AI Architect MCP in coding agents

Now that AI Architect is installed and your repositories are indexed, the next step is to connect it to your AI coding tools (such as Claude Code, Cursor, Windsurf, GitHub Copilot, etc.) through the Model Context Protocol (MCP).

#### Quick setup (recommended)

**Save time with our automated installer!** We provide a one-command setup that automatically configures AI Architect for all compatible AI coding tools on your system.

The automated installer will:

* Detect all supported AI tools installed on your system
* Configure them automatically with your MCP credentials
* Get you up and running in seconds instead of manually configuring each tool

👉 [**Try our Quick MCP Integration Guide**](https://docs.bito.ai/ai-architect/quick-mcp-integration-with-ai-coding-agents) for automated setup across all your tools.

#### Manual setup

If you prefer hands-on control over your configuration or encounter issues with automated setup, we provide detailed step-by-step guides for each supported AI coding tool:

* [**Guide for Claude Code**](https://docs.bito.ai/ai-architect/guide-for-claude-code)
* [**Guide for Cursor**](https://docs.bito.ai/ai-architect/guide-for-cursor)
* [**Guide for Windsurf**](https://docs.bito.ai/ai-architect/guide-for-windsurf)
* [**Guide for GitHub Copilot (VS Code)**](https://docs.bito.ai/ai-architect/guide-for-github-copilot-vs-code)
* [**Guide for Junie (JetBrains)**](https://docs.bito.ai/ai-architect/guide-for-junie-jetbrains)
* [**Guide for JetBrains AI Assistant**](https://docs.bito.ai/ai-architect/guide-for-jetbrains-ai-assistant)

Each guide walks you through the complete manual configuration process for that specific tool.

## Configuring AI Architect for Bito AI Code Review Agent

Now that you have **AI Architect** set up, you can take your code quality to the next level by integrating it with [**Bito's AI Code Review Agent**](https://bito.ai/product/ai-code-review-agent/). This powerful combination delivers significantly more accurate and context-aware code reviews by leveraging the deep codebase knowledge graph that AI Architect has built.

**Why integrate AI Architect with AI Code Review Agent?**

When the AI Code Review Agent has access to AI Architect's knowledge graph, it gains a comprehensive understanding of your entire codebase architecture — including microservices, modules, APIs, dependencies, and design patterns.

This enables the AI Code Review Agent to:

* **Provide system-aware code reviews** - Understand how changes in one service or module impact other parts of your system
* **Catch architectural inconsistencies** - Identify when new code doesn't align with your established patterns and conventions
* **Detect cross-repository issues** - Spot problems that span multiple repositories or services
* **Deliver more accurate suggestions** - Generate fixes that are grounded in your actual codebase structure and usage patterns
* **Reduce false positives** - Better understand context to avoid flagging valid code as problematic

#### Getting started with AI Architect-powered code reviews

1. Log in to [**Bito Cloud**](https://alpha.bito.ai/home/welcome)
2. Open the [**AI Architect Settings**](https://alpha.bito.ai/home/ai-architect/settings?mode=self-hosted) dashboard.
3. In the **Server URL** field, enter your **Bito MCP URL**
4. In the **Auth token** field, enter your **Bito MCP Access Token**

**Need help getting started?** Contact our team at [**support@bito.ai**](mailto:support@bito.ai) to request a trial. We'll help you configure the integration and get your team up and running quickly.

## Upgrading AI Architect

Upgrade your AI Architect installation to the latest version while preserving your data and configuration. The upgrade process:

* Automatically detects your current version
* Downloads and extracts the new version
* Migrates your configuration and data
* Seamlessly transitions to the new version
* Preserves all indexed repositories and settings

#### Upgrade instructions

#### Option 1: Upgrade from within your installation (Recommended)

If you're running **version 1.1.0 or higher**, navigate to your current installation directory and run:

```shellscript
cd /path/to/bito-ai-architect
```

```shellscript
./scripts/upgrade.sh --version=latest
```

#### Option 2: Upgrade from external location

If you need to run the upgrade from outside your installation directory (useful for **version 1.0.0**), use the `--old-path` parameter:

```shellscript
# Download the standalone upgrade script
curl -O https://github.com/gitbito/ai-architect/blob/main/upgrade.sh
chmod +x upgrade.sh

# Run upgrade with explicit path
./upgrade.sh --old-path=/path/to/bito-ai-architect --version=latest
```

#### Upgrade parameters

The upgrade script supports the following parameters:

```shellscript
# Description
--version=VERSION

# Upgrade to specific version
--version=latest

# Upgrade from custom URL or file
--url=file:///path/to/package.tar.gz

# Specify installation path (required if running outside installation directory)
--old-path=/opt/bito-ai-architect

# Show help message
--help
```

{% hint style="info" %}
**Your data is safe:** All repositories, indexes, API keys, and settings are automatically preserved during upgrade.
{% endhint %}

{% hint style="info" %}
**Important:** You can only upgrade within the same deployment type. To switch from **Docker Compose** to **Kubernetes** or vice versa, you must use the `./setup.sh --clean` command, which will result in data loss.
{% endhint %}

## Troubleshooting guide

```shellscript
# Check all services
bitoarch status
bitoarch health --verbose

# View full configuration
bitoarch show-config --raw

# Test MCP connection
bitoarch mcp-test

# Check indexing status with details
bitoarch index-status --raw

# Check setup log
tail -f setup.log

# Local log files
tail -f var/logs/cis-provider/provider.log
tail -f var/logs/cis-manager/manager.log

# Complete logs
./setup.sh --logs

# Reset installation (removes all data and configuration)
./setup.sh --clean

# Then run setup again
./setup.sh

# To stop all the service
./setup.sh --stop

# Restart service (for env based config updates)
./setup.sh --restart

# Force pull latest images based on service-versions.json and restart services
./setup.sh --update
```

#### Commands specific to Kubernetes-based deployment

```shellscript
# Check Kubernetes pod status
# All pods should show "Running" status.
kubectl get pods -n bito-ai-architect

# Check detailed information about a specific Kubernetes pod
kubectl describe pod <pod-name> -n bito-ai-architect

# Access Kubernetes pod shell
kubectl exec -it -n bito-ai-architect \
  $(kubectl get pod -n bito-ai-architect -l app.kubernetes.io/component=provider -o jsonpath='{.items[0].metadata.name}') \
  -- /bin/sh

# Stop KIND cluster (preserves data)
docker stop bito-ai-architect-control-plane

# Start KIND cluster again
docker start bito-ai-architect-control-plane

# Delete KIND cluster completely
kind delete cluster --name bito-ai-architect

# View Provider service logs:
kubectl logs -n bito-ai-architect -l app.kubernetes.io/component=provider --tail=100 -f

# View Manager service logs:
kubectl logs -n bito-ai-architect -l app.kubernetes.io/component=manager --tail=100 -f
```

## Available commands

For complete reference of AI Architect CLI commands, refer to [Available commands](https://docs.bito.ai/ai-architect/available-commands).
