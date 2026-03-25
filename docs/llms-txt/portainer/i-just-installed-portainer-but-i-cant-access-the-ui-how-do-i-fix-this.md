# Source: https://docs.portainer.io/2.33-lts/faqs/installing/i-just-installed-portainer-but-i-cant-access-the-ui-how-do-i-fix-this.md

# Source: https://docs.portainer.io/sts/faqs/installing/i-just-installed-portainer-but-i-cant-access-the-ui-how-do-i-fix-this.md

# Source: https://docs.portainer.io/faqs/installing/i-just-installed-portainer-but-i-cant-access-the-ui-how-do-i-fix-this.md

# I just installed Portainer but I can't access the UI, how do I fix this?

As a security precaution, when Portainer is first installed it will wait for 5 minutes for an administrator user to be created (part of the initial setup). If a user is not created within those 5 minutes, the Portainer Server will stop listening for requests.

To resolve this, you will need to manually stop and restart the Portainer container.
