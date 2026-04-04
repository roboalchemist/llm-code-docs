# Source: https://docs.sonarsource.com/sonarqube-cloud/standards.md

# Setting your quality standards

In SonarQube Cloud, code quality and code security standards are enforced through two mechanisms: *quality profiles* and *quality gates*.

Every project has a quality profile set for each supported language. The profile defines which rules will be applied during code review and analysis.

After analysis, the *quality gate* takes the resulting metrics and compares them to its defined thresholds to determine if the code meets the requirements for release or merge.

The quality profile and quality gate of every new project are set to built-in defaults, (called *Sonar way*). The Sonar way quality profile and quality gate represent the optimum combination of rules and thresholds for most projects, guiding developers in using good coding practices and principles to improve code quality and code security.

{% hint style="info" %}
*While in most projects you can leave the quality gate and quality profile with their default definitions, there are cases where you may want to change them. This section will help you do that.*
{% endhint %}

{% content-ref url="standards/about-new-code" %}
[about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code)
{% endcontent-ref %}

{% content-ref url="standards/managing-quality-gates" %}
[managing-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates)
{% endcontent-ref %}

{% content-ref url="standards/managing-quality-profiles" %}
[managing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles)
{% endcontent-ref %}

{% content-ref url="standards/ai-code-assurance" %}
[ai-code-assurance](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance)
{% endcontent-ref %}
