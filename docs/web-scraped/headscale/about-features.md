# Source: https://headscale.net/stable/about/features/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/about/features.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/about/features.md "View source of this page")

# Features[¶](#features "Permanent link")

Headscale aims to implement a self-hosted, open source alternative to the Tailscale control server. Headscale\'s goal is to provide self-hosters and hobbyists with an open-source server they can use for their projects and labs. This page provides on overview of Headscale\'s feature and compatibility with the Tailscale control server:

[] Full \"base\" support of Tailscale\'s features

[] Node registration

[] Interactive

[] Pre authenticated key

[] [DNS](../../ref/dns/)

[] [MagicDNS](https://tailscale.com/kb/1081/magicdns)

[] [Global and restricted nameservers (split DNS)](https://tailscale.com/kb/1054/dns#nameservers)

[] [search domains](https://tailscale.com/kb/1054/dns#search-domains)

[] [Extra DNS records (Headscale only)](../../ref/dns/#setting-extra-dns-records)

[] [Taildrop (File Sharing)](https://tailscale.com/kb/1106/taildrop)

[] [Routes](../../ref/routes/)

[] [Subnet routers](../../ref/routes/#subnet-router)

[] [Exit nodes](../../ref/routes/#exit-node)

[] Dual stack (IPv4 and IPv6)

[] Ephemeral nodes

[] Embedded [DERP server](../../ref/derp/)

[] Access control lists ([GitHub label \"policy\"](https://github.com/juanfont/headscale/labels/policy%20%F0%9F%93%9D))

[] ACL management via API

[] Some [Autogroups](https://tailscale.com/kb/1396/targets#autogroups), currently: `autogroup:internet`, `autogroup:nonroot`, `autogroup:member`, `autogroup:tagged`, `autogroup:self`

[] [Auto approvers](https://tailscale.com/kb/1337/acl-syntax#auto-approvers) for [subnet routers](../../ref/routes/#automatically-approve-routes-of-a-subnet-router) and [exit nodes](../../ref/routes/#automatically-approve-an-exit-node-with-auto-approvers)

[] [Tailscale SSH](https://tailscale.com/kb/1193/tailscale-ssh)

[] [Node registration using Single-Sign-On (OpenID Connect)](../../ref/oidc/) ([GitHub label \"OIDC\"](https://github.com/juanfont/headscale/labels/OIDC))

[] Basic registration

[] Update user profile from identity provider

[] OIDC groups cannot be used in ACLs

[] [Funnel](https://tailscale.com/kb/1223/funnel) ([#1040](https://github.com/juanfont/headscale/issues/1040))

[] [Serve](https://tailscale.com/kb/1312/serve) ([#1234](https://github.com/juanfont/headscale/issues/1921))

[] [Network flow logs](https://tailscale.com/kb/1219/network-flow-logs) ([#1687](https://github.com/juanfont/headscale/issues/1687))