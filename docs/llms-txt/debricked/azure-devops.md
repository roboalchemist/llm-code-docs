# Source: https://docs.debricked.com/tools-and-integrations/integrations/azure-devops.md

# Azure DevOps

With our CI integration to Azure DevOps you can automatically upload your latest commits and pull requests to OpenText Core SCA or whenever you run your pipeline. Our Azure DevOps integration support the same options as our Bitbucket integration.

### Integrate a single repository <a href="#integrateasinglerepository" id="integrateasinglerepository"></a>

#### Configure OpenText Core SCA token <a href="#configuredebrickedtoken" id="configuredebrickedtoken"></a>

1. Start by [**generating an access token**](https://docs.debricked.com/product/administration/generate-access-token). Copy the token so that you can use it in the next step.
2. Configure your DEBRICKED\_TOKEN variable by going to **\[your repository] -> Pipelines -> \[your pipeline name] -> Edit -> Variables**. Make sure to check “Keep this value secret” so that you do not expose your login credentials to the world.

#### Configure Azure pipelines <a href="#configureazurepipelines" id="configureazurepipelines"></a>

Depending on what package manager you are using there are different step setups.

In order to analyze all dependencies in your project, their versions, and relations, files containing the resolved dependency trees have to be created prior to scanning. Those depend on the package manager used. OpenText Core SCA tries to generate the lacking files, which can negatively affect speed and accuracy.

**Example 1:** If [**npm**](https://www.npmjs.com/) is used in your project you will have a package.json file, but in order to scan all your dependencies, OpenText Core SCA requires either package-lock.json or yarn.lock as well.

**Example 2:** If [**Maven**](https://maven.apache.org/) is used in your project, you will have a "pom.xml" file, but in order to resolve all your dependencies, OpenText Core SCA requires a second file, as Maven does not offer a lock file system. Instead, "Maven dependency:tree" plugin can be used to create a file called "*.debricked-maven-dependencies.tgf".*

1. Add the [template](http://github.com/debricked/cli/tree/main/examples/templates/Azure) to your "azure-pipelines.yml" file (if the file does not exist, create one)

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/Azure/azure-pipelines.yml>" %}

2. Commit your changes to "azure-pipelines.yml" and watch the CI run.

#### Configure Azure pipelines - video guide <a href="#configureazurepipelines-videoguide" id="configureazurepipelines-videoguide"></a>

{% embed url="<https://www.youtube.com/watch?v=-k39oFJGE-I>" %}

### Integrate multiple repositories <a href="#integratemultiplerepositories" id="integratemultiplerepositories"></a>

Integrating many repositories with one configuration using Azure DevOps can greatly simplify the process of managing and deploying code across multiple projects.

#### Step 1: Create a variable group <a href="#step1-createavariablegroup" id="step1-createavariablegroup"></a>

To avoid having to add the `DEBRICKED_TOKEN` to every integrated repository, it is possible to share the OpenText Core SCA token between repositories. In order to enable this, you should create a variable group:

1. [Generate a OpenText Core SCA access token](https://docs.debricked.com/product/administration/generate-access-token).
2. Sign into your organization and select your project.
3. Go to **Pipelines** → **Library** → **Variable groups**.
4. Click **+ Variable group**.
5. Enter a suitable name for your variable group, for example, "OpenText Core SCA”.
6. Click **+ Add**.
7. Add your token to a secret variable called `DEBRICKED_TOKEN` (to make it secret, toggle the "lock" icon at the end of the row).
8. Click **Save**.
9. Go to the **Pipeline permissions** tab.
10. Click the three vertical dots and choose **Open access** to allow access in all pipelines. If you want to, it is also possible to just specify specific pipelines who should get access. After this, you can use the created variable in your repository pipelines.

#### Step 2: Create new service connection <a href="#step2-createnewserviceconnection" id="step2-createnewserviceconnection"></a>

If you would like to use our shared template out-of-the box without modifications, you should first create a service connection to GitHub. If you are, however, planning on copying the main template into your own organization you can skip this step.

1. Go to **Project settings** → **Service connections**.
2. Click **Create service connection**.
3. Select **Github** from the list and click **Next**.
4. Under **OAuth Configuration** drop-down, select **AzurePipelines**.
5. Click **Authorize** and follow instructions, using your own GitHub account.
6. Give new service connection name, which you will use as a value for ***endpoint*** parameter later on
7. Click **Save**.

#### Step 3: Use template in pipelines of required repositories <a href="#step3-usethetemplateinpipelinesofrequiredrepositories" id="step3-usethetemplateinpipelinesofrequiredrepositories"></a>

You can now use the following template in pipelines of repositories you want to integrate with OpenText Core SCA. The triggering template refers directly to the [**Azure DevOps template**](https://github.com/debricked/cli/blob/main/examples/templates/Azure/azure-pipelines.yml) core repository found in the OpenText Core SCA CLI repository. If you want to make modifications to it, it is also possible to copy the template from the CLI repository into a core repository of your own, which you would then refer to in the triggering template below.

NOTE: During the first run of the pipeline, you will be asked permission to run the subsequent jobs. You should click **Permit.**

#### Triggering template <a href="#triggeringtemplate" id="triggeringtemplate"></a>

```bash
trigger:
  branches:
    include:
      - '*' # Run on all branches

variables:
  - group: <variable_group_name>

resources:
  repositories:
    - repository: <repository_reference>
      type: <repository_type>
      name: <username_or_project>/<repository_name>
      endpoint: <service_connection_name>

jobs:
  - template: <resource_template_file_name>@<repository_reference>
    parameters:
      DEBRICKED_TOKEN: $(DEBRICKED_TOKEN)
```

#### Option 1: Directly referencing the OpenText Core SCA core repository <a href="#option1-directlyreferencingthedebrickedcorerepository" id="option1-directlyreferencingthedebrickedcorerepository"></a>

By directly referencing the OpenText Core SCA core repository, you will automatically receive any new updates made to the OpenText Core SCA core repository template. If you want to customize the template, use the setup described in option 2 below.

1. In the repositories that you want to trigger the shared pipeline from, paste the triggering template above to an azure pipelines yaml file.
2. Fill in the variables to match the OpenText Core SCA core repository according to the list below. If youare not using the variable group from step 1, remove the ***variables*** section from the triggering template:
   * \<variable\_group\_name> - The name of the variable group created in step 1.
   * \<repository\_reference> - The named reference of your choice.
   * \<repository\_type> -  github
   * \<username\_or\_project> - debricked
   * \<repository\_name> - cli
   * \<service\_connection\_name> - The name of the service connection created in step 2.
   * \<resource\_template\_file\_name> -  examples/templates/Azure/azure-pipelines.yml

#### Option 2: Using your own core repository in Azure DevOps <a href="#option2-usingyourowncorerepositoryinazuredevops" id="option2-usingyourowncorerepositoryinazuredevops"></a>

By using your own core repository containing the template in Azure DevOps, you do not need to create a service connection and can customise the template to your liking.

1. Create a new repository in your organisation or use an already existing one as the core.
2. Paste the OpenText Core SCA template contents from [the OpenText Core SCA template](https://github.com/debricked/cli/blob/main/examples/templates/Azure/azure-pipelines.yml) into an "azure pipelines yaml" file:

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/Azure/azure-pipelines.yml>" %}

3. If you want to set up scanning in this repository as well and want to use the variable group from step 1, add the ***variables*** section from the triggering template above into the template under the “debricked\_scan” job.
4. In the repositories that you want to trigger the shared pipeline from, paste the triggering template above to an "azure pipelines yaml" file. If you are not using a service connection, you should remove the ***endpoint*** variable from the triggering template.
5. Fill in the variables to match the chosen core repository according to the list below. If you are not using the variable group from step 1, remove the ***variables*** section from the triggering template:
   * \<variable\_group\_name> - The name of the variable group created in step 1.
   * \<repository\_reference> - The named reference of your choice.
   * \<repository\_type> - git
   * \<username\_or\_project> - The name of the azure project containing your core repository.
   * \<repository\_name> - The name of the core repository.
   * \<service\_connection\_name> - This variable is not needed if the core repository exists in your organisation. Remove the endpoint variable.
   * \<resource\_template\_file\_name> - The path or name to the template file in your core repository.

### Credentials for pull requests <a href="#credentialsforpullrequests" id="credentialsforpullrequests"></a>

OpenText Core SCA can generate pull requests for you, but to be able to use it in Azure DevOps, you should provide the credentials so that the pull request can be created on your Azure DevOps instance.

You can generate a Personal access token by going to the **User settings** -> **Personal access** tokens. You should:

1. Select your organization (or you can create a token for all accessible organizations).
2. Set custom expiration date to the maximum possible value.
3. Grant the token the code (read, write and manage) scope. When you try to create a Pull Request inside the OpenText Core SCA tool, it will automatically ask you for your credentials when needed.
4. Fill out the form:

* Host: enter the domain, e.g.: "<https://dev.azure.com/>", "<https://azure.yourcompany.com>", "<https://org.visualstudio.com>"
* Token: enter the personal access token created before and enter

7. After clicking **Confirm**, the merge request generation will start.

#### Opening a OpenText Core SCA generated pull request on Azure DevOps - video guide <a href="#openingadebrickedgeneratedpullrequestonazuredevops-videoguide" id="openingadebrickedgeneratedpullrequestonazuredevops-videoguide"></a>

{% embed url="<https://www.youtube.com/watch?v=lvMDlE65LGw>" %}
