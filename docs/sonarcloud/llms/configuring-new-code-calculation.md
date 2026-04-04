# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/configuring-new-code-calculation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/configuring-new-code-calculation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/configuring-new-code-calculation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/configuring-new-code-calculation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/configuring-new-code-calculation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/configuring-new-code-calculation.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/configuring-new-code-calculation.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/configuring-new-code-calculation.md

# New code definition

When your project is created, the new code definition set at the organization level is applied to your project by default. However, you can select another new code definition for your project. See [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") for additional information.

### Setting the new code definition for your project <a href="#setting-new-code-definition-for-project" id="setting-new-code-definition-for-project"></a>

As a project admin, you can set the new code definition for your project in the UI (except the Specific version and Specific date options) or using the Web API, at creation time or anytime later as explained below.

{% hint style="info" %}
For more compliance with the Clean as You Code methodology, the Specific version and Specific date options can only be set using the Web API, as it would require frequent user action to be kept up to date.
{% endhint %}

#### In the UI <a href="#in-the-ui" id="in-the-ui"></a>

To set or change the new code definition for your project in the UI:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Go to **Administration > New Code**.
3. Select the option you want to apply to your project.
4. Select **Save**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-7ceab7fcf416edfd061939962cb854ff3559195e%2Fbd73dfb95026cfd878922f2d78e51a50bbf0e1e5.png?alt=media" alt="The new code definition used by your project can be defined in SonarQube Cloud at any time. Note that you must run a new analysis to see your changes take affect."><figcaption></figcaption></figure></div>

#### Via the Web API <a href="#via-the-web-api" id="via-the-web-api"></a>

To use the [web-api](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api "mention") to set your new code definition, you need to use an alternative endpoint, POST [api/settings/set](https://sonarcloud.io/web_api/api/settings?query=settings\&deprecated=false).

You need to make two separate API calls as explained below depending on the selected new code option.

<details>

<summary>Previous version</summary>

| **Previous version** |                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **First call**       | <p><br></p>                                                                                                                                |
| Endpoint             | `api/settings/set`                                                                                                                         |
| Method               | `POST`                                                                                                                                     |
| Parameters           | <p>component: <code>\<project\_key></code></p><p>key: <code>sonar.leak.period</code></p><p>value: <code>previous\_version</code></p>       |
| <p><br></p>          | <p><br></p>                                                                                                                                |
| **Second call**      | <p><br></p>                                                                                                                                |
| Endpoint             | `api/settings/set`                                                                                                                         |
| Method               | `POST`                                                                                                                                     |
| Parameters           | <p>component: <code>\<project\_key></code></p><p>key: <code>sonar.leak.period.type</code> </p><p>value: <code>previous\_version</code></p> |

</details>

<details>

<summary>Specific version</summary>

| **Specific version** |                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **First call**       | <p><br></p>                                                                                                                      |
| Endpoint             | `api/settings/set`                                                                                                               |
| Method               | `POST`                                                                                                                           |
| Parameters           | <p>component: <code>\<project\_key></code></p><p>key: <code>sonar.leak.period</code></p><p>value: <code>\<version></code></p>    |
| <p><br></p>          | <p><br></p>                                                                                                                      |
| **Second call**      | <p><br></p>                                                                                                                      |
| Endpoint             | `api/settings/set`                                                                                                               |
| Method               | `POST`                                                                                                                           |
| Parameters           | <p>component: <code>\<project\_key></code></p><p>key: <code>sonar.leak.period.type</code> </p><p>value: <code>version</code></p> |

</details>

<details>

<summary>Number of days</summary>

| **Number of days** |                                                                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| **First call**     | <p><br></p>                                                                                                                            |
| Endpoint           | `api/settings/set`                                                                                                                     |
| Method             | `POST`                                                                                                                                 |
| Parameters         | <p>component: <code>\<project\_key></code></p><p>key: <code>sonar.leak.period</code></p><p>value: <code>\<number\_of\_days></code></p> |
| <p><br></p>        | <p><br></p>                                                                                                                            |
| **Second call**    | <p><br></p>                                                                                                                            |
| Endpoint           | `api/settings/set`                                                                                                                     |
| Method             | `POST`                                                                                                                                 |
| Parameters         | <p>component: <code>\<project\_key></code></p><p>key: <code>sonar.leak.period.type</code> </p><p>value: <code>days</code></p>          |

</details>

<details>

<summary>Specific date</summary>

| **Specific date** |                                                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **First call**    | <p><br></p>                                                                                                                      |
| Endpoint          | `api/settings/set`                                                                                                               |
| Method            | `POST`                                                                                                                           |
| Parameters        | <p>component: <code>\<project\_key></code></p><p>key: <code>sonar.leak.period</code></p><p>value: <code>\<YYYY-MM-DD></code></p> |
| <p><br></p>       | <p><br></p>                                                                                                                      |
| **Second call**   | <p><br></p>                                                                                                                      |
| Endpoint          | `api/settings/set`                                                                                                               |
| Method            | `POST`                                                                                                                           |
| Parameters        | <p>component: <code>\<project\_key></code></p><p>key: <code>sonar.leak.period.type</code></p><p>value: <code>date</code></p>     |

</details>

{% hint style="info" %}
It’s not necessary to pass the organization key since the project key is unique across all the organizations (The `component` parameter accepts only a single value).
{% endhint %}

### Additional setup and recommendations <a href="#additional-setup-and-recommendations" id="additional-setup-and-recommendations"></a>

Make sure to follow the recommendations about the [verifying-code-checkout-step](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/scanner-environment/verifying-code-checkout-step "mention").

We also recommend completing your merges using the fast-forward option without a merge commit; examples include GitHub’s squash and merge or rebase and merge options. That way, blame for merged commits will always have a more recent commit date.

#### If using Previous version option <a href="#if-using-previous-version-option" id="if-using-previous-version-option"></a>

The current version of a project is determined in different ways depending on the build system:

* If the analysis is done using the [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention"), then SonarQube Server reads the version from the `pom.xml` file.
* If the analysis is done with the [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention") then SonarQube Server reads the version from the `build.gradle` file.
* In all other cases, you must explicitly specify the version by setting the analysis parameter `sonar.projectVersion`.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention")
* [setting-new-code-definition-at-organization-level](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/setting-new-code-definition-at-organization-level "mention")
