# Source: https://rustdesk.com/docs/en/self-host/client-configuration/advanced-settings/

# Advanced Settings

All advanced settings in custom clients are covered here.

## Privilege Levels for Settings

There are four types of settings:

- Override settings, in `Web Console` â `Custom Clients`
- Default settings, in `Web Console` â `Custom Clients`
- User settings, in the RustDesk client
- Strategy settings, in `Web Console` â `Strategies`

The hierarchy of privilege for these settings is as follows: `Override > Strategy > User > Default`.

## Security Settings

### access-mode

Set the access mode (permissions) for incoming connections.

**Location**:

- **Desktop** Settings â Security â Permissions
- **Mobile**

Install requiredValuesDefaultExampleNcustom, full, viewcustom`access-mode=custom`
### enable-keyboard

Enable keyboard/mouse input for incoming connections.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable keyboard
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-keyboard=Y`
### enable-clipboard

Enable copy and paste for incoming connections.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable clipboard
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-clipboard=Y`
### enable-file-transfer

Enable file copy and paste or file transfer (session) for incoming connections.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable file transfer
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-file-transfer=Y`
### enable-camera

Enable camera for incoming connections.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable camera
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-camera=Y`
### enable-terminal

Enable terminal for incoming connections.

**Location**:

**Desktop** Settings â Security â Permissions â Enable terminal
Install requiredValuesDefaultExampleNY, NY`enable-terminal=Y`
### enable-remote-printer

Enable remote printer for incoming connections.

**Location**:

- **Windows** Settings â Security â Permissions â Enable remote printer

Install requiredValuesDefaultExampleNY, NY`enable-remote-printer=Y`
### enable-audio

Enable audio record and transfer to peer.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable audio
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-audio=Y`
### enable-tunnel

Enable TCP tunneling.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable TCP tunneling
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-tunnel=Y`
### enable-remote-restart

Enable restarting by the control side.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable remote restart
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-remote-restart=Y`
### enable-record-session

Enable sessions to be recorded.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable recording session
- **Mobile** Settings â Share screen â Enable recording session

Install requiredValuesDefaultExampleNY, NY`enable-record-session=Y`
### enable-block-input

Enable the control side to block other users&rsquo; input.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable blocking user input (Windows only)
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-block-input=Y`
### allow-remote-config-modification

Allow the control side to change the settings in controlled RustDesk UI.

**Location**:

- **Desktop** Settings â Security â Permissions â Enable remote configuration modification
- **Mobile**

Install requiredValuesDefaultExampleNY, NN`allow-remote-config-modification=Y`
### enable-lan-discovery

Allows LAN peers to discover me.

After LAN discovery, WOL can work if supported locally.

**Location**:

- **Desktop** Settings â Security â Security â Deny LAN discovery
- **Mobile** Settings â Share screen â Deny LAN discovery

Install requiredValuesDefaultExampleYY, NY`enable-lan-discovery=Y`
### direct-server

Enable direct IP access.

**Location**:

- **Desktop** Settings â Security â Security â Enable direct IP access
- **Mobile** Settings â Share screen â Direct IP access

Install requiredValuesDefaultExampleNY, NN`direct-server=Y`
### direct-access-port

Direct IP access port.

**Location**:

- **Desktop** Settings â Security â Security â Direct IP access port (Show if &ldquo;Enable direct IP access&rdquo; is checked)
- **Mobile** Settings â Share screen â Direct IP access

Install requiredValuesDefaultExampleN21118`direct-access-port=21118`
### whitelist

Use IP Whitelisting.

**Location**:

- **Desktop** Settings â Security â Security â Use IP Whitelisting
- **Mobile** Settings â Share screen â Use IP Whitelisting

Install requiredValuesDefaultExampleN`,` or `<ip1>,<ip2>,<ip3>``,` means no filter`whitelist=,`
### allow-auto-disconnect & auto-disconnect-timeout

Automatically close incoming sessions after a period of user inactivity.

**Location**:

- **Desktop** Settings â Security â Security â Automatically close incoming sessions on user inactivity
- **Mobile** Settings â Share screen â Automatically close incoming sessions on user inactivity

OptionInstall requiredValuesDefaultExampleallow-auto-disconnectNY, NN`allow-auto-disconnect=Y`auto-disconnect-timeoutNTimeout in minutes10`auto-disconnect-timeout=10`
### allow-only-conn-window-open

Only allow connection if RustDesk window is open.

**Location**:

- **Desktop** Settings â Security â Security â Only allow connection if RustDesk window is open
- **Mobile**

Install requiredValuesDefaultExampleYY, NN`allow-only-conn-window-open=N`
### approve-mode

Accept incoming connections via password or manually click.

**Location**:

- **Desktop** Settings â Security â Password â Dropdown box
- **Mobile** Share screen â Dropdown menu on right-up corner

Install requiredValuesDefaultExampleNpassword, click, password-clickpassword-click`approve-mode=password-click`
### verification-method

