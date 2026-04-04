# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/rpg.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/rpg.md

# RPG

This language is available only in the SonarQube Cloud Enterprise plan. See the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") page for more details.

### Supported versions

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

RPG IV (ILE RPG) for IBM™ i Version >= V3R1 <= 7.3 are fully supported<sup>1</sup>

RPG IV (ILE RPG) for IBM™ i Version > 7.3 are supported<sup>1</sup>

<sup>1</sup> : Free-form partial and full formats are supported.

### Language specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the RPG-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **RPG**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Source code extraction <a href="#source-code-extraction" id="source-code-extraction"></a>

In order to analyze your source code with SonarQube Cloud you need to first extract it onto a file system. You can use your own tool or an open-source tool; Sonar does not provide any connectors or source code extraction tools.

### RPG source format <a href="#rpg-source-format" id="rpg-source-format"></a>

Depending on your extraction process, your RPG source files may include an extra margin on the left of the 80 columns used for code. This margin is in addition to the standard margin which takes up characters 1-5 in the 80-character source format (when "fully free-form" is not used). The extra margin is controlled through the `sonar.rpg.leftMarginWidth` property. By default, it is set to 12, which is the size of the margin in an IBM "source physical file". If your RPG source files do not contain such a margin, you should set `sonar.rpg.leftMarginWidth` to `0`.

You can find an [example file](https://github.com/SonarSource/sonar-scanning-examples/blob/master/sonar-scanner/src/rpg/MYPROGRAM.rpg) illustrating a 12-character margin in our sample project.

You should also make sure to set `sonar.sourceEncoding` to the appropriate encoding. Please check the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for details.

### Free-Form Support <a href="#free-form-support" id="free-form-support"></a>

Free-form is supported for all kinds of specifications and SQL statements that exist in IBM i 7.4. Fully free-form code (starting with `**FREE`) is also supported.
