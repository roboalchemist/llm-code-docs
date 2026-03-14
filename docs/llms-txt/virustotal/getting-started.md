# Source: https://virustotal.readme.io/reference/getting-started.md

# Getting started

In order to use the API you must [sign up to VirusTotal Community](https://www.virustotal.com/gui/join-us). Once you have a valid VirusTotal Community account you will find your personal API key in your personal settings section. This key is all you need to use the VirusTotal API.

> ❗️ Important
>
> The VirusTotal public API must not be used in commercial products or services. It can not be used as a substitute for antivirus products and it can not be integrated in any project that may harm the antivirus industry directly or indirectly. Noncompliance of these terms will result in immediate permanent ban of the infractor individual or organization.
>
> Under all circumstances VirusTotal's [Terms of Service](https://virustotal.readme.io/docs/terms-of-service) and [Privacy Policy](https://virustotal.readme.io/docs/privacy-policy) must be respected.

By default any VirusTotal Community registered user is entitled to an API key that allows them to interact with a basic set of endpoints. Advanced calls and higher limits are available via the premium API, which requires special privileges. [Contact us](https://www.virustotal.com/gui/contact-us/premium-services) if you would like to learn more about how to obtain access.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/73a8178-Screen_Shot_2019-10-16_at_3.51.46_PM.png",
        "Screen Shot 2019-10-16 at 3.51.46 PM.png",
        1028
      ],
      "align": "center",
      "sizing": "smart",
      "border": true
    }
  ]
}
[/block]

## Most popular API endpoints

* [Upload a file for scanning](https://virustotal.readme.io/reference/files-scan): analysis your file with 70+ antivirus products, 10+ dynamic analysis sandboxes and a myriad of other security tools to produce a threat score and relevant context to understand it.
* [Get a file report by hash](https://virustotal.readme.io/reference/file-info): given a {md5, sha1, sha256} hash, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products, 10+ dynamic analysis sandboxes and a myriad of other security tools and datasets.
* [Scan URL](https://virustotal.readme.io/reference/scan-url): analysis your URL with 70+ antivirus products/blocklists and a myriad of other security tools to produce a threat score and relevant context to understand it.
* [Get a URL analysis report](https://virustotal.readme.io/reference/url-info): given a URL, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.
* [Get a domain report](https://virustotal.readme.io/reference/domain-info): given a domain, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.
* [Get an IP address report](https://virustotal.readme.io/reference/ip-info): given an IP address, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.