# Source: https://northflank.com/docs/v1/application/network/enable-multi-project-networking.md

# Enable multi-project networking

Projects on Northflank are, by default, self-contained, secure networks. Other than by [publicly exposing](configure-ports#public-ports) or [securely forwarding](https://northflank.com/docs/v1/api/forwarding) a service or addon, resources in your project remain accessible only to other resources within the same project.

You can, however, configure projects to securely allow ingress network traffic from other projects, without publicly exposing them to the internet. This allows your services access to resources in other projects that would normally be inaccessible, for example to query a database or access an API that you do not want to expose to the public internet.

## Allow ingress from other projects

You can configure which projects are allowed network ingress on the [project's settings page](https://app.northflank.com/s/project/settings).

You can only allow ingress for projects which are in the same team, and deployed on the same cluster. For example, you cannot enable ingress to a project hosted on Northflank's managed cloud from a [project hosted on another provider](https://northflank.com/docs/v1/application/bring-your-own-cloud/use-other-cloud-providers-with-northflank).

Select the projects you want to allow access to the project you are configuring. Enabling ingress for a project is one-way, and does not also enable egress. To access to resources across both, or multiple, projects, you will need to allow ingress in each project respectively. See the table below for an example.

| Project | Ingress projects | Can access |
| --- | --- | --- |
| A | B, C | - |
| B | C | A |
| C | - | A, B |

To disable access, simply remove the projects from the ingress projects list.

![Allowing ingress networking from another project in the Northflank application](https://assets.northflank.com/documentation/v1/application/network/enable-multi-project-networking/multi-project-networking.png)

## Access resources from other projects

### Access services

When you allow ingress to a project, ports on combined and deployment services in the project will be assigned a new address listed under `ingress projects`. These addresses will only allow access from the projects specified in the network ingress settings.

![Multi-project network addresses in the Northflank application](https://assets.northflank.com/documentation/v1/application/network/enable-multi-project-networking/project-network-dns.png)

### Access addons

You can use the same connection details to access addons from other projects as you do to access the addon from within the same project.

## Next steps

- [Network security: Set IP policies and add basic authentication to your deployments.](/v1/application/network/networking-on-northflank)
- [Add private ports: Configure ports to allow your services to communicate securely within your project.](/v1/application/network/configure-ports#private-ports)
- [Forward deployments and databases: Forward deployments and databases to your local machine for development.](/v1/api/forwarding)
- [Configure basic authentication: Require users to enter a username and password to access your site.](/v1/application/network/add-security-policies-for-ports#require-credentials)
