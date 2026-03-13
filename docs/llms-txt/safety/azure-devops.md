# Source: https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/azure-devops.md

# Azure DevOps

This is a guide to setting up and configuring Safety to scan your Azure DevOps repositories for dependency security vulnerabilities. This enables you to configure security and compliance scans on your repositories on new commits, new branches, pull requests, and more.

You can set up Safety to run security scans on your Python repositories in Azure DevOps using Azure Pipelines.

### Step 1: Get your Safety API Key

To scan any systems for security vulnerabilities, you first need a Safety account. [You can create a Safety account and get your API key here.](https://platform.safetycli.com/organization/apikeys)

### Step 2: Set up an Azure DevOps Pipeline on your Repository

Azure Pipelines are a simple and powerful way to build, test, and deploy your code hosted in Azure DevOps. Integrating Safety into your CI/CD pipeline enables automated security and compliance checks for every commit, pull request, or scheduled run.

If you don’t already have a pipeline configured, follow these Microsoft guides to get started:

* [Get started with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started-yaml?view=azure-devops)
* [Build Python apps with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/languages/python?view=azure-devops)

Once your pipeline is in place, proceed to the next step to configure Safety CLI.

***

### Step 2.5: Set up a Self-Hosted Agent (Optional)

If you prefer to run pipelines on your own infrastructure—such as a local machine or internal server—you can configure a self-hosted agent instead of using Microsoft's hosted runners.

For complete setup instructions, see:

* [Set up a self-hosted agent in Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/v2-linux?view=azure-devops)

Once your agent is configured and running, reference its pool name in your pipeline YAML:

```yaml
pool:
  name: Default
```

This tells Azure DevOps to execute the pipeline on the self-hosted runner you just configured in the `Default` agent pool.

### Step 3: Configure your azure-pipelines.yml YAML file to run Safety

Azure Pipelines are configured using an `azure-pipelines.yml` file at the root of your Azure DevOps repository. Here is an example YAML file that installs and runs Safety to scan your Python environment for security vulnerabilities.

```yaml
# Safety Security Scans Template

# This template allows you to run security scans on your Python dependencies.
# The workflow is configured to run on pushes to the 'main' branch.

trigger:
  - main  # Triggers the pipeline on changes to the 'main' branch

pool:
  name: Default  # Uses the default agent pool defined in Azure DevOps

steps:
  - script: |
      # Upgrade pip to the latest version
      python3 -m pip install --upgrade pip

      # Install Safety CLI – Safety’s command-line tool for dependency scanning
      pip install safety

      # (Optional) Install your project dependencies if you want to scan the active environment.
      # This is not required, Safety can scan your static files directly (e.g., requirements.txt, pyproject.toml)
      # You may also use Poetry or Pipenv instead.
      # pip3 install -r requirements.txt

      # Run Safety to scan the local Python environment
      # This will check all installed packages (including transitive dependencies) for vulnerabilities
      safety --key $(SAFETY_API_KEY) --stage cicd scan
    env:
      SAFETY_API_KEY: $(SAFETY_API_KEY)  # Injects your Safety API key as an environment variable
      SAFETY_CLI_DISABLE_LOCAL_CONFIG: "1"  # Disables any local Safety config to avoid misconfiguration
```

### Final Step: Add your Safety API Key as an Azure DevOps pipeline variable

Your Safety script requires the Safety API key to connect to Safety and retrieve the latest commercial vulnerability database.

There are two ways to securely inject the API key into your pipeline:

**Option 1: Define the variable in a Variable Group (via Library)**

* Navigate to your project in Azure DevOps.
* Go to Pipelines > Library.
* Create a new Variable Group or select an existing one.
* Add a variable named `SAFETY_API_KEY` and paste in your key.
* Check "Keep this value secret" to secure the key.

**Option 2: Define the variable in the pipeline UI**

* Go to your pipeline in Azure DevOps.
* Click Edit, then select the "Variables" tab.
* Add a new variable named `SAFETY_API_KEY`.
* Paste in your key and mark it as secret.

Either method will make the `$(SAFETY_API_KEY)` variable available to your pipeline, allowing the YAML configuration to authenticate successfully with Safety CLI.

### You're done!

That's it! You now have a fully working Azure DevOps pipeline that will run and scan your Python dependencies for security vulnerabilities on new pushes and pull requests using Safety's commercial vulnerability database.

If there is a vulnerability found, Safety will return a non-zero exit code and fail the test. You can then see the pipeline's output in Azure DevOps to view what Safety found and how to patch the vulnerabilities.

### Next Steps: Configure your pipeline file, and learn more about Safety

There are many more configuration options on Azure Pipelines. For example, you can:

* Set up this pipeline to only run on certain branches or run when other conditions are met.
* Configure it to run periodically using a cron so that your repository is scanned for security vulnerabilities every hour or every day, not just when new code is committed.

You can read more about Azure Pipelines on their [documentation page](https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops).

And for more on Safety CLI, visit [Safety CLI Documentation](https://docs.safetycli.com).
