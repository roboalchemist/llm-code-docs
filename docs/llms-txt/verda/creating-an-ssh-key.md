<!-- Source: https://docs.verda.com/cpu-and-gpu-instances/creating-an-ssh-key.md -->

# Managing SSH Keys

## Creating an SSH Key

### Linux

Run the following in your terminal:

```bash
ssh-keygen -t ed25519
```

By default, the key will be stored in `$HOME/.ssh/id_ed25519`, you can change the location if needed. You will be prompted for a passphrase next.

{% hint style="info" %}
In general, it is a good idea to set a passphrase for your private key.
{% endhint %}

If you used the default key name it is now saved in `$HOME/.ssh/id_ed25519.pub`

To view your public key, type:

```bash
 cat .ssh/id_ed25519.pub
```

You can now add your public key to your project to be available when creating new instances.

Go to `Keys -> SSH Keys -> Create` and paste your key into the window that looks like this:

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-d6a00c8bd18028b8e8e24cb2813b7a239333fd2b%2FSSH%20key.png?alt=media" alt=""><figcaption></figcaption></figure>

Next, you can add your key, deploy your server and your key will automatically be allowed on your instance!

### Windows

When setting up compute, you need to provide an SSH key to provide secure access to your server.

Here, you will learn how to create such a key using PuttyGen.

When installing Putty, you can choose to install PuttyGen as well, so let's fire it up:

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-bb39f9fd6a0b8eee19187b96a7886da848519389%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

We choose `Ed25519` as the type of key, and click 'Generate'. Move your cursor over the grey area, and your key will appear.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-ab0ac0aa6339c6048f536034a93c3211ab309094%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Don't forget to add a passphrase to your keys!
{% endhint %}

Copy the output in the `Public key` field on top and **save your private key somewhere safe.** You can use PuttyGen to re-generate your public key from your private key but not vice versa; hence, we only need to save the private key.

When creating your server, you can paste the output in the Key input field.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-d6a00c8bd18028b8e8e24cb2813b7a239333fd2b%2FSSH%20key.png?alt=media" alt=""><figcaption></figcaption></figure>

Next, you can add your key, deploy your server and your key will automatically be allowed on your instance!

***

## Add/remove SSH key to existing instance

Log into the instance.

Edit the file `/root/.ssh/authorized_keys` and add the new key in a new line, or remove an existing key.
