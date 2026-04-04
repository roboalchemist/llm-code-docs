# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/jcl.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/jcl.md

# JCL

JCL analysis is available starting with the Enterprise plan and is supported by SonarQube for Eclipse when running in connected mode. See the[subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") and [Connected mode](https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/connected-mode) pages for more details.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the JCL-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **JCL**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Source code extraction <a href="#source-code-extraction" id="source-code-extraction"></a>

To analyze your source code with SonarQube Cloud, you first need to extract it onto a filesystem. You can use your own tool or an open-source tool; Sonar does not provide any connectors or source code extraction tools.

### JCL source format <a href="#jcl-source-format" id="jcl-source-format"></a>

Depending on your extraction process, your JCL source files may include extra characters beyond the 72nd columns, and include the 8 additional characters up to column 80, or even go beyond that column.

When that happens, the parser will:

* consider everything up to the 71st column as valid JCL code,
* look at the character in the 72nd column, to determine whether a continuation is present or not,
* consider everything beyond the 72nd column as an inline comment, even when the text goes beyond the 80th column.
