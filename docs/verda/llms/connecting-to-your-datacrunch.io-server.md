<!-- Source: https://docs.verda.com/cpu-and-gpu-instances/connecting-to-your-datacrunch.io-server.md -->

# Connecting to Your Server

After setting up your server, you receive access using the IP address stated in the console. You can also easily copy the SSH login from the instance card or overview page.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-ea751af91abc81f6a236dafdfad7b61d8d94ed8c%2Flogin.png?alt=media" alt=""><figcaption></figcaption></figure>

If you are using a command line tool/terminal, you can connect to your instance using the following command:

```bash
ssh -i /path/to/your/key/id_rsa root@135.181.63.202
```

Alternatively, you can use your favorite SSH client to connect to the server. Below is an example using Putty:

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-d2fed88305be1f05e1aac4e1c551934f3079baea%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Add your server info to Putty and click `Save`. After saving, you will need to add your private key:

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-c474cd81d8a4ddecd8c8b114ad32b39176503c8f%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Add your key, go back to `session` and save again. Don’t forget to click save again on `session`, or your private key won’t be saved!

Next, we click `Open` and are greeted with our login screen. Use username `root` to proceed. If you used an authentication key with a passphrase, you will be prompted to type it in. You should now be logged in now!

{% hint style="info" %}
Tip: You can paste text into your terminal in Putty by right-clicking. You can copy things from your terminal to your Windows desktop by just selecting text (no need to press `ctrl+c` or copy), it will save the text in the clipboard.
{% endhint %}
