# Source: https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/github/github-actions.md

# GitHub Actions

## Introduction to GitHub Actions

[GitHub Actions](https://github.com/features/actions) is a powerful automation tool that integrates directly with GitHub repositories to allow you to automate your workflow by setting up a series of commands (actions) that execute in response to specific GitHub events like a push or a pull request. These actions can be used for a variety of tasks, such as testing code, deploying applications and, in the case of Safety, scanning for vulnerabilities.

[**The Safety CLI Scanner GitHub Action**](https://github.com/marketplace/actions/pyupio-safety-action) enables automated scanning of your projects for vulnerabilities directly within your GitHub workflow.

Link to Safety GitHub Action: <https://github.com/marketplace/actions/pyupio-safety-action>

## Setting Up the Safety GitHub Action

### **Step 1: Create a Safety Account and Obtain an API Key**

* To utilize the Safety CLI scanner, you first need to [create a Safety account](https://platform.safetycli.com/register/).
* Once your account is set up, you can obtain your API key from your [Safety Dashboard](https://platform.safetycli.com/). This key will be used to authenticate your GitHub Action with Safety's services.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FwAVEJQ8iG3lVIfbSunzS%2FScreenshot%202024-07-15%20at%2012.03.09.png?alt=media&#x26;token=9dcfc131-825a-45ce-8abc-4319c14c470a" alt=""><figcaption><p>Organization and User API Keys are available in Organization->API Keys</p></figcaption></figure>

### **Step 2: Configure the GitHub Secret**

* After obtaining your Safety API key, go to your GitHub repository's settings.
* Navigate to the '[Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)' section and add a new secret.
* Name the secret (e.g., `SAFETY_API_KEY`) and paste your Safety API key as the value.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FjE4NmTUEBcc0gRhQArox%2FScreenshot%202024-07-15%20at%2012.07.00.png?alt=media&#x26;token=d1626338-f245-4bd6-a308-57989521ee43" alt=""><figcaption><p>Add a new Secret to your Repo called SAFETY_API_KEY</p></figcaption></figure>

### **Step 3: Set Up the Workflow File**

* You may need to create a Personal Access Token (PAT) with workflow permissions in order to push a workflow file to your repo. To do so, please [refer to this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
* In your repository, create a new file in the `.github/workflows` directory. You can name this file according to its purpose (e.g., `safety_scan.yml`).
* Add the following content to your workflow file:

```yaml
name: Example workflow for Python using Safety Action
on: push
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
      - name: Run Safety CLI to check for vulnerabilities
        uses: pyupio/safety-action@v1
        with:
          api-key: ${{ secrets.SAFETY_API_KEY }}

```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F4dJmDKDMdREoEHFsG2Xz%2FScreenshot%202024-07-15%20at%2012.29.26.png?alt=media&#x26;token=6efefe85-a895-4651-8ca4-ec561c4dd05a" alt=""><figcaption></figcaption></figure>

### **Step 4: Activate the Workflow**

* Commit and push the workflow file to your repository.
* The Safety CLI Scanner Action will run automatically on each push, scanning your Python project for any vulnerabilities.

### **Additional Configurations (Optional)**

* You can customize the behaviour of the Safety Action by using various properties.
* You can also add arguments like `--detailed-output` to get more information from the scan:

```yaml
name: Example workflow customizing the Safety Action
on: push
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
      - name: Run Safety CLI to check for vulnerabilities
        uses: pyupio/safety-action@v1
        with:
          api-key: ${{ secrets.SAFETY_API_KEY }}
          args: --detailed-output # To always see detailed output from this action

```

#### Available Properties

<table><thead><tr><th>Property</th><th width="122.33333333333331">Default</th><th>Description</th></tr></thead><tbody><tr><td>api-key</td><td></td><td>Your Safety API Key</td></tr><tr><td>output-format</td><td>screen</td><td>Options are: screen, json, html, spdx, none</td></tr><tr><td>args</td><td></td><td>Override the default arguments to Safety CLI 3.</td></tr></tbody></table>

For more detailed information about Safety's CLI and its functionalities, please refer to [Safety 3 Documentation](https://docs.safetycli.com/safety-docs) or contact our [Support Team](https://docs.safetycli.com/safety-docs/support/support).
