# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/administration/manage-users-and-roles-in-puc/set-password-requirements.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/administration/manage-users-and-roles-in-puc/set-password-requirements.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/administration/manage-users-and-roles-in-puc/set-password-requirements.md

# Set password requirements

If the server is configured for local Pentaho security authentication, users can change their own passwords. Additionally, as a Pentaho administrator, you can add options to set minimum password length and pre-defined character requirements. See [Set the Authentication Method](https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/administration/set-the-authentication-method) for instructions on setting local or external security authentication.

Perform the following steps to set password requirements:

1. Navigate to the `server/pentaho-server/pentaho-solutions/system` directory and open the `security.properties` file with any text editor.

   By default, the password length is set to `0` and the special character requirement is set to `false`, as shown in the following example code:

   ```
   PUC_USER_PASSWORD_LENGTH=0
   PUC_USER_PASSWORD_REQUIRE_SPECIAL_CHARACTER=false
   ```
2. Change the default values in the `security.properties` file to your password requirements:
   1. Set `PUC_USER_PASSWORD` to the minimum valid password length.

      The acceptable password length is one plus the minimum length you set. For example, if you set `PUC_USER_PASSWORD=10`, the acceptable password length is 11 or more. You can set the minimum length to be between 1 and 99. If you set the minimum length to zero (`PUC_USER_PASSWORD=0`) this requirement is disabled.
   2. Set `PUC_USER_PASSWORD_REQUIRE_SPECIAL_CHARACTER` to true (`PUC_USER_PASSWORD_REQUIRE_SPECIAL_CHARACTER=true`) to require use of special characters to enforce stronger passwords.

      When this requirement is set to `true`, the system checks for special characters. The password is not accepted if it does not include a #, @, $, %, or ! special character.
3. Save and close the file.
4. Restart the Pentaho Server.

You now have in place password requirements based on the length and special character options you set in the `security.properties` file.
