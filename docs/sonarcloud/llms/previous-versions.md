# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/resources/previous-versions.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/resources/previous-versions.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/resources/previous-versions.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/resources/previous-versions.md

# Previous versions

Please remember that Sonar officially supports only the latest version of [VS Code](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/6LPRABg3ubAJhpfR5K0Y/ "mention").

In version 4.13.0, *SonarLint for VS Code* was renamed *SonarQube for VS Code*. Below, we’ve retained the name *SonarLint* when appropriate because it is what you should see in that version of the extension.

### Installing previous versions <a href="#installing-previous-versions" id="installing-previous-versions"></a>

A limited version history is available on the **Version History** tab of the [SonarQube for VS Code Marketplace page](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode).

Installation of an earlier version is possible by downloading the appropriate asset from the [Releases](https://github.com/SonarSource/sonarlint-vscode/releases) page before following the [offline-installation](https://docs.sonarsource.com/sonarqube-for-vs-code/getting-started/offline-installation "mention") instructions.

### Legacy Connected Mode <a href="#legacy-connected-mode" id="legacy-connected-mode"></a>

#### SonarLint v3.6-v3.7 <a href="#sonarlint-v36v37" id="sonarlint-v36v37"></a>

Starting from v3.6 of SonarLint for VSCode, to set up SonarQube Server or SonarQube Cloud connections, open a **SONARLINT CONNECTED MODE** view in VSCode.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-a276f8b657bf51a0d91c4575cd7deedea8b9d374%2F6f40f05646df2b38d207b04ccf55c7d25ca4350d.png?alt=media" alt="Adding a SonarQube or SonarCloud connection is easy when using the connection wizard." width="363"><figcaption></figcaption></figure></div>

Select either **Add SonarQube Connection** or **Add SonarCloud Connection**, and complete the fields.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-6ac2b2f599c36f02bb6bd5469be0b6dc9aefd390%2Ff167155f7a2235c9719d49691887e6fd0adde04f.png?alt=media" alt="Add the SonarQube server details to set up your connection with SonarLint." width="375"><figcaption></figcaption></figure></div>

For SonarQube connections, provide your **SonarQube Server URL** and **User Token**. For SonarCloud connections, provide your **Organization Key** and **User Token**. User Tokens should be generated on the SonarQube/SonarCloud side and pasted into the **User Token field**.

User Tokens can be generated using these pages:

* SonarQube - `https://<your-sonarqube-url>/account/security/`
* SonarCloud - `https://sonarcloud.io/account/security/`

**Connection Name** is a friendly name for your connections. In the case of multiple connections, it also acts as a `connectionId`.

SonarLint for VSCode v3.6 and above has the option to enable/disable **Receive notifications** when starting a new connection. Notifications can also be enabled/disabled from the UI while editing the connection setting (see next image below). Action buttons used to edit/delete existing, or create additional connections will be revealed in the UI when hovering over each connection.

Select **Save Connection** and verify that the new connection was set up successfully in the Connected Mode view.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-1e740478ba50d5149fb818b99f271693878f7790%2F13f5b33d486a720fd936ae99841a3d41476bc05f.png?alt=media" alt="Your active connections are available in the SonarLint Connected Mode tab." width="240"><figcaption></figcaption></figure></div>

Action buttons to edit/delete existing, or create additional connections will be revealed when hovering over each connection.

**Project binding v3.6-3.7**

Establish your SONARLINT CONNECTED MODE as described above.

Project Bindings can be configured either at the workspace level or in every workspace folder by modifying the `settings.json` file. Example:

```json
{
    "sonarlint.connectedMode.project": {
        "projectKey": "the-project-key"
    }
}
```

If you plan to use multiple connections to different SonarQube servers and/or SonarQube Cloud organizations, simply give a unique `connectionId` to each entry and use them as reference in the binding. Example:

```json
// In project1/.vscode/settings.json
{
    "sonarlint.connectedMode.project": {
        "connectionId": "mySonar",
        "projectKey": "the-project-key-on-sq"
    }
}

// In project2/.vscode/settings.json
{
    "sonarlint.connectedMode.project": {
        "connectionId": "myOrgOnSonarCloud",
        "projectKey": "the-project-key-on-sc"
    }
}
```

#### SonarLint v3.5.4 and lower <a href="#sonarlint-v354-and-lower" id="sonarlint-v354-and-lower"></a>

Connection details should be configured in the VSCode user settings (user token, SonarQube Server URL, or SonarQube Cloud organization). For security reasons, the token should not be stored in SCM with workspace settings (why we suggest configuring in VSCode user settings).

Example for SonarQube Server:

```json
{
    "sonarlint.connectedMode.connections.sonarqube": [
        { 
            "serverUrl": "https://sonarqube.mycompany.com",
            "token": "<generated from SonarQube account/security page>" 
        }
    ]
}
```

Example for SonarCloud:

```json
{
    "sonarlint.connectedMode.connections.sonarcloud": [
        { 
            "organizationKey": "myOrg", 
            "token": "<generated from https://sonarcloud.io/account/security/>"
        }
    ]
}
```

Notifications from your project’s Quality Gate can be toggled using the `disableNotifications` field in a server connection definition.

**Project binding v3.5.4 and lower**

SonarLint v3.5.4 and earlier allows bindings either at the workspace level, or at each workspace folder. Example:

```json
{
    "sonarlint.connectedMode.project": {
        "projectKey": "the-project-key"
    }
}
```

If you plan to use multiple connections, to different SonarQube servers and/or SonarQube Cloud organizations, simply give a unique `connectionId` to each entry, and use them as reference in the binding. Example:

```json
// In user settings
{
    "sonarlint.connectedMode.connections.sonarqube": [
        {
            "connectionId": "mySonar",
            "serverUrl": "https://sonarqube.mycompany.com",
            "token": "xxx"
        }
    ]
    "sonarlint.connectedMode.connections.sonarcloud": [
        {
            "connectionId": "myOrgOnSonarCloud",
            "organizationKey": "myOrg",
            "token": "yyy"
        }
    ]
}

// In project1/.vscode/settings.json
{
    "sonarlint.connectedMode.project": {
        "connectionId": "mySonar",
        "projectKey": "the-project-key-on-sq"
    }
}

// In project2/.vscode/settings.json
{
    "sonarlint.connectedMode.project": {
        "connectionId": "myOrgOnSonarCloud",
        "projectKey": "the-project-key-on-sc"
    }
}
```
