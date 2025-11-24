# Source: https://gitlab.consulting/en-gb/blog/2025/11/04/migrate-from-pipeline-variables-to-pipeline-inputs-for-better-security.md


# Secure Your GitLab Pipelines: Switch from Variables to Inputs
<h2 id="enhance-security-by-migrating-from-pipeline-variables-to-pipeline-inputs">Enhance Security by Migrating from Pipeline Variables to Pipeline Inputs</h2>
<p>GitLab is continuously evolving to provide secure and efficient DevSecOps workflows. One of the latest improvements encourages users to move from using pipeline variables to pipeline inputs, offering better control and reducing risk during execution.</p>
<p>Pipeline variables have traditionally offered flexibility, but they can introduce potential security vulnerabilities and make pipeline runs harder to audit. With pipeline inputs, developers gain safer interaction with CI/CD processes by explicitly defining expected input values and enforcing types directly in <code>.gitlab-ci.yml</code>.</p>
<p>This change helps mitigate accidental or malicious misuse of variables. For example, secrets that were previously passed via variables at run-time may become harder to track, while pipeline inputs offer structured and traceable data entry. Security-conscious teams will especially benefit from this enhancement.</p>
<p>Starting with GitLab 16.5, users can define pipeline inputs using new schema syntax, allowing for parameters like strings, booleans, and predefined options. The transition is backward compatible and can be phased in gradually, securing pipelines without disrupting workflows.</p>
<p>At IDEA GitLab Solutions, a Select GitLab Partner, we help teams across Czech Republic, Slovakia, Croatia, Serbia, Slovenia, Macedonia, the United Kingdom, and beyond transition to best practices using GitLab’s latest features. Whether you&rsquo;re hosting on GitLab.com or self-managed, our <a href="https://gitlab.consulting/en-gb/?mtm_campaign=internal-blog-link&amp;mtm_kwd=en-gb:migrate-from-pipeline-variables-to-pipeline-inputs-for-better-security">consulting services and licensing</a> can give your DevSecOps workflow the security upgrade it needs.</p>
<p>Ensure your pipelines align with modern security standards—migrate today to pipeline inputs.</p>


