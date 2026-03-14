# Source: https://virustotal.readme.io/docs/higher-quota.md

# How can I have access to a higher quota?

Special privileges can be considered for honeypots, honeyclients and other projects providing resources (samples or URLs) to VirusTotal. If your are submitting hundreds new files per day from your honeypot, please don't hesitate to contact us for additional quota. If you have a smaller number of samples, some things you can do:

* Adjust your scripts to wait 30 to 60 seconds before retrying up to X times,  if you get a over quota 204 response code (api v2) or 429 (api v3).
* Implement logic to efficiently make use of your quota, for example:

1. Check the hash on VirusTotal to see if we have already analyzed it.
2. If we do not have the file upload and scan it.
3. Repeat steps 1 and 2 for all the files you want to check. This will ensure all  the files are on our scanning queue. Once all of your files have been uploaded, then poll us for results in the order you submitted the files.

VirusTotal also has a [premium API](https://docs.virustotal.com/reference/overview) to which you can subscribe. This API allows you, among other things, to have a higher rate and get additional information, you can read more at this [article](https://virustotal.readme.io/docs/difference-public-private).

If any of these alternatives suits your purposes do not hesitate to [contact us](https://www.virustotal.com/gui/contact-us/premium-services).