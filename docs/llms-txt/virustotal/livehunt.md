# Source: https://virustotal.readme.io/docs/livehunt.md

# Livehunt

<style>

.tbd {  
  background-color: lightgray;  
}  
table {  
  width: 100%;  
  padding: 5px 2px 11px 4px;  
  font-size: 12px;  
  vertical-align: top;  
}  
table td:first-child {  
  max-width: 200px;  
}  
table td:nth-child(2) {  
  max-width: 90px;  
  text-align: center;  
}  
table td:nth-child(3) {  
  max-width: 250px;  
}  
table td:nth-child(4) {  
  max-width: 250px;  
  font-family: monospace;  
}  
</style>

Livehunt allows you to hook into the stream of files analyzed by VirusTotal and get notified whenever one of them matches a certain rule written in the [YARA](https://virustotal.github.io/yara-x/) language. By applying YARA rules to the files analyzed by VirusTotal you should be able to get a constant flow of malware files classified by family, discover new malware files not detected by antivirus engines, collect files written in a given language or packed with a specific run-time packer, create heuristic rules to detect suspicious files, and, in general, enjoy the benefits of YARA's versatility acting on the huge amount of files processed by VirusTotal every day.

Livehunt applies your YARA rules to every file analyzed by VirusTotal, both when the file is submitted by some user, and when a file is re-analyzed. The difference between a submission and a re-analysis is that in the former case the user is in possession of the file and is uploading it to VirusTotal (not necessarily for the first time), in the latter case some existing file is being analyzed again. A submission always triggers an analysis, but files can be re-analyzed later without being submitted by a user.

When a file matches one of your rules, a notification is generated with details about the file and the matching rule.

Files that are larger than 100MB are not scanned by Livehunt at all.

[Creating Livehunt rules](#creating-livehunt-rules)\
[Livehunt notifications](#livehunt-notifications)\
[Writing YARA rules for Livehunt](#writing-yara-rules-for-livehunt)\
[Livehunt-specific variables](#livehunt-specific-variables)

# Creating Livehunt rules

Livehunt rules are organized into rulesets, which are simply a collection of YARA rules that share common settings, the total size of the rules in text form can not exceed 1MB. In order to create a new ruleset follow these steps:

1.  On the homepage, click on the **Hunting** menu at the top of the screen or the corresponding icon in the toolbar, either option leads you to the same place:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/livehunt_menu_20231009.png",
        null,
        "Livehunt menu"
      ],
      "align": "center"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/livehunt_menu_icon_20231009.png",
        null,
        "Livehunt menu"
      ],
      "align": "center"
    }
  ]
}
[/block]

2.  Then click on the **New Livehunt Ruleset** and choose the matching entity among files, URLs, IPs or domains:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/livehunt_new_20231009.png",
        null,
        "Livehunt New Ruleset"
      ],
      "align": "center"
    }
  ]
}
[/block]

3.  A window will be opened with a text editor in which you can write your YARA rules and control its settings. The image below illustrates the usage of this window.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/livehunt_editor_20231009.png",
        null,
        "Livehunt Editor"
      ],
      "align": "center"
    }
  ]
}
[/block]

1. Ruleset name.
2. You can use different templates or you can use a known file to create rules based on its attributes.
3. YARA rules
4. The matching entity.
5. You can share the ruleset to other members of the VirusTotal community.
6. The save rule button.
7. Enable/disable the ruleset. If the ruleset is disabled you won't receive any notifications from it.
8. Maximum number of notifications that you will receive from this ruleset in any given 24 hours period.
9. Add email addresses to receive notifications by email (one per line).
10. You can create a retrohunt job using this rule.
11. You can run tests of the ruleset among a list of specific hashes.

