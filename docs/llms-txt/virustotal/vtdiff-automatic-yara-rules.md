# Source: https://virustotal.readme.io/docs/vtdiff-automatic-yara-rules.md

# VTDIFF - Automatic YARA rules

VTDIFF helps threat analysts in creating YARA rules by automating the identification optimal patterns to detect groups of files (malware families, threat campaigns, threat actor toolset). These patterns can be used in [Livehunt](https://virustotal.readme.io/docs/livehunt) YARA rules, [Retrohunt](https://virustotal.readme.io/docs/retrohunt) jobs and [VT GREP](https://virustotal.readme.io/docs/vtgrep) content searches. 

\*\*What do you mean by optimal?\*\*VTDIFF takes into account binary sequence prevalence across the entire VirusTotal dataset in order to make sure it does not suggest patterns that are shared by a large number of files, e.g. the DOS stub in portable executables: "*The program Cannot be run in DOS mode*". In other words, VTDIFF tries to generate patterns that will not produce false positives. 

Answers to other frequently asked questions can be found in the [VTDiff FAQ](https://virustotal.readme.io/docs/how-does-vtdiff-work) section.

# Accessing VTDIFF

VTDIFF has two main entry points. Given a **VT Enterprise file search, you can select a group of files** by acting on their checkboxes, this will activate the VTDIFF button in the tools menu:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_send_20231009.png",
        null,
        "VTDiff send"
      ],
      "align": "center"
    }
  ]
}
[/block]

You can also get to VTDIFF by using the **left navigation bar** in VT Enterprise:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_navigationbar_20231009.png",
        null,
        "VTDiff navigation bar"
      ],
      "align": "center"
    }
  ]
}
[/block]

This will then take you to your historical VTDIFFs view, where you can set up a new session:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_newsession_20231009.png",
        null,
        "VTDiff new session"
      ],
      "align": "center"
    }
  ]
}
[/block]

A session modal will open up allowing you to specify a list of hashes to match and also a list of hashes to exclude, that will fine tune your job:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_createsession_20231009.png",
        null,
        "VTDiff send"
      ],
      "align": "center"
    }
  ]
}
[/block]

# VT Enterprise search list workflow

Let’s imagine our starting point is a single hash, a malicious document that drops second stage payload via macros. The hash is:

[45cfff04a95b3c40e2e8ee4b9c9ae1e75448f27eb119c079973e8a4b4459c930](https://www.virustotal.com/gui/file/45cfff04a95b3c40e2e8ee4b9c9ae1e75448f27eb119c079973e8a4b4459c930/detection)

In order to be able to build an optimal rule to detect this file and other variants of the same campaign/family we first need to identify a collection of files belonging to such family. 

We can pinpoint other variants by making use of the different clustering mechanisms that VT Intelligence provides ([vhash, imphash, ssdeep, icon/thumbnail vizhash, antivirus labels, distinctive static properties, etc.](https://virustotal.readme.io/docs/file-search-modifiers)). In this case we are going to pivot to other documents with the exact same visual layout by clicking on the file’s thumbnail:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_thumbnail_20231009.png",
        null,
        "VTDiff thumbnail"
      ],
      "align": "center"
    }
  ]
}
[/block]

This will trigger the following search:

<https://www.virustotal.com/gui/search/main_icon_dhash:7e12021282222000/files>

By hovering over the detection ratio you will see that the antivirus labels do indeed confirm that the matches belong to the same malware family. Similarly, the thumbnail of the files in the list clearly indicate that they have the very same visual layout. 

Select the first 8 matches:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_checkboxes_20231009.png",
        null,
        "VTDiff checkboxes"
      ],
      "align": "center"
    }
  ]
}
[/block]

When you do so, the VTDIFF icon in the tools menu bar activates itself:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_send2_20231009.png",
        null,
        "VTDiff send"
      ],
      "align": "center"
    }
  ]
}
[/block]

Click on it in order to set up a VTDIFF session for those hashes. Commonly abused file types such as documents do not require you to provide a list of hashes to exclude, the backend will set up an exclusion list automatically. **If you want to refine the VTDIFF session and avoid false positives produced in previous VTDIFF jobs, you can use the exclusion list**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_exclusion_20231009.png",
        null,
        "VTDiff exclusion list"
      ],
      "align": "center"
    }
  ]
}
[/block]

