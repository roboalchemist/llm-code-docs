# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions

Title: Use GitHub Actions to make code updates in Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions

Markdown Content:
You can use a [GitHub Actions workflow](https://docs.github.com/actions/learn-github-actions/introduction-to-github-actions#the-components-of-github-actions) to define a workflow to automatically build and deploy code to your function app in Azure Functions.

A YAML file (.yml) that defines the workflow configuration is maintained in the `/.github/workflows/` path in your repository. This definition contains the actions and parameters that make up the workflow, which is specific to the development language of your functions. A GitHub Actions workflow for Functions performs the following tasks, regardless of language:

1.   Set up the environment.
2.   Build the code project.
3.   Deploy the package to a function app in Azure.

The Azure Functions action handles the deployment to an existing function app in Azure.

You can create a workflow configuration file for your deployment manually. You can also generate the file from a set of language-specific templates in one of these ways:

*   In the Azure portal
*   Using the Azure CLI
*   From your GitHub repository

If you don't want to create your YAML file by hand, select a different method at the top of the article.

*   An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

*   A GitHub account. If you don't have one, sign up for [free](https://github.com/join).

*   A working function app hosted on Azure with source code in a GitHub repository.

*   [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli), when developing locally. You can also use the Azure CLI in Azure Cloud Shell.

Since GitHub Actions uses your publish profile to access your function app during deployment, you first need to get your publish profile and store it securely as a [GitHub secret](https://docs.github.com/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).

Important

The publish profile is a valuable credential that allows access to Azure resources. Make sure you always transport and store it securely. In GitHub, the publish profile must only be stored in GitHub secrets.

To download the publishing profile of your function app:

1.   In the [Azure portal](https://portal.azure.com/), locate the page for your function app, expand **Settings**>**Configuration** in the left column.

2.   In the **Configuration** page, select the **General settings** tab and make sure that **SCM Basic Auth Publishing Credentials** is turned **On**. When this setting is **Off**, you can't use publish profiles, so select **On** and then **Apply**.

3.   Go back to the function app's **Overview** page, and then select **Get publish profile**.

![Image 1: Download publish profile](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-how-to-github-actions/get-publish-profile.png)

4.   Save and copy the contents of the file.

1.   In [GitHub](https://github.com/), go to your repository.

2.   Go to **Settings**.

3.   Select **Secrets and variables > Actions**.

4.   Select **New repository secret**.

5.   Add a new secret with the name `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` and the value set to the contents of the publishing profile file.

6.   Select **Add secret**.

GitHub can now authenticate to your function app in Azure.

The best way to manually create a workflow configuration is to start from the officially supported template.

1.   Choose either **Windows** or **Linux** to make sure that you get the template for the correct operating system.

    *   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions#tabpanel_1_windows)
    *   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions#tabpanel_1_linux)

Deployments to Linux use `runs-on: ubuntu-latest`.

2.   Copy the language-specific template from the Azure Functions actions repository using the following link:

3.   Update the `env.AZURE_FUNCTIONAPP_NAME` parameter with the name of your function app resource in Azure. You may optionally need to update the parameter that sets the language version used by your app, such as `DOTNET_VERSION` for C#.

4.   Add this new YAML file in the `/.github/workflows/` path in your repository.

When you use the portal to enable GitHub Actions, Functions creates a workflow file based on your application stack and commits it to your GitHub repository in the correct directory.

The portal automatically gets your publish profile and adds it to the GitHub secrets for your repository.

You can get started quickly with GitHub Actions through the Deployment tab when you create a function in Azure portal. To add a GitHub Actions workflow when you create a new function app:

1.   In the [Azure portal](https://portal.azure.com/), select **Deployment** in the **Create Function App** flow.

![Image 2: Screenshot of Deployment option in Functions menu.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-how-to-github-actions/github-actions-deployment.png)

2.   Enable **Continuous Deployment** if you want each code update to trigger a code push to Azure portal.

3.   Enter your GitHub organization, repository, and branch.

![Image 3: Screenshot of GitHub user account details.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-how-to-github-actions/github-actions-github-account-details.png)

4.   Complete configuring your function app. Your GitHub repository now includes a new workflow file in `/.github/workflows/`.

To add a GitHub Actions workflow to an existing function app:

1.   Navigate to your function app in the [Azure portal](https://portal.azure.com/) and select **Deployment Center**.

2.   For **Source** select **GitHub**. If you don't see the default message _Building with GitHub Actions_, select **Change provider** choose **GitHub Actions** and select **OK**.

3.   If you haven't already authorized GitHub access, select **Authorize**. Provide your GitHub credentials and select **Sign in**. To authorize a different GitHub account, select **Change Account** and sign in with another account.

4.   Select your GitHub **Organization**, **Repository**, and **Branch**. To deploy with GitHub Actions, you must have write access to this repository.

5.   In **Authentication settings**, choose whether to have GitHub Actions authenticate with a **User-assigned identity** or using **Basic authentication** credentials. For basic authentication, the current credentials are used.

6.   Select **Preview file** to see the workflow file that gets added to your GitHub repository in `github/workflows/`.

7.   Select **Save** to add the workflow file to your repository.

You can use the [`az functionapp deployment github-actions add`](https://learn.microsoft.com/en-us/cli/azure/functionapp/deployment/github-actions) command to generate a workflow configuration file from the correct template for your function app. The new YAML file is then stored in the correct location (`/.github/workflows/`) in the GitHub repository you provide, while the publish profile file for your app is added to GitHub secrets in the same repository.

1.   Run this `az functionapp` command, replacing the values `githubUser/githubRepo`, `MyResourceGroup`, and `MyFunctionapp`:

```
az functionapp deployment github-actions add --repo "githubUser/githubRepo" -g MyResourceGroup -n MyFunctionapp --login-with-github
```

This command uses an interactive method to retrieve a personal access token for your GitHub account.

2.   In your terminal window, you should see something like the following message:

```
Please navigate to https://github.com/login/device and enter the user code XXXX-XXXX to activate and retrieve your GitHub personal access token.
```
3.   Copy the unique `XXXX-XXXX` code, browse to [https://github.com/login/device](https://github.com/login/device), and enter the code you copied. After entering your code, you should see something like the following message:

```
Verified GitHub repo and branch
Getting workflow template using runtime: java
Filling workflow template with name: func-app-123, branch: main, version: 8, slot: production, build_path: .
Adding publish profile to GitHub
Fetching publish profile with secrets for the app 'func-app-123'
Creating new workflow file: .github/workflows/master_func-app-123.yml
```
4.   Go to your GitHub repository and select **Actions**. Verify that your workflow ran.

You can create the GitHub Actions workflow configuration file from the Azure Functions templates directly from your GitHub repository.

1.   In [GitHub](https://github.com/), go to your repository.

2.   Select **Actions** and **New workflow**.

3.   Search for _functions_.

![Image 4: Screenshot of search for GitHub Actions functions templates. ](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-how-to-github-actions/github-actions-functions-templates.png)

4.   In the displayed functions app workflows authored by Microsoft Azure, find the one that matches your code language and select **Configure**.

5.   In the newly created YAML file, update the `env.AZURE_FUNCTIONAPP_NAME` parameter with the name of your function app resource in Azure. You may optionally need to update the parameter that sets the language version used by your app, such as `DOTNET_VERSION` for C#.

6.   Verify that the new workflow file is being saved in `/.github/workflows/` and select **Commit changes...**.

If for some reason you need to update or change an existing workflow configuration, just navigate to the `/.github/workflows/` location in your repository, open the specific YAML file, make any needed changes, and then commit the updates to the repository.

The following template example uses version 1 of the `functions-action` and a `publish profile` for authentication. The template depends on your chosen language and the operating system on which your function app is deployed:

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions#tabpanel_3_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions#tabpanel_3_linux)

If your function app runs on Windows, select **Windows**.

*   [.NET](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions#tabpanel_4_dotnet_linux)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions#tabpanel_4_java_linux)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions#tabpanel_4_javascript_linux)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions#tabpanel_4_python_linux)
*   [PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions#tabpanel_4_powershell_linux)

```
name: Deploy DotNet project to Azure Function App

on:
  [push]

env:
  AZURE_FUNCTIONAPP_NAME: 'your-app-name'   # set this to your function app name on Azure
  AZURE_FUNCTIONAPP_PACKAGE_PATH: '.'       # set this to the path to your function app project, defaults to the repository root
  DOTNET_VERSION: '6.0.x'                   # set this to the dotnet version to use (e.g. '2.1.x', '3.1.x', '5.0.x')

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment: dev
    steps:
    - name: 'Checkout GitHub Action'
      uses: actions/checkout@v3

    - name: Setup DotNet ${{ env.DOTNET_VERSION }} Environment
      uses: actions/setup-dotnet@v3
      with:
        dotnet-version: ${{ env.DOTNET_VERSION }}

    - name: 'Resolve Project Dependencies Using Dotnet'
      shell: bash
      run: |
        pushd './${{ env.AZURE_FUNCTIONAPP_PACKAGE_PATH }}'
        dotnet build --configuration Release --output ./output
        popd

    - name: 'Run Azure Functions Action'
      uses: Azure/functions-action@v1
      id: fa
      with:
        app-name: ${{ env.AZURE_FUNCTIONAPP_NAME }}
        package: '${{ env.AZURE_FUNCTIONAPP_PACKAGE_PATH }}/output'
        publish-profile: ${{ secrets.AZURE_FUNCTIONAPP_PUBLISH_PROFILE }}
```

The Azure Functions action (`Azure/functions-action`) defines how your code is published to an existing function app in Azure, or to a specific slot in your app.

The following parameters are required for all function app plans:

| Parameter | Explanation |
| --- | --- |
| _**app-name**_ | The name of your function app. |
| _**package**_ | This is the location in your project to be published. By default, this value is set to `.`, which means all files and folders in the GitHub repository will be deployed. |

The following parameters are required for the Flex Consumption plan:

| Parameter | Explanation |
| --- | --- |
| _**sku**_ | Set this to `flexconsumption` when authenticating with publish-profile. When using RBAC credentials or deploying to a non-Flex Consumption plan, the Action can resolve the value, so the parameter doesn't need to be included. |
| _**remote-build**_ | Set this to `true` to enable a build action from Kudu when the package is deployed to a Flex Consumption app. Oryx build is always performed during a remote build in Flex Consumption; don't set **scm-do-build-during-deployment** or **enable-oryx-build**. By default, this parameter is set to `false`. |

The following parameters are specific to the Consumption, Elastic Premium, and App Service (Dedicated) plans:

| Parameter | Explanation |
| --- | --- |
| _**scm-do-build-during-deployment**_ | (Optional) Allow the Kudu site (for example, `https://<APP_NAME>.scm.azurewebsites.net/`) to perform pre-deployment operations, such as [remote builds](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies#remote-build). By default, this is set to `false`. Set this to `true` when you do want to control deployment behaviors using Kudu instead of resolving dependencies in your GitHub workflow. For more information, see the [`SCM_DO_BUILD_DURING_DEPLOYMENT`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#scm_do_build_during_deployment) setting. |
| _**enable-oryx-build**_ | (Optional) Allow Kudu site to resolve your project dependencies with Oryx. By default, this is set to `false`. If you want to use [Oryx](https://github.com/Microsoft/Oryx) to resolve your dependencies instead of the GitHub Workflow, set both **scm-do-build-during-deployment** and **enable-oryx-build** to `true`. |

Optional parameters for all function app plans:

| Parameter | Explanation |
| --- | --- |
| _**slot-name**_ | This is the [deployment slot](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-slots) name to be deployed to. By default, this value is empty, which means the GitHub Action will deploy to your production site. When this setting points to a non-production slot, ensure the **publish-profile** parameter contains the credentials for the slot instead of the production site. _Currently not supported in Flex Consumption_. |
| _**publish-profile**_ | The name of the GitHub secret that contains your publish profile. |
| _**respect-pom-xml**_ | Used only for Java functions. Whether it's required for your app's deployment artifact to be derived from the pom.xml file. When deploying Java function apps, you should set this parameter to `true` and set `package` to `.`. By default, this parameter is set to `false`, which means that the `package` parameter must point to your app's artifact location, such as `./target/azure-functions/` |
| _**respect-funcignore**_ | Whether GitHub Actions honors your .funcignore file to exclude files and folders defined in it. Set this value to `true` when your repository has a .funcignore file and you want to use it exclude paths and files, such as text editor configurations, .vscode/, or a Python virtual environment (.venv/). The default setting is `false`. |

Keep the following considerations in mind when using the Azure Functions action:

*   When using GitHub Actions, the way that your code is deployed depends on your hosting plan, as shown in this table:

| Hosting plan | Deployment method |
| --- | --- |
| [Flex Consumption](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan) | [One deploy](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies#one-deploy) |
| [Elastic Premium](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan) | [Zip deploy](https://learn.microsoft.com/en-us/azure/azure-functions/deployment-zip-push) to apps on the [Consumption](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan) |
| [Dedicated (App Service)](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan) | [Zip deploy](https://learn.microsoft.com/en-us/azure/azure-functions/deployment-zip-push) to apps on the [Consumption](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan) |
| [Consumption](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan) | Windows: [Zip deploy](https://learn.microsoft.com/en-us/azure/azure-functions/deployment-zip-push) Linux: [external package URL](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies#external-package-url)* | 
* The ability to run your apps on Linux in a Consumption plan is planned for retirement. For more information, see [Azure Functions Consumption plan hosting](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan).

*   The credentials required by GitHub to connect to Azure for deployment are stored as Secrets in your GitHub repository and accessed in the deployment as `secrets.<SECRET_NAME>`.

*   The easiest way for GitHub Actions to authenticate with Azure Functions for deployment is by using a publish profile. You can also authenticate using a service principal. To learn more, see [this GitHub Actions repository](https://github.com/Azure/functions-action).

*   The actions for setting up the environment and running a build are generated from the templates and are language specific.

*   The templates use `env` elements to define settings unique to your build and deployment.
