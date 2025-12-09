# Source: https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/synology/dsm-7/

# Synology DSM 7.2

After DSM 7.2 update, Synology renamed their &ldquo;Docker&rdquo; package to &ldquo;Container Manager&rdquo;. It brings a new GUI, and comes with &ldquo;docker-compose&rdquo; within its GUI, which make you create Docker more easily.

## Supported models and requirements

Container Manager brings ARM64 support for some low-end models, such as J series, for detail list of supported model, please check Synology website.
Most of time you won&rsquo;t need to install extra RAM for install Docker and RustDesk Server.

## 1. Install Container Manager (Docker)

Open &ldquo;Package Center&rdquo;, search and install &ldquo;Container Manager&rdquo;.

## 2. Create folder

After you installed &ldquo;Container Manager&rdquo;, it will create a Shared Folder called `docker`, let&rsquo;s put our server&rsquo;s data here.

Open your File Station, create a folder named `rustdesk-server`(or whatever you like). Then create a folder named `data` in it just like the picture.

## 3. Create container

Open your Container Manager, go to Project and click Create.

Enter the project name `rustdesk-server` and change Source from &ldquo;Upload compose.yml&rdquo; to &ldquo;Create compose.yml&rdquo;, and copy following contents to the box.

```
services:
  hbbs:
    container_name: hbbs
    image: rustdesk/rustdesk-server:latest # Please change this to rustdesk/rustdesk-server-pro:latest if you want to install Pro.
    command: hbbs
    volumes:
      - ./data:/root
    network_mode: host
    depends_on:
      - hbbr
    restart: always

  hbbr:
    container_name: hbbr
    image: rustdesk/rustdesk-server:latest # Please change this to rustdesk/rustdesk-server-pro:latest if you want to install Pro.
    command: hbbr
    volumes:
      - ./data:/root
    network_mode: host
    restart: always

# Because using docker host mode
# Just in case you forgot the ports:
# 21114 TCP for web console, only available in Pro version
# 21115 TCP for NAT type test
# 21116 TCP TCP hole punching
# 21116 UDP heartbeat/ID server
# 21117 TCP relay
```

Please skip `Web portal settings` then done.

## 4. Check it is working

Open your File Station, you should see `id_ed25519`, `id_ed25519.pub` on your `docker/rustdesk-server/data` folder. You could download it and open it though any text editor or use Synology Text Editor. This is the public key that you need for your RustDesk client.

The public key will looks like this:

Check here to set up your client. Only `ID server` and `Key` is needed. `Relay server` isn&rsquo;t needed because we&rsquo;ve set it in `hbbs`, `hbbs` will provide this information automatically.

## 5. Set port forwarding on your router

Go to your router&rsquo;s admin webpage, find anything related to `Port forwarding`, it should appear in `WAN` or `Firewall` settings.

If you still can&rsquo;t find the setting, Google search `{Router brand} + port forwarding` or `{Router model} + port forwarding`. If this device is from your ISP, ask them.

Open these required ports:

- `21114` TCP for web console, only available in Pro version
- `21115` TCP for NAT type test
- `21116` TCP TCP hole punching
- `21116` UDP heartbeat/ID server
- `21117` TCP relay