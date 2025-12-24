# Source: https://help.realvnc.com/hc/en-us/articles/4409166919441-How-do-I-use-the-Session-Recording-feature-in-RealVNC-Connect

# How do I use the Session Recording feature in RealVNC Connect? 

[Follow](/hc/en-us/articles/4409166919441-How-do-I-use-the-Session-Recording-feature-in-RealVNC-Connect/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360077753378/Jack_Naisbett_Professional_Headshot_for_web_-_Copy.jpg)

**[Jack N RealVNC](/hc/en-us/profiles/364261730191-Jack-N-RealVNC)**

Updated July 25, 2025 10:53

# What is Session Recording? 

Starting with RealVNC Viewer 6.21.920 (Windows, Mac and Linux) / RealVNC Viewer 6.22.826 (Raspberry Pi) and RealVNC Server 6.8.0 you can record your RealVNC Connect sessions as a [webm](https://www.webmproject.org/about/) video file.

This feature can only be used on desktops (Windows, Linux, and Mac) which are listed as [Supported Platforms for VNC Connect](/hc/en-us/articles/360002252798). Session recording is not supported on Real[VNC Viewer and RealVNC Server for Mobile.]

# [How do I record my sessions?] 

When connected to a RealVNC Server that supports session recording, click the toolbar button [![icon.png](/hc/article_attachments/4409278774545)] to begin and end a recording.

![2.png](/hc/article_attachments/4409166880785)

For an overview of how it works, please watch the video below:

[![](https://static.realvnc.com/media/images/ScreenRecordingVideoBanner-02.original.jpg)](https://www.youtube-nocookie.com/embed/i5q1vhoI6NA)

# Where are recordings saved? 

[Recordings will be saved locally to a folder on the RealVNC Viewer device, and will not be accessible from RealVNC systems or its employees.]

[The location of the recording will by default be the standard media folder for the OS] -- on Windows desktops this is %USERPROFILE%\\Videos\\RealVNC\\.

This location can be altered in RealVNC Viewer\'s Preferences, Recording section, by using the Choose folder button, and then navigating to a new location before selecting OK.

![3.png](/hc/article_attachments/4409160215825)

You can open the recording location from the RealVNC Viewer by selecting "Show in folder", from here you can play back the recorded sessions with any standard webm file viewer, such as modern web browsers, or Microsoft Windows Films & TV viewer. 

# [How do I configure Session Recording?] 

## [RealVNC Viewer] 

Configuration options allow the recording of all sessions by default, or enabling and disabling a recording within a session. To access the configuration options, open the RealVNC Viewer Application Preferences dialog, by using RealVNC Viewer's File menu and selecting Preferences. Next, then navigate to the Recording section:

![1.png](/hc/article_attachments/4409166860945)

## RealVNC Server 

Session recording can also be enabled or disabled in RealVNC Server, by opening RealVNC Server\'s Options dialog and navigating to the Users & Permissions section. Here you can set Global Permissions or per-user/per-group permissions to allow or disallow connected RealVNC Viewer users to record sessions.

![4.png](/hc/article_attachments/4409166881041)

Other RealVNC Server options for session recording can be found in the Expert section, for example to configure the duration of notification prompts when recording starts and stops, or whether to show a persistent notification when a recording is taking place.

![RecordingQuery_Parameter.png](/hc/article_attachments/10206507845917)

#### New in RealVNC Server 7.1.0 

When the RecordQuery Parameter is set to True, the owner of the remote device will see the following prompt. If they are happy for the session to be recorded, they should click \'Allow\'.

![VNC_Server_Prompt.png](/hc/article_attachments/10156327964445)

# [How do I record an On-Demand Assist session?] 

[Starting with RealVNC Viewer 7.1.0 and On-Demand Assist 2.1.0, technicians can record an On-Demand Assist session as a [webm](https://www.webmproject.org/about/) video file.]

When connected to a user\'s device, click the toolbar button [![icon.png](/hc/article_attachments/4409278774545)] to begin and end a recording.

![2.png](/hc/article_attachments/4409166880785)

The end user will see the following pop up, if they are happy for the session to be recorded they should click \'Allow\'. 

![ODA_Prompt.png](/hc/article_attachments/10156009952669)

This popup will timeout after 30 seconds, and the technician will be unable to control the session while the prompt is displayed.

Once the end user has accepted the prompt, session recording will then be allowed for the duration of the session. 

# [Troubleshooting] 

If you see the error \'This session cannot be recorded because the remote computer does not allow it.\' this means either:

-   The version of RealVNC Viewer you are running does not support session recording in On-Demand Assist; or
-   RealVNC Server has the RecordQuery parameter set to True and your version of RealVNC Viewer does not support it. 

![Screen_Recording_denied.png](/hc/article_attachments/10156451217181)

You can download the latest version of RealVNC Viewer [here](https://www.realvnc.com/en/connect/download/viewer/).