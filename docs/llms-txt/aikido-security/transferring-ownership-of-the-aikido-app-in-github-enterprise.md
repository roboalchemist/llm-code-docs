# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-github-enterprise/transferring-ownership-of-the-aikido-app-in-github-enterprise.md

# Transferring Ownership of the Aikido App in Github Enterprise (Cloud & Server)

When you create the Aikido GitHub App inside your GitHub Enterprise environment, it is set up under the account of the user performing the installation. This follows the default GitHub flow when no prior ownership choice is known.

You can transfer the app to any other user or organization in your GitHub Enterprise Server environment at any time. This has no impact on how the app operates.

To transfer ownership, follow the steps below.

{% stepper %}
{% step %}

### Go to the Github App's developer Settings page

In your GitHub Server environment, navigate to Settings > Developer Settings > GitHub Apps.\
Click on "Edit".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FRSQv666dC74rFZh5RkqE%2FScherm%C2%ADafbeelding%202025-12-02%20om%2010.15.04.png?alt=media&#x26;token=d4f5f6f6-d07e-4c19-83dc-435a7e1e1ccb" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Go to Advanced settings

In the left-hand navigation, go to the "Advanced" settings and scroll all the way down on the page until you see this section. \
\
Click on "Transfer ownership"<br>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F6GK1ce9BbATKp2X0woxG%2FScherm%C2%ADafbeelding%202025-12-02%20om%2010.17.15.png?alt=media&#x26;token=7ab9f996-e070-4894-a6eb-97a585c0d7e2" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Transfer ownership

Once you've clicked the button, you need to confirm the name of the App, and then you can select the organization or user to which you want to transfer the ownership.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FptOiNtbkk5MXLSo4EBEr%2FScherm%C2%ADafbeelding%202025-12-02%20om%2010.17.43.png?alt=media&#x26;token=1fad0324-3086-473c-a515-4cda2a9a1f64" alt=""><figcaption></figcaption></figure>

{% endstep %}

{% step %}

### Success

The App is now transferred to the new owner.
{% endstep %}
{% endstepper %}
