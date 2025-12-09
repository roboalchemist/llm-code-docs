# Source: https://rustdesk.com/docs/en/self-host/rustdesk-server-pro/installscript/script/

# install.sh

Note

Don&rsquo;t forget to get your license from https://rustdesk.com/pricing/, check license page for more details.

Please read OSS installation first before doing this simple install. You can know more underlying details there.

## Install

Copy and paste the above command into your Linux terminal to install RustDesk Server Pro.

`wget -qO- https://raw.githubusercontent.com/rustdesk/rustdesk-server-pro/main/install.sh | bash`

Note

I recommend using the Docker image; it greatly simplifies the process of deploying the solution as well as updating it. The resource consumption is very low.

And please run above under your home directory rather than a diretory you have no write permission.

What it does:

- Install some dependencies
- Setup UFW firewall if available
- Create a working directory `/var/lib/rustdesk-server` and a log directory `/var/log/rustdesk-server`
- Installs executables into `/usr/bin`
- Download and extract RustDesk Pro Services to the above folder
- Create systemd services for hbbs and hbbr (service names are `rustdesk-hbbs.service` and `rustdesk-hbbr.service`)
- If you choose Domain, it will install Nginx and Certbot, allowing the API to be available on port `443` (HTTPS) and get an SSL certificate over port `80`, it is automatically renewed. When the https is ready, please access with `https://yourdomain.com` rather than `https://yourdomain.com:21114`.

Note

How to Set up HTTPS for web console manually.

Note

If the systemd service fails to start, it is probably related to SELinux, please check this.

Note

If your client cannot connect to your server or you cannot access the web console, please check this.

## Upgrade

Copy and paste the above command into your Linux terminal to upgrade your existing RustDesk Server Pro installation, this could also be saved locally and scheduled with cron.

`wget -qO- https://raw.githubusercontent.com/rustdesk/rustdesk-server-pro/main/update.sh | bash`

Note

If you encounter issues with this script, I would suggest you go through the script and execute the steps manually, one by one.

And please run above under your home directory rather than a diretory you have no write permission.

What it does:

- Checks for new versions of RustDesk Server Pro
- If it finds a new version, it removes the API files and downloads new executables and API files

## Convert from open source

Copy and paste the above command into your Linux terminal to convert from RustDesk Server to RustDesk Server Pro.

`wget -qO- https://raw.githubusercontent.com/rustdesk/rustdesk-server-pro/main/convertfromos.sh | bash`

Note

Please add `21114` TCP port to your firewall, this is additional port for web console and user login in RustDesk client.

Note

I would suggest switching to a Docker installation if you encounter issues with this script. Alternatively, you can go through the script and execute the steps manually, one by one.

What it does:

- Disable and removes the old services
- Install some dependencies
- Setup UFW firewall if available
- Create a folder `/var/lib/rustdesk-server` and copy the certs here
- Delete `/var/log/rustdesk` and create `/var/log/rustdesk-server`
- Download and extract RustDesk Pro Services to the above folder
- Create systemd services for hbbs and hbbr (service names are rustdesk-hbbs.service and rustdesk-hbbr.service)
- If you choose Domain, it will install Nginx and Certbot, allowing the API to be available on port 443 (HTTPS) and get an SSL certificate over port 80, it is automatically renewed