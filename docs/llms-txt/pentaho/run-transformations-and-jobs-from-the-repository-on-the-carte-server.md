# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/run-transformations-and-jobs-from-the-repository-on-the-carte-server.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/run-transformations-and-jobs-from-the-repository-on-the-carte-server.md

# Run Transformations and Jobs from the Repository on the Carte Server

To run a job or transformation remotely on a Carte server, you first need to copy the local `repositories.xml` from the user's `.kettle` directory to the Carte server's `$HOME/.kettle` directory. The Carte service also looks for the `repositories.xml` file in the directory from which Carte was started.

For more information about locating or changing the .`.kettle` home directory, see the **Administer Pentaho Data Integration and Analytics** document.
