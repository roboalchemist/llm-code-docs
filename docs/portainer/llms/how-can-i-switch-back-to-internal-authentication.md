# Source: https://docs.portainer.io/2.33-lts/faqs/troubleshooting/access-and-authentication/how-can-i-switch-back-to-internal-authentication.md

# Source: https://docs.portainer.io/sts/faqs/troubleshooting/access-and-authentication/how-can-i-switch-back-to-internal-authentication.md

# Source: https://docs.portainer.io/faqs/troubleshooting/access-and-authentication/how-can-i-switch-back-to-internal-authentication.md

# How can I switch back to internal authentication?

If you are able to log into Portainer as an administrator you can change your authentication method under Settings, [Authentication](https://docs.portainer.io/admin/settings/authentication) and selecting Internal.

If you are unable to log into Portainer (for example if you have been locked out due to a external authentication / SSO misconfiguration) you can force using internal authentication by going to:

```
https://localhost:9443/#!/internal-auth
```

Replace <https://localhost:9443> with the URL and port of your Portainer server. You can then log in as the initial administrator user you first set up when installing Portainer.

If you don't have the password for the initial administrator user, you can use our [password reset helper.](https://docs.portainer.io/advanced/reset-admin)
