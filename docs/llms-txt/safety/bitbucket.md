# Source: https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/bitbucket.md

# BitBucket

This is a guide to setting up and configuring Safety to scan your BitBucket repositories for dependency security vulnerabilities. This enables you to configure security and compliance scans on your repositories on new commits, new branches, pull requests, and more.

You can set up Safety to run security scans on your Python repositories in BitBucket using BitBucket pipelines.

### Step 1: Get your Safety API Key

To scan any systems for security vulnerabilities, you first need a Safety account. [You can create a Safety account and get your API key here.](https://platform.safetycli.com/register/)

### Step 2: Set up a Bitbucket Pipeline on your repository (If you don't have one already)

BitBucket pipelines are an easy and powerful way to run CI/CD processes on your codebases hosted on BitBucket. Adding Safety security scans to your repositories is as easy as adding a few lines of code to your BitBucket pipeline configuration file to install and run Safety CLI.

We've created some full pipeline examples below if you don't have one set up yet. If you need help configuring your pipeline, you can read more on [getting startup with BitBucket pipelines](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/) as well as [setting up BitBucket pipelines in Python projects](https://support.atlassian.com/bitbucket-cloud/docs/python-with-bitbucket-pipelines/).

### Step 3: Configure your bitbucket-pipelines.yml YAML file to run Safety

BitBucket pipelines are configured using a `bitbucket-pipelines.yml` YAML file at the root of your BitBucket repository. Here is an example YAML file that installs and runs Safety to scan your Python environment for security vulnerabilities.

YAML

```yaml
#  Safety Security Scans Template

#  This template allows you to run security scans on your Python dependencies.
#  The workflow allows running tests on the default branch.

image: python:3.12

pipelines:
  default:
    - parallel:
      - step:
          # Run Safety to scan your Python Environment (recommended and best practice)
          name: Safety Security Scan on the Python Environment
          script:
            # Install Safety CLI - Safety's command-line tool
            - pip install safety
            # Install your Python dependencies as per usual. 
            # This example uses requirements.txt and pip, but you may use Poetry with its Pipfiles, or pipenv with its pyproject.toml file. 
            - pip install -r requirements.txt
            # Run safety to scan the local Python environment. This will scan all installed dependencies, including any transitive dependncies that get installed during your installation
            - safety --key $SAFETY_API_KEY --stage cicd scan
```

Your pipeline YAML file will likely end up running other tests and actions and deployments. All you have to do to ensure that Safety is scanning your dependencies for security vulnerabilities is to ensure that the following code (script) is in your YAML file amongst your other tests and scripts that are running.

YAML

```yaml
...
  script:
    # Install Safety - PyUp's command-line tool
    - pip install safety
    # Install your Python dependencies as per usual. 
    # This example uses requirements.txt and pip, but you may use Poetry with its Pipfiles, or pipenv with its pyproject.toml file. 
    - pip install -r requirements.txt
    # Run safety to scan the local Python environment. This will scan all installed dependencies, including any transitive dependncies that get installed during your installation
    - safety --key $SAFETY_API_KEY --stage cicd scan
```

### Final Step: Add your Safety API Key as a BitBucket repository variable

Your safety script requires the Safety API key to connect to Safety and get the latest commercial vulnerability database.

To link up this API key to the $SAFETY\_API\_KEY variable defined in your pipeline YAML file (example above), you need to add your Safety API key as a BitBucket repository variable.&#x20;

To do this, navigate to your repository on BitBucket, then **Repository settings** then the **Repository variables** sub-menu.

Once added, the new variable should display like the screenshot below on the BitBucket repository variable page:

![918](https://files.readme.io/6b80389-Screen_Shot_2022-02-01_at_7.27.19_PM.png)

### You're done!

That's it! You now have a fully working BitBucket pipeline that will run and scan your Python dependencies for security vulnerabilities on new pushes and pull requests using Safety's commercial vulnerability database.

If there is a vulnerability found, Safety will return a non-zero exit code and fail the test. You can then see the pipeline's output in Bitbucket to see what Safety found and how to patch the vulnerabilities. Here is our example running on a new pull request:

<figure><img src="https://files.readme.io/76d8aab-Screen_Shot_2022-02-01_at_7.46.14_PM.png" alt=""><figcaption></figcaption></figure>

### Next Steps: Configure your Pipeline file, and learn more about Safety

**BitBucket Pipelines**\
There are many more configuration options on BitBucket Pipelines. For example, you can set up this Pipeline to only run on certain branches or run when other conditions are met. You can also configure it to run periodically using a cron so that your repository is scanned for security vulnerabilities every hour or every day, not just when new code is committed.

You can read more about BitBucket's pipelines on their [documentation page](https://support.atlassian.com/bitbucket-cloud/docs/configure-bitbucket-pipelinesyml/).
