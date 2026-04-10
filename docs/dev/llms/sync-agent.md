# Source: https://dev.writer.com/agent-builder/sync-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sync agents between local and cloud

This guide shows you how to synchronize your agents between local development and Writer Cloud environments. This allows local development offline and cloud development and deployment when you wish to share your agent with your team.

<Tip>To avoid conflicts, work in one environment at a time, then explicitly sync your changes to the other environment when ready. This ensures your changes are properly tracked and preserved across environments.</Tip>

## Overview

There are two main synchronization workflows:

1. **Cloud to local**: Start with a cloud agent and bring it to local development
2. **Local to cloud**: Start locally and push to the cloud

Both workflows involve downloading an agent's configuration from one environment and importing it into another.

Before starting, ensure you have:

* A Writer API key. Learn how to [create and manage API keys](/api-reference/api-keys).
* The `writer` package installed. Learn how to [install the Writer Framework package](/agent-builder/local-development#install-the-writer-framework-package).
* If you plan to do both local and cloud development, review [considerations for dual-environment development](#considerations-for-dual-environment-development) to properly handle environment variables and secrets for both local and cloud development.

## Cloud to local workflow

If you've already created an agent in the AI Studio Agent Builder web editor and want to continue development locally:

### Step 1: Export from cloud

From your cloud agent in Agent Builder, click the three dots in the top right corner of your agent and select **Download agent .zip file** to download a `.zip` file containing your agent's configuration.

<img src="https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=89922197cb60c38a2f1e74d210eaef29" alt="" data-og-width="468" width="468" data-og-height="260" height="260" data-path="images/agent-builder/export-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=280&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=6db01e6c16c3816705ac3a3e12e7058c 280w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=560&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=3e94fc65d17bffa63c6c90219b429f50 560w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=840&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=e149d947ccb465cec113a4c2f20efdc1 840w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=1100&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=a0e3f5276f5a6fab90b59e44b611a603 1100w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=1650&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=1fd4420c9b0f4e04408f79fe44a27e24 1650w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=2500&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=04e456c78c228ffce56687841de69b52 2500w" />

<Note>The downloaded zip file contains your agent's UI components and blueprints in a hidden folder called `.wf`. If the zip file appears to only contain generic starter files, check for the `.wf` folder which contains the internal configuration files for your agent.</Note>

### Step 2: Create local project

Create a new local project with Writer Framework and import the cloud agent by unzipping the export file you downloaded:

```bash  theme={null}
# Create a new local project
writer create my-cloud-agent
cd my-cloud-agent
```

### Step 3: Import the cloud agent into your local project

Import the cloud agent by unzipping the export file you downloaded into your local project:

```bash  theme={null}
# The export file contains all your agent's configuration from the web editor
unzip your-agent-export.zip
```

<Tip>If you don't see the import/export agent functionality in your local development environment, make sure you're running the latest version of Writer Framework. Run `pip install --upgrade writer` to get the latest version with all features.</Tip>

Because the export file contains all your agent's configuration, the terminal asks you to confirm file-by-file whether you'd like to overwrite your local project's files.

Type `A` to replace all files in your local project with the exported agent.

You can also choose the following options:

* `y` to replace an individual file
* `r` to rename an individual file
* `N` to cancel the import and not replace any files

```bash  theme={null}
my-agent unzip ~/Downloads/export.zip
Archive:  /Users/Downloads/export.zip
  inflating: README.md
replace main.py? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
```

### Step 4: Set up environment variables

Set up a `.env` file in your local project directory and add your Writer API key:

```bash  theme={null}
# .env
export WRITER_API_KEY="[your_api_key]"
```

Run the following command to activate the environment variables:

```bash  theme={null}
source .env
```

### Step 5: Start local development

Start the local development server:

```bash  theme={null}
writer edit .
```

Your local environment now contains an exact copy of your cloud agent, and you can continue development locally.

## Local to cloud workflow

To start development locally and then push to the cloud development environment, follow these steps:

### Step 1: Create local project

Start with a local project:

```bash  theme={null}
writer create my-local-agent
cd my-local-agent
writer edit .
```

### Step 2: Develop locally

Build your agent locally using the Writer Framework development environment. You have full access to:

* Python code editing
* UI component configuration
* Blueprint design
* Local testing and debugging

### Step 3: Prepare for cloud sync

Before syncing to the cloud, ensure your code handles both Vault and environment variables as described in the [handle environment variables and secrets](#handle-environment-variables-and-secrets) section.

<Warning>Remove or move your `.env` file before syncing to prevent it from showing in the cloud editor.</Warning>

### Step 4: Download the local agent's export file

When you're ready to sync your local agent to the cloud, download the local agent's export file from the web editor.

In the visual editor interface, click the three dots in the top right corner of your agent and select **Download agent .zip file** to download a `.zip` file containing your agent's configuration.

<img src="https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=89922197cb60c38a2f1e74d210eaef29" alt="" data-og-width="468" width="468" data-og-height="260" height="260" data-path="images/agent-builder/export-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=280&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=6db01e6c16c3816705ac3a3e12e7058c 280w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=560&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=3e94fc65d17bffa63c6c90219b429f50 560w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=840&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=e149d947ccb465cec113a4c2f20efdc1 840w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=1100&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=a0e3f5276f5a6fab90b59e44b611a603 1100w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=1650&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=1fd4420c9b0f4e04408f79fe44a27e24 1650w, https://mintcdn.com/writer/L16Zd2tduYwpqh6w/images/agent-builder/export-agent.png?w=2500&fit=max&auto=format&n=L16Zd2tduYwpqh6w&q=85&s=04e456c78c228ffce56687841de69b52 2500w" />

<Tip>If you don't see the import/export agent functionality in your local development environment, make sure you're running the latest version of Writer Framework. Run `pip install --upgrade writer` to get the latest version with all features.</Tip>

The export file includes all files in your local project, including a hidden `.wf` folder that contains your UI components and blueprints as internal JSON files. Don't include sensitive information in the exported file because it is visible in the cloud editor.

### Step 5: Import the local agent into your cloud project

Open the Agent Builder web editor in AI Studio and click the three dots in the top right corner of your agent. Then select **Import agent .zip file** to upload the local agent's export file.

A modal appears and asks you to confirm that you are overwriting your existing agent.

<img src="https://mintcdn.com/writer/D6F1U8ssbbBGA470/images/agent-builder/overwrite-agent.png?fit=max&auto=format&n=D6F1U8ssbbBGA470&q=85&s=9a20868e4eaba52adef471895c896984" alt="" data-og-width="1946" width="1946" data-og-height="640" height="640" data-path="images/agent-builder/overwrite-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/D6F1U8ssbbBGA470/images/agent-builder/overwrite-agent.png?w=280&fit=max&auto=format&n=D6F1U8ssbbBGA470&q=85&s=e3397608ac70817b5aff681084d90b32 280w, https://mintcdn.com/writer/D6F1U8ssbbBGA470/images/agent-builder/overwrite-agent.png?w=560&fit=max&auto=format&n=D6F1U8ssbbBGA470&q=85&s=51f5a4d1f437cbdf69ef533ab1d630dc 560w, https://mintcdn.com/writer/D6F1U8ssbbBGA470/images/agent-builder/overwrite-agent.png?w=840&fit=max&auto=format&n=D6F1U8ssbbBGA470&q=85&s=991c64fef70d459d932e7b5f344d4c5b 840w, https://mintcdn.com/writer/D6F1U8ssbbBGA470/images/agent-builder/overwrite-agent.png?w=1100&fit=max&auto=format&n=D6F1U8ssbbBGA470&q=85&s=c7d4de643a65fcf4223f8d3171e4df32 1100w, https://mintcdn.com/writer/D6F1U8ssbbBGA470/images/agent-builder/overwrite-agent.png?w=1650&fit=max&auto=format&n=D6F1U8ssbbBGA470&q=85&s=240d332f08b3754e307b02e652858a7e 1650w, https://mintcdn.com/writer/D6F1U8ssbbBGA470/images/agent-builder/overwrite-agent.png?w=2500&fit=max&auto=format&n=D6F1U8ssbbBGA470&q=85&s=a5470b37438a3caddd8dce0c6e118fd1 2500w" />

Check the box to acknowledge that you're replacing your existing agent and click **Import** to continue.

## Deploy your agent

After syncing your agent to the cloud, deploy it following the [standard cloud workflow](/agent-builder/quickstart#deploy-the-agent).

From the agent editor interface in Agent Builder, click **Configure deployment** in the top right corner of the Agent Builder interface. You can also access the deployment configuration by going to the [AI Studio homepage](https://app.writer.com/aistudio) and selecting the agent you created.

If the agent isn't deployed, you see a toggle bar that says **Draft**.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d5bb311eb3357a77ba67a5268a79b711" alt="" data-og-width="1280" width="1280" data-og-height="266" height="266" data-path="images/agent-builder/not-deployed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=81fbd0401e689b9f764c3deb4eaae769 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=aa9351ab6eee77f041bae7926c231c16 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=edcebe62cdb6c3de4c0630789fc25dd4 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c38132de7e6a8ae3f37002ceab6dd42c 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=773cedd074e71f6663243e2187cc3283 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bab6ed2f764bae8a1f102a49a1b2e2b1 2500w" />

To deploy the agent, toggle the bar. Writer deploys the agent to the Writer cloud, which takes a moment to complete.

When you deploy the agent, the toggle bar shows **Deployed**. It also shows a list of the teams in your organization, which you can use to grant access to the agent. You must select at least one team before you can view the URL for the deployed agent.

## Considerations for dual-environment development

* **Local-only libraries**: If you install Python packages locally that aren't listed in [Python libraries installed in Agent Builder](/agent-builder/python-libraries), your agent won't run in the cloud version of Agent Builder because those packages aren't available there.

* **Environment file visibility**: Your `.env` file is visible in plain text in the cloud editor when you sync your local project. Any file you add to your local project is included in the export file to the cloud. Before syncing, move your `.env` file to a different location or delete it to prevent it from showing in the cloud editor, and add your secrets to Vault.

* **Vault availability**: Vault is only available in the cloud version of Agent Builder. For local development, you must use environment variables. Structure your code to handle both scenarios gracefully.

* **Keep your local Writer Framework package up to date**: When you sync your agent to the cloud, the cloud version of Agent Builder uses the latest version of the Writer Framework package. If you're using a different version of the Writer Framework package in your local project, you might encounter errors when you sync to the cloud. To avoid this, keep your local Writer Framework package up to date by running the following command:

```bash  theme={null}
pip install --upgrade writer
```

### Handle environment variables and secrets

The following code shows an example of how to look for secrets in Vault first, then fall back to environment variables:

```python  theme={null}
import os

def get_secret(key, default=None):
    """Get a secret from Vault if available, otherwise from environment variables"""
    try:
        # Try to get from Vault first (cloud environment). The `vault` object is available in Python code blocks and in event handlers.
        return vault[key]
    except KeyError:
        # Fall back to environment variables (local development)
        return os.getenv(key, default)

# Usage example
api_key = get_secret("WRITER_API_KEY", "default_key")
database_url = get_secret("DATABASE_URL")
```

## Next steps

* Learn about [local development](/agent-builder/local-development) workflows
* Understand how to [deploy your agent](#deploy-your-agent) from the cloud
* Explore [custom Python code](/agent-builder/python-code) for advanced functionality

<feedback />
