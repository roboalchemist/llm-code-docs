# Source: https://docs.tabnine.com/main/getting-started/install/client-setup-private-installation/visual-studio-private-installation.md

# Visual Studio 2022 & 2026 (Private/Enterprise-SaaS)

Once you’ve joined your team’s Tabnine account, the next step is to install Tabnine Extension for Visual Studio 2022 or Visual Studio 2026.

### Install the Tabnine extension for Visual Studio 2022 <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0920f6c4e65f036c6c903f4f4357aa6baf40aee1%2Fvs.webp?alt=media" alt="" data-size="line"> ***OR*** Visual Studio 2026 <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line">

1. Download the Tabnine extension for Visual Studio using the link in Tabnine's console:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FmazW8MGPGLVX6f54iBur%2FScreenshot%202025-12-09%20at%2011.33.39.png?alt=media&#x26;token=895ae6dc-b417-4fbd-ac26-a895be59dac8" alt="Welcome to Tabnine starting screen"><figcaption></figcaption></figure>

2. Click on the downloaded file and run the installer.

You will need to close and reopen Visual Studio to add the Tabnine extension. After closing Visual Studio, open it normally. A VSIX Installer window will appear.

2. On the following screen, click <mark style="background-color:$info;">**Modify**</mark>:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-cf15cf5f8d7394342f3207dfa652a768da7cd77a%2FScreenshot%202025-03-03%20at%2014.03.12.png?alt=media" alt=""><figcaption></figcaption></figure>

Modifications may take a couple of minutes:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-24e5529cf9487c6c006b55c7c6aa41932da66289%2FScreenshot%202025-03-03%20at%2014.03.23.png?alt=media" alt=""><figcaption></figcaption></figure>

4. Once the extension is installed, you should see the following screen:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f41fb5101dbbe57b74d600c7cc209a87526e8d9a%2FScreenshot%202025-03-03%20at%2014.05.36.png?alt=media" alt=""><figcaption></figcaption></figure>

You can elect to click <mark style="color:blue;">View Install Log</mark> if you wish. When you're finished, press <mark style="background-color:$info;">**Close**</mark>.

5. Restart your IDE.

### Configure the Tabnine Server URL

Once the IDE has been restarted and the extension is initialized, you’ll need to set the URL of your Tabnine Enterprise Server, by going to **Tools > Options > Tabnine** menu

If you don’t have the URL, contact your Tabnine admin within your organization.

1. Click **Open settings.**
2. Update **Server URL** settings with the **Tabnine Enterprise Server URL**
3. Restart your IDE.

### Sign in to Tabnine

Once you restart the IDE and the extension is initialized, you’ll be prompted to sign in to Tabnine. Click **sign-in.**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5b0247d7d96b6543e5bd1b14d15de39ee3e283d8%2Fvs5%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You can also sign in by opening the **Extensions > Tabnine Enterprise** menu.
{% endhint %}

Next, a browser window will open and you'll be prompted to log in to Tabnine. Click **Sign In:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-4cd77c284020ff52e597ba49996e199e8a54eb9d%2FSSO%20sign%20in.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If your organization doesn't have SSO, you'll see the following screen. Sign in using your Tabnine user credentials:

<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-1e907b26012c91a5dc68a526fe86d1f58ac286af%2FTabnine%20Sign%20Up.png?alt=media" alt="" data-size="original">
{% endhint %}

Once you’ve successfully signed in, you'll see the following message:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c88bce24b996ea43eb3b3f72b4af04971b41c15a%2FScreenshot%202025-03-03%20at%2011.58.15.png?alt=media" alt=""><figcaption></figcaption></figure>

Once you see this confirmation screen, close the browser and return to your IDE. You should see the confirmation message:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9b34bd3d1df1a006c3a40c61631c5296262993f6%2Fvs9%20(1).webp?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Now [start using Tabnine](https://docs.tabnine.com/main/getting-started/quickstart)!
