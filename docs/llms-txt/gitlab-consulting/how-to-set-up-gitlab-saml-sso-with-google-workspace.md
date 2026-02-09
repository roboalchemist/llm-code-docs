# Source: https://gitlab.consulting/en-gb/blog/2026/01/27/how-to-set-up-gitlab-saml-sso-with-google-workspace.md


# Integrating GitLab SAML SSO with Google Workspace: A Step-by-Step Guide
<h2 id="configure-gitlab-saml-sso-with-google-workspace">Configure GitLab SAML SSO with Google Workspace</h2>
<p>Secure and simplify access to your GitLab instance by setting up Single Sign-On (SSO) using SAML with Google Workspace. This integration ensures seamless authentication for users across your organisation, enhances your security posture, and aligns DevSecOps practices with enterprise identity management standards.</p>
<h3 id="why-use-saml-sso-with-gitlab">Why Use SAML SSO with GitLab?</h3>
<p>SAML-based SSO allows IT administrators to centralise access control and streamline user login processes. By connecting GitLab to Google Workspace, users can authenticate using their corporate credentials, reducing login complexity and improving compliance.</p>
<h3 id="step-by-step-overview">Step-by-Step Overview</h3>
<ol>
<li><strong>Prepare GitLab</strong>: On your self-managed GitLab instance (Premium or Ultimate tier), navigate to Admin Area &gt; Settings &gt; SAML SSO. Generate or note down the required GitLab SAML metadata including the <code>Assertion consumer service URL</code> and <code>Identifier</code>.</li>
<li><strong>Set Up Google Workspace</strong>: In the Google Admin Console, go to Apps &gt; Web and mobile apps, and add a new custom app. Under the SAML settings, paste GitLab’s metadata and configure the ACS URL and Entity ID appropriately.</li>
<li><strong>Assign Attributes</strong>: Configure attribute mapping in Google Workspace to pass essential fields like <code>email</code>, <code>first_name</code>, and <code>last_name</code>, ensuring GitLab receives the correct identity information.</li>
<li><strong>Enable SAML in GitLab</strong>: Back in GitLab, input the Google IdP’s metadata, including the <code>SAML SSO URL</code> and <code>X.509 Certificate</code>. Save the changes and test the integration.</li>
<li><strong>Test and Go Live</strong>: Ensure users can log in via SSO. Optionally, enforce SAML-based authentication for enhanced security.</li>
</ol>
<h3 id="professional-support-available">Professional Support Available</h3>
<p>Setting up SAML SSO can significantly benefit your DevSecOps operations. If you need expert guidance on configuring SAML integration or managing GitLab licences, our team at <a href="https://gitlab.consulting/en-gb/?mtm_campaign=internal-blog-link&amp;mtm_kwd=en-gb:how-to-set-up-gitlab-saml-sso-with-google-workspace">IDEA GitLab Solutions</a> is ready to help. We offer professional GitLab consulting and licensing tailored for organisations in the Czech Republic, Slovakia, Croatia, Serbia, Slovenia, North Macedonia, the UK and beyond—including remote support across Israel, South Africa, and Paraguay.</p>
<p>Visit <a href="https://gitlab.consulting/en-gb/?mtm_campaign=internal-blog-link&amp;mtm_kwd=en-gb:how-to-set-up-gitlab-saml-sso-with-google-workspace">IDEA GitLab Solutions</a> to learn more about our services and accelerate your GitLab deployment.</p>