What type of password can be used, `temporary password` refers to the one-time random password.
Install requiredValuesDefaultExampleNuse-temporary-password, use-permanent-password, use-both-passwordsuse-both-passwords`verification-method=use-permanent-password`
### temporary-password-length

- **Desktop** Settings â Security â Password â One-time password length
- **Mobile** Share screen â Dropdown menu on right-up corner â One-time password length

The length of the temporary password.
Install requiredValuesDefaultExampleN6, 8, 10`temporary-password-length=6`
### proxy-url

The proxy URL.

Currently support `http` and `socks5`.

**Location**:

- **Desktop** Settings â Network â Proxy â Socks5/Http(s) proxy
- **Mobile**

Examples:

- **http** `proxy-url=http://192.168.0.2:12345`
- **https** `proxy-url=https://192.168.0.2:12345`
- **socks5** `proxy-url=socks5://192.168.0.2:1080`

### proxy-username & proxy-password

Proxy username and password.

**Location**:

- **Desktop** Settings â Network â Proxy â Socks5/Http(s) proxy
- **Mobile**

OptionInstall requiredValuesDefaultExampleproxy-usernameN`proxy-username=user`proxy-passwordN`proxy-password=pass`
## General Settings

### theme

Controls the UI theme of RustDesk client.

**Location**:

- **Desktop** Settings â General â Theme
- **Mobile** Settings â Settings â Theme

Install requiredValuesDefaultExampleNdark, light, systemsystem`theme=system`
### lang

Controls the language of RustDesk client.

**Location**:

- **Desktop** Settings â General â Language
- **Mobile** Settings â Settings â Language

Install requiredValuesDefaultExampleNdefault, ar, bg, &mldr;default`lang=default`
Currently available languages are:

ar, bg, ca, cs, da, de, el, en, eo, es, et, fa, fr, he, hr, hu, id, it, ja, ko, kz, lt, lv, nb, nl, pl, pt, ro, ru, sk, sl, sq, sr, sv, th, tr, uk, vn, zh-cn, zh-tw

You can check LANGS in the code for the latest language list.

### allow-auto-record-incoming

Automatically record incoming sessions.

**Location**:

- **Desktop** Settings â General â Recording â Automatically record incoming sessions
- **Mobile** Settings â Recording â Automatically record incoming sessions

Install requiredValuesDefaultExampleNY, NN`allow-auto-record-incoming=Y`
### allow-auto-record-outgoing

Automatically record outgoing sessions.

**Location**:

- **Desktop** Settings â General â Recording â Automatically record outgoing sessions
- **Mobile** Settings â Recording â Automatically record outgoing sessions

Install requiredValuesDefaultExampleVersionNY, NN`allow-auto-record-outgoing=Y`>= 1.3.2
### video-save-directory

The directory to save recorded videos.

**Location**:

- **Desktop** Settings â General â Recording â Video save directory
- **Mobile** Settings â Recording

Default values:

- **macOS** ~/Movies/**app_name**
- **Linux** ~/Videos/**app_name**
- **Windows** %USERPROFILE%\Videos\**app_name**
- **Android** /Storage/emulated/0/**app_name**/ScreenRecord

**Note**: Replace **app_name** means current app name.

### enable-confirm-closing-tabs

Controls whether to show a confirm dialog before closing all remote tabs.

**Location**:

