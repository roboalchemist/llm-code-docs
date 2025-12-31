# Source: https://learn.sparkfun.com/tutorials/sparcade-edison-as-a-web-server-for-browser-games

## Introduction

The [Intel^®^ Edison](https://www.sparkfun.com/products/13024) is essentially a tiny computer with onboard WiFi. As such, we can configure the Edison to act as an access point (AP) and a web server at the same time to serve simple browser-based games.

[![Edison as a game server](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-01.jpg)

At big events like Maker Faires, internet is often nonexistent or hard to come by. One way to serve a web page to attendees is to create a WiFi access point to which they connect. This type of off-grid \"dark node\" is how projects like [LibraryBox](http://librarybox.us/) work.

### Required Materials

Parts for this project can be found in the [Edison SIK](https://www.sparkfun.com/products/13742). Specifically, you will need:

### Suggested Reading

Before continuing with this project, we suggest you be familiar with a few concepts:

- [Edison SIK: Weather on an LCD](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-9-weather-on-an-lcd)
- [Intro to Linux Command Line](http://linuxcommand.org/lc3_learning_the_shell.php)
- [How Do Web Servers Work?](https://aprelium.com/data/doc/2/abyssws-linux-doc-html/howdowswork.html)

## Hardware Hookup

Connect the Edison to a Base Block and GPIO Block. See [this guide](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/building-the-block-stack) on how to connect the Blocks (note that the ADC Block is not needed for this project).

[![Edison with LCD](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/5/Exp_09-LCD_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/5/Exp_09-LCD_bb.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

## Configure the Edison

We need to configure the Edison to act as an access point before we can program it with the server and game.

### Install XDK

Follow [these instructions](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/installing-the-intel-xdk-iot-edition) to install the Intel^®^ XDK.

### Flash the Latest Firmware

Follow the [Edison firmware flashing guide](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/updating-the-edison-firmware) to update to the latest firmware.

### Connect to the Edison

Plug a USB cable into the OTG port of the Edison. Follow [these instructions](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/appendix-c-using-a-usb-network) to set up USB networking on your host computer.

Use an SSH program (e.g., [PuTTY](http://www.putty.org/)) or the built-in SSH terminal of the XDK to connect to the Edison. Note that the default IP address of the Edison on the USB network is 192.168.2.15.

### Configure WiFi

Once logged into the Edison over SSH (username: root, no password), run the command:

    configure_edison --setup

Follow the onscreen instructions to set a password (highly recommended!), change the Edison\'s name (e.g., \"sparcade\"), and connect to the internet via WiFi.

**NOTE**: Remember the device name you set! It should be the same name used for the SSID and hostname in future steps. This is because mDNS uses the hostname for the local network name, and we want it to match with the Dnsmasq name. I use \"sparcade\" for everything.

### Configure Hostapd

[Hostapd](https://wiki.gentoo.org/wiki/Hostapd) is a Linux utility capable of turning WiFi network cards into access points. Luckily, the Edison has Hostapd installed by default. All we have to do is configure it. Back up the original hostapd.conf file, and modify a new one:

    mv /etc/hostapd/hostapd.conf.bak
    vi /etc/hostapd/hostapd.conf

In the vi text editor, press \'i\' to edit text and insert the following (you can copy the text and press \'shift\' + \'insert\' together to paste into vi):

    interface=wlan0
    ssid=sparcade
    hw_mode=g
    channel=6
    auth_algs=1
    wmm_enabled=0

Save and exit by pressing \'esc\', type `:wq`, and press \'enter\'.

### Configure Hosts

The [hosts file](https://en.wikipedia.org/wiki/Hosts_(file)) lets us map names to IP addresses without having to rely on a DNS server. We want to associate the name \"sparcade\" and \"sparcade.local\" with our own IP address, which is 192.168.42.1 by default.

Backup the original hosts file and edit a new one:

    mv /etc/hosts /etc/hosts.bak
    vi /etc/hosts

Add the following:

    127.0.0.1       localhost.localdomain           localhost       sparcade.local  sparcade
    192.168.42.1    sparcade.local                  sparcade

Save and exit.

### Configure DHCP

The Edison uses [udhcp](https://udhcp.busybox.net/) as a lightweight DHCP server for access point (AP) mode. This service hands out IP addresses to clients that connect to its AP. We\'ll want to configure the udhcp daemon so that sparcade.local is associated with the AP\'s IP address (192.168.42.1). It\'s a bit of a cheat, since we aren\'t running a full [DNS server](https://en.wikipedia.org/wiki/Domain_Name_System) to associate website names with IP addresses.

Edit the configuration file:

    vi /etc/hostapd/udhcpd-for-hostapd.conf

Scroll down to the bottom of the file, and add the following:

    opt subnet 255.255.255.0
    opt hostname sparcade
    opt domain local
    opt dns 192.168.42.1

Save and exit.

### Install Dnsmasq

We will also use another tool, [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html), to help associate the server name (\"sparcade.local\") with the Edison\'s WiFi IP Address (192.168.42.1). Install it with the following commands:

    wget http://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.45.tar.gz
    tar xvf dnsmasq-2.45.tar.gz
    cd dnsmasq-2.45
    make install

Configure dnsmasq with:

    vi /etc/dnsmasq.conf

Enter the following:

    no-resolv
    interface=wlan0

Save and exit.

### Set Dnsmasq to Run on Boot

Because we manually compiled and installed dnsmasq, there is nothing that tells it to run whenever the Edison boots. To do that, we need to create a [systemd](https://www.freedesktop.org/wiki/Software/systemd/) service.

    vi /lib/systemd/system/dnsmasq.service

Copy in the following:

    [Unit]
    Description=DHCP and DNS caching server.
    After=network.target

    [Service]
    ExecStart=/usr/local/sbin/dnsmasq -k --conf-file=/etc/dnsmasq.conf
    ExecReload=/bin/kill -HUP $MAINPID
    Restart=on-failure
    RestartSec=5

    [Install]
    WantedBy=multi-user.target

Save and exit. To register the service (so it runs on boot), enter the commands:

    systemctl daemon-reload
    systemctl enable dnsmasq.service

### Disable Default Server

Finally, we want to disable the web server that the Edison runs whenever it enters into AP mode. To do that, run:

    systemctl disable edison_config.service

And now we can restart the Edison:

    reboot

### Set Edison as Access Point

Once the Edison has finished booting back up, turn on AP mode. Do that by holding the PWR button (on the side of the Base Block) for two to seven seconds (I recommend counting to 4).

[![Hold this button for 4 seconds](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-02_annotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-02_annotated.jpg)

## The Code

Download the Sparcade game server code:

[Sparcade code](https://github.com/ShawnHymel/Sparcade/archive/master.zip)

Unzip it and open the project in XDK. Connect to the Edison, upload the code, and run it. If you need a refresher on how to use the XDK, see [this guide](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/using-the-xdk).

[![XDK running Sparcade code](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/5/Sparcade_XDK.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/5/Sparcade_XDK.jpg)

*The XDK showing the Sparcade server running. Click on the image to see a larger version.*

### What\'s Going On?

The code for Sparcade might be confusing at first glance. In main.js, we use the *express* and *http* node modules to create a simple web server. These serve the files found in the *www* directory (our game).

If you open up *www/index.html*, you will see the basic web page that gets sent to any client that requests a page from \"sparcade.local\". This page tells the client\'s browser to download a few JavaScript (.js) files, which then run a [Phaser](http://phaser.io/)-based game on the [Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) element in the page.

Whenever the player dies (loses all lives), the client creates a [socket.io](http://socket.io/) connection back to the server and sends the player\'s score. The server compares the player\'s score against its list of Top 10 high scores, and, if the player ranked, it sends an initials request back to the client.

The player, if ranked in the top scores, enters their initials into the game, and their client sends their initials back to the server. The server then adds the user\'s initials and score to the list of Top 10 scores, which is continuously displayed on the LCD.

## Play!

From your phone, tablet or computer, connect to the **Sparcade** WiFi access point. Note that you will not have internet connection!

[![Connecting to the dark node](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-05.jpg)

Open up a browser and navigate to **http://sparcade.local/**.

**NOTE:** Some browsers require you to type the \"http://\" part or the \"/\" at the end of the address. If your browser is still having trouble getting the web page, try typing in the IP address of the Edison in the browser\'s address bar: **192.168.42.1**.

You should see the game appear in your browser. Vortex is a [Tempest](https://en.wikipedia.org/wiki/Tempest_%28video_game%29) clone. You pilot a ship around a circle and shoot incoming enemies. Prevent any ships from leaving the blue circle, and don\'t get shot!

Vortex is a simple arcade game \-- you have three extra lives, and one shot kills. The purpose is to get the high score.

[![Playing Vortex](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-03.jpg)

As you and other people play the game, scores will be sent back to the server. If you are lucky and skilled enough to be in the Top 10, the game will ask you for your initials. The LCD on the Edison will scroll through the Top 10 high scores of everyone who has played!

[![Vortex with high scores from the Sparcade server](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/5/Sparcade_Tutorial-04.jpg)

*Smaller [jumper wires](https://www.sparkfun.com/products/124) are used here to keep the breadboard looking nice.*