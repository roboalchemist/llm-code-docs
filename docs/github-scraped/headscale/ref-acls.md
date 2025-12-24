# Source: https://headscale.net/stable/ref/acls/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/ref/acls.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/ref/acls.md "View source of this page")

# ACLs

Headscale implements the same policy ACLs as Tailscale.com, adapted to the self-hosted environment.

For instance, instead of referring to users when defining groups you must use users (which are the equivalent to user/logins in Tailscale.com).

Please check <https://tailscale.com/kb/1018/acls/> for further information.

When using ACL\'s the User borders are no longer applied. All machines whichever the User have the ability to communicate with other hosts as long as the ACL\'s permits this exchange.

## ACL Setup[¶](#acl-setup "Permanent link")

To enable and configure ACLs in Headscale, you need to specify the path to your ACL policy file in the `policy.path` key in `config.yaml`.

Your ACL policy file must be formatted using [huJSON](https://github.com/tailscale/hujson).

Info on how these policies are written can be found [here](https://tailscale.com/kb/1018/acls/).

Please reload or restart Headscale after updating the ACL file. Headscale may be reloaded either via its systemd service (`sudo systemctl reload headscale`) or by sending a SIGHUP signal (`sudo kill -HUP $(pidof headscale)`) to the main process. Headscale logs the result of ACL policy processing after each reload.

## Simple Examples[¶](#simple-examples "Permanent link")

- [**Allow All**](https://tailscale.com/kb/1192/acl-samples#allow-all-default-acl): If you define an ACL file but completely omit the `"acls"` field from its content, Headscale will default to an \"allow all\" policy. This means all devices connected to your tailnet will be able to communicate freely with each other.

  ::: 
      
  :::

- [**Deny All**](https://tailscale.com/kb/1192/acl-samples#deny-all): To prevent all communication within your tailnet, you can include an empty array for the `"acls"` field in your policy file.

  ::: 
      
  :::

## Complex Example[¶](#complex-example "Permanent link")

Let\'s build a more complex example use case for a small business (It may be the place where ACL\'s are the most useful).

We have a small company with a boss, an admin, two developers and an intern.

The boss should have access to all servers but not to the user\'s hosts. Admin should also have access to all hosts except that their permissions should be limited to maintaining the hosts (for example purposes). The developers can do anything they want on dev hosts but only watch on productions hosts. Intern can only interact with the development servers.

There\'s an additional server that acts as a router, connecting the VPN users to an internal network `10.20.0.0/16`. Developers must have access to those internal resources.

Each user have at least a device connected to the network and we have some servers.

- database.prod
- database.dev
- app-server1.prod
- app-server1.dev
- billing.internal
- router.internal

![ACL implementation example](../../images/headscale-acl-network.png)

When [registering the servers](../../usage/getting-started/#register-a-node) we will need to add the flag `--advertise-tags=tag:<tag1>,tag:<tag2>`, and the user that is registering the server should be allowed to do it. Since anyone can add tags to a server they can register, the check of the tags is done on headscale server and only valid tags are applied. A tag is valid if the user that is registering it is allowed to do it.

Here are the ACL\'s to implement the same permissions as above:

[acl.json]

    ,
      // tagOwners in tailscale is an association between a TAG and the people allowed to set this TAG on a server.
      // This is documented [here](https://tailscale.com/kb/1068/acl-tags#defining-a-tag)
      // and explained [here](https://tailscale.com/blog/rbac-like-it-was-meant-to-be/)
      "tagOwners": ,
      // hosts should be defined using its IP addresses and a subnet mask.
      // to define a single host, use a /32 mask. You cannot use DNS entries here,
      // as they're prone to be hijacked by replacing their IP addresses.
      // see https://github.com/tailscale/tailscale/issues/3800 for more information.
      "hosts": ,
      "acls": [
        // boss have access to all servers
        ,

        // admin have only access to administrative ports of the servers, in tcp/22
        ,

        // we also allow admin to ping the servers
        ,

        // developers have access to databases servers and application servers on all ports
        // they can only view the applications servers in prod and have no access to databases servers in production
        ,
        // developers have access to the internal network through the router.
        // the internal network is composed of HTTPS endpoints and Postgresql
        // database servers.
        ,

        // servers should be able to talk to database in tcp/5432. Database should not be able to initiate connections to
        // applications servers
        ,
        ,

        // interns have access to dev-app-servers only in reading mode
        ,

        // Allow users to access their own devices using autogroup:self (see below for more details about performance impact)
        
      ]
    }

## Autogroups[¶](#autogroups "Permanent link")

Headscale supports several autogroups that automatically include users, destinations, or devices with specific properties. Autogroups provide a convenient way to write ACL rules without manually listing individual users or devices.

### `autogroup:internet`[¶](#autogroupinternet "Permanent link")

Allows access to the internet through [exit nodes](../routes/#exit-node). Can only be used in ACL destinations.

    

### `autogroup:member`[¶](#autogroupmember "Permanent link")

Includes all users who are direct members of the tailnet. Does not include users from shared devices.

    

### `autogroup:tagged`[¶](#autogrouptagged "Permanent link")

Includes all devices that have at least one tag.

    

### `autogroup:self`[¶](#autogroupself "Permanent link")

**(EXPERIMENTAL)**

The current implementation of `autogroup:self` is inefficient

Includes devices where the same user is authenticated on both the source and destination. Does not include tagged devices. Can only be used in ACL destinations.

    

*Using `autogroup:self` may cause performance degradation on the Headscale coordinator server in large deployments, as filter rules must be compiled per-node rather than globally and the current implementation is not very efficient.*

If you experience performance issues, consider using more specific ACL rules or limiting the use of `autogroup:self`.

    ,
      ,
      ,
      ,
      
    }

### `autogroup:nonroot`[¶](#autogroupnonroot "Permanent link")

Used in Tailscale SSH rules to allow access to any user except root. Can only be used in the `users` field of SSH rules.