- **Desktop** Settings â General â Other â Confirm before closing multiple tabs
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-confirm-closing-tabs=Y`
### enable-abr

Enable adaptive bitrate.

**Location**:

- **Desktop** Settings â General â Other â Adaptive bitrate
- **Mobile** Settings â Share screen â Adaptive bitrate (beta)

Install requiredValuesDefaultExampleNY, NY`enable-abr=Y`
### allow-remove-wallpaper

Remove wallpaper during incoming sessions.

**Location**:

- **Desktop** Settings â General â Other â Remove wallpaper during incoming sessions
- **Mobile**

Install requiredValuesDefaultExampleNY, NN`allow-remove-wallpaper=N`
### enable-open-new-connections-in-tabs

Controls whether to use a new tab or a new window to open a new connection.

**Location**:

- **Desktop** Settings â General â Other â Open connection in new tab
- **Mobile**

Install requiredValuesDefaultExampleNY, NY`enable-open-new-connections-in-tabs=Y`
### allow-always-software-render

Always use software rendering.

**Location**:

- **Desktop** Settings â General â Other â Always use software rendering
- **Mobile**

Install requiredValuesDefaultExampleNY, NN`allow-always-software-render=N`
### allow-linux-headless

Allow incoming connection if there&rsquo;s no displays.

This option requires desktop environment, Xorg server and GDM, see PR 3902.

**Location**:

- **Desktop** Settings â General â Other â Allow Linux headless
- **Mobile**

Install requiredValuesDefaultExampleYY, NN`allow-linux-headless=N`
### enable-hwcodec

Enable hardware encoding to make the picture smoother.

**Location**:

- **Desktop**
- **Mobile** Settings â Hardware codec

Install requiredValuesDefaultExampleNY, NY`enable-hwcodec=Y`
### peer-card-ui-type

Controls the view of peer cards, includes &ldquo;Big tiles&rdquo;, &ldquo;Small tiles&rdquo; and &ldquo;List&rdquo;.

**Location**:

- **Desktop** Home â Peer panel â Right top grid icon
- **Mobile**

Install requiredValuesDefaultExampleN0, 1, 20`peer-card-ui-type=0`
**0** Big tiles
**1** Small tiles
**2** List

### peer-sorting

Controls the ordering of peer cards.

**Location**:

- **Desktop** Home â Peer panel â Right top sort icon
- **Mobile**

Install requiredValuesDefaultExampleNRemote ID, Remote Host, UsernameRemote ID`peer-sorting=Remote ID`
### sync-ab-with-recent-sessions

Controls whether to sync the address book with recent sessions.

**Location**:

- **Desktop** Home â Peer panel â Address book â Tags â Dropdown menu â Sync with recent sessions
- **Mobile** Home â Peer panel â Address book â Tags â Dropdown menu â Sync with recent sessions

Install requiredValuesDefaultExampleNY, NN`sync-ab-with-recent-sessions=N`
### sync-ab-tags

Controls whether to sort the address book tags.

**Location**:

- **Desktop** Home â Peer panel â Address book â Tags â Dropdown menu â Sort tags
- **Mobile** Home â Peer panel â Address book â Tags â Dropdown menu â Sort tags

Install requiredValuesDefaultExampleNY, NN`sync-ab-tags=N`
### filter-ab-by-intersection

Filter address book by tag intersection.

**Preview**: PR #5985

**Location**:

- **Desktop** Home â Peer panel â Address book â Tags â Dropdown menu â Filter by intersection
- **Mobile** Home â Peer panel â Address book â Tags â Dropdown menu â Filter by intersection

Install requiredValuesDefaultExampleNY, NN`filter-ab-by-intersection=N`
### use-texture-render

**Location**:

**Desktop** Settings â General â Other â Use texture render

Use texture rendering to make the pictures smoother. You could try disabling this option if you encounter rendering issues. Only available on desktop.
ValuesDefaultExampleY, Nlinux:Y, macOS:N, win7:N, win10+:Y`use-texture-render=Y`
### enable-udp-punch

**Location**:

**Desktop** Settings â General â Other â Enable UDP hole punching
**Mobile** Settings â Enable UDP hole punching

Available since RustDesk 1.4.1, RustDesk Server Pro 1.6.2
ValuesDefaultExampleY, NY`enable-udp-punch=N`
### enable-ipv6-punch

**Location**:

**Desktop** Settings â General â Other â Enable IPv6 P2P connection
**Mobile** Settings â General â Other â Enable IPv6 P2P connection

Available since RustDesk 1.4.1, RustDesk Server Pro 1.6.2
ValuesDefaultExampleY, Nselfhost:N, otherwise:Y`enable-ipv6-punch=N`
## Display Settings

### view-only

This option will set the &ldquo;view-only&rdquo; option for every peer after the first connection.

Then the &ldquo;view-only&rdquo; option in each peer&rsquo;s settings will controls whether the connection is view-only.

**Location**:

- **Desktop** Settings â Display â Other default options â View mode
- **Mobile** Settings â Display settings â Other default options â View mode

Install requiredValuesDefaultExampleNY, NN`view-only=Y`
### show-monitors-toolbar

Controls whether to show monitors in toolbar.

**Location**:

- **Desktop** Settings â Display â Other default options â Show monitors toolbar
- **Mobile**

Install requiredValuesDefaultExampleNY, NN`show-monitors-toolbar=Y`
### collapse-toolbar

Controls whether the remote toolbar is collapsed after connecting.

**Location**:

- **Desktop** Settings â Display â Other default options â Collapse toolbar
- **Mobile**

Install requiredValuesDefaultExampleNY, NN`collapse-toolbar=Y`
### show-remote-cursor

This option will set the &ldquo;show-remote-cursor&rdquo; option for every peer after the first connection.

Then the &ldquo;show-remote-cursor&rdquo; option in each peer&rsquo;s settings will controls whether the remote cursor is displayed in the remote control page.

**Location**:

- **Desktop** Settings â Display â Other default options â Show remote cursor
- **Mobile** Settings â Display settings â Other default options â Show remote cursor

Install requiredValuesDefaultExampleNY, NN`show-remote-cursor=N`
### follow-remote-cursor

This option will set the &ldquo;follow-remote-cursor&rdquo; option for every peer after the first connection.

Then the &ldquo;follow-remote-cursor&rdquo; option in each peer&rsquo;s settings will controls whether to follow the remote cursor.

**Preview**: PR 7717

**Location**:

- **Desktop** Settings â Display â Other default options â Follow remote cursor
- **Mobile** Settings â Display settings â Other default options â Follow remote cursor

Install requiredValuesDefaultExampleNY, NN`follow-remote-cursor=Y`
### follow-remote-window

This option will set the &ldquo;follow-remote-window&rdquo; option for every peer after the first connection.

Then the &ldquo;follow-remote-window&rdquo; option in each peer&rsquo;s settings will controls whether to follow the remote window.

**Preview**: PR 7717

**Location**:

- **Desktop** Settings â Display â Other default options â Follow remote window focus
- **Mobile** Settings â Display settings â Other default options â Follow remote window focus

Install requiredValuesDefaultExampleNY, NN`follow-remote-window=Y`
### zoom-cursor

This option will set the &ldquo;zoom-cursor&rdquo; option for every peer after the first connection.

The &ldquo;zoom-cursor&rdquo; option in each peer&rsquo;s settings will then control whether the cursor is scaled based on the current image scale.

**Location**:

- **Desktop** Settings â Display â Other default options â Zoom cursor
- **Mobile**

Install requiredValuesDefaultExampleNY, NN`zoom-cursor=Y`
### show-quality-monitor

This option will set the &ldquo;show-quality-monitor&rdquo; option for every peer after the first connection.

The &ldquo;show-quality-monitor&rdquo; option in each peer&rsquo;s settings will then control whether to show the quality monitor.

**Location**:

- **Desktop** Settings â Display â Other default options â Show quality monitor
- **Mobile** Settings â Display settings â Other default options â Show quality monitor

Install requiredValuesDefaultExampleNY, NN`show-quality-monitor=Y`
### disable-audio

This option will set the &ldquo;disable-audio&rdquo; option for every peer after the first connection.

The &ldquo;disable-audio&rdquo; option in each peer&rsquo;s settings will then control whether to play sound.

**Location**:

- **Desktop** Settings â Display â Other default options â Mute
- **Mobile** Settings â Display settings â Other default options â Mute

Install requiredValuesDefaultExampleNY, NN`disable-audio=Y`
### enable-file-copy-paste

This option will set the &ldquo;enable-file-copy-paste&rdquo; option for every peer after the first connection.

The &ldquo;enable-file-copy-paste&rdquo; option in each peer&rsquo;s settings will then control enable file copy and paste in connection.

**Location**:

- **Desktop** Settings â Display â Other default options â Enable file copy and paste (Windows only)
- **Mobile**

Install requiredValuesDefaultExampleNY, NN`enable-file-copy-paste=Y`
### disable-clipboard

This option will set the &ldquo;disable-clipboard&rdquo; option for every peer after the first connection.

The &ldquo;disable-clipboard&rdquo; option in each peer&rsquo;s settings will then control whether to enable text copy and paste.

**Location**:

- **Desktop** Settings â Display â Other default options â Disable clipboard
- **Mobile** Settings â Display settings â Other default options â Disable clipboard

Install requiredValuesDefaultExampleNY, NN`disable-clipboard=Y`
### lock-after-session-end

This option will set the &ldquo;lock-after-session-end&rdquo; option for every peer after the first connection.

The &ldquo;lock-after-session-end&rdquo; option in each peer&rsquo;s settings will then control whether to lock the peer machine after the session ends.

**Location**:

- **Desktop** Settings â Display â Other default options â Lock after session end
- **Mobile** Settings â Display settings â Other default options â Lock after session end

Install requiredValuesDefaultExampleNY, NN`lock-after-session-end=Y`
### privacy-mode

This option will set the &ldquo;privacy-mode&rdquo; option for every peer after the first connection.

The &ldquo;privacy-mode&rdquo; option in each peer&rsquo;s settings will then control whether to use privacy mode after connecting.

**Location**:

- **Desktop** Settings â Display â Other default options â Privacy mode
- **Mobile** Settings â Display settings â Other default options â Privacy mode

Install requiredValuesDefaultExampleNY, NN`privacy-mode=Y`
### i444

This option will set the &ldquo;i444&rdquo; option for every peer after the first connection.

The &ldquo;i444&rdquo; option in each peer&rsquo;s settings will then control whether to use true color.

**Location**:

- **Desktop** Settings â Display â Other default options â True color (4:4:4)
- **Mobile** Settings â Display settings â Other default options â True color (4:4:4)

Install requiredValuesDefaultExampleNY, NN`i444=Y`
### reverse-mouse-wheel

This option will set the &ldquo;reverse-mouse-wheel&rdquo; option for every peer after the first connection.

The &ldquo;reverse-mouse-wheel&rdquo; option in each peer&rsquo;s settings will then control whether to reverse mouse wheel.

**Location**:

- **Desktop** Settings â Display â Other default options â Reverse mouse wheel
- **Mobile** Settings â Display settings â Other default options â Reverse mouse wheel

Install requiredValuesDefaultExampleNY, NN`reverse-mouse-wheel=Y`
### swap-left-right-mouse

This option will set the &ldquo;swap-left-right-mouse&rdquo; option for every peer after the first connection.

The &ldquo;swap-left-right-mouse&rdquo; option in each peer&rsquo;s settings will then control whether to swap left-right mouse button.

**Location**:

- **Desktop** Settings â Display â Other default options â Swap left-right mouse button
- **Mobile** Settings â Display settings â Other default options â Swap left-right mouse button

Install requiredValuesDefaultExampleNY, NN`swap-left-right-mouse=Y`
### displays-as-individual-windows

This option will set the &ldquo;displays-as-individual-windows&rdquo; option for every peer after the first connection.

The &ldquo;displays-as-individual-windows&rdquo; option in each peer&rsquo;s settings will then control whether to show displays as individual windows.

**Preview**: PR 5945

**Location**:

- **Desktop** Settings â Display â Other default options â Show displays as individual windows
- **Mobile**

Install requiredValuesDefaultExampleNY, NN`displays-as-individual-windows=Y`
### use-all-my-displays-for-the-remote-session

This option will set the &ldquo;use-all-my-displays-for-the-remote-session&rdquo; option for every peer after the first connection.

The &ldquo;use-all-my-displays-for-the-remote_session&rdquo; option in each peer&rsquo;s settings will then control whether to use all my displays for the remote session.

**Preview**: PR 6064

**Location**:

- **Desktop** Settings â Display â Other default options â Use all my displays for the remote session
- **Mobile**

Install requiredValuesDefaultExampleNY, NN`use-all-my-displays-for-the-remote-session=Y`
### view-style

This option will set the &ldquo;view-style&rdquo; option for every peer after the first connection.

The &ldquo;view-style&rdquo; option in each peer&rsquo;s settings will then control the view style.

**Location**:

- **Desktop** Settings â Display â Default view style
- **Mobile** Settings â Display settings â Default view style

Install requiredValuesDefaultExampleNoriginal, adaptiveoriginal`view-style=original`
### scroll-style

This option will set the &ldquo;scroll-style&rdquo; option for every peer after the first connection.

The &ldquo;scroll-style&rdquo; option in each peer&rsquo;s settings will then control the scroll style.

**Location**:

- **Desktop** Settings â Display â Default scroll style
- **Mobile**

Install requiredValuesDefaultExampleNscrollauto, scrollbar, scrolledgescrollauto`scroll-style=scrollauto`
**Note**: The `scrolledge` option is available starting from RustDesk 1.4.4.

### edge-scroll-edge-thickness

This option controls the edge thickness when `scroll-style` is set to `scrolledge`. The edge thickness determines the size of the scrollable area at the screen edges.

This option is only effective when `scroll-style=scrolledge`.

**Location**:

- **Desktop** Settings â Display â Edge scroll edge thickness

Install requiredValuesDefaultExampleN20-150100`edge-scroll-edge-thickness=100`
**Note**: This option is available starting from RustDesk 1.4.4.

### image-quality

This option will set the &ldquo;image-quality&rdquo; option for every peer after the first connection.

The &ldquo;image-quality&rdquo; option in each peer&rsquo;s settings will then control the image quality.

**Location**:

- **Desktop** Settings â Display â Default image quality
- **Mobile** Settings â Display settings â Default image quality

Install requiredValuesDefaultExampleNbest, balanced, low, custombalanced`image-quality=balanced`
### custom-image-quality

This option will set the &ldquo;custom-image-quality&rdquo; option for every peer after the first connection.

The &ldquo;custom-image-quality&rdquo; option in each peer&rsquo;s settings will then control the image quality if &ldquo;image-quality&rdquo; is set to custom.

**Location**:

- **Desktop** Settings â Display â Default image quality â Custom
- **Mobile** Settings â Display settings â Default image quality â Custom

Install requiredValuesDefaultExampleN[10.0, 2000.0]50.0`custom-image-quality=50`
### custom-fps

This option will set the &ldquo;custom-fps&rdquo; option for every peer after the first connection.

The &ldquo;custom-fps&rdquo; option in each peer&rsquo;s settings will then control the fps if &ldquo;image-quality&rdquo; is set to custom.

**Location**:

- **Desktop** Settings â Display â Default image quality â Custom
- **Mobile** Settings â Display settings â Default image quality â Custom

Install requiredValuesDefaultExampleN[5, 120]30`custom-fps=30`
### codec-preference

This option will set the &ldquo;codec-preference&rdquo; option for every peer after the first connection.

The &ldquo;codec-preference&rdquo; option in each peer&rsquo;s settings will then control codec for images.

**Location**:

- **Desktop** Settings â Display â Default codec
- **Mobile** Settings â Display settings â Default codec

Install requiredValuesDefaultExampleNauto, vp8, vp9, av1, h264, h265auto`codec-preference=auto`
**Caution**: Options other than &ldquo;vp8&rdquo; and &ldquo;vp9&rdquo; may not work. This depends on what your machine supports.

### terminal-persistent

This option will set the &ldquo;terminal-persistent&rdquo; option for every peer after the first connection.

The &ldquo;terminal-persistent&rdquo; option in each peer&rsquo;s settings will then control whether to keep terminal sessions on disconnect.

**Location**:

- **Desktop** Settings â Display â Other default options â Keep terminal sessions on disconnect
- **Mobile** Settings â Display settings â Other default options â Keep terminal sessions on disconnect

Install requiredValuesDefaultExampleNY, NN`terminal-persistent=Y`
### trackpad-speed

This option will set the &ldquo;trackpad-speed&rdquo; option for every peer after the first connection.

The &ldquo;trackpad-speed&rdquo; option in each peer&rsquo;s settings will then control the fps if &ldquo;trackpad-speed&rdquo; is set to custom.

**Location**:

- **Desktop** Settings â Display â Default trackpad speed
- **Mobile** Settings â Display settings â Default trackpad speed

Install requiredValuesDefaultExampleN[10, 1000]100`trackpad-speed=100`
## Others

### preset-address-book-name & preset-address-book-tag & preset-address-book-alias & preset-address-book-password & preset-address-book-note

Preset address book name, device tag, device alias, device password, device note, https://github.com/rustdesk/rustdesk-server-pro/issues/257.
You can set preset-address-book-name only if you do not want to set tag.
Please use valid address book name and tag on your address book page of web console.
OptionInstall requiredValuesDefaultExamplepreset-address-book-nameN`preset-address-book-name=<address book name>`preset-address-book-tagN`preset-address-book-tag=<address book tag name>`preset-address-book-aliasN`preset-address-book-alias=<device alias>`preset-address-book-passwordN`preset-address-book-password=<device password>`preset-address-book-noteN`preset-address-book-note=<device note>`
preset-address-book-alias, preset-address-book-password, preset-address-book-note are available in RustDesk client >=1.4.3, pro >= 1.6.6.

### disable-group-panel

Disable group panel (next to address book panel, it is named to &ldquo;Accessible devices&rdquo; since 1.3.8) on RustDesk client, https://github.com/rustdesk/rustdesk-server-pro/issues/250.
OptionInstall requiredValuesDefaultExampledisable-group-panelNY, NN`disable-group-panel=Y`
### pre-elevate-service

Automatic elevation on run for Windows portable, https://github.com/rustdesk/rustdesk-server-pro/issues/252.
OptionInstall requiredValuesDefaultExamplepre-elevate-serviceNY, NN`pre-elevate-service=Y`
### disable-floating-window

When the Android service starts, it will display a floating window, which helps prevent the system from killing the RustDesk service.
ValuesDefaultExampleY, NN`disable-floating-window=Y`
### floating-window-size

When the Android service starts, it will display a floating window, which helps prevent the system from killing the RustDesk service. When the size is less than 120, the floating window will be difficult to be clicked. A very small size may not be able to keep the background service on some devices.
ValuesDefaultExample[32, 320]120`floating-window-size=120`
### floating-window-untouchable

By default, clicking on the floating window will pop up a menu. After setting it to &lsquo;untouchable&rsquo;, clicking or swiping will pass through the floating window and be transmitted to the underlying window. After being set to &lsquo;untouchable&rsquo;, the position of the floating window cannot be changed, and the system may automatically set the floating window to be semi-transparent. However, this feature may not work in a small number of applications, such as the GitHub app.
ValuesDefaultExampleY, NN`floating-window-untouchable=Y`
### floating-window-transparency

Android floating windows have adjustable transparency. If you want to enable but hide the floating window, you can set the transparency to 0, the floating window will be automatically set to &lsquo;untouchable&rsquo; in order to pass through click events.
ValuesDefaultExample[0, 10]10`floating-window-transparency=5`
### floating-window-svg

If an icon is not set for the Android floating window, it will default to displaying the RustDesk icon.
When setting, please write the text content of SVG into one line, and pay attention to the SVG support limitations.
DefaultExampleRustDesk icon`floating-window-svg=<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg t="1717559129252" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4248" xmlns:xlink="http://www.w3.org/1999/xlink" width="32" height="32"><path d="M950.857143 512c0 242.285714-196.571429 438.857143-438.857143 438.857143S73.142857 754.285714 73.142857 512 269.714286 73.142857 512 73.142857s438.857143 196.571429 438.857143 438.857143z" fill="#1296db" p-id="4249"></path></svg>`
### keep-screen-on

