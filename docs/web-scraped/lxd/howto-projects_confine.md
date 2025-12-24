# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/projects_confine/

[]

# How to confine users to specific projects[¶](#how-to-confine-users-to-specific-projects "Link to this heading")

You restrict users or clients to specific projects. Projects can be configured with features, limits, and restrictions to prevent misuse. See [[Instances grouping with projects]](../../explanation/projects/#exp-projects) for more information.

How to confine users to specific projects depends on whether LXD is accessible via the [[HTTPS API]](#projects-confine-https), or via the [[Unix socket]](#projects-confine-users).

[]

## Confine users to specific projects on the HTTPS API[¶](#confine-users-to-specific-projects-on-the-https-api "Link to this heading")

You can confine access to specific projects by restricting the TLS client certificate that is used to connect to the LXD server. See [[Restricted TLS certificates]](../../explanation/authorization/#restricted-tls-certs) for more information. Only certificates returned by [`lxc`]` `[`config`]` `[`trust`]` `[`list`] can be managed in this way.

[[▶] [Watch on YouTube]](https://www.youtube.com/watch?v=4iNpiL-lrXU&t=525s)

Note

The UI does not currently support configuring project confinement for certificates of this type. Use the CLI or API to set up confinement.

You can also confine access to specific projects via group membership and [[Fine-grained authorization]](../../explanation/authorization/#fine-grained-authorization). The permissions of OIDC clients and fine-grained TLS identities must be managed with [`lxc`]` `[`auth`] subcommands and the [`/1.0/auth`] API.

To create a TLS client and restrict the client to a single project, follow these instructions:

CLI

API

Create a restricted trust store entry with access to a project

If you're using token authentication:

    lxc config trust add --projects <project_name> --restricted

To add the client certificate directly:

    lxc config trust add <certificate_file> --projects <project_name> --restricted

The client can then add the server as a remote in the usual way ([[[`lxc`]` `[`remote`]` `[`add`]` `[`<server_name>`]` `[`<token>`]]](../../reference/manpages/lxc/remote/add/#lxc-remote-add-md) or [[[`lxc`]` `[`remote`]` `[`add`]` `[`<server_name>`]` `[`<server_address>`]]](../../reference/manpages/lxc/remote/add/#lxc-remote-add-md)) and can only access the project or projects that have been specified.

Note

You can specify the [`--project`] flag when adding a remote. This configuration pre-selects the specified project. However, it does not confine the client to this project.

Create a fine-grained TLS identity with access to a project

First create a group and grant the group the [`operator`] entitlement on the project.

    lxc auth group create <group_name>
    lxc auth group permission add <group_name> project <project_name> operator

The [`operator`] entitlement grants members of the group permission to create and edit resources belonging to that project, but does not grant permission to delete the project or edit its configuration. See [[Fine-grained authorization]](../../explanation/authorization/#fine-grained-authorization) for more details.

Next create a TLS identity and add the identity to the group:

    lxc auth identity create tls/<client_name> [<certificate_file>] --group <group_name>

If [`<certificate_file>`] is provided the identity will be created directly. Otherwise, a token will be returned that the client can use to add the LXD server as a remote:

    # Client machine
    lxc remote add <remote_name> <token>

The client will be prompted with a list of projects to use as their default project. Only the configured project will be presented to the client.

Create a restricted trust store entry with access to a project

If you're using token authentication, create the token first:

    lxc query --request POST /1.0/certificates --data ''

See [[`POST`]` `[`/1.0/certificates`]](/lxd/latest/api/#/certificates/certificates_post) for more information.

The return value of this query contains an operation that has the information that is required to generate the trust token:

       ,
        ...
       }

Use this information to generate the trust token:

       echo -n '' | base64 -w0

To instead add the client certificate directly, send the following request:

    lxc query --request POST /1.0/certificates --data ''

The client can then authenticate using this trust token or client certificate and can only access the project or projects that have been specified.

On the client, generate a certificate to use for the connection:

       openssl req -x509 -newkey rsa:2048 -keyout "<keyfile_name>" -nodes \
       -out "<crtfile_name>" -subj "/CN=<client_name>"

Then send a POST request to the [`/1.0/certificates?public`] endpoint to authenticate:

       curl -k -s --key "<keyfile_name>" --cert "<crtfile_name>" \
       -X POST https://<server_address>/1.0/certificates \
       --data ''

See [[`POST`]` `[`/1.0/certificates?public`]](/lxd/latest/api/#/certificates/certificates_post_untrusted) for more information.

**Create a fine-grained TLS identity with access to a project**

First create a group and grant the group the [`operator`] entitlement on the project.

    lxc query --request POST /1.0/auth/groups --data ''

    lxc query --request PUT /1.0/auth/groups/<group_name> --data '
      ]
    }'

The [`operator`] entitlement grants members of the group permission to create and edit resources belonging to that project, but does not grant permission to delete the project or edit its configuration. See [[Fine-grained authorization]](../../explanation/authorization/#fine-grained-authorization) for more details.

Next create a TLS identity and add the identity to the group:

    lxc query --request POST /1.0/auth/identities/tls --data ''

See [[`POST`]` `[`/1.0/auth/identities/tls`]](/lxd/latest/api/#/auth/identitites/identities_post_tls) for more information.

The return value of this query contains the information that is required to generate the trust token:

       

Use this information to generate the trust token:

       echo -n '' | base64 -w0

To instead add the client certificate directly, send the following request:

    lxc query --request POST /1.0/certificates --data ''

If the certificate was added directly, the client is now authenticated with LXD. If a token was used, the client must use it to add their certificate.

On the client, generate a certificate to use for the connection:

       openssl req -x509 -newkey rsa:2048 -keyout "<keyfile_name>" -nodes \
       -out "<crtfile_name>" -subj "/CN=<client_name>"

Send a POST request to the [`/1.0/auth/identities/tls?public`] endpoint to authenticate:

       curl --insecure --key "<keyfile_name>" --cert "<crtfile_name>" \
       -X POST https://<server_address>/1.0/auth/identities/tls \
       --data ''

See [[`POST`]` `[`/1.0/auth/identities/tls?public`]](/lxd/latest/api/#/auth/identities/identities_post_tls_untrusted) for more information.

To confine access for an existing certificate:

CLI

API

**Trust store entry**

Use the following command:

    lxc config trust edit <fingerprint>

Make sure that [`restricted`] is set to [`true`] and specify the projects that the certificate should give access to under [`projects`].

**Fine-grained TLS or OIDC identity**

Create a group with the [`operator`] entitlement on the project:

    lxc auth group create <group_name>
    lxc auth group permission add <group_name> project <project_name> operator

Then add the group to the identity. For TLS identities run:

    lxc auth identity group add tls/<client_name> <group_name>

The [`<client_name>`] must be unique. If it is not, the certificate fingerprint of the client can be used.

For OIDC identities, run:

    lxc auth identity group add oidc/<client_name> <group_name>

The [`<client_name>`] must be unique. If it is not, the email address of the client can be used.

**Trust store entry**

Send the following request:

    lxc query --request PATCH /1.0/certificates/<fingerprint> --data ''

Make sure that [`restricted`] is set to [`true`] and specify the projects that the certificate should give access to under [`projects`].

**Fine-grained TLS or OIDC identity**

Create a group with the [`operator`] entitlement on the project:

    lxc query --request POST /1.0/auth/groups --data ''

    lxc query --request PUT /1.0/auth/groups/<group_name> --data '
      ]
    }'

Then add the group to the identity. For TLS identities run:

    lxc query --request PATCH /1.0/auth/identities/tls/<client_name> --data ''

The [`<client_name>`] must be unique. If it is not, the certificate fingerprint of the client can be used.

For OIDC identities, run:

    lxc query --request PATCH /1.0/auth/identities/oidc/<client_name> --data ''

The [`<client_name>`] must be unique. If it is not, the email address of the client can be used.

[]

## Confine users to specific LXD projects via Unix socket[¶](#confine-users-to-specific-lxd-projects-via-unix-socket "Link to this heading")

[[▶] [Watch on YouTube]](https://www.youtube.com/watch?v=6O0q3rSWr8A)

If you use the [LXD snap](https://snapcraft.io/lxd), you can configure the multi-user LXD daemon contained in the snap to dynamically create projects for all users in a specific user group.

To do so, set the [`daemon.user.group`] configuration option to the corresponding user group:

    sudo snap set lxd daemon.user.group=<user_group>

Make sure that all user accounts that you want to be able to use LXD are a member of this group.

Once a member of the group issues a LXD command, LXD creates a confined project for this user and switches to this project. If LXD has not been [[initialized]](../initialize/#initialize) at this point, it is automatically initialized (with the default settings).

If you want to customize the project settings, for example, to impose limits or restrictions, you can do so after the project has been created. To modify the project configuration, you must have full access to LXD, which means you must be part of the [`lxd`] group and not only the group that you configured as the LXD user group.