# Source: https://docs.datafold.com/integrations/code-repositories/bitbucket.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bitbucket

## 1. Issue an Access Token

### Bitbucket Cloud

To get the [repository access token](https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-access-token/), navigate to your Bitbucket repository settings and create a new token.

When configuring your token, enable following permissions:

* **Pull requests** -> **Write**, so that Datafold can post reports with Data Diff results to pull requests.
* **Webhooks** -> **Read and write**, so that Datafold can configure all webhooks that we need automatically.

<Frame caption="Bitbucket Access Token">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8f59ced50090f42d1c8126a9a816c86a" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a8c5abd09425e95ad760081c3a461fe1 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5956cdaead951b18d186e4fa896f1480 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=597c82abfed30f0c62b2ae780249ffdf 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5f108a2379805bd2202d12826ac7396e 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=75df67fbd366291cb00b18b4a7c0d15f 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_access_token-31e43bcafa70921b2f847623fbc149e5.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ab81b22af16b5f1e373c98f1f86d14d1 2500w" />
</Frame>

### Bitbucket Data Center / Server

To get a [repository access token](https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html), navigate to your Bitbucket repository settings and create a new token.

When configuring your token, enable **Repository admin** permissions.
We need admin access to the repository to be able to post reports with Data Diff results to pull requests, and also configure all necessary webhooks automatically.

<Frame caption="Bitbucket Server Access Token">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=fe7a17de6da297d97624585a9c6415ba" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=24c9641828996ace84a453d73f2fcb79 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a015dacba7bca059ccc2bd0cd2fb0ff5 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5d55f42df68f5f9e804882cdceb00557 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c03ff8b4f2236f7f4efae41ac718ab67 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b1a45716ff752606d26f83f4d4e69b92 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bitbucket_server_access_token-c2504c12d9bef6081251b9eb6aa0b12b.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=59e569fcb832271a9dfc56596828d516 2500w" />
</Frame>

## 2. Configure integration in Datafold

Navigate back to Datafold and fill in the configuration form.

### Bitbucket Cloud

* **Personal/project Access Token**: the token you created in step 1.
* **Repository**: your Bitbucket repository name.
  For example, if your Bitbucket project URL is `https://bitbucket.org/datafold/dbt/`, your Project Name is `datafold/dbt`.

### Bitbucket Data Center / Server

* **Personal/project Access Token**: the token you created in step 1.
* **Repository**: the full URL of your Bitbucket repository.
  For example, `https://bitbucket.myorg.com/projects/datafold/repos/dbt`.
