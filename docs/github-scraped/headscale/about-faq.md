# Source: https://headscale.net/stable/about/faq/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/about/faq.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/about/faq.md "View source of this page")

# Frequently Asked Questions[¶](#frequently-asked-questions "Permanent link")

## What is the design goal of headscale?[¶](#what-is-the-design-goal-of-headscale "Permanent link")

Headscale aims to implement a self-hosted, open source alternative to the [Tailscale](https://tailscale.com/) control server. Headscale\'s goal is to provide self-hosters and hobbyists with an open-source server they can use for their projects and labs. It implements a narrow scope, a *single* Tailscale network (tailnet), suitable for a personal use, or a small open-source organisation.

## How can I contribute?[¶](#how-can-i-contribute "Permanent link")

Headscale is \"Open Source, acknowledged contribution\", this means that any contribution will have to be discussed with the Maintainers before being submitted.

Please see [Contributing](../contributing/) for more information.

## Why is \'acknowledged contribution\' the chosen model?[¶](#why-is-acknowledged-contribution-the-chosen-model "Permanent link")

Both maintainers have full-time jobs and families, and we want to avoid burnout. We also want to avoid frustration from contributors when their PRs are not accepted.

We are more than happy to exchange emails, or to have dedicated calls before a PR is submitted.

## When/Why is Feature X going to be implemented?[¶](#whenwhy-is-feature-x-going-to-be-implemented "Permanent link")

We don\'t know. We might be working on it. If you\'re interested in contributing, please post a feature request about it.

Please be aware that there are a number of reasons why we might not accept specific contributions:

- It is not possible to implement the feature in a way that makes sense in a self-hosted environment.
- Given that we are reverse-engineering Tailscale to satisfy our own curiosity, we might be interested in implementing the feature ourselves.
- You are not sending unit and integration tests with it.

## Do you support Y method of deploying headscale?[¶](#do-you-support-y-method-of-deploying-headscale "Permanent link")

We currently support deploying headscale using our binaries and the DEB packages. Visit our [installation guide using official releases](../../setup/install/official/) for more information.

In addition to that, you may use packages provided by the community or from distributions. Learn more in the [installation guide using community packages](../../setup/install/community/).

For convenience, we also [build container images with headscale](../../setup/install/container/). But **please be aware that we don\'t officially support deploying headscale using Docker**. On our [Discord server](https://discord.gg/c84AZQhmpx) we have a \"docker-issues\" channel where you can ask for Docker-specific help to the community.

## What is the recommended update path? Can I skip multiple versions while updating?[¶](#what-is-the-recommended-update-path-can-i-skip-multiple-versions-while-updating "Permanent link")

Please follow the steps outlined in the [upgrade guide](../../setup/upgrade/) to update your existing Headscale installation. Its best to update from one stable version to the next (e.g. 0.24.0 → 0.25.1 → 0.26.1) in case you are multiple releases behind. You should always pick the latest available patch release.

Be sure to check the [changelog](https://github.com/juanfont/headscale/blob/main/CHANGELOG.md) for version specific upgrade instructions and breaking changes.

## Scaling / How many clients does Headscale support?[¶](#scaling-how-many-clients-does-headscale-support "Permanent link")

It depends. As often stated, Headscale is not enterprise software and our focus is homelabbers and self-hosters. Of course, we do not prevent people from using it in a commercial/professional setting and often get questions about scaling.

Please note that when Headscale is developed, performance is not part of the consideration as the main audience is considered to be users with a modest amount of devices. We focus on correctness and feature parity with Tailscale SaaS over time.

To understand if you might be able to use Headscale for your use case, I will describe two scenarios in an effort to explain what is the central bottleneck of Headscale:

1.  An environment with 1000 servers

2.  they rarely \"move\" (change their endpoints)

3.  new nodes are added rarely

4.  An environment with 80 laptops/phones (end user devices)

5.  nodes move often, e.g. switching from home to office

Headscale calculates a map of all nodes that need to talk to each other, creating this \"world map\" requires a lot of CPU time. When an event that requires changes to this map happens, the whole \"world\" is recalculated, and a new \"world map\" is created for every node in the network.

This means that under certain conditions, Headscale can likely handle 100s of devices (maybe more), if there is *little to no change* happening in the network. For example, in Scenario 1, the process of computing the world map is extremely demanding due to the size of the network, but when the map has been created and the nodes are not changing, the Headscale instance will likely return to a very low resource usage until the next time there is an event requiring the new map.

In the case of Scenario 2, the process of computing the world map is less demanding due to the smaller size of the network, however, the type of nodes will likely change frequently, which would lead to a constant resource usage.

Headscale will start to struggle when the two scenarios overlap, e.g. many nodes with frequent changes will cause the resource usage to remain constantly high. In the worst case scenario, the queue of nodes waiting for their map will grow to a point where Headscale never will be able to catch up, and nodes will never learn about the current state of the world.

We expect that the performance will improve over time as we improve the code base, but it is not a focus. In general, we will never make the tradeoff to make things faster on the cost of less maintainable or readable code. We are a small team and have to optimise for maintainability.

## Which database should I use?[¶](#which-database-should-i-use "Permanent link")

We recommend the use of SQLite as database for headscale:

- SQLite is simple to setup and easy to use
- It scales well for all of headscale\'s use cases
- Development and testing happens primarily on SQLite
- PostgreSQL is still supported, but is considered to be in \"maintenance mode\"

The headscale project itself does not provide a tool to migrate from PostgreSQL to SQLite. Please have a look at [the related tools documentation](../../ref/integration/tools/) for migration tooling provided by the community.

The choice of database has little to no impact on the performance of the server, see [Scaling / How many clients does Headscale support?](#scaling-how-many-clients-does-headscale-support) for understanding how Headscale spends its resources.

## Why is my reverse proxy not working with headscale?[¶](#why-is-my-reverse-proxy-not-working-with-headscale "Permanent link")

We don\'t know. We don\'t use reverse proxies with headscale ourselves, so we don\'t have any experience with them. We have [community documentation](../../ref/integration/reverse-proxy/) on how to configure various reverse proxies, and a dedicated \"reverse-proxy-issues\" channel on our [Discord server](https://discord.gg/c84AZQhmpx) where you can ask for help to the community.

## Can I use headscale and tailscale on the same machine?[¶](#can-i-use-headscale-and-tailscale-on-the-same-machine "Permanent link")

Running headscale on a machine that is also in the tailnet can cause problems with subnet routers, traffic relay nodes, and MagicDNS. It might work, but it is not supported.

## Why do two nodes see each other in their status, even if an ACL allows traffic only in one direction?[¶](#why-do-two-nodes-see-each-other-in-their-status-even-if-an-acl-allows-traffic-only-in-one-direction "Permanent link")

A frequent use case is to allow traffic only from one node to another, but not the other way around. For example, the workstation of an administrator should be able to connect to all nodes but the nodes themselves shouldn\'t be able to connect back to the administrator\'s node. Why do all nodes see the administrator\'s workstation in the output of `tailscale status`?

This is essentially how Tailscale works. If traffic is allowed to flow in one direction, then both nodes see each other in their output of `tailscale status`. Traffic is still filtered according to the ACL, with the exception of `tailscale ping` which is always allowed in either direction.

See also <https://tailscale.com/kb/1087/device-visibility>.

## My policy is stored in the database and Headscale refuses to start due to an invalid policy. How can I recover?[¶](#my-policy-is-stored-in-the-database-and-headscale-refuses-to-start-due-to-an-invalid-policy-how-can-i-recover "Permanent link") 

Headscale checks if the policy is valid during startup and refuses to start if it detects an error. The error message indicates which part of the policy is invalid. Follow these steps to fix your policy:

- Dump the policy to a file: `headscale policy get --bypass-grpc-and-access-database-directly > policy.json`
- Edit and fixup `policy.json`. Use the command `headscale policy check --file policy.json` to validate the policy.
- Load the modified policy: `headscale policy set --bypass-grpc-and-access-database-directly --file policy.json`
- Start Headscale as usual.

Full server configuration required

The above commands to get/set the policy require a complete server configuration file including database settings. A minimal config to [control Headscale via remote CLI](../../ref/remote-cli/) is not sufficient. You may use `headscale -c /path/to/config.yaml` to specify the path to an alternative configuration file.

## How can I avoid to send logs to Tailscale Inc?[¶](#how-can-i-avoid-to-send-logs-to-tailscale-inc "Permanent link")

A Tailscale client [collects logs about its operation and connection attempts with other clients](https://tailscale.com/kb/1011/log-mesh-traffic#client-logs) and sends them to a central log service operated by Tailscale Inc.

Headscale, by default, instructs clients to disable log submission to the central log service. This configuration is applied by a client once it successfully connected with Headscale. See the configuration option `logtail.enabled` in the [configuration file](../../ref/configuration/) for details.

Alternatively, logging can also be disabled on the client side. This is independent of Headscale and opting out of client logging disables log submission early during client startup. The configuration is operating system specific and is usually achieved by setting the environment variable `TS_NO_LOGS_NO_SUPPORT=true` or by passing the flag `--no-logs-no-support` to `tailscaled`. See <https://tailscale.com/kb/1011/log-mesh-traffic#opting-out-of-client-logging> for details.