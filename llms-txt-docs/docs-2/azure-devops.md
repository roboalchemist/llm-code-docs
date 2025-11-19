# Source: https://docs.datafold.com/integrations/code-repositories/azure-devops.md

# Azure DevOps

## 1. Issue an Access Token

To get your [repository access token](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=Windows#create-a-pat), navigate to your Azure DevOps settings and create a new token.

When configuring your token, enable following permissions:

* **Code** -> **Read & write**
* **Identity** -> **Read**

We need write access to the repository to post reports with Data Diff results to pull requests, and read access to identities to be able to properly display Azure DevOps users in the Datafold UI.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=79b790bb635c11e7b92e046ff26ff193" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1a9c8b05e52cd7cc63fa37a0856e9eaa 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a9b631782274cc2200e89fd0dbb92ffe 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c7af01cd57c6ce4d42ffe11912e50df7 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=315e5317bf383a490093666fdcb99325 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0a2bdbaf542c8837df118334980bf94b 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure_devops_access_token-7bd79728ae3447aa77f4246a1e66b249.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5855c1335750b1b7ada5081fd672b267 2500w" />
</Frame>

## 2. Configure integration in Datafold

Navigate back to Datafold and fill in the configuration form.

* **Personal/project Access Token**: the token you created in step 1.
* **Organization**: your Azure DevOps organization name.
* **Project**: your Azure DevOps project name.
* **Repository**: your Azure DevOps repository name.

For example, if your Azure DevOps repository URL is `https://dev.azure.com/datafold/analytics/_git/dbt`:

* Your **Organization** is `datafold`
* your **Project** is `analytics`
* your **Repository** is `dbt`
