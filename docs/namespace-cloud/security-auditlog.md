<!-- Source: https://namespace.so/docs/security/auditlog -->

# Audit Logs

Changes made to your workspace, instances, and volumes produce audit logging entries which can be used for security and debugging purposes.

Audit entries are available in Namespace's UI and can be filtered for certain actions or actors.

![Audit Events Table](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Faudit-events-ui.124cbc7a.png&w=1920&q=75)

Audit Events in the Namespace Dashboard

## Audit Log Forwarding (SIEM)

Namespace also supports pushing audit events to a customer provided SIEM (Security Information & Event Management) solution.
This allows for centralized analysis, streamlined compliance, and real-time threat detection within your existing security tooling.

Audit Log Forwarding is available to **Enterprise** customers.

To set up Audit Log Forwarding with SIEM for your workspace, reach out via your dedicated support channel or email us at
[support@namespace.so](mailto:support@namespace.so).

# Audit Log Types

Namespace audit logs include many different actions, including contextual data to understand exactly what happened.
The most important actions and what data they contain are detailed below:

## artifact.expire

An artifact's expiration time was updated.

```
{
    "action": "artifact.expire",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "namespace": "builds",
        "new_expired_at": "2024-12-31T00:00:00Z",
        "path": "my-artifact"
    },
    "tenant_id": "tenant_..."
}
```

## artifact.finalize

An artifact was finalized (upload completed).

```
{
    "action": "artifact.finalize",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "namespace": "builds",
        "path": "my-artifact"
    },
    "tenant_id": "tenant_..."
}
```

## artifact.resolve

An artifact was resolved (downloaded or accessed).

```
{
    "action": "artifact.resolve",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "namespace": "builds",
        "path": "my-artifact"
    },
    "tenant_id": "tenant_..."
}
```

## billing.contact.update

The billing contact information was updated.

```
{
    "action": "billing.contact.update",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "tenant_id": "tenant_..."
}
```

## devbox.create

A devbox was created.

