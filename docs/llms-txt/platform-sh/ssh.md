# Source: https://docs.upsun.com/development/ssh.md

# Connect securely with SSH

When you interact with a deployed environment, you need to guard your connection against unauthorized access.
Use Secure Shell (SSH) to provide a secure channel.

You can securely log in to your deployed app to troubleshoot and read logs.
And create a tunnel to export data through.
And interact with your project through the CLI.
All secured through SSH.

## Connect to apps

To connect to an app securely with SSH, follow two steps.

### 1. Authenticate with the CLI

To authenticate with the CLI:

1. Install the [Upsun CLI](https://docs.upsun.com/administration/cli.md).
2. Run `upsun login`.
3. In the open browser window, log in with your Upsun account credentials.
   (This webpage is encrypted with [HTTPS](https://docs.upsun.com/define-routes/https.md), making it secure.)
4. Authorize the CLI to use your account.

A certificate gets stored in your local SSH configuration.
The certificate is automatically cycled every hour for a new certificate as long as your session is active.

If you are inactive for an extended period,
your certificate expires and you are asked to login again the next time you use a command that requires authentication.

You are now ready to run CLI commands and connect to an environment.

### 2. Connect to an app with SSH

To access an app in a given environment via the CLI, run the following command:

```bash
upsun ssh --project <PROJECT_ID> --environment <ENVIRONMENT_NAME> --app <APPLICATION_NAME>
```

Replace each of ``<PROJECT_ID>``, ``<ENVIRONMENT_NAME>``, and ``<APPLICATION_NAME>`` with the values you want to access.
To find these values in the Console,
navigate to the environment you want to access and click **SSH** in the top right-hand corner.

Alternatively, just run `upsun ssh` and select the values from each list presented to you.

Once you've connected, you get a welcome message detailing which environment you're connected to.

Now you can interact with the environment as you want.
Note that your app's file system is read-only,
except for any [mounts you've defined](https://docs.upsun.com/create-apps/image-properties/mounts.md).

## Connect to services

To connect to a service, you need the [service credentials](https://docs.upsun.com../../add-services.md#connect-to-a-service).
Then you can connect either with a [direct tunnel](#use-a-direct-tunnel) or a [tunnel in your app](#use-an-app-tunnel).

### Use a direct tunnel

To open SSH tunnels for all of your services, run the following command:

```bash
upsun tunnel:open
```

You get output similar to the following:

```bash
SSH tunnel opened to database at: http://127.0.0.1:30000

Logs are written to: ~/.upsun/tunnels.log

List tunnels with: upsun tunnels
View tunnel details with: upsun tunnel:info
Close tunnels with: upsun tunnel:close

Save encoded tunnel details to the PLATFORM_RELATIONSHIPS variable using:
  export PLATFORM_RELATIONSHIPS="$(platform tunnel:info --encode)"
```

Use the returned host (in this case `http://127.0.0.1:30000`) for your connection
and fill in the details with the rest of your [service credentials](https://docs.upsun.com../../add-services.md#connect-to-a-service).

The `tunnel:open` command connects all relationships defined in your [app configuration](https://docs.upsun.com../../create-apps.md).

To open only one connection when you have multiple relationships defined, run `tunnel:single`.
By default, this opens a tunnel at `http://127.0.0.1:30000`.
You can specify the port for the connection using the `--port` flag.

### Use an app tunnel

Many database applications (such as MySQL Workbench) support establishing their own SSH tunnel.
You need to use [SSH keys](https://docs.upsun.com/development/ssh/ssh-keys.md) for authentication.
Consult the documentation for your application for how to enter SSH credentials.

#### Get SSH connection details

To get the host and username for connections, follow these steps:

You get output similar to the following:

```bash {}
jyu7waly36ncj-main-7rqtwti--app@ssh.us.upsun.com
```

 - Navigate to the environment you want to connect to.
 - Click **SSH** in the top right-hand corner.
 - You get output similar to the following: 
``jyu7waly36ncj-main-7rqtwti--app@ssh.us.upsun.com``

The host is everything after the `@` and the username is what's before it.
In this case, the host is `ssh.us.upsun.com` and the username is `jyu7waly36ncj-main-7rqtwti--app`.
The host is the same for the entire project, while the username varies by environment.

To connect to a service, fill in the details with the rest of your [service credentials](https://docs.upsun.com../../add-services.md#connect-to-a-service).

## Alternative authentication methods

There are three basic ways to authenticate with Upsun:

* [Through the CLI](#1-authenticate-with-the-cli)
  * The fastest and easiest method.
  * Supports multifactor authentication.
  * Automatically generates new certificates to keep your connection safe.
  * Necessary when using the CLI and when your organization has multifactor authentication set up.
* [Using SSH keys](https://docs.upsun.com/development/ssh/ssh-keys.md)
  * Requires more setup on your part.
  * Represents only a single authentication method.
  * Requires you to regularly change the keys to maintain security.
  * Useful for checking out code as part of an automated process.
* [Using API tokens](https://docs.upsun.com../../administration/cli/api-tokens.md)
  * Good for letting automation tools use the CLI.
  * Requires you to regularly change the tokens to maintain security.

## SSH into an MFA-protected environment

For enhanced security, as an organization owner or admin user,
you can [enforce multifactor authentication (MFA) within your organization](https://docs.upsun.com/administration/security/mfa.md#enforce-mfa-within-your-organization).

As a project contributor, if you haven't enabled MFA on your user account and SSH into an environment that is protected by MFA,
you get an error message. See how you can [troubleshoot that error message](https://docs.upsun.com/development/ssh/troubleshoot-ssh.md#mfa-related-error-message).

