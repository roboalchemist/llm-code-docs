# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/gradle-private-packages.md

# Gradle - Private Packages

If your repo is using private packages, Aikido needs access to the private package repositories in order to create a Gradle lockfile or to update your Gradle dependencies. You can configure environment variables in Aikido to authenticate to the private package respositories.

## Configuration in Aikido

You can configure Aikido to authenticate with your private registry by following the steps below:<br>

1. Go to your account's settings page for AutoFix, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on “Connect Registry”, the configuration modal will now be shown.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FYFWXexDS4Gx3i7om01g6%2Fimage.png?alt=media&#x26;token=b12aa66b-e89a-4137-af11-eb975a34abfe" alt=""><figcaption></figcaption></figure>

3. Select the “Gradle” section.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FqSGSMW9BfcAlaTEaB32p%2Fimage.png?alt=media&#x26;token=5f3d25bc-0812-4970-91d9-3b7968395f35" alt=""><figcaption></figcaption></figure>

4. Add the environment variables required for your build file as your identifier for where your private registry is stored. All environment variables that contain `GRADLE` are allowed.
5. Make sure these environment variables match your `build.gradle`  file
6. Click “*Connect Registry*” to save the configuration.<br>

Aikido will now use these environment variables when creating Gradle lockfiles or updating your Gradle dependencies.
