# Source: https://help.realvnc.com/hc/en-us/articles/360002249697-Setting-up-and-Managing-your-RealVNC-Connect-Team

# Setting up and Managing your RealVNC Connect Team 

[Follow](/hc/en-us/articles/360002249697-Setting-up-and-Managing-your-RealVNC-Connect-Team/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360077753378/Jack_Naisbett_Professional_Headshot_for_web_-_Copy.jpg)

**[Jack N RealVNC](/hc/en-us/profiles/364261730191-Jack-N-RealVNC)**

Updated October 31, 2025 10:00

You can manage all your remote computers with [cloud connectivity](https://help.realvnc.com/hc/en-us/articles/360002249737) enabled, and the people permitted to access those computers, online in the [RealVNC Connect Portal](https://manage.realvnc.com/).

We'll automatically create a team for each RealVNC Connect subscription you have. If you have more than one subscription, you'll have more than one team; use the team picker at the bottom left of the portal to switch between them:

![Screenshot 2025-10-15 100051.png](/hc/article_attachments/31426083708189)

These teams are completely separate. When you sign in, please make sure you are working with the right team.

[]

# Changing your team\'s name 

The name of your team can be changed under **Organization \> Team Management** page, if you are the team Owner, Admin or Manager.

 

![Screenshot 2025-10-15 100257.png](/hc/article_attachments/31426083709213)

# Adding a remote computer to your team 

Adding a remote computer to your team means enabling online licensing and cloud connectivity (optional for subscriptions with direct connectivity) for that computer. You can see the computers in your team on the **Computers** page of the RealVNC Connect Portal:\
\

![Screenshot 2025-10-15 102725.png](/hc/article_attachments/31426044487197)\
\
To add a remote computer to your team, simply [download and install RealVNC Server](https://www.realvnc.com/en/connect/download/vnc/). You will be prompted for your RealVNC Account details during installation and these will be used to apply the subscription. For more information on applying your subscription, please see [Licensing RealVNC Connect](/hc/en-us/articles/360002249677).\
\
Please note that you will only be able to license RealVNC Server using the subscription owner\'s RealVNC account details by default, however, you can [promote team members](https://help.realvnc.com/hc/en-us/articles/360002317817-Can-I-promote-people-to-help-administer-my-team) to grant them the ability to license RealVNC Server on the subscription owners behalf.

[]

# Renaming a computer in your team 

You rename a computer as it appears in your Team and RealVNC Viewer on the **Computers** page of the RealVNC Connect Portal. To rename a computer, click the blue pencil next to the computer, enter the name and then click the blue tick:

![Screenshot 2025-10-15 103352.png](/hc/article_attachments/31426083711773)

# Removing a computer from your team 

Removing a computer from your team means disabling online licensing and cloud connectivity for that computer:

-   This means the computer will no longer be remotely accessible using a cloud connection; you will need to make a desk-side visit to enable it again.
-   If your subscription includes offline licensing and direct connections, you may still be able to establish direct connections to the computer (depending on the network).

You can remove a computer from your team using one of the methods shown below.

## Using the RealVNC Connect portal 

To remove a remote computer you've previously [added](https://help.realvnc.com/hc/en-us/articles/360002249677-Licensing-VNC-Connect-#realvnc-server-0-1) to your team:

1.  Sign in to the [RealVNC Connect Portal](https://manage.realvnc.com).
2.  Navigate to the **Devices -\>** **Computers** section.
3.  Locate the computer and choose **Remove from team** from the **\...** menu.

Team members will no longer be able to establish [cloud connections] to this computer. You can now uninstall RealVNC Server, install it on a different computer, and [apply your subscription](https://help.realvnc.com/hc/en-us/articles/360002249677-Licensing-VNC-Connect-#realvnc-server-0-1) there instead.

If you have a subscription that includes direct connectivity, people can still establish [direct connections](/hc/en-us/articles/360002249797) to the computer. To prevent this, make sure you uninstall RealVNC Server.

## Using the command line 

Run the appropriate command (below) on the computer to be removed from the team.

### Windows 

``` ps
"C:\Program Files\RealVNC\VNC Server\vncserver.exe" -service -leavecloud
```

**Note: the command must be run with Administrator privilege.**

### Mac 

``` sh
sudo /Library/vnc/vncserver -service -leavecloud
```

### Linux 

``` sh
sudo vncserver-x11 -service -leavecloud
```

## Using API Access 

If you have access to the API Access feature, you can remove computers from your team using a [REST API](https://docs.realvnc.com/api-access.html#tag/Entries/operation/deleteEntry). For more information about API Access feature, please see [API Access - API documentation and example scripts](/hc/en-us/articles/6521249110685)

[]

# Adding a person to your team 

You can invite people you trust into your team by clicking the **Invite people** button on the **People \> Users** page of the RealVNC Connect Portal.

Each invitee receives an email; they should follow the instructions to create their own RealVNC account, and when they do you'll see them appear in the list of users on the **Users** page:

![team-people-list.png](/hc/article_attachments/4413024422673)\

For an in-depth guide on inviting users, please see [How do I invite people in to my team to share remote access?](/hc/en-us/articles/360004933471)

If your subscription includes it, we recommend mandating that every team member [enables 2-factor authentication](https://help.realvnc.com/hc/en-us/articles/360002250077).

By default, a new team member:

-   Has the [`User`] role. This means the person can use RealVNC Viewer to discover and connect to remote computers, but cannot manage the team. [See how to promote people](/hc/en-us/articles/360002317817).
-   Can automatically discover all the remote computers in your team. [See how to restrict discovery](/hc/en-us/articles/360002320778).

[]

# Removing a person from your team 

You can remove a person from your team on the **People** page of the RealVNC Connect Portal.

![team-remove-person-menu.png](/hc/article_attachments/4413024432785)\

This person will no longer be able to see the team or connect to any of that teams computers. In most circumstances, there's no further action to take. However if you:

1.  Have a subscription that includes direct connectivity
2.  Have installed RealVNC Server on a particular remote computer
3.  Only establish [direct connections](/hc/en-us/articles/360002249797) to that computer

\...then you should additionally remove the person from the list of [registered RealVNC Server users](/hc/en-us/articles/360002253618) for that computer. Until you do, this person *will* still be able to establish direct connections.

You cannot remove the team owner. Contact us if you need to change ownership.

[]

# Promoting people to help manage the team 

You can promote team members to help you manage the team, which may be useful if there are many computers and people in the team.

Each person you invite has a *role.*

For information on roles, see [Can I promote people to help administer my team?](/hc/en-us/articles/360002317817)

You can change roles on the **People** page of the RealVNC Connect Portal.

[]

# Restricting remote computer access to certain people 

You can divide responsibility for remote computers among the people in your team by assigning discovery permissions on the **Computers** page of the RealVNC Connect Portal.

**\*There's no way to bypass our discovery service. If a team member does not have permission to discover a particular computer, they cannot possibly establish a [cloud connection](https://help.realvnc.com/hc/en-us/articles/360002249737) to it.**

You can assign permissions to an individual computer:

![team-computer-individual-discoveryperms.png](/hc/article_attachments/4413031666577)\

Remove the default [`Everyone`]` `[`in`]` `[`the`]` `[`team`] permission and select **+ Add a person or group of people** to explicitly name team members:

![team-computer-everyone-permission.png](/hc/article_attachments/4413038000529)\

**\*Those *not* explicitly named will be denied access. If there's no-one in the list, the computer will be inaccessible.**

Alternatively, you can group computers together on the **Computers** page and then assign team members to groups, if it makes it easier. You can even create groups of people on the **People** page and then assign people groups to computer groups on the **Computers** page.