# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/before-you-begin-archive-installation.md

# Before you begin

Review these prerequisites before you start the archive installation.

This guide assumes that you have:

* Read the overview of installation options in the [Pentaho installation](https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp) article to ensure that this method is the best installation option for you.
* Checked the [Components Reference](https://docs.pentaho.com/install/9.3-install/components-reference) to ensure that your server computer, Pentaho Repository database, and web browser meet Pentaho's requirements for this version of the software.
* Uninstalled any evaluation version of Pentaho. See the **Try Pentaho Data Integration and Analytics** document for instructions.

## Audience

IT administrators who know where the data is stored, how to connect to it, details about the computing environment, and how to use the command line to issue commands for Microsoft Windows or Linux.

## Tools

You must supply a web application server that meets the hardware and software requirements indicated in the [Components Reference](https://docs.pentaho.com/install/9.3-install/components-reference), as well as a supported operating system and JRE or JDK. Additionally, you will need a text editor and a ZIP tool to complete some of the steps in this installation process.

The Pentaho Repository contains solution content, scheduling, and audit tables needed for the Pentaho Server to operate. You can house the Pentaho Repository on PostgreSQL, MySQL, MS SQL Server, or Oracle. With this installation option, you must supply, install, and configure your chosen database yourself.

## Login Credentials

You must be logged on to an account that has administrative privileges to perform the tasks in these sections. Additionally, Linux users need to use the `root` account for some tasks.

## Requirements for Archive Installation

An archive installation requires these items and expertise:

| Requirements                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| You Supply                    | <p>Each of the following items must meet or exceed the requirements in the <a href="../../../components-reference">Components Reference</a>:- Computer with a supported operating system and hardware configuration.</p><ul><li>Oracle Java Runtime Environment (JRE) or Oracle Java Development Kit (JDK).</li><li>Pentaho Repository database (PostgreSQL, MySQL, MS SQL Server or Oracle). You can also use a preexisting Pentaho repository platform.</li><li>Pentaho Repository database JDBC Drivers (PostgreSQL, MySQL, MS SQL Server or Oracle).</li></ul> |
| We Supply                     | <ul><li>Installation package.</li><li>The web application server (Tomcat).</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Technologies Used             | <ul><li>Tomcat web application server (provided by Pentaho).</li><li>A PostgreSQL, MySQL, MS SQL Server, or Oracle database.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Expertise                     | <ul><li>Knowledge of your networking environment, including database port numbers if they differ from the default and IP address.</li><li>Permission to access installation directories.</li><li>Root or administrative access.</li></ul>                                                                                                                                                                                                                                                                                                                          |
| Approximate Installation Time | <ul><li>60 to 90 minutes.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

You can download the Pentaho software from the \[<https://support.pentaho.com/home]\\(https://support.pentaho.com/home)>.
