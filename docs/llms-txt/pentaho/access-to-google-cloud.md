# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-google-cloud.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-google-cloud.md

# Access to Google Cloud

To access Google cloud from PDI, you must have a Google account and service account credentials in the form of a JSON format key file. Additionally, you must set permissions for your Google Cloud accounts. To create service account credentials, see <https://cloud.google.com/storage/docs/authentication>.

Perform the following steps to set up your system to use Google Cloud storage:

1. Download the service account credentials file that you have created using the Google API Console to your local machine.
2. Create a new system environmental variable on your operating system named **GOOGLE\_APPLICATION\_CREDENTIALS**.
3. Set the path to the downloaded JSON service account credentials file as the value of the **GOOGLE\_APPLICATION\_CREDENTIALS** variable.

You are now ready to access files from the Google Cloud Storage file system in PDI.
