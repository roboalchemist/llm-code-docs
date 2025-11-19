# Source: https://herd.laravel.com/docs/macos/troubleshooting/restarting-services.md

# Restarting Services

# Restarting Herd Services

It might happen that Herd displays that a service like `FPM` is not running for a specific PHP version. This can happen if Herd is unable to properly shut down all background services when you close the app or migrate from a previous setup.

## Via the GUI

You may force a restart of all Herd services by clicking on the Herd icon in the menu bar and holding the `option` key `⌥`.
This will change the `Stop all` menu item to `Force stop all`. Click on it to forcefully stop all Herd services, and then click on `Start all` to restart them.

## Via the terminal

To kill all stray services, go to your terminal and perform the `killall` command for every service that is still running, naming the services.

## Force a shutdown of all Herd services

This command shuts down all processes that Herd might run (PHP 7.4 - 8.4, Nginx and Dnsmasq).

### Shutdown all Herd services on Apple Silicon Macs

```shell  theme={null}
sudo killall nginx-arm64 dnsmasq-arm64 \
php74-fpm \
php80-fpm \
php81-fpm \
php82-fpm \
php83-fpm \
php84-fpm
```

### Shutdown all Herd services on Intel Macs

```shell  theme={null}
sudo killall nginx-x86 dnsmasq-x86 \
php74-fpm \
php80-fpm \
php81-fpm \
php82-fpm \
php83-fpm \
php84-fpm
```

## Restart the background service

Herd has a background service that is responsible for running nginx and dnsmasq as root on your machine. You can shutdown this services by terminating if via the activity monitor of macOS and searching for a service with the name `de.beyondco.herd.helper`.
