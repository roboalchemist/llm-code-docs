# Source: https://docs.verda.com/clusters/instant-clusters/deploying-your-cluster.md

# Deploying an Instant Cluster

## Deploying an instant cluster

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-e402ab263434e139175bc12aad23bf07a994eead%2Fcluster.png?alt=media" alt=""><figcaption></figcaption></figure>

Deploy an instant cluster by clicking the **Deploy Cluster** button on the top right of the **Clusters** page. In the next screen, you can choose your contract duration (starting from 1 day) and the number of GPUs (depending on the available resources) you would like to have in your cluster.

Select the operating system and CUDA version you want to use (we recommend CUDA 13.0):

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-692515d0c3d1ef3a336a2ac552d3e2dfa739ae1b%2Fcluster%20os.png?alt=media" alt=""><figcaption></figcaption></figure>

Next, select your shared filesystem size. File systems are mounted as follows:

* Local storage is mounted to `/mnt/local_disk` on each worker node.
* SFS is mounted to `/home` on all nodes, including the jump host.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-44dc1624f5b89e97b8f4ed0c2691e1843a9fae78%2Fcluster%20storage.png?alt=media" alt=""><figcaption></figcaption></figure>

You also need to supply your SSH public key before you deploy. We recommend you choose the cluster hostname appropriately, since your worker nodes will inherit the hostname as the prefix.

Once the above steps are done, you deploy the cluster, just like you would an [ordinary Verda cloud instance](https://docs.verda.com/cpu-and-gpu-instances/set-up-a-gpu-instance).

## Accessing your cluster

Once deployment has been done, please give the cluster around 20 minutes to start.

Please also note that the jump host node will become accessible a few minutes before the worker nodes are ready, when starting the cluster for the first time.

{% hint style="info" %}
The default Linux user for your on-demand cluster is `ubuntu`
{% endhint %}

Once the cluster has been created, you can proceed to log in by copying the `ssh ubuntu@CLUSTER_IP` command from the **Clusters** screen in the console.

You can login to the individual worker nodes from your jumphost by running `ssh WORKER_NAME`

{% hint style="info" %}
You can use tab-completion with SSH to quickly login to your worker nodes
{% endhint %}

## Running jobs

We recommend using [Slurm](https://docs.verda.com/clusters/instant-clusters/slurm) to run jobs on the cluster.
