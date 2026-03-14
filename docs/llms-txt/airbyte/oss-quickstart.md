# Source: https://docs.airbyte.com/platform/using-airbyte/getting-started/oss-quickstart.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/getting-started/oss-quickstart.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/getting-started/oss-quickstart.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/getting-started/oss-quickstart.md

# Source: https://docs.airbyte.com/platform/1.6/using-airbyte/getting-started/oss-quickstart.md

# Quickstart

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

This quickstart guides you through deploying a local instance of Airbyte Self-Managed Community, Airbyte's open source product. Setup only takes a few minutes, and you can start moving data immediately.

## Overview[​](#overview "Direct link to Overview")

This quickstart is for most people who want to manage their own Airbyte instance. It assumes you have basic knowledge of command-line tools. It's also helpful, but not necessary, to understand the basics of Docker.

This quickstart shows you how to:

* [Install Docker Desktop](#part-1-install-docker-desktop)
* [Install abctl](#part-2-install-abctl)
* [Run Airbyte](#part-3-run-airbyte)
* [Set up authentication](#part-4-set-up-authentication)
* [Decide on your next steps](#whats-next)

If you don't want to self-manage Airbyte, skip this guide. Sign up for an [Airbyte Cloud](https://cloud.airbyte.com/signup) trial and [start syncing data](/platform/1.6/using-airbyte/getting-started/add-a-source.md) now.

If you want to use Python to move data, Airbyte's Python library, [PyAirbyte](/platform/1.6/using-airbyte/pyairbyte/getting-started.md), might be the best fit for you. It's a good choice if you're using Jupyter Notebook or iterating on an early prototype for a large data project and don't need to run your own server.

## Suggested resources[​](#suggested-resources "Direct link to Suggested resources")

For best performance, run Airbyte on a machine with 4 or more CPUs and at least 8-GB of memory. Airbyte also runs with 2 CPUs and 8-GB of memory in low-resource mode. This guide explains how to do both. Follow this [Github discussion](https://github.com/airbytehq/airbyte/discussions/44391) to up-vote and track progress toward supporting lower resource environments.

## Part 1: Install Docker Desktop[​](#part-1-install-docker-desktop "Direct link to Part 1: Install Docker Desktop")

Install Docker Desktop on your machine, if you haven't already. Follow the steps for your operating system in Docker's online help, linked below.

* [Mac](https://docs.docker.com/desktop/install/mac-install/)
* [Windows](https://docs.docker.com/desktop/install/windows-install/)
* [Linux](https://docs.docker.com/desktop/install/linux-install/)

You don't need to do anything with Docker, but you do need to run it in the background. Once it's open, minimize it and proceed to Part 2.

Why do you need Docker?

Airbyte runs on Kubernetes. When you deploy Airbyte locally, it uses Docker to create a Kubernetes cluster on your computer.

For best performance, run Airbyte on a machine with 4 or more CPUs and at least 8-GB of memory. We also support running Airbyte with 2 CPUs and 8-GB of memory in low-resource mode. This guide explains how to do both. Follow this [Github discussion](https://github.com/airbytehq/airbyte/discussions/44391) to upvote and track progress toward supporting lower resource environments.

## Part 2: Install abctl[​](#part-2-install-abctl "Direct link to Part 2: Install abctl")

abctl is Airbyte's command-line tool for deploying and managing Airbyte.

### Install abctl the fast way (Mac, Linux)[​](#install-abctl-the-fast-way-mac-linux "Direct link to Install abctl the fast way (Mac, Linux)")

This is the best way to get abctl, but this method doesn't work on Windows.

1. Open a terminal and run the following command.

   ```
   curl -LsfS https://get.airbyte.com | bash -
   ```

2. If your terminal asks you to enter your password, do so.

When installation completes, you see `abctl install succeeded.`

### Install abctl manually (Mac, Linux, Windows)[​](#install-abctl-manually-mac-linux-windows "Direct link to Install abctl manually (Mac, Linux, Windows)")

To install abctl yourself, follow the instructions for your operating system.

* Mac
* Linux
* Windows

Use [Homebrew](https://brew.sh/) to install abctl.

1. Install Homebrew, if you haven't already.

2. Run the following commands after you install Homebrew.

   ```
   brew tap airbytehq/tap
   brew install abctl
   ```

3. Keep abctl up to date with Homebrew, too.

   ```
   brew upgrade abctl
   ```

1) Verify your processor architecture.

   ```
   uname -m
   ```

   If the output is `x86_64`, you'll download the **linux-amd64** release. If the output is `aarch64` or similar, you'll download the **linux-arm64** release.

2) Download the file that is compatible with your machine's processor architecture

   [Latest Linux Release](https://github.com/airbytehq/abctl/releases/latest)

3) Extract the archive. This creates a directory named `abctl`, which contains the executable and other needed files.

   ```
   tar -xvzf {name-of-file-downloaded.linux-*.tar.gz}
   ```

4) Make the extracted executable accessible. This allows you to run `abctl` as a command.

   ```
   chmod +x abctl/abctl
   ```

5) Add `abctl` to your PATH. This allows you to run `abctl` from any directory in your terminal.

   ```
   sudo mv abctl /usr/local/bin
   ```

6) Verify the installation. If this command prints the installed version of abctl, you can now use it to manage a local Airbyte instance.

   ```
   abctl version
   ```

1. Verify your processor architecture.

   1. Press ` Windows` + `I`.

   2. Click **System** > **About**.

   3. Next to **Processor**, if it says `AMD`, you'll download the **windows-amd64** release. If the output is `ARM` or similar, you'll download the **windows-arm64** release.

2. Download the latest release of `abctl`.

   [Latest Windows Release](https://github.com/airbytehq/abctl/releases/latest)

3. Extract the zip file to a destination of your choice. This creates a folder containing the abctl executable and other required files. Copy the filepath because you'll need this in a moment.

4. Add the executable to your `Path` environment variable.

   1. Click  **Start** and type `environment`.

   2. Click **Edit the system environment variables**. The System Properties opens.

   3. Click **Environment Variables**.

   4. Find the Path variable and click **Edit**.

   5. Click **New**, then paste the file path you saved in step 3.

   6. Click **OK**, then click **OK**, then close the System Properties.

5. Open a new Command Prompt or PowerShell window. Changes to your Path variable only take effect in a new Window.

6. Verify abctl is installed correctly. If this command prints the installed version of abctl, you can now use it to manage a local Airbyte instance.

   ```
   abctl version
   ```

## Part 3: Run Airbyte[​](#part-3-run-airbyte "Direct link to Part 3: Run Airbyte")

1. Open Docker Desktop, [which you installed previously](#part-1-install-docker-desktop).

2. Install Airbyte. To do this, open a terminal and run the following command.

   ```
   abctl local install
   ```

   To run Airbyte in a low-resource environment (fewer than 4 CPUs), specify the `--low-resource-mode` flag to the local install command.

   ```
   abctl local install --low-resource-mode
   ```

   note

   If you see the warning `Encountered an issue deploying Airbyte` with the message `Readiness probe failed: HTTP probe failed with statuscode: 503`, allow installation to continue. You may need to allocate more resources for Airbyte, but installation can complete anyway. See [Suggested resources](#suggested-resources).

   Installation may take up to 30 minutes depending on your internet connection. When it completes, your Airbyte instance opens in your web browser at <http://localhost:8000>. As long as Docker Desktop is running in the background, use Airbyte by returning to <http://localhost:8000>. If you quit Docker Desktop and want to return to Airbyte, start Docker Desktop again. Once your containers are running, you can access Airbyte normally.

3. Enter your **Email** and **Organization name**, then click **Get Started**.

Airbyte asks you to log in with a password, but you don't have one yet. Proceed to Part 4 to get one.

## Part 4: Set up authentication[​](#part-4-set-up-authentication "Direct link to Part 4: Set up authentication")

To access your Airbyte instance, you need a password.

1. Get your default password.

   ```
   abctl local credentials
   ```

   This outputs something like this:

   ```
   Credentials:
   Email: user@example.com
   Password: a-random-password
   Client-Id: 03ef466c-5558-4ca5-856b-4960ba7c161b
   Client-Secret: m2UjnDO4iyBQ3IsRiy5GG3LaZWP6xs9I
   ```

2. Return to your browser and use that password to log into Airbyte.

3. Optional: Since you probably want to set your own password, you can change it any time.

   ```
   abctl local credentials --password YourStrongPasswordExample
   ```

   Your Airbyte server restarts. Once it finishes, use your new password to log into Airbyte again.

## What's next[​](#whats-next "Direct link to What's next")

Congratulations! You have a fully functional instance of Airbyte running locally.

### Move data[​](#move-data "Direct link to Move data")

In Airbyte, you move data from [sources](/platform/1.6/using-airbyte/getting-started/add-a-source.md) to [destinations](/platform/1.6/using-airbyte/getting-started/add-a-destination.md). The relationship between a source and a destination is called a [connection](/platform/1.6/using-airbyte/getting-started/set-up-a-connection.md). Try moving some data on your local instance.

### Deploy Airbyte[​](#deploy-airbyte "Direct link to Deploy Airbyte")

If you want to scale data movement in your organization, you probably need to move Airbyte off your local machine. You can deploy to a cloud provider like AWS, Google Cloud, or Azure. You can also use a single node like an AWS EC2 virtual machine. See the [deployment guide](/platform/1.6/deploying-airbyte/.md) to learn more.

## Uninstall Airbyte[​](#uninstall-airbyte "Direct link to Uninstall Airbyte")

To stop running all containers, but keep your data:

```
abctl local uninstall
```

To stop running containers and delete all data:

1. Uninstall Airbyte with the `--persisted` flag.

   ```
   abctl local uninstall --persisted
   ```

2. Clear any remaining information abctl created.

   ```
   rm -rf ~/.airbyte/abctl
   ```
