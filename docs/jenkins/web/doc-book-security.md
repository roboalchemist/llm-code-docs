# Source: https://www.jenkins.io/doc/book/security/

Title: Securing Jenkins

URL Source: https://www.jenkins.io/doc/book/security/

Markdown Content:
Chapter Sub-Sections

*   [Access Control](https://www.jenkins.io/doc/book/security/access-control)
*   [Securing Jenkins](https://www.jenkins.io/doc/book/security/securing-jenkins)
*   [Managing Security](https://www.jenkins.io/doc/book/security/managing-security)
*   [Controller Isolation](https://www.jenkins.io/doc/book/security/controller-isolation)
*   [Securing Builds](https://www.jenkins.io/doc/book/security/securing-builds)
*   [CSRF Protection](https://www.jenkins.io/doc/book/security/csrf-protection)
*   [Content Security Policy](https://www.jenkins.io/doc/book/security/csp)
*   [Rendering User Content](https://www.jenkins.io/doc/book/security/user-content)
*   [Access Control for Builds](https://www.jenkins.io/doc/book/security/build-authorization)
*   [Handling Environment Variables](https://www.jenkins.io/doc/book/security/environment-variables)
*   [Markup Formatters](https://www.jenkins.io/doc/book/security/markup-formatter)
*   [Securing SCM credentials for Organization Folders and Multibranch Pipelines](https://www.jenkins.io/doc/book/security/securing-org-folders-and-multibranch-pipelines)
*   [Exposed Services and Ports](https://www.jenkins.io/doc/book/security/services)
*   [Credentials](https://www.jenkins.io/doc/book/security/credentials)

Jenkins is used everywhere from workstations on corporate intranets, to high-powered servers connected to the public internet. To safely support this wide spread of security and threat profiles, Jenkins offers many configuration options for enabling, customizing, or disabling various security features.

Many of the security options are enabled by default when passing the interactive setup wizard to ensure that Jenkins is secure. Others involve environment-specific setup and trade-offs and depend on specific use cases supported in individual Jenkins instances.

This chapter will introduce the various security options available to Jenkins administrators and users, explaining the protections offered, and trade-offs to disabling some of them.

[](https://www.jenkins.io/doc/book/security/#basic-setup)Basic Setup
--------------------------------------------------------------------

[Controller Isolation](https://www.jenkins.io/doc/book/security/controller-isolation)
Builds should not be executed on the built-in node, but that is just the beginning: This section discusses what other steps can be taken to protect the controller from being impacted by running builds.

**This must be configured according to the needs of your environment.**

[Access Control](https://www.jenkins.io/doc/book/security/access-control)
By default, Jenkins does not allow anonymous access, and a single admin user exists. This chapter discusses which level of access is provided by permissions and how to safely grant access to more users.

_This is set up securely by the setup wizard. If the setup wizard is disabled on first launch, this may not be configured securely by default._

[](https://www.jenkins.io/doc/book/security/#build-behavior)Build Behavior
--------------------------------------------------------------------------

[Access Control for Builds](https://www.jenkins.io/doc/book/security/build-authorization)
Learn how to restrict what individual builds can do in Jenkins once they’re running.

**This must be configured according to the needs of your environment.**

[Securing Builds](https://www.jenkins.io/doc/book/security/securing-builds)
Learn about how builds can interfere with each other and your infrastructure, and what to do about it.

**This must be configured according to the needs of your environment.**

[Handling Environment Variables](https://www.jenkins.io/doc/book/security/environment-variables)
Improperly written build scripts may be tricked into behaving differently than intended due to special environment variable names or values being injected as build parameters. This section discusses how to protect your builds.

**This must be configured according to the needs of your environment.**

[Securing Organization Folder and Multibranch Pipeline Credentials](https://www.jenkins.io/doc/book/security/securing-org-folders-and-multibranch-pipelines)
Learn about how credentials for Organization Folder and Multibranch Pipeline Credentials may be accessible to unprivileged users in ways you did not anticipate, and what to do about it.

**This must be configured according to the needs of your environment.**

[](https://www.jenkins.io/doc/book/security/#user-interface)User Interface
--------------------------------------------------------------------------

[CSRF Protection](https://www.jenkins.io/doc/book/security/csrf-protection)
Jenkins protects from cross-site request forgery (CSRF) by default. This chapter explains how to work around any problems this may cause.

_This is set up securely by default._

[Content Security Policy](https://www.jenkins.io/doc/book/security/csp)
Jenkins 2.539 and newer allows administrators to set up Content Security Policy protection. This chapter explains how to set it up, how to customize it, and how to identify potential problems.

**This must be configured according to the needs of your environment.**

[Markup Formatter](https://www.jenkins.io/doc/book/security/markup-formatter)
The default markup formatter renders text as entered (i.e. escaping HTML metacharacters). This chapter explains how to switch to a different markup formatter and explains what admins need to be aware of.

_This is set up securely by default._

[Rendering User Content](https://www.jenkins.io/doc/book/security/user-content)
By default, Jenkins strictly limits the features useable in user content (files from workspaces, archived artifacts, etc.) it serves. This chapter discusses how to customize this and make HTML reports and similar content both functional and safe to view.

_This is set up securely by default._

* * *

* * *

[Was this page helpful?](https://www.jenkins.io/doc/book/security/#feedback)

Please submit your feedback about this page through this [quick form](https://www.jenkins.io/doc/feedback-form/).

Alternatively, if you don't wish to complete the quick form, you can simply indicate if you found this page helpful?

See existing feedback [here](https://docs.google.com/spreadsheets/d/1IIdpVs39JDYKg0sLQIv-MNO928qcGApAIfdW5ohfD78).