```
{
    "action": "devbox.create",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "site": "sjc1"
    },
    "targets": [
        {
            "devbox_id": "...",
            "type": "devbox"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## devbox.expire

A devbox was expired (terminated).

```
{
    "action": "devbox.expire",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "devbox_id": "...",
            "type": "devbox"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## federation.github.associate

Namespace's [GitHub federation](/docs/federation/github-actions) application has been associated with the workspace.

```
{
    "action": "federation.github.associate",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "github_installation_id": "1234...",
            "type": "github_installation"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## federation.github.deassociate

Namespace's [GitHub federation](/docs/federation/github-actions) application has been deassociated from the workspace.

```
{
    "action": "federation.github.deassociate",
    "actor": {
        "claims": {
            "login": "octocat"
        },
        "source": "github",
        "type": "external"
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "github_installation_id": "1234...",
            "type": "github_installation"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## github.installation.associate

Namespace's [GitHub runner](/docs/solutions/github-actions) application has been associated with the workspace.

```
{
    "action": "github.installation.associate",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "github_installation_id": "1234...",
            "type": "github_installation"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## github.installation.deassociate

Namespace's [GitHub runner](/docs/solutions/github-actions) application has been deassociated from the workspace.

```
{
    "action": "github.installation.deassociate",
    "actor": {
        "claims": {
            "login": "octocat"
        },
        "source": "github",
        "type": "external"
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "github_installation_id": "1234...",
            "type": "github_installation"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## github.profile.build\_custom\_image

A custom image build was triggered for a GitHub runner profile.

```
{
    "action": "github.profile.build_custom_image",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "github_profile_id": "...",
            "type": "github_profile"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## github.profile.create

A GitHub runner profile has been created.

```
{
    "action": "github.profile.create",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "github_profile_id": "...",
            "type": "github_profile"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## github.profile.delete

A GitHub runner profile has been deleted.

```
{
    "action": "github.profile.delete",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "github_profile_id": "...",
            "type": "github_profile"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## github.profile.update

A GitHub runner profile has been updated.

```
{
    "action": "github.profile.update",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "github_profile_id": "...",
            "type": "github_profile"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## instance.destroy

An instance was destroyed.

```
{
    "action": "instance.destroy",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "instance_id": "...",
            "type": "instance"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## instance.ssh

An SSH session was initiated with a workspace instance.

```
{
    "action": "instance.ssh",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "instance_id": "...",
            "type": "instance"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## registry.manifest.create

A container manifest was pushed to the registry.

```
{
    "action": "registry.manifest.create",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "image_digest": "sha256:..."
    },
    "targets": [
        {
            "image_ref": "nscr.io/abc123/my-app@sha256:...",
            "type": "registry_image"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## registry.manifest.delete

A container manifest was deleted from the registry.

```
{
    "action": "registry.manifest.delete",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "image_digest": "sha256:..."
    },
    "targets": [
        {
            "image_ref": "nscr.io/abc123/my-app@sha256:...",
            "type": "registry_image"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## registry.repository.delete

A container repository was deleted from the registry.

```
{
    "action": "registry.repository.delete",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "image_ref": "nscr.io/abc123/my-app@sha256:...",
            "type": "registry_image"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## registry.tag.create

A tag was created in the container registry.

```
{
    "action": "registry.tag.create",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "image_digest": "sha256:...",
        "image_tag": "latest"
    },
    "targets": [
        {
            "image_ref": "nscr.io/abc123/my-app@sha256:...",
            "type": "registry_image"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## registry.tag.delete

A tag was deleted from the container registry.

```
{
    "action": "registry.tag.delete",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "image_tag": "latest"
    },
    "targets": [
        {
            "image_ref": "nscr.io/abc123/my-app@sha256:...",
            "type": "registry_image"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## token.revokable.create

An API token was created for the workspace.

```
{
    "action": "token.revokable.create",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "expires_at": "2025-01-01T00:00:00Z",
        "name": "CI Token",
        "token_id": "tok_..."
    },
    "tenant_id": "tenant_..."
}
```

## token.revokable.refresh

An API token expiry was refreshed.

```
{
    "action": "token.revokable.refresh",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "expires_at": "2025-02-01T00:00:00Z",
        "minimum_duration": "720h0m0s",
        "previous_expires_at": "2025-01-01T00:00:00Z"
    },
    "tenant_id": "tenant_..."
}
```

## token.revokable.revoke

An API token was revoked.

```
{
    "action": "token.revokable.revoke",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "token_id": "tok_..."
    },
    "tenant_id": "tenant_..."
}
```

## token.revokable.used

An API token was used to authenticate.

```
{
    "action": "token.revokable.used",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "tenant_id": "tenant_..."
}
```

## vault.list

Vault secrets were listed for the workspace.

```
{
    "action": "vault.list",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "tenant_id": "tenant_..."
}
```

## vault.resolve

A vault secret was resolved (accessed).

```
{
    "action": "vault.resolve",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "secret_id": "sec_...",
            "type": "vault_secret"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## vault.set

A vault secret was created or updated.

```
{
    "action": "vault.set",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "secret_id": "sec_...",
            "type": "vault_secret"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## volume.release

Emitted when a volume is released by an actor, e.g. by pressing `[Release]` in the Web application.

```
{
    "action": "volume.release",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "tag": "my-volume"
    },
    "tenant_id": "tenant_..."
}
```

## vpc.attach

A VPC network segment was attached to an instance.

```
{
    "action": "vpc.attach",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "targets": [
        {
            "network_segment_tag": "egress-...",
            "type": "network_segment"
        }
    ],
    "tenant_id": "tenant_..."
}
```

## workspace.membership.add

A user has been added to the workspace.

```
{
    "action": "workspace.membership.add",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "role": "READER"
    },
    "targets": [
        {
            "email": "quux@example.com",
            "type": "user",
            "user_id": "user_..."
        }
    ],
    "tenant_id": "tenant_..."
}
```

## workspace.membership.remove

A user has been removed from the workspace.

```
{
    "action": "workspace.membership.remove",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "role": "READER"
    },
    "targets": [
        {
            "email": "quux@example.com",
            "type": "user",
            "user_id": "user_..."
        }
    ],
    "tenant_id": "tenant_..."
}
```

## workspace.membership.sso\_join

A user joined the workspace via SSO.

```
{
    "action": "workspace.membership.sso_join",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "role": "READER"
    },
    "targets": [
        {
            "email": "quux@example.com",
            "type": "user",
            "user_id": "user_..."
        }
    ],
    "tenant_id": "tenant_..."
}
```

## workspace.membership.update

The role of a workspace member was changed.

```
{
    "action": "workspace.membership.update",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "role": "ADMIN"
    },
    "targets": [
        {
            "email": "quux@example.com",
            "type": "user",
            "user_id": "user_..."
        }
    ],
    "tenant_id": "tenant_..."
}
```

## workspace.ownership.transfer

Ownership of a Workspace has been transferred to a different user

```
{
    "action": "workspace.ownership.transfer",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "previous_owner": {
            "email": "old-owner@example.com",
            "type": "user",
            "user_id": "user..."
        }
    },
    "targets": [
        {
            "email": "quux@example.com",
            "type": "user",
            "user_id": "user_..."
        }
    ],
    "tenant_id": "tenant_..."
}
```

## workspace.token.emit

An authorization token has been emitted for the workspace, e.g. a user signed in.

```
{
    "action": "workspace.token.emit",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "duration": "600s"
    },
    "tenant_id": "tenant_..."
}
```

## workspace.trust.update

The workspace trust relationships were updated.

```
{
    "action": "workspace.trust.update",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "metadata": {}
    },
    "tenant_id": "tenant_..."
}
```

## workspace.update

The Workspace configuration was updated.

```
{
    "action": "workspace.update",
    "actor": {
        "email": "foobar@example.com",
        "type": "user",
        "user_id": "user_..."
    },
    "at": "2025-03-14T21:08:41+00:00",
    "attributes": {
        "name": "New Workspace Name"
    },
    "tenant_id": "tenant_..."
}
```

Last updated February 2, 2026
