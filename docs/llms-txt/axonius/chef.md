# Source: https://docs.axonius.com/docs/chef.md

# Chef

Chef provides continuous automation for building, deploying, and managing infrastructure, compliance, and applications in modern, legacy, and hybrid environments.

## Adapter Parameters

1. **Chef Domain** *(required)* - The hostname of the Chef server.

2. **Organization** *(required)* -  The name of your organization as it appears in Chef.

3. **Client** and **Client Key File (pem)** *(required)* -  Axonius uses the **username** and the **key file** of a Chef user for authorization. See below instructions.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

<Image alt="Chef.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Chef.png" />

## Creating a User in Chef for Axonius Usage

There are 2 options for creating a User:

* Create a user through **Chef Manage (Chef Web UI)**. Follow the steps [here](https://docs.chef.io/server_users.html#chef-manage) to create this user and retrieve its key file.
* Create a user through the **command line**. Follow the steps [here](https://docs.chef.io/server/server_users/#chef-manage) to create the user and generate the client key file. Keep the key file in a safe place.