This is for the Android controlled side. Note that keeping the screen on depends on the floating window.
ValuesDefaultExamplenever, during-controlled, service-onduring-controlled`keep-screen-on=never`
### enable-directx-capture

This is for the Windows controlled side. If you don&rsquo;t encounter any problems, it is recommended to use the default settings, which prioritize using DirectX for screenshots instead of using GDI directly.
ValuesDefaultExampleY, NY`enable-directx-capture=N`
### enable-android-software-encoding-half-scale

This is for the Android controlled side. By default, when the resolution is greater than 1200, hardware encoding uses the original resolution, while software encoding uses half the resolution, as software encoding is slower. This option is used to set whether software encoding should be scaled to half the resolution.
ValuesDefaultExampleY, NY`enable-android-software-encoding-half-scale=N`
### allow-remote-cm-modification

Controls whether to allow the control side to click on the connection management window to accept connections, change permissions, etc.

https://github.com/rustdesk/rustdesk/issues/7425
ValuesDefaultExampleY, NN`allow-remote-cm-modification=Y`
### remove-preset-password-warning

Controls whether to remove the security warning on GUI when there is preset password in custom client.

https://github.com/rustdesk/rustdesk-server-pro/discussions/286

https://github.com/rustdesk/rustdesk/discussions/7956
ValuesDefaultExampleY, NY`remove-preset-password-warning=Y`
### hide-security-settings / hide-network-settings / hide-server-settings / hide-proxy-settings / hide-websocket-settings / hide-remote-printer-settings

