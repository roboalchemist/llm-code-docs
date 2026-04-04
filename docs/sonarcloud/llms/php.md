# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/php.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/php.md

# PHP

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

Versions 5.0 to 8.4 are fully supported.

### Supported frameworks and tools <a href="#supported-frameworks-and-tools" id="supported-frameworks-and-tools"></a>

Laravel, Symfony, WordPress, Laminas, and Zend.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the PHP-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **PHP**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Turning issues off <a href="#turning-issues-off" id="turning-issues-off"></a>

The best way to deactivate an individual issue you don’t intend to fix is to mark it as accepted or false positive through the Sonar UI.

If you need to deactivate a rule (or all rules) for an entire file, then issue exclusions are the way to go. But if you only want to deactivate a rule across a subset of a file - all the lines of a method or a class - you can use a PHPDoc comment `/* @SuppressWarnings("php:S2077") */` or an attribute `#[SuppressWarnings("php:S2077")]`.

### Analyze php.ini files <a href="#analyze-phpini-files" id="analyze-phpini-files"></a>

The PHP analyzer can analyze `php.ini` files with some specific rules (if these rules are activated in your quality profile). `php.ini` files must be part of the project you are analyzing, meaning the `php.ini` files have to be inside the directories listed in `sonar.sources`. Rules targeting `php.ini` files can be quickly identified through the ["php-ini"](https://rules.sonarsource.com/php/tag/php-ini) tag set on them.

### Related pages <a href="#related-pages" id="related-pages"></a>

* Test coverage [overview](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/overview "mention")
* [External Analyzer Reports](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports) ([PHPStan](https://phpstan.org/), [Psalm](https://psalm.dev/))
