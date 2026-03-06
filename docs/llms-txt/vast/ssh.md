# Source: https://docs.vast.ai/documentation/instances/connect/ssh.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# SSH Connection

> Learn how to securely connect to Vast.ai instances using SSH. Generate keys, establish connections, use port forwarding, and integrate with VS Code.

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Connect to Vast.ai Instances via SSH",
  "description": "A comprehensive guide to securely connecting to Vast.ai instances using SSH including generating SSH keys, adding keys to your account, establishing connections, using tmux, port forwarding, SCP/SFTP file transfer, VS Code integration, and troubleshooting.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Generate SSH Key Pair",
      "text": "Generate an SSH key pair using 'ssh-keygen -t ed25519 -C \"your_email@example.com\"' in your terminal. This creates two files: id_ed25519 (private key - keep safe) and id_ed25519.pub (public key - safe to share). Alternatively, use the Vast CLI with 'vastai create ssh-key --api-key YOUR_API_KEY' to generate and automatically register keys."
    },
    {
      "@type": "HowToStep",
      "name": "Add Public Key to Vast Account",
      "text": "Copy your public key using 'cat ~/.ssh/id_ed25519.pub' (Linux/Mac) or 'Get-Content $env:USERPROFILE\\.ssh\\id_ed25519.pub' (Windows PowerShell). Add it to your Vast account at cloud.vast.ai/manage-keys/. New keys only apply to instances created after adding."
    },
    {
      "@type": "HowToStep",
      "name": "Start Instance and Get Connection Details",
      "text": "Create a new instance with SSH launch mode. Once the instance is running, click the SSH icon on the instance card to view your connection command which includes the port, IP address, and optional port forwarding setup."
    },
    {
      "@type": "HowToStep",
      "name": "Connect via SSH",
      "text": "Enter the SSH connection command in your terminal (e.g., 'ssh -p 20544 root@142.214.185.187 -L 8080:localhost:8080'). Accept the host key fingerprint when prompted. You'll be placed into a tmux session by default for reliability."
    },
    {
      "@type": "HowToStep",
      "name": "Use Additional Features (Optional)",
      "text": "Use tmux commands (Ctrl+b+c for new window, Ctrl+b+n to cycle). Set up SSH local port forwarding with -L flags to access remote ports locally. Transfer files with SCP ('scp -P PORT file root@IP:/path') or SFTP ('sftp -P PORT root@IP'). Integrate with VS Code using the Remote-SSH extension."
    }
  ]
})
}}
/>

## About SSH

**SSH (Secure Shell)** is a protocol for safely connecting to remote servers. It encrypts your connection so you can:

* Log in securely
* Run commands remotely
* Transfer files without exposing your data

<Note>
  Vast.ai instances are configured to accept keys only - Password authentication is disabled for improved security.
</Note>

## Quick start: Generate and add your SSH key to your Vast account

