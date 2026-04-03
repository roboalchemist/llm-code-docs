# Access and security overview -

Source: https://docs.lambda.ai/public-cloud/access-security/

---

[identity and access management ](../../tags/#tag:identity-and-access-management)[security and compliance ](../../tags/#tag:security-and-compliance)
# Access and security [# ](#access-and-security)

This page describes Lambda Cloud's access management and security features. 

## Access management [# ](#access-management)

Lambda provides lightweight access management mechanisms to ensure secure access while minimizing friction. 

### API keys [# ](#api-keys)

The Lambda Cloud API uses API keys to authenticate incoming requests. You can generate a new API key pair or view your existing API keys by visiting the [API keys page ](http://cloud.lambda.ai/api-keys)in the Lambda Cloud console. API keys have full access to all Lambda API operations. 

### SSH keys [# ](#ssh-keys)

Before you launch an instance, you must add an SSH key to your Lambda Cloud account. When you go through the process of launching an instance, you'll be prompted to supply this SSH key so you can securely connect to the instance after launching. You can import an existing key if you have one, or you can generate a new one in the Lambda Cloud console. 

For guidance on setting up an SSH key, see [Connecting to an instance > Setting up SSH access ](../on-demand/connecting-instance/#setting-up-ssh-access). 

### Teams [# ](#teams)

You can add new members to your Lambda account by inviting them to join your *Team *. Each Team member can be either an *Admin *or a *Member *: 

- Both roles have full access to your Lambda resources. Each can create API keys, launch and terminate instances, and retrieve audit logs, for example. 
- Admins can also invite or remove Team members, modify the project's payment information, and rename the team. 
The invitee's email address must not already be associated with an existing Lambda account. If your team member already has a Lambda account, ask them to provide a different address or, if feasible, to close their existing account. 

For details on creating and updating Teams, see [Teams ](../teams/). 

Important 

**Each role has full access to your Lambda resources. **Make sure to invite only trusted persons to your Team.
