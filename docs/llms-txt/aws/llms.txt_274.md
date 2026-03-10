# Source: https://docs.aws.amazon.com/dcv/latest/access-console/llms.txt

# Amazon DCV Access Console Console Guide

- [Prerequisites](https://docs.aws.amazon.com/dcv/latest/access-console/prerequisites.html)
- [Getting started](https://docs.aws.amazon.com/dcv/latest/access-console/getting-started.html)
- [Release Notes and Document History](https://docs.aws.amazon.com/dcv/latest/access-console/doc-history-release-notes.html)

## [What is Amazon DCV Access Console?](https://docs.aws.amazon.com/dcv/latest/access-console/what-is-access-console.html)

- [Requirements](https://docs.aws.amazon.com/dcv/latest/access-console/requirements.html): The Amazon DCV Access Console has the following requirements.
- [Authentication methods](https://docs.aws.amazon.com/dcv/latest/access-console/console-authentication.html): The Authentication Server for the Amazon DCV Access Console can be setup to use either Pluggable Authentication Modules (PAM), HTTP Header authentication, or external OAuth providers.
- [Datastore](https://docs.aws.amazon.com/dcv/latest/access-console/datastore.html): Amazon DCV Access Console persists user data, group data, session templates and the permission data related to them through integrations with external databases.
- [Certificates](https://docs.aws.amazon.com/dcv/latest/access-console/certificates.html): In order to provide a HTTPS connection between the different components, a SSL certificate is required for each of the hosts.
- [Networking and connectivity](https://docs.aws.amazon.com/dcv/latest/access-console/networking-connectivity.html): The Amazon DCV Access Console components can all be installed on a single host or on different hosts.
- [Open source code](https://docs.aws.amazon.com/dcv/latest/access-console/open-source.html): The Amazon DCV Access Console consists of installable software packages that include a Handler, an Authentication Server, a Web Client, and a Setup Wizard configured to provide a graphical interface for the Amazon DCV Session Manager broker.


## [Setting up](https://docs.aws.amazon.com/dcv/latest/access-console/setup.html)

- [Using the Setup Wizard](https://docs.aws.amazon.com/dcv/latest/access-console/using-setup-wizard.html): The Setup Wizard is a CLI designed to help you install the Amazon DCV Access Console, and configure the hosts you plan to install the components on.

### [Setting up on a single host](https://docs.aws.amazon.com/dcv/latest/access-console/set-up-one-host.html)

This section explains how to install the Amazon DCV Access Console components on a single host.

- [Step 1: Prepare the environment](https://docs.aws.amazon.com/dcv/latest/access-console/prepare-environment.html): The Amazon DCV Access Console has three components Handler, Web Client, and Authentication Server.
- [Step 2: Run the Setup Wizard](https://docs.aws.amazon.com/dcv/latest/access-console/run-setup-wizard-single.html): The Setup Wizard will install the components and dependencies for the Access Console, and configure a single host to run all of the Access Console components.

### [Setting up on multiple hosts](https://docs.aws.amazon.com/dcv/latest/access-console/setting-up-multiple-hosts.html)

This section explains how to install the Amazon DCV Access Console components on a multiple hosts.

- [Step 1: Prepare your environment](https://docs.aws.amazon.com/dcv/latest/access-console/prepare-environment-multiple.html): The Amazon DCV Access Console has three components Handler, Web Client, and Authentication Server.
- [Step 2: Run the Setup Wizard](https://docs.aws.amazon.com/dcv/latest/access-console/run-setup-wizard-multiple.html): The Setup Wizard will install the components and dependencies for the Access Console, and configure a single host to run all of the Access Console components.
- [Step 3: Install the components](https://docs.aws.amazon.com/dcv/latest/access-console/install-components.html): After preparing the Handler, Web Client, and Authentication Server components, you must install them on the hosts you prepared.
- [Verifying the setup](https://docs.aws.amazon.com/dcv/latest/access-console/verify-setup.html): At this point, the Amazon DCV Access Console should be accessible at the public DNS of the Web Client host.
- [Generating a self-signed certificate](https://docs.aws.amazon.com/dcv/latest/access-console/generate-certs.html): Every host that is running a Amazon DCV Access Console component needs to have a certificate.


## [Using the Access Console](https://docs.aws.amazon.com/dcv/latest/access-console/using-console.html)

### [Sessions](https://docs.aws.amazon.com/dcv/latest/access-console/sessions.html)

A session is a span of time when the Amazon DCV server is able to accept connections from a client.

- [Creating a session](https://docs.aws.amazon.com/dcv/latest/access-console/creating-session.html): To use this console, you must create a session.
- [Connecting to a session](https://docs.aws.amazon.com/dcv/latest/access-console/connecting-session.html): You can connect to a session after it has been created.
- [Closing a session](https://docs.aws.amazon.com/dcv/latest/access-console/closing-session.html): After youâre completely done with your work, you can Close a session and release the underlying resource back to the host server.

### [Session templates](https://docs.aws.amazon.com/dcv/latest/access-console/session-templates.html)

A Amazon DCV session template is created by admins to define the details of the session to be created.

- [Creating a session template](https://docs.aws.amazon.com/dcv/latest/access-console/creating-session-template.html): A session template is required to create sessions within the console.
- [Assigning a session template to users or groups](https://docs.aws.amazon.com/dcv/latest/access-console/assigning-session-template.html): In order for users to create sessions, they must first have a session template assigned to them.
- [Duplicating a session template](https://docs.aws.amazon.com/dcv/latest/access-console/duplicating-session-template.html): Instead of creating a new session template, you can choose to duplicate an existing session template and change its parameters to your specifications.
- [Editing a session template](https://docs.aws.amazon.com/dcv/latest/access-console/editing-session-template.html): If you need to adjust any sessions details, you can edit the parameters of an existing session template.
- [Deleting a session template](https://docs.aws.amazon.com/dcv/latest/access-console/deleting-session-template.html): You can delete a session template when you're completely done with it.
- [Hosts](https://docs.aws.amazon.com/dcv/latest/access-console/hosts.html): On the Hosts page, you can view a list of host machines (either cloud or on-premises) you have installed Amazon DCV servers configured with Amazon DCV Session Manager.


## [Managing users](https://docs.aws.amazon.com/dcv/latest/access-console/managing-users.html)

- [Importing users and groups](https://docs.aws.amazon.com/dcv/latest/access-console/importing-users-groups.html): Users will only appear in the Amazon DCV Access Console if they have been directly imported from the Access Console, or have already logged in.

### [Users](https://docs.aws.amazon.com/dcv/latest/access-console/users.html)

The Amazon DCV Access Console allows admins to manage users, their roles and their access to the Console.

- [User roles](https://docs.aws.amazon.com/dcv/latest/access-console/user-roles.html): There are two roles a user can have with the Amazon DCV Access Console: admin and user.

### [User groups](https://docs.aws.amazon.com/dcv/latest/access-console/user-groups.html)

The Amazon DCV Access Console allows admins to manage user groups and their assigned templates.

- [Creating user groups](https://docs.aws.amazon.com/dcv/latest/access-console/creating-user-groups.html): You can create a user group directly from the Access Console, by selecting users and assigning templates.
- [Editing user groups](https://docs.aws.amazon.com/dcv/latest/access-console/editing-user-groups.html): You can edit a user group directly from the Access Console, and are able to modify the group name, users in the group and templates assigned to the group.


## [Custom branding](https://docs.aws.amazon.com/dcv/latest/access-console/custom-branding.html)

- [Adding your custom branding](https://docs.aws.amazon.com/dcv/latest/access-console/adding-custom-branding.html): To customize the Amazon DCV Access Console with your organizational branding, you need to update the following with your preferred configurations:


## [Configuration file reference](https://docs.aws.amazon.com/dcv/latest/access-console/config-file-ref.html)

- [Authentication Server configuration files](https://docs.aws.amazon.com/dcv/latest/access-console/auth-server-config.html): The Authentication Server has two configuration files (/etc/dcv-access-console-auth-server/access-console-auth-server.properties and /etc/dcv-access-console-auth-server/access-console-auth-server-secrets.properties) that include parameters that can be configured to customize the Amazon DCV Access Console functionality connecting to different components.
- [Handler configuration files](https://docs.aws.amazon.com/dcv/latest/access-console/handler-config-files.html): The Handler has two configuration files (/etc/dcv-access-console-handler/access-console-handler.properties and /etc/dcv-access-console-handler/access-console-handler-secrets.properties) that include parameters that can be configured to customize the Amazon DCV Access Console functionality connecting to different components.
- [Web Client configuration files](https://docs.aws.amazon.com/dcv/latest/access-console/web-client-config-files.html): The Web Client configuration has two configuration files (/etc/dcv-access-console-webclient/access-console-webclient.properties and /etc/dcv-access-console-webclient/access-console-webclient-secrets.properties) that include parameters that can be configured to customize the Amazon DCV Access Console functionality connecting to different components.


## [Upgrading the Access Console](https://docs.aws.amazon.com/dcv/latest/access-console/upgrading-access-console.html)

- [Upgrading Amazon DCV Access Console on a single host](https://docs.aws.amazon.com/dcv/latest/access-console/upgrading-single-host.html): The Wizard will update the components for the Access Console, reload and restart all of the Access Console components.
- [Upgrading Amazon DCV Access Console on multiple hosts](https://docs.aws.amazon.com/dcv/latest/access-console/upgrading-multiple-hosts.html): To upgrade the Handler, Authentication Server, and Web Client components, you must run the following commands.


## [Troubleshooting](https://docs.aws.amazon.com/dcv/latest/access-console/troubleshooting.html)

- [Using the component log files](https://docs.aws.amazon.com/dcv/latest/access-console/using-component-log-files.html): You can use the Amazon DCV Access Console component log files to identify and troubleshoot problems with the different Amazon DCV Access Console components.
- [Using browser and network log files](https://docs.aws.amazon.com/dcv/latest/access-console/using-browser-network-log-files.html): The web browser communicates with the Handler component to view and modify resources.
- [Managing the component processes](https://docs.aws.amazon.com/dcv/latest/access-console/managing-component-process.html): The Amazon DCV Access Console components, such as Authentication Server, Handler, Web Client, run while processes on their hosts and can be managed using the command systemctl.
- [Handler fails to communicate with the broker](https://docs.aws.amazon.com/dcv/latest/access-console/handler-failures.html): If there are communication failures between Handler component and Session Manager Broker, âBroker authentication errorâ will appear in the browser logs or BrokerAuthenticationException: {"error":"unauthorized_client"} in the handler logs.
- [I'm having problems logging in](https://docs.aws.amazon.com/dcv/latest/access-console/login-errors.html): During login, the Web Client uses OAuth 2.0 with the Authentication Server to receive an access token that is used to obtain user information and other information from the Handler.
- [Known issues](https://docs.aws.amazon.com/dcv/latest/access-console/known-issues.html): The Amazon DCV Access Console has the following known issues.


## [Security](https://docs.aws.amazon.com/dcv/latest/access-console/dcv-security.html)

- [Data protection](https://docs.aws.amazon.com/dcv/latest/access-console/data-protection.html): Learn how the AWS shared responsibility model applies to data protection when using Amazon DCV.
- [Compliance validation](https://docs.aws.amazon.com/dcv/latest/access-console/security-compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
