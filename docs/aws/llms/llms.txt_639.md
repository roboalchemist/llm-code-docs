# Source: https://docs.aws.amazon.com/outposts/latest/install-server/llms.txt

# AWS Outposts Server installation guide

> AWS Outposts is a fully-managed service that extends AWS infrastructure, APIs, and tools to customer premises. When you order an AWS Outposts server, you are responsible for the installation. This guide contains the requirements and the steps to install the AWS Outposts server at your site.

- [Installing an AWS Outposts server](https://docs.aws.amazon.com/outposts/latest/install-server/install-server.html)
- [Step 1: Grant permissions](https://docs.aws.amazon.com/outposts/latest/install-server/install-grant.html)
- [Step 2: Inspect](https://docs.aws.amazon.com/outposts/latest/install-server/install-inspect.html)
- [Step 3: Rack mount](https://docs.aws.amazon.com/outposts/latest/install-server/install-mount.html)
- [Site requirements](https://docs.aws.amazon.com/outposts/latest/install-server/outposts-requirements.html)

## [Step 4: Power up](https://docs.aws.amazon.com/outposts/latest/install-server/install-power.html)

- [Attach NSK](https://docs.aws.amazon.com/outposts/latest/install-server/power-attach-nsk.html): You must attach the NSK to the server so it can decrypt data on the server during operation.
- [Power on](https://docs.aws.amazon.com/outposts/latest/install-server/power-on.html): Use the following procedures to connect your Outposts server to its power source and then verify that the server has powered on.
- [Check the NSK Power LED](https://docs.aws.amazon.com/outposts/latest/install-server/power-check-led.html): AWS Outposts supports two versions of NSK: Atlas 2.0 and Atlas 3.0.


## [Step 5: Connect your network](https://docs.aws.amazon.com/outposts/latest/install-server/install-network.html)

- [Configure QSFP network](https://docs.aws.amazon.com/outposts/latest/install-server/connect-2.html): With the QSFP breakout cable, you use breakouts to segment traffic.


## [Step 6: Configure connection and authorize](https://docs.aws.amazon.com/outposts/latest/install-server/install-authorize.html)

- [Connect your laptop](https://docs.aws.amazon.com/outposts/latest/install-server/authorize-1.html): Connect the USB cable to your laptop first and then to the server.
- [Create a serial connection](https://docs.aws.amazon.com/outposts/latest/install-server/authorize-2.html): The following are instructions to create a serial connection from your laptop to the Outposts server.
- [Configure and test the connection](https://docs.aws.amazon.com/outposts/latest/install-server/authorize-3.html): Use the following procedures to configure and test the connection between your server and AWS using the Outpost Configuration Tool.
- [Authorize the server](https://docs.aws.amazon.com/outposts/latest/install-server/authorize-4.html): Use the following procedure to authorize the server.
- [Verify the NSK LEDs](https://docs.aws.amazon.com/outposts/latest/install-server/authorize-5.html): After the provisioning process completes, check the NSK LEDs.


## [Command reference](https://docs.aws.amazon.com/outposts/latest/install-server/oct-reference.html)

- [clear-dns](https://docs.aws.amazon.com/outposts/latest/install-server/oct-clear-dns.html): The clear-dns command deletes the DNS (Domain Name Server) IP address.
- [clear-service-link-static-ip](https://docs.aws.amazon.com/outposts/latest/install-server/oct-clear-service-link-static-ip.html): The clear-service-link-static-ip command deletes the service link IP address.
- [describe-ip](https://docs.aws.amazon.com/outposts/latest/install-server/oct-describe-ip.html): The describe-ip command returns the IP assignment status and configuration of each connected link.
- [describe-links](https://docs.aws.amazon.com/outposts/latest/install-server/oct-describe-links.html): The describe-links command returns information about the network links on the server.
- [describe-reachability](https://docs.aws.amazon.com/outposts/latest/install-server/oct-describe-reachability.html): The describe-reachability command determines whether the Outposts server can reach the Outpost configuration endpoint in the Region.
- [describe-resolve](https://docs.aws.amazon.com/outposts/latest/install-server/oct-describe-resolve.html)
- [echo](https://docs.aws.amazon.com/outposts/latest/install-server/oct-echo.html): The echo command displays the value that you set for a variable using the command.
- [export](https://docs.aws.amazon.com/outposts/latest/install-server/oct-export.html): The export command sets IAM credentials as environment variables.
- [get-connection](https://docs.aws.amazon.com/outposts/latest/install-server/oct-get-connection.html): The get-connection command returns the status of the service link connection between the Outposts server and the Outpost service in the AWS Region for the Outposts server.
- [get-dns](https://docs.aws.amazon.com/outposts/latest/install-server/oct-get-dns.html): The get-dns command returns the DNS (Domain Name Server) IP address.
- [get-service-link-static-ip](https://docs.aws.amazon.com/outposts/latest/install-server/oct-get-service-link-static-ip.html): The get-service-link-static-ip command, when used after you set the static configuration for the service link with the set-service-link-static-ip command, returns the service link static configuration values.
- [reboot](https://docs.aws.amazon.com/outposts/latest/install-server/oct-reboot.html): The reboot command reboots the Outposts server.
- [set-dns](https://docs.aws.amazon.com/outposts/latest/install-server/oct-set-dns.html): The set-dns command sets the DNS (Domain Name Server) IP address.
- [set-service-link-static-ip](https://docs.aws.amazon.com/outposts/latest/install-server/oct-set-service-link-static-ip.html): The set-service-link-static-ip command sets the static configuration for the service link.
- [start-connection](https://docs.aws.amazon.com/outposts/latest/install-server/oct-start-connection.html): The start-connection command initiates a connection with the Outpost service in the Region for the Outposts server.
