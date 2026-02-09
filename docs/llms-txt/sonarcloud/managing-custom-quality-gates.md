# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-gates/managing-custom-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/quality-standards-administration/managing-quality-gates/managing-custom-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-gates/managing-custom-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-gates/managing-custom-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-gates/managing-custom-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-gates/managing-custom-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/managing-custom-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/managing-custom-quality-gates.md

# Managing custom quality gates

*This feature is only available in the Team and Enterprise plans. See* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") *for more information.*

Two built-in quality gates are provided in your organization but you can create your own quality gates, called custom quality gates. To manage custom quality gates, you need the Administer Quality Gates permission. With this permission, you can also associate projects to quality gates in your organization.

For more information about quality gates, read the [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention") page.

To associate a custom quality gate with projects, check out the [associating-projects-with-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/associating-projects-with-quality-gate "mention") page.

### Creating a custom quality gate <a href="#creating-a-custom-quality-gate" id="creating-a-custom-quality-gate"></a>

You can create a custom quality gate from scratch or by duplication. When you create a custom quality gate from scratch, the conditions of the built-in quality gate **Sonar way** are automatically copied to the new record to make your custom quality gate ready for Clean as You Code.

<details>

<summary>From scratch</summary>

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization.
2. In organization’s navigation bar, select **Quality Gates**.
3. In the left panel, select the **Create** button. The **Create Quality Gate** dialog opens.
4. In the dialog, enter the name of the new quality gate and select **Create**.
5. You can now update, add or remove the conditions of the new quality gate. See **Managing a custom quality gate’s conditions** below.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d7e71adbea2dbfe42b560ce1eddd92e27ded1646%2F348169fa5c7a260922122f970d69d3c5bf29c348.png?alt=media" alt="You can create a custom quality gate from scratch in SonarQube Cloud by selecting the Create button."><figcaption></figcaption></figure></div>

</details>

<details>

<summary>By duplication</summary>

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization.
2. In organization’s navigation bar, select **Quality Gates**.
3. In the left panel, select the quality gate you want to duplicate.
4. In the top right corner of the quality gate, select the More Actions button and then **Copy**. The **Copy Quality Gate** dialog opens.
5. In the dialog, enter the name of the new quality gate and select **Copy**.
6. You can now update, add or remove the conditions of the new quality gate. See **Managing a custom quality gate’s conditions** below.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-281efcc15ecef7a4bde17c35ddf0ddeaa7853e89%2F00bbe759637a42b79c13b6b466a947dd2505d49c.png?alt=media" alt="Select the three-dots menu to copy an existing SonarQube Cloud quality gate that you want to customize."><figcaption></figcaption></figure>

</details>

### Managing a custom quality gate’s conditions <a href="#managing-conditions" id="managing-conditions"></a>

You can add or remove conditions. You can update the value of an existing condition. Remember that you define failing conditions: if one of the conditions is met, the quality gate fails. For more information about conditions, see the article about [#definition-based-on-conditions](https://docs.sonarsource.com/sonarqube-cloud/standards/introduction-to-quality-gates#definition-based-on-conditions "mention").

**To update a condition:**

1. Select the pen icon in the far right of the condition row. If there is no pen icon, select first the **Unlock editing** button, below the **Conditions** section.\
   The **Update Condition** dialog opens.
2. Enter the new condition’s value and select **Update Condition**.

**To add a new condition:**

1. Select **Add Condition**. The **Add Condition** dialog opens.
2. In **Where?** select to which code, new or overall, the condition applies. New code is defined through the New Code Defintion (NCD). See the[about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") page for more information.
3. In **Quality Gate fails when**, select the metric to which the condition applies. For information about the metrics, see the [metric-definitions](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions "mention") page.
4. In **Value**, enter the condition’s value.

{% hint style="info" %}
Quality gate conditions related to severity currently use type severities. For more details, see the list of Issue management solution metrics in the [#issues](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#issues "mention") table.
{% endhint %}

**To remove a condition:**

1. Select the dustbin icon in the far right of the condition row. The **Delete Condition** dialog opens.
2. Select **Delete**.

### Upgrading a quality gate for CaYC <a href="#upgrading-to-clean-as-you-code" id="upgrading-to-clean-as-you-code"></a>

We recommend configuring all your quality gates to prevent issues in new code. For more information, see the [#quality-gate-and-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/introduction-to-quality-gates#quality-gate-and-new-code "mention") article.

If your quality gate is not configured for CaYC, you can easily upgrade it as follows:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization.
2. In organization’s navigation bar, select **Quality Gates**.
3. In the left panel, select the custom quality gate you want to upgrade.
4. In **You are a few conditions away from Clean as You Code**, select **Review and Update**. The **Update Quality Gate** dialog opens.
5. Review the proposed update and select **Update Quality Gate** to execute the update.

### Renaming a custom quality gate <a href="#renaming-quality-gate" id="renaming-quality-gate"></a>

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization.
2. In organization’s navigation bar, select **Quality Gates**.
3. In the left panel, select the custom quality gate you want to rename.
4. In the top right corner of your quality gate, select the More Actions button and then **Rename**. The **Rename Quality Gate** dialog opens.
5. Enter the new name and select **Rename**.

### Deleting a custom quality gate <a href="#deleting-quality-gate" id="deleting-quality-gate"></a>

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization.
2. In organization’s navigation bar, select **Quality Gates**.
3. In the left panel, select the custom quality gate you want to delete.
4. In the top right corner of your quality gate, select the More Actions button and then **Delete**.
5. Confirm the deletion.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention")
* [viewing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/viewing-quality-gate "mention")
* [changing-default-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/changing-default-quality-gate "mention")
* [associating-projects-with-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/associating-projects-with-quality-gate "mention")
* [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention")
* [quality-gates-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gates-for-ai-code "mention")
* [changing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate "mention")