Controls whether to hide some settings. Please ensure `Disable settings` is turned off, otherwise these won&rsquo;t work.

https://github.com/rustdesk/rustdesk-server-pro/issues/263

https://github.com/rustdesk/rustdesk-server-pro/issues/276
ValuesDefaultExampleY, NN`hide-security-settings=Y`
### hide-username-on-card

Controls whether to show username in the list of devices. Because sometimes, the username is too long, will hide the other info.

https://github.com/rustdesk/rustdesk-server-pro/issues/284#issuecomment-2216521407
ValuesDefaultExampleY, NN`hide-username-on-card=Y`
### hide-help-cards

Controls whether to show UAC / permission warnings on GUI.

https://github.com/rustdesk/rustdesk/issues/8687
ValuesDefaultExampleY, NN`hide-help-cards=Y`
### display-name

Change your display name which will be shown on the popup when you connect to remote device. By default it displays login user&rsquo;s name first, otherwise it displays your OS username.

https://github.com/rustdesk/rustdesk-server-pro/issues/277

### disable-udp

Controls whether to use TCP only. It will not use UDP 21116 any more, TCP 21116 will be used instead.
ValuesDefaultExampleY, NN`disable-udp=Y`
### preset-user-name / preset-strategy-name / preset-device-group-name / preset-device-username / preset-device-name / preset-note

