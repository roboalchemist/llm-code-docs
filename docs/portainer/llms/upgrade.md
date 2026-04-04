# Source: https://docs.portainer.io/2.33-lts/start/upgrade.md

# Source: https://docs.portainer.io/sts/start/upgrade.md

# Source: https://docs.portainer.io/start/upgrade.md

# Updating Portainer

Portainer releases contain new features and bug fixes so it's important to keep your installation up to date. We have [tested and validated](https://docs.portainer.io/requirements-and-prerequisites#valid-configurations) all Portainer version upgrades from 2.0.0 up to the latest release.

While it's possible that an untested unvalidated update path might work, we recommend that all update paths are tested and validated on a non-critical system before applying them to your production systems.

{% hint style="info" %}
We added a [backup and restore feature](https://docs.portainer.io/admin/settings#backup-portainer) to Portainer BE 2.7 and strongly recommend that you take a backup of your Portainer instance before updating.
{% endhint %}

{% hint style="info" %}
Starting with CE 2.9 and BE 2.10 Portainer is HTTPS enabled by default and uses port `9443` to serve the UI. HTTP can still be enabled on port `9000` if required.
{% endhint %}

## Update order

In general, we recommend updating your Portainer Server deployment *before* you update the Portainer Agents. When we release new versions of Portainer we ensure that Portainer Server is able to talk to older versions of the Agent, and in most cases the reverse is true, but in some instances we make changes to the Agent that are not fully backward compatible with older versions of Portainer Server.

## Updating Portainer

### From within Portainer

{% hint style="warning" %}
Updating from within Portainer to STS versions (or within STS versions) is currently not available. Only LTS versions will be offered through the in-app update. To switch to or update to STS versions, follow the [manual instructions](#manually-update-portainer) below.
{% endhint %}

From 2.19, Business Edition users are able to update their Portainer installation directly from within Portainer. To do so, click the **Update now** link in the update notification in the bottom left of the Portainer UI.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/BiAodOBcqOcpgv9wynd0/2.19-update-notification.png" alt=""><figcaption></figcaption></figure>

In the confirmation dialog, click **Start update** to proceed with the update.

{% hint style="warning" %}
Remember to [back up your Portainer installation](https://docs.portainer.io/admin/settings#backup-portainer) before updating!
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/dGCoQWhdKjTUkOmPcqLP/2.19-update-confirmation.png" alt=""><figcaption></figcaption></figure>

### Manually update Portainer

If you would prefer to manually update your Portainer installation, choose your platform then follow the instructions:

{% content-ref url="upgrade/docker" %}
[docker](https://docs.portainer.io/start/upgrade/docker)
{% endcontent-ref %}

{% content-ref url="upgrade/swarm" %}
[swarm](https://docs.portainer.io/start/upgrade/swarm)
{% endcontent-ref %}

{% content-ref url="upgrade/podman" %}
[podman](https://docs.portainer.io/start/upgrade/podman)
{% endcontent-ref %}

{% content-ref url="upgrade/kubernetes" %}
[kubernetes](https://docs.portainer.io/start/upgrade/kubernetes)
{% endcontent-ref %}

### Update the Portainer Agent

To update the standard (non-Edge) Portainer Agent, you can find instructions in the above platform-specific links ([Docker Standalone](https://docs.portainer.io/start/docker#agent-only-upgrade), [Docker Swarm](https://docs.portainer.io/start/upgrade/swarm), [Podman](https://docs.portainer.io/start/upgrade/podman) and [Kubernetes](https://docs.portainer.io/start/upgrade/kubernetes)).

If you are using the Portainer Edge Agent, we have specific update instructions for you:

{% content-ref url="upgrade/edge" %}
[edge](https://docs.portainer.io/start/upgrade/edge)
{% endcontent-ref %}

### Upgrading to Business Edition

If you are coming from Portainer CE or the 1.24.x branch, we have guides for you as well.

{% content-ref url="upgrade/tobe" %}
[tobe](https://docs.portainer.io/start/upgrade/tobe)
{% endcontent-ref %}
