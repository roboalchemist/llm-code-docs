# Source: https://fly.io/docs/getting-started/launch-demo

Title: Launch a demo app

URL Source: https://fly.io/docs/getting-started/launch-demo

Markdown Content:
[Docs](https://fly.io/docs/)[Getting started](https://fly.io/docs/getting-started)Launch a demo app![Image 1: Illustration by Annie Ruygt of a rocket on the launch pad](https://fly.io/static/images/launch-demo.png)
In this step-by-step guide you’ll use Fly Launch to deploy a simple “hello fly” demo app to Fly.io.

The first step is installing all the tools you need to work with Fly Launch. Which is one tool: flyctl.

[](https://fly.io/docs/getting-started/launch-demo#1-install-flyctl)1. Install flyctl
-------------------------------------------------------------------------------------

flyctl is a command-line utility that lets you work with Fly.io using `fly` commands, from creating your account to deploying your applications. It runs on your local device so you’ll want to install the version that’s appropriate for your operating system.

### [](https://fly.io/docs/getting-started/launch-demo#macos) macOS

If you have the [Homebrew](https://brew.sh/) package manager installed, flyctl can be installed by running:

```
brew install flyctl
```

If not, you can run the install script:

```
curl -L https://fly.io/install.sh | sh
```

If you used curl to install flyctl, then you need to add the flyctl directory to your shell rc file. Check the output of the install script for the entries to copy and paste into the file. Now you can use the `fly` command from any directory.

### [](https://fly.io/docs/getting-started/launch-demo#linux) Linux

Run the install script:

```
curl -L https://fly.io/install.sh | sh
```

### [](https://fly.io/docs/getting-started/launch-demo#windows) Windows

Run the PowerShell install script:

```
pwsh -Command "iwr https://fly.io/install.ps1 -useb | iex"
```

If you encounter an error saying the `pwsh` command is not found, `powershell` can be used instead, though we recommend [installing the latest version of PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows).

[](https://fly.io/docs/getting-started/launch-demo#2-sign-up-or-sign-in)2. Sign up or sign in
---------------------------------------------------------------------------------------------

Sign up for an account or [sign in](https://fly.io/docs/getting-started/launch-demo#sign-in-to-your-flyio-account) to your existing account.

### [](https://fly.io/docs/getting-started/launch-demo#sign-up-for-a-fly-io-account)Sign up for a Fly.io account

If it’s your first time using Fly.io, you’ll need to create an account. To sign up, run:

```
fly auth signup
```

This will take you to the sign-up page where you can use your email address, your Google account, or your GitHub account to create a Fly.io account. When you sign up with GitHub, we’ll send you a confirmation email with a link to set a password; you’ll need a password so we can actively verify that it’s you for some Fly.io operations.

**Note:** At some point, you’ll be prompted for credit card payment information. New accounts start on our Pay As You Go plan. See [Pricing](https://fly.io/docs/about/pricing) and [Billing](https://fly.io/docs/about/billing/) for more details.

After signing up you’ll be returned to your command line, ready to use Fly.io.

### [](https://fly.io/docs/getting-started/launch-demo#sign-in-to-your-fly-io-account)Sign in to your Fly.io account

If you already have a Fly.io account, all you need to do is sign in with flyctl. To sign in, run:

```
fly auth login
```

When your browser opens to the Fly.io sign-in screen, enter your user name and password to sign in. If you signed up with GitHub, then click `Sign in with GitHub` to sign in.

After logging in you’ll be returned to your command line, ready to use Fly.io.

Microsoft WSL users may need to run the following command, which creates a symbolic link that allows the browser to open:

`ln -s /usr/bin/wslview /usr/local/bin/xdg-open`

[](https://fly.io/docs/getting-started/launch-demo#3-launch-the-demo-app)3. Launch the demo app
-----------------------------------------------------------------------------------------------

Fly Launch helps you quickly deploy almost any kind of app using a Docker image. For this example, you’ll use our pre-built Docker image, `flyio/hellofly:latest`, to create and deploy the demo app.

Running `fly launch` to create a new app generates a [`fly.toml` config file](https://fly.io/docs/reference/configuration/) with some useful defaults that you can tweak through a web interface before deploying the app. When you run a command post-deploy, flyctl looks for a `fly.toml` file to get the app name and the configuration to apply.

To create the demo app, run:

```
fly launch --image flyio/hellofly:latest
```

You’ll get a summary of the defaults for your app. For example:

```
Using image flyio/hellofly:latest
Creating app in /Users/username/my-app-name
We're about to launch your app on Fly.io. Here's what you're getting:

Organization: MyName                 (fly launch defaults to the personal org)
Name:         my-app-name            (derived from your directory name)
Region:       Secaucus, NJ (US)      (this is the fastest region for you)
App Machines: shared-cpu-1x, 1GB RAM (most apps need about 1GB of RAM)
Postgres:     <none>                 (not requested)
Redis:        <none>                 (not requested)

? Do you want to tweak these settings before proceeding? (y/N)
```

Fly launch creates an app name by appending a random name to your project directory name. App names must be globally unique.

To change any settings, type `y` at the prompt to open the Fly Launch page, then click **Confirm Settings** to confirm and deploy the demo app.

Or just type `n` to accept the default and deploy the app.

Example `fly launch` output:

```
Created app 'my-app-name' in organization 'personal'
Admin URL: https://fly.io/apps/my-app-name
Hostname: my-app-name.fly.dev
Wrote config file fly.toml
Validating /Users/username/my-app-dir/fly.toml
Platform: machines
✓ Configuration is valid
==> Building image
Searching for image 'flyio/hellofly:latest' remotely...
image found: img_z1nr0lpjz9v5q98w

Watch your deployment at https://fly.io/apps/my-app-name/monitoring

Provisioning ips for my-app-name
  Dedicated ipv6: 2a09:8280:1::42:a8f4
  Shared ipv4: 66.241.124.213
  Add a dedicated ipv4 with: fly ips allocate-v4

This deployment will:
 * create 2 "app" machines

No machines in group app, launching a new machine
Creating a second machine to increase service availability
Finished launching new machines
-------
NOTE: The machines for [app] have services with 'auto_stop_machines = true' that will be stopped when idling
-------
Visit your newly deployed app at https://my-app-name.fly.dev/
```

[](https://fly.io/docs/getting-started/launch-demo#4-check-your-apps-status)4. Check your app’s status
------------------------------------------------------------------------------------------------------

After the app is deployed, use the `fly status` command to get the basic details about your new app. For example:

```
fly status
```

```
App
  Name     = hellofly          
  Owner    = personal       
  Hostname = hellofly.fly.dev
  Image    = flyio/hellofly:latest

Machines
PROCESS ID              VERSION REGION  STATE   ROLE   CHECKS   LAST UPDATED
app     148e453b7d7289  1       ord     started                 2023-05-17T17:39:37Z
app     5683d311c3228e  1       ord     stopped                 2023-05-17T17:38:44Z
```

In this example, the app has a DNS hostname of `hellofly.fly.dev`. The app has two Machines running in the ord (Chicago) region. We recommend running at least two Machines to improve availability.

[](https://fly.io/docs/getting-started/launch-demo#5-visit-your-app)5. Visit your app
-------------------------------------------------------------------------------------

You can connect to your deployed app with the `fly apps open` command, which opens a browser to `https://<my-app-name>.fly.dev/` for a secure connection.

You’ve successfully launched your first app on Fly.io!

For fun, add `/<your-name>` to `fly apps open` and your name will be appended to the app’s path to add an extra greeting from the hellofly application.

```
fly apps open /fred
```

```
opening https:http://hellofly.fly.dev/fred ...
```

You just deployed an app on Fly.io!

[](https://fly.io/docs/getting-started/launch-demo#deploy-changes)Deploy changes
--------------------------------------------------------------------------------

You probably don’t need to make any changes to our demo app. But when you do make changes to an app on Fly.io, deploy a new release with:

```
fly deploy
```

Now that you have a working demo app, learn [what you can do with Fly Launch](https://fly.io/docs/launch/).

[](https://fly.io/docs/getting-started/launch-demo#delete-the-demo-app)Delete the demo app
------------------------------------------------------------------------------------------

When you’re done playing with the demo app, delete it so you’re not using unnecessary resources:

```
fly apps destroy
```

[](https://fly.io/docs/getting-started/launch-demo#grow-and-scale)Grow and scale
--------------------------------------------------------------------------------

Read about some of the ways you can increase availability, capacity, and performance with Fly.io:

*   Follow the blueprint for [extra Machines for more resilient apps](https://fly.io/docs/blueprints/resilient-apps-multiple-machines/)
*   Read up on [App availability and resiliency](https://fly.io/docs/reference/app-availability/)
*   [Autoscale Machines based on load or custom metrics](https://fly.io/docs/reference/autoscaling/)
*   [Scale Machine CPU and RAM](https://fly.io/docs/apps/scale-machine/)
*   [Scale Machine count](https://fly.io/docs/apps/scale-count/)
*   Try out [Fly GPUs](https://fly.io/docs/gpus/)
