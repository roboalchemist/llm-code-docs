# Source: https://docs.icepanel.io/other-information/troubleshooting.md

# Troubleshooting

## Network error

1. Ensure you have a working internet connection.
2. Check the [IcePanel status](https://status.icepanel.io) website for any downtime or planned maintenance.
3. If you have the [Allow CORS](https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf), [uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) or other Chrome plugins that modify network requests, make sure IcePanel is added to your whitelist.
4. If you have a corporate firewall make sure the IcePanel REST API is whitelisted at `api.icepanel.io`.

### Opening IcePanel shows the loading screen forever

1. Ensure you have a working internet connection.
2. Check the [IcePanel status](https://status.icepanel.io) website for any downtime or planned maintenance.
3. If you're on a corporate network, try a private network (organizations often block our WebSocket)
   * If this fixes the problem you'll need to ask your network administrator to whitelist our WebSocket connection for `wss://app.icepanel.io/real-time`

### Error logging into SSO (auth/web-storage-unsupported)

This happens if the browser does not support web storage or if the user disables them.

This can happen if Chromes "Block third-party cookies" option is enabled. Either disable this or add `https://app.icepanel.io` as an exception in the section below.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FTnmdQ9FA0l5janUAdmRH%2Fchrome-auth-cookie-exception%20(1).png?alt=media&#x26;token=55862775-2ffe-41bc-9686-120618ccd9bc" alt=""><figcaption><p>Chrome auth cookie exception</p></figcaption></figure>

### Error loading diagram (WebGL unsupported in this browser)

Ensure the `Use graphics acceleration when available` option is enabled in your web browser.

### Error 'CanvasRenderer is not yet implemented'

To solve this error, make sure Graphics Acceleration is enabled in your browser.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FJF3Sqm7S6ulTLbOTvdEz%2Fimage.png?alt=media&#x26;token=1e9dd6e5-ad68-4e48-a4af-bff3299c7cd4" alt=""><figcaption><p>Graphics Acceleration</p></figcaption></figure>

### Error trying to create diagrams via API

You need to ensure the position of the x and y axes is a multiple of 4. Otherwise, you will receive the error `Rect position not in grid was specified.`
