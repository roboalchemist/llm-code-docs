# Source: https://docs.verda.com/clusters/instant-clusters/good-to-know-1.md

# Local Users

### Local Cluster Users

When deploying a cluster with an OS image labeled beta, the environment includes a dedicated virtual machine running an identity management platform called [Kanidm](https://kanidm.com/). This allows you to manage local users, groups and SSH keys centrally across the cluster.

> To get that OS image enabled for your user, please contact support.

### Setup details

The identity management service is reacahable on address `auth.cluster.verda.internal` from within the cluster.

It runs inside a docker container called `kanidm` and the service node has the `kanidm` CLI tool installed that you will use to manage:

* Groups
* Local users with or without root access
* SSH public keys per user

Important Note on Groups: If you use the suggested group name `cluster_users`, members are automatically added to the `docker` group on the nodes. If you choose a different group name, you must manually update the `kanidm-unixd` and `sshd` [configurations](https://kanidm.github.io/kanidm/stable/integrations/pam_and_nsswitch.html?highlight=unixd#the-unix-daemon) on your jumphost and worker nodes.

### Groups and User Creation

Login to the service node by using the jumphost as an SSH jumphost:

```bash
ssh -J ubuntu@public.ip.to.jumphost root@auth.cluster.verda.internal
```

Recover the initial password for user `idm_admin`:

```bash
docker exec -i -t kanidm kanidmd recover-account idm_admin
```

Initialize the kanidm CLI using the password found in the above recover-account:

```bash
# kanidm login --name idm_admin
Enter password: [hidden]
Login Success for idm_admin@auth.cluster.verda.internal
```

Create groups with GIDs [great than 65536](https://kanidm.github.io/kanidm/stable/accounts/posix_accounts_and_groups.html#gid-number-generation):

```bash
kanidm group create cluster_users
kanidm group posix set cluster_users --gidnumber 70000
# kanidm group create cluster_admins
# kanidm group posix set cluster_admins --gidnumber 70001
```

Creating an example user and add it to the `cluster_users` group:

```bash
kanidm person create jsmith1 "John Smith"
kanidm person posix set jsmith1 --shell /bin/bash
kanidm person posix set jsmith1 --gidnumber 76001
kanidm group add-members cluster_users jsmith1

kanidm person ssh add-publickey jsmith1 'jsmith_key_1' "ssh-rsa AAA..."

kanidm person posix show jsmith1
```

### Accessing the Cluster

One configured, users can login to the jumphost directly:

`ssh jsmith1@public.ip.to.jumphost`

### Internal SSH & Node Access

* **Home Directories**: These are stored on a shared NFS mount and are available across all nodes.
* **SSH Agent Forwarding**: For security reasons, we recommend leaving agent forwarding disabled.
* **Internal Keys:** To allow your user to SSH from the jumphost to worker nodes, generate an internal key pair:

```bash
ssh jsmith1@public.ip.to.jumphost
ssh-keygen -t ssh-rsa
cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
```

To avoid "Host Verification" prompts when moving between nodes, update your `known_hosts` file:

```bash
for host in $(grep datacrunch.io /etc/hosts | awk '{print $2}'); do
  ssh-keyscan -H $host >> $HOME/.ssh/known_hosts
done
```

### Elevated Privileges

If you wish to grant sudo access to the `cluster_admins` group across the compute nodes, run the following command from the **jumphost**:

```bash
pdsh -g compute_node 'sudo bash -c "echo \"%cluster_admins ALL=(ALL:ALL) NOPASSWD: ALL\" > /etc/sudoers.d/cluster_admins"'
```
