# Source: https://docs.bugbug.io/troubleshooting/vpn-or-a-firewall.md

# VPN or a Firewall

If your app [environment](https://docs.bugbug.io/editing-tests/variables#work-with-different-development-environments) is not publicly available, for example only available in your local network or a private network with a VPN or behind a firewall, you can't run the [cloud tests](https://docs.bugbug.io/running-tests/in-cloud-on-server) because BugBug will not be able to access your app. You have several potential workarounds though.&#x20;

{% hint style="warning" %}
Recommended solution:\
\
Set your VPN/Firewall/Server settings to allow BugBug to connect from our IP range. You can find the IP list here:[ BugBug IP list](https://app.bugbug.io/api/v1/config/ips/)&#x20;
{% endhint %}

{% hint style="info" %}
We provide an IP list generated from the API in case of feature changes on our site. Please do not hardcode it to avoid future problems. Use API response. We are still developing for the better.&#x20;
{% endhint %}

## **Other options:**&#x20;

### **Solution A:** Publish your app but protect it with a password

Use a tool such as [ngrok.com](https://ngrok.com/) and publish your app publicly at the specific password-protected subdomain with authentication. More about ngrok? See [our documentation](https://docs.bugbug.io/running-tests/test-your-local-build-or-protected-web-page-using-ngrok) on setting up this tool

### Solution B: Add an exception in your firewall/VPN

Let in BugBug based on custom headers or custom user-agent.&#x20;

1. In the project settings set your custom header to some shared secret value
2. In your VPN/Firewall/Server settings add a rule to allow traffic with headers containing this shared secret

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8YJettgG4aJVAXuR7L6d%2FZrzut%20ekranu%202023-03-17%20104152.png?alt=media&#x26;token=5f613d89-5940-40ef-8234-9a16d2afc9d0" alt=""><figcaption></figcaption></figure>

### **Solution C: run tests locally**&#x20;

You can still [execute the tests manually](https://docs.bugbug.io/running-tests/test-in-your-browser) on a machine that has access to the app environment. The disadvantage is that you can't [schedule tests](https://docs.bugbug.io/running-tests/schedules).

{% hint style="danger" %}
**Upcoming feature:** we are working on a command line interface that would allow you to run BugBug tests remotely on your own internal development server.
{% endhint %}
