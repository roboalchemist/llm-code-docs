# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-github-enterprise.md

# Connect GitHub Enterprise (Cloud & Server)

Aikido integrates with [Github Enterprise Cloud](https://docs.github.com/en/get-started/onboarding/getting-started-with-github-enterprise-cloud) and [GitHub Enterprise Server](https://docs.github.com/en/enterprise-server@3.19/admin/overview/about-github-enterprise-server) through a secure, app-based connection. This allows Aikido to access the repositories you choose while keeping full control.

### Installation

Aikido connects to your GitHub Enterprise setup by creating a GitHub App on your server. The app includes the permissions and callbacks needed for Aikido to work. After it is created, you can install it in any organisation on your GitHub Server instance that you want to link to Aikido.\
\
To create the GitHub app on your instance, follow the steps below.

{% stepper %}
{% step %}

### Create your account

If you don’t have an Aikido account yet, create one through Google or Microsoft first. This is required before you can connect your GitHub Enterprise Server.

Open the [setup installation page](https://app.aikido.dev/onboarding/github-server/install-app), enter the URL of your GitHub Enterprise and click `Next, Install App`.

{% hint style="warning" %}
If your GitHub Enterprise Server is not reachable from the internet, enable the Broker setting.

For details about how the Aikido Broker works, [see the documentation.](https://help.aikido.dev/miscellaneous-info/aikido-broker-for-internal-applications)
{% endhint %}

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FwIvfeXwO6TJAZNHOhhEW%2FScreenshot%202025-12-03%20at%2017.05.52.png?alt=media&#x26;token=fb4dffc0-b376-41e3-a820-621817dc3748" alt=""><figcaption></figcaption></figure>

{% endstep %}

{% step %}

### Install Aikido Github App on your Github Enterprise

A file named `install.html` is downloaded to your machine. It contains an HTML page with a form that sends a JSON payload to your GitHub Enterprise to create the GitHub App.

Open the file in your browser and select Install to continue the setup process.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fp9oazDrex1FjdANY139U%2FScreenshot%202025-11-25%20at%2017.41.41.png?alt=media&#x26;token=60c75430-4153-4b2e-85e4-e1e8544bc3cb" alt="" width="375"><figcaption></figcaption></figure>

After clicking "Install" you are redirected to a page on your GitHub Enterprise that prompts you to install the app. Choose `Create GitHub App for User` to create the app on your server.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F2d6VFuX7mrqjK01fHajy%2FScherm%C2%ADafbeelding%202025-11-25%20om%2016.12.59.png?alt=media&#x26;token=207335a2-4cb2-4ff2-a008-2e91913a716b" alt="" width="563"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Authorize Aikido Github app

Now you need to authorize the new GitHub App with your user account through OAuth. This step confirms that the app was created correctly and that you have permission to use it. The screen you see will be similar to the example below.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FJXheF9D7xoNYw13ikbfh%2Ftest.png?alt=media&#x26;token=c65e8924-be12-4fda-848e-0809a1900e4a" alt="" width="375"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Connect Github organization

Choose the GitHub organisation where you want to install the application and link it to Aikido. You can add more organisations later. After selecting the organisation, confirm the authorization for the GitHub App.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FpPKnUuZwjWSh8GPKBCWB%2Ftester.webp?alt=media&#x26;token=7465aa35-8984-4aed-ada7-678cf3708150" alt="" width="375"><figcaption></figcaption></figure>

You are now redirected back to Aikido where you can choose which repositories should be scanned. Select the repositories you want and continue. Aikido will start scanning the chosen applications.
{% endstep %}

{% step %}

### Explore Aikido

After granting access and validating the repositories you want to scan, Aikido will automatically start scanning. After about 1 minute, you should see the first results come in
{% endstep %}
{% endstepper %}

#### Managing the GitHub Enterprise App

{% content-ref url="connect-github-enterprise/connect-additional-organizations-to-aikido" %}
[connect-additional-organizations-to-aikido](https://help.aikido.dev/code-scanning/connect-your-source-code/connect-github-enterprise/connect-additional-organizations-to-aikido)
{% endcontent-ref %}

{% content-ref url="connect-github-enterprise/transferring-ownership-of-the-aikido-app-in-github-enterprise" %}
[transferring-ownership-of-the-aikido-app-in-github-enterprise](https://help.aikido.dev/code-scanning/connect-your-source-code/connect-github-enterprise/transferring-ownership-of-the-aikido-app-in-github-enterprise)
{% endcontent-ref %}
