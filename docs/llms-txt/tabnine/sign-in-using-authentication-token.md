# Source: https://docs.tabnine.com/main/getting-started/install/client-setup-private-installation/sign-in-using-authentication-token.md

# Sign In Using Authentication Token

### Sign in to the Tabnine plugin using an authentication token <a href="#sign-in-to-the-tabnine-plugin-using-an-authentication-token" id="sign-in-to-the-tabnine-plugin-using-an-authentication-token"></a>

For some IDE setups, it's not possible to activate the Tabnine plugin via the regular flow.

This includes setups such as Remote SSH, Docker, or WSL where the browser isn't available on the remote machine.

In these cases, you can activate the Tabnine plugin by signing in using an authentication token.

{% tabs %}
{% tab title="VS Code" %}

1. Open the **Command Pallet**
2. Run: **Tabnine: Sign in using auth token**

<figure><img src="https://open-2c.gitbook.com/url/preview/site_xstLD/~gitbook/image?url=https%3A%2F%2F3652871471-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F03uIXF1SrI5fdiuQqdFr%252Fuploads%252Fgit-blob-91ed4a84a36c6244040172d07b15e56e20c63a90%252Fimage.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=13676d9c&#x26;sv=2" alt=""><figcaption></figcaption></figure>

1. The following popup will appear:

<figure><img src="https://open-2c.gitbook.com/url/preview/site_xstLD/~gitbook/image?url=https%3A%2F%2F3652871471-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F03uIXF1SrI5fdiuQqdFr%252Fuploads%252Fgit-blob-87be237e7591d6f4e7671ffd2eacfcaff32959c1%252Fimage%2520%2817%29.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=cdc8eb77&#x26;sv=2" alt=""><figcaption></figcaption></figure>

1. If you already have an authentication token, click **Sign In** and skip to the relevant step below
2. If you don't already have a token, click **Get auth token**
3. The browser will open with the following [screen](https://app.tabnine.com/auth/sign-in/manual) for signing up, which includes a secret personal authentication token:

<figure><img src="https://open-2c.gitbook.com/url/preview/site_xstLD/~gitbook/image?url=https%3A%2F%2F3652871471-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F03uIXF1SrI5fdiuQqdFr%252Fuploads%252Fgit-blob-842c222e8d305877c38cffce3e1c4b65c9e308e0%252Fimage.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=adaed71c&#x26;sv=2" alt=""><figcaption></figcaption></figure>

1. Copy the token and go back to your IDE.
2. Paste your authentication token in the following popup and click **Enter**

<figure><img src="https://open-2c.gitbook.com/url/preview/site_xstLD/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FYD9KAz4nlJYH8c5k1BCpQDqs-pnf-gqlJJv0MDZmnd8otSm7CvRZi32UaQxOF7wlWQZzv-G_XTUB7otAyqR7HRzPVwyVpgwHBsyoPEyspuWRPfV39ZlJ4s81sITxyes3Cqi1wRhPFkN3kiu5KwmVBgSAkw%3Ds2048&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=ed12f9ef&#x26;sv=2" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="JetBrains IDEs" %}

1. Click **double shift** do open the **Search Everywhere** window
2. Type **Tabnine: Sign in using auth token**

<figure><img src="https://open-2c.gitbook.com/url/preview/site_xstLD/~gitbook/image?url=https%3A%2F%2F3652871471-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F03uIXF1SrI5fdiuQqdFr%252Fuploads%252Fgit-blob-07c9da3c8118d0dc3442c02760d7e6c0cb22754e%252Fimage%2520%2822%29.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=abd8720&#x26;sv=2" alt=""><figcaption></figcaption></figure>

1. The following popup will appear

<figure><img src="https://open-2c.gitbook.com/url/preview/site_xstLD/~gitbook/image?url=https%3A%2F%2F3652871471-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F03uIXF1SrI5fdiuQqdFr%252Fuploads%252Fgit-blob-61bccc66b7f2df78859cc3ddb130c84dc87c4d92%252Fimage.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=c43efd77&#x26;sv=2" alt=""><figcaption></figcaption></figure>

1. If you already have an authentication token, click **Sign In** and skip to the relevant step below.
2. If you do not already have a token, click **Get auth token**
3. The browser will open with following [screen](https://app.tabnine.com/auth/sign-in/manual) (sign in if you are not), with a secret personal authentication token:

<figure><img src="https://open-2c.gitbook.com/url/preview/site_xstLD/~gitbook/image?url=https%3A%2F%2F3652871471-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F03uIXF1SrI5fdiuQqdFr%252Fuploads%252Fgit-blob-cac76885b4a0a3915e42d2ff3ef264de2294240f%252Fimage.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=118d36c3&#x26;sv=2" alt=""><figcaption></figcaption></figure>

1. Copy the token and go back to the IDE.
2. Paste your authentication token in the following popup and click **Enter**

<figure><img src="https://open-2c.gitbook.com/url/preview/site_xstLD/~gitbook/image?url=https%3A%2F%2F3652871471-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F03uIXF1SrI5fdiuQqdFr%252Fuploads%252Fgit-blob-62e11782b7b8b60afd9ea6c2a375deaad7e04de8%252Fimage.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=a8e76cbf&#x26;sv=2" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}
