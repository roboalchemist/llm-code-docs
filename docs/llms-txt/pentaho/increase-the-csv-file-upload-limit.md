# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/increase-the-csv-file-upload-limit.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/increase-the-csv-file-upload-limit.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/increase-the-csv-file-upload-limit.md

# Increase the CSV file upload limit

You may find that you need to increase the size of the upload limit for your CSV files. These steps guide you through this process.

1. Go to `/pentaho-server/pentaho-solutions/system` and open the `pentaho.xml` file.
2. Edit the XML as needed (sizes are measured in bytes):

   ```xml
   <file-upload-defaults>
         <relative-path>/system/metadata/csvfiles/</relative-path>

         <!-- max-file-limit is the maximum file size, in bytes, to allow to be uploaded to the server -->
         <max-file-limit>10000000</max-file-limit>

         <!-- max-folder-limit is the maximum combined size of all files in the upload folder, in bytes. -->
         <max-folder-limit>500000000</max-folder-limit>

   </file-upload-defaults>
   ```
3. Save your changes to the file.
4. In the User Console, go to **Tools** > **Refresh System Settings** to ensure that the change is implemented.
5. Restart the User Console.
