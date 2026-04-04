# Source: https://io.net/docs/guides/architecture/io-tunnels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# IO Tunnels

> Reverse tunnels technology provides a way to bypass firewall and NAT restrictions, enabling secure access to remote resources. This article discusses the concept of reverse tunnels, how they work, and how io.net uses them to simplify engineer access to AntMiners Clusters.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6923016-1_2.png?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=4723597bc74686bdf9ea469532b8c82c" alt="" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/docs/6923016-1_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6923016-1_2.png?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=335369df63b564d3b43e98da787c85cc 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6923016-1_2.png?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=5d45cca366d8b48e6b670091a0826e51 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6923016-1_2.png?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=599f61dd7f8800c02a986fbb8436eb9f 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6923016-1_2.png?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=3b351bd37e7543b8790abc0fd7e3c0bf 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6923016-1_2.png?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=2ca9d972928f39f3677a1d8fd28c5a03 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6923016-1_2.png?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=18c14441340bac2e149d775e5a17f6ab 2500w" />
</Frame>

### Understanding Reverse Tunnels

A *Reverse tunnel* is a method to establish a secure connection from a client to a remote server by opening an inbound connection on the server side. This is the opposite of a conventional forward tunnel, where a client opens a connection to the server. By using reverse tunnels, engineers can access remote resources behind NAT routers and firewalls without the need for complex network configurations.

### How Reverse Tunnels Work

1. The remote server (IO Worker) initiates a connection to the client (engineer's machine) through an intermediate server (io.net server).
2. The io.net server listens for incoming connections from both the client and the remote server. Once the connection is established, data can be exchanged between the client and the remote server through the tunnel as if they were directly connected.

The io.net network employs reverse tunnels to simplify access to io.net miners for engineers.

The process involves:

1. The IO Worker establishes a connection to the io.net server, creating a reverse tunnel.
2. The engineer's machine connects to the io.net server as an intermediary.
3. The io.net server routes traffic between the engineer's machine and the IO Worker through the reverse tunnel. Engineers can securely access and manage IO Workers without the need for complex network configurations or dealing with firewalls and NAT restrictions.

### Benefits of Reverse Tunnels

1. **Simplified Access**: Engineers can easily access IO Workers without worrying about network restrictions, port forwarding, or VPNs.
2. **Enhanced Security**: Reverse tunnels provide a secure communication channel, ensuring data privacy and integrity.
3. **Scalability**: io.net can manage multiple IO Workers simultaneously, allowing engineers to work efficiently.
4. **Flexibility**: Reverse tunnels work across various platforms, ensuring compatibility with different operating systems and environments.
