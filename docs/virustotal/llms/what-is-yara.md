# Source: https://virustotal.readme.io/docs/what-is-yara.md

# What is YARA?

[YARA](https://virustotal.github.io/yara-x/) is an open-source tool designed to help malware researchers identify and classify malware samples. It makes it possible to create descriptions (or *rules*) for malware families based on textual and/or binary patterns. YARA is multi-platform, running on Linux, Windows and Mac OS X. It can be used through its command-line interface or from Python scripts with the YARA-Python extension.

Let's see an example:

```
rule silent_banker : banker  
{
    meta:
        description = "This is just an example"
        thread_level = 3
        in_the_wild = true

    strings:
        $a = {6A 40 68 00 30 00 00 6A 14 8D 91}
        $b = {8D 4D B0 2B C1 83 C0 27 99 6A 4E 59 F7 F9}
        $c = "UVODFRYSIHLNWPEJXQZAKCBGMT"

    condition:
        $a or $b or $c
}

```

The above rule is telling YARA that any file containing one of the three strings must be reported as *silent\_banker*. This is just a simple example, more complex and powerful rules can be created by using wild-cards, case-insensitive strings, regular expressions, special operators and many other features that you'll find explained in [YARA's documentation](https://virustotal.github.io/yara-x/docs/intro/getting-started/).

For more information about YARA please visit its official website: <https://virustotal.github.io/yara-x/>. If you would rather want to use Yara on VirusTotal's incoming submissions in order to identify malware families for in-depth study, you may want to learn more about [VirusTotal Hunting](https://virustotal.readme.io/docs/whats-vthunting).