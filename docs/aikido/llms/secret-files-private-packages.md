# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/secret-files-private-packages.md

# Secret Files - Private packages

For Aikido to update dependencies that include private packages, it needs **access to your private registries** so it can generate accurate lockfile updates.

Many container-based systems (like Kubernetes and Docker) use **Secret Files** that allow you to mount a secret on the filesystem. In Aikido you can provide secrets files, which will be stored encrypted and injected into your workflows.

During Autofix, the Secret File will be written to a temporary file on the filesystem. The path of the temporary file will be stored in the environment variable you provide.

This means when our system detects vulnerabilities in dependencies, it can seamlessly authenticate with private registries, automatically patch the affected packages, and update the lockfiles, all while keeping your credentials safe.

## Configuration in Aikido

Once write access to the repos is set up, you can configure Aikido to authenticate with your private registry by following the steps below:

1. Go to your account's settings page for AutoFix, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on "*Connect registry*" to see the modal below

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F8iBS9g9gW9p7gEgARbx6%2Fimage.png?alt=media&#x26;token=73053209-4347-4b70-a59b-4fa35a388714" alt=""><figcaption></figcaption></figure>

3. When you select *"Secret Files"* you will be able to enter the content of the Secret File and the name of the environment variable that will be used to read the path to the secret file.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FYT6NUI1Nmc6XDAqcAozV%2Fimage.png?alt=media&#x26;token=d054c2a7-547e-47e0-8ccb-73a8e3a41173" alt=""><figcaption></figcaption></figure>

4. Fill in the "Secret Content" and "Environment Variable" and add as many secret files as needed.
