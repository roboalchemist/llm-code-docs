# Source: https://rustdesk.com/docs/en/self-host/rustdesk-server-pro/installscript/windows/

# Windows Install (deprecated)

Note

Windows security policy is tricky, if this tutorial does not work for you, or you encounter unstable connection, please migrate to a Linux server.

Note

The GUI version, `RustDeskServer.setup.exe` has not been maintained any more, not recommended.

## Install

The Microsoft Visual C++ Redistributable is required to run rustdesk on Windows. You can download it here

- Get your license from https://rustdesk.com/pricing.html, check license page for more details.
- Download the the Windows installer from GitHub.
- Unzip the Windows installer.
- Run the Installer and follow the steps on screen. Or manually install with PM2 or NSSM.
- Once its completed open RustDesk Server.
- Follow the prompts as they guide you through the install.
- Click `Services` and then `Start`.
- Once the install is complete go to `http://youripaddress:21114`.
- Log in with the username `admin` and password `test1234`.
- Enter your license code purchased in step 1.

## Use IIS as Proxy

Please ensure `Dynamic Content Compression` is installed (this is an IIS Feature which can be installed with Server Roles).

- Open IIS (Or install it).
- Create a new website for RustDesk with the bindings (Ideally 443) and relevant certificate. Basic settings should point this to a blank folder. (If you use the default site, make sure there are no other files in the folder).
- On IIS, install Application Request Routing and URL Rewrite.

## Application Request Routing

- Under the IIS Server Host open Application Request Routing.
- Go to Server Proxy Settings.
- Enable proxy and all settings will appear, you can leave them as the defaults.
- Save the settings and we can go to the next step: URL Rewrite.

## URL Rewrite

- Open the site on IIS on the left pane and double-click on URL Rewrite.
- Click `Add rules`.
- Set up a new reverse proxy rule.
- Setup the local address (the 21114 address)
Inbound Rule â the RustDesk internal 21114 address
Outbound Rules â `From` is the RustDesk internal 21114 address and `To` is the external address.
Note: No http / https before the addresses â they are automatically handled. Also, ensure all the addresses are accessible both internally and externally.

## Compression

- Disable `Dynamic Content Compression`.

## Troubleshooting

If you have an error 500.52 add the mentioned variables: IIS acting as reverse proxy: Where the problems start.

You maybe need to change your SSL Settings to &ldquo;Require SSL â Ignore&rdquo;.