Assign user / strategy / device group / device username / device-name(hostname) / note to device. You can also do this via command line.

https://github.com/rustdesk/rustdesk-server-pro/discussions/304

device group is available in RustDesk client >=1.3.8, pro >= 1.5.0

preset-device-username, preset-device-name, preset-note are available in RustDesk client >=1.4.3, pro >= 1.6.6.

### default-connect-password

You use the `default connection password` to establish connections to remote devices. This password is configured on the controlling side and should not be confused with any preset password found on the controlled (incoming-only) client.

e.g. `default-connect-password=abcd1234`

### enable-trusted-devices

Allow trusted devices to skip 2FA verification.

https://github.com/rustdesk/rustdesk/discussions/8513#discussioncomment-10234494
ValuesDefaultExampleY, NY`enable-trusted-devices=N`
### hide-tray

Disable the tray icon in the systray.

https://github.com/rustdesk/rustdesk-server-pro/issues/332
ValuesDefaultExampleY, NN`hide-tray=Y`
### one-way-clipboard-redirection

Disable clipboard sync from controlled side to controlling side, available in RustDesk client >=1.3.1 (controlled side)

https://github.com/rustdesk/rustdesk/discussions/7837
ValuesDefaultExampleY, NN`one-way-clipboard-redirection=Y`
### one-way-file-transfer

