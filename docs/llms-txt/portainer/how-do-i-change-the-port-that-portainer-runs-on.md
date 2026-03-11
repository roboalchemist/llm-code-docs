# Source: https://docs.portainer.io/2.33-lts/faqs/installing/how-do-i-change-the-port-that-portainer-runs-on.md

# Source: https://docs.portainer.io/sts/faqs/installing/how-do-i-change-the-port-that-portainer-runs-on.md

# Source: https://docs.portainer.io/faqs/installing/how-do-i-change-the-port-that-portainer-runs-on.md

# How do I change the port that Portainer runs on?

By default, Portainer runs on port 9443. To change the port, edit the `-p` parameter of your docker run command to suit. For example, if you wanted Portainer to listen on port 443:

```
-p 443:9443
```
