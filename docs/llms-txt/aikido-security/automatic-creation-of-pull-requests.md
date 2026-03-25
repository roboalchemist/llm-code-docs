# Source: https://help.aikido.dev/aikido-autofix/automatic-creation-of-pull-requests.md

# Automatic Creation of Pull Requests

Aikido allows for automatic PR creation on a **daily basis**, handling mass upgrades of different versions through lockfile updates. Fine tune the Pull Request title, label and other settings with "PR Configuration"

{% hint style="warning" %}
Automatic creation is currently available for dependencies, containers and pentest autofixes.
{% endhint %}

### Setup automatic creation <a href="#setup-automatic-creation" id="setup-automatic-creation"></a>

**Step 1:** Go to [Autofix Settings](https://app.aikido.dev/issues/fix/settings) page

**Step 2:** Scroll down to Automated PRs. Enable the toggle for 'Autocreation of PRs'<br>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F3mpJkwi7GwZjzPc6DQ3C%2Fimage.png?alt=media&#x26;token=7099003c-6fae-491a-b106-c8f71c18cb61" alt=""><figcaption></figcaption></figure>

**Step 3:** The configuration modal opens. You can enable autocreation for dependencies in code repos, automated fixes for Docker containers or automatically fix pentest issues. Make sure to select code repositories and containers for which you want PRs created.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FiMLt9UzhYrqhq2NgbOaD%2Fimage.png?alt=media&#x26;token=3fd5c2cb-817b-4942-8c1b-8fbdc8f86f9b" alt=""><figcaption></figcaption></figure>

**Step 4:** Test whether new PRs are created correctly by clicking the **Test Autocreation** button.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FvReuPYbcFTyMW3btVQgb%2Fimage.png?alt=media&#x26;token=1ef3fc2e-18fe-4fef-86bc-723ee96bef68" alt=""><figcaption></figcaption></figure>

### Pull Request Configuration <a href="#pull-request-configuration" id="pull-request-configuration"></a>

You can configure pull request properties (such as the title, labels, branch name, and commit message) on the AutoFix PR Configuration page. More docs can be found [here](https://help.aikido.dev/aikido-autofix/configure/autofix-pr-configuration).
