# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/security-hotspots.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/security-hotspots.md

# Security hotspots

### What is a security hotspot? <a href="#what-is-a-security-hotspot" id="what-is-a-security-hotspot"></a>

SonarQube’s code analysis and review finds Security issues and Security Hotspots within your code. Security Hotspot highlights security-sensitive code that the developer needs to review. Upon review, you’ll either find no threat, or you will need to apply a fix to secure the code.

You can think of hotspots as an example of [defense in depth](https://en.wikipedia.org/wiki/Defense_in_depth_\(computing\)), where several redundant layers of protection are added to an application to make it more resilient in the event of an attack.

### Vulnerability or hotspot? <a href="#vulnerability-or-hotspot" id="vulnerability-or-hotspot"></a>

The main difference between a hotspot and a vulnerability is *the need for a review* before deciding whether to apply a fix:

* With a hotspot, a security-sensitive piece of code is highlighted, but overall application security may not be impacted; It’s up to the developer to review the code to determine whether or not a fix is needed to secure the code.
* With a vulnerability, a problem that impacts the application’s security has been discovered that needs to be fixed immediately.

An example is the [RSPEC-2092](https://jira.sonarsource.com/browse/RSPEC-2092), where the use of *cookie secure flag* is recommended to prevent cookies from being sent over non-HTTPS connections, but a review is needed because:

* HTTPS is the main protection against MITM attacks; the secure flag only acts as additional protection in case of failures in network security.
* The cookie may be designed to be sent everywhere (non-HTTPS websites included) because it’s a tracking cookie or similar.

With hotspots, we try to give some freedom to users and educate them on how to choose the most relevant/appropriate protections, depending on the context - budget, threats, etc.

### Why are security hotspots important? <a href="#why-are-security-hotspots-important" id="why-are-security-hotspots-important"></a>

While the need to fix individual hotspots depends on the context, you should view security hotspots as an essential part of improving an application’s robustness. The more fixed hotspots there are, the more secure your code is in the event of an attack. Reviewing security hotspots allows you to:

* **Understand the risk**: Understand when and why you need to apply a fix in order to reduce an information security risk (threats and impacts).
* **Identify protections**: While reviewing hotspots, you’ll see how to avoid writing code that is at risk, determine which fixes are in place, and determine which fixes still need to be implemented to fix the highlighted code.
* **Identify impacts**: With hotspots, you’ll learn how to apply fixes to secure your code based on the impact on overall application security. Recommended secure coding practices are included on the hotspots page to assist you during your review.

### Lifecycle <a href="#lifecycle" id="lifecycle"></a>

Security hotspots have a dedicated lifecycle. To make status changes, the user needs the **Administer Security Hotspots** permission, which is enabled by default. Users with the **Browse** permission can comment on or change the user assigned to a security hotspot.

#### Statuses <a href="#statuses" id="statuses"></a>

Through the lifecycle, a security hotspot takes one of the following statuses:

* **To review**: The default status of new Security Hotspots set by SonarQube Cloud. Security Hotspot has been reported and needs to be checked.
* **Fixed**: A developer has reviewed the Security Hotspot and applied a fix.
* **Safe**: A developer has reviewed the Security Hotspot and determined that no change is necessary, for example, because other more relevant protections are already in place.

### Workflow <a href="#workflow" id="workflow"></a>

Follow this workflow to review security hotspots and apply any fixes needed to secure your code.

#### Review priority <a href="#review-priority" id="review-priority"></a>

When SonarQube Cloud detects a security hotspot, it’s added to the list of security hotspots according to its review priority from high to low. Hotspots with a high review priority are the most likely to contain code that needs to be secured and require your attention first.

Review priority is determined by the security category of each security rule. Rules in categories that are ranked high on the OWASP Top 10 and CWE Top 25 standards are considered to have a high review priority. Rules in categories that aren’t ranked high or aren’t mentioned on the OWASP Top 10 or CWE Top 25 standards are rated as medium or low.

#### Reviewing hotspots <a href="#reviewing-hotspots" id="reviewing-hotspots"></a>

When reviewing a hotspot, you should:

1. Review the **What’s the risk** tab to understand why the security hotspot was raised.
2. From the **Are you at risk** tab, read the **Ask Yourself Whether** section to determine if you need to apply a fix to secure the code highlighted in the hotspot.
3. From the **How can you fix it** tab, follow the **Recommended Secure Coding Practices** to fix your code if you’ve determined it’s unsafe.

After following these steps, assign one of the following status updates to the security hotspot:

* **To Review**: if the issue needs to be reviewed.
* **Fixed**: if you have applied a fix to secure the code highlighted by the hotspot.
* **Safe**: if the code is already secure and doesn’t need to be fixed. (for example, other more relevant protections are already in place).

#### Review history <a href="#review-history" id="review-history"></a>

The **Review history** tab shows the history of the security hotspot, including the status that it’s been assigned, and any comments the reviewer had regarding the hotspot.

### Reviewing hotspots in your IDE <a href="#reviewing-hotspots-in-your-ide" id="reviewing-hotspots-in-your-ide"></a>

Seeing a security hotspot directly in the IDE can help you better understand its context and decide whether it is safe or not. Unfortunately, the SonarQube Cloud Open in IDE feature is not available for security hotspots at this time. See the [#opening-in-ide](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/fixing#opening-in-ide "mention") article for details.

The methods to find and fix security hotspots vary by IDE. Please check out the respective SonarQube for IDE documentation pages for these details:

* [Security hotspots](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/using/security-hotspots "mention") in SonarQube for VS Code
* [Security hotspots](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/using/security-hotspots "mention") in SonarQube for IntelliJ
* [Security hotspots](https://app.gitbook.com/s/5CSDwdOaYoOAGYNiRqgl/using/security-hotspots "mention") in SonarQube for Visual Studio
* [Security hotspots](https://app.gitbook.com/s/kadXEH8HkykK7lKaDvVq/using/security-hotspots "mention") in SonarQube for Eclipse
