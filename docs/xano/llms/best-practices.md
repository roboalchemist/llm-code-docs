# Source: https://docs.xano.com/security/best-practices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices

### Authentication

Authentication is handled by **JWE** tokens, which is an industry standard.

**Authentication** is how a user logs in or signs up to an application. Xano provides secure out-of-the-box authentication via JWE (JSON Web Encryption) tokens. JWE tokens are self-contained and provide data integrity, authenticity, non-repudiation, and confidentiality.

**OAuth**, which stands for “**Open Authorization**,”\*\* **allows third-party services to exchange your information without you having to give away your password**.\*\*

\*\*OAuth \*\*providers such as Facebook, Google, LinkedIn, and GitHub login are available in the Xano marketplace to easily enable.

### Single-Tenancy

On Xano's dedicated resource plans, the user's Instance is on a single-tenant deployment or architecture. This means that the user is the only tenant on the server (Instance) architecture and that all the server resources and CPU are dedicated to the tenant. Single-tenancy has a variety of benefits including:

\*\*Data Separation \*\*- Data is kept separate from other users since the Instance is isolated. This allows for independence of data and greater customization of software and hardware.

**Data Security** - If one user has a breach of data, then another user is safe from the breach since their data is stored on a completely separate Instance.

**Reliability & Performance** - Since the Instance is only dependent and serves a single tenant, performance and reliability are significantly increased. The alternative would be the Instance serving many different users.

**Recovery** - With a single-tenancy backups are also isolated, making it easier and more reliable to restore from backups in the event of a disaster.

### Password Requirements

Xano requires password minimums for logging in to a Xano account. A password must be a minimum of eight (8) characters, maximum of 256 characters, at least one (1) alphabetic character, and at least one (1) numeric character. These password requirements are only for login by email and password.

Password requirements for Single Sign-On (SSO) are managed by the SSO provider.

### 2FA Security

Two-factor authentication (2FA) security, or two-step authentication, can be enabled for logging in to a Xano account. 2FA security requires the use of two different forms of identification to access and authenticate an account. It is an extra layer of security beyond email and password credentials that secures an account by requiring an authentication step from something that belongs to the user.

2FA security can be enabled from the account page of a Xano account. [Learn how to enable 2FA](/your-xano-account/account-page#enabling-2fa-two-factor-authentication).

### Inactivity Timeout

To protect your privacy, Xano includes an inactivity timer which will log you out after 2 hours of inactivity by default, but this can be adjusted or disabled entirely via your account settings. This is based on mouse activity and works across multiple tabs.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2c15fe7a-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=73aa8e5f6bda72958870dc2ecf282732" width="1662" height="753" data-path="images/2c15fe7a-image.jpeg" />
</Frame>

### Enforcement

On certain Xano plans, you have the ability to enable security policy enforcement through your Instance settings.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/eb3bdbef-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=9a44ad9537efe88eca08abe6a022736d" width="392" height="540" data-path="images/eb3bdbef-image.jpeg" />
</Frame>

**Require 2FA** enforces that your users not only have two-factor authentication enabled, but that they have logged in using that method.

**Authentication Enforcement** enables requiring your team members to authenticate using one or more of the enabled services you choose.

**Allowed SSO Hosts** enforces the email address domains allowed when team members log in. As an example, if we wanted our team members to only authenticate using Github accounts that use a xano.com email address, we could check Github under Authentication Enforcement, and add xano.com as an allowed SSO host.

### Sensitive Data Flagging

Xano maintains a [request history](/maintenance-monitoring-and-logging/request-history) of incoming requests of your APIs. To ensure that no sensitive data is not logged in the request history, you can enable the **Sensitive Data** flag on that database field to ensure it is not stored.

<Info>
  The **sensitive data** flag only impacts the inputs of a request when using database link, which automatically creates inputs for you based on database fields; you will want to ensure that the sensitive data is not returned elsewhere in your function stack.
</Info>

In the settings for the field you would like to hide, enable the **Sensitive Data** flag.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/be768767-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=7fc03c4db8499e82726611ff708b46ef" width="429" height="195" data-path="images/be768767-image.jpeg" />
</Frame>

**Sensitive Data Flag - Disabled**

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/96354465-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=99d3cca38dc7f4e14d402ce46ba68729" width="431" height="695" data-path="images/96354465-image.jpeg" />
</Frame>

**Sensitive Data Flag - Enabled**

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/453d441d-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=5f8d74765f9481c7076f998d88b1ed3e" width="429" height="692" data-path="images/453d441d-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).