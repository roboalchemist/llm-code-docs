# Source: https://docs.portainer.io/2.33-lts/faqs/installing/how-can-i-ensure-portainers-configuration-is-retained.md

# Source: https://docs.portainer.io/sts/faqs/installing/how-can-i-ensure-portainers-configuration-is-retained.md

# Source: https://docs.portainer.io/faqs/installing/how-can-i-ensure-portainers-configuration-is-retained.md

# How can I ensure Portainer's configuration is retained?

#### Docker Standalone

The commands in our [installation guide](https://docs.portainer.io/start/install/server) include the creation of a portainer\_data volume for Portainer to store data, and using this will ensure that the configuration remains even when the Portainer container is restarted, upgraded or removed.

#### Docker Swarm&#x20;

Our [recommended deployment](https://docs.portainer.io/start/install/server/swarm) stack file constrains Portainer to a manager node, which will work well if you have a single manager node. If you have multiple managers however this will potentially become a problem. Each stack or service update action could move the Portainer container between manager nodes, and you may see Portainer appear as a fresh install. One solution is to constrain your Portainer container to the node where your Portainer data is being persisted. To do this, you will first need to find the hostname of the node where the Portainer volume is being persisted. Within Portainer, from the menu select **Volumes** and note down the value in the **Host** column for your Portainer volume (usually called portainer\_portainer\_data). In the below example, this is ce-manager01.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/sJzlUhsZsjkldPzzAUdn/2.9-swarm-portainer-volume-constrain-1.gif" alt=""><figcaption></figcaption></figure>

Next, from the menu select **Services** then the portainer\_portainer service, then click **Placement constraints**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/091vu8MgXsD3CDegXSeH/2.9-swarm-portainer-volume-constraints-2.gif" alt=""><figcaption></figcaption></figure>

Click the **placement constraint** button to add a new constraint. Enter node.hostname for the **Name** and the hostname you gathered previously for the **Value**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Hv745p3Bf1PkyvrSBFLG/image.png" alt=""><figcaption></figcaption></figure>

#### Kubernetes

For Kubernetes environments we recommend using a default StorageClass with cluster-available storage to avoid issues. Alternatively you can use a nodeSelector with your deployment to restrict the Portainer instance to a chosen node. This method is described in more detail in our [Kubernetes installation guide.](https://docs.portainer.io/start/install/server/kubernetes/baremetal)
