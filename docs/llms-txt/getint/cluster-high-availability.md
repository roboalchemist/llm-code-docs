# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/on-premise-deployment/cluster-high-availability.md

# Cluster High Availability

## Monitoring

## Availability&#x20;

Getint.io Cluster application is a combination of different components, mainly Java Application, PostgreSQL database, NGINX balancer. All being built with different frameworks and running independently from each other. All can run on a one or multiple machines, it all depends on a deployment architecture you select.&#x20;

All of above, can become a point of failure, but after all, business directly depends on a Cluster application and this is what we will focus in first place to monitor and ensure highest possible uptime.

We decided to prepare for you a short guide taking you step by step on how to setup basic and efficient low level monitoring over a Cluster application processes with **Monit** and how to start them up in case of failure.

**Install Monit**

```
sudo apt-get update && sudo apt-get upgrade
sudo apt install monit
sudo monit
```

**Configure**

```
sudo systemctl status monit
# you should see info saying monit is running

sudo vim /etc/monit/monitrc
# - change interval to 60 seconds:
# - uncomment set httpd lines if you want to access monit web ui
```

/etc/monit/monitrc file would look like this

```
  set daemon 60            # check services at 2-minute intervals
  with start delay 240    # optional: delay the first check by 4-minutes (by

  set log /var/log/monit.log

  set idfile /var/lib/monit/id
  set statefile /var/lib/monit/state

  set eventqueue
      basedir /var/lib/monit/events # set the base directory where events will be stored
      slots 100                     # optionally limit the queue size

 set httpd port 2812 and
     use address <YOUR_IP_ADDRESS>  # only accept connection from localhost
     allow localhost        # allow localhost to connect to the server and
     allow admin:monit      # require user 'admin' with password 'monit'

   include /etc/monit/conf.d/*
   include /etc/monit/conf-enabled/*
```

Reload Monit

```
sudo systemctl restart monit
sudo systemctl enable monit
```

..
