# Source: https://docs.searxng.org/admin/installation-scripts.html

[]

# Installation Script[¶](#installation-script "Link to this heading")

Update the OS first!

To avoid unwanted side effects, update your OS before installing SearXNG.

The following will install a setup as shown in [[the reference architecture]](architecture.html#arch-public). First you need to get a clone of the repository. The clone is only needed for the installation procedure and some maintenance tasks.

further read

-   [[DevOps tooling box]](../utils/index.html#toolboxing)

Jump to a folder that is readable by *others* and start to clone SearXNG, alternatively you can create your own fork and clone from there.

    $ cd ~/Downloads
    $ git clone https://github.com/searxng/searxng.git searxng
    $ cd searxng

further read

-   [[How to inspect & debug]](update-searxng.html#inspect-searxng)

To install a SearXNG [[reference setup]](installation-searxng.html#use-default-settings-yml) including a [[uWSGI setup]](architecture.html#architecture-uwsgi) as described in the [[Step by step installation]](installation-searxng.html#installation-basic) and in the [[uWSGI]](installation-uwsgi.html#searxng-uwsgi) section type:

    $ sudo -H ./utils/searxng.sh install all

Attention

For the installation procedure, use a *sudoer* login to run the scripts. If you install from [`root`], take into account that the scripts are creating a [`searxng`] user. In the installation procedure this new created user does need to have read access to the cloned SearXNG repository, which is not the case if you clone it into a folder below [`/root`]!

further read

-   [[How to update]](update-searxng.html#update-searxng)

When all services are installed and running fine, you can add SearXNG to your HTTP server. We do not have any preferences regarding the HTTP server, you can use whatever you prefer.

We implemented installation procedures for:

-   [[NGINX]](installation-nginx.html#installation-nginx)

-   [[Apache]](installation-apache.html#installation-apache)