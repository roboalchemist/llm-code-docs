# Source: https://docs.gitguardian.com/self-hosting/management/application-management/admin-area.md

# Admin Area

> Access and use the GitGuardian self-hosted admin area for system-wide configuration and user management.

This section serves as a comprehensive dashboard for administrators, providing essential tools and insights for managing your GitGuardian Self-Hosted instance. It enables effective monitoring of system health, user management, and configuration of instance settings.

:::info
When installing GitGuardian as Self-Hosted, there can only be one workspace per instance.
:::

## Health Check

A page dedicated to monitoring the overall health and performance of your GitGuardian instance. This ensures that all systems are functioning correctly and efficiently, highlighting potential issues before they impact your workflow. More information on the [Checking environment health](../../troubleshoot/health-check) page.

## Users

Provides a comprehensive list of all users within your GitGuardian instance. It allows for detailed user management, including adding new users and monitoring user activity.

You have the ability to:

- **Force a Password Reset:** Ensure security by forcing a password reset for any user.
- **Promote a User to Admin:** Grant admin privileges to users, giving them access to the admin area.
- **Revoke Admin Rights:** Remove admin privileges from users as needed.

:::warning
The `admin` privilege is specifically designed to control access to the Admin Area access. To adjust workspace access levels (`manager`, `member`, or `restricted`), navigate to the members settings section within your workspace. Detailed information is available on the **[workspace setting](../../../platform/enterprise-administration/workspace-settings)** page.
:::

## License

Manage your GitGuardian license here. This includes viewing your current license details, updating license information, and understanding your license utilization to ensure compliance and optimal usage. More information on the [License Management](../../license-management) page.

For [embedded cluster](../../installation/installation-embedded-cluster) configurations, gain direct access to the KOTS admin area from here. Further details are provided on the [Access to the KOTS Admin Console](../infrastructure-management/admin-console.md) page.

## Settings

The Settings section allows for comprehensive customization of your GitGuardian instance to meet organizational requirements. It includes:

- **Signup Restrictions:** Control user access by allowing entry only through invitation or Single Sign-On (SSO) mechanisms, ensuring secure and regulated user addition. Further details can be found on the [Security recommendations and information](../../security/recommendations#signup-restrictions) page.
- **Preferences:** A table of preferences provides flexibility, enabling fine-tuning of your GitGuardian instance for enhanced usability and efficiency. Additional information is available on the [Configure preferences](../application-management/preferences) page.
- **Certificate-based authentication:** Verify and Troubleshoot [certificate-based authentication](../infrastructure-management/cert-based-auth) page.
- **Machine Learning**: Enrich past incidents using [Machine Learning](./machine-learning)
- **Honeytoken Configuration:** Integrate with your AWS organization to generate and monitor honeytokens, bolstering your security measures. Learn more on the [Honeytoken for self-hosted](../../../honeytoken/self-hosted) page.
- **Email Configuration:** Choose between Sendgrid or SMTP for email services. For setup instructions, visit the [Configure the email system](../application-management/email-configuration) page.

### AI Filters

AI Filters translate natural language into existing GitGuardian filters on the **Incidents**, **Perimeter**, and **Audit Logs** pages, allowing you to quickly locate relevant data. Filters configured via AI can also be saved as [views](../../../platform/collaboration-and-sharing/saved-views#gitguardian-views) for future use, streamlining access to frequently used filter sets.

To enable AI Filters on self-hosted instances:

1. Navigate to the Admin area of your GitGuardian instance, under **Settings > General > Preferences**.
2. In **Filters**, set `ai_filters_enabled` to `true`.
3. Ensure an [OpenAI API key](https://platform.openai.com/api-keys) is configured under **On-Premise** > `openai_api_key`.

## Encryption Key Rotation

Enhance your security posture by periodically rotating encryption keys. This section provides tools and procedures for updating the encryption keys used to secure your data, helping to safeguard against unauthorized access. Detailed instructions are available on the [Database Security](../../security/database-security#update-postgresql-data-encryption-key) page.

## Tasks

### Worker tasks

The Worker Tasks page allows you to monitor task activity and worker usage, helping you identify performance issues and optimize scaling for your GitGuardian self-hosted instance.

![Worker Tasks Overview](/img/self-hosting/management/application-management/admin_area_worker_tasks.png)

### Periodic tasks

The Periodic Tasks page allows you to adjust schedules and fine-tune periodic tasks to enhance the performance of your GitGuardian self-hosted instance. It is important to exercise caution and avoid making changes without proper guidance. For assistance or additional support, it is recommended to contact the **[support team](mailto:support@gitguardian.com)** directly.

![Periodic Tasks Overview](/img/self-hosting/management/application-management/admin_area_periodic_tasks.png)
