# Source: https://docs.jit.io/docs/welcome-to-onboarding.md

# Onboarding Overview

Welcome to Jit!

**The first onboarding step is to connect Jit with your GitHub, GitLab, Bitbucket or Azure DevOps account**:

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            background-color: #f4f4f4;\n            margin: 0;\n            padding: 5px;\n        }\n\n        .onboarding-section {\n            display: flex;\n            justify-content: space-around;\n            max-width: 800px;\n            margin: auto;\n            gap: 10px;\n        }\n\n        .onboarding-box {\n            background-color: #ffffff;\n            border: 1px solid #ccc;\n            border-radius: 8px;\n            padding: 5px;\n            text-align: center;\n            transition: transform 0.3s, box-shadow 0.3s;\n            text-decoration: none;\n            color: #333;\n            flex: 1; /* Ensures the boxes take equal space */\n        }\n\n        .onboarding-box:hover {\n            transform: scale(1.05);\n            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);\n        }\n\n        .onboarding-box h3 {\n            margin: 0;\n            font-size: 1.2em;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"onboarding-section\">\n        <a href=\"https://docs.jit.io/docs/integrating-with-github\" class=\"onboarding-box\">\n            <h4>Connect Jit with your GitHub account</h4>\n        </a>\n        <a href=\"https://docs.jit.io/docs/connect-jit-with-your-gitlab-account\" class=\"onboarding-box\">\n            <h4>Connect Jit with your GitLab account</h4>\n      </a>\n        <a href=\"https://docs.jit.io/docs/connect-jit-with-your-bitbucket-account\" class=\"onboarding-box\">\n            <h4>Connect Jit with your Bitbucket account</h4>\n      </a>        \n\t\t\t<a href=\"https://docs.jit.io/docs/connect-jit-with-your-azure-dev-ops-account\" class=\"onboarding-box\">\n            <h4>Connect Jit with your Azure DevOps account</h4>\n        </a>\n\n    </div>\n\n</body>\n</html>"
}
[/block]

<br />

***

### What happens when you connect Jit with your SCM account?

Integrating with your SCM account will automatically activate the following code scanners:

* Static Application Security Testing (SAST) to detect security flaws in your custom code
* Software Composition Analysis (SCA) to detect known vulnerabilities in open source components
* Secrets Detection to flag hardcoded secrets in your code, such as passwords, API keys and cloud provider tokens.

The scanners will analyze your code using two flows:

1. The first scanning flow is a full codebase scan (or a full scan of selected repositories/projects). The first codebase scan will take place the moment you connect Jit with your SCM account. The results of the scan are documented in the [Findings page](https://docs.jit.io/v5.0/docs/jit-findings).
2. The second scanning flow is continuous scanning for every code change, which is experienced by developers within your SCM account. This flow is designed to make it easy for developers to consistently resolve code security issues before deployment.

Other important notes:

* Activate additional scanners by navigating to **ASPM → Security Plans** (left menu) → **Jit Max Security Plan**
* Integrating Jit with your cloud environment will enable other core Jit features, including:
  * Contextual prioritization that assigns risk scores to each security issue based on their runtime context (AWS and GCP only)
  * Cloud Security Posture Management to scan your cloud infrastructure in runtime for misconfigurations (AWS, GCP, and Azure)
* [Explore Jit's features](https://docs.jit.io/v5.0/docs/explore-jit) to learn more.