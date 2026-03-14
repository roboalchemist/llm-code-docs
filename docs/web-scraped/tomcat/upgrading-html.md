# Source: https://tomcat.apache.org/upgrading.html

Title: Apache Tomcat® - Upgrading Apache Tomcat

URL Source: https://tomcat.apache.org/upgrading.html

Markdown Content:
### Overview

Upgrading Apache Tomcat® can be straightforward or complicated, depending upon the complexity of your environment. This document explains some of the basics of upgrading Apache Tomcat and can be used as a starting point for you to establish your own environment-specific upgrade plans and procedures.

### Table of Contents

*   [Not Covered](https://tomcat.apache.org/upgrading.html#Not_Covered)
    1.   [Patches](https://tomcat.apache.org/upgrading.html#Patches)
    2.   [Embdded Tomcat](https://tomcat.apache.org/upgrading.html#Embdded_Tomcat)

*   [Upgrade Types](https://tomcat.apache.org/upgrading.html#Upgrade_Types)
*   [Versioning](https://tomcat.apache.org/upgrading.html#Versioning)
*   [Major Upgrades](https://tomcat.apache.org/upgrading.html#Major_Upgrades)
    1.   [Read the Migration Guide](https://tomcat.apache.org/upgrading.html#Major_Upgrades/Read_the_Migration_Guide)
    2.   [Migrating your server.xml file](https://tomcat.apache.org/upgrading.html#Migrating_your_server.xml_file)
    3.   [Other Important Files](https://tomcat.apache.org/upgrading.html#Other_Important_Files)

*   [Minor Upgrades](https://tomcat.apache.org/upgrading.html#Minor_Upgrades)
    1.   [Read the Migration Guide](https://tomcat.apache.org/upgrading.html#Minor_Upgrades/Read_the_Migration_Guide)

*   [Split Configurations](https://tomcat.apache.org/upgrading.html#Split_Configurations)

### Not Covered

There are some topics _not_ covered by this basic upgrade guide.

#### Patches

The Apache Tomcat project does not provide patches. If a feature, bug-fix, or security patch is announced in a specific version of Tomcat, then you must upgrade to that version. You may be able to get patches from your OS vendor or other technical-support organization, but the Apache Tomcat project will not supply such patches.

#### Embdded Tomcat

Upgrading Apache Tomcat being used in an embdded environment is not covered in this documentation. It is assumed that if you are using Apache Tomcat in an embdded environment, then you have the knowledge necessary to perform an upgrade without introductory documentation as is provided, here.

### Upgrade Types

Upgrades can be separated into two different kinds of upgrades: upgrades between major versions (e.g. from 9.0 to 10.0) – known as a "major upgrade", and upgrades within a single version (e.g. 9.0.45 to 9.0.85) – known as a "minor upgrade". The steps to follow are different for each type of upgrade.

### Versioning

Apache Tomcat version numbers are of the form X.Y.Z where X.Y is the "major" version number, and the Z is the revision-number within the major version. Upgrading between Tomcat 10.1 and 11.0 is considered a "major upgrade" while upgrading from 10.1.20 to 10.1.21 is considered a "minor upgrade".

### Major Upgrades

When upgrading between major versions of Tomcat (e.g. 9.0 to 10.1), it is best to start with a stock installation of Tomcat, then and adapt the new configuration files to meet your needs, add your applications, etc.

#### Read the Migration Guide

You should read the migration guide(s) that are relevant to your particular upgrade page. If you are upgrading from Apache Tomcat 9.0 to Apache Tomcat 10.1, you should read the "Tomcat 10.1 Migration Guide" which covers everything that applies for upgrading from the previous version.

If you are upgrading past several versions at once, you should read all the migration guides in between. For example, if you are upgrading from Tomcat 8.5 to Tomcat 10.1, you should read the "Tomcat 9.0 Migration Guide", the "Tomcat 10.0 Migration Guide", and the "Tomcat 10.1 Migration Guide".

#### Migrating your server.xml file

Probably the most important configuration file you will have to migrate is your `conf/server.xml` file.

One way to quickly determine what kinds of changes might be necessary for your `server.xml` file is to use the `diff` program to compare your existing old-Tomcat-version file with the stock configuation file that came with your old version of Apache Tomcat.

For example:

`$ diff /path/to/stock/tomcat/conf/server.xml /path/to/your/tomcat/conf/server.xml`

This will display the changes made to the original file that are unique to your environment. You can adapt these changes to the new installation of your new Apache Tomcat version.

#### Other Important Files

There are some other configuration files you may want to copy or adapt from your previous installation. Here is a list of those other files you may have customized in your old installation.

*   conf/web.xml
*   conf/context.xml
*   conf/tomcat-users.xml
*   conf/logging.properties
*   bin/setenv.sh (if it exists)
*   conf/catalina.properties
*   conf/catalina.policy
*   conf/jaspic-providers.xml

If you are unsure, you can use the same technique shown above to check for any differences between your installation and a stock Apache Tomcat configuration file.

### Minor Upgrades

Often, minor upgrades are very simple and you can use the same configuration files as the previous version with no changes.

#### Read the Migration Guide

It is still important to read the [Migration Guide](https://tomcat.apache.org/migration.html) for the major version you are using, specifically the "upgrading" section.

The Migration Guide also contains an "Noteable Changes" section which includes changes within the major version – that is, a minor version within a major version's revision numbers – which contains a very important change. These kinds of changes include the the introduction of new defaults, new requirements (usually for security), or breaking changes from previous versions (also usually for security).

Finally, the Migration Guide has a section that allows you to compare the stock configuration files between minor versions to see if any important changes have been made between those versions. It's easy to use: simply choose your old-version and new-version from the drop-down boxes on the Migration Guide page and then "View Differences".

### Split Configurations

In `RUNNING.txt`, there is a section titled _Advanced Configuration - Multiple Tomcat Instances_. It is intended to describe how a single Apache Tomcat installation can be used to run multiple separate server instances. This technique can be used to help simplify upgrades.

There is a presentation available which will walk you through the process of splitting your installation, and then describes how to perform an upgrade.

[_Split your Tomcat Installation for Easier Upgrades_](https://tomcat.apache.org/presentations.html#latest-split-installation)
