# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/html.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/html.md

# HTML

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the HTML-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **HTML**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### PHP code analysis <a href="#php-code-analysis" id="php-code-analysis"></a>

PHP and HTML analyzers both analyze files with extensions: `.php`, `.php3`, `.php4`, `.php5`, `.phtml`.

File metrics, such as the number of lines of code, can only be measured by one of the languages, PHP or HTML. They are handled by the PHP analyzer by default, and by HTML analyzer if for some reason the former is not present.

The HTML analyzer inspects PHP files even if the PHP file extensions are not included in the list of file extensions to analyze.
