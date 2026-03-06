# Source: https://docs.vast.ai/documentation/instances/connect/windows-guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows SSH Guide

> Learn how to securely connect to Vast.ai instances using SSH on Windows. Understand the basics of SSH, how to generate and add keys, and how to use PuTTY and MobaXterm for GUI-based connections.

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Connect to Vast.ai Instances from Windows",
  "description": "A comprehensive guide to connecting to Vast.ai instances from Windows using GUI tools including PuTTY and MobaXterm, covering key generation, configuration, and connection setup.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Choose Connection Method",
      "text": "Modern Windows supports CLI SSH commands in PowerShell. For GUI-based connections, use tools like PuTTY or MobaXterm. Alternatively, use Jupyter Terminal for a simple web-based terminal with session persistence."
    },
    {
      "@type": "HowToStep",
      "name": "Generate SSH Keys with PuTTY/MobaXterm",
      "text": "For PuTTY: Open PuTTYGen, click Generate, move mouse to generate randomness, save both public and private keys (.ppk format). For MobaXterm: Navigate to Tools > MobaKeyGen, click Generate, save keys. Copy the full public key to clipboard."
    },
    {
      "@type": "HowToStep",
      "name": "Add Public Key to Vast Account",
      "text": "Go to cloud.vast.ai/manage-keys/ and paste your public key. Keys stored at account level are automatically added to new instances. For existing instances, add keys from the instance card."
    },
    {
      "@type": "HowToStep",
      "name": "Configure and Connect",
      "text": "For PuTTY: Enter IP address and port in Session tab, set username to 'root' in Connection > Data, browse for private key in Connection > SSH > Auth > Credentials, save session, and click Open. For MobaXterm: Create new SSH session, enter remote host, specify username (root), set port, select private key file, and click OK to connect."
    }
  ]
})
}}
/>

## Windows Powershell

Modern versions of Windows support running CLI ssh commands in PowerShell.  We recommemnd you use the CLI wherever possible.

<Note>
  This guide will focus only on **Windows GUI tools.**  If you would like to proceed with the CLI, please navigate to the [full SSH guide](/documentation/instances/sshscp) for setup information.
</Note>

## Jupyter Terminal - SSH Alternative

As a simple alternative to SSH, you might like to consider Jupyter Terminal instead.  All instances started in Jupyter launch mode will have this enabled.  It is a very straightforward web-based terminal with session persistence.  It's great for a quick CLI session.

Access the terminal from the SSH connections interface

<img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=01afd3db4a7a5b5dc23f5794e18f48b0" alt="" data-og-width="800" width="800" data-og-height="174" height="174" data-path="images/instances-windows-ssh.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6144c64d7c043f429e98d93686efcfd1 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=4e5a1fdf286d7570a0c945b35dbb2dac 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=98431659bbf4572ced674c07a839544a 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=9ae1e305072ccd33cd036c7237a8589d 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=4f062d82a46e8def6872e61aeb1b534e 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=9e3581a13c0e56a78a97a5b6f3c8cd74 2500w" />

<Frame caption="Jupyter Terminal">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-2.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6e9f775b251b25e48aa29dce3694ed9c" alt="Jupyter Terminal" data-og-width="1218" width="1218" data-og-height="416" height="416" data-path="images/instances-windows-ssh-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-2.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=1a0848ed5618a1c06ed6ab2c01f46662 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-2.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=27d69a5fbd9d2d556f82eb1b790f33f9 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-2.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=f7a34b14e0af0df378232dfc71def7ff 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-2.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=97c9839a83a300f223a99f94030b92d1 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-2.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7b3b0014c8df7cb421197000e49a87e7 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-2.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=d6eac253a2e655c70c5683219ce7e498 2500w" />
</Frame>

## GUI Setup Guide (Windows)

Several GUI tools are available to help with SSH connectivity.  While it is often most straightforward to use the terminal we will cover some of the popular options here.

For each application we will assume the following:

* IP address: 142.114.29.158
* Port: 46230
* Username: root

To find your own connection details you can click the SSH button on your instance card.

