# Source: https://docs.debricked.com/tools-and-integrations/integrations/bitbucket.md

# Bitbucket

With CI integration to Bitbucket you can upload your latest commits and pull requests to OpenText Core SCA automatically, or whenever you run your pipeline.

### **Integrate a single repository** <a href="#integrateasinglerepository" id="integrateasinglerepository"></a>

1. Start by [generating an access token](https://docs.debricked.com/product/administration/generate-access-token). Copy the token so that you can use it in the next step.
2. Configure your DEBRICKED\_TOKEN by going to your **repository -> Repository settings -> Repository variables**.
3. Paste in the access token from the previous step. Make sure to secure the token, so that it does not show in the logs.
4. Go to your repository and add the following template to your "bitbucket-pipelines.yml" file (if the file doesn't exist, create one):

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/Bitbucket/bitbucket-pipelines.yml>" %}

5. Commit your changes to "bitbucket-pipelines.yml" and watch the CI run.

Example output:&#x20;

For more information on Bitbucket Pipes, please visit <https://bitbucket.org/product/features/pipelines>

### **Integrate multiple repositories** <a href="#integratemultiplerepositories" id="integratemultiplerepositories"></a>

> *Note that this functionality is only available on the Bitbucket Premium plan.*

Integrating many repositories with one configuration using Bitbucket can greatly simplify the process of managing and deploying code across multiple projects.

You can set this up with shared pipeline configurations:

**Step 1: Create a Workspace variable**

To avoid having to add the DEBRICKED\_TOKEN to every integrated repository, it is possible to share the Debricked token between repositories. In order to enable this, you need to create a Workspace variable. **Note**: This can only be done by administrators:

1. [Generate a Debricked access token](https://docs.debricked.com/product/administration/generate-access-token).
2. Sign in to your organization.
3. From your profile avatar, select a workspace.
4. Click the **Settings** cog on the top navigation bar.
5. Click **Workspace settings** from the **Settings** drop-down menu.
6. In the menu on the left, go to **Pipelines** > **Workspace variables**.
7. Add your token to a secured variable called DEBRICKED\_TOKEN.

**Step 2: Create a repository for the shared pipeline definition**

Set up a repository within your workspace for the shared pipeline definition:

1. Create a new repository in your workspace or enter an already existing one.
2. Create a "bitbucket pipelines yaml" file and paste the Debricked template contents. By default, the template sets up scanning in this repository as well. It is, however, possible to deactivate this, by removing or commenting out the bottom pipelines definition (rows 17-19):

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/Bitbucket/bitbucket-pipelines.yml>" %}

**Step 3: Set up a reference to the shared pipeline definition in the required repositories**

The final step is to set up the reference template for all repositories you would like to integrate with Debricked.

1. Create a "bitbucket pipelines yaml" file in the repository that will reference the shared pipeline definition and paste the contents below.
2. Adjust the references to point to the repository and branch containing the file created in step 2:

```bash
pipelines:
  default:
    running-debricked-scan:
      import: <repository_name>:<branch_name>:debricked-scan
```
