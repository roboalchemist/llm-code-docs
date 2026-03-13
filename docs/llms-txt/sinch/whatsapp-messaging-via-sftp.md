# Source: https://docs.sinch.com/technical-documentation/api-and-integrations/whatsapp-messaging-via-sftp.md

# WhatsApp Messaging via SFTP

Here is the WhatsApp messaging via FTP process.

#### Connection Details <a href="#connection-details" id="connection-details"></a>

|                    |                                                              |
| ------------------ | ------------------------------------------------------------ |
| **Hostname**       | ftp-messaging.wavy.global                                    |
| **Port**           | 2222                                                         |
| **Protocol**       | SFTP (transfer over ssh, providing client-server encryption) |
| **Authentication** | username + password (supplied by our tech support)           |

<mark style="color:red;">**It is necessary to add your IPs to our firewalls authorized IPs list!**</mark>

If it is necessary to get firewall allowance for the port 2222, you must allow the DNS, or the IPs 200.219.220.54 and 45.236.179.22

**This document is intended as a guide for messages sent through the new WhatsApp messaging via FTP format**

* The file format was based on sending an SMS file via FTP.
* Sending HSMs will be possible in this first version.

**To trigger messages via FTP, you must generate a file with the formatting in the example below:**

**HSM Message:**

```
2018-10-16;10:00;20:00;HSM;chatclub_welcome;EN;DETERMINISTIC;name|company
phone;name;company
551999999999;Name1;Sinch
551999999999;Name2;Sinch
```

| 1st line:                                               |
| ------------------------------------------------------- |
| Send date (for scheduling cases)                        |
| Start send time (for scheduling cases)                  |
| End send time (for scheduling cases)                    |
| Message type must be: **HSM**                           |
| HSM name (elementName)                                  |
| HSM language (languageLocale)                           |
| HSM language Deterministic or Fallback (languagePolicy) |
| name of HSM parameters                                  |

**Notes for the first line:**

1. Parameter names must match the column names
2. Information that will not be used may be left blank, **however** you should keep the semicolon as separation. Example of a case where we did not use scheduling (the first fields are between semicolons and have no information within): ; ; ; HSM;chatclub\_welcome;pt\_BR;DETERMINISTIC;name|company
3. By default, the languagePolicy will be **Deterministic.**
4. The names of HSM parameters should be separated by **" | " and not by " ; "**

| 2nd line:                              |
| -------------------------------------- |
| Column names                           |
| 3rd and remaining lines:               |
| Recipient and values of HSM parameters |

**​**
