# Source: https://support.anydesk.com/docs/session-recording

AnyDesk supports recording a session from both ends of the connection. These recordings are always stored locally and can be deactivated in the [settings](https://support.anydesk.com/knowledge/settings#recording).

-   Session recordings are stored in the.ANYDESK file format.

-   Session recordings can only be played using an AnyDesk client.

-   AnyDesk can **set whether only incoming, outgoing connections, or both** should be recorded.

-   Session quality or performance is not affected when session recording is enabled.

-   Modifications like watermark or additional display elements are not supported.

-   Concurrent sessions will create a separate recording for each session.

### Settings   

Recording Settings can be found in the main menu under *Settings \> Recording***.**

In these settings, users can automatically:

-   Automatically record incoming sessions at the session start

-   Automatically record outgoing sessions at the sessions start

Users can also **start recording in the middle of an active session** by pressing the record button **![recording](https://f.hubspotusercontent40.net/hubfs/7940397/Help%20Center/Session%20Settings/recording.png)** in the [AnyDesk toolbar](https://support.anydesk.com/knowledge/session-settings#active-session).

### **Filename Formatting** 

The filename for recordings contains:

-   Session type: outgoing or incoming

-   Both clients\' Alias and ID

**Note:** Sessions are stored in the .ANYDESK file format and conversion are not supported at this time.

The filename is always in the format:

``` 
<incoming/outgoing> <name_other_client> (<ID_other_client>)-<name_your_client> (<ID_your_client>).anydesk
```

**Caution:** Please note that if AnyDesk is installed, the name of the client will always be SYSTEM as it is the SYSTEM user that starts AnyDesk.

For more differences between portable and installed versions of AnyDesk, please see [Portable vs. Installed](https://support.anydesk.com/knowledge/portable-vs-installed).

### **Session Player**   

The Session Player supports:

-   Start from the beginning of the recording

-   Start/Pause

-   Fast Forward

-   Super Fast Forward

-   Skip to a certain point

The recording can be played by double-clicking the file in the File Explorer or selecting \"Screen Recording\" in the main menu.

[**[Default save locations:]**]

**Windows:** %homepath%\\Videos\\AnyDesk

**macOS:** \~/.anydesk/AnyDesk

**Linux:** \~/Videos/AnyDesk

Custom paths based on the local device are supported.