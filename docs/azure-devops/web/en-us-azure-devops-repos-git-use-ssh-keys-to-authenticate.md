# Source: https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops

Title: Use SSH key authentication - Azure Repos

URL Source: https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

You can connect to your Git repos through SSH on macOS, Linux, or Windows to securely connect with Azure DevOps.

Important

SSH URLs have changed, but old SSH URLs continue to work. If you've already set up SSH, update your remote URLs to the new format:

Up to date SSH URLs start with `ssh.dev.azure.com`. The previous URLs use `vs-ssh.visualstudio.com`.

*   Verify which remotes are using SSH. Run `git remote -v` in your shell or use a GUI client instead.
*   Visit your repository on the web and select **Clone**.
*   Select **SSH** and copy the new SSH URL.
*   In your shell run `git remote set-url <remote name> <new SSH URL>` for each remote of a repository you wish to update. Alternatively, use a GUI client to update the remote URLs.

| Category | Requirements |
| --- | --- |
| **Permissions** | [Access to clone the repository](https://learn.microsoft.com/en-us/azure/devops/repos/git/set-git-repository-permissions?view=azure-devops#default-repository-permissions) |
| **Policies** | [SSH authentication enabled](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/change-application-access-policies?view=azure-devops) |

SSH public key authentication works with an asymmetric pair of generated encryption keys. The _public_ key is shared with Azure DevOps and used to verify the initial ssh connection. The _private_ key is kept safe and secure on your system.

The following steps cover configuration of SSH key authentication on the following platforms using the command line (also called `shell`):

*   Linux
*   macOS
*   Windows systems running [Git for Windows](https://www.git-scm.com/download/win)

Note

If you've already created RSA SSH keys on your system, skip this step and [configure your SSH keys](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#configuration). To verify this go to your home directory and look into the `.ssh` folder (`%UserProfile%\.ssh\` on Windows or `~/.ssh/` on Linux, macOS, and Windows with Git Bash). If you see two files named `id_rsa` and `id_rsa.pub` respectively continue with [configuring your SSH keys](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#configuration).

To use key-based authentication, you first need to generate public/private key pairs for your client. **ssh-keygen.exe** is used to generate key files and the algorithms DSA, RSA, ECDSA, or Ed25519 can be specified. If no algorithm is specified, Ed25519 is used.

Note

The only SSH key type supported by Azure DevOps is _RSA_.

To generate key files using the RSA algorithm supported by Azure DevOps (either RSA-SHA2-256 or RSA-SHA2-512), run one of the following commands from a PowerShell or another shell such as `bash` on your client:

```
ssh-keygen -t rsa-sha2-256
```

Or

```
ssh-keygen -t rsa-sha2-512
```

The output from the command should display the following output (where `username` is your username):

```
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\username/.ssh/id_rsa):
```

You can press Enter to accept the default, or specify a path and/or filename where you would like your keys to be generated. At this point, you're prompted to use a passphrase to encrypt your private key files. The passphrase can be empty but not recommended. The passphrase works with the key file to provide two-factor authentication.

```
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\username/.ssh/id_rsa.
Your public key has been saved in C:\Users\username/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:FHK6WjcUkcfQjdorarzlak1Ob/x7AmqQmmx5ryYYV+8 username@LOCAL-HOSTNAME
The key's randomart image is:
+---[RSA 3072]----+
|      . ** o     |
|       +.o= .    |
|      . o+       |
|      .+. .      |
|     .ooS  .     |
|  . .oo.=.o      |
|   =.= O.= .     |
|  . B BoE + . .  |
|   . *+*o. .o+   |
+----[SHA256]-----+
```

Now you have a public/private RSA key pair in the location specified. The .pub files are public keys, and files without an extension are private keys:

```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        10/11/2022   6:29 PM           2610 id_rsa
-a----        10/11/2022   6:29 PM            578 id_rsa.pub
```

Important

Never share the contents of your private key. If the private key is compromised, attackers can use it to trick servers into thinking the connection is coming from you. Private key files are the equivalent of a password and should be protected the same way.

Associate the public key generated in the previous step with your user ID.

Note

You have to repeat this operation for each organization you have access to and want to use SSH with.

1.   Open your security settings by browsing to the web portal and selecting the icon next to the avatar in the upper right of the user interface. Select **SSH public keys** in the menu that appears.

![Image 1: Screenshot that shows the SSH public keys menu item and the user avatar selected in Azure DevOps.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/use-ssh-authentication/select-ssh-public-keys.png?view=azure-devops)

2.   Select **+ New Key**.

![Image 2: Screenshot of accessing security configuration in Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/use-ssh-authentication/ssh-accessing-security-key.png?view=azure-devops)

3.   Copy the contents of the public key (for example, `id_rsa.pub`) that you generated into the **Public Key Data** field.

Important

Avoid adding whitespace or new lines into the **Key Data** field, as they can cause Azure DevOps to use an invalid public key. When pasting in the key, a newline often is added at the end. Be sure to remove this newline if it occurs. 
![Image 3: Screenshot showing configuring a Public Key in Azure DevOps.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/use-ssh-authentication/ssh-key-input.png?view=azure-devops)

4.   Give the key a useful description (this description is displayed on the **SSH public keys** page for your profile) so that you can remember it later. Select **Save** to store the public key. Once saved, you can't change the key. You can delete the key or create a new entry for another key. There are no restrictions on how many keys you can add to your user profile.

5.   On the **SSH Public Keys** overview page, the server fingerprints are displayed. Make note of the SHA256 fingerprint to use when you first connect to Azure DevOps via SSH.

![Image 4: Screenshot of accessing security configuration in Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/use-ssh-authentication/ssh-accessing-security-key.png?view=azure-devops)

6.   Test the connection by running the following command:

```
ssh -T git@ssh.dev.azure.com
```

If you're connecting for the first time, you should receive the following output:

```
The authenticity of host 'ssh.dev.azure.com (<IP>)' can't be established.
RSA key fingerprint is SHA256:ohD8VZEXGWo6Ez8GSEJQ9WpafgLFsOfLOtGGQCQo6Og.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Compare the fingerprint with the SHA256 fingerprint displayed on the previously mentions **SSH Public Keys** page. Proceed only if they match!

7.   Enter `yes` to continue. If everything is configured correctly, the output should look like this:

```
Warning: Permanently added 'ssh.dev.azure.com' (RSA) to the list of known hosts.
 remote: Shell access is not supported.
 shell request failed on channel 0
```

If not, see the section on [Questions and troubleshooting](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#questions-and-troubleshooting).

1.   Copy the SSH clone URL from the web portal. In this example, the SSH clone URL is for a repo in an organization named **fabrikam-fiber**, as indicated by the first part of the URL after `dev.azure.com`.

![Image 5: Screenshot showing Azure Repos SSH cloned URL.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/use-ssh-authentication/ssh-clone-url.png?view=azure-devops)

2.   Run `git clone` from the command prompt.

```
git clone git@ssh.dev.azure.com:v3/fabrikam-fiber/FabrikamFiber/FabrikamFiber
```

If you aren't using an SSH Agent, you're prompted to enter your passphrase:

```
Cloning into 'FabrikamFiber'...
Enter passphrase for key '/c/Users/username/.ssh/id_rsa':
remote: Azure Repos
remote: Found 127 objects to send. (50 ms)
Receiving objects: 100% (127/127), 56.67 KiB | 2.58 MiB/s, done.
Resolving deltas: 100% (15/15), done.
```

If you're instead prompted to verify a fingerprint, read [Step 2: Add the public key to Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#step-2-add-the-public-key-to-azure-devops) again. For other problems, read the section on [Questions and troubleshooting](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#questions-and-troubleshooting).

Tip

To make the most of SSH it is common to use an SSH Agent to manage your SSH key(s). Setting up an agent is beyond the scope of this article, though.

**A:** The **recommended course of action** is to follow the steps above to [create and upload a new SSH key](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#step-1-create-your-ssh-keys).

**As an alternative option**, a Project Collection Admin can disable the policy that validates the SSH key expiration date. **By default, the Validate SSH key expiration policy is enabled.** For more information, see [SSH key policies](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/change-application-access-policies?view=azure-devops#ssh-key-policies).

You automatically receive a notification 7 days prior and when your key expires. Along with these notifications, you will also see the messaging below:

```
remote: Authentication failed: your SSH key has expired. To restore access, visit https://aka.ms/ado-ssh-public-key-expired for guidance.
remote: Public key authentication failed.
fatal:  Could not read from remote repository.
```

**A:** There are two different warning messages could see:

```
ssh-rsa is about to be deprecated and your request has been throttled. Please use rsa-sha2-256 or rsa-sha2-512 instead. Your session will continue automatically. For more details see https://devblogs.microsoft.com/devops/ssh-rsa-deprecation.
```

Or

```
You’re using ssh-rsa that is about to be deprecated and your request has been blocked intentionally. Any SSH session using ssh-rsa is subject to brown out (failure during random time periods). Please use rsa-sha2-256 or rsa-sha2-512 instead. For more details see https://devblogs.microsoft.com/devops/ssh-rsa-deprecation.
```

If you modified your SSH config to downgrade your security settings for Azure DevOps by adding the following to your `~/.ssh/config` (`%UserProfile%\.ssh\config` on Windows) file:

```
Host ssh.dev.azure.com vs-ssh.visualstudio.com
  HostkeyAlgorithms +ssh-rsa
```

Remove these lines now and make sure `rsa-sha2-256` and/or `rsa-sha2-512` are allowed.

For more information, see the [blog post](https://devblogs.microsoft.com/devops/ssh-rsa-deprecation/).

**A:** There are multiple different problems that you could experience:

*   **Use of unsupported ssh-rsa**

```
You’re using ssh-rsa that is unsupported. Please use rsa-sha2-256 or rsa-sha2-512 instead. For more details see https://devblogs.microsoft.com/devops/ssh-rsa-deprecation.
```

If you modified your SSH config to downgrade your security settings for Azure DevOps by adding the following to your `~/.ssh/config` (`%UserProfile%\.ssh\config` on Windows) file:

```
Host ssh.dev.azure.com vs-ssh.visualstudio.com
   HostkeyAlgorithms +ssh-rsa
```

Remove these lines now and make sure `rsa-sha2-256` and/or `rsa-sha2-512` are allowed.

For more information, see the [blog post](https://devblogs.microsoft.com/devops/ssh-rsa-deprecation/).

*   **No matching host key**

This problem shouldn't happen on Azure DevOps Service or on more recent Azure DevOps Server versions as mentioned in the [blog post](https://devblogs.microsoft.com/devops/ssh-rsa-deprecation/).

```
Unable to negotiate with <IP> port 22: no matching host key type found. Their offer: ssh-rsa
```

Modify your SSH config to downgrade your security settings for Azure DevOps by adding the following to your `~/.ssh/config` (`%UserProfile%\.ssh\config` on Windows) file:

```
Host ssh.dev.azure.com vs-ssh.visualstudio.com
   HostkeyAlgorithms +ssh-rsa
```
Important

OpenSSH deprecated the `ssh-rsa` public key signature algorithm in [version 8.2](https://www.openssh.com/txt/release-8.2) and disabled it by default in [version 8.8](https://www.openssh.com/txt/release-8.8). 
*   **No matching MAC**

```
Unable to negotiate with <IP> port 22: no matching MAC found. Their offer: hmac-sha2-256,hmac-sha2-512
```

Modify your SSH config to downgrade your security settings for Azure DevOps by adding the following to your `~/.ssh/config` (`%UserProfile%\.ssh\config` on Windows) file:

```
Host ssh.dev.azure.com vs-ssh.visualstudio.com
   MACs +hmac-sha2-512,+hmac-sha2-256
```
*   **No matching key exchange method**

```
Unable to negotiate with <IP> 22: no matching key exchange method found. Their offer: diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha256
```

Modify your SSH config to downgrade your security settings for Azure DevOps by adding the following to your `~/.ssh/config` (`%UserProfile%\.ssh\config` on Windows) file:

```
Host ssh.dev.azure.com vs-ssh.visualstudio.com
   KexAlgorithms +diffie-hellman-group-exchange-sha256,+diffie-hellman-group14-sha1,+diffie-hellman-group1-sha1
```
Important

The key exchange algorithm `diffie-hellman-group1-sha1` has been disabled by default in [version 6.9](https://www.openssh.com/txt/release-6.9) of OpenSSH and `diffie-hellman-group14-sha1` in [version 8.2](https://www.openssh.com/txt/release-8.2). 

Tip

For self-hosted instances of Azure DevOps Server and TFS use the appropriate hostname in the `Host` line instead of `ssh.dev.azure.com vs-ssh.visualstudio.com`.

**A:** You can use an SSH Agent. Linux, macOS, and Windows (starting with [Windows 10 (build 1809)](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview) or by using Git for Windows with Git Bash) all ship with an SSH Agent. The SSH Agent can be used to cache your SSH keys for repeated use. Consult your SSH vendor's manual for details on how to use it.

**A:** Yes. Load the private key with PuTTYgen, go to **Conversions** menu, and select **Export OpenSSH key**. Save the private key file and then follow the steps to [set up nondefault keys](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#newkeys). Copy your public key directly from the PuTTYgen window and paste into the **Key Data** field in your security settings.

**A:** You can verify the fingerprint of the public key uploaded with the one displayed in your profile through the following `ssh-keygen` command run against your public key using the command line. You need to change the path and the public key filename if you aren't using the defaults.

Note

As of August/September 2024, we are migrating from MD5 to SHA-256 hashes. You may need to choose the correct function during the transition period.

```
ssh-keygen -l -E md5 -f <path_to_your_public_key> -- use this for MD5 fingerprints
ssh-keygen -l -E sha256 -f <path_to_your_public_key> -- use this for SHA-256 fingerprints
```

You can then compare the signature to the one in your profile. This check is useful if you have connection problems or have concerns about incorrectly pasting in the public key into the **Key Data** field when adding the key to Azure DevOps.

**A:** You need to update the `origin` remote in Git to change over from an HTTPS to SSH URL. Once you have the [SSH clone URL](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#step-3-clone-the-git-repository-with-ssh), run the following command:

```
git remote set-url origin <SSH URL to your repository>
```

Git commands accessing the remote called `origin` uses SSH.

**A:** Azure DevOps Services currently doesn't support LFS over SSH. Use HTTPS to connect to repos with Git LFS tracked files.

**A:** To use a key stored in a different place than the default, perform these two tasks:

1.   The keys must be in a folder that only you can read or edit. If the folder has wider permissions, SSH doesn't use the keys.

2.   You must let SSH know the location of the key, for example, by specifying it as an "Identity" in the SSH config:

```
Host ssh.dev.azure.com
  IdentityFile ~/.ssh/id_rsa_azure
  IdentitiesOnly yes
```

The `IdentitiesOnly yes` setting ensures that SSH doesn't use any other available identity to authenticate. This setting is particular important if more than one identity is available.

**A:** Generally, when you configure multiple keys for an SSH client, the client attempts to authenticate with each key sequentially until the SSH server accepts one.

However, this approach doesn't work with Azure DevOps due to technical constraints related to the SSH protocol and the structure of our Git SSH URLs. Azure DevOps accepts the first key provided by the client during authentication. If this key is invalid for the requested repository, the request fails without attempting any other available keys, resulting in the following error:

```
remote: Public key authentication failed.
fatal: Could not read from remote repository.
```

For Azure DevOps, you need to configure SSH to explicitly use a specific key file. The procedure is the same as when using a key stored in a [nondefault location](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#non-default-keys). Tell SSH to use the correct SSH key for the Azure DevOps host.

**A:** Azure DevOps blindly accepts the first key that the client provides during authentication. If that key is invalid for the requested repository, the request fails with the following error:

```
remote: Public key authentication failed.
fatal: Could not read from remote repository.
```

This failure is because all Azure DevOps URLs share the same hostname (`ssh.dev.azure.com`), making it impossible for SSH to distinguish between them by default. However, you can modify your SSH configuration to differentiate between different organizations by providing distinct keys for each. Use host aliases to create separate `Host` sections in your SSH configuration file.

```
# The settings in each Host section are applied to any Git SSH remote URL with a
# matching hostname.
# Generally:
# * SSH uses the first matching line for each parameter name, e.g. if there's
#   multiple values for a parameter across multiple matching Host sections
# * "IdentitiesOnly yes" prevents keys cached in ssh-agent from being tried before
#   the IdentityFile values we explicitly set.
# * On Windows, ~/.ssh/your_private_key maps to %USERPROFILE%\.ssh\your_private_key,
#   e.g. C:\Users\<username>\.ssh\your_private_key.

# Imagine that we have the following two SSH URLs:
# * git@ssh.dev.azure.com:v3/Fabrikam/Project1/fab_repo
#   * For this, we want to use `fabrikamkey`, so we'll create `devops_fabrikam` as
#     a Host alias and tell SSH to use `fabrikamkey`.
# * git@ssh.dev.azure.com:v3/Contoso/Project2/con_repo
#   * For this, we want to use `contosokey`, so we'll create `devops_contoso` as
#     a Host alias and tell SSH to use `contosokey`.
#
# To set explicit keys for the two host aliases and to tell SSH to use the correct
# actual hostname, add the next two Host sections:
Host devops_fabrikam
  HostName ssh.dev.azure.com
  IdentityFile ~/.ssh/private_key_for_fabrikam
  IdentitiesOnly yes

Host devops_contoso
  HostName ssh.dev.azure.com
  IdentityFile ~/.ssh/private_key_for_contoso
  IdentitiesOnly yes
```

Afterwards, instead of using the real URLs, tell Git you want to use these URLs for each repository as remote by replacing the hostname in the existing remotes with `devops_fabrikam` and `devops_contoso` respectively. For example, `git@ssh.dev.azure.com:v3/Fabrikam/Project1/fab_repo` would become `git@devops_fabrikam:v3/Fabrikam/Project1/fab_repo`.

**A:** There are a few notifications you may receive regarding your SSH key(s).

*   A new SSH key was added to your organization

*   An SSH key associated with your account will expire in 7 days and will not be valid for authentication.

*   An SSH key associated with your account has expired and is no longer valid for authentication.

**Example notification**

![Image 6: Screenshot showing SSH key email notification.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/use-ssh-authentication/ssh-key-added-email.png?view=azure-devops)

**A:** If you receive an SSH key registration notification you didn't initiate, your credentials could be compromised.

The next step would be to investigate whether or not your password is compromised. Changing your password is always a good first step to defend against this attack vector. If you're a Microsoft Entra user, talk with your administrator to check if your account was used from an unknown source/location.

**A:** Some Linux distributions, such as Fedora Linux, have crypto policies that require stronger SSH signature algorithms than Azure DevOps supports (as of January 2021). There's an open [feature request](https://developercommunity.visualstudio.com/idea/365980/support-non-rsa-keys-for-ssh-authentication.html) to add this support.

You can work around the issue by adding the following code to your SSH configuration (`~/.ssh/config`):

```
Host ssh.dev.azure.com vs-ssh.visualstudio.com
  PubkeyAcceptedKeyTypes +ssh-rsa
```

Tip

For self-hosted instances of Azure DevOps Server and TFS use the appropriate hostname in the `Host` line instead of `ssh.dev.azure.com vs-ssh.visualstudio.com`.
