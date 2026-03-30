# Source: https://docs-containers.back4app.com/docs/cicd-setup.md

---
title: CI/CD Setup
slug: docs/cicd-setup
createdAt: 2026-01-26T17:19:37.310Z
updatedAt: 2026-01-28T14:15:07.175Z
---

Welcome! This guide will help you set up automatic deployment for your Back4App project. When you're done, pushing code to GitHub will automatically update your Back4App app.

**No prior experience with GitHub Actions is required.**

***

## Table of Contents

1. [**What Does This Do?**](./#what-does-this-do)
2. [**What You'll Need**](./#what-youll-need)
3. [**Step 1: Clone Your Repository**](./#step-1-clone-your-repository)
4. [**Step 2: Set Up Back4App CLI and Project Structure**](./#step-2-set-up-back4app-cli-and-project-structure)
5. [**Step 3: Find Your Back4App App IDs**](./#step-3-find-your-back4app-app-ids)
6. [**Step 4: Edit the Workflow File**](./#step-4-edit-the-workflow-file)
7. [**Step 5: Add Your Secrets to GitHub**](./#step-5-add-your-secrets-to-github)
8. [**Step 6: Create Your Branches**](./#step-6-create-your-branches)
9. [**Step 7: Deploy!**](./#step-7-deploy)
10. [**How to Use It Daily**](./#how-to-use-it-daily)
11. [**Troubleshooting**](./#troubleshooting)
12. [**Glossary**](./#glossary)

***

## ⚠️⚠️⚠️ VERY IMPORTANT ⚠️⚠️⚠️

Though flexible and configurable, this Continuous Integration and Continuous Delivery (CI/CD) project is aimed at running Back4app Backend as a Service (BaaS) projects **ONLY**.

You might change it and adapt it to your specific needs, using this as a template, but have in mind that it does many checkings on Back4app's BaaS folders, files and settings, so ensure to adapt accordingly.

A few of those checks include:

```text
  - A configured Back4app Backend as a Service project, which you can obtain by using the Back4app Command Line Interface tool (CLI): https://www.back4app.com/docs/local-development/parse-cli
```

***

## What Does This Do?

This workflow automatically uploads your code to Back4App whenever you push changes to GitHub.

**Here's how it works:**

```none
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│  You push code  │   →→→   │  GitHub Actions │   →→→   │  Back4App app   │
│  to GitHub      │         │  runs workflow  │         │  is updated     │
└─────────────────┘         └─────────────────┘         └─────────────────┘
```

**Two distinct branches:**

| When you push to...  | Your code goes to...                     |
| -------------------- | ---------------------------------------- |
| `development` branch | Development Back4App app (for testing)   |
| `main` branch        | Production Back4App app (for real users) |

This lets you test changes safely before releasing them to your users.

:::BlockQuote
⚠️⚠️⚠️ **Tip:** In order for this flow to work as it is, the branches **MUST** be named like above. ⚠️⚠️⚠️
:::

***

## What You'll Need

Before starting, make sure you have:

- [ ] A GitHub account with:
- [ ] A Repository created for your App
- [ ] Two branches named exactly `development` and `main`
- [ ] A Back4App account
- [ ] **Two Back4App apps created:**
- [ ] One for Development (development and testing)
- [ ] One for Production (live/real users)
- [ ] Your project code in a GitHub repository
- [ ] A code editor (like VS Code, Cursor, or even GitHub's web editor)

:::BlockQuote
⚠️ **Important:** The branch names must be exactly `development` and `main` for this workflow to work as is!
:::

### Don't have two Back4App apps yet?

You'll need to create them first:

1. Log into Back4App
2. Click the **"New App"** button on the top right side
3. Create your first app and name it something like "DevelopmentApp"
4. Create your second app and name it something like "ProductionApp"

:::BlockQuote
💡 **Tip:** Keep the names simple so you can tell them apart easily.
:::

***

## Step 1: Clone Your Repository

Before you can add files to your project, you need to download (clone) your GitHub repository to your computer.

### 1.1 Find your repository URL

1. **Go to your repository on GitHub**
   - Open your web browser
   - Go to `github.com/YOUR-USERNAME/YOUR-REPO-NAME`
2. **Click the green "Code" button**
   - It's near the top right of the file list
3. **Copy the URL**
   - Make sure "HTTPS" is selected (it's the default)
   - Click the 📋 copy button next to the URL
   - The URL looks like: `https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git`

### 1.2 Clone the repository to your computer

🍎 **macOS**

1. **Open Terminal**
   - Press `Cmd + Space` to open Spotlight
   - Type "Terminal"
   - Press Enter
2. **Navigate to where you want to store your project**

```bash
# Go to your Documents folder (or wherever you want to work)
cd ~/Documents
```

1. **Clone the repository**

```bash
# Replace the URL with your actual repository URL
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

1. **Enter the project folder**

```bash
# Replace YOUR-REPO-NAME with your actual repository name
cd YOUR-REPO-NAME
```



🐧 **Linux**

1. **Open your terminal**
2. **Navigate to where you want to store your project**

```bash
# Go to your home folder (or wherever you want to work)
cd ~
```

1. **Clone the repository**

```bash
# Replace the URL with your actual repository URL
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

1. **Enter the project folder**

```bash
# Replace YOUR-REPO-NAME with your actual repository name
cd YOUR-REPO-NAME
```



🪟 **Windows (PowerShell)**

1. **Open PowerShell**
   - Press `Win + X`
   - Select "Windows PowerShell"
2. **Navigate to where you want to store your project**

```powershell
# Go to your Documents folder (or wherever you want to work)
cd ~\Documents
```

1. **Clone the repository**

```powershell
# Replace the URL with your actual repository URL
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

1. **Enter the project folder**

```powershell
# Replace YOUR-REPO-NAME with your actual repository name
cd YOUR-REPO-NAME
```



🪟 **Windows (Command Prompt)**

1. **Open Command Prompt**
   - Press `Win + R`
   - Type "cmd"
   - Press Enter
2. **Navigate to where you want to store your project**

```cmd
REM Go to your Documents folder (or wherever you want)
cd %USERPROFILE%\Documents
```

1. **Clone the repository**

```cmd
REM Replace the URL with your actual repository URL
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

1. **Enter the project folder**

```cmd
REM Replace YOUR-REPO-NAME with your actual repository name
cd YOUR-REPO-NAME
```



🪟 **Windows (Git Bash)**

If you installed Git for Windows, you have Git Bash which works like macOS/Linux:

1. **Open Git Bash**
   - Right-click on your Desktop or in a folder
   - Select "Git Bash Here"
2. **Navigate to where you want to store your project**

```bash
# Go to your Documents folder (or wherever you want)
cd ~/Documents
```

1. **Clone the repository**

```bash
# Replace the URL with your actual repository URL
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

1. **Enter the project folder**

```bash
# Replace YOUR-REPO-NAME with your actual repository name
cd YOUR-REPO-NAME
```



### 1.3 Verify the clone worked

After cloning, you should see your project files. Run this command to check:

```bash
ls -la
```

On Windows Command Prompt, use:

```cmd
dir
```

You should see your project files listed, including any existing files from your repository.

### 1.4 Open the project in your code editor

📝 **VS Code or Cursor**

**Option A: From the terminal**

```bash
# Opens VS Code in current folder
code .

# Opens Cursor in current folder
cursor .
```

**Option B: From the application**

1. Open VS Code or Cursor
2. Click **File** → **Open Folder**
3. Navigate to your project folder
4. Click **Open**



📝 **Other editors**

1. Open your code editor
2. Look for **File** → **Open** or **File** → **Open Folder**
3. Navigate to the folder where you cloned your repository
4. Open it



:::BlockQuote
✅ **Success!** You now have a local copy of your repository. Any changes you make here can be pushed back to GitHub.
:::

***

## Step 2: Set Up Back4App CLI and Project Structure

Before adding the workflow file, you need to set up the Back4App Command Line Interface (CLI) and connect it to your Back4App apps. This will create the necessary `cloud` folder structure in your project.

:::BlockQuote
📖 **Official Documentation:** [**Back4App CLI Setup Guide**](https://www.back4app.com/docs/local-development/parse-cli)
:::

### 2.1 Install the Back4App CLI

The CLI lets you manage your Back4App apps from your terminal.

🍎 **macOS**

**Prerequisites:** You need Python installed on your Mac (it usually comes pre-installed).

1. **Open Terminal** (press `Cmd + Space`, type "Terminal", press Enter)
2. **Run the installation command:**

```bash
curl https://raw.githubusercontent.com/back4app/parse-cli/back4app/installer.sh | sudo /bin/bash
```

1. **Enter your password** when prompted (you won't see characters as you type - that's normal)
2. **Verify the installation:**

```bash
b4a --version
```

1. You should see a version number.



🐧 **Linux**

**Prerequisites:** You need Python installed.

1. **Open your terminal**
2. **Run the installation command:**

```bash
curl https://raw.githubusercontent.com/back4app/parse-cli/back4app/installer.sh | sudo /bin/bash
```

1. **Enter your password** when prompted
2. **Verify the installation:**

```bash
b4a --version
```



🪟 **Windows**

1. **Download the CLI executable:**
   - Go to: [**https://github.com/back4app/parse-cli/releases**](https://github.com/back4app/parse-cli/releases)
   - Download the file named `b4a.exe`
2. **Move the file to make it accessible globally:**
   - Move `b4a.exe` to `C:\Windows\System32\`
   - (You may need administrator permission)
3. **Verify the installation:**
   - Open Command Prompt or PowerShell
   - Run:

```cmd
b4a --version
```



### 2.2 Get Your Back4App Account Key

You need an Account Key to connect the CLI to your Back4App account.

1. **Log into Back4App** at back4app.com
2. **Click on your profile icon** (top-right corner of the dashboard)
3. **Look for "Account Keys"** in the menu
4. **Give your Account Key a name** and click the **"+"** button on the right side
5. **A new Account Key will be created** - Copy your new key immediately

:::BlockQuote
⚠️ **Important:** Keep your Account Key secret! Never share it or commit it to your repository.
:::

Write it down somewhere safe:

```none
My Account Key: ________________________________
```

### 2.3 Configure the CLI with Your Account Key

Now connect the CLI to your Back4App account.

1. **Open your terminal** and navigate to your project folder:

```bash
cd /path/to/your-project
```

1. **Run the configuration command:**

```bash
b4a configure accountkey
```

1. **Paste your Account Key** when prompted and press Enter

:::BlockQuote
💡 **Note:** If you've configured a key before and need to update it, use:
:::

```bash
b4a configure accountkey -d
```

### 2.4 Link Your Back4App App to Your Local Project

This step creates the Back4App cloud code structure inside your cloned repository.

:::BlockQuote
⚠️ **Important:** Run this command **inside your cloned repository folder** (from Step 1). This ensures the Back4App files are added to your git-tracked project!
:::

1. **Make sure you're in your cloned repository folder:**

```bash
# Navigate to your cloned repo (the folder from Step 1)
cd ~/Documents/YOUR-REPO-NAME

# Verify you're in the right place (should show .git folder)
ls -la
```

1. **Run the new app command:**

```bash
b4a new
```

1. **When prompted, choose to link an existing app:**
   - You'll see options like `(n)ew` or `(e)xisting`
   - Type `e` and press Enter to link an existing app
2. **Select your DEVELOPMENT app** from the list
   - Use the project's number to choose
   - Press Enter to select
3. **When asked for "Directory Name:"**
   - Just press **Enter** to accept the default (uses your app name)
   - Or type a simple name like `app` and press Enter
   - The CLI will create a subfolder with this name
4. **When asked about blank project:**

```none
Please type "(b)lank" if you wish to setup a blank project, otherwise press ENTER:
```

:::Paragraph{listStyleType="disc" indent="2"}
Just press **Enter** to get the default template with sample files
:::

1. **The CLI creates the files in a subfolder:**

```none
your-project/                ← Your cloned repo
├── .git/                    ← Already exists from Step 1
└── MyApp/                   ← Subfolder created by CLI (name may vary)
    ├── cloud/
    │   └── main.js
    ├── public/
    │   └── index.html
    ├── .parse.local
    └── .parse.project
```

### 2.4.1 Move Files to Repository Root

The workflow expects the `cloud` folder to be in the **root** of your repository, not in a subfolder.

**Follow these steps:**

**Step A:** First, find out what the subfolder is called:

```bash
ls
```

You'll see something like:

```none
MyApp
```

(The name will be whatever your Back4App app is called)

**Step B:** Run these 4 commands one by one, replacing `MyApp` with the name you saw above:

🍎 **macOS / 🐧 Linux / Git Bash**

```bash
mv MyApp/* .
```

```bash
mv MyApp/.parse.local .
```

```bash
mv MyApp/.parse.project .
```

```bash
rmdir MyApp
```



🪟 **Windows (PowerShell)**

```powershell
Move-Item -Path "MyApp\*" -Destination "."
```

```powershell
Move-Item -Path "MyApp\.parse.local" -Destination "."
```

```powershell
Move-Item -Path "MyApp\.parse.project" -Destination "."
```

```powershell
Remove-Item -Path "MyApp"
```



🪟 **Windows (Command Prompt)**

```cmd
move MyApp\* .
```

```cmd
move MyApp\.parse.local .
```

```cmd
move MyApp\.parse.project .
```

```cmd
rmdir MyApp
```



**Step C:** Verify it worked:

```bash
ls -la
```

You should see `cloud/` and `public/` folders in the root (not inside a subfolder).

8. **After moving, your repository should look like this:**

```javascript
your-project/                ← Your cloned repo
├── .git/                    ← Git directory (from Step 1)
├── cloud/
│   └── main.js              ← Your Cloud Code goes here
├── public/
│   └── index.html           ← Optional: web hosting files
├── .parse.local             ← App configuration
└── .parse.project           ← Project configuration
```

:::BlockQuote
⚠️ **Important:** The `cloud/main.js` file is where your Cloud Code lives. This is what gets deployed to Back4App!
:::

### 2.5 Create the GitHub Workflows Folder

Now add the folder for GitHub Actions.

:::BlockQuote
⚠️ **Important:** Make sure you are **inside your cloned repository folder** (from Step 1). This folder already contains the `.git` directory which is essential for pushing code to GitHub!
:::

🍎 **macOS / 🐧 Linux**

```bash
# You should already be in your cloned repo folder from Step 1
# If not, navigate to it:
cd ~/Documents/YOUR-REPO-NAME

# Verify you're in a git repository (should show your branch name)
git status

# Create the workflows folder
mkdir -p .github/workflows
```



🪟 **Windows (PowerShell)**

```powershell
# You should already be in your cloned repo folder from Step 1
# If not, navigate to it:
cd ~\Documents\YOUR-REPO-NAME

# Verify you're in a git repository (should show your branch name)
git status

# Create the workflows folder
New-Item -ItemType Directory -Force -Path ".github\workflows"
```



🪟 **Windows (Command Prompt)**

```cmd
REM You should already be in your cloned repo folder from Step 1
REM If not, navigate to it:
cd %USERPROFILE%\Documents\YOUR-REPO-NAME

REM Verify you're in a git repository (should show your branch name)
git status

REM Create the workflows folder
mkdir .github\workflows
```



📝 **Using VS Code or Cursor**

1. Open your **cloned repository folder** in VS Code or Cursor (the one from Step 1)
2. In the Explorer sidebar (left panel), right-click on empty space
3. Select **"New Folder"**
4. Name it `.github` (yes, with the dot at the beginning)
5. Right-click on the `.github` folder
6. Select **"New Folder"**
7. Name it `workflows`



### 2.6 Add the Workflow File

Download the the `simpleDeploy.yaml` file from here:&#x20;

::File[]{src="https://api.archbee.com/api/presign/yD3zCY-NNBBIfd0uqcfR5/4lNWwggzw4zAm1jre-6JU-20260126-174946.yaml" label="simpleDeploy.yaml"}

&#x20;and copy it into the `.github/workflows/` folder.

### 2.7 Verify Your Project Structure

After completing this step, your **cloned repository** should look like this:

```none
your-project/                    ← This is your cloned repo folder
├── .git/                        ← Git directory (ESSENTIAL - created when you cloned)
├── .github/
│   └── workflows/
│       └── simpleDeploy.yaml    ← The deployment workflow
├── cloud/
│   └── main.js                  ← Your Cloud Code
├── public/                      ← (Optional) Web hosting files
│   └── index.html
├── .parse.local                 ← Back4App app config
├── .parse.project               ← Back4App project config
└── ... (your other files)
```

:::BlockQuote
📁 **Workflow file location:** `.github/workflows/simpleDeploy.yaml`
:::

::::BlockQuote
⚠️ **Don't see the&#x20;**`.git`**&#x20;folder?**:::Paragraph{listStyleType="disc" indent="1"}
On macOS/Linux: Hidden folders (starting with `.`) may not show by default. Run `ls -la` in terminal to see them.
::::::Paragraph{listStyleType="disc" listStart="2" indent="1"}
On Windows: Enable "Show hidden files" in File Explorer settings.
::::::Paragraph{listStyleType="disc" listStart="3" indent="1"}
**If&#x20;**`.git`**&#x20;is truly missing:** You're not in the cloned repository! Go back to Step 1 and clone your repo properly.
:::
::::

:::BlockQuote
✅ **Success!** Your cloned repository now has the Back4App structure and the workflow file. The `.git` folder ensures you can push changes to GitHub.
:::

***

## Step 3: Find Your Back4App App IDs

You need to find the Application ID for each of your two Back4App apps.

### What is an Application ID?

It's a unique code that identifies your app. It looks something like this:

```none
JrOq8xfZSBWLxC1oD1aBr94gGVTV11Axo12kyus0
```

### How to find it:

1. **Log into Back4App** at back4app.com
2. **Click on your DEVELOPMENT app** from the dashboard
3. **In the Overview tab** (on the left side), look for **App ID** (on the right side)
4. **Copy the "App ID"** value

Write it down or paste it somewhere safe:

```none
My Development App ID: ________________________________
```

6. **Go back to the dashboard** and repeat for your PRODUCTION app:

```none
My Production App ID: ________________________________
```

:::BlockQuote
⚠️ **Important:** Make sure you don't mix them up! Label which is which.
:::

***

## Step 4: Edit the Workflow File

Now you'll put your App IDs into the workflow file.

### 4.1 Open the file

Open `.github/workflows/simpleDeploy.yaml` in your code editor.

### 4.2 Find lines 38-39

Look for this section near the top of the file:

```yaml
env:
  # ┌─────────────────────────────────────────────────────────────────────────┐
  # │ EDIT THESE VALUES - Replace with your actual Back4App Application IDs  │
  # └─────────────────────────────────────────────────────────────────────────┘
  DEVELOPMENT_APP_ID: "YOUR_DEVELOPMENT_APP_ID_HERE"
  PRODUCTION_APP_ID: "YOUR_PRODUCTION_APP_ID_HERE"
```

### 4.3 Replace the placeholder values

Change the placeholder text to your actual App IDs:

**Before:**

```yaml
  DEVELOPMENT_APP_ID: "YOUR_DEVELOPMENT_APP_ID_HERE"
  PRODUCTION_APP_ID: "YOUR_PRODUCTION_APP_ID_HERE"
```

**After (example):**

```yaml
  DEVELOPMENT_APP_ID: "JrOq8xfZSBWLxC1oD1aBr94gGVTV11Aks8ur08Kk"
  PRODUCTION_APP_ID: "v9pS0Ps4VTBwnVISz0TaVQ7vyDXVc8Alo42K096B"
```

:::BlockQuote
⚠️ **Important:** Keep the quotation marks around the IDs!
:::

### 4.4 Save the file

Press `Ctrl + S` (Windows/Linux) or `Cmd + S` (Mac) to save.

***

## Step 5: Add Your Secrets to GitHub

Secrets are like passwords - they're kept hidden and secure. You need to add two secrets to your GitHub repository.

### What secrets do you need?

| Secret Name            | What It Is                                        |
| ---------------------- | ------------------------------------------------- |
| `BACK4APP_EMAIL`       | The email address you use to log into Back4App    |
| `BACK4APP_ACCOUNT_KEY` | A special key from your Back4App account settings |

### 5.1 Find your Back4App Account Key

If you already created an Account Key in Step 2.2, you can use the same one. Otherwise:

1. **Log into Back4App** at back4app.com
2. **Click on your profile icon** (top-right corner of the dashboard)
3. **Look for "Account Keys"** in the menu
4. **Give your Account Key a name** and click the **"+"** button on the right side
5. **Copy your new key** immediately

:::BlockQuote
💡 **Tip:** If you already configured the CLI in Step 2, you already have an Account Key. You can use the same one for the GitHub secret.
:::

### 5.2 Add secrets to GitHub

1. **Go to your repository on GitHub**
   - Open your web browser
   - Go to `github.com/YOUR-USERNAME/YOUR-REPO-NAME`
2. **Click the "Settings" tab**
   - It's in the top menu bar of your repository
   - (You need to be the owner or have admin access)
3. **Find "Secrets and variables" in the left sidebar**
   - Click on it to expand
   - Click on **"Actions"**
4. **Add the first secret (BACK4APP\_EMAIL)**
   - Click the green **"New repository secret"** button
   - **Name:** Type `BACK4APP_EMAIL` (exactly like this, all capitals)
   - **Secret:** Type your Back4App email address
   - Click **"Add secret"**
5. **Add the second secret (BACK4APP\_ACCOUNT\_KEY)**
   - Click **"New repository secret"** again
   - **Name:** Type `BACK4APP_ACCOUNT_KEY` (exactly like this, all capitals)
   - **Secret:** Paste your Back4App Account Key
   - Click **"Add secret"**

### 5.3 Verify your secrets

After adding both secrets, you should see them listed:

```none
Repository secrets
──────────────────
BACK4APP_ACCOUNT_KEY    Updated just now
BACK4APP_EMAIL          Updated just now
```

:::BlockQuote
✅ **Note:** You won't be able to see the actual values - that's normal! GitHub hides them for security.
:::

***

## Step 6: Create Your Branches

The workflow uses two branches: `development` and `main`.

### What are branches?

Think of branches like parallel versions of your project:

- `development` - Where you test new features
- `main` - The stable version for real users

### Check if you already have these branches

🖥️ **Using Terminal/Command Line**

```bash
# Navigate to your project
cd your-project

# See all your branches
git branch -a
```

Look for `development` and `main` in the list.



🌐 **Using GitHub Website**

1. Go to your repository on GitHub
2. Click the branch dropdown (usually says "main" or "master")
3. See if `development` and `main` are listed



### Create missing branches

If you need to create the branches:

**Create the 'development' branch**

```bash
# Make sure you're in your project folder
cd your-project

# Create and switch to development branch
git checkout -b development

# Push it to GitHub
git push -u origin development
```



**Create the 'main' branch**

```bash
# Create and switch to main branch
git checkout -b main

# Push it to GitHub
git push -u origin main
```



### ⚠️ About "master" vs "main"

Some older repositories use `master` instead of `main`. This workflow uses `main`.

If your repository has `master` but not `main`, you have two options:

**Option A: Rename master to main**

```bash
git branch -m master main
git push -u origin main
```

**Option B: Edit the workflow file** to use `master` instead of `main`:

Find this section in `simpleDeploy.yaml`:

```yaml
on:
  push:
    branches:
      - development
      - main
```

Change `main` to `master`:

```yaml
on:
  push:
    branches:
      - development
      - master
```

***

## Step 7: Deploy!

You're all set up! Now let's test it.

### 7.1 Commit and push your changes

```bash
# Add all your changes (including the workflow file)
git add .

# Create a commit
git commit -m "Add deployment workflow"

# Push to development branch first (for testing)
git checkout development
git push origin development
```

### 7.2 Watch the magic happen

1. **Go to your repository on GitHub**
2. **Click the "Actions" tab**
3. **You should see a workflow running!**

The workflow will show each step as it runs:

- ✅ Green checkmark = Step completed successfully
- 🔄 Yellow spinner = Step is running
- ❌ Red X = Step failed (click to see what went wrong)

### 7.3 Check the results

If everything worked, you'll see:

```none
✅ DEPLOYMENT COMPLETE!
```

And your Back4App Development app will have your latest code!

***

## How to Use It Daily

Once set up, using this workflow is simple:

### For everyday development:

```bash
# Make your changes to the code
# Then:
git add .
git commit -m "Describe what you changed"
git push origin development
```

→ This deploys to your **Development** Back4App app

### When you're ready to release to users:

```bash
# Switch to main branch
git checkout main

# Merge your tested changes from development
git merge development

# Push to main
git push origin main
```

→ This deploys to your **Production** Back4App app

### Quick reference:

| Action           | Command                       | Result                  |
| ---------------- | ----------------------------- | ----------------------- |
| Test new code    | `git push origin development` | Updates Development app |
| Release to users | `git push origin main`        | Updates Production app  |

***

## Troubleshooting

### ❌ "DEVELOPMENT\_APP\_ID has not been configured!"

**What it means:** You didn't edit the workflow file with your App IDs.

**How to fix:**

1. Open `.github/workflows/simpleDeploy.yaml`
2. Find lines 38-39
3. Replace `YOUR_DEVELOPMENT_APP_ID_HERE` with your actual App ID
4. Save, commit, and push again

***

### ❌ "BACK4APP\_EMAIL secret is not set!"

**What it means:** GitHub can't find the secret you were supposed to add.

**How to fix:**

1. Go to your repo on GitHub → Settings → Secrets and variables → Actions
2. Check if `BACK4APP_EMAIL` exists (exact spelling, all capitals)
3. If not, add it (see [**Step 5**](./#step-5-add-your-secrets-to-github))

***

### ❌ "BACK4APP\_ACCOUNT\_KEY secret is not set!"

**What it means:** Same as above, but for the account key.

**How to fix:**

1. Go to your repo on GitHub → Settings → Secrets and variables → Actions
2. Check if `BACK4APP_ACCOUNT_KEY` exists
3. If not, add it (see [**Step 5**](./#step-5-add-your-secrets-to-github))

***

### ❌ Workflow doesn't run when I push

**Possible causes:**

1. **Wrong branch name:** The workflow only runs on `development` and `main`. Check your branch:

```bash
git branch
```

1. **Workflow file in wrong location:** It must be at exactly:

```none
.github/workflows/simpleDeploy.yaml
```

1. **YAML syntax error:** Make sure you didn't accidentally break the file format when editing.

***

### ❌ "b4a deploy" fails

**Possible causes:**

1. **Wrong App ID:** Double-check that you copied the correct Application IDs
2. **Wrong Account Key:** Your account key might be incorrect or expired
3. **No permission:** Make sure your Back4App account has access to both apps

***

### ❌ Health check shows unexpected response

**What it means:** The deployment probably worked, but the verification step got an unusual response.

**This is usually okay!** The important thing is whether the "Deploy to Back4App" step succeeded.

Check your Back4App dashboard to confirm the deployment worked.

***

### I need more help!

If you're stuck:

1. **Read the error message carefully** - It usually tells you exactly what's wrong
2. **Check the Actions tab on GitHub** - Click on the failed run, then click on the failed step to see details
3. **Compare your setup** with this guide step-by-step
4. **Ask for help** - Include the exact error message when asking

***

## Glossary

New to some of these terms? Here's what they mean:

| Term                  | What It Means                                                              |
| --------------------- | -------------------------------------------------------------------------- |
| **Branch**            | A separate version of your code. Like having a "draft" and a "final" copy. |
| **Commit**            | A saved snapshot of your changes, with a message describing what you did.  |
| **Push**              | Uploading your commits from your computer to GitHub.                       |
| **Repository (Repo)** | Your project's home on GitHub - contains all your code and history.        |
| **Workflow**          | An automated process that runs when something happens (like pushing code). |
| **Secret**            | A hidden value (like a password) stored securely in GitHub.                |
| **Application ID**    | A unique code that identifies your Back4App app.                           |
| **Account Key**       | A password-like code that proves you own your Back4App account.            |
| **Cloud Code**        | JavaScript code that runs on Back4App's servers.                           |
| **CLI**               | Command Line Interface - a way to control programs by typing commands.     |

***

## Summary Checklist

Use this checklist to make sure you've completed everything:

- [ ] Created `.github/workflows/` folder in your project
- [ ] Copied `simpleDeploy.yaml` into that folder
- [ ] Found your Development App ID from Back4App
- [ ] Found your Production App ID from Back4App
- [ ] Edited `simpleDeploy.yaml` with both App IDs (lines 38-39)
- [ ] Added `BACK4APP_EMAIL` secret to GitHub
- [ ] Added `BACK4APP_ACCOUNT_KEY` secret to GitHub
- [ ] Created `development` branch (or confirmed it exists)
- [ ] Created `main` branch (or confirmed it exists)
- [ ] Pushed code and saw the workflow run successfully

**Once all boxes are checked, you're done! 🎉**

***

## What's Next?

Now that you have automatic deployments working, you might want to:

1. **Set up branch protection** - Prevent accidental pushes to `main`
2. **Add collaborators** - Let team members push code too
3. **Try the advanced workflow** - Check out `deploy.yaml` for more features like:
   - Automatic code linting (ESLint)
   - Code formatting (Prettier)
   - Running tests (Jest)
   - More than 2 environments

***

**Congratulations on setting up your first CI/CD pipeline! 🚀**

*CI/CD = Continuous Integration / Continuous Deployment - fancy words for "automatically test and deploy code"*
