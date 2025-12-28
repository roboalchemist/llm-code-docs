# Source: https://docs.searxng.org/admin/installation-nginx.html

[]

# NGINX[¶](#nginx "Link to this heading")

This section explains how to set up a SearXNG instance using the HTTP server [nginx](https://docs.nginx.com/nginx/admin-guide/). If you have used the [[Installation Script]](installation-scripts.html#installation-scripts) and do not have any special preferences you can install the [[SearXNG site]](#nginx-searxng-site) using [[searxng.sh]](../utils/searxng.sh.html#searxng-sh-overview):

    $ sudo -H ./utils/searxng.sh install nginx

If you have special interests or problems with setting up nginx, the following section might give you some guidance.

further reading

-   [nginx](https://docs.nginx.com/nginx/admin-guide/)

-   [nginx beginners guide](https://nginx.org/en/docs/beginners_guide.html)

-   [nginx server configuration](https://docs.nginx.com/nginx/admin-guide/web-server/web-server/#setting-up-virtual-servers)

-   [Getting Started wiki](https://www.nginx.com/resources/wiki/start/)

-   [uWSGI support from nginx](https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html)

```
<!-- -->
```
-   [The nginx HTTP server](#the-nginx-http-server)

-   [NGINX's SearXNG site](#nginx-s-searxng-site)

-   [Disable logs](#disable-logs)

## [The nginx HTTP server](#id2)[¶](#the-nginx-http-server "Link to this heading")

If [nginx](https://docs.nginx.com/nginx/admin-guide/) is not installed, install it now.

Ubuntu / debian

Arch Linux

Fedora / RHEL

    sudo -H apt-get install nginx

    sudo -H pacman -S nginx-mainline
    sudo -H systemctl enable nginx
    sudo -H systemctl start nginx

    sudo -H dnf install nginx
    sudo -H systemctl enable nginx
    sudo -H systemctl start nginx

Now at [http://localhost](http://localhost) you should see a *Welcome to nginx!* page, on Fedora you see a *Fedora Webserver - Test Page*. The test page comes from the default [nginx server configuration](https://docs.nginx.com/nginx/admin-guide/web-server/web-server/#setting-up-virtual-servers). How this default site is configured, depends on the linux distribution:

Ubuntu / debian

Arch Linux

Fedora / RHEL

    less /etc/nginx/nginx.conf

There is one line that includes site configurations from:

    include /etc/nginx/sites-enabled/*;

    less /etc/nginx/nginx.conf

There is a configuration section named [`server`]:

    server 

    less /etc/nginx/nginx.conf

There is one line that includes site configurations from:

    include /etc/nginx/conf.d/*.conf;

[]

## [NGINX's SearXNG site](#id3)[¶](#nginx-s-searxng-site "Link to this heading")

Now you have to create a configuration file ([`searxng.conf`]) for the SearXNG site. If [nginx](https://docs.nginx.com/nginx/admin-guide/) is new to you, the [nginx beginners guide](https://nginx.org/en/docs/beginners_guide.html) is a good starting point and the [Getting Started wiki](https://www.nginx.com/resources/wiki/start/) is always a good resource *to keep in the pocket*.

Depending on what your SearXNG installation is listening on, you need a http or socket communication to upstream.

socket

http

    location /searxng 

    # To serve the static files via the HTTP server
    #
    # location /searxng/static/ 

    location /searxng 

    # To serve the static files via the HTTP server
    #
    # location /searxng/static/ 

The [[Installation Script]](installation-scripts.html#installation-scripts) installs the [[reference setup]](installation-searxng.html#use-default-settings-yml) and a [[uWSGI setup]](installation-uwsgi.html#uwsgi-setup) that listens on a socket by default.

Ubuntu / debian

Arch Linux

Fedora / RHEL

Create configuration at [`/etc/nginx/sites-available/`] and place a symlink to [`sites-enabled`]:

    sudo -H ln -s /etc/nginx/sites-available/searxng.conf \
                  /etc/nginx/sites-enabled/searxng.conf

In the [`/etc/nginx/nginx.conf`] file, in the [`server`] section add a [include](https://nginx.org/en/docs/ngx_core_module.html#include) directive:

    server 

Create two folders, one for the *available sites* and one for the *enabled sites*:

    mkdir -p /etc/nginx/default.d
    mkdir -p /etc/nginx/default.apps-available

Create configuration at [`/etc/nginx/default.apps-available`] and place a symlink to [`default.d`]:

    sudo -H ln -s /etc/nginx/default.apps-available/searxng.conf \
                  /etc/nginx/default.d/searxng.conf

Create a folder for the *available sites*:

    mkdir -p /etc/nginx/default.apps-available

Create configuration at [`/etc/nginx/default.apps-available`] and place a symlink to [`conf.d`]:

    sudo -H ln -s /etc/nginx/default.apps-available/searxng.conf \
                  /etc/nginx/conf.d/searxng.conf

Restart services:

Ubuntu / debian

Arch Linux

Fedora / RHEL

    sudo -H systemctl restart nginx
    sudo -H service uwsgi restart searxng

    sudo -H systemctl restart nginx
    sudo -H systemctl restart uwsgi@searxng

    sudo -H systemctl restart nginx
    sudo -H touch /etc/uwsgi.d/searxng.ini

## [Disable logs](#id4)[¶](#disable-logs "Link to this heading")

For better privacy you can disable nginx logs in [`/etc/nginx/nginx.conf`].

    http