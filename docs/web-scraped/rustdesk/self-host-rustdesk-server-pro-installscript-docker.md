# Source: https://rustdesk.com/docs/en/self-host/rustdesk-server-pro/installscript/docker/

# Docker

## Docker Compose (Recommended)

With Docker Compose you HAVE to use `network_mode: "host"` to ensure licensing works. Install Docker using this guide to ensure its the most up to date!

Copy the below into `compose.yml`.

```
services:
  hbbs:
    container_name: hbbs
    image: docker.io/rustdesk/rustdesk-server-pro:latest
    command: hbbs
    volumes:
      - ./data:/root
    network_mode: &#34;host&#34;

    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: hbbr
    image: docker.io/rustdesk/rustdesk-server-pro:latest
    command: hbbr
    volumes:
      - ./data:/root
    network_mode: &#34;host&#34;
    restart: unless-stopped
```

Then run `sudo docker compose up -d` or `podman-compose up -d`

`sudo apt install podman-compose` for `podman-compose` installation

Note

How to Set up HTTPS for web console manually.

## Docker Commands

Install Docker with this guide to ensure its the most up to date!

Or you can install docker with this single command.

```
bash <(wget -qO- https://get.docker.com)
```

Run the following commands (s6 image may need `./data:/data` instead of `./data:/root`):

```
sudo docker image pull rustdesk/rustdesk-server-pro
sudo docker run --name hbbs -v ./data:/root -td --net=host --restart unless-stopped docker.io/rustdesk/rustdesk-server-pro hbbs
sudo docker run --name hbbr -v ./data:/root -td --net=host --restart unless-stopped docker.io/rustdesk/rustdesk-server-pro hbbr
```

Note

The above example uses `sudo` and `--net=host`, this will not work on Windows please remove these commands, if you remove `--net=host` please check below.

```
macaddrhbbs=$(echo -n A0-62-2F; dd bs=1 count=3 if=/dev/random 2>/dev/null |hexdump -v -e '/1 &#34;-%02X&#34;')
sudo docker run --name hbbs -p 21114:21114 -p 21115:21115 -p 21116:21116 -p 21116:21116/udp -p 21118:21118 -v ./data:/root -td --mac-address=&#34;$macaddrhbbs&#34; --restart unless-stopped docker.io/rustdesk/rustdesk-server-pro hbbs
sudo docker run --name hbbr -p 21117:21117 -p 21119:21119 -v ./data:/root -td --restart unless-stopped docker.io/rustdesk/rustdesk-server-pro hbbr
```

Note

How to Set up HTTPS for web console manually.

If you have problem with SELinux on Fedora, please check this issue.