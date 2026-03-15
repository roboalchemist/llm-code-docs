# Source: https://docs.jit.io/docs/faq.md

# FAQ

## Overview of Jit

**Q: What is Jit?**\
A: Jit is a platform designed to simplify and enhance application security by integrating seamlessly with development workflows. It offers capabilities like branch scanning, policy management, and contextual prioritization to help teams manage security risks efficiently. For more details, visit the [About Jit](#) page.

**Q: Can Jit integrate with GitHub and GitLab?**\
A: Yes, Jit supports integration with both GitHub and GitLab to streamline security workflows and ensure seamless collaboration between teams. Check the [GitHub Integration Guide](#) and [GitLab Integration Guide](#) for detailed setup instructions.

**Q: How does Jit integrate with existing tools?**\
A: Jit integrates with tools like GitHub, GitLab, and CI/CD pipelines, as well as popular IDEs and cloud platforms, to ensure seamless adoption and enhanced workflow efficiency.

**Q: What makes Jit different from competitors?**\
A: Jit stands out with its developer-centric approach, contextual prioritization of vulnerabilities, and emphasis on automation and ease of use, making security a seamless part of the development process.

**Q: Is Jit's platform easy to use?**\
A: Yes, Jit is designed with usability in mind, providing intuitive interfaces, clear documentation, and integrations that simplify security management for developers and security teams alike.

**Q: How can a development team use Jit to improve release cycles?**\
A: Jit enables development teams to integrate security scans early in the development process, providing real-time feedback and automating risk mitigation, which reduces delays in release cycles.

***

## Platform Capabilities

**Q: Does Jit support operations in the EU region?**\
A: Yes, Jit supports operations within the EU region. For detailed information on selecting your preferred region and understanding the benefits of regional support, please refer to our [Regional Jit](https://docs.jit.io/docs/regional-jit) documentation.

**Q: Can Jit’s reports help me identify and prioritize risks?**\
A: Yes, Jit provides detailed reporting that helps teams understand their security posture, track progress, and prioritize risks based on contextual factors.

**Q: What are Jit's reporting capabilities?**\
A: Jit’s reports provide insights into security vulnerabilities, compliance alignment, and risk prioritization, helping teams track progress and make data-driven decisions.

**Q: How can Jit help improve my organization’s security posture over time?**\
A: Jit tracks key metrics like vulnerability resolution times and compliance adherence, offering actionable insights and trends that help organizations proactively strengthen their security posture.

**Q: Can Jit’s configuration be managed through code?**\
A: Yes, Jit supports configuration-as-code, allowing you to define security policies and workflows in version-controlled repositories for better scalability and automation.

**Q: How do I set up IDE integration with Jit?**\
A: Jit offers IDE integration to provide real-time feedback during development. Follow the setup instructions in the [Developer Experience](#) section of the documentation for your specific IDE.

**Q: Can Jit integrate with CI/CD pipelines?**\
A: Yes, Jit integrates seamlessly with CI/CD pipelines, allowing for automated scans and enforcement of security policies during the development lifecycle.

**Q: What are Jit's customization options?**\
A: Jit offers customizable security policies, workflows, and reporting to align with your team’s specific needs and objectives.

**Q: Can Jit detect vulnerabilities in dependencies from third-party vendors?**\
A: Yes, Jit’s dependency scanning features can identify vulnerabilities in third-party libraries, providing actionable recommendations to mitigate associated risks.

***

## Security Features

**Q: What types of security scans does Jit support?**\
A: Jit supports various security scans, including Static Application Security Testing (SAST), Software Composition Analysis (SCA), and Secrets Detection. These help identify vulnerabilities and risks in your codebase and dependencies.

**Q: How does Jit handle security vulnerabilities?**\
A: Jit identifies vulnerabilities through comprehensive scanning and prioritizes them using contextual information to recommend actionable remediation steps.

**Q: How does Jit handle dependency vulnerabilities?**\
A: Jit provides dependency scanning features to identify vulnerabilities in third-party libraries and suggests actionable steps to mitigate risks effectively.

**Q: What is contextual prioritization?**\
A: Contextual prioritization is a feature in Jit that uses factors like criticality and exploitability to rank security issues, ensuring teams address the most impactful problems first.

**Q: How does Jit handle false positives?**\
A: Jit uses advanced algorithms and user feedback to minimize false positives and continuously improve detection accuracy.

**Q: How does Jit handle secret detection?**\
A: Jit scans for exposed secrets in your codebase and provides actionable insights to help you secure sensitive information promptly.

**Q: Does Jit support on-premise installations?**\
A: Currently, Jit operates as a cloud-based platform. On-premise installations may be considered in the future based on demand.

**Q: What is Jit's approach to security orchestration?**\
A: Jit automates security tasks, integrates with development workflows, and provides tools for effective collaboration, enabling teams to manage risks efficiently.

**Q: How does Jit minimize alert fatigue for security teams?**\
A: Jit prioritizes alerts based on context and criticality, reduces false positives, and offers customizable notifications to ensure teams focus on the most relevant security issues.

**Q: Does Jit provide advanced insights for multi-cloud environments?**\
A: Yes, Jit offers tools like CSPM (Cloud Security Posture Management) and IaC (Infrastructure as Code) scanning to help teams secure multi-cloud deployments.

***

## Developer Tools and Workflow Automation

**Q: What are Jit's automation capabilities?**\
A: Jit automates security scans, policy enforcement, and reporting, reducing manual effort and enabling faster issue resolution.

**Q: What is Jit's approach to developer engagement?**\
A: Jit focuses on empowering developers with actionable feedback, real-time insights, and integrations that fit seamlessly into their existing workflows.

**Q: How does Jit support developer workflows?**\
A: Jit integrates with IDEs, CI/CD pipelines, and collaboration tools to provide developers with the context and tools they need to address security issues efficiently.

**Q: Does Jit offer real-time security alerts?**\
A: Yes, Jit provides real-time notifications for critical security issues, enabling teams to respond promptly and minimize risks.

***

## Compliance and Policies

**Q: Can I create custom security policies in Jit?**\
A: Yes, Jit allows you to create and enforce custom security policies tailored to your organization’s requirements. These policies can be applied at various levels, such as repositories or teams. See the [Custom Policies](#) page for more information.

**Q: Does Jit support compliance frameworks?**\
A: Jit is designed to help teams align with compliance frameworks by providing tools to enforce security best practices and generate reports that demonstrate adherence.

**Q: How does Jit support compliance requirements?**\
A: Jit helps teams meet compliance standards through automated policy enforcement, detailed reporting, and tools for audit readiness.

***

## Troubleshooting

**Q: What should I do if my selected branch is missing from the repository?**\
A: If the branch being scanned is no longer available, Jit will mark the repository as "not scanned" in the UI. Once the branch is restored, a new scan can be triggered to resume coverage.

**Q: How do I resolve pipeline errors?**\
A: Refer to the [Pipelines](#) section in the documentation for troubleshooting steps. Common issues include incorrect configurations or missing dependencies in your CI/CD workflows.

**Q: How do I add users to Jit?**\
A: To add users:

* Go to Administration & Settings > Users.
* Click Add User and enter their email addresses.
* Assign appropriate roles and permissions.
* For detailed instructions, visit the Users documentation.

**Q: What should I do if a pipeline fails?**\
A: If a pipeline fails:

* Check the Pipelines > Errors section for detailed error logs.
* Verify your configurations in the Policies and Controls settings.
* Consult the Troubleshooting Pipelines page for additional tips.

**Q: How do I set up Jit for my repositories?**\
A: To add repositories:

* Go to the [Settings](#) > Repositories section.
* Connect your version control system (e.g., GitHub, GitLab).
* Select the repositories you want to monitor.
* Configure the desired detection policies and controls.
* For more details, visit the [Getting Started with Jit](#) page.

***

## Future Enhancements and Feedback

**Q: How can I request a new feature or improvement in Jit?**\
A: You can provide feedback or request new features by contacting the Jit support team or through your account dashboard. Your feedback is valuable and helps shape future enhancements.

**Q: Will Jit support multi-branch scanning in the future?**\
A: Multi-branch scanning may be considered based on user demand and feedback. The current focus is on optimizing single-branch capabilities to ensure the best user experience.

**Q: Are there plans to allow branch changes via the UI?**\
A: While branch changes currently require contacting support, this feature may be added in the future if there is sufficient demand and alignment with user workflows.

***

## Glossary

**SAST:** Static Application Security Testing—a method for analyzing source code for vulnerabilities.\
**SCA:** Software Composition Analysis—a method for identifying vulnerabilities in third-party dependencies.\
**SBOM:** Software Bill of Materials—a list of components in a software application, useful for managing dependencies and ensuring compliance.\
**CSPM:** Cloud Security Posture Management—tools and practices for securing cloud resources.\
**IaC:** Infrastructure as Code—a practice of managing and provisioning infrastructure through code.