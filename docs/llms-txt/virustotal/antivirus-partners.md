# Source: https://virustotal.readme.io/reference/antivirus-partners.md

# Antivirus Partners

VirusTotal Monitor Partner's aim is to ease false positive handling by antivirus companies. It is designed to provide VirusTotal participating AV scanners with hashes, file content, metadata and ownership information for any detection of a file in a Monitor collection. Note that files will only be shared upon a false positive.

As stated in [VirusTotal Monitor overview](#monitor-overview) software developers having an account in Monitor can upload their goodware collection to be periodically analysed by participating antivirus scanners. Note that these accounts are handed over to users once VirusTotal staff verifies and identifies them. Any of the hashes detected by your engine will be available in the [Monitor Partner webapp](https://www.virustotal.com/monitor-partners/) or via the API calls documented bellow.

A common flow is described below:

* A Monitor account is handed over to a user.
* Users upload some files and make some comments on them in the details metadata section.
* At some point in time or just after being uploaded a file is detected by your engine.
* A new hash appears in the [/hashes](#monitorpartner-hashes) endpoint or in the [website Analyses tab](https://www.virustotal.com/monitor-partners/analyses).
* You request [items](#monitorpartner-hashes-items) to get files with that particular hash from any user collection, a hash could appear in different collections with different details. This situation (one hash/many files) may happen for example because sometimes software developers include certain versions of operating system files with their binaries, so one owner may be the operating system developer and the rest some other software developers. The details about each item owner can be obtained requesting the [Monitor API endpoint](#monitor-items-owner).
* You can also request [hash analyses](#monitorpartner-hashes-analyses) to get hash historic scanning information.
* Once a false positive is confirmed your engine signatures may be updated and in the next cycle and the hash will disappear from the Analyses.
* Alternatively, you can confirm that the detection is correct and hide it from your analyses posting
  a [comment](#monitorpartner-hashes-comments) over it. You can always access these hashes filtering with ignored tag over [hashes](#monitorpartner-hashes) and revert this action.

For your convenience we generate a [daily CSV](#monitorpartner-detectionsbundle-download) formatted file with company name, hash and url with your detections. A new bundle is available each day at 1am UTC.
Additionally you can use this **[example python script](https://www.virustotal.com/monitor-partners/tools/vt_monitor_partner_downloader.py)** to generate a similar report for your account at the current time, it will download all related hash files and its metadata storing it on your filesystem in json format.

You can also access information about your engine detections and collection size in daily statistics.

Here are some Monitor Partner website captures:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/28e40d5-VirusTotal_Monitor_Partners_-_Google_Chrome_185.png",
        "VirusTotal Monitor Partners - Google Chrome_185.png",
        1388,
        985,
        "#eaeaeb"
      ]
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e9f9d2f-VirusTotal_Monitor_Partners_-_Google_Chrome_186.png",
        "VirusTotal Monitor Partners - Google Chrome_186.png",
        1388,
        985,
        "#e7e8ed"
      ]
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6c3cf73-VirusTotal_Monitor_Partners_-_Google_Chrome_187.png",
        "VirusTotal Monitor Partners - Google Chrome_187.png",
        1388,
        985,
        "#e7e9ed"
      ]
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6a4c0cc-VirusTotal_Monitor_Partners_-_Google_Chrome_188.png",
        "VirusTotal Monitor Partners - Google Chrome_188.png",
        1388,
        985,
        "#e7e8ec"
      ]
    }
  ]
}
[/block]