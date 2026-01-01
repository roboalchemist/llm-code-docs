## Use a proxy server

A ***proxy server**** acts as an intermediary between a client device and the Internet.
To configure your Raspberry Pi as a proxy server client, follow the instructions in this section.

You will need:

** the IP address or hostname and port of your proxy server
** a username and password for your proxy (if required)

### Configure your Raspberry Pi

You will need to set up three environment variables (`http*proxy`, `https*proxy`, and `no*proxy`) so your Raspberry Pi knows how to access the proxy server.

Open a terminal window, and open the file `/etc/environment` using nano:

```console
$ sudo nano /etc/environment
```

Add the following to the `/etc/environment` file to create the `http*proxy` variable:

```bash
export http*proxy="http://<proxy*ip*address>:<proxy*port>"
```

Replace the `<proxy*ip*address>` and `<proxy*port>` placeholders with the IP address and port of your proxy.

[NOTE]
====
If your proxy requires a username and password, add them using the following format:

```bash
export http*proxy="http://<username>:<password>@proxyipaddress:proxyport"
```

Replace the `<username>` and `<password>` placeholders with the username and password you use to authenticate with your proxy.
====

Enter the same information for the environment variable `https*proxy`:

```bash
export https*proxy="http://username:password@proxyipaddress:proxyport"
```

Create the `no*proxy` environment variable, which is a comma-separated list of addresses your Raspberry Pi should not use the proxy for:

```bash
export no*proxy="localhost, 127.0.0.1"
```

Your `/etc/environment` file should now look like the following:

```bash
export http*proxy="http://username:password@proxyipaddress:proxyport"
export https*proxy="http://username:password@proxyipaddress:proxyport"
export no*proxy="localhost, 127.0.0.1"
```

Press ****Ctrl + X**** to save and exit.

### Update the `sudoers` file

To use the proxy environment variables with operations that run as `sudo`, such as downloading and installing software, update `sudoers`.

Use the following command to open `sudoers`:

```console
$ sudo visudo
```

Add the following line to the file so `sudo` will use the environment variables you just created:

```bash
Defaults	env*keep+="http*proxy https*proxy no_proxy"
```

Press ****Ctrl + X*** to save and exit.

### Reboot your Raspberry Pi

Reboot your Raspberry Pi for the changes to take effect. You should now be able to access the internet via your proxy server.