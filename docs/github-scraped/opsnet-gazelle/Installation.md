# Installation Notes

Note: We make no guarantee of completeness or accuracy of these install notes.
The most up-to-date notes on a basic install setup is found through our
docker-compose.yml setup we use for development. Please reference it before
asking questions.

Note: If overwhelmed by these instructions, we urge you to NOT run a tracker
in production. Doing such requires more additional steps not covered here
(setting up proxies, tunneling, LUKS encryption, TCP tuning, etc.) that messing
up would put the privacy / security of both yourself and your users at risk.

The docker installation does all this for you, but in production you need
to do this by hand.

## Step 1: Install Dependencies

First, install the PHP and JS dependencies to setup and run the site:

```bash
composer install
npm install
```

## Step 2: Install Services

Install and setup the following services:

* MySQL
* memcached
* sphinxsearch

Depending on your OS, these may be available in the package manager. You can see
what versions of the above we support by looking at our docker-compose.yml
configuration.

## Step 3: Configure Memcached

For up memcached, we recommend giving it multiple threads and several
gigs of RAM, for example:

```bash
memcached -d -m 5120 -s /var/run/memcached.sock -a 0777 -t4 -C -u nobody
```

This will give memcached 4 threads and 5GB of RAM. Tune this accordingly
depending on how large your server and how many users you have. Look at
your cache eviction. If you are seeing hundreds of items evicted per second,
you need to scale up drastically. If you are seeing zero evictions, you
have allocated too much RAM and should scale down. Ideally you should only
see expired unfetched activity.

## Step 4: Create MySQL Roles

Create the required MySQL roles according to [MySQL Roles](MySQL-Roles.md).
Use <www.random.org> to generate passwords.

## Step 5: Configure Application

Review `lib/config.php`. Edit `lib/override.config.php` as needed.
You should be able to launch boris from the command line.

## Step 6: Run Migrations

Run the phinx migrations to populate the database:

```bash
vendor/bin/phinx migrate
vendor/bin/phinx migrate -c misc/phinx-pg.php
```

## Step 7: Configure Sphinx

We recommend you use the included `misc/docker/sphinxsearch/sphinx.conf`.
You can copy this to `/etc/sphinx/sphinx.conf`. You need to fill in the
details of the SQL server from `lib/override.config.php` and you may need to
create the `/var/lib/sphinx` folder.

More information is available at: <https://sphinxsearch.com/docs/current.html>

Run the indexer to finish the setup:

```bash
/usr/bin/indexer -c /etc/sphinx/sphinx.conf --all
```

## Step 8: Build Stylesheets

Generate stylesheets and their previews by running:

```bash
npm run build
```

Note, generating the previews requires a Chrome instance on the host.

## Step 9: Setup Web Server

Setup your web server. We recommend using nginx (<https://nginx.com/>).
A sample configuration for nginx can be found in `misc/docker/web/nginx.conf`.

## Step 10: Setup Cronjobs

Set up the cronjobs for the background task scheduler and Sphinx updates.
See [Crontab](Crontab.md).

## Step 11: Start Developing

Start modifying stuff. Hopefully, everything will have gone smoothly so far
and nothing will have exploded.
