# Source: https://docs.replit.com/teams/enterprise-privacy-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Enterprise Privacy Settings

> Configure organization-wide privacy, security, and source control settings to protect your team's code and deployments.

As an enterprise admin, you can configure organization-wide settings that control how team members interact with code, deployments, and external platforms. These settings help maintain security standards, protect intellectual property, and ensure compliance with enterprise policies.

## Accessing privacy settings

<Accordion title="How to access Privacy Settings">
  1. Navigate to your enterprise workspace
  2. Select **Settings**
  3. Select **Advanced** to view all available settings
</Accordion>

<Frame>
  <img src="https://mintcdn.com/replit/ZUXeyZU2H5Htb4wk/images/teams/advanced_privacy_settings.png?fit=max&auto=format&n=ZUXeyZU2H5Htb4wk&q=85&s=0f78320cd6e88ed0aa621886bc946c77" alt="Enterprise Settings page showing the Advanced tab with Privacy Settings, Security Settings, and Source Control Settings sections" data-og-width="1127" width="1127" data-og-height="1201" height="1201" data-path="images/teams/advanced_privacy_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/ZUXeyZU2H5Htb4wk/images/teams/advanced_privacy_settings.png?w=280&fit=max&auto=format&n=ZUXeyZU2H5Htb4wk&q=85&s=2b6676089cdfe5acbe02407d263603e7 280w, https://mintcdn.com/replit/ZUXeyZU2H5Htb4wk/images/teams/advanced_privacy_settings.png?w=560&fit=max&auto=format&n=ZUXeyZU2H5Htb4wk&q=85&s=6f4b43167a055bb038b31fd19baca820 560w, https://mintcdn.com/replit/ZUXeyZU2H5Htb4wk/images/teams/advanced_privacy_settings.png?w=840&fit=max&auto=format&n=ZUXeyZU2H5Htb4wk&q=85&s=b9c99ed374608e3f47fc41dad5f05762 840w, https://mintcdn.com/replit/ZUXeyZU2H5Htb4wk/images/teams/advanced_privacy_settings.png?w=1100&fit=max&auto=format&n=ZUXeyZU2H5Htb4wk&q=85&s=7f65821d4eaf442d57bb58b795a004a1 1100w, https://mintcdn.com/replit/ZUXeyZU2H5Htb4wk/images/teams/advanced_privacy_settings.png?w=1650&fit=max&auto=format&n=ZUXeyZU2H5Htb4wk&q=85&s=1b7972d785acd3ca246d7f8b31a24298 1650w, https://mintcdn.com/replit/ZUXeyZU2H5Htb4wk/images/teams/advanced_privacy_settings.png?w=2500&fit=max&auto=format&n=ZUXeyZU2H5Htb4wk&q=85&s=840a57457e78859e30bbf7ebb1aeeb51 2500w" />
</Frame>

## Privacy settings

Privacy settings control how apps are published and accessed within your organization.

<CardGroup cols={2}>
  <Card title="Private deployments" icon="lock">
    Require all new apps to be published as private, restricting access to authenticated team members only
  </Card>

  <Card title="Password-protected deployments" icon="key">
    Allow team members to add password protection to their published apps
  </Card>

  <Card title="Private development URLs" icon="shield-halved">
    Require authentication for all app development URLs, including SSO for SAML-enabled organizations
  </Card>

  <Card title="Ban public apps" icon="eye-slash">
    Prevent team members from creating public apps that can be forked or viewed by anyone
  </Card>
</CardGroup>

### Private deployments

When enabled, all new apps must be published as private. Private apps are only accessible to authenticated members of your organization.

**When to use this setting:**
**When to use this setting:**

* The organization handles sensitive data or proprietary applications
* You need to ensure apps are not accidentally made public
* Compliance requirements mandate restricted access to published applications
* You need to ensure apps are not accidentally made public
* Compliance requirements mandate restricted access to published applications

<Note>
  This setting applies only to newly published apps. Existing published apps retain their current visibility settings.
</Note>

### Password-protected deployments

Control whether team members can create password-protected deployments. When enabled, builders can add an additional layer of security by requiring a password to access their published apps.

**When to use this setting:**

* You want to allow sharing apps with external stakeholders without making them fully public
* Teams need to demo applications to clients before wider release
* You require granular access control beyond organization membership

### Require private development URLs

When enabled, all app development URLs require authentication. If your organization has enabled SAML, development URLs require SSO authentication.

