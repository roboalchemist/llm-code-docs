# Source: https://docs.readthedocs.com/platform/latest/commercial/single-sign-on.html

# Single sign-on (SSO)[](#single-sign-on-sso "Link to this heading")

Note

This feature is only available on [Read the Docs for Business](https://app.readthedocs.com/).

Single sign-on is an optional feature on Read the Docs for Business for all users. By default, you will use [[teams]](../guides/manage-read-the-docs-teams.html) within Read the Docs to manage user authorization. SSO will allow you to grant permissions to your organization's projects in an easy way.

Currently, we support two different types of single sign-on:

-   Authentication *and* authorization are managed by the identity provider (GitHub, Bitbucket or GitLab)

-   Authentication (*only*) is managed by the identity provider (Google Workspace account with a verified email address)

[]

## Single sign-on with GitHub, Bitbucket, or GitLab[](#single-sign-on-with-github-bitbucket-or-gitlab "Link to this heading")

Using an identity provider that supports authentication and authorization allows organization owners to manage who has access to projects on Read the Docs, directly from the provider itself. If a user needs access to your documentation project on Read the Docs, that user just needs to be granted permissions in the Git repository associated with the project.

Once you enable this option, your existing Read the Docs teams will not be used. All authentication will be done using your git provider, including any two-factor authentication and additional single sign-on that they support.

Learn how to configure this SSO method with our [[How to setup single sign-on (SSO) with GitHub, GitLab, or Bitbucket]](../guides/setup-single-sign-on-github-gitlab-bitbucket.html).