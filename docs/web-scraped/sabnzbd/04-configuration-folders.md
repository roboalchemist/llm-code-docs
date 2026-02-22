# SABnzbd Configuration - Folders

## User Folders

OS-specific default locations for the settings below can be found [here](/wiki/advanced/directory-setup).

**Temporary Download Folder** | Enter the path to a folder SABnzbd can use to store files as they are downloaded. Once the file is complete, it will verify then extract to the Complete Folder. You can just enter "Incomplete" to keep it relative to your Base Folder or enter the full path such as `C:\Incomplete` and SABnzbd will create the folder.
---|---
**Minimum Free Space for Temporary Download Folder**
Advanced | There should be enough space to contain the largest complete job + 10% to repair jobs. When free space on the drive that holds the temporary folder is below this, SABnzbd is automatically pauses.
You enter the amount in bytes but you can use factors like `K, M, G` etc.
**Completed Download Folder** | The completed download folder is the default download location for all items, unless indicated otherwise from the [Categories](/wiki/configuration/4.5/categories) page.
**Minimum Free Space for Completed Download Folder**
Advanced | There should be enough space to contain the largest complete job and some more if the extracted files are larger when unpacked. When free space on the drive that holds the complete folder is below this, SABnzbd is automatically paused.
You enter the amount in bytes but you can use factors like `K, M, G` etc.
NOTE Will not work if a [category folder](/wiki/configuration/4.5/categories) is on a different disk than the main Complete Download Folder.
**Auto resume**
Advanced | Downloading will automatically resume if the minimum free space is available again. Applies to both the Temporary and Complete Download Folder. Checked every few minutes.
**Permissions for completed downloads**
Advanced | Set permissions pattern for completed files/folders using octal notation, for macOS and Linux only.
Example: `755` or `777`, see: [Unix permissions](/wiki/advanced/unix-permissions).
**Watched Folder** |  This is a folder that is periodically checked for new NZB files. When a file is stored in this folder, SABnzbd will consider this a download job. It will scan the folder and processes the supported files: `.nzb, .gz, or .bz2` and archives `.zip, .rar, or .7z,`. The process will add the NZB to the queue and remove the file from the watched folder if successful. ZIP/RAR/7z archives should only contain .nzb files inside (.nfo are silently ignored). The Watched Folder supports [Categories](/wiki/configuration/4.5/categories) in two ways:

* **Categories:** Create a folder inside your watched folder with the same name as one of your categories. Placing a file inside that folder will add the category with the same name as the sub-folder when it is imported.
Example: If you have a category called `Random`, place a file inside `C:\WatchedFolder\Random` and it will be picked up and assigned to the `Random` category (if it exists).
* **Filename Prefix:** If an NZB file has a prefix, for example `{{movies}}My favorite movie.nzb`, it will be handled as the file `My favorite movie.nzb`, having category `movies`.

**Watched Folder Scan Speed**
Advanced |  Number of seconds between filesystem scans of the Watched Folder setting above. Setting it to `0` disables the automatic scans, but scans can still be triggered from the menu on the main page.

**Scripts Folder** | This specifies the folder where user scripts (post-processing and pre-queue) are stored. On Windows, users may specify a .cmd or .bat file; other extensions can be executed with the `PATHEXT` variable. On Unix any installed script type can be used, including common choices such as shell or Python, provided the file is executable (`chmod +x file`) and starts with a valid [shebang line](https://en.wikipedia.org/wiki/Shebang_\(Unix\)).
Read more about creating [Post-processing](/wiki/configuration/4.5/scripts/post-processing-scripts) and [Pre-queue](/wiki/configuration/4.5/scripts/pre-queue-scripts) scripts.
**Email Templates Folder**
Advanced | You can define your own [Email Templates](/wiki/extra/email-templates).
**Password File**
Advanced | A text file of known passwords, one password per line, that should be attempted on passworded RAR files. See also [Password-protected RARs](/wiki/advanced/password-protected-rars).
WARNING Checking passwords takes time, do not list more than ~20 passwords in this file!

## System Folders

OS-specific default locations for the settings below can be found [here](/wiki/advanced/directory-setup).

| Setting | Description |
|---------|-------------|
| **Administrative Folder** | Location for queue, admin and history database |
**Backup Folder**
Advanced |  Location where the backups of the configuration file and databases are stored.
If left empty, the backup will be created in the Completed Download Folder.
See also [Create Backup](/wiki/configuration/4.5/general#toc3).
**Log Folder**
Advanced | This folder holds error/warning/info/debug logging data.
**.nzb Backup Folder**
Advanced | When SABnzbd adds an nzb to the queue it creates a local of the NZB file in this folder. If you leave this box empty, no files will be saved.

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
