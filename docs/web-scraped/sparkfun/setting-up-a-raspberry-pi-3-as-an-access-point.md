# Source: https://learn.sparkfun.com/tutorials/setting-up-a-raspberry-pi-3-as-an-access-point

## Introduction

**Note:** This tutorial was based on instructions found on [this blog](https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd/).

The [Raspberry Pi 3](https://www.sparkfun.com/products/14643) comes with a built-in wireless adapter, which makes it easy to configure it as a WiFi hotspot to share Internet or host your own internal web site. The first part of this guide will show you how to set up the Pi to broadcast its SSID, accept WiFi connections, and hand out IP addresses (using DHCP). The next section shows you how to enable a pass-through Ethernet connection should you want to share your Internet connection.

[![Raspberry Pi 3 B+](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/2/8/14643-Raspberry_Pi_3_B_-02.jpg)](https://www.sparkfun.com/raspberry-pi-3-b.html)

### [Raspberry Pi 3 B+](https://www.sparkfun.com/raspberry-pi-3-b.html) 

[ DEV-14643 ]

The Raspberry Pi 3 B+ is here to provide you with the same Pi as before, but now with gigabit and PoE capable Ethernet!

[ [\$43.50] ]

### Before You Get Started!

You will want a [Raspberry PI 3](https://www.sparkfun.com/products/14643) or [Raspberry Pi Zero W](https://www.sparkfun.com/products/14277) along with any hookup accessories you might need (for example, [a power adapter](https://www.sparkfun.com/products/13831) and [micro SD card](https://www.sparkfun.com/products/13833)).

You will want to load an operating system (OS) onto the SD card and be able to log into the Pi and open a terminal.

**Note:** This tutorial was created with Raspbian Stretch (version: March 2018). Using a different version may require performing different steps than what\'s shown in this tutorial. If you would like to download the March 2018 version of Raspbian, it can be found below.\
\

[Raspbian Stretch (version: March 2018) Download (ZIP)](http://downloads.raspberrypi.org/raspbian/images/raspbian-2018-03-14/2018-03-13-raspbian-stretch.zip)

\

If you need help installing an OS onto the Raspberry Pi, these tutorials can be helpful:

- The [getting an OS part of the Raspberry Pi 3 Starter Kit guide](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide#getting-an-os) walks you through a few options to installing NOOBS on the Pi.
- [Getting Started with the Raspberry Pi Zero Wireless tutorial](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless) is a good place to start if you have a Pi Zero W.
- The [Headless Raspberry Pi Setup guide](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup) is useful if you are looking to configure your Pi without a monitor, keyboard, or mouse (e.g. log in through serial or SSH).

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless)

### Getting Started with the Raspberry Pi Zero Wireless 

Learn how to setup, configure and use the smallest Raspberry Pi yet, the Raspberry Pi Zero - Wireless.

[](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup)

### Headless Raspberry Pi Setup 

Configure a Raspberry Pi without a keyboard, mouse, or monitor.

## Set Up WiFi Access Point

Make sure your Raspberry Pi is connected to the Internet. Open a [terminal window](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) (either in a console window or over a serial/SSH connection).

### Install Packages

To install the required packages, enter the following into the console:

    language:bash
    sudo apt-get -y install hostapd dnsmasq

*Hostapd* is a program that allows you to use the WiFi radio as an access point, and *Dnsmasq* is a lightweight combination of DHCP and DNS services (handing out IP addresses and translating domain names into IP addresses).

### Set Static IP Address

In recent versions of Raspbian, network configuration is managed by the *dhcpcd* program. As a result, we\'ll need to tell it to ignore the wireless interface, *wlan0*, and set a static IP address elsewhere.

**Note:** If you are connected to your Raspberry Pi using SSH over wireless, you will want to connect with a keyboard/mouse/monitor, Ethernet, or serial instead until we get the access point configured.

Edit the *dhcpcd* file:

    language:bash
    sudo nano /etc/dhcpcd.conf

Scroll down, and at the bottom of the file, add:

    language:bash
    denyinterfaces wlan0

Your terminal window should look similar to the image below.

[![Prevent dhcpcd from configuring wlan0](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_01.png)

Save and exit by pressing [ctrl] + [x] and [y] when asked.

Next, we need to tell the Raspberry Pi to set a static IP address for the WiFi interface. Open the *interfaces* file with the following command:

    language:bash
    sudo nano /etc/network/interfaces

At the bottom of that file, add the following:

    language:bash
    auto lo
    iface lo inet loopback

    auto eth0
    iface eth0 inet dhcp

    allow-hotplug wlan0
    iface wlan0 inet static
        address 192.168.5.1
        netmask 255.255.255.0
        network 192.168.5.0
        broadcast 192.168.5.255

Your terminal window should look similar to the image below.

[![Set WiFi static IP address in the Raspberry Pi\'s interfaces file](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_02a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_02a.png)

Save and exit by pressing [ctrl] + [x] and [y] when asked.

### Configure Hostapd

We need to set up *hostapd* to tell it to broadcast a particular SSID and allow WiFi connections on a certain channel. Edit the *hostapd.conf* file (this will create a new file, as one likely does not exist yet) with this command:

    language:bash
    sudo nano /etc/hostapd/hostapd.conf

Enter the following into that file. Feel fee to change the `ssid` (WiFi network name) and the `wpa_passphrase` (password to join the network) to whatever you\'d like. You can also change the `channel` to something in the 1-11 range (if channel 6 is too crowded in your area).

    language:bash
    interface=wlan0
    driver=nl80211
    ssid=MyPiAP
    hw_mode=g
    channel=6
    ieee80211n=1
    wmm_enabled=1
    ht_capab=[HT40][SHORT-GI-20][DSSS_CCK-40]
    macaddr_acl=0
    auth_algs=1
    ignore_broadcast_ssid=0
    wpa=2
    wpa_key_mgmt=WPA-PSK
    wpa_passphrase=raspberry
    rsn_pairwise=CCMP

Your terminal window should look similar to the image below.

[![Configure Hostapd](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_03.png)

Save and exit by pressing [ctrl] + [x] and [y] when asked.

Unfortunately, *hostapd* does not know where to find this configuration file, so we need to provide its location to the *hostapd* startup script. Open */etc/default/hostapd*:

    language:bash
    sudo nano /etc/default/hostapd

Find the line `#DAEMON_CONF=""` and replace it with:

    language:bash
    DAEMON_CONF="/etc/hostapd/hostapd.conf"

Your terminal window should look similar to the image below.

[![Configure Hostapd to load the .conf file on boot](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_04.png)

Save and exit by pressing [ctrl] + [x] and [y] when asked.

### Configure Dnsmasq

*Dnsmasq* will help us automatically assign IP addresses as new devices connect to our network as well as work as a translation between network names and IP addresses. The **.conf** file that comes with *Dnsmasq* has a lot of good information in it, so it might be worthwhile to save it (as a backup) rather than delete it. After saving it, open a new one for editing:

    language:bash
    sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.bak
    sudo nano /etc/dnsmasq.conf

In the blank file, paste in the text below. Note that we set up DHCP to assign addresses to devices between `192.168.5.100` and `192.168.5.200`. Remember that `192.168.5.1` is reserved for the Pi. So, anything between `192.168.5.2 - 192.168.5.9` and between `192.168.5.201 - 192.168.5.254` can be used for devices with static IP addresses.

    language:bash
    interface=wlan0 
    listen-address=192.168.5.1
    bind-interfaces 
    server=8.8.8.8
    domain-needed
    bogus-priv
    dhcp-range=192.168.5.100,192.168.5.200,24h

Your terminal window should look similar to the image below.

[![Set up dnsmasq with DHCP on WiFi](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_05.png)

Save and exit by pressing [ctrl] + [x] and [y] when asked.

### Test WiFi connection

Restart the Raspberry Pi using the following command:

    language:bash
    sudo reboot

After your Pi restarts (no need to log in), you should see **MyPiAP** appear as a potential wireless network from your computer.

[![Raspberry Pi broadcasting its WiFi network](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_06.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_06.png)

Connect to it (the network password is **raspberry**, unless you changed it in the *hostapd.conf* file). Open a terminal on your computer and enter the command `ipconfig` (Windows) or `ifconfig` (Mac, Linux). You should see that you have been assigned an IP address in the `192.168.5.100 - 192.168.5.200` range.

Here\'s an example of what you may see after connecting wirelessly to the Pi.

[![IP address assigned by the DHCP server on the Raspberry Pi](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_07a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_07a.png)

If you just want to use the Pi as a standalone WiFi access point, you can stop here. If you want to connect it to another network (over Ethernet) in order to share Internet (much like a WiFi router), continue on.

## Enable Packet Forwarding

We can use the Raspberry Pi as a router by being able to connect it to another network over Ethernet and have WiFi-connected devices be able to talk to that network. By doing this, we can share an Internet connection from the Pi.

### Configure NAT

Make sure you are logged into your Pi. Edit the */etc/sysctl.conf* file:

    language:bash
    sudo nano /etc/sysctl.conf

Look for the line `#net.ipv4.ip_forward=1`, and uncomment it by deleting the `#`.

    language:bash
    net.ipv4.ip_forward=1

Your terminal window should look similar to the image below.

[![Enable IPv4 packet forwarding](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_08.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_08.png)

Save and exit by pressing [ctrl] + [x] and [y] when prompted.

Finally, we need to configure Network Address Translation (NAT) between the Ethernet and WiFi interfaces to allow devices on both networks to communicate with each other. In the terminal, enter the following:

    language:bash
    sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE  
    sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
    sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

This will work for now, but on reboot, the Pi will revert back to its previous state. To fix this, we need these NAT rules to be applied each time it starts up. Save the current rules to a file with this command:

    language:bash
    sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"

Linux provides us with a number of ways to run commands on boot. Usually, the easiest is to put those commands into the */etc/rc.local* script. To have our NAT rules restored on boot, we edit the *rc.local* file:

    language:bash
    sudo nano /etc/rc.local

Just above the `exit 0` line (which ends the script), add the following:

    language:bash
    iptables-restore < /etc/iptables.ipv4.nat 

Your terminal window should look similar to the image below.

[![Restore NAT rules during boot with rc.local](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_09.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_09.png)

Save and exit by pressing [ctrl] + [x] and [y] when prompted.

### Test It Out

Restart your Pi:

    language:bash
    sudo reboot

Give your Pi a couple minutes to restart (once again, no need to log in). Connect an Ethernet cable from your Internet router (or switch, etc.) to your Pi. Once the Pi has started, connect to the **MyPiAP** network from your computer. Open a web browser, and navigate to the website of your choice.

[![Example of a good website](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_10.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_10.png)

You can also open a terminal on your computer and ping a known Internet address (e.g. `8.8.8.8` is one of Google\'s Public DNS servers).

[![Ping 8.8.8.8 over the Raspberry Pi WiFi network](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_11.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/1/RPi_AP_screenshot_11.png)