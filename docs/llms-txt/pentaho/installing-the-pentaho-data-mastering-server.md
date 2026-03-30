# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/installing-the-pentaho-data-mastering-server.md

# Installing the Pentaho Data Mastering server

Install the Pentaho Data Mastering server so that you can use the Pentaho Data Mastering
\
application to maintain your organization's most important data.

{% hint style="info" %}
**Important**: Components for Pentaho Data Mastering must be installed in the following order:

1. OpenObserver APM tool components
2. Keycloak IAM server components
3. Pentaho Data Mastering server components If you have intalled a component out of order, uninstall that component and then install the components in order.
   {% endhint %}

Complete the following steps to install the Pentaho Data Mastering server:

1. Open a file transfer tool, like the PuTTY client, and log into the server.
2. Run the following command to view the choices for installing, uninstalling, starting, and stopping components on the Pentaho Data Mastering server:

   `cd /opt/mdm/`
   \
   `./mdm.sh`\
   &#x20;\
   For example, the following image shows the choices that are shown when you run the
   \
   `mdm.sh` command:<br>

   <figure><img src="https://728502995-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fice38OqJsmUCytyCg7bk%2Fuploads%2FGBFzEzlB2Z9nWmRj9KY1%2Fimage.png?alt=media&#x26;token=31939011-56f2-4e36-9bdc-758513a59305" alt=""><figcaption></figcaption></figure>
3. Enter the number for the `Installing all the MDM components` choice.
4. Confirm that you want to proceed with the choice by typing `Yes` and pressing **Enter**.
5. Run the following command to verify that the Pentaho Data Mastering components are up and running in the Docker container: \
   `$ sudo docker ps` \
   For example, the following image shows the running status of the Pentaho Data Mastering components:<br>

   <figure><img src="https://728502995-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fice38OqJsmUCytyCg7bk%2Fuploads%2FfO1PpCSHOjZDscy6VwKh%2Fimage.png?alt=media&#x26;token=3d4158c1-bbd2-4bb7-af0e-0d3332ea69e8" alt=""><figcaption></figcaption></figure>

**Next steps**

After you have installed the Pentaho Data Mastering server, see [validating-installation-of-pentaho-data-mastering](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/validating-installation-of-pentaho-data-mastering "mention").
