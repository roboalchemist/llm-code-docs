# Source: https://docs.safetycli.com/safety-docs/support/headless-authentication.md

# Headless Authentication

For users who wish to perform scans on machines with no browser, e.g. EC2 instances, it is possible to authenticate the scan session by leveraging another machine with a browser installed.&#x20;

1. Start by installing the latest version of Safety:

```
pip install safety==3.4.0
```

2. When installed, start by authenticating the session using the new headless option.

```
safety auth login --headless
```

3. You should see the following: “Running in headless mode. Please copy and open the following URL in a browser. Copy and paste this url into your browser.”&#x20;

* Copy and paste the URL from the Terminal into a browser on another machine that does have one.
* Once authenticated on that browser a code will show on the success screen.
* Click the JSON code on the screen. This will copy the code to the clipboard.
* Paste that JSON code string into the original prompt in your Terminal.
* The Safety session should now be authenticated on the machine without a browser installed.&#x20;
