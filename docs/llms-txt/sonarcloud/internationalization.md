# Source: https://docs.sonarsource.com/sonarqube-community-build/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/extension-guide/internationalization.md

# Source: https://docs.sonarsource.com/sonarqube-server/extension-guide/internationalization.md

# Internationalization

This page gives guidelines to i10n for:

* Plugin developers who would like to apply the i18n mechanism in their own plugins, so that these plugins can be available in several languages.
* People who would like to help the community by making the platform available in a new language.

### Principles <a href="#principles" id="principles"></a>

Although the basics of the i18n mechanism are the same for every part of the ecosystem, the packaging differs depending on what you are developing:

* Translations for SonarQube Server: making SonarQube Server available in a new language requires you to develop and publish a new language pack plugin.
  * By default, SonarQube Server embeds the English pack.
  * All other language pack plugins, like the French pack plugin, are maintained by the community and are available through the Marketplace (category "Localization").
* Translations for the SonarQube community plugins: open-source plugins from the SonarQube community must embed only the bundles for the default locale (en). Translations will be done in the language pack plugins.
* Translations for other plugins: closed-source/commercial/independent plugins must embed the bundles for the default locale and the translations for every language they want to support.
* After installing a language, users must change their browser language to see the changes reflected in their plugins.

### Translation bundles <a href="#translation-bundles" id="translation-bundles"></a>

Localized messages are stored in properties files:

* These are regular properties files with key/value pairs where you put most translations
* These files must be stored in the org.sonar.l10n package (usually in the `src/main/resources/org/sonar/l10n` directory)
* The names of these files must follow the convention `<key of the plugin to translate>_<language>.properties`, for example `widgetlabs_fr.properties` or `core_fr.properties` for the core bundle. See `sonar-packaging-maven-plugin` for details on plugin key derivation.
* Messages can accept arguments. Such entries would look like:
  * `myplugin.foo=This is a message with 2 params: the first "{0}" and the second "{1}".`
* Messages can accept pluralization. Such entries would look like:
  * `myplugin.foo={x, number} {x, plural, one {thing} other {things}}`
  * We use it for example with a combination of 2 labels: `component_navigation.last_analysis_had_warnings=Last analysis had {warnings}` and `component_navigation.x_warnings={warningsCount, number} {warningsCount, plural, one {warning} other {warnings}}`. This renders `Last analysis had 1 warning` if `warningsCount` equals 1 and `Last analysis had 2 warnings` otherwise, in this case 2.
  * Learn more about this syntax [here](https://formatjs.io/docs/core-concepts/icu-syntax/).

{% hint style="warning" %}
**UTF-8 encoding**\
In the Java API, properties files are supposed to be encoded in ISO-8859 charset. Without good tooling, it can be quite annoying to write translations for languages that do not fit in this charset. This is why we decided to encode the properties files in UTF-8, and let Maven turn them into ASCII at build time thanks to native2ascii-maven-plugin (check the French plugin pom.xml). This makes the process of writing translations with a standard editor far easier.
{% endhint %}

#### How to read localized messages from a plugin extension? <a href="#how-to-read-localized-messages-from-a-plugin-extension" id="how-to-read-localized-messages-from-a-plugin-extension"></a>

The component `org.sonar.api.i18n.I18n` is available for web server extensions. Scanner extensions cannot load bundles.

### Writing a language pack <a href="#writing-a-language-pack" id="writing-a-language-pack"></a>

A language pack defines bundles for SonarQube Server and/or plugins.

#### Creating a language pack <a href="#creating-a-language-pack" id="creating-a-language-pack"></a>

The easiest way to create a new pack is to copy the [Chinese pack](https://github.com/SonarQubeCommunity/sonar-l10n-zh) and adapt it to your language.

#### Maintaining a language pack <a href="#maintaining-a-language-pack" id="maintaining-a-language-pack"></a>

In the pom file, set the versions of SonarQube Server and of the plugins you want to translate. When it’s time to update your language pack for a new version of SonarQube Server or a plugin, the easiest way to see what keys are missing is to run:

`mvn test`

If the build fails, it means that some keys are missing. Go to `target/l10n` to check the reports for each bundle. Missing keys are listed under `Missing translations are:`

```css-79elbk
Missing translations are:
code_viewer.no_info_displayed_due_to_security=Due to security settings, no information can be displayed.
comparison.version.latest=LATEST
...
```

Each time you add a new bundle or update an existing one, please create a JIRA ticket on the corresponding l10n component in order to track changes.

### Localizing a plugin <a href="#localizing-a-plugin" id="localizing-a-plugin"></a>

This section applies if you are developing a closed-source plugin. If your plugin falls in this category, it must embed its own bundles. Bundles must be defined in `src/main/resources/org/sonar/l10n/<plugin key>_<language>.properties`

The default bundle is mandatory and must be in English. For example, the plugin with the key `mysonarplugin` must define the following files in order to enable the French translation:

* `org/sonar/l10n/mysonarplugin.properties`
* `org/sonar/l10n/mysonarplugin_fr.properties`
