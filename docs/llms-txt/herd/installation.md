# Source: https://herd.laravel.com/docs/macos/getting-started/installation.md

# Installation

export const InlineNewsletterForm = ({id}) => <div className="newsletter-card-container">
        <Card>
            <div className="newsletter-card-content">
                <h1 className="font-medium text-2xl sm:text-3xl text-gray-800 dark:text-white">Laravel Herd Quick Wins</h1>
                <div className="text-lg text-gray-800 dark:text-white mb-4">Make the most of Herd in your first week — even if you're new to Laravel. Written for the 50,000+ devs using Herd every day.</div>
            </div>
            
            <script src="https://f.convertkit.com/ckjs/ck.5.js"></script>
            <form action={`https://app.kit.com/forms/${id}/subscriptions`} method="post" data-sv-form={id} data-uid="19dc730a0c" data-format="inline" data-version="5" className="pt-2 mb-8" data-options="{&quot;settings&quot;:{&quot;after_subscribe&quot;:{&quot;action&quot;:&quot;message&quot;,&quot;success_message&quot;:&quot;Success! Please check your email to confirm your subscription.&quot;,&quot;redirect_url&quot;:&quot;&quot;},&quot;analytics&quot;:{&quot;google&quot;:null,&quot;fathom&quot;:null,&quot;facebook&quot;:null,&quot;segment&quot;:null,&quot;pinterest&quot;:null,&quot;sparkloop&quot;:null,&quot;googletagmanager&quot;:null},&quot;modal&quot;:{&quot;trigger&quot;:&quot;timer&quot;,&quot;scroll_percentage&quot;:null,&quot;timer&quot;:5,&quot;devices&quot;:&quot;all&quot;,&quot;show_once_every&quot;:15},&quot;powered_by&quot;:{&quot;show&quot;:false,&quot;url&quot;:&quot;https://kit.com/features/forms?utm_campaign=poweredby&amp;utm_content=form&amp;utm_medium=referral&amp;utm_source=dynamic&quot;},&quot;recaptcha&quot;:{&quot;enabled&quot;:false},&quot;return_visitor&quot;:{&quot;action&quot;:&quot;show&quot;,&quot;custom_content&quot;:&quot;&quot;},&quot;slide_in&quot;:{&quot;display_in&quot;:&quot;bottom_right&quot;,&quot;trigger&quot;:&quot;timer&quot;,&quot;scroll_percentage&quot;:null,&quot;timer&quot;:5,&quot;devices&quot;:&quot;all&quot;,&quot;show_once_every&quot;:15},&quot;sticky_bar&quot;:{&quot;display_in&quot;:&quot;top&quot;,&quot;trigger&quot;:&quot;timer&quot;,&quot;scroll_percentage&quot;:null,&quot;timer&quot;:5,&quot;devices&quot;:&quot;all&quot;,&quot;show_once_every&quot;:15}},&quot;version&quot;:&quot;5&quot;}">
                <div data-style="clean">
                    <ul class="formkit-alert formkit-alert-error" data-element="errors" data-group="alert"></ul>
                    <div data-element="fields" className="formkit-fields">
                        <input className="formkit-input w-full" name="email_address" aria-label="Email Address" placeholder="Email Address" required type="email" style={{
  borderColor: "rgb(227, 227, 227)",
  minWidth: "350px",
  flexGrow: 0
}} />
                        <button data-element="submit" className="py-3 w-full px-8 bg-brand text-white font-bold rounded-lg">
                            <span>Subscribe</span>
                        </button>
                    </div>
                </div>
            </form>
        </Card>
    </div>;

<CardGroup cols={2}>
  <Card title="Download Herd" icon="download" href="https://herd.laravel.com/download">
    Download Laravel Herd
  </Card>

  <Card title="Purchase Herd Pro" icon="credit-card" href="https://herd.laravel.com/checkout">
    Purchase a license for Herd Pro
  </Card>
</CardGroup>

# Why Herd?

Herd is a blazing fast, native Laravel and PHP development environment for macOS.
It provides everything that you need to get started with Laravel development. It ships with PHP, [nginx](https://nginx.org/en/), [dnsmasq](https://en.wikipedia.org/wiki/Dnsmasq) and [Node.js](https://nodejs.org/).

You can integrate Herd with [Laravel Forge](https://forge.laravel.com) and use a single tool from setting up your site locally to deploying it on a remote server.

[Herd Pro](https://herd.laravel.com/#features) completes your development environment with service management for databases, caches, and more. It comes with testing and debugging tools tailored to Laravel and you'll love them when you're working on web applications every day.

After installing Herd, it serves all sites on your machine via `*.test` domains – it's like [Laravel Valet](https://laravel.com/docs/valet) but has no dependencies and doesn't need Homebrew. It ships with its own, pre-compiled binaries which makes it blazing fast to install and use.

More than 50,000 web developers use Herd every day to create awesome web applications for their users, and [they love it](https://herd.laravel.com/#testimonials).

<InlineNewsletterForm id="7711601" />

# Requirements

Herd requires macOS 12.0 or higher.

# Installation

You can download the latest version of Herd [here](https://herd.laravel.com/download).

After downloading the DMG file, double-click the file to open it, and drag the Herd icon to the Applications folder. Once Herd is installed, open it from your Applications folder which triggers the onboarding process.

The onboarding process downloads the latest PHP version and installs a Herd background service on your machine. This background service needs admin permissions and is responsible for handling nginx and dnsmasq.

After the installation process is complete, you have a fully-functioning PHP and Laravel development environment. This means you can invoke the `herd`, `php`, `laravel`, and `composer` binaries from your terminal:

```shell  theme={null}
herd --version
php --version
laravel --version
composer --version
node --version
```

Herd does not alter any existing services on your system, and if it's not for you, you can easily switch back to your previous setup.

If you migrate from a different development setup, we've dedicated guides for [Laravel Sail](/macos/migration-guides/sail) and [MAMP/MAMP PRO](/macos/migration-guides/mamp) and a quick one from Laravel Valet below.

User from a different setups or beginners can go to the next chapter and [learn how to manage your sites](/macos/getting-started/sites) with Herd.

# Migrate from Valet

Herd makes it easy to migrate all of your existing Valet sites, certificates and settings to Herd.
Upon opening Herd for the first time, Herd automatically detects your existing Valet installation and migrates all existing sites, certificates and settings to Herd.

If Valet is still running, Herd asks you to stop Valet before continuing with the installation.

It is important to note that Herd will does not modify your existing Valet installation in any way. This means that you can easily switch back to Valet at any time.
Just quit Herd and run `valet start` to start Valet again.

## Using Herd with Fish

If you are using the [Fish](https://fishshell.com/) shell, you need to run the following command to add the Herd binaries to your path:

```shell  theme={null}
fish_add_path -U $HOME/Library/Application\ Support/Herd/bin/
```
