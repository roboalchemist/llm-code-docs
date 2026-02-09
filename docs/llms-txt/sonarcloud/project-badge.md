# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/project-badge.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/project-badge.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/project-badge.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/project-badge.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/project-badge.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/project-badge.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/project-badge.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/project-badge.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/project-badge.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/project-badge.md

# Using a project badge

You can include dynamic SonarQube Server badges on your web pages to display information about your project such as the current value of specific metrics or the current quality gate status.

Markdown snippets and simple image URLs are provided to generate the badge code. A unique security token is generated for each project badge and is required to make the badge accessible from third-party tools.

{% hint style="warning" %}
Using project badges can expose sensitive information like your security rating and other metrics. You should only use them in trusted environments.
{% endhint %}

### Generating the badge code <a href="#generating-badge" id="generating-badge"></a>

To generate the code of your dynamic project badge:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more information.
2. In the top right corner, select **Project Information**.
3. In the **Badges** section:
   1. Select the information type you want to display: metric value or quality gate status.
   2. If you selected the metric value information type, select the metric in **Customize badge**.
   3. In Code format, select **Markdown** (markdown snippet) or **Image URL only** depending on how you want to include your badge.
   4. Select the **Copy** button to copy the code of your badge.

### Renewing the badge token <a href="#renewing-token" id="renewing-token"></a>

If a project badge URL is accessed by someone who should not have access to it, you can renew the project badge’s unique token provided you’re a project admin. This invalidates any existing project badge URLs, and you’ll have to update all locations where the badge is being used.

To renew the badge token:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more information.
2. In the top right corner, select **Project Information**.
3. In the **Badges** section, select **Renew token**.

### Using the AI Code Assurance project badge <a href="#ai-code-assurance" id="ai-code-assurance"></a>

The AI Code Assurance project badge is available if your project adheres to recommended Standards for AI generated code. See [ai-code-assurance](https://docs.sonarsource.com/sonarqube-server/ai-capabilities/ai-code-assurance "mention") for more information. Follow these instructions before using the AI Code Assurance badge.

Sonar recognizes that AI-generated code should be monitored with additional quality standards. Recommended checks include high standards to reduce code complexity, remove bugs, and eliminate injection vulnerabilities. SonarQube’s AI Code Assurance features bring confidence that your AI-generated code is being reviewed to avoid any accountability crisis.

These objectives are achieved with three features that allow Quality Standard administrators to qualify projects as AI Code Assured:

1. [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/ai-code-assurance/overview#label-projects-with-ai-code "mention")
2. [#apply-qualified-quality-gate](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/ai-code-assurance/overview#apply-qualified-quality-gate "mention")
3. Publish an AI Code Assurance badge externally to your websites to [monitor-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/ai-code-assurance/monitor-projects-with-ai-code "mention").
