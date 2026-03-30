# Source: https://docs.iredmail.org/iredmail-easy.what.is.ssh.jump.server.html

Title: iRedMail Easy: What is SSH jump server

URL Source: https://docs.iredmail.org/iredmail-easy.what.is.ssh.jump.server.html

Markdown Content:
It's common that you have a protected Linux/BSD server that isn’t publicly accessible. Typically, you may have what is commonly referred to as a _**jump server**_ or _**bastion server**_ which is accessible from a public network (sometimes this jump server would be in a DMZ, and also Linux/BSD), you connect to this jump server first, then connect to the protected server from jump server.

Sample setup:

```
+--------+       +-------------+      +------------------+
| Laptop | <---> | Jump server | <--> | Protected server |
+--------+       +-------------+      +------------------+
```

You can connect to the protected server through jump server via ssh with command like below:

```
ssh -v -J user1@jump-server user2@protected-server
```

References
----------

*   [SSH manual page](https://man.openbsd.org/ssh#J)