<Frame caption="SSH Button">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-3.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=ff769315673347ef690cfa1a5168a993" alt="SSH Button" data-og-width="800" width="800" data-og-height="437" height="437" data-path="images/instances-windows-ssh-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-3.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=433737469b8b469f8799c9d4eebe6b4a 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-3.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=874c7c6327d6d6bbbee6e05eb08ab1ba 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-3.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=5801549c88b09e5a52c779ffa9bd6cef 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-3.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=c0212dac5d7ad26942f0c198e6673327 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-3.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=d8f49a6a201b0292b6e38deb95622140 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-3.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=c3a2207921ae96ed0de7bc44b7746a6c 2500w" />
</Frame>

<br />

<Frame caption="Example SSH Details">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-4.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=2f5b7d8657e179d2f32ba673adf1b046" alt="Example SSH Details" data-og-width="800" width="800" data-og-height="445" height="445" data-path="images/instances-windows-ssh-4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-4.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=02670ec999f69b155c8cc4b60fa9a28a 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-4.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=db65d1eb7a7a25b05a9642d5e4c74b6a 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-4.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0334de4cee6dd03d3f385eb12ed08212 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-4.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=90d806f9d3cfe83906d8206b15163852 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-4.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=fb5528ab0a4df50e56ed88144351821f 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-4.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6d585ab30e3e2a81e99abb9d240788d7 2500w" />
</Frame>

### PuTTY

[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/) consists of two important components - PuTTY for making connections and PuTTYGen for creating SSH keys.

First, we will generate a public and private key pair.  PuTTy uses its own `.ppk` private key type.

Open PuTTYGen and click the 'Generate' button.  You will be asked to move your mouse around until the green bar is full.

<Frame caption="PuTTYgen Key Generation">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-5.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=96d7795b67e0028c2f45e134c6ff8fc3" alt="Key generation interface" data-og-width="800" width="800" data-og-height="624" height="624" data-path="images/instances-windows-ssh-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-5.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=1b079377223811bde80122adaaf03358 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-5.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=e33bf747fdf6540b30bfc67a1eb0cdf3 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-5.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=b23bb52da9abb40c36e7c0ee17240325 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-5.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=c826e72ebcafa810fa42ae318414762d 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-5.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=8d73ba5fc29c76f7d40dcc4190e47d7c 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-5.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=4181475561d0f4125c9ceb18fbd13592 2500w" />
</Frame>

Once the key generation has completed, save both your public and private key somewhere safe such as in your Documents folder.  Optionally you can enter a passphrase for your private key for added security.

