# Source: https://herd.laravel.com/docs/macos/guides/wordpress.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# WordPress

# How to set up a WordPress site

While Herd was mainly developed with Laravel in mind, most concepts apply to working with WordPress, too. Herd supports standard WordPress setups as well as Bedrock with its different folder structure. This guide covers the installation of a standard WordPress site via a zip file but you can apply the same concepts when using the WordPress CLI or cloning a git repository.

## Code Directory

Herd uses the concept of *parked paths* for serving sites via `.test` domains. By default, Herd creates and parks the `~/Herd` directory and every folder that you create in this directory is reachable via its own domain.

This means that you can simply move or install a site to this directory and don't have to create it via the Site Manager in Herd – it just works.

## Database Setup

While Laravel uses SQLite as default, WordPress requires either MySQL or MariaDB as database service for your site. You can set up this database via a free tool like [dbngin](https://dbngin.com) or set up a database instance via a [Herd service](/macos/herd-pro-services/services).

<Note>
  [Herd Pro]() allows you to install database instances and other complementary services directly from Herd – but you can also download and run the database of your choice separately.
</Note>

## Local Domains

As described above, Herd serves all directories in your parked paths via local `.test` domains. This means that you can move a site into the directory `my-wordpress-site` and access it via [http://my-wordpress-site.test](http://my-wordpress-site.test).

If you are running a multisite and want to point multiple domains to a single WordPress installation, you can use Herd links to create more local domains. You can either do that via the Site Manager as described in the chapter [linking sites](/macos/getting-started/sites#linking-an-existing-site) or use the terminal with the commands below.

```bash  theme={null}
cd ~/Herd/my-wordpress-site
herd link my-second-domain
```

These commands go into your site directory and create the local domain [http://my-second-domain.test](http://my-second-domain.test) to your site. It's now accessible via both domains and you can proceed with your normal configuration.

## Drivers

Herd uses drivers to detect frameworks and serve sites to your browser. These drivers support standard WordPress installations and Bedrock but you can write [custom drivers](/macos/extending-herd/custom-drivers) if you are using a different setup for your site. So if your setup is supported by default, you can skip this step but it's important to know that customized installations might need a custom driver or there will simply be a 404 error.

## Installation

The installation of a new WordPress site is straight forward. At first, you need to set up a database. Herd Pro users can go to `Settings > Services` and select their MySQL instance and then open TablePlus or AdminerEvo in the menu on the right to create the database. If you are familiar with MySQL on the command line, you can do that as well.

After that, simply follow these steps:

1. Download the latest version of WordPress from the [official site](https://wordpress.org/download/)
2. Extract the zip file into a parked Herd directory, for example `~/Herd`
3. Rename the directory to your domain, in this guide, we're using the local domain `wordpress-guide.test`, so the directory name is `wordpress-guide`.
4. Go to [http://wordpress-guide.test](http://wordpress-guide.test) and follow the installation process.

If you are using a different port for your database instance, make sure to add this port to the database host during the installation. When using Herd, the database username is `root` and has no password.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b8b42cbcaa62cd3b3ad5bdaad990c71e" data-og-width="1570" width="1570" data-og-height="1352" height="1352" data-path="images/docs/guides_wordpress_database.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a915cb826c5addc45f18c126fadc336a 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=08505e86b49b8837ef23742f83c15263 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5bfb0dd99bf5112099998ba5887ca323 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=eaf692677092428a43f4e37505ab06aa 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c82bf7921b47695e53f4fb78c9bf2947 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4cc083a2baae911d8545c902072d7b2a 2500w" />
</Frame>

Your WordPress site is now running via Herd and you can start working on it.

## Debugging with Dumps

[Herd Pro](/#plans) allows you to debug your site with a convenient `dump` helper. So if you're working on plugins and need to output data for debugging purposes, this is super powerful. In this example, we\`re creating a very basic plugin and dumping a string and all existing posts of the fresh WordPress install.

```php  theme={null}
/*
Plugin Name: My Herd Plugin
Plugin URI: https://example.com/my-herd-plugin
Description: A simple plugin to demonstrate WordPress plugin development.
Version: 1.0
Author: Your Name
Author URI: https://example.com
License: GPL2
*/

// Hook into an action
add_action('wp_head', 'my_custom_function');

function my_custom_function() {
    dump("Hello from Herd 👋");
    dump(get_posts());
}
```

When opening any page of your site, the function runs and sends the debug output to the dumps window where it looks like this example.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3794b56425f6ed2e9f87ab57bdaf3280" data-og-width="1914" width="1914" data-og-height="1660" height="1660" data-path="images/docs/guides_wordpress_dumps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=183f6716062bc5b61088c9a145b82bcd 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=10855adf35fb9591ef3591be72b143ce 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cd1381bd9d2eb18dff2d75662d37a08b 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b4798242a440a3f1eb99ae00de45aa3d 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b73f71f7e22a2186560da91e32ae2ceb 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=54f4fe178b74ee9d6dfcd2d1d8361b9c 2500w" />
</Frame>

## Test Emails

Testing emails can be cumbersome and even result in sending emails to your users when you're connected to a real mail service. Herd solves this by running a local email server that catches your mails and sends them to an internal email client that you can use for testing the email.

The quickest way to set up mails in Herd Pro is by defining a mailer in the `functions.php`. Simply paste the following snippet to the end of your `functions.php` to receive emails in Herd.

```php  theme={null}
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

Every time when your application sends an email, it uses Herd's integrated mail service. If it's the first email from this application, it creates an inbox for this application based on the username of the configuration so that you can easily identify emails and where they are from.

You can test this feature by logging out of your site and using the password reset form to trigger an email.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=131f3b183c1da67a1a6143dd94934499" data-og-width="2134" width="2134" data-og-height="1304" height="1304" data-path="images/docs/guides_wordpress_mails.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b0747bcf08b25316db08074e71f498eb 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5b07c818918c8923ac88979c6d4eb2c1 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c9b8d4e411fc993b4e4c9f76f3a08c5f 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ea430aa911399a2110a876e5c63016fb 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=80e205a5acff0788d624f0d8ce6cacc5 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=318abdddd2a121e8a5ff3ddf96c01136 2500w" />
</Frame>

After setting up your first WordPress site in Herd, you can now follow the docs to learn more about all features in more detail and fully leverage Herd when using it every day.
