# Source: https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/github.md

# GitHub

## GitHub Actions

This is a guide to setting up and configuring Safety to scan your GitHub repositories for dependency security vulnerabilities using Safety as a GitHub Action. This enables you to configure security and compliance scans on your repositories on new commits, new branches, pull requests, and more.Safety is available as an action in the [GitHub Marketplace](https://github.com/marketplace/actions/pyupio-safety).

#### Step 1: Get your Safety API Key <a href="#step-1-get-your-safety-api-key" id="step-1-get-your-safety-api-key"></a>

To scan any systems for security vulnerabilities, you first need a Safety API key. You can create a Safety account and get your API key [here](https://safetycli.com/contact-sales).

In your GitHub repository, navigate to **Settings** -> **Secrets** -> **Actions**, and add your Safety API key as a secret that matches the variable name you've used in the workflow YAML file (`SAFETY_API_KEY` in all the examples here). Once added, it should look similar to the screenshot below:​​

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F66efviut0LyscT2xhSHv%2F7cb6184-8886cae-Screen_Shot_2022-02-02_at_5.27.37_PM.png?alt=media&#x26;token=4f66d70d-4b60-44c5-8d3a-57b7d138055b" alt="" width="563"><figcaption></figcaption></figure>

#### Step 2: Set up a GitHub Actions workflow on your repository (If you don't have one already) <a href="#step-2-set-up-a-github-actions-workflow-on-your-repository-if-you-dont-have-one-already" id="step-2-set-up-a-github-actions-workflow-on-your-repository-if-you-dont-have-one-already"></a>

GitHub Actions are an easy and powerful way to run CI/CD processes on your codebases hosted on GitHub. Adding Safety security scans to your repositories is as easy as adding a few lines of code to your Github Action workflow configuration file to run Safety.We've created some full pipeline examples below if you don't have one set up yet. If you need help configuring your Python workflow, you can read more on [getting startup with GitHub workflows in Python](https://docs.github.com/actions/automating-builds-and-tests/building-and-testing-nodejs-or-python?langId=py).

#### Step 3: Configure your GitHub workflow YAML file to run Safety scans <a href="#step-3-configure-your-github-workflow-yaml-file-to-run-safety-scans" id="step-3-configure-your-github-workflow-yaml-file-to-run-safety-scans"></a>

GitHub Actions are configured using YAML workflow files in a special `.github/workflows/` folder. Here is an example YAML file that runs Safety to scan your project for security vulnerabilities. This will scan in auto-detect mode, which will try and scan the most appropriate thing automatically.You can read more about Safety's scan modes and different options.YAML# This workflow will run Safety security scans on all dependencies that are installed into the environment.# For more information see: <https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions#> Saved to \`.github/workflows/safety.yml\`​name: Safety Security Scan​on:push: # Run on every push to any branchpull\_request: # Run on new pull requests​jobs:safety:runs-on: ubuntu-lateststeps:- uses: safety/safety\@2.3.4with:api-key: ${{secrets.SAFETY\_API\_KEY}}
