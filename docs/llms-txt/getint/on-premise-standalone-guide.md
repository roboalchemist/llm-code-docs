# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/on-premise-deployment/installing-getint-onpremise/on-premise-standalone-guide.md

# On-Premise/Standalone Guide

### Changing Getint license

* Navigate to SYSTEM
* Click on LICENSE tab
* Click EDIT button
* Paste received license from support team
* Click SUBMIT button

New license should be applied and already used by GetInt

### Running GetInt on different HTTP port / HTTPS

GetInt application is Java web application that as all other web apps, can be run on different HTTP ports. HTTP port 80 is a default port.&#x20;

**How to change port?**

You can simply change it in getint.env file, value for PORT variable, e.g. change it to 8080 port.

```
PORT=8080
```

After a change restart of application will be needed.

**Setting up HTTPS with SSL certificate**

At the moment, easiest way of doing this is to use some proxy server like NGINX which will handle SSL certificates and proxy traffic to GetInt application.

For NGINX, here is a configuration file that when included into NGINX main configuration, will listen at 443 port and for traffic to \<DOMAIN>. It is loading SSL cert and key. Such traffic will be internally proxied to GetInt application running on \<PORT> port.

\<DOMAIN> and \<PORT> is sth that you have to specify according to your GetInt deployment. \<DOMAIN> is domain name which you open when you want to access GetInt and \<PORT> is a port defined in getint.env file.

```
server { 
    listen 443; 
    server_name <DOMAIN>; 
    ssl_certificate     /opt/getint/certs/fullchain.pem;
    ssl_certificate_key /opt/getint/certs/privkey.pem;
    ssl on; 
    ssl_session_cache  builtin:1000  shared:SSL:10m;
    ssl_protocols  TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers HIGH:!aNULL:!eNULL:!EXPORT:!CAMELLIA:!DES:!MD5:!PSK:!RC4;
    ssl_prefer_server_ciphers on; 
    
    location / { 
        proxy_pass http://localhost:<PORT>; 
        proxy_set_header        Host $host; 
        proxy_set_header        X-Real-IP $remote_addr; 
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for; 
        proxy_set_header        X-Forwarded-Proto $scheme;
        proxy_read_timeout  90; 
        proxy_redirect http://127.0.0.1:<PORT> $host;
    } 
}
```

### Updating version

At the moment updates are handled manually.&#x20;

There is experimental feature for performing updates in almost fully automatic way but its not yet ready to use in production.&#x20;

**Manual way**

* Download and unpack new version of GetInt
* From unpacked directory, copy getint.jar file from synchronizer/libs dir and copy to \<CURRENT\_INSTALLATION>/synchronizer/libs directory
* Restart application

{% embed url="<https://www.youtube.com/watch?v=uCHNWq1jdiU>" %}
