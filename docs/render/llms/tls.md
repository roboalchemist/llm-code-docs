# Source: https://render.com/docs/tls.md

# Fully Managed TLS Certificates

All applications and static sites hosted on Render come with *fully managed and free TLS* certificates. There is no setup and you don't need to do anything at all; everything just works out of the box.

Render uses Let's Encrypt and Google Trust Services to issue certificates for your custom domain and *automatically renews* them before their expiration date.

You get free TLS certificates for the `onrender.com` subdomain for your service, as well as the [custom domains](custom-domains) you add to it, including *wildcard domains*.

Finally, Render automatically redirects all `HTTP` requests to `HTTPS` so your users' security is never compromised.