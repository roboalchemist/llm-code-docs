# Source: https://documentation.ubuntu.com/lxd/en/latest/explanation/security/

[][]

# Security[¶](#security "Link to this heading")

[[▶] [Watch on YouTube]](https://www.youtube.com/watch?v=cOOzKdYHkus)

Consider the following aspects to ensure that your LXD installation is secure:

-   Keep your operating system up-to-date and install all available security patches.

-   Use only supported LXD versions (LTS releases or the latest feature release).

-   Restrict access to the LXD daemon and the remote API.

-   Configure your network interfaces to be secure.

-   Do not use privileged containers unless required. If you use privileged containers, put appropriate security measures in place.

See the following sections for detailed information. Also see: [[How to harden security for LXD]](../../howto/security_harden/#howto-security-harden).

If you discover a security issue, see the [LXD security policy](https://github.com/canonical/lxd/blob/main/SECURITY.md) for information on how to report the issue.

## Supported versions[¶](#supported-versions "Link to this heading")

Never use unsupported LXD versions in a production environment.

LXD has two types of releases:

-   Feature releases

-   LTS releases

For feature releases, only the latest one is supported, and we usually don't do point releases. Instead, users are expected to wait until the next feature release.

For LTS releases, we do periodic bugfix releases that include an accumulation of bugfixes from the feature releases. Such bugfix releases do not include new features.

[]

## Access to the LXD daemon[¶](#access-to-the-lxd-daemon "Link to this heading")

LXD is a daemon that can be accessed locally over a Unix socket or, if configured, remotely over a TLS socket. Anyone with access to the socket can fully control LXD, which includes the ability to attach host devices and file systems or to tweak the security features for all instances.

Therefore, make sure to restrict the access to the daemon to trusted users.

### Local access to the LXD daemon[¶](#local-access-to-the-lxd-daemon "Link to this heading")

The LXD daemon runs as root and provides a Unix socket for local communication. Access control for LXD is based on group membership. The root user and all members of the [`lxd`] group can interact with the local daemon.

Important

Local access to LXD through the Unix socket always grants full access to LXD. This includes the ability to attach file system paths or devices to any instance as well as tweak the security features on any instance.

Therefore, you should only give such access to users who you'd trust with root access to your system.

[]

### Access to the remote API[¶](#access-to-the-remote-api "Link to this heading")

By default, access to the daemon is only possible locally. By setting the [[`core.https_address`]](../../server/#server-core:core.https_address) configuration option, you can expose the same API over the network on a TLS socket. See [[How to expose LXD to the network]](../../howto/server_expose/#server-expose) for instructions. Remote clients can then connect to LXD and access any image that is marked for public use.

There are several ways to authenticate remote clients as trusted clients to allow them to access the API. See [[Remote API authentication]](../../authentication/#authentication) for details.

In a production setup, you should set [[`core.https_address`]](../../server/#server-core:core.https_address) to the single address where the server should be available (rather than any address on the host). In addition, you should set firewall rules to allow access to the LXD port only from authorized hosts/subnets.

[]

## Container security[¶](#container-security "Link to this heading")

LXD containers can use a wide range of features for security.

Also see the [LXC security page](https://linuxcontainers.org/lxc/security/) on [`linuxcontainers.org`] for details on LXC container security and the applied kernel features.

### Unprivileged containers[¶](#unprivileged-containers "Link to this heading")

By default, containers are *unprivileged*, meaning that they operate inside a user namespace, restricting the abilities of users in the container to that of regular users on the host with limited privileges on the devices that the container owns.

Unprivileged containers are safe by design: The container UID 0 is mapped to an unprivileged user outside of the container. It has extra rights only on resources that it owns itself.

This mechanism ensures that most security issues (for example, container escape or resource abuse) that might occur in a container apply just as well to a random unprivileged user, which means they are a generic kernel security bug rather than a LXD issue.

Tip

If data sharing between containers isn't needed, you can enable [[`security.idmap.isolated`]](../../reference/instance_options/#instance-security:security.idmap.isolated), which will use non-overlapping UID/GID maps for each container, preventing potential DoS attacks on other containers.

### Privileged containers[¶](#privileged-containers "Link to this heading")

LXD can also run *privileged* containers. In privileged containers, the container UID 0 is mapped to the host's UID 0.

Such privileged containers are not root-safe, and a user with root access in such a container will be able to DoS the host as well as find ways to escape confinement.

LXC applies some protection measures to privileged containers to prevent accidental damage of the host (where damage is defined as things like reconfiguring host hardware, reconfiguring the host kernel, or accessing the host file system). This protection of the host and prevention of escape is achieved through mandatory access control ([`apparmor`], [`selinux`]), Seccomp filters, dropping of capabilities, and namespaces. These measures are valuable when running trusted workloads, but they do not make privileged containers root-safe.

Therefore, you should not use privileged containers unless required. If you use them, make sure to put appropriate security measures in place.

## Network security[¶](#network-security "Link to this heading")

Make sure to configure your network interfaces to be secure. Which aspects you should consider depends on the networking mode you decide to use.

[]

### Bridged NIC security[¶](#bridged-nic-security "Link to this heading")

The default networking mode in LXD is to provide a "managed" private network bridge that each instance connects to. In this mode, there is an interface on the host called [`lxdbr0`] that acts as the bridge for the instances.

The host runs an instance of [`dnsmasq`] for each managed bridge, which is responsible for allocating IP addresses and providing both authoritative and recursive DNS services.

Instances using DHCPv4 will be allocated an IPv4 address, and a DNS record will be created for their instance name. This prevents instances from being able to spoof DNS records by providing false host name information in the DHCP request.

The [`dnsmasq`] service also provides IPv6 router advertisement capabilities. This means that instances will auto-configure their own IPv6 address using SLAAC, so no allocation is made by [`dnsmasq`]. However, instances that are also using DHCPv4 will also get an AAAA DNS record created for the equivalent SLAAC IPv6 address. This assumes that the instances are not using any IPv6 privacy extensions when generating IPv6 addresses.

In this default configuration, whilst DNS names cannot not be spoofed, the instance is connected to an Ethernet bridge and can transmit any layer 2 traffic that it wishes, which means an instance that is not trusted can effectively do MAC or IP spoofing on the bridge.

In the default configuration, it is also possible for instances connected to the bridge to modify the LXD host's IPv6 routing table by sending (potentially malicious) IPv6 router advertisements to the bridge. This is because the [`lxdbr0`] interface is created with [`/proc/sys/net/ipv6/conf/lxdbr0/accept_ra`] set to [`2`], meaning that the LXD host will accept router advertisements even though [`forwarding`] is enabled (see [[`/proc/sys/net/ipv4/*`] Variables](https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt) for more information).

However, LXD offers several bridged NIC security features that can be used to control the type of traffic that an instance is allowed to send onto the network. These NIC settings should be added to the profile that the instance is using, or they can be added to individual instances, as shown below.

The following security features are available for bridged NICs:

  Key                                                                  Type   Default                                            Required   Description
  -------------------------------------------------------------------- ------ -------------------------------------------------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`security.mac_filtering`]    bool   [`false`]   no         Prevent the instance from spoofing another instance's MAC address
  [`security.ipv4_filtering`]   bool   [`false`]   no         Prevent the instance from spoofing another instance's IPv4 address (enables [`mac_filtering`])
  [`security.ipv6_filtering`]   bool   [`false`]   no         Prevent the instance from spoofing another instance's IPv6 address (enables [`mac_filtering`])

One can override the default bridged NIC settings from the profile on a per-instance basis using:

    lxc config device override <instance> <NIC> security.mac_filtering=true

Used together, these features can prevent an instance connected to a bridge from spoofing MAC and IP addresses. These options are implemented using either [`xtables`] ([`iptables`], [`ip6tables`] and [`ebtables`]) or [`nftables`], depending on what is available on the host.

It's worth noting that those options effectively prevent nested containers from using the parent network with a different MAC address (i.e using bridged or [`macvlan`] NICs).

The IP filtering features block ARP and NDP advertisements that contain a spoofed IP, as well as blocking any packets that contain a spoofed source address.

If [`security.ipv4_filtering`] or [`security.ipv6_filtering`] is enabled and the instance cannot be allocated an IP address (because [`ipvX.address=none`] or there is no DHCP service enabled on the bridge), then all IP traffic for that protocol is blocked from the instance.

When [`security.ipv6_filtering`] is enabled, IPv6 router advertisements are blocked from the instance.

When [`security.ipv4_filtering`] or [`security.ipv6_filtering`] is enabled, any Ethernet frames that are not ARP, IPv4 or IPv6 are dropped. This prevents stacked VLAN Q-in-Q (802.1ad) frames from bypassing the IP filtering.

### Routed NIC security[¶](#routed-nic-security "Link to this heading")

An alternative networking mode is available called "routed". It provides a virtual Ethernet device pair between container and host. In this networking mode, the LXD host functions as a router, and static routes are added to the host directing traffic for the container's IPs towards the container's [`veth`] interface.

By default, the [`veth`] interface created on the host has its [`accept_ra`] setting disabled to prevent router advertisements from the container modifying the IPv6 routing table on the LXD host. In addition to that, the [`rp_filter`] on the host is set to [`1`] to prevent source address spoofing for IPs that the host does not know the container has.

## Related topics[¶](#related-topics "Link to this heading")

How-to guides:

-   [[How to harden security for LXD]](../../howto/security_harden/#howto-security-harden)

-   [[How to expose LXD to the network]](../../howto/server_expose/#server-expose)

Explanation:

-   [[Remote API authentication]](../../authentication/#authentication)