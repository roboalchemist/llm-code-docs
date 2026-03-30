# Source: https://docs.salad.com/container-engine/explanation/container-groups/ssh-and-terminal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SSH & Terminal Access

*Last Updated: January 30, 2026*

SaladCloud provides two ways to access a shell inside your running container instances: a web-based terminal directly in
the Portal, and SSH access for connecting from your local machine or other SSH clients.

## SSH Access

Use SSH to open a shell on a running container instance after adding your public key in the SaladCloud Portal.

### 1. Create or Obtain an SSH Key

If you already have an SSH key pair, you can skip this step. To check for existing keys:

```bash  theme={null}
ls -la ~/.ssh/
```

Look for files named `id_ed25519.pub`, `id_rsa.pub`, or similar `.pub` files.

To create a new SSH key:

```bash  theme={null}
ssh-keygen -t ed25519 -C "you@example.com"
```

This creates `~/.ssh/id_ed25519` (private key) and `~/.ssh/id_ed25519.pub` (public key). Your public key will look
similar to this:

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHKz8vGk9XpFmEqTcvN7LMfPxWkR5yJQ2nBdW1cLmK4p you@example.com
```

### 2. Copy Your Public Key

```bash  theme={null}
cat ~/.ssh/id_ed25519.pub
```

### 3. Add the Key in the Portal

There are two ways to access the SSH key settings:

* Click your username in the upper-right corner and select **SSH Keys**, or
* Click **SSH Keys** in the left sidebar menu

Paste your public key into the field and save it.

<img src="https://mintcdn.com/salad/NZr5UzWB2OULDSAI/container-engine/images/ssh-access-1.png?fit=max&auto=format&n=NZr5UzWB2OULDSAI&q=85&s=4ace6127fd5bb134f44a9863c42bfb8f" alt="" data-og-width="977" width="977" data-og-height="510" height="510" data-path="container-engine/images/ssh-access-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/NZr5UzWB2OULDSAI/container-engine/images/ssh-access-1.png?w=280&fit=max&auto=format&n=NZr5UzWB2OULDSAI&q=85&s=daccc8ca7ff875f3eae3a02be07ee3f7 280w, https://mintcdn.com/salad/NZr5UzWB2OULDSAI/container-engine/images/ssh-access-1.png?w=560&fit=max&auto=format&n=NZr5UzWB2OULDSAI&q=85&s=e6a9dcfae751af71d45bf1e6b75004f5 560w, https://mintcdn.com/salad/NZr5UzWB2OULDSAI/container-engine/images/ssh-access-1.png?w=840&fit=max&auto=format&n=NZr5UzWB2OULDSAI&q=85&s=ea88fcdb5ae1ca0e2ab7114b6efdb9f7 840w, https://mintcdn.com/salad/NZr5UzWB2OULDSAI/container-engine/images/ssh-access-1.png?w=1100&fit=max&auto=format&n=NZr5UzWB2OULDSAI&q=85&s=902b11842ce7ab0cf04392881dd38011 1100w, https://mintcdn.com/salad/NZr5UzWB2OULDSAI/container-engine/images/ssh-access-1.png?w=1650&fit=max&auto=format&n=NZr5UzWB2OULDSAI&q=85&s=91812b9d7481cab1609f7efb0008bf20 1650w, https://mintcdn.com/salad/NZr5UzWB2OULDSAI/container-engine/images/ssh-access-1.png?w=2500&fit=max&auto=format&n=NZr5UzWB2OULDSAI&q=85&s=5ec24db374f625f99d453599057aeb5d 2500w" />

### 4. Connect to a Container Instance

1. Open your container group in the Portal and click on a running instance.

2. You will see an SSH command displayed in a text box above the terminal. Command will look something like this:

   ```bash  theme={null}
   ssh root@<hostname> -p <port>
   ```

3. Copy the command and paste it into your terminal.

4. The Portal also displays the key fingerprint for verification, so you can confirm you're connecting with the correct
   key.

SSH automatically tries default key files from `~/.ssh/` (such as `id_ed25519`, `id_rsa`, `id_ecdsa`), so the command
shown in the Portal works without modification for most users.

If your key has a custom name or is stored in a non-standard location, add the `-i` flag to specify your key name and
location:

```bash  theme={null}
ssh -i ~/.ssh/my_custom_key root@<hostname> -p <port>
```

## Terminal Access

The web-based terminal provides quick access directly from your browser without any SSH setup.

1. Open the [SaladCloud Portal](https://portal.salad.com) and navigate to your container group.
2. Click on a running instance.
3. Click on the **Terminal** tab to open an interactive shell.
