# Source: https://docs.verda.com/cpu-and-gpu-instances/remote-desktop-access.md

# Remote desktop access

Sometimes it is useful to manage the CPU and GPU instances from a visual desktop interface.

Follow these steps to set up a remote desktop environment with VNC server using [TigerVNC](https://tigervnc.org/) on Linux systems like Ubuntu 24.04. This setup allows you to remotely access a lightweight graphical desktop on Verda virtual machine instances.

## Connect to your instance using SSH

```bash
ssh user@INSTANCE_IP_ADDRESS
```

### Update The System

Follow the instructions on [Securing Your Instance](https://docs.verda.com/cpu-and-gpu-instances/securing-your-instance) if you have not done that before

```bash
apt update
apt upgrade
```

#### Install XFCE Desktop Environment and tigerVNC server

```bash
apt install xfce4 xfce4-goodies tigervnc-standalone-server tigervnc-common
```

#### Remove nvidia drivers and reboot <mark style="color:red;">if</mark> using CPU only node

```bash
# Do only if using CPU node
apt remove *nvidia*
reboot
```

#### Start the VNC server

```bash
tigervncserver -xstartup /usr/bin/startxfce4
```

Now your instance has a VNC server running and is ready for the VNC connection. Next commands are run on the machine that you want to use for viewing and controlling the desktop.

#### Create an SSH tunnel to secure the VNC connetion

Run this command on the machine that you will use to connect to your instance. If you want to keep the SSH tunnel connection in the background, you can use `screen` or `tmux` commands.

```bash
ssh -L 5901:localhost:5901 username@REMOTE_IP
```

#### Connect Using a VNC Client

Use any VNC viewer (e.g., TigerVNC Viewer, RealVNC, or Remmina) and connect to localhost:5901.

#### Tips

* You can change the vnc ports and make multiple connections, they will get assigned different ports 5901, 5902 etc..
* You can also use other compatible Linux desktop environments like Ubuntu Desktop (Gnome), KDE Plasma on the instances. [XFCE Desktop](https://www.xfce.org/) is recommended for most users since it is lightweight and simple to use without much configuration and works with default Verda OS images.
