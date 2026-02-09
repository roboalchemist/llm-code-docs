# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/system-functions/enabling-ai-generated-fix-suggestions.md

# AI-generated fix suggestions

*This feature is available in* [*Early Access*](https://www.sonarsource.com/legal/early-access/?_gl=1*1cnxd7l*_gcl_aw*R0NMLjE3MjYwNjEzMzYuQ2p3S0NBandfNFMzQmhBQUVpd0FfNjRZaHRaajloc0NiVllqSDlWQnBFNThseVJNU3AwRGZJXzFxVUlpVEM5OGNzeWdZTG9lenF1ZU1ob0NyMGtRQXZEX0J3RQ..*_gcl_au*NzgzMTE3MTA4LjE3MjQwNjY1Mjc.*_ga*MjA1OTIwMzU4OS4xNzI0MDY2NTI3*_ga_9JZ0GZ5TC6*MTcyNjA5MzA2Ni4zNy4xLjE3MjYwOTMwNzMuNTMuMC4w)*, in Enterprise Edition and above.*

As an instance administrator, you can enable or disable AI-generated fix suggestions on your instance. SonarQube uses OpenAI’s GPT-4 to generate the suggestions.

To do this, go to **Administration** > **Configuration** > **General Settings** > **AI CodeFix** > and select **Enable AI CodeFix**.

{% hint style="info" %}
You’ll need a a connection to the internet to connect to Sonar’s AI fix suggestions service.

The service is provided via api.sonarqube.io and has these static IP addresses:

99.83.135.55 (CIDR: 99.83.135.55/32)

15.197.164.24 (CIDR: 15.197.164.24/32)
{% endhint %}

Once enabled, developers can get AI-generated fix suggestions from the **Issues** page in their projects. See [fixing](https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/issues/fixing "mention") for more details.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [ai-features](https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/ai-features "mention")
* [fixing](https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/issues/fixing "mention")
* [project-settings](https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/project-settings "mention") ("Marking a project as containing AI-generated code" section).
