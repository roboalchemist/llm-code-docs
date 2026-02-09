# Tailscale Quickstart Guide

**Source:** https://tailscale.com/kb/1017/install

---

## Setting Up Your Tailnet

### Create a Tailnet

1. Visit tailscale.com and select **Get Started**, or download the client and sign up via login.tailscale.com
2. Authenticate using a supported SSO identity provider
3. Choose between **Business use** or **Personal use**
4. Install the client on your first device using your credentials
5. Add a second device by selecting its OS and sharing the installation link
6. Access the admin console to manage your network

**Plan Details:** Custom domain signups qualify for a 14-day Enterprise trial. Public email addresses like @gmail.com enroll in the free Personal plan, which includes three users and most Enterprise features.

### Device Management

Devices receive automatically generated names based on their OS hostname. You can rename them through the **Machines** page for better organization. MagicDNS is enabled by default, allowing you to "communicate with devices across your tailnet easier" using device names instead of IP addresses.

### Adding Users

**Team members** with matching custom domain emails can log in automatically. **External users** receive email invites or shareable links, then authenticate via SSO providers.

## Advanced Features

- **Exit Nodes:** Route traffic through designated tailnet devices for privacy
- **Subnet Routers:** Access devices without Tailscale clients installed (like printers)
- **Access Control:** Define custom permissions using ACLs and grants
- **Monitoring:** Track network traffic, client activity, and SSH sessions

## Use Case Examples

- Developers can deploy Kubernetes/Docker, use Tailscale Serve/Funnel, and share prototypes
- IT admins can manage SSH, integrate cloud platforms, and automate via API
- Personal users can stream media, implement ad blocking, and play Minecraft privately

## Support Resources

Visit tailscale.com/contact/support for troubleshooting guides, production best practices, security hardening, and firewall integration assistance.
