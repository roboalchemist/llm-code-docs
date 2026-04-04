# Source: https://docs.bugbug.io/running-tests/test-your-local-build-or-protected-web-page-using-ngrok.md

# Test your local build or protected web page using ngrok

You can use BugBug to test your local build or private site with restricted access. For this action, you have to use a third-party tool like ngrok.&#x20;

{% hint style="info" %}
ngrok is **not** part of BugBug. It's a 3rd party tool that exposes your website to a public URL address. Before you decide to use this tool, you may want to contact your network administrator.
{% endhint %}

ngrok opens a dedicated, secure tunnel that publicizes your local port for Internet access. When your local build or protected page is accessible through the public URL address created by ngrok, BugBug can open that site through a dedicated URL and start running tests or help you record steps.

### Set up ngrok&#x20;

First, visit a ngrok website and download the application to set up a tool, then unzip it to a designated location.

When you launch ngrok, you will need to provide an auth token. You need to register and open your account on the ngrok website.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F77YucDF70YsYnacOGNSE%2Fng%20auth%20token.png?alt=media&#x26;token=0804357e-e579-4bb4-aac2-2cb1ab26db16" alt=""><figcaption></figcaption></figure>

Then open a ngrok command-line shell and copy-paste the command&#x20;

<pre><code><strong>$ ./ngrok config add-authtoken {{yourAuthToken}}
</strong></code></pre>

### Fire up the ngrok&#x20;

Once you have opened and configured the auth token for ngrok, you can publish your local build or private page to the public.

#### Set up your local build and verify the localhost port.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdOc21hLl0FptbfoGAuY9%2FZrzut%20ekranu%202023-04-21%20095724.png?alt=media&#x26;token=f2e17c00-48a4-46a5-b25d-b4886c515ed7" alt=""><figcaption></figcaption></figure>

Then enter in your terminal **ngrok** command with the port related to your application, e.g., for **3000**:

```
$ ./ngrok http 3000
```

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FLyRKAa1MOaM0bSTVUljo%2FZrzut%20ekranu%202023-04-20%20155026.png?alt=media&#x26;token=e08c0c19-0e63-4b5f-bff2-8292df16208c" alt=""><figcaption></figcaption></figure>

Then ngrok opens a secure tunnel where your local build gets a public URL that can be used in BugBug tests (screenshot below).<br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F17wld6wsZR8JRD5FNZMy%2FZrzut%20ekranu%202023-04-21%20100114.png?alt=media&#x26;token=b3f69e44-6118-4663-a195-24ff2593e6d8" alt=""><figcaption><p>You can check out it in the browser. </p></figcaption></figure>

#### If your page is on a private server&#x20;

**If the website is running on a private server** then you are likely using a URL like `http://private.mycompany.com` to access it. In this case, you’ll create a tunnel to that URL using this command (with the private server URL swapped in):

```
$ ./ngrok http -host-header=rewrite private.mycompany.com:80
```

ngrok will print the same connection status to the console as above, with the public URL that is accessible to BugBug.&#x20;

### Record a test &#x20;

Once you successfully create a public URL with your local build or protected page, you can start recording tests with BugBug. Just use a URL provided by ngrok at the beginning of the process.<br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNTeLBaml8TwbIOsbOWL3%2FZrzut%20ekranu%202023-04-21%20102545.png?alt=media&#x26;token=bc256662-5461-494d-9040-1b8b2ee441c4" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
On the free plan, ngrok changes the URL each time it is restarted. So you need to update the test URL when ngrok provides a new one.
{% endhint %}

If you want to avoid this problem, you can use paid plans and set up a dedicated domain for your account. See the [ngrok doc](https://ngrok.com/docs/guides/how-to-set-up-a-custom-domain/) for more information.

To easily update the URL address follow these steps.

1. Open a test and go to the first step.&#x20;
2. Then change the URL address <br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FraznaE9fpfgOsT0Hy0xE%2Fng%20url.png?alt=media&#x26;token=5dd26400-4124-4b98-874a-e76e5fdad61e" alt=""><figcaption></figcaption></figure>

To make it easier to maintain a large number of tests, use a local variable that helps you to change the URL only in one place for all tests that use it.

<div><figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FDFG8T0C08BpSte1zPurz%2FZrzut%20ekranu%202023-04-21%20104317.png?alt=media&#x26;token=f61b6625-90b7-41a6-b180-75eedb0f6709" alt=""><figcaption><p>Create a variable </p></figcaption></figure> <figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F3hvknFbC5iLgyXHuUGSB%2FZrzut%20ekranu%202023-04-21%20104402.png?alt=media&#x26;token=1e77596f-ca7d-4c0f-9d8a-b71da2b88ccd" alt=""><figcaption><p>Use it in test </p></figcaption></figure></div>

For more info about variables, please visit [Variables](https://docs.bugbug.io/editing-tests/variables) in our documentation.

### Alternatives

Like many solutions, ngrok has alternatives, and you can choose something else.

* [Serveo](http://serveo.net/)
* [Localhost](http://localhost.run/)
* [Cloudfared](https://github.com/cloudflare/cloudflared)
* [LocalTunnel](https://github.com/localtunnel/localtunnel)
