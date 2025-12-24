# Source: https://help.realvnc.com/hc/en-us/articles/360002249677-Licensing-RealVNC-Connect

# Licensing RealVNC Connect 

[Follow](/hc/en-us/articles/360002249677-Licensing-RealVNC-Connect/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360022267298/MicrosoftTeams-image__3_.png)

**[Tegan](/hc/en-us/profiles/366602748777-Tegan)**

Updated December 05, 2023 14:22

#### Licensing has changed in VNC 7.x 

[Click here](https://help.realvnc.com/hc/en-us/articles/8881174740637) to learn more

You must license the [RealVNC Server](https://www.realvnc.com/connect/download/vnc) you install on every remote device you want to access, and if your subscription is licensed per-user, [RealVNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) on every device you want to access from.

*[You don't need to license any software if you only use On-Demand Assist. Instead, you simply name technicians online, and licensing is handled automatically for those people from then on.]*[]

# Licensing online using the cloud 

## RealVNC Server 

To license RealVNC Server using the cloud, you can either make a desk-side visit and sign in to RealVNC Server using your RealVNC account credentials, or if your subscription includes mass deployment, deploy a [cloud connectivity token](https://help.realvnc.com/hc/en-us/articles/360005474138).

The Licensing Wizard should appear automatically when RealVNC Server is installed, but if it doesn't you can right-click the RealVNC Server tray icon and select **Licensing**:

![faq-licensing.png](/hc/article_attachments/4412487285009)

Enter the email address and password you used when you signed up for your [RealVNC account](https://manage.realvnc.com/):

![license-wizard-sign-in.png](/hc/article_attachments/4412481331985)

NOTE: If you have multiple subscriptions, you will be asked to choose which subscription (or team) to join your computer to. Please ensure you choose the correct team otherwise you may be unable to access your computer remotely.

## RealVNC Viewer 

RealVNC Viewer only needs to be licensed when connecting to a RealVNC Server using a per user subscription.

To license RealVNC Viewer using the cloud, you must have desk-side access to RealVNC Viewer. To apply our license, click the **Sign In** button and enter your RealVNC account credentials, or if you have enabled [Azure AD SSO](https://help.realvnc.com/hc/en-us/articles/5459490226333), use your Azure AD credentials.

![viewer_signin.png](/hc/article_attachments/8923945895325)

# Licensing with an offline license 

If your subscription includes offline licensing, you can license RealVNC Connect offline by either making a desk-side visit, at the command line, or using policy. You may want to do this if the computers are not currently connected to the Internet, or you prefer to not enable cloud connectivity.

For the steps to obtain and apply an offline license, please see [Applying an offline license to RealVNC Connect](https://help.realvnc.com/hc/en-us/articles/360029797672)

**Note: If you use an offline license only [direct connectivity](https://help.realvnc.com/hc/en-us/articles/360002249797) is enabled.**

# Licensing in bulk or remotely 

If you want to license RealVNC Connect in bulk or remotely, you can either:

-   Deploy a [cloud connectivity token](https://help.realvnc.com/hc/en-us/articles/360005474138) to enable cloud connectivity and/or direct connectivity (RealVNC Server only); or
-   Deploy an [offline license](https://help.realvnc.com/hc/en-us/articles/360029797672) to enable direct connectivity only

The above options require that your subscription includes mass deployment and/or offline licensing.

# Relicensing at renewal time 

For most people, we'll automatically handle relicensing RealVNC Connect on all your remote computers when your subscription renews.

Note, if you have a subscription that includes offline licensing and originally licensed VNC Connect on a computer using your offline license, when you renew you will need to [manually apply](https://help.realvnc.com/hc/en-us/articles/360029797672) the new offline license to that computer.

Providing a computer is connected to the Internet, you can add it to your team and benefit from [automatic relicensing via our cloud service](https://help.realvnc.com/hc/en-us/articles/360022499712), saving you having to apply a new license key manually, while being able to disable cloud connectivity on that computer (RealVNC Server only).