**When to use this setting:**
**When to use this setting:**

* You need to prevent unauthorized access to in-progress applications
* Security policies require all development environments to be protected
* You want to ensure only authenticated team members can view development previews
* Your security policy requires all development environments to be protected
* You want to ensure only authenticated team members can view development previews

<Warning>
  This setting applies retroactively to all existing apps in your organization.
</Warning>

### Ban public apps

When enabled, all new apps are automatically set to private within your organization. Public apps can be forked and have their source code viewed by anyone on the internet.

**When to use this setting:**
**When to use this setting:**

* Organizational intellectual property must remain confidential
* You need to prevent accidental exposure of proprietary code
* Compliance requirements prohibit public code repositories
* You need to prevent accidental exposure of proprietary code
* Compliance requirements prohibit public code repositories

### Ban source code export

When enabled, team members cannot export app source code as a zip file. This prevents code from being downloaded and shared outside of the Replit platform.

**When to use this setting:**
**When to use this setting:**

* You need to maintain strict control over where source code resides
* Security policies prohibit local copies of code
* You want to ensure all development happens within managed environments
* Your security policy prohibits local copies of code
* You want to ensure all development happens within your managed environment

## Security settings

Security settings help you enforce vulnerability scanning and other protective measures.

### Require security scan

Configure whether all apps must pass a security scan before publishing. Security scans detect vulnerabilities, exposed secrets, and other security issues in your code.

Available options:

| Setting     | Description                                          |
| ----------- | ---------------------------------------------------- |
| **Off**     | Security scans are optional                          |
| **Require** | All apps must pass a security scan before publishing |

**When to use this setting:**
**When to use this setting:**

* Security compliance requirements must be met
* You want to prevent accidental exposure of API keys or secrets
* You need to ensure consistent security standards across all published apps
* You want to prevent accidental exposure of API keys or secrets
* You need to ensure consistent security standards across all published apps

<Note>
  This setting does not apply to apps that were published before the setting was enabled.
</Note>

## Source control settings

Source control settings help you enforce version control practices and protect your organization's code repositories.

### Require Git remote

When enabled, all apps must have local changes pushed to a Git remote before publishing. This ensures that all code changes are tracked in your organization's version control system.

**When to use this setting:**
**When to use this setting:**

* All code must be backed up in Git
* You need an audit trail of all code changes
* Workflows require code review before publishing
* You need an audit trail of all code changes
* Your workflow requires code review before publishing

<Note>
  This setting does not apply to apps that were published before the setting was enabled.
</Note>

### Private remotes

Control whether team members can use public Git repositories. When set to require private remotes, team members can only push to private repositories on platforms like GitHub.

Available options:

| Setting                    | Description                                                       |
| -------------------------- | ----------------------------------------------------------------- |
| **Off**                    | Team members can use public or private repositories               |
| **Require for non-admins** | Non-admin team members must use private repositories              |
| **Require for all**        | All team members, including admins, must use private repositories |

**When to use this setting:**
**When to use this setting:**

* Public code repositories are prohibited
* You need to ensure proprietary code is not accidentally pushed to public repos
* Compliance requirements mandate private version control
* You need to ensure proprietary code is not accidentally pushed to public repos
* Compliance requirements mandate private version control

## Best practices

<AccordionGroup>
  <Accordion title="Start with private-by-default" icon="shield">
    Enable **Private deployments** and **Ban public apps** to ensure all new apps are private by default. This prevents accidental exposure of sensitive applications.
  </Accordion>

  <Accordion title="Enforce security scanning" icon="magnifying-glass">
    Set **Require security scan** to catch vulnerabilities before apps go live. This helps maintain consistent security standards across your organization.
  </Accordion>

  <Accordion title="Protect development environments" icon="code">
    Enable **Require private development URLs** to ensure even in-progress work is protected. This is especially important for organizations handling sensitive data.
  </Accordion>

  <Accordion title="Control source code access" icon="code-branch">
    <Accordion icon="code-branch">
      Combine **Ban source code export** with **Private remotes** requirements to maintain complete control over code location and access.
    </Accordion>
  </Accordion>
</AccordionGroup>

## Related resources

* [Information Security](/teams/information-security/overview) - Learn about Replit's security practices and compliance standards
* [SAML authentication](/teams/identity-and-access-management/saml) - Configure single sign-on for your organization
* [Groups and permissions](/teams/identity-and-access-management/groups-and-permissions) - Manage team member access with roles and groups
