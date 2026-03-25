# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp.md

# Setting up password encryption after upgrading

As an IT administrator, you may need to enhance your company's security by encrypting the passwords that are currently stored as plain text in configuration files. For example, you need to meet specific server security levels for regulatory compliance. Before applying password encryption on your upgraded Pentaho, you must set up your upgrade to work with password encryption.

After upgrading your Pentaho Server to the latest version, you can set up password encryption. To get started, you must first set up the server to work with password encryption before applying it.

Perform the following actions if you want to set up your system for password encryption:

1. Modify the Tomcat Context XML file.
2. Update the Jackrabbit Repository XML file.
3. Verify your Quartz properties.
4. Update your Hibernate configuration.
