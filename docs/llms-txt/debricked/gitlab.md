# Source: https://docs.debricked.com/tools-and-integrations/integrations/gitlab.md

# GitLab

With CI integration to GitLab you can automatically upload your latest commits and pull requests to OpenText Core SCA whenever you run your pipeline. Our GitLab integration support the same options as our Bitbucket integration, read more about the options here: <https://bitbucket.org/debricked/debricked-scan>

OpenText Core SCA supports both the cloud version and the self-hosted version of GitLab.

### **Configure** OpenText Core SCA **token** <a href="#configuredebrickedtoken" id="configuredebrickedtoken"></a>

Start by [generating an access token](https://docs.debricked.com/product/administration/generate-access-token). Copy the token so that you can use it in the next step.

Configure your *DEBRICKED\_TOKEN*:

1. Go to your **Repository**.
2. Go to **Settings** -> **CI/CD**.
3. Expand the **Variables** field.
4. Paste in the access token from the previous step. Make sure to mask the token, so that it does not show in the logs.

### **Configure GitLab CI or CD job** <a href="#configuregitlabci-cdjob" id="configuregitlabci-cdjob"></a>

Depending on what package manager you are using there are different job setups.

In order for us to analyze all dependencies in your project, their versions, and relations, files containing the resolved dependency trees have to be created prior to scanning. Those depend on the package manager used. If files are lacking, OpenText Core SCA tries to generate the lacking files, which can negatively affect speed and accuracy.

**Example 1:** If [**npm**](https://www.npmjs.com/) is used in your project you will have a "package.json" file, but in order for us to scan all your dependencies, OpenText Core SCA requires either "package-lock.json" or "yarn.lock" as well.

**Example 2:** If [**Maven**](https://maven.apache.org/) is used in your project, you will have a pom.xml file, but in order for us to resolve all your dependencies, OpenText Core SCA requires a second file, as Maven does not offer a lock file system. Instead, "Maven dependency:tree" plugin can be used to create a file called "*.debricked-maven-dependencies.tgf".*

1. Add the template to your "*.gitlab-ci.yml"* file (if the file does not exist, create one).

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/GitLab/gitlab-ci.yml>" %}

2. Commit your changes to "*.gitlab-ci.yml"* and watch the CI run.

### Integrate many repositories using one configuration with GitLab <a href="#integratemanyrepositoriesusingoneconfigurationwithgitlab" id="integratemanyrepositoriesusingoneconfigurationwithgitlab"></a>

Integrating many repositories with one configuration using GitLab can greatly simplify the process of managing and deploying code across multiple projects.

You can set this up with multi-project pipelines:

1. Start [generating an access token](https://docs.debricked.com/product/administration/generate-access-token).
2. In GitLab, create a file in a new or existing repository and paste the OpenText Core SCA template:

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/GitLab/gitlab-ci.yml>" %}

3. To avoid having to add the `DEBRICKED_TOKEN` to every integrated repository, it is possible to set up the token as a *var* for either:\
   \- [a group of projects](https://docs.gitlab.com/ee/ci/variables/#for-a-group)\
   \- [your entire instance](https://docs.gitlab.com/ee/ci/variables/#for-an-instance)
4. Trigger it in target project(s) by adding the following code and adjusting the reference to point to the file created in step 2:

   ```bash
   debricked-scan:
     trigger:
       include:
         - project: '<org_name>/<repository_name>'
           ref: '<branch_name>'
           file: '/path/to/file.gitlab-ci.yml'
   	strategy: depend
   ```

   &#x20;
5. The process is complete.

### **Credentials for merge requests** <a href="#credentialsformergerequests" id="credentialsformergerequests"></a>

Debricked can generate merge requests for you, but to be able to use it in GitLab, you should provide the credentials, so that the merge requests can be created on your GitLab instance.

You can use either:

* Personal access tokens
* Project-scoped access tokens (currently available in paid versions of Gitlab), unique for every project

You can generate a Personal access token by going to the **User settings**. You should grant the token the API scope.

Then when you try to create a Merge Request inside the Debricked tool, it will automatically ask you for your credentials when needed.

After clicking **Confirm**, the merge request generation should start.
