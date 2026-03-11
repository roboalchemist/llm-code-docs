# Source: https://docs-containers.back4app.com/docs/local-development/parse-cli.md

---
title: Command Line Interface Setup
slug: docs/local-development/parse-cli
description: In this guide you learn how to install and use the CLI tool
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-25T15:38:03.681Z
updatedAt: 2026-01-23T12:10:48.867Z
---

The Back4app Command Line Interface (CLI) is a powerful tool for managing apps, deploying code, and handling cloud functions directly from your terminal. This guide will walk you through installation, configuration, and key features to get you started.

## **What You Can Do With Back4app CLI**

- Create and manage Back4app applications.
- Deploy Cloud Code Functions and other local files.
- Manage app versions and releases.
- Deploy web applications.
- Install and manage NPM modules.

## 1  - Installation

### Prerequisites

:::hint{type="info"}
- A Back4app account. [**Sign up here**](https://www.back4app.com).
- Python on your machine.
:::

### **For macOS and Linux**

**Option 1: Install via Script**

1. Open your terminal and run:

:::BlockQuote
curl https\://raw\.githubusercontent.com/back4app/parse-cli/back4app/installer.sh | sudo /bin/bash
:::

&#x20;   2\.  The tool will be installed as `b4a` in `/usr/local/bin/b4a.`

**Option 2: Manual Installation**

1. Check your system's architecture by running:

:::BlockQuote
*uname -pm*
:::

&#x20;   2\.  Download the correct executable for your system from [**this repository**](https://github.com/back4app/parse-cli/blob/back4app/installer.sh).

&#x20;   3\.  Move the downloaded file to `/usr/local/bin/`:

:::BlockQuote
mv \<downloaded\_file> /usr/local/bin/b4a
chmod 755 /usr/local/bin/b4a
:::

&#x20;   4\.  The CLI is now ready to use.

### **For Windows**

- Download the [**b4a.exe**](https://github.com/back4app/parse-cli/releases/download/release_3.3.1/b4a.exe) file from the [**releases page**](https://github.com/back4app/parse-cli/releases).
- Move the file to `C:\Windows\System32` to make it accessible globally.2 - Configuration

### **Connect CLI to Your Back4app account**

1. Log into your Back4app account.
2. Generate an account key:
   - Hover over the "Hello, \[username]" menu.
   - Go to **Account Keys** and create a new key.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Vtf9h_neBfwWz0MOTYGb8_screenshot-2024-11-28-at-164118.png)

&#x20;   3\.  Configure the key in the CLI:

:::BlockQuote
b4a configure accountkey
:::

Paste your account key when prompted.

:::hint{type="danger"}
This command will only work for the **first time&#x20;**&#x79;ou do this setup on a specific computer. Otherwise, run b4a configure accountkey -d to overwrite your old key with a new one.
:::

The account keys you’ve used are stored in $\{HOME}/.back4app/netrc for Mac and Linux.

## 3 - Usage

### **Create a New App**

1. Open the terminal and run: `b4a new`
2. Select "(n)ew" to create a new app.
3. Follow the prompts to name and set up your app.

### **Deploy Cloud Functions**

1. Create your local Cloud Code file, e.g., `main.js`:

```javascript
Parse.Cloud.define("hello", (request) => {
  return "Hello, world!";
});
```

&#x20;   2\.  Deploy the code:

:::BlockQuote
b4a deploy
:::

The CLI will upload your `cloud` and `public` folders to Back4app.

### **Other Useful Commands**

| Command      | Description                               |
| ------------ | ----------------------------------------- |
| b4a list     | List all apps connected to your account.  |
| b4a deploy   | Deploy Cloud Code and hosting files.      |
| b4a releases | Gets the releases for an app.             |
| b4a rollback | Rolls back the version for the given app. |

Run `b4a help` for a full list of commands.

## 4 -**&#x20;Troubleshooting**

### **Common Issues**

- **Permission Errors**: Use `sudo` for Linux/Mac installations or ensure the Windows executable is in the correct directory.
- **Connection Problems**: Verify your account key configuration by re-running `b4a configure accountkey`.
- **Deployment Errors**: Check the `.parse.local` and `.parse.project` files for correct configuration.

## 5 -**&#x20;Next Steps**

- Experiment with Cloud Code by writing custom functions.
- Explore the [**local Parse Server environment**](https://www.back4app.com/docs/local-development/parse-server-local) for offline development.

## **Conclusion**

With the Back4app CLI, you can efficiently manage your applications, deploy updates, and leverage powerful Cloud Code functions. Follow this guide to get started and explore the full potential of Back4app's CLI tool.