[Back to top](#top)

# Livehunt notifications

The [IOC Stream view](https://virustotal.readme.io/docs/ioc-stream-threat-feeds) is an evolution to the previous Livehunt Notifications view. This view allows users to digest the incoming VT flux into relevant threat feeds that you can study here or easily export to improve detection in your security technologies.

You will see different tabs for different Threat Feeds. Please check our [IOC Stream view](https://virustotal.readme.io/docs/ioc-stream-threat-feeds) for more details.

[Back to top](#top)

# Writing YARA rules for Livehunt

Livehunt uses an up-to-date version of YARA, which means that the [latest YARA documentation](https://virustotal.github.io/yara-x/docs/intro/getting-started/) is usually the place to go for a detailed description of the language and its features. However, there are a few things that you need to know while creating YARA rules specifically tailored for Livehunt.

* Rules for which YARA raise performance warnings are not accepted by Livehunt. Such rules are usually very slow and degrade the service both for you and the rest of the users.
* You can not use **include** statements in your rules.
* Standard modules currently supported are:
  * [**pe**](https://virustotal.github.io/yara-x/docs/modules/pe/)
  * [**elf**](https://virustotal.github.io/yara-x/docs/modules/elf/)
  * [**dotnet**](https://virustotal.github.io/yara-x/docs/modules/dotnet/)
  * [**lnk**](https://virustotal.github.io/yara-x/docs/modules/lnk/)
  * [**macho**](https://virustotal.github.io/yara-x/docs/modules/macho/)
  * [**math**](https://virustotal.github.io/yara-x/docs/modules/math/)
  * [**magic**](https://yara.readthedocs.io/en/latest/modules/magic.html)
  * [**hash**](https://virustotal.github.io/yara-x/docs/modules/hash/)
  * [**string**](https://virustotal.github.io/yara-x/docs/modules/string/)
  * [**time**](https://virustotal.github.io/yara-x/docs/modules/time/)
* **Important:** In addition to the standard modules enumerated above, you can also use the **vt** module. This module has been specifically created for Livehunt and Retrohunt and exposes additional information about the file being scanned. You can find more details about this in the following [article](https://virustotal.readme.io/docs/writing-yara-rules-for-livehunt).

[Back to top](#top)

# Livehunt-specific variables

YARA offers a mechanism for [defining custom variables](https://virustotal.github.io/yara-x/docs/writing_rules/external-global-variables/) that can be used later in your rule's condition statement. In Livehunt this mechanism is used for providing additional information about the file being scanned that can be used for creating more powerful rules.

Using these variables you can construct YARA rules that say things like: *"give me the files containing the strings 'foo' and 'bar', and detected by more than two antivirus vendors"* or *"give me the files detected by antivirus X"* or *"give me new files that antivirus X detects as 'baz'"*. The following examples speak for themselves:

```
rule Example\_1 {   
 strings:   
 $a = "dummy"   
 condition:   
 // Files containing 'dummy' and detected by Panda   
 $a and panda   
}  
```

```
rule Example\_2 {   
 condition:   
 // Files detected by Panda or F-Secure   
 panda or f\_secure   
} 
```

```
rule Example\_3 {   
 condition:   
 // Files detected by more than 10 engines.   
 positives > 10   
}
```

 

This is the full list of YARA variables defined by Livehunt:

| Variable    | Type    | Description                                                                                                                                                              |
| ----------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| file\_name  | string  | File's name as it was last submitted to VirusTotal.                                                                                                                      |
| file\_type  | string  | String that contains information about the file type, described in the table below.                                                                                      |
| imphash     | string  | File's import hash                                                                                                                                                       |
| md5         | string  | File's MD5                                                                                                                                                               |
| new\_file   | boolean | True if this is the first time the file is submitted to VirusTotal                                                                                                       |
| positives   | integer | Number of antivirus engines detecting the file                                                                                                                           |
| sha256      | string  | File's SHA-256                                                                                                                                                           |
| sha1        | string  | File's SHA-1                                                                                                                                                             |
| signatures  | string  | Detection signatures from all antivirus engines concatenated together and separated by spaces. This variable is normally used with **contains** or **matches** operators |
| submissions | integer | Number of times the file has been submitted to VirusTotal. The value is 1 for the first submission.                                                                      |
| ssdeep      | string  | File's [ssdeep](https://ssdeep-project.github.io/ssdeep/index.html) hash                                                                                                 |
| tags        | string  | File's tags concatenated together and separated by spaces.                                                                                                               |
| vhash       | string  | File's vhash                                                                                                                                                             |

This is the full list of available file types with the corresponding value of the *file\_type* variable.

| File type                               | Value of file\_type                                      |
| --------------------------------------- | -------------------------------------------------------- |
| OpenOffice Draw                         | document openoffice draw odg                             |
| Win32 EXE                               | executable windows win32 pe peexe                        |
| Win32 DLL                               | executable windows win32 pe pedll                        |
| Windows Installer                       | installer windows msi                                    |
| E-book                                  | document ebook epub                                      |
| LaTeX                                   | document latex                                           |
| TrueType Font                           | font truetype ttf                                        |
| Embedded OpenType font                  | font opentype eof                                        |
| Web Open Font Format                    | font openfont woff                                       |
| Compiled HTML Help                      | chm help                                                 |
| Win16 EXE                               | executable windows win16 ne neexe                        |
| Win16 DLL                               | executable windows win16 ne nedll                        |
| Shell script                            | script shell                                             |
| DOS EXE                                 | executable dos mz                                        |
| DOS COM                                 | executable dos com                                       |
| AWK                                     | source awk                                               |
| COFF                                    | executable coff                                          |
| ELF                                     | executable linux elf                                     |
| Linux kernel                            | linux                                                    |
| Linux RPM package                       | linux rpm                                                |
| Linux                                   | linux                                                    |
| Mach-O                                  | executable mac macho                                     |
| Java Bytecode                           | executable java-bytecode class                           |
| Macintosh Disk Image                    | executable mac dmg                                       |
| Debian Package                          | executable linux deb                                     |
| Apple software package                  | executable mac pkg                                       |
| ZIP                                     | compressed zip                                           |
| GZIP                                    | compressed gzip                                          |
| BZIP                                    | compressed bzip                                          |
| RZIP                                    | compressed rzip                                          |
| DZIP                                    | compressed dzip                                          |
| 7ZIP                                    | compressed 7zip                                          |
| Windows shortcut                        | windows lnk                                              |
| JAR                                     | compressed jar                                           |
| RAR                                     | compressed rar                                           |
| MS Compress                             | compressed mscompress                                    |
| ACE                                     | compressed ace                                           |
| ARC                                     | compressed arc                                           |
| ARJ                                     | compressed arj                                           |
| ASD                                     | compressed asd                                           |
| BlackHole                               | compressed blackhole                                     |
| KGB                                     | compressed kgb                                           |
| ZLIB                                    | compressed zlib                                          |
| TAR                                     | compressed tar                                           |
| Google Chrome Extension                 | crx chrome extension browser                             |
| Mozilla Firefox Extension               | xpi firefox extension browser                            |
| HTML                                    | internet html                                            |
| XML                                     | internet xml                                             |
| Flash                                   | internet flash swf                                       |
| FLA                                     | multimedia video fla                                     |
| IE cookie                               | internet iecookie                                        |
| BitTorrent link                         | internet bittorrent                                      |
| Email                                   | internet email                                           |
| Outlook                                 | internet email outlook                                   |
| JPEG                                    | multimedia image jpeg jpg                                |
| TIFF                                    | multimedia image tiff                                    |
| GIF                                     | multimedia image gif                                     |
| PNG                                     | multimedia image png                                     |
| BMP                                     | multimedia image bmp                                     |
| GIMP                                    | multimedia image gimp                                    |
| Adobe InDesign                          | multimedia image indesign                                |
| Adobe Photoshop                         | multimedia image photoshop psd                           |
| Targa                                   | multimedia image targa                                   |
| XWS                                     | multimedia image xwd                                     |
| DIB                                     | multimedia image dib                                     |
| JNG                                     | multimedia image jng                                     |
| ICO                                     | multimedia image ico                                     |
| FlashPix                                | multimedia image fpx                                     |
| EPS                                     | multimedia image eps                                     |
| SVG                                     | multimedia image svg                                     |
| Windows Enhanced Metafile               | multimedia image emf                                     |
| AppleDouble Format                      | apple appledouble                                        |
| C                                       | source c                                                 |
| C++                                     | source cpp                                               |
| Text                                    | text                                                     |
| Script                                  | script                                                   |
| PHP                                     | source php                                               |
| Python                                  | source python                                            |
| Perl                                    | source perl                                              |
| Ruby                                    | source ruby                                              |
| OGG                                     | multimedia video ogg                                     |
| FLC                                     | multimedia animation flc                                 |
| FLI                                     | multimedia animation fli                                 |
| MP3                                     | multimedia audio mp3                                     |
| FLAC                                    | multimedia audio flac                                    |
| WAV                                     | multimedia audio wav                                     |
| MIDI                                    | multimedia audio midi                                    |
| AVI                                     | multimedia video avi                                     |
| MPEG                                    | multimedia video mpeg                                    |
| QuickTime                               | multimedia video quicktime qt                            |
| ASF                                     | multimedia video asf                                     |
| DivX                                    | multimedia video divx                                    |
| FLV                                     | multimedia video flv                                     |
| WMA                                     | multimedia audio wma                                     |
| WMV                                     | multimedia video wmv                                     |
| RealMedia                               | multimedia video realmedia rm                            |
| MOV                                     | multimedia video mov                                     |
| MP4                                     | multimedia audio mp4                                     |
| 3GP                                     | multimedia video 3gp                                     |
| Dyalog                                  | source dyalog                                            |
| Fortran                                 | source fortran                                           |
| ROM BIOS                                | rom bios firmware                                        |
| Symbian                                 | executable mobile symbian                                |
| Network capture                         | internet cap pcap                                        |
| ISO image                               | compressed isoimage                                      |
| PDF                                     | document pdf                                             |
| PostScript                              | document ps postscript                                   |
| MS Word Document                        | document msoffice text word doc                          |
| Office Open XML Document                | document msoffice text word docx                         |
| MS PowerPoint Presentation              | document msoffice presentation powerpoint ppt            |
| Office Open XML Presentation            | document msoffice presentation powerpoint pptx           |
| MS Excel Spreadsheet                    | document msoffice spreadsheet excel xls                  |
| Office Open XML Spreadsheet             | document msoffice spreadsheet excel xlsx                 |
| Rich Text Format                        | document msoffice text word rtf                          |
| Office Open XML Slide Show              | document msoffice presentation powerpoint slideshow ppsx |
| Java                                    | source java                                              |
| Apple related                           | apple apple-gen                                          |
| Macintosh related                       | apple macintosh mac macintosh-gen                        |
| AppleSingle Format                      | apple applesingle                                        |
| CAB                                     | compressed cab                                           |
| Macintosh HFS                           | apple macintosh mac machfs                               |
| Apple Plist                             | apple appleplist                                         |
| Macintosh Library                       | apple mac maclib                                         |
| Pascal                                  | source pascal                                            |
| PalmOS                                  | executable mobile palmos                                 |
| WinCE                                   | executable mobile wince                                  |
| Android                                 | executable mobile android apk                            |
| iPhone                                  | executable mobile iphone ios                             |
| OpenOffice Presentation                 | document openoffice presentation odp                     |
| OpenOffice Spreadsheet                  | document openoffice spreadsheet ods                      |
| OpenOffice Document                     | document openoffice text odt                             |
| Hangul (Korean] Word Processor document | document hangul text hwp                                 |
| Samsung document                        | document samsungdoc text gul                             |
| OpenOffice Math                         | document openoffice math odf                             |

[Back to top](#top)