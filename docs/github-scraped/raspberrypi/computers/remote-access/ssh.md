[[ssh]]
## Access a remote terminal with SSH

You can access the terminal of a Raspberry Pi remotely from another computer on the same network using the ***S****ecure ****SH****ell (SSH) protocol.

### Enable the SSH server

By default, Raspberry Pi OS disables the SSH server. Enable SSH in one of the following ways:

[tabs]
======
On the desktop: +
1. From the **Preferences** menu, launch **Control Centre**.
1. Navigate to the **Interfaces** tab.
1. Select **Enabled** next to **SSH**.
1. Click **OK**.

While flashing a fresh OS image: +
To configure SSH on a completely new installation of Raspberry Pi OS:
+
1. Follow the instructions in the xref:../computers/getting-started.adoc#raspberry-pi-imager[Install with Imager] guide.
1. In the ****Customisation > Remote Access**** tab, toggle the ****Enable SSH**** switch to the active position.
1. Select ****Use password authentication**** to log in using the same username and password you use while physically using your Raspberry Pi. Select ****Use public key authentication**** to xref:remote-access.adoc#configure-ssh-without-a-password[configure an SSH key] for login with SSH key-based authentication.

From the terminal: +
1. Enter `sudo raspi-config` in a terminal window.
1. Select `Interfacing Options`.
1. Navigate to and select `SSH`.
1. Choose `Yes`.
1. Select `Ok`.
1. Choose `Finish`.

Manually: +
1. Create an empty file named `ssh` in the boot partition:
+
```console
$ sudo touch /boot/firmware/ssh
```
1. Reboot the machine:
+
```console
$ sudo reboot
```
======

### Connect to an SSH server

Open a terminal window on your computer and enter the following command, replacing the `<ip address>` placeholder with the xref:remote-access.adoc#ip-address[IP address of the Raspberry Pi you're trying to connect to] and `<username>` with your username:

```console
$ ssh <username>@<ip address>
```

When the connection works, you will see a security warning. Type `yes` to continue. You will only see this warning the first time you connect.

Enter your account password when prompted.

You should now see the Raspberry Pi command prompt:

```console?prompt=<username>@<hostname> ~ $
<username>@<hostname> ~ $
```

You are now connected to the Raspberry Pi remotely, and can execute commands.

NOTE: If you receive a `connection timed out` error, you may have entered the wrong IP address for the Raspberry Pi. Check the xref:remote-access.adoc#ip-address[IP address of the Raspberry Pi].

#### Forward X11 over SSH

NOTE: On macOS and Windows, you must install a third-party X server to use X11 forwarding.

X11 enables graphical applications over SSH. Pass the `-Y` flag to forward an X session over SSH:

```console
$ ssh -Y <username>@<ip address>
```

Once authenticated, you will see the command line as usual. However, you can also open graphical windows that an X server can render for you. For example, type the following command to launch a https://www.geany.org/[Geany] window:

```console
$ geany &
```

### Configure SSH without a password

To remotely access your Raspberry Pi without providing a password each time you connect, use an SSH keypair.

#### Preconfigure an OS image with Raspberry Pi Imager

When configuring an operating system image with Raspberry Pi Imager, you can preconfigure SSH keys to use an existing key on the computer where you run Imager.

1. Follow the xref:getting-started.adoc#raspberry-pi-imager[install using Imager] guide to configure your boot image.
1. On the ****Remote Access**** tab, toggle the **Enable SSH** switch to the active position.
1. Select **Use public key authentication**.
** If you already have an SSH public key stored in `~/.ssh/id*rsa.pub`, Imager automatically uses that public key to prefill the text box.
** Otherwise, browse to the location of your public key.
1. Select ****Next**** to proceed with the imaging process.

#### Manually configure an SSH key

If you already have an installation of Raspberry Pi OS, you can update your existing configuration to use SSH key authentication.

#### Check for existing SSH public keys

To check for an existing SSH public key on the computer you use to remotely connect to the Raspberry Pi, run the following command:

```console
$ ls ~/.ssh
```

If you see files named `id*ed25519.pub`, `id*rsa.pub`, or `id*dsa.pub`, you already have an SSH key. Skip SSH keypair generation and proceed to xref:remote-access.adoc#add-ssh-key-identity[add the SSH key to your list of SSH identities].

#### Generate new SSH keypair

TIP: This guide provides instructions to generate a new RSA key. For additional security, you can instead generate a http://ed25519.cr.yp.to/[Ed25519] key. Pass `-t ed25519` to `ssh-keygen` and replace `rsa` with `ed25519` when referencing your public and private key file names to use an Ed25519 key.

To generate a new SSH keypair, enter the following command:

```console
$ ssh-keygen
```

When asked where to save the key, press **Enter** to use the default location, `~/.ssh/id*rsa`.

When asked for an optional keyphrase, press **Enter* to use no keyphrase.

Run the following command to check the contents of the `.ssh` directory:

```console
$ ls ~/.ssh
```

You should see the files `id*rsa` and `id*rsa.pub`:

```
authorized*keys  id*rsa  id*rsa.pub  known*hosts
```

The `id*rsa` file contains your private key. Keep this secure on the computer you use to remotely connect to the Raspberry Pi.

The `id*rsa.pub` file contains your public key. You will share this key with your Raspberry Pi. When you connect with the Raspberry Pi remotely, it will use this key to verify your identity.

[[add-ssh-key-identity]]
#### Add the SSH key to your list of SSH identities

Start the SSH agent:

```console
$ eval "$(ssh-agent -s)"
```

Next, add your key identities to `ssh-agent` with the following command:

```console
$ ssh-add ~/.ssh/id*rsa
```

[[copy-your-public-key-to-your-raspberry-pi]]
#### Copy a public key to your Raspberry Pi

On the computer you use to remotely connect to the Raspberry Pi, use the following command to securely copy your public key to the Raspberry Pi:

```console
$ ssh-copy-id <username>@<ip address>
```

When prompted, enter the password for your user account on the Raspberry Pi.
You can now connect to your Raspberry Pi without entering a password.

#### Manually copy a public key to your Raspberry Pi

If your operating system does not support `ssh-copy-id`, you can instead copy your public key with xref:remote-access.adoc#scp[`scp`].

First, *on your Raspberry Pi*, create the directory where Linux expects to find keys:

```console
$ mkdir .ssh
```

Then, configure the proper permissions for the `.ssh` directory:

```console
$ chmod 700 .ssh
```

*On your usual computer*, use `scp` to copy your public key to a file named `.ssh/authorized*keys` on your Raspberry Pi:

```console
$ scp .ssh/id*rsa.pub <username>@<ip address>:.ssh/authorized*keys
```

TIP: The command above assumes you have never before authorized any keys to access your Raspberry Pi. If you have previously added at least one key, you should instead add a new line containing the public key to the end of the `authorized*keys` file to preserve your existing keys.

When prompted, enter the password for your user account on the Raspberry Pi.

Then, *on your Raspberry Pi*, configure permissions for the `authorized*keys` file:

```console
$ chmod 644 .ssh/authorized*keys
```

You can now connect to your Raspberry Pi without entering a password.