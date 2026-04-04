# Source: https://docs.debricked.com/tips-and-tricks/debricked-cli-migration-guide.md

# OpenText Core SCA CLI migration guide

The Legacy CLI has now been officially deprecated. Going forward, all the efforts and enhancements will be dedicated solely to the new OpenText Core SCA CLI. Thus, OpenText Core SCA strongly recommends and encourages your transition to the new CLI in order to stay aligned with the latest features and improvements.\
Read on to find out why you should migrate to the new CLI and what actions are needed from your side.

### **Advantages of new CLI**

The new OpenText Core SCA CLI is distributed as a self-contained binary, removing the need for a PHP environment. This makes it easier to install, integrate, run, and upgrade. Following are the new functionalities and improvements made the new CLI:

* Automatic application of git metadata to scans
* Faster scanning\*: Finding and uploading files is now significantly faster
* Improved call graph generation for vulnerable functionality
* Manifest-less/fingerprint matching&#x20;

\*In the new CLI, a new cutting-edge technology: [High Performance Scans](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) is incorporated . This technology enables you to accurately and swiftly resolve full dependency trees for repositories without a lock file.

### **Migration to new CLI**

Migration to the new CLI is a simple process, but the pipeline configuration needed will differ depending on your CI/CD tool. OpenText Core SCA has created templates using the new CLI for all natively supported integrations. With the new CLI it is also easier than before to set up an integration with a non-natively supported CI/CD tool. The templates for setting up the integration can be found below. If you need help in setting up your migration, do not hesitate to [contact OpenText Core SCA support team](https://docs.debricked.com/overview/help) which will help you get set up with the new CLI.

* **GitHub actions**
  * [GitHub example template](https://github.com/debricked/cli/blob/main/examples/templates/GitHub/debricked.yml)
  * To integrate several repositories with a single configuration check out [this page](https://docs.debricked.com/tools-and-integrations/integrations/github#integratemultiple-repositories)
* **Azure DevOps**
  * [Azure example template](https://github.com/debricked/cli/blob/main/examples/templates/Azure/azure-pipelines.yml)
  * To integrate several repositories with a single configuration check out [this page](https://docs.debricked.com/tools-and-integrations/integrations/azure-devops#integratemultiplerepositories)
* **GitLab CICD**
  * [GitLab example template](https://github.com/debricked/cli/blob/main/examples/templates/GitLab/gitlab-ci.yml)
  * To integrate several repositories with a single configuration check out [this page](https://docs.debricked.com/tools-and-integrations/integrations/gitlab#integratemanyrepositoriesusingoneconfigurationwithgitlab)
* **Bitbucket**
  * [Bitbucket example template](https://github.com/debricked/cli/blob/main/examples/templates/Bitbucket/bitbucket-pipelines.yml)
  * To integrate several repositories with a single configuration check out [this page](https://docs.debricked.com/tools-and-integrations/integrations/bitbucket#integratemultiplerepositories)
* **Argo**
  * [Argo example template](https://github.com/debricked/cli/blob/main/examples/templates/Argo/argo.yml)
* **Travis**
  * [Travis example template](https://github.com/debricked/cli/blob/main/examples/templates/Travis/travis.yml)
* **CircleCI**
  * [CircleCI example template](https://github.com/debricked/cli/blob/main/examples/templates/CircleCI/config.yml)
* **Jenkins**
  * [Jenkins example template](https://github.com/debricked/cli/blob/main/examples/templates/Jenkins/Jenkinsfile)
* **BuildKite**
  * [BuildKite example template](https://github.com/debricked/cli/blob/main/examples/templates/BuildKite/pipeline.yml)
* **Other**, If your CI/CD tool is not mentioned above
  * Because the CLI is distributed as a self-contained binary, using it in your CI/CD is often as simple as downloading the binary and running \`debricked scan\`. An example of how that script might look, using a linux based CI/CD setup, can be found below.

    ```bash
    - curl -L https://github.com/debricked/cli/releases/download/release-v1/cli_linux_x86_64.tar.gz | tar -xz debricked
    - ./debricked scan
    ```
