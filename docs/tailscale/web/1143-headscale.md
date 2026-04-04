# Access Azure Windows VMs Privately Using Tailscale

**Source:** https://tailscale.com/kb/1143/headscale

---

## Overview

This guide demonstrates how to securely connect Windows virtual machines running on Microsoft Azure to a Tailscale network for private access and connectivity.

## Prerequisites

You'll need an active Tailscale network with at least one device already configured. Reference the official getting started materials if you're new to Tailscale setup.

## Setup Steps

### Step 1: Configure the Windows VM

Create a Windows Datacenter Edition virtual machine in Azure. During the networking configuration phase:

- Select **Advanced** for the network security group
- Create a policy permitting UDP port 41641 ingress to enable direct connections and reduce latency
- Consider temporarily allowing RDP and SSH for initial setup

Download the Windows installer and either:
- Use browser-based login (if the system has GUI access), or
- Execute the CLI command via `cmd.exe` with an authentication key, specifying `--accept-dns=false` to preserve Azure's DNS configuration

### Step 2: Configure Route Advertisement

From `cmd.exe`, advertise both your subnet and Azure's DNS server:

```shell
tailscale set --advertise-routes=10.1.0.0/24,168.63.129.16/32 --accept-dns=false
```

(Replace the subnet address with your actual range)

### Step 3: Set Up Split DNS

In the admin console's DNS section, add the Azure DNS server as a resolver "restricted to the `internal.cloudapp.net` domain" to make internal hostnames accessible across your Tailscale network.

### Step 4: Remove Public Access

Once connected through Tailscale, delete the public SSH ingress rule from your network security settings.

## Advanced: 4via6 Subnet Routers

For networks with overlapping IPv4 address ranges, implement 4via6 subnet routing to direct traffic appropriately.
