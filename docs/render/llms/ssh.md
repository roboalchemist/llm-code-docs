# Source: https://render.com/docs/ssh.md

# SSH and Shell Access — Connect to your services from your terminal or the Render Dashboard.

You can initiate a shell session to your Render service from its *Shell* page in the [Render Dashboard](https://dashboard.render.com):

[image: Accessing a service via its Shell page in the Render Dashboard]

If your service is [scaled](scaling) to multiple instances, you can connect to a specific instance using the *Instance* dropdown.

You can also SSH into your services from the terminal after [completing setup](#ssh-setup).

## Compatible service types

Support for shell access varies by service type:

| Service type | Dashboard shell | SSH |
| --- | --- | --- |
| *Paid [web service](web-services)* | 🟢 | 🟢 |
| *[Private service](private-services)* | 🟢 | 🟢 |
| *[Background worker](background-workers)* | 🟢 | 🟢 |
| *[Cron job](cronjobs)* | 🟨 [See details.](#cron-job-connections) | ❌ |
| *[Free](free) web service* | ❌ | ❌ |
| *Other service types (static sites, datastores)* | ❌ | ❌ |

## SSH setup

### 1. Generate an SSH key pair

> *Skip this step if you already have an SSH key on your machine that you want to use.*

1. Run the following command to generate an Ed25519 key pair in the `~/.ssh` directory:

   ```shell
   ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519
   ```

   You can optionally use a different [key type](#supported-key-types).

2. The command prompts you to provide an optional passphrase for your private key (recommended for added security).

3. The command generates two files in your `~/.ssh` directory:

   - `~/.ssh/id_ed25519` (private key)
   - `~/.ssh/id_ed25519.pub` (public key)

> *Your private key is a secret credential. Don't share it with anyone.*
>
> To enable SSH access, you'll share the _public_ key with Render.

### 2. Add your public key to your Render account

1. Open your [Account settings page](http://dashboard.render.com/settings#ssh-public-keys) in the Render Dashboard.
2. Find the *SSH Public Keys* section and click *+ Add SSH Public Key*. The creation dialog appears.
3. Provide a descriptive *Name* for the key (e.g., "Personal Laptop").
4. Copy the full contents of your _public_ key file (ends in `.pub`) to your clipboard.

   On macOS, you can use the `pbcopy` command to copy the file to your clipboard:

   ```shell
   pbcopy < ~/.ssh/id_ed25519.pub
   ```

5. Paste your public key into the *Key* field:

   [image: Adding an SSH public key to your Render account]

6. Click *Add SSH Public Key* button to save your key.

All set! You're ready to [start an SSH session](#starting-an-ssh-session).

## Starting an SSH session

After completing [SSH setup](#ssh-setup), you can start SSH sessions from your terminal using the [Render CLI](cli), or by running the `ssh` command directly.

Select a method from the tabs below:

**Render CLI**

1. [Install and log in to the Render CLI](cli#setup) if you haven't already.
2. Run the following command:

   ```shell
   render ssh
   ```

   This opens an interactive menu that lists your workspace's SSH-compatible services.

3. Use the arrow keys to select a service and press *Enter*. The interactive menu closes and the SSH session starts.

To skip menu-based selection, you can include your service's ID directly in the `render ssh` command:

```shell
render ssh srv-abc123
```

**SSH command**

1. In the [Render Dashboard](https://dashboard.render.com), open the settings for the service you want to connect to.

2. Click the *Connect* dropdown in the upper right and select the *SSH* tab:

   [image: Obtaining a service's SSH command in the Render Dashboard]

> *Don't see the SSH tab?* The selected service is not SSH-compatible. See [Compatible service types](#compatible-service-types).

3. Copy the SSH command to your clipboard.

4. Paste the SSH command into your terminal and run it.

   ```shell
   ssh YOUR_SERVICE@ssh.YOUR_REGION.render.com
   ```

5. You might see a warning like this:

   ```
   The authenticity of host 'render.com (IP_ADDRESS)' can't be established.
   ED25519 key fingerprint is (SSH_KEY_FINGERPRINT)
   Are you sure you want to continue connecting (yes/no)?
   ```

   If you do, confirm that the fingerprint in the message matches Render’s
   [public key fingerprint](#renders-public-key-fingerprints) for your region. If it does, type `yes` to continue.

6. If you receive a "permission denied" message, see [Troubleshooting permission failures](#troubleshooting-permission-failures).

### Connecting to a specific instance

By default, SSH sessions connect to a random running instance of your service. To connect to a _specific_ instance, include that instance's 5-character slug in the hostname of your SSH command:

```shell{outputLines:1,3-4}
# Random instance
ssh srv-abc123@ssh.oregon.render.com

# Specific instance
ssh srv-abc123-d4e5f@ssh.oregon.render.com
```

As shown above, you append the instance slug to the service's ID (separated by a hyphen) to form the complete hostname.

Instance slugs are visible in your service's [logs](logging) and [application metrics](service-metrics#cpu-and-memory-usage). You cannot SSH into an instance that is no longer running.

### Troubleshooting permission failures

If you receive a "Permission denied" error, Render rejected the incoming SSH session. Take the following steps first to troubleshoot this issue:

#### Confirm which SSH key you're using

Add the "verbose" flag (`-v`) to your SSH command to get more details about which key is being used:

```shell{outputLines:2-9}
ssh -v YOUR_SERVICE@ssh.YOUR_REGION.render.com
[...]
debug1: identity file /Users/YOUR_NAME/.ssh/id_ed25519 type 3
debug1: identity file /Users/YOUR_NAME/.ssh/id_ed25519-cert type -1
[...]
debug1: Next authentication method: publickey
debug1: Offering public key: /Users/YOUR_NAME/.ssh/id_ed25519
[...]
Permission denied (publickey).
```

#### Confirm which keys are attached to your Render account

1. List any keys you have loaded into the [ssh-agent](https://en.wikipedia.org/wiki/Ssh-agent).

   ```shell
   ssh-add -l
   ```

   This should should print out a long string of numbers and letters.

   ```
   256 SHA256:SSH_KEY_FINGERPRINT YOUR_NAME@YOUR_HOST (ED25519)
   ```

2. Open your settings page in the [Dashboard](https://dashboard.render.com/) and find the list of SSH public keys.

3. Compare the list of SSH keys with the output from the `ssh-add` command.

If you don't see your public key listed, you can [add it to your account](#ssh-setup).

## Render's public key fingerprints

Public key fingerprints can be used to validate a connection to a remote server.

Render’s public SSH key fingerprints are as follows:

| Region | Fingerprint |
| --- | --- |
| *Oregon* | `SHA256:KkZPgnApmttFYSkdJsCi7B01sgZPMI6kY53MDbbanGM` |
| *Ohio* | `SHA256:kRDsLlrHqOyqso58sEKyO6ZFMPj7p24zfNxYJ42yXGI` |
| *Virginia* | `SHA256:NCpSwboPnqL/Nvyy2Qc8Kgzpc3P/f3w5wDphhc+UZO0` |
| *Frankfurt* | `SHA256:dBRrCEA0tBkvaYLzzDw/mzaANw6nUJO961Zx806spZs` |
| *Singapore* | `SHA256:CUlRyv4TZ0vmHwmhsJkII/pz2cO4IgvR+ykqnRsOQFs` |

You can also directly add Render's public keys to your `$SSH_DIR/known_hosts` file. Render's full set of entries is as follows:

```bash
# RENDER PUBLIC KEYS
# ------------------

# Oregon
ssh.oregon.render.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFON8eay2FgHDBIVOLxWn/AWnsDJhCVvlY1igWEFoLD2

# Ohio
ssh.ohio.render.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINMjC1BfZQ3CYotN1/EqI48hvBpZ80zfgRdK8NpP58v1

# Virginia
ssh.virginia.render.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ6uO0jKQX9IjefnLz+pxTgfPhsPBhNuvxmvCFrxqxAM

# Frankfurt
ssh.frankfurt.render.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILg6kMvQOQjMREehk1wvBKsfe1I3+acRuS8cVSdLjinK

# Singapore
ssh.singapore.render.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGVcVcsy7RXA60ZyHs/OMS5aQj4YQy7Qn2nJCXHz4zLA
```

## Usage details

### Supported key types

Render supports the following key types:

- `ed25519`
- `ecdsa`
- `rsa`

Render also supports U2F/FIDO hardware authenticated keys like a YubiKey.

- `ed25519-sk`
- `ecdsa-sk`

### Cron job connections

When you connect to a cron job from the Dashboard shell, Render spins up a new, temporary instance of the service and connects to it. This instance includes your cron job's latest build and configuration. It does _not_ automatically execute the cron job's command. After you close the shell session, Render deprovisions the instance.

It is not possible to connect to the actual cron job instances that run as part of your cron schedule.

### Automatic session closure

Render automatically closes a service's active SSH sessions in the following cases:

- The service is redeployed or restarted for any reason.
- Render is scheduled to perform maintenance on underlying infrastructure that enables SSH connections.
  - In this case, Render gives existing connections one hour before automatically closing them.

For long-running commands, consider spinning up a [one-off job](one-off-jobs) instead of SSHing into an active instance.

### Memory usage

SSH and dashboard shell sessions use the same memory pool that's allocated for your service instance. Using SSH requires about 2 MB of memory, plus about 3 MB for each active session (not including memory used by processes executed during the session).

As an example, let's say we SSH into one service instance from two different computers to run bash. In this case, memory usage would look like this:

- 8 MB for SSH
  - 2 MB for SSH access
  - 2x3 MB for the two SSH sessions
- 7 MB for bash
  - 2x3.5 MB for the two bash processes

Total memory usage in this case is about 15 MB.