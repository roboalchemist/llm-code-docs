# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/manual-cleanup-of-the-temporary-folder.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/manual-cleanup-of-the-temporary-folder.md

# Manual cleanup of the Temporary folder

Every time you generate content on the Pentaho Server, temporary files are created on the local file system in the `/pentaho-solutions/system/tmp/` folder. In some cases, the Pentaho Server may not properly purge that temporary content, leaving behind orphaned artifacts that can slowly build up and reduce performance on the volume that contains the `pentaho-solutions` folder. One way to address this issue is to mount the `/tmp` folder on a separate volume, thereby siphoning off all disk trash asssociated with creating new content. However, you will still have to perform a manual garbage collection procedure on this folder on a regular basis. You can accomplish this via a script that runs through your system scheduler; it should be safe to delete any content files in this directory that are more than a week old.
