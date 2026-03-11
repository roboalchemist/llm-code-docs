# Source: https://help.aikido.dev/virtual-machine-scanning/misc/virtual-machine-reachability-analysis.md

# Virtual Machine Reachability Analysis

Virtual Machine Reachability Analysis shows how a VM can be reached inside your cloud network. It builds an interactive diagram of the network path to an instance (for example: Internet → Load Balancer → VM), including the ports involved, so you can quickly spot unintended exposure.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FYdtsDt16c6PhJ1lZ8P71%2FScreenshot%202026-03-03%20at%2015.19.39.png?alt=media&#x26;token=89547012-ae7e-4148-9bcb-3dde50d04ed1" alt=""><figcaption></figcaption></figure>

## What it helps you do

* Confirm public exposure: See if a VM is reachable from the internet, and through which components.
* Understand the path: Visualize the exact route traffic can take (load balancers, network hops), not just a single “public/private” label.
* Reduce risk faster: Identify surprising entry points and tighten access where needed.

## Where to find it

In [Virtual Machines](https://app.aikido.dev/virtual-machines), hover over your VM and select View Virtual Machine Reachability. This opens the reachability diagram view for that instance.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FYX38Xd4FkqBP2kBDrVN4%2FScreenshot%202026-03-03%20at%2015.25.01.png?alt=media&#x26;token=03758f44-635c-4106-ad2e-cf39df512f77" alt=""><figcaption></figcaption></figure>
