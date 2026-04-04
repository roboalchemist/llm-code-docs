# Source: https://docs.curator.interworks.com/users_groups/user_security/password_reset.md

# Source: https://docs.curator.interworks.com/site_administration/backend_administrators/password_reset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Password Reset 

> Reset backend administrator passwords through self-service or administrative override when access is lost.

Forget your backend administrator password?

A Curator backend administrator user's password can easily be reset by other users who have Backend User access.

## No one left to reset your password?

If there is no one else with administrative access to the system, the account can also be reset using the steps below.

1. Connect to the server running Curator. (Windows: RDP, or with Linux: SSH)

2. Open a command prompt \[Windows Only, Linux will start in a command prompt.]

3. Change to the webroot directory where Curator is installed.
   Here are some examples:

   * **Windows (Apache: Standard):**

     ```Apache  theme={null}
     cd C:\InterWorks\Curator\htdocs;
     ```

   * **Windows (IIS: Legacy):**

     ```Windows  theme={null}
     cd C:\InterWorks\Curator\wwwdata;
     ```

   * **Linux:**

     ```Linux  theme={null}
     cd /var/www/html;
     ```

4. Run "artisan" to reset the administrative user:

   ```PHP  theme={null}
   php artisan winter:passwd
   ```