Disable file transfer from controlled side to controlling side, available in RustDesk client >=1.3.1 (controlled side)

https://github.com/rustdesk/rustdesk/discussions/7837
ValuesDefaultExampleY, NN`one-way-file-transfer=Y`
### sync-init-clipboard

If sync initial clipboard when establishing connection (only from controlling side to controlled side), available in RustDesk client >=1.3.1 (controlling side)

https://github.com/rustdesk/rustdesk/discussions/9010
ValuesDefaultExampleY, NN`sync-init-clipboard=Y`
### allow-logon-screen-password

If allow password input on logon screen when click-only approve mode is used, available in RustDesk client >=1.3.1 (controlled side)

https://github.com/rustdesk/rustdesk/discussions/9269
ValuesDefaultExampleY, NN`allow-logon-screen-password=Y`
### allow-https-21114

Typically, HTTPS uses port 443. When the API server&rsquo;s port is mistakenly set to 21114, RustDesk client will remove the 21114 port setting by default. Setting the option to Y allows the use of 21114 as the HTTPS port. Available in RustDesk client >=1.3.9.

https://github.com/rustdesk/rustdesk-server-pro/discussions/570
ValuesDefaultExampleY, NN`allow-https-21114=Y`
### allow-d3d-render

D3D render can get high FPS and reduce the cpu usage, but the remote control screen may be black on some devices. Available in RustDesk client >=1.3.9, windows only.
ValuesDefaultExampleY, NN`allow-d3d-render=Y`
### allow-hostname-as-id

