# Source: https://docs.sonarsource.com/sonarqube-mcp-server/build-and-configure/build.md

# Build your SonarQube MCP Server

As described in the [#mcp-server-setup-in-your-ide](https://docs.sonarsource.com/sonarqube-mcp-server/quickstart-guide#mcp-server-setup-in-your-ide "mention"), launching the SonarQube MCP server is most easily done using the container image. However, you do have other options.&#x20;

### Build locally

We recommend setting up the SonarQube MCP Server with the container image as explained in the [#launch-the-server-from-the-container-image](https://docs.sonarsource.com/sonarqube-mcp-server/quickstart-guide#launch-the-server-from-the-container-image "mention") article, but if you want to build it locally, check out the [#prerequisites](https://docs.sonarsource.com/sonarqube-mcp-server/readme#prerequisites "mention"), then follow these steps:

1. Clone the SonarQube MCP Server project from the [sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) repository.
2. Run the following Gradle command to clean the project and build the application:\
   ./gradlew clean build -x test. The JAR file will be created in `build/libs/`.
3. Perform the manual installation as explained below.

If you prefer, the JAR file is downloadable as an **Asset** on the [MCP server Releases page](https://github.com/SonarSource/sonarqube-mcp-server/releases).

### Manual installation

After you’ve built the SonarQube MCP Server locally, you’ll need to manually install it in your MCP client. Add the following to your MCP configuration’s JSON file.&#x20;

The main difference between the server setup of SonarQube Cloud and SonarQube server is:

* SonarQube Cloud requires a User token and an organization name.
* SonarQube Server and SonarQube Community Build require a User token and server URL.

{% tabs %}
{% tab title="SONARQUBE CLOUD" %}

```json
{
  "sonarqube": {
    "command": "java",
    "args": [
        "-jar",
        "<PathToYourSonarQubeMCPServerJAR>"
    ],
    "env": {
        "STORAGE_PATH": "<PathToYourMCPStorage>",
        "SONARQUBE_TOKEN": "<YourSonarQubeUserToken>",
        "SONARQUBE_ORG": "<YourOrganization>"
    }
  }
}
```

{% hint style="warning" %}
*User tokens* are required when setting up connected mode or an MCP Server between SonarQube (Server, Cloud) and SonarQube for IDE. Note that the binding will not function properly if *project tokens*, *global tokens*, or *scoped organization tokens* are used during the setup process.
{% endhint %}
{% endtab %}

{% tab title="SONARQUBE SERVER" %}

```json
{
  "sonarqube": {
    "command": "java",
    "args": [
        "-jar",
        "<PathToYourSonarQubeMCPServerJAR>"
    ],
    "env": {
        "STORAGE_PATH": "<PathToYourMCPStorage>",
        "SONARQUBE_TOKEN": "<YourSonarQubeUserToken>",
        "SONARQUBE_URL": "<YourSonarQubeURL>"
    }
  }
}
```

{% hint style="warning" %}
*User tokens* are required when setting up connected mode or an MCP Server between SonarQube (Server, Cloud) and SonarQube for IDE. Note that the binding will not function properly if *project tokens*, *global tokens*, or *scoped organization tokens* are used during the setup process.
{% endhint %}
{% endtab %}
{% endtabs %}

### Deployment options.&#x20;

Depending on your user environment, you may want to deploy your MCP server in different ways. Check out the page about configuring your server and pick the right [#transport-mode](https://docs.sonarsource.com/sonarqube-mcp-server/configure#transport-mode "mention") for you.
