# Source: https://jam.dev/docs/record-a-jam/instant-replay.md

# Instant Replay

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FZDFlIjSNIg59J2kzOtU6%2Finstantreplay.gif?alt=media&#x26;token=bcc33065-eb09-4746-8f36-eed62d2fcc81" alt=""><figcaption></figcaption></figure>

### Overview

Instant Replay captures bugs the moment they happen, with complete technical context, and packages everything into a shareable link. No need to stop your workflow or recreate issues. In just two clicks you'll be able to send engineers everything they need to debug.<br>

### Key Benefits

* **Complete technical context:** Automatically captures DOM replay, console logs, network requests, and device information
* **Zero workflow disruption:** Capture bugs instantly without stopping to recreate or re-record
* **Engineer-ready format:** All diagnostics packaged into one shareable link for tickets or direct communication
* **Privacy controls:** Crop video content before sharing to protect sensitive information<br>

### How It Works

When you create an Instant Replay, Jam automatically captures and includes:

* **Up to 2 minutes** of DOM session replay
* **Console logs** with errors and warnings
* **Network requests** with full inspection capabilities
* **Environment details:** URL, timestamp, country, device, OS, browser
* **Technical specs:** Viewport size and network speed

Everything gets packaged into a single link that integrates seamlessly with your existing bug tracking workflow.

#### Capture Behavior

{% hint style="info" %}
Instant Replay captures up to 2 minutes of session activity. For newly opened tabs or data-heavy websites, the capture duration may be shorter.
{% endhint %}

#### Privacy Controls

Before sharing your Instant Replay, you can crop the video to remove any sections you don't want to include. This gives you complete control over what technical context gets shared with your team.

#### Technical Limitations

<table><thead><tr><th>Scenario</th><th>Capture Duration</th><th data-hidden></th></tr></thead><tbody><tr><td>Standard browsing</td><td>Up to 2 minutes</td><td></td></tr><tr><td>Newly opened tabs</td><td>May be less than 2 minutes</td><td></td></tr><tr><td>Data-heavy websites</td><td>May be less than 2 minutes</td><td></td></tr></tbody></table>

<details>

<summary>How far back can Instant Replay capture?</summary>

Up to 2 minutes of session activity, though this may be shorter for newly opened tabs or websites with heavy data loads.

</details>

<details>

<summary>Can I control what gets shared in my Instant Replay?</summary>

Yes. You can crop the video portion of your Instant Replay before sharing to remove any content you don't want included.

</details>

<details>

<summary>What technical information is automatically included?</summary>

Every Instant Replay includes DOM session replay, console logs, network requests, URL, timestamp, device information, browser details, and viewport size.

</details>
