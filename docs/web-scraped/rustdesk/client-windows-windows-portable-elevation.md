# Source: https://rustdesk.com/docs/en/client/windows/windows-portable-elevation/

# Windows Portable Elevation

Windows portable programs do not have administrator privileges, which can lead to the following issues:

- The screen cannot be transmitted when the UAC (User Account Control) window pops up.
- When an elevated window, such as the Task Manager, pops up, the mouse becomes unresponsive.

By elevating privileges, RustDesk can create a process with administrator privileges during startup or a session, enabling it to perform screenshotting and mouse operations, thereby avoiding the above problems.

## Elevate at startup

This way, remote users don&rsquo;t need to request elevation when connecting. There are two methods:

- 
Method 1: Change the name of the portable program to include `-qs-` (1.2.0, 1.2.1, 1.2.2, 1.2.3 versions end with `qs.exe`). Click the left mouse button to run, click `Accept` in the UAC window.

- 
Method 2: Right-click and run as administrator.

## Elevate at the controlled end

The controlled end can directly click `Accept and Elevate` when connecting, or click `Elevate` when already connected.
ConnectingConnected
## Request elevation at the control end

After selecting `Request Elevation` from the action menu, the following dialog box will appear. If you choose `Ask the remote user for authentication`, you won&rsquo;t need to input a username and password, but the user on the remote computer must have administrator privileges. If you select `Transmit the username and password of administrator`, the user on the remote computer only needs to accept in the UAC window. After sending the request, please wait for the user on the other side to accept the UAC window. Upon confirmation, a success message will appear. Note that **both methods require someone on the controlled end to accept the UAC window**. Therefore, if there is no one available on the other side, elevation should not be requested at the control end.
MenuDialog**Wait****Success**
## How to Choose

ScenarioMethodNo elevation requiredInstall the programNo user available at the controlled endRename
*or*
Run with administratorUser available at the controlled end
*and*
Immediate elevation when connected
*and*
Accept-via-click connectionClick `Accept and Elevate` when receiving the connection at the controlled endUser available at the controlled end
*and*
Elevation as neededClick `Elevate` on the connection management window at the controlled end
*or*
Request elevation at the control end