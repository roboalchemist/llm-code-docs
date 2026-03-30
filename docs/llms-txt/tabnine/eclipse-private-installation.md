# Source: https://docs.tabnine.com/main/getting-started/install/client-setup-private-installation/eclipse-private-installation.md

# Eclipse (Private/Enterprise-SaaS)

Once you’ve joined your team’s Tabnine account, the next step is to install Tabnine in Eclipse.\
This article guides you through the process.

## Install from your private update site <a href="#install-from-marketplace" id="install-from-marketplace"></a>

1. In Eclipse, go to **Eclipse** > **Help** and select **Install New Software:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c5aa9bee4cc5e110751f9e4c80ecea400e3f2bc5%2Fec1%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

2. Click **Add:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-83641b80f2249baadf8ed4646ff877634d31151a%2Fec2%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

3. In the **Add Repository** screen, add the details of your Tabnine Enterprise Server.
4. Enter the following URL for **Location:** https\://{YOUR TABNINE SERVER URL}/update/eclipse
5. Click **Add:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-841dcb5dabc2de977a6896bf6eff73665a7bf53f%2Fec3%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note:

If you have an internal certificate authority you will need to add:

1\. Locate the eclipse.ini file in your Eclipse installation and open it

2\. Below the line `-vmargs`, add the following lines, then save the file:

Mac OS:

**`-Djavax.net.ssl.trustStore=NUL`**

**`-Djavax.net.ssl.trustStoreType=KeychainStore`**

Windows:

**`-Djavax.net.ssl.trustStore=NUL`**

**`-Djavax.net.ssl.trustStoreType=Windows-ROOT`**

3\. Restart eclipse.
{% endhint %}

4. Select **Tabnine Eclipse Plugin** **- Self Hosted** and click **Next:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-946cc1a5690438a735b8146d27fe9a1de6a7c852%2Fec4%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

5. On the following screen, click **Next:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-dcede4db11611176b1a9c01b2c737ffcd8042ea4%2Fec5%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

6. Accept the terms and click **Finish:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-177af5336248253240916b0c4ed47915c8908119%2Fec6%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

7. Under **Authority / Update Site**, select your site and click **Trust Selected:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5c0077e850ae216ee05c532feb7fc1e789e39c1b%2Fec7%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

8. You'll see that the installation is in progress:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-116de13f3bbe8209ddc4052fdde84c477d90dd37%2Fec8%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

9. Once installation is complete, click **Restart Now** to restart your IDE:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ffe92e2e933b7860764e9622d52845da3baed405%2Fec9%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

### Configure the Tabnine Server URL

1. After your IDE restarts, you'll see the Tabnine logo on the status bar with a message requesting that you set the Tabnine Enterprise Server URL:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ac1f51d48ea7f730aae8165bc200fee0eb02d1a2%2Fec10%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

2. Click the status bar message, and then click <mark style="background-color:blue;">**Open settings**</mark>**:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-4822301e96a0ad73079f34fbcce768b55066fa4d%2Fec11%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

3. Set your Tabnine Enterprise Server URL to \[https\://{YOUR TABNINE SERVER URL}], click <mark style="background-color:blue;">**Apply and Close**</mark>**,** and restart your IDE:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ebfc9c60930cb8ee6fbd9eacbcb8ab196838e746%2Fec12%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

4. Wait for Tabnine Enterprise to initialize:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-462a88b255a937ef279732bc176edd1a37d3bd7e%2Fec13%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

### Sign in to Tabnine

1. Tabnine will ask you to sign in. Click the message and then click **Login:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d643c39a23cf72242625328961cca3eeddca73fa%2Fec14%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

2. A browser window will open and you'll be prompted to log in to Tabnine. Click **Sign In:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-4cd77c284020ff52e597ba49996e199e8a54eb9d%2FSSO%20sign%20in.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If your organization doesn't have SSO, you'll see the following screen. Sign in using your Tabnine user credentials

<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-1e907b26012c91a5dc68a526fe86d1f58ac286af%2FTabnine%20Sign%20Up.png?alt=media" alt="" data-size="original">
{% endhint %}

3. Once you’ve successfully signed in, you'll see the following message:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-52fd3aa5731f03c30d5b97e3d94cf0d82b05e0af%2FTabnine%20authenticated.png?alt=media" alt=""><figcaption></figcaption></figure>

Once you see this confirmation screen, close the browser and return to your IDE.

Now [start using Tabnine](https://docs.tabnine.com/main/getting-started/quickstart)!
