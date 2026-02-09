# Installation on Windows

**Source:** https://tailscale.com/kb/1018/install-windows

---

Docs›How-to Guides›Manage Access›Manage access control›Manage ACLsManage permissions using ACLsTailscale now secures access to resources using grants, a next-generation access control policy syntax. Grants provide all original ACL functionality plus additional capabilities.ACLs will continue to work indefinitely; Tailscale will not remove support for this first-generation syntax from the product. However, Tailscale recommends migrating to grants and using grants for all new tailnet policy file configurations because ACLs will not receive any new features.
ACLs are available on all plans, but certain functionality might be restricted on some plans.
Tailscale's access control methodology follows the least privilege and zero trust principles. There are two ways to define access controls for your tailnet: access control lists (ACLs) and grants. Both methods follow a deny-by-default principle and are defined in the tailnet policy file using a declarative huJSON syntax.
ACLs represent the traditional network layer approach to managing access within your tailnet, where you define a set of devices or users who can access ports on other devices. Each ACL you create must define a source and a destination. They let you precisely define access controls for users and devices on your Tailscale network (known as a tailnet).
{
"acls": [
{
"action": "accept",
"src": [  ], // These sources (devices or users)
"dst": [ : ], // can access these destination devices on their defined ports
}
]
}
You can use the visual policy editor to manage your tailnet policy file. Refer to the visual editor reference for guidance on using the visual editor.
When you first create your tailnet, the default tailnet policy file enables communication between all devices within the tailnet. You can modify your policy file (including editing ACLs) to fit your needs.
ACLs are deny-by-default, directional, locally enforced, and don't affect local network traffic.
Deny-by-default. Using a default deny policy prevents communication between devices without explicit access to each other. However, in the absence of an acls section in the tailnet policy file, Tailscale applies the default allow all policy.
Directional. Allowing a source to connect to a destination doesn't mean the destination can connect to the source (unless a policy explicitly enables it).
Locally enforced. A device enforces incoming connections based on the access rules distributed to all devices in your tailnet. Rule enforcement happens on each device directly, without further involvement from Tailscale's coordination server.
ACLs do not affect what a device can or cannot access on its local network.
For more information about Tailscale's approach to access control, refer to RBAC like it was meant to be.
If you don't define any access control policies, Tailscale applies the default allow all ACL policy. To deny all traffic, use an empty object for the acls section in your tailnet policy file.
Edit ACLs
You can edit your tailnet's access rules by using the Access controls page of the admin console, GitOps for Tailscale ACLs, or the Tailscale API. Refer to Editing ACLs for more information.
Refer to tailnet policy file syntax to learn about creating access control policies or the sample ACLs for examples of common policies.
Availability by plan
ACLs are available on all plans, but certain functionality might be restricted on some plans.
AvailabilityOn all plansOn the Personal, Personal Plus, Premium, and Enterprise plansAccess rules for...AnyTailscale IPSubnet CIDR RangeAutogroupsTagsHostsIP setsAnyTailscale IPSubnet CIDR RangeAutogroupsGroupsUsersTagsHostsIP setsAccess rules specifying...PortsProtocolsACL sections for...aclhoststeststagOwnersautoApproversnodeAttrspostures with default device posture attributes onlyipsetsaclgroupshoststeststagOwnersautoApproversssh for Tailscale SSHnodeAttrs for Tailscale Funnelpostures with default, custom, and third-party attributes (Personal, Personal Plus, and Enterprise plans only)ipsets
