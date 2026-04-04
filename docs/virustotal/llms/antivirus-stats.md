# Source: https://virustotal.readme.io/docs/antivirus-stats.md

# Why don't you have statistics comparing antivirus performance?

VirusTotal service was not designed as a tool to perform antivirus comparative analyses, but as a tool that checks suspicious samples with several antivirus solutions and helps antivirus labs by forwarding them the malware they fail to detect. Those who use VirusTotal to perform antivirus comparative analyses should know that they are making many implicit errors in their methodology, the most obvious being:

* VirusTotal's antivirus engines are command line versions, so depending on the product, they will not behave exactly the same as the desktop versions: for instance, desktop solutions may use techniques based on behavioral analysis and count with personal firewalls that may decrease entry points and mitigate propagation, etc.
* In VirusTotal desktop-oriented solutions coexist with perimeter-oriented solutions; heuristics in this latter group may be more aggressive and paranoid, since the impact of false positives is less visible in the perimeter. It is simply not fair to compare both groups.
* Some of the solutions included in VirusTotal are parametrized (in coherence with the developer company's desire) with a different heuristic/aggressiveness level than the official end-user default configuration.

These are just three examples illustrating why using VirusTotal for antivirus testing is a bad idea, you can read more about [VirusTotal and antivirus comparatives](http://blog.virustotal.com/2012/08/av-comparative-analyses-marketing-and.html) in our blog.