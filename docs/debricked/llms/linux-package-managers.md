# Source: https://docs.debricked.com/overview/language-support/linux-package-managers.md

# Linux package managers

Apart from the various programming package management systems, OpenText Core SCA also supports package managers for various Linux distributions, allowing you to find and monitor potential vulnerabilities of your server or Docker container.

To start tracking your server or Docker vulnerabilities, you should first execute your package manager(s) list command and redirect the output to a text file:

* For Debian, Ubuntu and most derivatives, execute the following command:

```
apt list --installed > apt.list
```

* For Alpine Linux which is widely used by Docker containers, execute the following command:

```
apk list --installed > apk.list
```

To scan them for dependencies, the output file(s) should be either committed to the repository or manually uploaded.