Launch the session. A VTDIFF job generally takes under a minute to conclude. Note that this is a heavy process, VTDIFF will iterate over all files provided with sliding windows of different sizes, checking whether binary subsequences are common to the selection and whether these are not too noisy when considering the entire VirusTotal dataset.

A list of binary patterns will be produced:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_patterns_20231009.png",
        null,
        "VTDiff patterns"
      ],
      "align": "center"
    }
  ]
}
[/block]

Note that you can click on the search icon next to each binary pattern in order to trigger an n-gram [content search](https://virustotal.readme.io/docs/vtgrep) for it:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_vtgrep_20231009.png",
        null,
        "VTDiff vtgrep"
      ],
      "align": "center"
    }
  ]
}
[/block]

This will allow you to understand the kind of files that match each pattern and whether they are prone to false positives. You can also easily search for an AND combination of some of them, which will probably be far more effective than an individual search. Select the first three patterns and click on the search icon in the top actions menu bar:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_patternssearch_20231009.png",
        null,
        "VTDiff patterns search"
      ],
      "align": "center"
    }
  ]
}
[/block]

That will trigger for files that contain those 3 binary patterns. VirusTotal maintains a 5PB n-gram index to power lightning-fast content searches:

<https://www.virustotal.com/gui/search/content:%7BF95F6482C9A84C7ECF0E2ACF43E422397578580CBA4D5BA8A23CD76E1DA9105538BA68249AB0CC2D359E76AF9A164392EBDBAF6543A5DAEBA8E72183BA84119A%7D%20AND%20content:%7B62463C65465A7A464C66467C6827446746%7D%20AND%20content:%7B776F72642F6D656469612F696D616765312E746966%7D>

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_thumbnails_20231009.png",
        null,
        "VTDiff thumbnails"
      ],
      "align": "center"
    }
  ]
}
[/block]

Judging by the thumbnails, sizes, antivirus results, tags, etc. it is clear that those three binary patterns have done a good job at finding other variants of the family/campaign. It is now clear that these patterns can be used to build a YARA rule or Retrohunt to either be notified of any new future file upload that belongs to this family or to map out the entire historical campaign. Livehunt YARA rules and Retrohunt jobs can also be set up using the top actions menu in VTDIFF listings:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_hunting_20231009.png",
        null,
        "VTDiff hunting"
      ],
      "align": "center"
    }
  ]
}
[/block]

One last word, note that the top actions menu also allows you to filter the patterns in order to focus exclusively on certain categories:

 

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_filter_20231009.png",
        null,
        "VTDiff filter"
      ],
      "align": "center"
    }
  ]
}
[/block]

 

# Hash list workflow

Sometimes you might want to create a VTDIFF session based on a list of pre-existing hashes, your starting point will no longer be a VT Intelligence search. In these cases you will use the navigation sidebar to access directly access VTDIFF:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_navbar_20231009.png",
        null,
        "VTDiff navbar"
      ],
      "align": "center"
    }
  ]
}
[/block]

The landing page allows you to create a new VTDIFF session. This requires you to copy\&paste the list of hashes to match in the inclusion text area.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-hunting/vtdiff_hashes_20231009.png",
        null,
        "VTDiff hashes"
      ],
      "align": "center"
    }
  ]
}
[/block]

**Exclusion hash lists will only be needed for less prevalent file types, however, even if exclusions are not required, you might often want to set up your own selection in order to filter out files that match previous iterations of a VTDIFF job that caused false positives.**

Note that the VTDIFF landing site lists the historical VTDIFF jobs that you launched in the past, this allows you to continue working with the identified patterns at a later stage and can come in handy if you mistakenly closed the browser tab.

From this point onward the workflow is exactly the same as the one described in the [previous section](#vt-enterprise-search-list-workflow).

To learn more about VTDIFF please refer to the [Frequently Asked Questions](https://virustotal.readme.io/docs/how-does-vtdiff-work).