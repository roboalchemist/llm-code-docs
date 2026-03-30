# 6.10.0 (Apr 2019)

Kurento Media Server **6.10** is seeing the light with some important news!

To install it: Installation Guide.

## Hello Ubuntu Bionic

Preliminary support for Ubuntu 18.04 LTS (Bionic Beaver) [https://releases.ubuntu.com/18.04/] has landed in Kurento, and all the CI machinery is already prepared to compile and generate Debian packages into a new repository.

To install KMS on this version of Ubuntu, just follow the usual installation instructions:

```
DISTRO="bionic"  # KMS for Ubuntu 18.04 (Bionic)

sudo apt-key adv \
    --keyserver hkp://keyserver.ubuntu.com:80 \
    --recv-keys 234821A61B67740F89BFD669FC8A16625AFA7A83

sudo tee "/etc/apt/sources.list.d/kurento.list" >/dev/null <<EOF
# Kurento Media Server - Release packages
deb [arch=amd64] http://ubuntu.openvidu.io/7.3.0 $DISTRO kms6
EOF

sudo apt-get update ; sudo apt-get install kurento-media-server

```