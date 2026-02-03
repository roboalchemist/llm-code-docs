# Source: https://herd.laravel.com/docs/macos/herd-pro-services/mail.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mail

# Working with emails

When you are working with emails locally, you need to make sure that these emails don't leave your machine and get sent to real users but it's also important to inspect them easily.

Herd Pro provides an SMTP mail server on your local machine that catches all outgoing emails instead of sending them to the world. It displays them in Herds own email client and provides rich debugging capabilities for all types of emails.

This saves you from sending emails to real users and frees you up from paying cloud services for developer email inboxes, not even requiring you to dig through log files when using the log driver. It's also super fast and organizes all emails per site.

<Frame>
  <img alt="Herd Pro Mail Server with a mail" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a05f97270532e7f58f75ca0c71698d7a" data-og-width="2774" width="2774" data-og-height="1712" height="1712" data-path="images/docs/mails-intro.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5fe04d828d9379ffbfe0c4358d117abd 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d70f76c42f366bec471a215074af8bab 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c812270bd4bb81c7b7991247745adf6f 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=0736a427709e0d1cc00549fc9d9ed9c9 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=64a6c303ddf269634f3a9a9b7e1a9a49 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=99907f4c16654a68080ecf1e3c0d49f1 2500w" />
</Frame>

## Setup

<Note>
  When using `laravel new` or Herd's site creation wizard, Herd configures the mail server in your `.env` file for you automatically.
</Note>

The mail server uses the SMTP protocol to accept mails but instead of sending them to their recipient, it saves them to an internal database.

You can use the settings below and add them to your local `.env` file to receive mails in the Herd Pro mail app.

<Tabs>
  <Tab title="Laravel">
    ```bash .env theme={null}
    MAIL_MAILER=smtp
    MAIL_HOST=127.0.0.1
    MAIL_PORT=2525
    MAIL_USERNAME=${APP_NAME}
    MAIL_PASSWORD=null
    MAIL_ENCRYPTION=null
    MAIL_FROM_ADDRESS="hello@example.com"
    MAIL_FROM_NAME="${APP_NAME}"
    ```
  </Tab>

  <Tab title="WordPress">
    ```php functions.php theme={null}
    function herd_mailer($phpmailer) {
        $phpmailer->isSMTP();
        $phpmailer->Host = '127.0.0.1';
        $phpmailer->SMTPAuth = true;
        $phpmailer->Port = 2525;
        $phpmailer->Username = 'WordPress';
        $phpmailer->Password = '';
    }

    add_action('phpmailer_init', 'herd_mailer');
    ```
  </Tab>

  <Tab title="Other Frameworks">
    Please refer to your framework specific documentation on how to configure outgoing emails and use the provided SMTP server host, port and username to connect to Laravel Herd.
  </Tab>
</Tabs>

The mail client groups incoming mails by the username of the mail sender. This allows you to create a dedicated inbox for each project.
Either specify a unique username manually, or use the `APP_NAME` environment variable to automatically use your application's name as the inbox name. Depending on your application name, you might need to set the username for your mailbox manually before emails show up in Herd.

## Changing the port

By default, the Herd Pro mail server runs on port `2525` but you can customize this configuration in the settings.

<Frame>
  <img alt="Herd Pro Mail Server Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d5d82bd5e094f047fba0a6d3ab9148b1" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_mail.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3cee717f65ee50c0170f4f2c249713f3 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b26158ab0ca5d3873e99246f58093c9d 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9348902335df6e5d1a8058b619a159e8 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7cde40c4866a304cb2a1003f0e86c0d0 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=34acfa7de14890f6430ac1b28e1b7dad 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8e7d3ba7e87ca11b046fd42923380f5a 2500w" />
</Frame>

## Inspecting mails

You may inspect the header values of an email by opening the sidebar of the email window at the top right.

The HTML source of the email or the raw email content are available via right-click on the email itself. They open in a new window, and you can open raw or HTML content of multiple mails at the same time.

<Frame>
  <img alt="Herd Pro Mail Server with a mail" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=092a2ed1314d5138b08f192d0bb33383" data-og-width="2774" width="2774" data-og-height="1712" height="1712" data-path="images/docs/mails-headers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=787e5717e0441d2ba005ef63ad189630 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=64f0a511ba23643101cb218794b33bc3 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d1764021224c945f85fe3dddcf5e2016 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c53bbeade8273206b94aa706f2248d5f 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=985a3b73a57654c1c0053bda7e6cb745 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d3344c3cc84238439beda6b1ccecc32e 2500w" />
</Frame>

## Attachments

Herd stores all attachments in your Herd application directory and creates a folder for each email with all attached files. You can either open them from this folder or directly from the email.

```
~/Library/Application Support/Herd/Log/mail
```

## Deleting mails

You can delete single emails by selecting the email and pressing the `Backspace` key but if you want to get rid of a whole inbox, you can use the trash icon in the top bar of the mail window.

## Troubleshooting

If you accidentally sent thousands of emails to Herd or something is wrong, you can check the SQLite database file where Herd stores all emails. You can find the file at:

```
~/Library/Application Support/Herd/HerdCoreData.sqlite
```

You can truncate all mail related tables in this file without breaking the rest of the application.
