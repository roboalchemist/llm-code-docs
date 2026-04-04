# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/email-settings.md

# Email

Tabnine relies on SMTP to send various internal emails. These include emails for user invitations, password reset, and email verification.

### Configure SMTP

{% hint style="info" %}
Only admins designated as **Installation Admins** have access to this section.
{% endhint %}

{% hint style="success" %}
There is an option to configure SMPT with OAuth. Contact Tabnine support to learn how.
{% endhint %}

Admins have the option to configure SMTP through the Tabnine console.

1. Sign in to the Tabnine console as an admin.
2. Go to the **Email** page under **Settings.**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-73d2df58f2787e811e10e328f40390430a221332%2FSH%20%20settings%20email.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Fill out the form with your configuration. Check each tooltip for more details.

**Port:** The default port is 25.

**TLS reject unauthorized:** The default is true.

**Authentication:** Default is false.

**Ignore SSL/TLS:** Default is false.

### Email verification

{% hint style="info" %}
This option is only available if Single Sign-on (SSO) is not configured
{% endhint %}

Admins have the option to control if email verification is a required step in the user invitation:

1. Sign in to the Tabnine console as an admin.
2. Go to the **Email** page, under **Settings**, and enable or disable **Email Verification.**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0b2501221a98c762a209b7055328b95cf50891bf%2FSH%20settings%20verification%20email.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
