# Source: https://help.aikido.dev/pentests/setting-up-authenticated-testing/oauth0-configuration.md

# Auth0 Configuration

The pentesting agents share session state across multiple instances. To ensure this works correctly, apply the following settings in Auth0.

{% stepper %}
{% step %}

#### Open Application Settings

Navigate to Applications → \[Your Application] → Settings.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F3OpINoGy0z9M7NS5fMk4%2Fimage.png?alt=media&#x26;token=2f24c860-1ff0-4305-80cd-66669cff3512" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Disable Refresh Token Rotation

[Refresh token rotation](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-13#section-4.12) issues a new refresh token on each token exchange. This interferes with the agents’ shared-session model and must be disabled.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FzoOGmfxh6c6li0FOn3eN%2Fimage.png?alt=media&#x26;token=b7eaa56c-6f1e-46ef-8276-916580c38bef" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Configure Refresh Token Lifetime

Configure the refresh token lifetime to a sufficiently long duration (recommended: greater than 7200 seconds) to reduce the frequency of agent re-authentication during execution.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F48SeruDqfQxoKYOaC2jh%2Fimage.png?alt=media&#x26;token=6441d69b-4b7b-4c8b-819d-317f5f26832a" alt=""><figcaption></figcaption></figure>

{% endstep %}
{% endstepper %}
