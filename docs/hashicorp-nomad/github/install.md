# Install

Source: https://developer.hashicorp.com/nomad/docs/install

Install Nomad
1.11.3 (latest)
1.11.2
1.11.1
1.11.0
1.10.5
1.10.4
1.10.3
1.10.2
1.10.1
1.10.0
1.9.7
1.9.6
1.9.5
1.9.4
1.9.3
1.9.1
1.9.0
1.8.4
1.8.3
1.8.2
1.8.1
1.8.0
1.7.7
1.7.6
1.7.5
1.7.4
1.7.3
1.7.2
1.7.1
1.7.0
1.6.10
1.6.9
1.6.8
1.6.7
1.6.6
1.6.5
1.6.4
1.6.3
1.6.2
1.6.1
1.6.0
1.5.17
1.5.16
1.5.15
1.5.14
1.5.13
1.5.12
1.5.11
1.5.10
1.5.9
1.5.8
1.5.7
1.5.6
1.5.5
1.5.4
1.5.3
1.5.2
1.5.1
1.5.0
1.4.14
1.4.13
1.4.12
1.4.11
1.4.10
1.4.9
1.4.8
1.4.7
1.4.6
1.4.5
1.4.4
1.4.3
1.4.2
1.4.1
1.4.0
1.3.16
1.3.15
1.3.14
1.3.13
1.3.12
1.3.11
1.3.10
1.3.9
1.3.8
1.3.7
1.3.6
1.3.5
1.3.4
1.3.3
1.3.2
1.3.1
1.3.0
1.2.16
1.2.15
1.2.14
1.2.13
1.2.12
1.2.11
1.2.10
1.2.9
1.2.8
1.2.7
1.2.6
1.2.5
1.2.4
1.2.3
1.2.2
1.2.1
1.2.0
1.1.18
1.1.17
1.1.16
1.1.15
1.1.14
1.1.13
1.1.12
1.1.11
1.1.10
1.1.9
1.1.8
1.1.7
1.1.6
1.1.5
1.1.4
1.1.3
1.1.2
1.1.1
1.1.0
1.0.18
1.0.17
1.0.16
1.0.15
1.0.14
1.0.13
1.0.12
1.0.11
1.0.10
1.0.9
1.0.8
1.0.7
1.0.6
1.0.5
1.0.4
1.0.3
1.0.2
1.0.1
1.0.0
0.12.12
0.12.11
0.12.10
0.12.9
0.12.8
0.12.7
0.12.6
0.12.5
0.12.4
0.12.3
0.12.2
0.12.1
0.12.0
0.11.8
0.11.7
0.11.6
0.11.5
0.11.4
0.11.3
0.11.2
0.11.1
0.11.0
0.10.9
0.10.8
0.10.7
0.10.6
0.10.5
0.10.4
0.10.3
0.10.2
0.10.1
0.10.0
0.9.7
0.9.6
0.9.5
0.9.4
0.9.3
0.9.2
0.9.1
0.9.0
0.8.7
0.8.6
0.8.5
0.8.4
0.8.3
0.8.2
0.8.1
0.8.0
0.7.1
0.7.0
0.6.3
0.6.2
0.6.1
0.6.0
0.5.6
0.5.5
0.5.4
0.5.3
0.5.2
0.5.1
0.5.0
0.4.1
0.4.0
0.3.2
0.3.1
0.3.0
0.2.3
0.2.2
0.2.1
0.2.0
0.1.2
0.1.1
0.1.0
macOS
Package manager
brew tap hashicorp/tap
brew
install
hashicorp/tap/nomad
Binary download
AMD64
Version: 1.11.3
Download
ARM64
Version: 1.11.3
Download
Windows
Binary download
AMD64
Version: 1.11.3
Download
Linux
Package manager
Ubuntu/Debian
CentOS/RHEL
Fedora 41
Fedora 42
Amazon Linux
Homebrew
wget
-O - https://apt.releases.hashicorp.com/gpg
|
sudo
gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo
"deb [arch=
$(
dpkg --print-architecture
)
signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com
$(
grep
-oP
'(?<=UBUNTU_CODENAME=).*'
/etc/os-release
||
lsb_release -cs
)
main"
|
sudo
tee
/etc/apt/sources.list.d/hashicorp.list
sudo
apt
update
&&
sudo
apt
install
nomad
sudo
yum
install
-y yum-utils
sudo
yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo
yum -y
install
nomad
sudo
dnf
install
-y dnf-plugins-core
sudo
dnf config-manager addrepo --from-repofile
=
https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
sudo
dnf -y
install
nomad
wget
-O- https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
|
sudo
tee
/etc/yum.repos.d/hashicorp.repo
sudo
yum list available
|
grep
hashicorp
sudo
dnf -y
install
nomad
sudo
yum
install
-y yum-utils shadow-utils
sudo
yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo
yum
install
nomad
brew tap hashicorp/tap
brew
install
hashicorp/tap/nomad
Binary download
AMD64
Version: 1.11.3
Download
ARM64
Version: 1.11.3
Download
Note
Complete this
tutorial
to learn how to install and verify HashiCorp tools on any Linux distribution, and create a custom Linux container with verified HashiCorp tools.
Release information
Changelog
Nomad Version: 1.11.3
GitHub
(opens in new tab)
Official releases
All officially supported HashiCorp release channels and their security guarantees.
View all
(opens in new tab)
Note
You can find the
SHA256 checksums for
Nomad
1.11.3
online and you can
verify the checksums signature file
which has been signed using
HashiCorp's GPG key
. Complete this
tutorial
to learn how to install and verify HashiCorp tools on any Linux distribution.
Next steps
12min
Install a HashiCorp Enterprise license
Add an Enterprise license to Vault, Consul, Nomad, or Boundary with environment variables, a license file, or a configuration value.
Consul
Nomad
Vault
Boundary
6min
Introduction to Nomad
Discover what HashiCorp Nomad is, become familiar with important related terms, and understand how Nomad fits into the application development workflow.
Nomad
Video
30min
Set up a Nomad cluster on AWS
Create a Nomad cluster with Consul on AWS and then enable ACLs. Use this cluster as a starting point for your Nomad workloads.
Nomad
Packer
Terraform
25min
Schedule edge Services with native service discovery
Schedule a demo application on the edge, use Nomad's native service discovery to connect edge services, and simulate unstable edge connections to learn how Nomad gracefully handles disconnected clients.
Nomad
Terraform
Packer
12min
Secure Nomad jobs with Consul service mesh
Configure Nomad for an ACL-enabled Consul cluster and run a sample job that uses Consul service mesh.
Consul
Nomad
10min
Migrate a monolith to microservices
Migrate a monolithic application to microservices using Consul and Nomad.
Nomad
Consul