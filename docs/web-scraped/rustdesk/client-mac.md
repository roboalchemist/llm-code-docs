# Source: https://rustdesk.com/docs/en/client/mac/

# Mac

## Installation

Open the .dmg file and drag `RustDesk` to `Applications` as below.

Make sure you have quit all running RustDesk. Also make sure you quit the RustDesk service shown on the tray.

## Allow RustDesk run

Unlock to changeClick on `App Store and identified developers`
## Enable permissions

Note

Due to macOS security policy change, our api which captures input on local side does not work any
more. You have to enable &ldquo;Input Monitoring&rdquo; permission on local Mac side.
Please follow this
https://github.com/rustdesk/rustdesk/issues/974#issuecomment-1185644923.

In version 1.2.4, you can try out `Input source 2` which can be seen by clicking on keyboard icon on the toolbar.

To capture screen, you need to grant RustDesk **Accessibility** permission and **Screen Recording** permission. RustDesk will guide you to the settings window.
RustDesk windowSettings window
If you have enabled it in the settings window, but RustDesk still warns. Please remove `RustDesk` from the settings windows by the `-` button, and click on `+` button, select `RustDesk` in `Applications`.

Note

https://github.com/rustdesk/rustdesk/issues/3261
Other helpless attempts:
`tccutil reset ScreenCapture com.carriez.RustDesk`
`tccutil reset Accessibility com.carriez.RustDesk`
Reboot is still required.

`-` and `+` buttonSelect `RustDesk`
Please copy above steps for **Screen Recording** permission.