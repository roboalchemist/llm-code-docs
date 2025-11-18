# Source: https://docs.anchorbrowser.io/advanced/dedicated-sticky-ip.md

# Dedicated Sticky IP

> Reserve a fixed IP address for a specific profile.

A **Dedicated Sticky IP** ensures that a specific profile uses by default the same IP address, reserved exclusively for that profile. This is helpful when IP consistency is required across sessions.

<Steps>
  <Step title="Enable sticky IP in profile creation">
    Use the [Create Profile API](https://docs.anchorbrowser.io/api-reference/profiles/create-profile?playground=open) to create a profile with a dedicated sticky IP by setting:

    ```json  theme={null}
    {
      "dedicated_sticky_ip": true
    }
    ```

    This allocates a dedicated IP that is not shared with other profiles.
  </Step>

  <Step title="Start sessions with the reserved IP">
    Any browser session started using this profile will automatically use the reserved sticky IP.
  </Step>

  <Step title="Override the IP with a custom proxy (optional)">
    To override the default sticky IP, set the `proxy` field when using the [Start Browser Session API](https://docs.anchorbrowser.io/api-reference/browser-sessions/start-browser-session).
  </Step>
</Steps>
