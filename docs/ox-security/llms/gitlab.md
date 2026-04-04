# Source: https://docs.ox.security/get-started/onboarding-to-ox/source-control/gitlab.md

# GitLab

GitLab is a web-based DevOps lifecycle tool that provides a Git repository manager providing wiki, issue-tracking, and continuous integration and deployment pipeline features.

Connecting your GitLab allows OX to map your apps and scan them for security issues.

### GitLab server

* **gitlab.com** - if you are using the public SaaS GitLab server, you can use either an "Identity provider" or "Token" login. The Token option has the address of the SaaS server by default.
* **GitLab Enterprise** - if you are using a private GitLab installation, use the "Token" login and provide the GitLab server URL on the "Token" login tab.

### Connection options

* **Identity Provider** - just click “Connect” under the “Identity Provider” tab and follow the instructions on the screen.

![GitLab connector](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-feec73edb17c0160720665af8702db81ba356c9c%2Fimage.png?alt=media)

{% file src="<https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8aab6a6065c018fc22dfb2d52bb3801549d8a7ae%2FGitLab%20Connector%20-%20Identity%20Provider.mp4?alt=media>" %}
GitLab Connector - Onboarding using Identity Provider - Video
{% endfile %}

* **Token** - Create a token in GitLab with the permissions (scopes) mentioned below, copy the token into the token field and click “Connect.”

![Token](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6c267b6fda6f826821b58b6008b65850c64013d6%2Fimage%20\(6\).png?alt=media)

### Token scopes required

* api
* read\_user
* read\_registry

![Token scopes](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c93965f5fdc6825d34237bf8cb1aca578ea1e804%2Fimage%20\(5\).png?alt=media)

Once you have verified GitLab connectivity, you can see all the repositories and select them for scanning.

### Setting repositories' scope

You can use the "Gear" icon to choose the repositories' scope OX will cover. Only repositories chosen here will be covered and scanned.

Here you can also decide what will happen by default with newly discovered repositories.

{% file src="<https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-de5aba894fd0bd66c32ff96810bcb76abaaff8f8%2FGitLab%20Connector%20-%20Token.mp4?alt=media>" %}
GitLab Connector - Onboarding using a Token - Video
{% endfile %}
