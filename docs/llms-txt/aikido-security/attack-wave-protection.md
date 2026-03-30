# Source: https://help.aikido.dev/zen-firewall/zen-features/attack-wave-protection.md

# Attack Wave Protection

The internet is constantly being scanned by automated tools. Security scanners like Nuclei, ZAP, Wapiti, and SQLMap probe applications for weaknesses, looking for sensitive files, testing hidden directories, and injecting malicious payloads. These reconnaissance attempts flood your servers with requests that waste CPU cycles and generate endless 404 errors.

## How It Works

Zen automatically detects these attack waves in real time by spotting probing patterns. For example:

* An IP making 15 suspicious requests within a minute.
* Attempts to access files like .env or wp-config.php.
* Requests for hidden directories like .git/config.
* Payloads designed to trigger SQL injection errors.<br>

When this behavior is detected, Zen flags it as an attack wave. This shifts your security posture from reactive to proactive, giving you instant visibility into who is systematically probing your applications.<br>

## What You’ll See

A live feed in your Aikido dashboard showing which IPs are targeting your applications.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FzycjF2iKX7DnHby0MGfw%2FScreenshot%202025-09-03%20at%2017.54.04.png?alt=media&#x26;token=a18fcfc2-2837-4708-aedc-450bee1c0ed9" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FhqzLhoZEwhxhSv8ceTss%2FScreenshot%202026-01-05%20at%2012.36.30.png?alt=media&#x26;token=7668de2c-1c51-4f33-b94a-490b9ec069a6" alt=""><figcaption></figcaption></figure>

### Try It Yourself

You can easily simulate an attack wave to confirm Zen is working. Just click Simulate Attack in your dashboard and watch the events appear.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FvvmZN3cVwXwJZwqNdvUI%2FScreenshot%202025-09-03%20at%2016.19.25.png?alt=media&#x26;token=1df1fd5d-f170-44d6-9a80-018e002d4e71" alt=""><figcaption></figcaption></figure>
