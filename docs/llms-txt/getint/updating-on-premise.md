# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/on-premise-deployment/updating-on-premise.md

# Updating On-Premise

### How to update Getint On-Premise deployed on Linux <a href="#how-to-update-getint-on-premise-deployed-on-linux" id="how-to-update-getint-on-premise-deployed-on-linux"></a>

1. **Open your terminal and sign in to the machine as a root user.**
   * Use the SSH command and replace `youripaddress` with the hostname or IP address of the server:

| ssh root\@youripaddress |
| ----------------------- |

1. **Enter your password:**
   * You’ll be prompted to enter your password for the specified username
2. **Open your Getint folder**
   * Enter`cd getint` to switch to the Getint directory
   * Now enter `cd synchronizer` to open the Getint installation folder
3. **Download Getint files:**
   * Getint will provide these. Use the command `wget` + the link to the files to download the installation package. For example, `wget <URL_FROM_GETINT_TEAM>`
   * Use the command `ls -al` to see the files in the current directory, and ensure the zip files are located there
4. **Updating Getint**
   * Run the command `./upgrade.sh` + the zip file. For example, the full command should be `./upgrade.sh getint-1.62.zip`
   * Wait for the files to install and use **ctrl + c** to close the logs and return to the directory
   * Alternatively, if you didn’t download the installation package, you can use this command to upgrade your version directly without downloading Getint files separately `./upgrade.sh` + the link to the files.
5. **Access Getint and ensure the version was updated**
   * These are the credentials you can use to log into Getint via your browser in case you didn’t change them when installing Getint for the first time:
     * Username: admin
     * Password: admin
   * Open the browser and type the URL which is the machine’s IP address. Alternatively, if you have any domain name assigned to the machine on which Getint is installed, you can type that domain name
   * Within Getint, look for the **“?”** icon in the bottom left corner of your screen, and click on it. This will show your current software version. Please verify that your version was upgraded successfully

{% hint style="info" %}
Please test your integration to confirm that it is working without errors. Additionally, if you previously experienced any issues with Getint, check whether they have been resolved after the update. If not, please reach out to our support team at <support@getint.io>, and we’ll assist you accordingly.
{% endhint %}

#### Video tutorial <a href="#video-tutorial" id="video-tutorial"></a>

{% embed url="<https://www.loom.com/share/7805f1a26c924f8ea5d4df7e8df6021d?sid=65ea022c-6b61-4b74-bfb3-4d72d7496300>" %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
