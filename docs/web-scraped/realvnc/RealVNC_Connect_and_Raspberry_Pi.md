# Source: https://help.realvnc.com/hc/en-us/articles/360002249917-RealVNC-Connect-and-Raspberry-Pi

# RealVNC Connect and Raspberry Pi 

[Follow](/hc/en-us/articles/360002249917-RealVNC-Connect-and-Raspberry-Pi/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360022267298/MicrosoftTeams-image__3_.png)

**[Tegan](/hc/en-us/profiles/366602748777-Tegan)**

Updated February 27, 2024 20:56

#### Running Pi OS Bookworm? 

Please see our guide: [Raspberry Pi 5, Bookworm and RealVNC Connect](https://help.realvnc.com/hc/en-us/articles/14110635000221-Raspberry-Pi-5-Bookworm-and-RealVNC-Connect)

RealVNC Server is included with Raspberry Pi OS (formerly Raspbian). It's completely free for non-commercial use; it just needs to be enabled.

You'll also need a [RealVNC Viewer application](https://www.realvnc.com/connect/download/viewer/) for the Windows, Mac or Linux computer, or iOS or Android mobile device you want to control your Pi from.

![raspberry-pi-connect.png](/hc/article_attachments/4414330996113)

[]

# Setting up your Raspberry Pi 

RealVNC Server is included with Raspberry Pi OS (formerly Raspbian) but you still have to enable it.

<div>

First, run the following commands to make sure you have the latest version:

</div>

[`sudo`]` `[`apt-get`]` `[`update`] \
[`sudo`]` `[`apt-get`]` `[`install`]` `[`realvnc-vnc-server`] 

If you're already using an older version of RealVNC Server, restart it:

[`sudo`]` `[`systemctl restart vncserver-x11-serviced`] 

If not, and you're already booted into the graphical desktop, select **Menu \> Preferences \> Raspberry Pi Configuration \> Interfaces** and make sure **VNC** is set to **Enabled**.

Alternatively, run the command [`sudo`]` `[`raspi-config`], navigate to **Interface Options \> VNC** and select **Yes**.

From now on, RealVNC Server will start automatically every time you boot your Raspberry Pi. 

By default, RealVNC Server remotes the graphical desktop running on your Raspberry Pi. However, if your Pi is headless (not plugged into a monitor) or not running a graphical desktop, RealVNC Server can still give you graphical remote access using a virtual desktop.

You can also install RealVNC Viewer on your Raspberry Pi, in case you want to control a remote computer (or another Raspberry Pi!). To do this, use the Recommended Software program, or run the command:

[`sudo`]` `[`apt-get`]` `[`install`]` `[`realvnc-vnc-viewer`]

[]

# Getting connected to your Raspberry Pi 

There are two ways to connect; cloud and direct. You can use either or both to access your Raspberry Pi.

To get connected, please make sure you've downloaded [the RealVNC Viewer app](https://www.realvnc.com/connect/download/viewer/) to computers or devices you want to control from.

[]

## Establishing a direct connection 

Direct connections are quick and simple providing you're joined to the same private local network as your Raspberry Pi (for example, a wired or Wi-Fi network at home, school or in the office).

If you're connecting over the Internet, it's much safer and more convenient to establish a cloud connection.

1.  On your Raspberry Pi, discover its private IP address by double-clicking the RealVNC Server icon on the taskbar and examining the status dialog:\
    \
    ![RealVNC_Server_Pi.png](/hc/article_attachments/13664641582493)\
    \

2.  On the device you will use to take control, run RealVNC Viewer and enter the IP address in the search bar:\
    \
    ![](/hc/article_attachments/12341439223325)

[]

## Establishing a cloud connection 

Cloud connections are convenient and encrypted end-to-end, and highly recommended for connections over the Internet. There's no firewall or router reconfiguration, and you don't need to know the IP address of your Raspberry Pi.

You'll need a RealVNC account; it's completely free to set up and only takes a few seconds. You can activate a free 14 day trial, or if using RealVNC Connect for personal, non-commercial reasons you can activate a Lite subscription. On Raspberry Pi, the Lite subscription has additional features that include both cloud and direct connectivity, system authentication, file transfer, printing and chat.

You can apply your Lite subscription to three Raspberry Pis and/or desktop computers in total. Please note you revert to the [standard Lite feature set](https://www.realvnc.com/en/connect/plan/lite/) for Windows, macOS and Linux desktop computers.

1.  Sign up for a RealVNC account by entering your email address in [the box on this page](https://manage.realvnc.com/en/auth/sign_up), and following the instructions.

2.  On your Raspberry Pi, select **Licensing** from the RealVNC Server status menu, click Next then enter your new RealVNC account\'s email and password and follow the on-screen instructions: \
    \
    ![RealVNC_Server_Pi_Licensing.png](/hc/article_attachments/13664641583645)\
    \

3.  On the device you will use to take control, run RealVNC Viewer and sign in using the same RealVNC account credentials.

4.  In RealVNC Viewer, a connection entry for your Raspberry Pi automatically appears under the name of your team. Simply tap or double-click to connect:\
    \
    ![](/hc/article_attachments/12341372815133)

## Authenticating to RealVNC Server 

To complete a connection you must authenticate to RealVNC Server. Enter the username and password you normally use to *log on* to your user account on the Raspberry Pi.

By default, these credentials are [`pi`] and [`raspberry`], but hopefully you'll have changed them to something more secure by now!

[]

# Transferring files to and from your Raspberry Pi 

You can transfer files to and from your Raspberry Pi providing you're connecting from RealVNC Viewer running on a Windows, macOS or Linux desktop computer.

-   To transfer files *to* your Raspberry Pi, click the RealVNC Viewer ![VNC_Viewer_Toolbar_File_Transfer_Small.png](/hc/article_attachments/4414337360529) toolbar button and follow the instructions. Detailed steps are [here](https://help.realvnc.com/hc/en-us/articles/360002250477).
-   To transfer files *from* your Raspberry Pi, use RealVNC Viewer to open the RealVNC Server dialog remotely, select **Menu \> File transfer**, and follow the instructions. Detailed steps are [here](https://help.realvnc.com/hc/en-us/articles/360002250477).

# Printing to a local printer 

It can be really useful to print to a printer attached to your Windows, macOS or Linux computer if no printer is set up for your Raspberry Pi. To do this, first run the following command on your Raspberry Pi to install [`cups`] (the Common Unix Printing System):

[`sudo`]` `[`apt-get`]` `[`install`]` `[`cups`]

Then, connect to your Pi using RealVNC Viewer and perform whatever the standard operation is for printing the file you want to print (for example, select a text editor's **File \> Print** menu option). RealVNC Server directs the output to RealVNC Viewer, and prints it to your local printer. There's more information about remote printing [here](https://help.realvnc.com/hc/en-us/articles/360002250537).

[]

# Creating and remoting a virtual desktop 

If your Raspberry Pi is headless (that is, not plugged into a monitor) or embedded in a robot, it's unlikely to be running a graphical desktop.

RealVNC Server can run in Virtual Mode to create a resource-efficient *virtual desktop* on demand, giving you graphical remote access even when there is no actual desktop to remote. This virtual desktop exists only in your Raspberry Pi's memory:

![raspberry-pi-virtual.png](/hc/article_attachments/4414323679249)

To do this:

1.  On your Raspberry Pi, run the command [`vncserver-virtual`]\
    Make a note of the IP address/display number printed to the console, for example [`192.167.5.149:1`]
2.  On the device you will use to take control, enter this information in RealVNC Viewer.

## Stopping a virtual desktop 

A virtual desktop persists until you explicitly destroy it. Run the following command when you are sure it is no longer needed:

[`vncserver-virtual`]` `[`-kill`]` `[`:<display-number>`]

Note this command will terminate any current connections without warning to those users.

[]

# Operating RealVNC Server at the command line 

You can operate RealVNC Server exclusively at the command line or via SSH if you prefer.

Common commands for Raspberry Pi OS (formerly Raspbian) are:

-   To start RealVNC Server now: [`sudo`]` `[`systemctl`]` `[`start`]` `[`vncserver-x11-serviced`]
-   To start RealVNC Server at next boot, and every subsequent boot: [`sudo`]` `[`systemctl`]` `[`enable`]` `[`vncserver-x11-serviced`]
-   To stop RealVNC Server: [`sudo`]` `[`systemctl`]` `[`stop`]` `[`vncserver-x11-serviced`]
-   To prevent RealVNC Server starting at boot: [`sudo`]` `[`systemctl`]` `[`disable`]` `[`vncserver-x11-serviced`]

[]

# Troubleshooting RealVNC Server 

## Changing the Raspberry Pi's screen resolution 

You may want to do this if:

-   Performance is impaired. A smaller screen resolution gives a more responsive experience.
-   Your Raspberry Pi is headless (that is, not plugged into a monitor) and the default initial screen resolution is too small.

To change the resolution, run the command [`sudo`]` `[`raspi-config`], navigate to **Display Options \> VNC Resolution**, and choose an option.

If this menu is not available, or you want more control, specify settings in the [`/boot/config.txt`] file:

  ----------------------------------------------------------------------------------------------------
  Setting                        Value                    Explanation
  ------------------------------ ------------------------ --------------------------------------------
  [`hdmi_force_hotplug`]   [`1`]              Tells your Pi an HDMI display is attached.

  [`hdmi_ignore_edid`]     [`0xa5000080`]     Ignores EDID/display data.

  [`hdmi_group`]           [`2`]              Defines the HDMI output group.

  [`hdmi_mode`]            [`16`]             Forces (for example) 1024x768 at 60Hz.

  [`dtoverlay`\                  [`vc4-fkms-v3d`]   Uses the Fake KMS (FKMS) driver
  ]                                                 
  ----------------------------------------------------------------------------------------------------

See the [Raspberry Pi documentation](https://www.raspberrypi.org/documentation/configuration/config-txt/README.md) for more [`hdmi_mode`] options, and information on [`/boot/config.txt`] in general. You will need to reboot your Raspberry Pi for any changes to take effect.

Note that settings you specify in this file override monitors you subsequently plug in (unless you revert [`hdmi_force_hotplug`]), so pick a resolution compatible with your regular monitor.

## Specifying a screen resolution for a virtual desktop 

If you run RealVNC Server in Virtual Mode to create a virtual desktop, you can specify the screen resolution (geometry) at start up, for example:

[`vncserver-virtual`]` `[`-RandR=800x600`]

You can even specify multiple screen resolutions and cycle between them.

## Optimizing for Raspberry Pi Zero and Pi 1 

If performance is impaired for direct connections to a Raspberry Pi Zero or Pi 1, try turning off encryption if you are sure your private local network is secure. This reduces CPU usage.

You cannot turn off encryption for cloud connections.

1.  On your Raspberry Pi, open the RealVNC Server dialog and select **Menu \> Options \> Expert**.
2.  Change the [`Encryption`] parameter to [`AlwaysOff`].
3.  Restart any existing connections.

If performance is still impaired, try reducing your Raspberry Pi's screen resolution.