# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/css.md

# CSS

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

In order to analyze CSS code, you need to have Node.js >= 8 installed on the machine running the scan. Set property `sonar.nodejs.executable` to an absolute path to Node.js executable, if standard `node` is not available.

If you have a community plugin that handles CSS installed on your SonarQube instance it will conflict with analysis of CSS, so it should be removed.

### Language-Specific Properties <a href="#language-specific-properties" id="language-specific-properties"></a>

Discover and update the CSS-specific [properties](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/analysis-parameters) in: **Administration > General Settings > CSS**

### Supported languages <a href="#supported-languages" id="supported-languages"></a>

* CSS, SCSS, Less
* Also ‘style’ inside PHP, HTML and VueJS files

### Related pages <a href="#related-pages" id="related-pages"></a>

* [importing-third-party-issues](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/importing-external-issues/importing-third-party-issues "mention") (StyleLint.io)

### Issue tracker <a href="#issue-tracker" id="issue-tracker"></a>

Check the [issue tracker](https://github.com/SonarSource/sonar-css/issues) for this language.
