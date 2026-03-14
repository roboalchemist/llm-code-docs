# Source: https://virustotal.readme.io/reference/software-publishers.md

# Software Publishers

VirusTotal Monitor is designed to analyse goodware collections, helping antivirus companies and software developers with the early detection of false positives (mistakenly flagging legit files as malicious).

Software developers can upload their files to the service and they will be periodically scanned with the latest VirusTotal antivirus signature sets, notifying users in the event that any antivirus flags their files and keeping a historical record of all analyses performed on their software collection.

In order to simplify false positive management and allow fast remediation, VirusTotal Monitor gives antivirus companies access to detected file metadata (file hash, file name and path, detection signature, and other user provided information).

For this purpose it is crucial that the user has an accurate and updated profile, as this information is going to be shared with the scanner companies if, and only if, files are detected. There is an API endpoint where the user can tweak their monitor preferences. This process can also be completed through the VirusTotal Monitor user interface:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b8a8b0f-Selection_179.png",
        "Selection_179.png",
        1218,
        576,
        "#fbfbfb"
      ]
    }
  ]
}
[/block]

Additionally you can use this [example python script](https://www.virustotal.com/monitor/tools/vt_monitor_uploader.py) to upload your files, just provide a origin folder and a remote destination and will iterate over files in that directories and upload them to your monitor account. Use the "--help" parameter to obtain a list of upload modifiers.