# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/jackrabbit-repository-perfomance-tuning/jackrabbit-runs-slowly-with-too-many-home-directories-performance-tuning.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/jackrabbit-repository-perfomance-tuning/jackrabbit-runs-slowly-with-too-many-home-directories-performance-tuning.md

# Jackrabbit runs slowly with too many home directories

Before Pentaho 6.1, the Jackrabbit repository ran slowly when there are too many home directories. Jackrabbit scanned each and every home directory on the first login after a server restart, calling **UserDetailService** for each home directory owner.

A flag has been added to skip user verification on principal creation by default. It retrieves user details from the user cache only, which speeds up repository loading.

You may need to restore the old behavior if your authorization system is expecting the Pentaho Server to load all of the user information on startup. Restore the old behavior by changing the **skipUserVerificationOnPrincipalCreation** to `false`. This allows user verification to operate in the same way it did before 6.1.

1. Navigate to the `pentaho-solutions/system/jackrabbit` directory.
2. Open the `security.properties` file with any text editor.
3. Locate the **skipUserVerificationOnPrincipalCreation** property and set the value as needed.
4. Save and close the file.

If you discover that you need to re-enable the old mode of verification, then it is likely an issue exists with your authentication system. We recommend contacting [Pentaho Support](https://support.pentaho.com/hc/en-us) if you need help.
