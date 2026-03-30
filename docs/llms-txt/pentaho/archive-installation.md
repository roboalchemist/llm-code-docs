# Source: https://docs.pentaho.com/install/pentaho-installation-overview-cp/archive-installation.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation.md

# Archive installation

If you are installing Pentaho in a production environment, use this method to install the Pentaho Server on a server machine while installing design tools on separate client workstations. It requires that you download and install Pentaho installation files.

You must also choose the Pentaho Repository database that you want to use, but you must download and install it yourself.

By default, the Archive Installation of the Pentaho Suite installs:

* BA plugins (such as Analyzer and Interactive Reports).
* DI plugins (such as Big Data and Marketplace).

The archive installation method provides you with a preconfigured Tomcat web application server. This method is most useful when you do not already have a web app server. As such, the archive installation method is an easier and quicker installation process versus a [manual installation](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation). This method is an archive by virtue of its being an image or "snapshot" of a Pentaho configuration built on Tomcat.

An archive installation is also useful if you already have existing Pentaho data or repositories that you created with a previous version of Pentaho or that you created with an evaluation installation of Pentaho. The archive installation method is an easy way to bring your existing Pentaho data into your production version.

Review these prerequisites before you start the archive installation.

This guide assumes that you have:

* Read the overview of installation options in the [Pentaho installation](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp) article to ensure that this method is the best installation option for you.
* Checked the [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference) to ensure that your server computer, Pentaho Repository database, and web browser meet Pentaho's requirements for this version of the software.
* Uninstalled any evaluation version of Pentaho. See the **Try Pentaho Data Integration and Analytics** document for instructions.
* Disabled your antivirus software during installation. Reasons for this are:
  * On Windows, Pentaho writes registry entries and files to the `Program Files` directory.
  * Pentaho accesses ports that some antivirus programs block.
  * Installation takes longer and the Pentaho User Console may have performance issues.

## Audience

IT administrators who know where the data is stored, how to connect to it, details about the computing environment, and how to use the command line to issue commands for Microsoft Windows or Linux.

## Tools

You must supply a web application server that meets the hardware and software requirements indicated in the [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference), as well as a supported operating system and JRE or JDK. Additionally, you will need a text editor and a ZIP tool to complete some of the steps in this installation process.

The Pentaho Repository contains solution content, scheduling, and audit tables needed for the Pentaho Server to operate. You can house the Pentaho Repository on PostgreSQL, MySQL, MariaDB, MS SQL Server, or Oracle. With this installation option, you must supply, install, and configure your chosen database yourself.

## Login Credentials

You must be logged on to an account that has administrative privileges to perform the tasks in these sections. Additionally, Linux users need to use the `root` account for some tasks.

## Requirements for Archive Installation

An archive installation requires these items and expertise:

| Requirements                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You Supply                    | <p>Each of the following items must meet or exceed the requirements in the <a href="../components-reference">Components Reference</a>:- Computer with a supported operating system and hardware configuration.</p><ul><li>Oracle Java Runtime Environment (JRE) or Oracle Java Development Kit (JDK).</li><li>Pentaho Repository database (PostgreSQL, MySQL, MariaDB. MS SQL Server. or Oracle). You can also use a preexisting Pentaho repository platform.</li><li>Pentaho Repository database JDBC Drivers (PostgreSQL, MySQL, MariaDB, MS SQL Server or Oracle).</li></ul> |
| We Supply                     | <ul><li>Installation package.</li><li>The web application server (Tomcat).</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Technologies Used             | <ul><li>Tomcat web application server (provided by Pentaho).</li><li>A PostgreSQL, MySQL, MariaDB, MS SQL Server, or Oracle database.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Expertise                     | <ul><li>Knowledge of your networking environment, including database port numbers if they differ from the default and IP address.</li><li>Permission to access installation directories.</li><li>Root or administrative access.</li></ul>                                                                                                                                                                                                                                                                                                                                       |
| Approximate Installation Time | <ul><li>60 to 90 minutes.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

You can download the Pentaho software from the \[<https://support.pentaho.com/home]\\(https://support.pentaho.com/home)>.
