# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/maintenance/deprecations/deprecation-policy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/maintenance/deprecations/deprecation-policy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/maintenance/deprecations/deprecation-policy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/maintenance/deprecations/deprecation-policy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/maintenance/deprecations/deprecation-policy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/maintenance/deprecations/deprecation-policy.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/deprecations/deprecation-policy.md

# Deprecation policy

### General principles <a href="#general-principles" id="general-principles"></a>

A backward-incompatible change or dropping of a public API endpoint, a workflow, or a feature is subject to the deprecation. Once deprecated, they will be removed in a future version:

* A deprecated feature can be dropped in the year following the year it was deprecated, after the new LTA, with a minimum of 6 months after deprecation.\
  For example, a feature deprecated in the 2025.2 version is kept until the 2026.1 LTA (Long-Term Active) version and dropped in the 2026.2 version or later. See [release-cycle-model](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/release-cycle-model "mention") for more information.
* See below for deprecated Web API or Plugin API components.

### Web API deprecation policy <a href="#deprecation" id="deprecation"></a>

The Web API deprecation policy states that:

* An API component must be deprecated before being dropped. Furthermore, if the underlying feature is not being dropped, a replacement component must immediately be provided.
* A deprecated API component must be fully supported until its drop (For instance the implementation of a deprecated method can’t be replaced by throwing a new UnsupportedOperationException()).
* The API release cycle is tied to the [release-cycle-model](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/release-cycle-model "mention").
* A deprecated API endpoint can be dropped in January of the year following the year it was deprecated, but not before 6 months after deprecation.

{% hint style="info" %}
Under special circumstances, for example, when there are security vulnerabilities that need to be addressed, we might make an exception and drop the deprecated API component earlier.
{% endhint %}

### Plugin API deprecation policy <a href="#plugin-api-deprecation-policy" id="plugin-api-deprecation-policy"></a>

The Plugin API deprecation policy states that:

* An API component must be deprecated before being dropped. Furthermore, if the underlying feature is not being dropped, a replacement component must immediately be provided.
* A deprecated API component must be fully supported until its drop (For instance the implementation of a deprecated method can’t be replaced by throwing a new UnsupportedOperationException()).
* The API is released independently of SonarQube Server (see the [version compatibility matrix](https://github.com/SonarSource/sonar-plugin-api?tab=readme-ov-file#sonarqube)).
* All breaking changes in the Plugin API must be preceded by a deprecation period of at least 2 years after the deprecation.

{% hint style="info" %}
Under special circumstances, for example, when there are security vulnerabilities that need to be addressed, we might make an exception and drop the deprecated API component earlier.
{% endhint %}

<details>

<summary>Deprecation mark</summary>

A Plugin API component is marked as deprecated with both:

* The annotation `@Deprecated`.
* The Javadoc tag `@deprecated` whose message must start with "in x.y", for example:

```css-79elbk
* /**
 * @deprecated in 4.2. Replaced by {@link #newMethod()}.
 */
@Deprecated
public void foo() {
...
}
```

</details>

### Policy recommendations for API users <a href="#recommendations-for-api-users" id="recommendations-for-api-users"></a>

* Regularly monitor the deprecation of API components and check if you’re currently using them. See [monitoring-api-deprecation](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/deprecations/monitoring-api-deprecation "mention").
* If you’re currently using deprecated API components:
  * Don’t add new uses of it.
  * Make the necessary updates in your next few releases so you’re ready for any breaking changes after the next LTA (Long-Term Active) release. See [release-cycle-model](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/release-cycle-model "mention") for more information.

### Deprecation notice <a href="#notice" id="notice"></a>

Feature removals and deprecations are announced in the [release-notes](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/release-notes "mention").

Plugin API deprecations are announced in the [sonar-plugi-api GitHub repository](https://github.com/SonarSource/sonar-plugin-api/releases).

### Related pages <a href="#related-pages" id="related-pages"></a>

* [web-api](https://docs.sonarsource.com/sonarqube-server/extension-guide/web-api "mention")
* [plugin-basics](https://docs.sonarsource.com/sonarqube-server/extension-guide/developing-a-plugin/plugin-basics "mention")