<Tabs>
  <Tab title="Terminal">
    **1. Generate a SSH key pair in your terminal**

    <CodeGroup>
      ```bash Bash theme={null}
      ssh-keygen -t ed25519 -C "your_email@example.com"
      ```

      ```powershell PowerShell theme={null}
      ssh-keygen -t ed25519 -C "your_email@example.com"
      ```
    </CodeGroup>

    1. Creates two files (by default in \~/.ssh/):
       * id\_ed25519 → your **private key** (keep safe, never share).
       * id\_ed25519.pub → your **public key** (safe to share, add to servers).
    2. -C "[your\_email@example.com](mailto:your_email@example.com)" is optional. Whatever you put there is stored as a comment in the public key file (e.g., id\_ed25519.pub). It's just for identification (helpful if you use multiple keys), not for security.

    <Note>
      When you run ssh-keygen -t ed25519 in **Windows PowerShell**, the keys are created in your Windows user profile folder:
      `C:\Users\<YourUsername>\.ssh\`
    </Note>

    **2. Copy your public key.**

    <CodeGroup>
      ```bash Bash theme={null}
      # Print the public key
      cat ~/.ssh/id_ed25519.pub
      ssh-ed25519 AAAAC3NzaC1lZ9DdI1NTE5AAAAIHWGYlMT8CxcILI/i3DsRvX74HNChkm4JSNFu0wmcv0a
      ```

      ```powershell PowerShell theme={null}
      # Print the public key
      Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
      ssh-ed25519 AAAAC3NzaC1lZ9DdI1NTE5AAAAIHWGYlMT8CxcILI/i3DsRvX74HNChkm4JSNFu0wm
      ```
    </CodeGroup>

    **3. Add it in your** [**vast account**](https://cloud.vast.ai/manage-keys/)

        <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0c4875e49e2b1250de56ca5d06c8dd8a" alt="" data-og-width="914" width="914" data-og-height="684" height="684" data-path="images/instances-sshscp.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=ce25808c68ef5747ae61afc47e21dbac 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=ad998abfde5ababac4ce81f09fd2d465 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=d02a30b53bd09b1014350478397dece5 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=8154e85ec34d201cde1ae4647f334bec 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6577c4d72389e767fb8ffe14e92167f8 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7e4c0d56416402102e8e115bc9c481e6 2500w" />
  </Tab>

  <Tab title="Vast CLI">
    **Add & Generate SSH Key (using** [**Vast CLI**](/cli/get-started)**)**

    1. **Install Vast CLI:**

       <CodeGroup>
         ```bash Bash theme={null}
         pip install vastai
         ```

         ```powershell PowerShell theme={null}
         py -m pip install vastai
         # or
         python -m pip install vastai
         ```
       </CodeGroup>

    2. **Generate an API key in your vast account:**
       1. Open [CLI page](https://cloud.vast.ai/cli/)
       2. Create an API key
          <Frame caption="API Key creation">
              <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-2.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=b87717158bb150f91e707186ee5e3d0f" alt="API Key creation" data-og-width="800" width="800" data-og-height="316" height="316" data-path="images/instances-sshscp-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-2.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=142b3c9d5f6649159213ffd6808b72dd 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-2.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=00b017024671fc23e9ff633b929ad068 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-2.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=29ff3c6567e5eb5fc92198a007d2cbb8 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-2.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=cff4606483c2ce7b077be309ed80af02 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-2.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=b154d75102218364a8a476b999b003dd 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-2.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=5959f2128d22d7794176c4fa391d30dd 2500w" />
          </Frame>

    3. **Generate a new SSH key pair** (you will need your vast API key):

       <CodeGroup>
         ```cli CLI theme={null}
         vastai create ssh-key --api-key YOUR_API_KEY
         ```

         ```cli CLI theme={null}
         vastai set api-key YOUR_API_KEY
         vastai create ssh-key
         ```
       </CodeGroup>

    * Saves keys as \~/.ssh/id\_ed25519 (private) and \~/.ssh/id\_ed25519.pub (public).
    * Backs up existing keys as .backup\_\[timestamp].
    * Keys are stored in your Vast account and used for new instances.
  </Tab>
</Tabs>

<Warning>
  * Adding a key to your account keys only applies to **new instances**.
  * Existing instances will **not** get the new key automatically. To add a key, use the **instance-specific SSH interface**.
  * For **VM instances**, changing keys requires recreating the VM.
</Warning>

## Connecting to your Instance

Start a new instance and click the SSH icon to see your connection information.

<Frame caption="Terminal Connection Options">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-3.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0baecee39ed1714254241d265a1583ef" alt="Connection details" data-og-width="1063" width="1063" data-og-height="453" height="453" data-path="images/instances-sshscp-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-3.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=23a7cc28f35a45da60ae7bac6851c5c3 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-3.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=55d399312c5cd759898b27d23d80fd05 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-3.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=46cf12ad1ed7a5fa4dc4e0f377c64059 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-3.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=8a954169f77ccb3e9ff2ce5d095d00e8 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-3.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=8d694128da14e5c0540821be56579377 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-3.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7cfb49180130e1d6dd523d2d90c9fe99 2500w" />
</Frame>

Now you can enter the connection command string into your terminal

```bash Bash theme={null}
ssh -p 20544 root@142.214.185.187 -L 8080:localhost:8080

The authenticity of host '[142.214.185.187]:20544 ([142.214.185.187]:20544)' can't be established.
ED25519 key fingerprint is SHA256:WTUphznpN0zikMp+L5EtZpiCH6EeZ2PA/7+DSXDRjT0.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

You should now see a screen similar to this. You will, by default, be placed into a tmux session.

