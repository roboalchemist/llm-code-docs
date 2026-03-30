# Source: https://docs.portainer.io/2.33-lts/admin/environments/groups.md

# Source: https://docs.portainer.io/2.33-lts/user/edge/groups.md

# Source: https://docs.portainer.io/sts/admin/environments/groups.md

# Source: https://docs.portainer.io/sts/user/edge/groups.md

# Source: https://docs.portainer.io/admin/environments/groups.md

# Source: https://docs.portainer.io/user/edge/groups.md

# Edge Groups

The Edge Groups feature lets you group together Edge environments either by manually selecting them or based on their [tags](https://docs.portainer.io/admin/environments/tags). This is useful if you manage multiple Edge environments in multiple zones.

{% hint style="info" %}
This functionality requires you to [enable Edge Compute](https://docs.portainer.io/admin/settings/edge) features.
{% endhint %}

From the menu select **Edge Groups** then click **Add Edge group**.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/yAL4oVPjwhS3VvW0ZdkZ/2.15-edge-groups.gif" alt=""><figcaption></figcaption></figure>

Give the group a descriptive name then select either **Static** or **Dynamic**:

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/FWm91gX1ntdI7HWbn8QO/2.15-edge-groups-name.png" alt=""><figcaption></figcaption></figure>

### **Option 1: Static**

This option lets you manually add environments to the group from a list. Select the required environments then click **Add edge group**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/3keIZ1Ta66jdy8VgkYSB/2.15-edge-groups-static.png" alt=""><figcaption></figcaption></figure>

### Option 2: Dynamic

This option lets you automatically associate environments via their tags. If you choose this option you will need to refine how Edge environments are dynamically associated.

| Option        | Overview                                                                                                              |
| ------------- | --------------------------------------------------------------------------------------------------------------------- |
| Partial Match | Will associate any environments matching at least one of the selected tags (environments can have more than one tag). |
| Full Match    | Will associate any environments matching all of the selected tags.                                                    |

When you select a tag from the dropdown, environments with that tag will appear in the results.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Wk0fTg9LG5ogt29kGHCI/2.15-edge-groups-dynamic.png" alt=""><figcaption></figcaption></figure>

Click **Add edge group** to associate the environments to the group.
