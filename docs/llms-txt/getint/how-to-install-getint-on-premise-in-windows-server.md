# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/on-premise-deployment/installing-getint-onpremise/how-to-install-getint-on-premise-in-windows-server.md

# How to Install Getint On-Premise in Windows Server

This guide provides a step-by-step process for setting up PostgreSQL, Java, and Getint on Windows Server. It covers the installation and configuration of PostgreSQL, downloading and preparing the trial version of our app, and running the application. With these instructions, you can smoothly set up and integrate Getint into your workflow.

{% hint style="warning" %}
This guide is only intended for Getint version v1.70 and above. Please ensure your Getint version is updated to this version before proceeding.
{% endhint %}

### Installing Getint in Windows Server <a href="#installing-getint-in-windows-server" id="installing-getint-in-windows-server"></a>

#### 1. Install PostgreSQL

* Follow all the steps located on the **PostgreSQL** website [here.](https://www.postgresql.org/docs/current/installation.html) All the software packages situated on this website are essential to PostgreSQL's correct function, which would equal the proper installation of Getint.

#### 2. Install JAVA JDK

* Download and install from Oracle's official site: [Java JDK.](https://www.oracle.com/java/technologies/downloads/?er=221886)

{% hint style="info" %}
At Getint, we support Java versions 8 through 17.
{% endhint %}

#### 3. Download and Unzip Getint

* Download the **Getint .zip package** from the provided source.
* Unzip the **downloaded file** to a location of your choice on the Windows Server. For example, you can unzip it to C:\Users\Administrator\Downloads\getint-1.68.
* The [Getint](http://getint.io) team will provide the URL to download the trial version. Please visit our [support portal](https://getint.io/help-center) and open a ticket if you need to download the latest version of Getint for your Windows Server.

#### 4. Open Command Prompt and Navigate to the Synchronizer Folder

* Open a terminal (Command Prompt) on the Windows Server.
* Navigate to the unzipped folder by using the cd command. For example:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJkg8YCckPMaCfcgNR5gy%2Fcmd%20synchronizer%20file.png?alt=media&#x26;token=07ce24e4-da39-4d4d-9559-7aae4dd118ab" alt=""><figcaption></figcaption></figure>

#### 5. Start Getint

* **Execute** the `call manager.bat start` command to start Getint:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBMpsuIpHU1cC4cpSboNv%2Fmanager.bat%20start%20command%20to%20initiate%20Getint.png?alt=media&#x26;token=6c44021b-6e7d-43c8-98c8-39d4c060c1b3" alt=""><figcaption></figcaption></figure>

* Getint will start on **port 80** by default.

* **To change the port**, open the manager.bat file and modify the port number by changing the line set PORT=80 to, for example, set PORT=8080. Then, **restart Getint** if it's already running.

* **To change the database** (you may use our database during the trial period), you can modify the datasource variables also defined in the manager.bat:

  ```

  set SPRING_DATASOURCE_USER=sa
  set SPRING_DATASOURCE_PASSWORD=
  set SPRING_DATASOURCE_DRIVER=org.h2.Driver
  set SPRING_DATASOURCE_URL=jdbc:h2:~/getintio-db;DB_CLOSE_DELAY=-1;INIT=CREATE SCHEMA IF NOT EXISTS public
  ```

* For example, to connect to the Postgres database, you can provide the following values:

  ```
  set SPRING_DATASOURCE_USER=postgres
  set SPRING_DATASOURCE_PASSWORD=postgres
  set SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/getint
  set SPRING_DATASOURCE_DRIVER=org.postgresql.Driver
  ```

{% hint style="info" %}
Running the .bat file in this manner will execute its commands in the foreground. This means the process will continue to run as long as the console remains open. Closing the console will stop the process, causing the [Getint.io](http://getint.io) .jar file to stop running. You must set the .bat file as a Windows Service to ensure it runs permanently.
{% endhint %}

#### 6. Open Your Browser and Access Getint

* **Open a web browser** on the same machine where Getint is running. Open your browser and type the URL, which is your machine's IP address. Alternatively, if you have a domain name assigned to the machine on which **Getint** is installed, you can type that domain name. If you have used a port other than 80, remember to include it in the address (i.e., the URL would be `http://10.0.0.32:8089`).
* **Type the machine's URL:**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FcrTkiNhR9UATL0Uz4Nvl%2FURL%20for%20Getint%20Initialization.png?alt=media&#x26;token=8220bf07-8c58-40fb-b6c6-c772c74402bc" alt=""><figcaption></figcaption></figure>

* Replace PORT with the port number configured in the `getint.env` file (default is 80).
* **The Getint UI should load.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FskvtAidJbWEcO1zbFSbf%2FGetint%20UI.png?alt=media&#x26;token=22b5d621-b57a-4f0b-82e3-2c3ffafbb0ac" alt=""><figcaption></figcaption></figure>

#### 7. Log In

* Use the following default credentials to sign in:
  * Username: admin
  * Password: admin

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvFH4ZVAPdAMNoSCliAvc%2Fcredentials%20for%20getint%20usage.png?alt=media&#x26;token=c20e468f-d941-4491-b13c-0e2024e20e92" alt=""><figcaption></figcaption></figure>

#### 8. Running Getint in the Background Using the Task Scheduler

To allow Getint to launch on startup, you can create a **Basic task** and add it to the **Task Scheduler** as shown below.

* Open the Task Scheduler, and click **Create Basic Task.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F22wUgNUHMUnfbQsT2znP%2FOpening%20the%20Task%20Scheduler.png?alt=media&#x26;token=f3c402e2-dbd6-4192-9444-d8dcb6f7d527" alt=""><figcaption></figcaption></figure>

* Name your task to identify it easily if you need to make changes later.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnXL6XzChw9X1P9y0R5AR%2FName%20your%20task.png?alt=media&#x26;token=e75a7927-4523-45ea-bd92-f612d57620db" alt=""><figcaption></figcaption></figure>

* Select the trigger for your task, also known as when you want the task to start. Select **when the computer starts,** so the run.bat file launches during each startup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJR6NMjJXsWCpmjYcTep0%2FSelect%20the%20trigger.png?alt=media&#x26;token=42e97f07-5a7a-44df-89d5-c396db43f2db" alt=""><figcaption></figcaption></figure>

* Select **start a program.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIIaFk06dhSN9LwzI0nYc%2FStarting%20a%20Program.png?alt=media&#x26;token=9e2891ee-cde7-48e4-922b-64a0b9a74dec" alt=""><figcaption></figcaption></figure>

* Use the Getint path to configure the task.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2NAe86c6vAflpn2Ymcox%2FUse%20Getint%20path%20to%20set%20the%20task.png?alt=media&#x26;token=85d90014-3f72-491a-bcbf-ae1cf76cce72" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you need any further help or if you are experiencing issues with your installation, feel free to open a support ticket at our [Support Portal.](https://getint.io/help-center)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
