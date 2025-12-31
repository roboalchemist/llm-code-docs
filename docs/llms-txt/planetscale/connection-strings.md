# Source: https://planetscale.com/docs/vitess/security/connection-strings.md

# Source: https://planetscale.com/docs/vitess/connecting/connection-strings.md

# Connection strings

## Creating a password

<Steps>
  <Step>
    To create a password, head to your database dashboard page at `https://app.planetscale.com/<ORGANIZATION>/<DATABASE_NAME>` and click on the "**Connect**" button.
  </Step>

  <Step>
    On the **Connect page**, select the branch you wanted to create a password for, pick a [password role](/docs/vitess/security/password-roles), and provide a recognizable name for the new credentials. Clicking `Create password` will then generate a **unique username and password pair** that can only be used to access the designated branch of your database. Take note of this password, as you won't be able to see it again.
  </Step>

  <Step>
    Once created, you can browse the connection string in different framework formats by selecting framework in the "Select your language or framework" section. This will also show you all of the files you need to modify to get connected with PlanetScale in your framework or language of choice.
  </Step>
</Steps>

<Note>
  There are two connection types for a password: `Primary` and `Replica`. The `Primary` connection type is used to connect to the primary region of your database, while the `Replica` connection type is used to route queries to your branch's replicas and read-only regions. You can create multiple passwords for a branch, each with a different connection type. [Read more about replicas](/docs/vitess/scaling/replicas).
</Note>

<Tip>
  Make sure you copy the credentials for your application and the "Other" format. We do not save the password in plaintext, so there will be no way to retrieve the password after you leave this page.
</Tip>

## Managing passwords

Once you've created the password, you can head over to the "**Passwords**" settings page available at `Organization > Database > Settings > Passwords` to manage them.

<Tip>
  You can also create passwords for branches other than `main` on this page.
</Tip>

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/connection-strings/manage-2.png?fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=07f620508e2a9ebd153dc80a3dcf7629" alt="Manage passwords page" data-og-width="1761" width="1761" data-og-height="604" height="604" data-path="docs/images/assets/docs/concepts/connection-strings/manage-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/connection-strings/manage-2.png?w=280&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=33d63bc6fe96ee960fac37e93b7e0853 280w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/connection-strings/manage-2.png?w=560&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=24cf5aaab28af798045f57cfbf2c7cbb 560w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/connection-strings/manage-2.png?w=840&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=6ff1f113234e375d4fc75f00839bcd04 840w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/connection-strings/manage-2.png?w=1100&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=e0279fb5a9bf953bf266f70e336d59c3 1100w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/connection-strings/manage-2.png?w=1650&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=c2cc871b1f3425d99314ecffe6d83b5a 1650w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/connection-strings/manage-2.png?w=2500&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=8216abe43a4fe2abffa93a3909f1a0d9 2500w" />
</Frame>

Clicking on the `...` icon on the row for your password allows you rename or delete the password.

## Renaming a password

Since the **username & password** pair is unique, the only metadata you can edit is the `display name` of the password.

## Deleting a password

Deleting a password will invalidate the username & password pair and **disconnect any active clients using this password**.

<Note>
  Any open database connections authenticated with a deleted password will be disconnected within five minutes.
</Note>

## Native MySQL authentication support

Use the tools you're familiar with to connect to PlanetScale databases.
PlanetScale supports both [MySQL native authentication](https://dev.mysql.com/doc/refman/8.0/en/native-pluggable-authentication.html), which is widely used to provide a secure connection to MySQL servers,
and [MySQL Caching SHA-2 authentication](https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html), which is the most secure authentication mechanism to connect to MySQL.
Based on your application needs and platform support, you can switch between the authentication modes, with the same password.

For a list of tested MySQL GUI clients, review our article on [how to connect MySQL GUI applications](/docs/vitess/tutorials/connect-mysql-gui).

## Strong security model

PlanetScale Passwords are created for use with a single database branch.
This strong security model allows you to generate passwords that are tied to a branch, and cannot access data/schema from another branch.

## IP restrictions

You can restrict database connections to specific IP ranges for a single password by updating its IP restrictions. For example, if you have a database for a web application and you create a password for use in the deployed application, you can restrict usage of that specific password to the IP ranges of the deployed application. If somebody attempts to connect to the database from outside of the deployed application, the connection will be refused. IP restrictions work on a per-password basis, so if you want to use the same restriction across passwords, they must be applied to each password separately.

Some passwords are incompatible with IP restrictions, and you will need to create a new password to use IP restrictions.

Examples of when you may want to use IP restrictions:

* You want to segment database access so that the production database can only be connected to from production environments or development branches.
* You use a bastion in production and want to ensure that all database connections originate or pass through the bastion.
* You want to allow a single client to be able to access your database (e.g., for debugging) and want to provide the least amount of access for them to do so.
* You have compliance requirements that require implementing a more stringent access control list in your database.

### Updating the IP restrictions for a password

1. Go to your database's "**Settings**" tab.
2. Click "**Passwords**."
3. You can update the IP restrictions for a password in two different ways: The first way is by opening the dropdown menu to the right of any password on the Passwords page and clicking "**Manage IP restrictions**." The second way is by clicking on the password and scrolling to the bottom of its page to update IP restrictions.
4. Add the IP ranges that you want to allow to connect using the selected password.

<Note>
  If your password has no IP restrictions, it is set to **allow all traffic**. Similarly, when you add a new IP range to the restrictions, all IP addresses out of this range cannot connect to your database using that password.
</Note>

## Disconnect clients by deleting passwords

PlanetScale automatically disconnects clients that are using a deleted password.
Head on over to the `Organization > Database > Settings > Passwords` page on your database branch to delete passwords for that branch.
It may take up to five minutes for all active clients to be disconnected.

## No plain text password storage

PlanetScale only stores hashes and metadata about your database passwords.
To add an extra layer of security to your database, we do not store any passwords in plaintext.

<Note>
  In the event that you lose a password, we cannot recover it for you. We recommend creating a new password with the
  same access level.
</Note>

## GitHub Secret Scanning integration

All passwords and service tokens generated for use with PlanetScale databases are part of [GitHub's Secret Scanning](https://docs.github.com/en/code-security/secret-security/about-secret-scanning) program. If any database passwords or service tokens are committed in plaintext to any public GitHub repository, we will be notified and take corrective action to delete the access tokens and cut off their access.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt