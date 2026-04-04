# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/sonarscanner-for-npm/using-the-sonarscanner-for-npm.md

# Using the SonarScanner for NPM

You can start the [introduction](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/sonarscanner-for-npm/introduction "mention") and thus, integrate it into your CI or build pipeline, in the following ways:

* From the command line.\
  A global mode installation of the scanner is required.
* From the command line with npx.\
  No scanner installation is required.
* By adding the analysis step to your build files.\
  The scanner must be added to the project’s devDependencies.

You can pass analysis parameters in the command line and in the analysis step coded in JS. In addition, the SonarScanner for NPM gets analysis parameters from different other sources: see [configuring-the-analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/sonarscanner-for-npm/configuring-the-analysis-parameters "mention"). To get started, you must configure at a minimum the [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/analysis-parameters "mention") and the [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/analysis-parameters "mention") used to connect to the server.

{% hint style="info" %}
The SonarScanners run on code that is checked out. See [verifying-code-checkout-step](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/various-setups/verifying-code-checkout-step "mention").
{% endhint %}

### Starting the scanner from the command line <a href="#command-line" id="command-line"></a>

1. Make sure the scanner is installed in global mode: see [installing](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/sonarscanner-for-npm/installing "mention").
2. Use the `sonar-scanner` command to start the analysis.\
   To pass analysis parameters in the command line, use the standard `-Dsonar.xxx=yyy` syntax.\
   Example:

```css-79elbk
sonar-scanner -Dsonar.host.url=https://myserver.com -Dsonar.token=019d1e2e04e
```

### Starting the scanner from the command line with npx <a href="#npx" id="npx"></a>

* Use the `npx sonarqube-scanner` command to start the analysis.\
  To pass analysis parameters in the command line, use the standard `-Dsonar.xxx=yyy` syntax.\
  Example:

```css-79elbk
npx sonarqube-scanner -Dsonar.host.url=https://myserver.com -Dsonar.token=019d1e2e04e
```

### Adding the analysis step to your build files <a href="#add-to-build-files" id="add-to-build-files"></a>

1. Make sure the scanner is installed in your project’s devDependencies: see [installing](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/sonarscanner-for-npm/installing "mention").
2. Code the analysis step in JS in your build files, as shown in the example below.

```css-79elbk
const scanner = require('sonarqube-scanner');
scanner(
  {
    serverUrl: 'https://sonarqube.mycompany.com',
    token: '019d1e2e04eefdcd0caee1468f39a45e69d33d3f', 
    options: {
      'sonar.projectName': 'My App',
      'sonar.projectDescription': 'Description for "My App" project...',
      'sonar.sources': 'src',
      'sonar.tests': 'test', 
    },
  },
  () => process.exit(),
);
```

Where the syntax is as follows:

```css-79elbk
sonarqube-scanner ( parameters, [callback] )
```

* parameters (format: Map)
  * serverUrl (format: String; optional): The URL of the SonarQube server. Defaults to the value of the SonarCloud URL (`sonar.scanner.cloudUrl` property).
  * token (format: String; optional): The [generating-and-using-tokens](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/user-account/generating-and-using-tokens "mention") used to connect to the SonarQube server or SonarCloud. Empty by default.
  * options (format: Map; optional): Used to pass extra parameters for the analysis. See [configuring-the-analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/sonarscanner-for-npm/configuring-the-analysis-parameters "mention") for more details.
* callback (format: Function; optional): Callback (the execution of the analysis is asynchronous).
