# Source: https://docs.aws.amazon.com/dcv/latest/sm-admin/llms.txt

# Amazon DCV Session Manager Administrator Guide

- [Release Notes and Document History](https://docs.aws.amazon.com/dcv/latest/sm-admin/doc-history-release-notes.html)

## [What is Session Manager?](https://docs.aws.amazon.com/dcv/latest/sm-admin/what-is-sm.html)

- [Requirements](https://docs.aws.amazon.com/dcv/latest/sm-admin/requirements.html): The Amazon DCV Session Manager Agent and Broker have the following requirements.


## [Setting up Session Manager](https://docs.aws.amazon.com/dcv/latest/sm-admin/setup.html)

- [Step 1: Prepare the Amazon DCV servers](https://docs.aws.amazon.com/dcv/latest/sm-admin/servers.html): You must have a fleet of Amazon DCV servers with which you intend to use Session Manager.
- [Step 2: Set up the broker](https://docs.aws.amazon.com/dcv/latest/sm-admin/broker.html): The broker must be installed on a Linux host.
- [Step 3: Set up the agent](https://docs.aws.amazon.com/dcv/latest/sm-admin/agent.html): The agent must be installed on all of the Amazon DCV server hosts in the fleet.
- [Step 4: Configure the Amazon DCV server](https://docs.aws.amazon.com/dcv/latest/sm-admin/configure-dcv-server.html): Configure the Amazon DCV server to use the broker as the external authentication server for validating client connection tokens.
- [Step 5: Verify the installations](https://docs.aws.amazon.com/dcv/latest/sm-admin/verify.html): After you have set up the agent, set up the broker, and configured both on the Amazon DCV server, you need to verify that the installations are functioning properly.


## [Configuring the Session Manager](https://docs.aws.amazon.com/dcv/latest/sm-admin/configure.html)

- [Scaling Session Manager](https://docs.aws.amazon.com/dcv/latest/sm-admin/scaling.html): To enable high availability and improve performance, you can configure Session Manager to use multiple Agents and Brokers.
- [Using tags on Amazon DCV servers](https://docs.aws.amazon.com/dcv/latest/sm-admin/targeting.html): You can assign custom tags to Session Manager Agents to help identify and categorize them and the Amazon DCV servers with which they are associated.
- [Configuring an external authorization server](https://docs.aws.amazon.com/dcv/latest/sm-admin/ext-auth.html): The authorization server is the server that is responsible for authenticating and authorizing the client SDKs and Agents.
- [Configuring broker persistence](https://docs.aws.amazon.com/dcv/latest/sm-admin/configure-broker-persistence.html): Session Manager brokers support integration with external databases.

### [Integrating with the Amazon DCV Connection Gateway](https://docs.aws.amazon.com/dcv/latest/sm-admin/configure-gateway-integration.html)

Amazon DCV Connection Gateway is an installable software package that enables users to access a fleet of Amazon DCV servers through a single access point to a LAN or VPC.

- [Amazon DCV server - DNS mapping reference](https://docs.aws.amazon.com/dcv/latest/sm-admin/dcv-server-dns-mapping.html): The Amazon DCV Connection Gateway requires the Amazon DCV serversâ DNS names in order to connect to the DCV server instances.
- [Integrating with Amazon CloudWatch](https://docs.aws.amazon.com/dcv/latest/sm-admin/cloudwatch.html): Session Manager supports integration with Amazon CloudWatch for Brokers running on Amazon EC2 instances, and also Brokers running on on-premises hosts.


## [Upgrading the Session Manager](https://docs.aws.amazon.com/dcv/latest/sm-admin/upgrading.html)

- [Upgrading the Amazon DCV Session Manager agent](https://docs.aws.amazon.com/dcv/latest/sm-admin/upgrading-agent.html): Amazon DCV Session Manager agents receive instructions from the broker and run them on their respective Amazon DCV servers.
- [Upgrading the Amazon DCV Session Manager broker](https://docs.aws.amazon.com/dcv/latest/sm-admin/upgrading-broker.html): Amazon DCV Session Manager brokers pass API requests to their relevant agents.


## [Broker CLI reference](https://docs.aws.amazon.com/dcv/latest/sm-admin/cli.html)

- [register-auth-server](https://docs.aws.amazon.com/dcv/latest/sm-admin/register-auth-server.html): Registers an external authentication server for use with the broker.
- [list-auth-servers](https://docs.aws.amazon.com/dcv/latest/sm-admin/list-auth-servers.html): Lists the external authentication servers that have been registered.
- [unregister-auth-server](https://docs.aws.amazon.com/dcv/latest/sm-admin/unregister-auth-server.html): Unregisters an external authentication server.
- [register-api-client](https://docs.aws.amazon.com/dcv/latest/sm-admin/register-api-client.html): Registers a Session Manager client with the broker and generates client credentials that can be used by the client to retrieve an OAuth 2.0 access token, which is needed to make API requests.
- [describe-api-clients](https://docs.aws.amazon.com/dcv/latest/sm-admin/describe-api-clients.html): Lists the Session Manager clients that have been registered with the broker.
- [unregister-api-client](https://docs.aws.amazon.com/dcv/latest/sm-admin/unregister-api-client.html): Deactivates a registered Session Manager client.
- [renew-auth-server-api-key](https://docs.aws.amazon.com/dcv/latest/sm-admin/renew-auth-server-api-key.html): Renews the public and private keys used by the broker to sign the OAuth 2.0 access tokens that are vended to the Session Manager client.
- [generate-software-statement](https://docs.aws.amazon.com/dcv/latest/sm-admin/generate-software-statement.html): Generates a software statement.
- [describe-software-statements](https://docs.aws.amazon.com/dcv/latest/sm-admin/describe-software-statements.html): Describes the existing software statements.
- [deactivate-software-statement](https://docs.aws.amazon.com/dcv/latest/sm-admin/deactivate-software-statement.html): Deactivates a software statement.
- [describe-agent-clients](https://docs.aws.amazon.com/dcv/latest/sm-admin/describe-agent-clients.html): Describes the agents that are registered with the broker.
- [unregister-agent-client](https://docs.aws.amazon.com/dcv/latest/sm-admin/unregister-agent-client.html): Unregister an agent from the broker.
- [register-server-dns-mappings](https://docs.aws.amazon.com/dcv/latest/sm-admin/register-server-dns-mappings.html): Register the DCV Servers - DNS names mappings coming from a JSON file.
- [describe-server-dns-mappings](https://docs.aws.amazon.com/dcv/latest/sm-admin/describe-server-dns-mappings.html): Describe the currently available DCV Servers - DNS names mappings.


## [Configuration File Reference](https://docs.aws.amazon.com/dcv/latest/sm-admin/file-ref.html)

- [Broker configuration file](https://docs.aws.amazon.com/dcv/latest/sm-admin/broker-file.html): The broker configuration file (/etc/dcv-session-manager-broker/session-manager-broker.properties) includes parameters that can be configured to customize the Session Manager functionality.
- [Agent Configuration File](https://docs.aws.amazon.com/dcv/latest/sm-admin/agent-file.html): The agent configuration file (/etc/dcv-session-manager-agent/agent.conf for Linux and macOS, and C:\Program Files\NICE\DCVSessionManagerAgent\conf\agent.conf for Windows) includes parameters that can be configured to customize the Session Manager functionality.
