# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-server-issues/library-conflicts.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-server-issues/library-conflicts.md

# Library conflicts

The Pentaho Server relies on many third-party libraries. These libraries provide everything from database connectivity to specific Java classes. If you have incompatible versions of any of these third-party libraries in your application server's global `lib` folder, they can cause a variety of problems related to starting and running the Pentaho Server.

Determine what versions are correct based on your needs for these third-party libraries. Some known-problematic JARs are:

* `commons-collections-3.2.jar` (from Pentaho)
* `jettison-1.01.jar` (from Pentaho)
