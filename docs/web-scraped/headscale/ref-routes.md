# Source: https://headscale.net/stable/ref/routes/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/ref/routes.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/ref/routes.md "View source of this page")

# Routes[¶](#routes "Permanent link")

Headscale supports route advertising and can be used to manage [subnet routers](https://tailscale.com/kb/1019/subnets) and [exit nodes](https://tailscale.com/kb/1103/exit-nodes) for a tailnet.

- [Subnet routers](#subnet-router) may be used to connect an existing network such as a virtual private cloud or an on-premise network with your tailnet. Use a subnet router to access devices where Tailscale can\'t be installed or to gradually rollout Tailscale.
- [Exit nodes](#exit-node) can be used to route all Internet traffic for another Tailscale node. Use it to securely access the Internet on an untrusted Wi-Fi or to access online services that expect traffic from a specific IP address.

## Subnet router[¶](#subnet-router "Permanent link")

The setup of a subnet router requires double opt-in, once from a subnet router and once on the control server to allow its use within the tailnet. Optionally, use [`autoApprovers` to automatically approve routes from a subnet router](#automatically-approve-routes-of-a-subnet-router).

### Setup a subnet router[¶](#setup-a-subnet-router "Permanent link")

#### Configure a node as subnet router[¶](#configure-a-node-as-subnet-router "Permanent link")

Register a node and advertise the routes it should handle as comma separated list:

    $ sudo tailscale up --login-server <YOUR_HEADSCALE_URL> --advertise-routes=10.0.0.0/8,192.168.0.0/24

If the node is already registered, it can advertise new routes or update previously announced routes with:

    $ sudo tailscale set --advertise-routes=10.0.0.0/8,192.168.0.0/24

Finally, [enable IP forwarding](#enable-ip-forwarding) to route traffic.

#### Enable the subnet router on the control server[¶](#enable-the-subnet-router-on-the-control-server "Permanent link")

The routes of a tailnet can be displayed with the `headscale nodes list-routes` command. A subnet router with the hostname `myrouter` announced the IPv4 networks `10.0.0.0/8` and `192.168.0.0/24`. Those need to be approved before they can be used.

    $ headscale nodes list-routes
    ID | Hostname | Approved | Available                  | Serving (Primary)
    1  | myrouter |          | 10.0.0.0/8, 192.168.0.0/24 |

Approve all desired routes of a subnet router by specifying them as comma separated list:

    $ headscale nodes approve-routes --identifier 1 --routes 10.0.0.0/8,192.168.0.0/24
    Node updated

The node `myrouter` can now route the IPv4 networks `10.0.0.0/8` and `192.168.0.0/24` for the tailnet.

    $ headscale nodes list-routes
    ID | Hostname | Approved                   | Available                  | Serving (Primary)
    1  | myrouter | 10.0.0.0/8, 192.168.0.0/24 | 10.0.0.0/8, 192.168.0.0/24 | 10.0.0.0/8, 192.168.0.0/24

#### Use the subnet router[¶](#use-the-subnet-router "Permanent link")

To accept routes advertised by a subnet router on a node:

    $ sudo tailscale set --accept-routes

Please refer to the official [Tailscale documentation](https://tailscale.com/kb/1019/subnets#use-your-subnet-routes-from-other-devices) for how to use a subnet router on different operating systems.

### Restrict the use of a subnet router with ACL[¶](#restrict-the-use-of-a-subnet-router-with-acl "Permanent link")

The routes announced by subnet routers are available to the nodes in a tailnet. By default, without an ACL enabled, all nodes can accept and use such routes. Configure an ACL to explicitly manage who can use routes.

The ACL snippet below defines three hosts, a subnet router `router`, a regular node `node` and `service.example.net` as internal service that can be reached via a route on the subnet router `router`. It allows the node `node` to access `service.example.net` on port 80 and 443 which is reachable via the subnet router. Access to the subnet router itself is denied.

[Access the routes of a subnet router without the subnet router itself]

    ,
      "acls": [
        
      ]
    }

### Automatically approve routes of a subnet router[¶](#automatically-approve-routes-of-a-subnet-router "Permanent link")

The initial setup of a subnet router usually requires manual approval of their announced routes on the control server before they can be used by a node in a tailnet. Headscale supports the `autoApprovers` section of an ACL to automate the approval of routes served with a subnet router.

The ACL snippet below defines the tag `tag:router` owned by the user `alice`. This tag is used for `routes` in the `autoApprovers` section. The IPv4 route `192.168.0.0/24` is automatically approved once announced by a subnet router owned by the user `alice` and that also advertises the tag `tag:router`.

[Subnet routers owned by alice and tagged with tag:router are automatically approved]

    ,
      "autoApprovers": 
      },
      "acls": [
        // more rules
      ]
    }

Advertise the route `192.168.0.0/24` from a subnet router that also advertises the tag `tag:router` when joining the tailnet:

    $ sudo tailscale up --login-server <YOUR_HEADSCALE_URL> --advertise-tags tag:router --advertise-routes 192.168.0.0/24

Please see the [official Tailscale documentation](https://tailscale.com/kb/1337/acl-syntax#autoapprovers) for more information on auto approvers.

## Exit node[¶](#exit-node "Permanent link")

The setup of an exit node requires double opt-in, once from an exit node and once on the control server to allow its use within the tailnet. Optionally, use [`autoApprovers` to automatically approve an exit node](#automatically-approve-an-exit-node-with-auto-approvers).

### Setup an exit node[¶](#setup-an-exit-node "Permanent link")

#### Configure a node as exit node[¶](#configure-a-node-as-exit-node "Permanent link")

Register a node and make it advertise itself as an exit node:

    $ sudo tailscale up --login-server <YOUR_HEADSCALE_URL> --advertise-exit-node

If the node is already registered, it can advertise exit capabilities like this:

    $ sudo tailscale set --advertise-exit-node

Finally, [enable IP forwarding](#enable-ip-forwarding) to route traffic.

#### Enable the exit node on the control server[¶](#enable-the-exit-node-on-the-control-server "Permanent link")

The routes of a tailnet can be displayed with the `headscale nodes list-routes` command. An exit node can be recognized by its announced routes: `0.0.0.0/0` for IPv4 and `::/0` for IPv6. The exit node with the hostname `myexit` is already available, but needs to be approved:

    $ headscale nodes list-routes
    ID | Hostname | Approved | Available       | Serving (Primary)
    1  | myexit   |          | 0.0.0.0/0, ::/0 |

For exit nodes, it is sufficient to approve either the IPv4 or IPv6 route. The other will be approved automatically.

    $ headscale nodes approve-routes --identifier 1 --routes 0.0.0.0/0
    Node updated

The node `myexit` is now approved as exit node for the tailnet:

    $ headscale nodes list-routes
    ID | Hostname | Approved        | Available       | Serving (Primary)
    1  | myexit   | 0.0.0.0/0, ::/0 | 0.0.0.0/0, ::/0 | 0.0.0.0/0, ::/0

#### Use the exit node[¶](#use-the-exit-node "Permanent link")

The exit node can now be used on a node with:

    $ sudo tailscale set --exit-node myexit

Please refer to the official [Tailscale documentation](https://tailscale.com/kb/1103/exit-nodes#use-the-exit-node) for how to use an exit node on different operating systems.

### Restrict the use of an exit node with ACL[¶](#restrict-the-use-of-an-exit-node-with-acl "Permanent link")

An exit node is offered to all nodes in a tailnet. By default, without an ACL enabled, all nodes in a tailnet can select and use an exit node. Configure `autogroup:internet` in an ACL rule to restrict who can use *any* of the available exit nodes.

[Example use of autogroup:internet]

    
      ]
    }

### Restrict access to exit nodes per user or group[¶](#restrict-access-to-exit-nodes-per-user-or-group "Permanent link")

A user can use *any* of the available exit nodes with `autogroup:internet`. Alternatively, the ACL snippet below assigns each user a specific exit node while hiding all other exit nodes. The user `alice` can only use exit node `exit1` while user `bob` can only use exit node `exit2`.

[Assign each user a dedicated exit node]

    ,
      "acls": [
        ,
        
      ]
    }

Warning

- The above implementation is Headscale specific and will likely be removed once [support for `via`](https://github.com/juanfont/headscale/issues/2409) is available.
- Beware that a user can also connect to any port of the exit node itself.

### Automatically approve an exit node with auto approvers[¶](#automatically-approve-an-exit-node-with-auto-approvers "Permanent link")

The initial setup of an exit node usually requires manual approval on the control server before it can be used by a node in a tailnet. Headscale supports the `autoApprovers` section of an ACL to automate the approval of a new exit node as soon as it joins the tailnet.

The ACL snippet below defines the tag `tag:exit` owned by the user `alice`. This tag is used for `exitNode` in the `autoApprovers` section. A new exit node which is owned by the user `alice` and that also advertises the tag `tag:exit` is automatically approved:

[Exit nodes owned by alice and tagged with tag:exit are automatically approved]

    ,
      "autoApprovers": ,
      "acls": [
        // more rules
      ]
    }

Advertise a node as exit node and also advertise the tag `tag:exit` when joining the tailnet:

    $ sudo tailscale up --login-server <YOUR_HEADSCALE_URL> --advertise-tags tag:exit --advertise-exit-node

Please see the [official Tailscale documentation](https://tailscale.com/kb/1337/acl-syntax#autoapprovers) for more information on auto approvers.

## High availability[¶](#high-availability "Permanent link")

Headscale has limited support for high availability routing. Multiple subnet routers with overlapping routes or multiple exit nodes can be used to provide high availability for users. If one router node goes offline, another one can serve the same routes to clients. Please see the official [Tailscale documentation on high availability](https://tailscale.com/kb/1115/high-availability#subnet-router-high-availability) for details.

Bug

In certain situations it might take up to 16 minutes for Headscale to detect a node as offline. A failover node might not be selected fast enough, if such a node is used as subnet router or exit node causing service interruptions for clients. See [issue 2129](https://github.com/juanfont/headscale/issues/2129) for more information.

## Troubleshooting[¶](#troubleshooting "Permanent link")

### Enable IP forwarding[¶](#enable-ip-forwarding "Permanent link")

A subnet router or exit node is routing traffic on behalf of other nodes and thus requires IP forwarding. Check the official [Tailscale documentation](https://tailscale.com/kb/1019/subnets/?tab=linux#enable-ip-forwarding) for how to enable IP forwarding.