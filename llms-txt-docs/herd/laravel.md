# Source: https://herd.laravel.com/docs/macos/guides/laravel.md

# Laravel

# How to set up a Laravel application

Herd's main purpose is serving Laravel developers by providing a fully integrated development stack with PHP and nginx at its core. Both services are complemented with all tools that you need to work on almost any Laravel application. This means that Herd is the right tool, no matter if you are just starting as a beginner or work with Laravel for a decade.

This guide covers all steps that you need to follow to get up and running with a new Laravel application but also works if you replace the application creation step with checking out an existing git repository.

## Code Directory

Herd uses the concept of *parked paths* for serving sites via `.test` domains. By default, Herd creates and parks the `~/Herd` directory and every folder that you create in this directory is reachable via its own domain.

Let's open your terminal and go into the directory:

```bash  theme={null}
cd ~/Herd
```

## Database Choices

Laravel ships with an SQLite database for your application by default but if you are familiar with MySQL or PostgreSQL, you should get a database instance up and running before you create or check our your application.

<Note>
  [Herd Pro]() allows you to install database instances and other complementary services directly from Herd – but you can also download and run the database of your choice separately.
</Note>

## Installing Laravel

The easiest way to download and install a fresh Laravel application is the command line. Herd ships with the Laravel installer, and it's already available in your CLI, so switch pack to the terminal and run the following command. The first line creates the application, the second line switches in your application directory for further commands.

```bash  theme={null}
laravel new my-first-application
cd my-first-application
```

If you have an existing Laravel application and git is available on your terminal, simply clone the repository and follow the setup guide for the application's readme file. It's usually something like this:

```bash  theme={null}
git clone path-to-your-repository
cd repository-name
cp .env.example .env
composer install
herd php artisan key:generate
herd php artisan migrate
```

## Visit your application in the browser

Your application is now up and running, and you can visit it via it's `.test` domain. Herd provides a command to open your browser directly from your terminal.

```bash  theme={null}
herd open
```

You can now start working on your application, if you've set up a favorite editor, in the Herd settings, you can open the editor via the command `herd edit`.

[Herd Pro](/#features) users can set up additional services and start using the integrated dump debugging feature, work with emails and check our their logs, so if you are using Herd Pro, this is how they work.

## Set up Services

You can set up and manage [services](/macos/herd-pro-services/services) directly in Herd with a convenient interface. Simply head over to the services tab in the settings and add the service that you need. Herd supports many widely used services like databases, caches, and search-, and storage engines.

### Databases

* [MySQL](/macos/herd-pro-services/mysql)
* [PostgreSQL](/macos/herd-pro-services/postgresql)
* [MongoDB](/macos/herd-pro-services/mongodb)

### Caches and Queues

* [Redis](/macos/herd-pro-services/redis)

### Boradcasting and Realtime

* [Laravel Reverb](/macos/herd-pro-services/laravel-reverb)

### Search

* [Meilisearch](/macos/herd-pro-services/meilisearch)
* [Typesense](/macos/herd-pro-services/typesense)

### Storage

* [MinIO](/macos/herd-pro-services/minio)

You can install all these services with a few clicks and decide if you want to start them with Herd automatically or only on demand.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1e9ddb35805c0f24be4cc37832ecc9f7" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=143a7e51e9b92ed5189c1d64f04130ea 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=08309c5a6b46d8d09bbaddb00c957c5c 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3aec2a3121209890f92af9728a31965e 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=80f9b060ec397fb7cdf863fdd6978fc9 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1eccb7cd7383fa6154a32f5f8073e50c 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a2edeac7a8d42e5634472ce2c0f4af97 2500w" />
</Frame>

## Debug with Dumps

The most common debugging method in Laravel is using the helpers for `dump()` or `dd()`. While `dd` stands for `dump and die` and stops your application, `dump` simply displays some output. Herd Pro has a separate dump window that displays this information in a great way and also allows you to listen for Eloquent queries, logs and more. As a first test, you can invoke the dump function and print out the simple string `hello from your app`.

Go to your terminal and start a tinker session by running the tinker command of the Herd command line interface. It proxies the tinker command of Laravel but always uses the application PHP:

```bash  theme={null}
herd tinker
```

Once tinker has started, you can use the dump helper to output the string:

```bash  theme={null}
dump("hello from your app");
```

When running this simple command, this opens the dump window and displays the string. You can use the `dump` and `dd` helper anywhere in your application to debug browser requests and CLI commands.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3b975ef5a985eb2051d8015d73d64a92" data-og-width="1844" width="1844" data-og-height="1342" height="1342" data-path="images/docs/dumps_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a3ce4cef8e7af2c5bd71f8cc549e1cb0 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=29cbe8f9f64e084d45280079f41e6d28 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=19c8014aa53e82cd33f2387469eb2e80 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b452cc108274a1006e4821ab70fe3bf6 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d940a060b7211ef941f030dc71e416fc 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7ac8ec169b70cdad36a87080fd8028a1 2500w" />
</Frame>

## Test Emails

Testing emails can be cumbersome and even result in sending emails to your users when you're connected to a real mail service. Herd solves this by running a local email server that catches your mails and sends them to an internal email client that you can use for testing the email.

To enable the email server for your application, go to the `env` file in the root of your application directory and make sure to update the mail settings according to the following configuration.

```bash  theme={null}
MAIL_MAILER=smtp
MAIL_HOST=127.0.0.1
MAIL_PORT=2525
MAIL_USERNAME=${APP_NAME}
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS="hello@example.com"
MAIL_FROM_NAME="${APP_NAME}"
```

Every time when your application sends an email, it uses Herd's integrated mail service. If it's the first email from this application, it creates an inbox for this application based on the name of the application so that you can easily identify emails and where they are from.

Please make sure that your application name does not include any special characters or if it does, simply change the `MAIL_USERNAME` in the configuration above to something easily identifiable.

So after you've setup up the mail service, let's test the configuration by creating a test email and sending it via tinker.

```bash  theme={null}
herd php artisan make:mail TestMail --markdown
herd tinker
```

Send the email in your tinker session via the mail facade.

```php  theme={null}
Mail::to('sebastian@beyondcode.com')->send(new \App\Mail\TestMail());
```

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a05f97270532e7f58f75ca0c71698d7a" data-og-width="2774" width="2774" data-og-height="1712" height="1712" data-path="images/docs/mails-intro.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5fe04d828d9379ffbfe0c4358d117abd 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d70f76c42f366bec471a215074af8bab 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c812270bd4bb81c7b7991247745adf6f 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=0736a427709e0d1cc00549fc9d9ed9c9 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=64a6c303ddf269634f3a9a9b7e1a9a49 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=99907f4c16654a68080ecf1e3c0d49f1 2500w" />
</Frame>

After setting up your first Laravel application in Herd, you can now follow the docs to learn more about all features in more detail and fully leverage Herd when using it every day.