Use hostname as id, spaces in the hostname are replaced with &lsquo;-&rsquo;. This is not 100% guaranteed and only occurs the first time the RustDesk client is run (i.e., on a newly installed client); if a conflict occurs, a random ID will be assigned.

Available in RustDesk client version 1.4.0 and later.
ValuesDefaultExampleY, NN`allow-hostname-as-id=Y`
### allow-websocket

Use WebSocket protocol to connect server and client. Only available in RustDesk client >=1.4.0 and Pro server >= 1.5.7. Note that WebSocket only supports relay connection.

To make WebSocket work, you need to configure your reverse proxy correctly, https://rustdesk.com/docs/en/self-host/rustdesk-server-pro/faq/#8-add-websocket-secure-wss-support-for-the-id-server-and-relay-server-to-enable-secure-communication-for-all-platforms

**Location**:

**Desktop** Settings â Network â Use Websocket
**Mobile** Settings â Use Websocket
ValuesDefaultExampleY, NN`allow-websocket=Y`
### allow-numeric-one-time-password

This option enables or disables the use of numeric-only one-time passwords.
Only available in RustDesk client >=1.4.1 and Pro server >= 1.5.9.

**Discussion**: https://github.com/rustdesk/rustdesk-server-pro/discussions/685

**Preview**: https://github.com/rustdesk/rustdesk/pull/11846
ValuesDefaultExampleY, NN`allow-numeric-one-time-password=Y`
### register-device

Do not register the device, you will not see it in the devices page on web console.

**Only available in Pro server >= 1.6.0 and requires custom2 license and number of concurrent connections >= 2.**

If `register-device=N`, below will not work for this device.

- Log in
- `--assign` command
- `preset-address-book-name`, `preset-address-book-tag`, `preset-address-book-alias`, `preset-address-book-password`, `preset-address-book-note` `preset-user-name`, `preset-strategy-name`, `preset-device-group-name`, `preset-device-username`, `preset-device-name`, `preset-note`
- Audit Logs
- Strategy

**Discussion**: https://github.com/rustdesk/rustdesk-server-pro/discussions/672 and https://github.com/rustdesk/rustdesk-server-pro/discussions/182
ValuesDefaultExampleY, NY`register-device=N`
### main-window-always-on-top

Always keep the main window on top.

**Discussion**: https://github.com/rustdesk/rustdesk-server-pro/issues/761

Only available in RustDesk client 1.4.2.
Install requiredValuesDefaultExampleNY, NN`main-window-always-on-top=N`
### relay-server

https://github.com/rustdesk/rustdesk-server-pro/issues/776#issuecomment-3306524913

### disable-discovery-panel

Disable `Discovered` panel (next to `Favorites` panel) on RustDesk client
OptionInstall requiredValuesDefaultExampledisable-discovery-panelNY, NN`disable-discovery-panel=Y`
### touch-mode

Controls whether to use touch mode or mouse mode during remote control sessions.

#### Version Behavior Differences

##### RustDesk (Controlling Side) < 1.4.3

After the first connection, this option sets the &ldquo;touch-mode&rdquo; setting for each peer. Thereafter, the individual settings of each peer determine whether to use touch mode or mouse mode.

**Location**:

- **Desktop**
- **Mobile** Settings â Display settings â Other default options â Touch mode

##### RustDesk (Controlling Side) >= 1.4.3

This option uniformly controls whether all peer devices use touch mode or mouse mode, overriding individual device settings.
ValuesDefaultExampleY, NN`touch-mode=Y`
### show-virtual-mouse

https://github.com/rustdesk/rustdesk/pull/12911

Controls the display of the virtual mouse when mobile -> desktop.

**Location**:

- **Desktop**
- **Mobile** Remote session -> bottom navigation bar -> gesture helper

Available since RustDesk 1.4.3
ValuesDefaultExampleY, NN`show-virtual-mouse=Y`
**Note**: This option should be configured in **Default settings** rather than **Override settings**.

### show-virtual-joystick

https://github.com/rustdesk/rustdesk/pull/12911

Controls the display of the virtual joystick when mobile -> desktop.

This option requires the **show-virtual-mouse** to be enabled.

**Location**:

- **Desktop**
- **Mobile** Remote session -> bottom navigation bar -> gesture helper

Available since RustDesk 1.4.3
ValuesDefaultExampleY, NN`show-virtual-joystick=Y`
**Note**: This option should be configured in **Default settings** rather than **Override settings**.

### allow-insecure-tls-fallback

By default, RustDesk verifies the server certificate for protocols using TLS.

With this option enabled, RustDesk will fall back to skipping the verification step and proceed in case of verification failure.

**Location**:

**Desktop** Settings â Network â Allow insecure TLS fallback
**Mobile** Settings â Allow insecure TLS fallback

Available since RustDesk 1.4.4
ValuesDefaultExampleY, NN`allow-insecure-tls-fallback=Y`