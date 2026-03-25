# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-repository-issues/unable-to-get-list-of-repositories.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-repository-issues/unable-to-get-list-of-repositories.md

# Unable to get list of repositories

When you are working with a repository and trying to execute a job or transformation remotely on a Carte server, the following error message may appear:

```
There was an error posting the transformation on the remote server:
   org.pentaho.di.core.exception.KettleException:
   Unable to get a list of repositories to locate repository 'repo'
```

To execute a job or transformation remotely on a Carte server, you first need to copy the local `repositories.xml` from the user's `.kettle` directory to the Carte server's `$HOME/.kettle` directory. The Carte service also looks for the `repositories.xml` file in the directory where Carte was started.
