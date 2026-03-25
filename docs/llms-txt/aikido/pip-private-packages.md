# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/pip-private-packages.md

# PIP - Private Packages

For Aikido to update dependencies that include private packages, it needs access to your private packages so it can generate accurate requirement file updates.  You can provide private git repository configuration in Aikido for this.

## Private PyPI registry <a href="#same-scm-organization" id="same-scm-organization"></a>

You can configure Aikido to authenticate with your private PyPI registry when updating the PIP dependencies by following the steps below:

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on "Connect Registry", the private registry modal will now be shown

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FGhzM7fCGBL95FyC5m0tq%2Fimage.png?alt=media&#x26;token=0a4e34d8-4611-492e-bf37-99c8f1bce789" alt=""><figcaption></figcaption></figure>

3. Select PIP and  provide the index URL to the PyPI registry including the username and password in the following format:

```
https://<username>:<password>@domain.com/repo
```

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FQx0v3agJXg7b1P84AVKx%2Fimage.png?alt=media&#x26;token=01a85d3f-50ea-481e-bf56-62590942c3c4" alt=""><figcaption></figcaption></figure>

4. Click "Connect Registry" to save the configuration.

If the private registry is hosted on **GitHub**, **GitLab**, **BitBucket** or **Azure DevOps**, consult the sections below.

## Private Git repository <a href="#configuration-in-aikido---private-rubygems-repository" id="configuration-in-aikido---private-rubygems-repository"></a>

### Same SCM organization <a href="#same-scm-organization" id="same-scm-organization"></a>

If the private Git repository for the pip is in the same organization as the code being autofixed, make sure your [AutoFix access token](https://app.aikido.dev/issues/fix/settings) has access to the private git repository.

### Different SCM organization <a href="#different-scm-organization" id="different-scm-organization"></a>

You can configure Aikido to authenticate with your private repositories when updating the dependencies by following the steps below:

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/settings/integrations/autofix).
2. Click on "Connect Registry", the configuration modal will now be shown

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FBjmMYpwfYClJ3UGFuZyZ%2Fimage.png?alt=media&#x26;token=fa7d6bcd-c8f6-42fa-94ad-63e7e5e7063b" alt=""><figcaption></figcaption></figure>

3. Select "Environment Variables"

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FubDFOmYcJB5z7ZjQZ4p2%2Fimage.png?alt=media&#x26;token=dc091855-5b6b-4a11-870c-13c090e8c177" alt=""><figcaption></figcaption></figure>

4. In the example above, we show a possible setup for a private GitHub repository. The environment variable key is `PIP_GITHUB__COM`, and the value is a GitHub access token with repository access.

| Provider     | Environment Variable Key | Value Format        |
| ------------ | ------------------------ | ------------------- |
| GitHub       | `PIP_GITHUB__COM`        | `your-access-token` |
| GitLab       | `PIP_GITLAB__COM`        | `your-access-token` |
| Bitbucket    | `PIP_BITBUCKET__ORG`     | `your-access-token` |
| Azure DevOps | `PIP_DEV__AZURE__COM`    | `your-access-token` |

5. Click "Connect Registry" to save the configuration.
