# Source: https://docs.sandboxes.cloud/docs/frequently-asked-questions.md

# Frequently Asked Questions

### Who can access my sandbox/workspace? Can I access my teammate’s sandbox/workspace?

Sandbox/workspace is accessible to all team members in the same organization. We optimize for convenience and promotes transparency within the team. To access a teammate’s sandbox, it's very similar to accessing the user's own sandbox, i.e., a user can:

* Use Web Console, find the sandbox from [Sandboxes page](https://sandboxes.cloud/sandboxes) and access it
* Use Command Line tool, `cs sandbox` related commands for all sandboxes in the Organization

### Who can access the endpoints of sandboxes?

By default, the exposed endpoints of sandboxes are protected by same login. So the User from an Organization need to login the same way to access the endpoints. However, recognizing that many API endpoints supports its own authentication mechanism, we allow users to specify the endpoints to be `Public` and only rely on the App's own login mechanism just like in production environment. Making endpoints `Public` is also helpful for demoing the App to external people.

### Will sandbox be automatically recycled? Will my code / data lost in sandbox?

Sandbox is designed to support permanent usage. To save resources, it can be `suspended`. Even when suspended, its configuration and disk volume will still be kept so that it can be `resumed` for operation. So as long as modification is saved to sandbox mounted disk volume, it will not be lost. Same goes for the persisted data in dependency services such as MySQL.

However, a user can delete a sandbox when it’s no longer useful. In such case, all the data local to the sandbox will be destroyed. We recommend to backup the work often to git repo hosted by vendors.

### Should I use one or multiple sandbox?

Our recommendation is to use one sandbox for one purpose to make best use of it.  You should not feel the need to limit yourself to only one sandbox and keep multiple context in it, although using one main sandbox for most active development need can provide more convenience in customizing it to your preference.