Next, copy the full public key to the clipboard and add it to your account at [https://cloud.vast.ai/manage-keys/](https://cloud.vast.ai/manage-keys/)

Any keys stored at the account level will automatically be added to new instances as they are created.  If you have an existing instance you can add keys to it from the instance card.

<img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-6.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=70eba6e9c8d4b61ceb20e91a802e00b2" alt="" data-og-width="800" width="800" data-og-height="331" height="331" data-path="images/instances-windows-ssh-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-6.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=2744d1c8720d75851d0d4d90ffe7c79c 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-6.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=d2e8ce8aed2a1e6e5b81dcbc8cffaf54 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-6.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7e0a8143f4e330b755faee21f9e29545 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-6.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=916e0cb13ac882e4b00d3717474c9e77 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-6.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=cf8b1b35769fe31579caf790af255b22 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-6.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=8b345084eb9d89f521f7aa3229ad3fe7 2500w" />

<Frame caption="Save Keys">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-7.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=b2bdf20bc2d7e43e9f62167537a7c538" alt="Save keys interface" data-og-width="800" width="800" data-og-height="624" height="624" data-path="images/instances-windows-ssh-7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-7.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=4f535ed20bbf88ee6ea8c44e6e791beb 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-7.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=9c8192d7ad06047c54511e85db04d02c 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-7.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=f40065d26158cac19696bf6963c9b071 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-7.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6a3b79d45d49db46aea38a2adbcd9f27 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-7.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=f8bdae2f6602a0640f1cda9cafc6abb8 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-7.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=1511cf5e9ac494196dbd0ad43688be5b 2500w" />
</Frame>

Now that we have a suitable key to use, close PuTTYGen and open the main PuTTY application.

In the 'Session' tab, enter the **IP address** and the **port**

<Frame caption="PuTTY session tab">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-8.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=cc7ef4d52e8e411520e7c9e4d40c22ee" alt="PuTTY session tab" data-og-width="800" width="800" data-og-height="786" height="786" data-path="images/instances-windows-ssh-8.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-8.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0db397f2a3f864f3b8842f52f2c79a9e 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-8.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=49dcb42f68c243dd6b1a9b07ce9c36a3 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-8.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=3af1a7ca25c1e2ecd18ebb53fcfa398b 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-8.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=891d2ab0c5ef2273e58307d35ad78b16 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-8.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=98dad0c976268cee21ff96b34ebd2017 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-8.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=4e333e496df5a6b639449cf36aa09b8a 2500w" />
</Frame>

Next, move to the 'Connection -> Data\` tab and set the Auto-login username to 'root'

<Frame caption="Connection data tab">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-9.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=92e594a978715a90e5a8bcfa98cadedf" alt="Connection data tab" data-og-width="800" width="800" data-og-height="786" height="786" data-path="images/instances-windows-ssh-9.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-9.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=a880607163526792b8ffad5e3118ddf8 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-9.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=d59c4954ebdef5872880eed68c39f941 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-9.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=354b252a5c1d03303c43cc8e57960329 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-9.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=03195a679ae929d104b7e2c84c41e7d9 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-9.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=a0dc903c821ce5778706d4d93d576921 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-9.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=ad3cd81d1fe4c36f60cd96851ad7cf9c 2500w" />
</Frame>

Now navigate to 'Connection -> SSH -> Auth -> Credentials' and browse for the private key (.ppk) that you saved earlier.&#x20;

<Frame caption="SSH credentials tab">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-10.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0a2a4c0820f2b67c6091851af565ed67" alt="SSH credentials tab" data-og-width="800" width="800" data-og-height="786" height="786" data-path="images/instances-windows-ssh-10.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-10.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=27ec13581bb90915fef3446d897b87e2 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-10.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0a6cb4fe27feadb93d69bf40446b9240 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-10.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=200b89937b26d65b78124746fe124754 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-10.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=532770c259de944567e4020a1ee4f1af 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-10.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6c7625d394b6fd29bcef822b34f6294d 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-10.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=25f9cf717dde52c09f398f587ca0283b 2500w" />
</Frame>

Finally navigate back to the 'Sessions' tab to save the connection details.  Here I have saved the session with the instance ID so that I can access it again later.&#x20;

<Frame caption="Save connection">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-11.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=5559b3736a5c13f78457fc4ae5eb578a" alt="Save connection" data-og-width="800" width="800" data-og-height="786" height="786" data-path="images/instances-windows-ssh-11.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-11.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=b61e8866a0bf34d0bc232a3321296c5c 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-11.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=8d4443568d5c1a30bf051a85b43afcc3 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-11.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=215ccefb8c60e1415affda68c9873aa5 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-11.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=534a52154745d739fd778f03942567ea 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-11.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=734f8b693d5087e72483431c287b30d3 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-11.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=8f5d6cf9157f834a7f21e4e3f20c99c7 2500w" />
</Frame>

Finally, Click the 'Open' button to be connected to your instance.

PuTTY has many additional features to explore.  Find the full documentation [here.](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)

### MobaXterm

First, we need to create a public and private key pair.  MobaXterm uses puTTY style `.ppk` keys.

Open the application and navigate to Tools -> MobaKeyGen (SSH Key Generator)

Glick the 'Generate' button.  You will be asked to move your mouse around until the green bar is full.

<Frame caption="Generate Key">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-12.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=bb298726a5f55d4af7ace09e6f19f137" alt="Key generation interface" data-og-width="800" width="800" data-og-height="626" height="626" data-path="images/instances-windows-ssh-12.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-12.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=26f42d827d995958b36a6a40348b7bf1 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-12.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=eed582b8dbdb611bfae6f4024ff4f7de 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-12.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6776683eb4ba13d1fd5c904ef015606e 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-12.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=88c4e527367d1f973db54ddd2913ed59 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-12.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=698278e206c50974cc36bd3b5eaa3719 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-12.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7492be4ab1a13ecc01ef32496b68b538 2500w" />
</Frame>

Once the key generation has completed, save both your public and private key somewhere safe such as in your Documents folder.  Optionally you can enter a passphrase for your private key for added security.

Next, copy the full public key to the clipboard and add it to your account at [https://cloud.vast.ai/manage-keys/](https://cloud.vast.ai/manage-keys/)

Any keys stored at the account level will automatically be added to new instances as they are created.  If you have an existing instance you can add keys to it from the instance card.

<Frame caption="Save Keys">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-13.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=3469c3b8071ce5d9b10d241855a8374d" alt="Save keys interface" data-og-width="800" width="800" data-og-height="626" height="626" data-path="images/instances-windows-ssh-13.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-13.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=26015547dd256f6952134e81af97a686 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-13.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=c14480a08837bc2f4e8988870f8767d6 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-13.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=5454b069c9d65427060b78a4266c33a6 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-13.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=a78471bd8cbfd81a1917ce9e9ca0e917 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-13.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=4512d6d0f186e979878a165e3fb848c9 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-13.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=8acfba6d5e9d2656fcbafd23aeda2d84 2500w" />
</Frame>

<br />

<img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-14.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6d27de25885e6114ba63d69a51d425f4" alt="" data-og-width="800" width="800" data-og-height="331" height="331" data-path="images/instances-windows-ssh-14.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-14.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=9debe52b5a9d54b20975b52a876da80e 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-14.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=ddb0889094e13398d171e8fde8441091 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-14.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=82683adab02f51fec9acccc7f479fac5 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-14.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=62872007343e5ef5304da60879f0ef75 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-14.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=f8fd65cc8c60f4303e665c618e21bde0 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-14.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0b0cbb4ce74ad948ad412694d17dcfc8 2500w" />

Now you can close the key generation interface.  We will create a new session.

Navigate to Sessions -> New Session -> SSH

<Frame caption="Create a Session">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-15.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=a9d56ff5e774e62362f0ed9459f77c89" alt="Sesison interface" data-og-width="800" width="800" data-og-height="536" height="536" data-path="images/instances-windows-ssh-15.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-15.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=9f5584b76bd620618798f13f4b534afe 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-15.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=3ce6c9a95e19f99e81658da87ada17b7 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-15.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=b68b12a3cd05a8aaf6ab080b109ed95a 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-15.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=33dca9df2ed3a8e88a352f303673e945 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-15.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=06019ae07050823e4f1470edd91c332c 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-15.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=2ddda34cd7aeed5952ba451d610dfe39 2500w" />
</Frame>

Important details to complete:

* Remote Host
* Specify Username (root)
* Port
* Use private key

Click 'OK' and you will be connected to the instance.

<Frame caption="Successful Connection">
    <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-16.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=c238ee5aa5afda020a4ca4dbe3afb110" alt="SSH terminal" data-og-width="950" width="950" data-og-height="567" height="567" data-path="images/instances-windows-ssh-16.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-16.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=3fe6a26dcbf150adf734df362658bdea 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-16.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=85b5e94b400caaa96d4d728c8537100a 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-16.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=18c5350f3aaa6c851720e1594701282f 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-16.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=aa7674dcaa1b3a780159c4be7641284c 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-16.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=5034fcc68cd8d1d92e37775185fdedc7 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-windows-ssh-16.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=32f3efe91475978cf14cf13673e01583 2500w" />
</Frame>

You can find the documentation for MobaXterm [here](https://mobaxterm.mobatek.net/documentation.html).

### Other GUI Clients

Many GUI clients are available for Windows and other operating systems, and although it is not possible to cover all of these here, the key things to remember when setting up are:

* Create a public and private key pair
* Add the public key to your vast account and any running instances
* Keep the private key safe
* Ensure you are connecting to the correct IP address and port as user `root`