<Frame caption="Connected to Instance">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-4.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=e3dadd004d54ec00fbe7236860f5adc2" alt="Instance SSH session" data-og-width="1254" width="1254" data-og-height="464" height="464" data-path="images/instances-sshscp-4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-4.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=a185fcc096f446ee40f48d6bc58a8871 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-4.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=fabdfe7e040ea540d21dc4c552966358 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-4.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=3d35d7fb1b7d2d5a1bd7731a02d5dff2 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-4.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=e259ec3f325fa860ba277948a5481ce8 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-4.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=53eb278140b2d8dd6507121fcaada6ee 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-4.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=29713333a4bf70aac4f71d5d96fb8bee 2500w" />
</Frame>

### Direct vs Proxy Connections

Vast offers both proxy (default) and direct connection methods for SSH:

* **Proxy SSH**: Works on all machines, slower for data transfer, uses Vast proxy server
* **Direct SSH**: Requires machines with open ports, faster and more reliable, preferred method

## Tmux

We connect you to a tmux session by default for reliability and to prevent unintentional termination of foreground processes. You can create a new bash terminal window with `ctrl+b` + `c`. Cycle through your windows with `ctrl+b` + `n`

There is an excellent guide for getting to grips with tmux at [https://tmuxcheatsheet.com](https://tmuxcheatsheet.com/)

If, however, you would prefer to disable TMUX, you can apply the following either in a terminal or from your template's on-start section.

```text Text theme={null}
touch ~/.no_auto_tmux
```

## SSH Local Port Forwarding

An often overlooked feature of SSH is its ability to forward local ports to another machine. When you access a server remotely over SSH, you can make ports from the remote machine available as if they were listening on your own device. This is a secure alternative to opening ports on the public interface as all data is transported over the SSH connection.

```bash Bash theme={null}
ssh -p 1234 root@180.123.123.123 -L 8080:localhost:8080 -L 5000:localhost:5000
```

This SSH command connects to the remote instance and sets up **local port forwarding** (SSH tunneling):

**Connection details:**

* Connects to IP 180.123.123.123 as user root
* Uses port 1234 instead of the default SSH port 22

**Port forwarding (the key part):**

* `-L 8080:localhost:8080` - Creates a tunnel so when you access localhost:8080 on your local machine, it forwards to port `8080` on the remote server
* `-L 5000:localhost:5000` - Same thing for port `5000`

You can repeat the `-L` arguments to forward as many ports as you need.

**What this means:** After connecting, you can open your web browser and go to [https://localhost:8080](https://localhost:8080) or [http://localhost:5000](http://localhost:5000) on your local computer, and you'll actually be accessing services running on those ports on the remote server. It's like creating secure "tunnels" through the SSH connection to reach applications on the remote machine that might not be directly accessible from the internet.

## SSH Alternative - Jupyter Terminal

As a simple alternative to SSH, you might like to consider Jupyter Terminal instead. All instances started in Jupyter launch mode will have this enabled. It is a very straightforward web-based terminal with session persistence. It's great for a quick CLI session.

Access the terminal from the SSH connections interface.

<img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-5.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=209bceca0c9c25960269d6af03a4ec00" alt="" data-og-width="800" width="800" data-og-height="174" height="174" data-path="images/instances-sshscp-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-5.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7fd1f0b63e9e32976482c161d8adb0ff 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-5.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=3a37e3391a09f2b2d5442640ad5371a1 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-5.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=445a424b204acae3aa5892c0fb5e19f7 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-5.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=3a1c02fd93343b38f04db5301a07abe1 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-5.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=9f74b697ddbcd0b226db17785c72ff8d 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-5.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=19409536de358a89230eeb9f50f1683c 2500w" />

## Troubleshooting

### Permission Denied (publickey)

If you get this error when trying to SSH:

1. Ensure your SSH key is added to your [Vast account](https://cloud.vast.ai/manage-keys/)
2. Verify you're using the correct private key
3. Check key file permissions: `chmod 600 ~/.ssh/id_ed25519`
4. Use `-vv` flag for detailed debug info: `ssh -vv -p PORT root@IP`

### SSH Key Changes

* New account keys only apply to NEW instances created after adding the key
* Existing instances keep their original keys (won't get new keys automatically)
* For VM instances, changing keys requires recreating the VM
* To add keys to existing instances, use the instance-specific SSH interface

### General Connection Issues

You can often determine the exact cause of a connection failure by using the -vv arguments with ssh to get more information.

Common reasons include:

* Using the wrong private key
* Incorrect permissions for your private key
* Public key not added to instance or account
* Connecting to the wrong port

## SCP & SFTP File Transfer

Both **SCP** (Secure Copy Protocol) and **SFTP** (SSH File Transfer Protocol) are tools for securely transferring files that piggyback on the SSH protocol. They use the same authentication and encryption as SSH.

### SCP (Secure Copy Protocol)

* **What it is:** Simple, command-line tool for copying files between local and remote machines
* **Best for:** Quick, one-time file transfers
* **Syntax:** `scp -P <port> source destination`

**Examples:**

```bash Bash theme={null}
# Copy file TO instance
scp -P <ssh_port> my_file.txt root@<instance_ip>:/workspace/
# Copy file FROM remote server
scp -P <ssh_port> root@<instance_ip>:/workspace/my_file.txt ./
# Copy entire directory
scp -P <ssh_port> -r  myfolder/ root@<instance_ip>:/workspace/
```

### SFTP (SSH File Transfer Protocol)

* **What it is:** Interactive file transfer program with a full command set
* **Best for:** Managing files, browsing directories, multiple operations
* **Usage:** CLI or GUI tools available

**Example:**

```bash Bash theme={null}
# Establish connection
sftp -P <ssh_port> root@<instance_ip>

Welcome to vast.ai. If authentication fails, try again after a few seconds, and double check your ssh key.
Have fun!
Connected to 79.116.73.220.
sftp> ls
hasbooted   onstart.sh
```

<Note>
  Note that both scp and sftp take the `-P` argument in uppercase. This differs from the ssh command which uses lowercase.
</Note>

## VS Code Integration

Once you have your ssh keys set up, connecting to VS Code is quite straightforward. We will cover the basics here.

### Install the Remote SSH extension

You will need to add the remote extension named 'Remote - SSH'.

<img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-6.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=17c9e3e3a16d8c26955d3514ae1711e6" alt="" data-og-width="800" width="800" data-og-height="197" height="197" data-path="images/instances-sshscp-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-6.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=9714350821d91df6127260d3433f50b3 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-6.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=b7c3b40e2a93fff71c0c308c8d5f0070 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-6.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=04210bc95d585b19614a206dffb5d617 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-6.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=518d8f0d739d5d41276570c9d30aa122 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-6.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6fc23484109e25873900841e94db4f0f 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-6.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=16596074877718ce9ab5d0053dfe01fd 2500w" />

### Open Remote Window

<Columns cols={2}>
  <div>
    Click the open remote window button.

    <Frame caption="Open Remote Window">
            <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-7.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=1b086f5d4c976f519aa1623f3a613297" alt="" data-og-width="800" width="800" data-og-height="275" height="275" data-path="images/instances-sshscp-7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-7.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0637c8e27f36d55cce47ea9bd360417b 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-7.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=eb85b4133b8347ac79300267e480de61 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-7.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=30d674f29c36de381fde6440d600278d 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-7.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=c7624f765c2507f9fc26fbb11ac33f61 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-7.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=ab25486608fd22422a7bb031a1e33a89 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-7.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=4eba58f81bfb08aa91466442c288973f 2500w" />
    </Frame>
  </div>

  <div>
    Enter your ssh address details in the box that appears at the top of your window
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-8.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=34351926e878b0b59c9a24d4262bbdba" alt="" data-og-width="800" width="800" data-og-height="64" height="64" data-path="images/instances-sshscp-8.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-8.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7a7c31202f250992d0ecf2f60a7ce0f1 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-8.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=e686d4d9c5c8fd436a5f1c547b3a84ff 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-8.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=460e9dce5de901e9a7010de836b7eead 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-8.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=a578db5eb4be54040bd057455814f09c 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-8.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=898a2017185b8f41fa66f6f8eba2d012 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-sshscp-8.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6fdf5538044a44f086057ea94227e7a7 2500w" />
  </div>
</Columns>

Now simply allow a moment for VS code to configure the instance and you will be able to work with the instance as if it was a local machine.

For more information, see the [VS Code documentation](https://code.visualstudio.com/docs/remote/ssh).

## Windows GUI Clients

For Windows users who prefer GUI tools, please see our [Windows Connection Guide](/documentation/instances/connect/windows-guide) for detailed setup instructions for PuTTY, MobaXterm, and other GUI clients.
