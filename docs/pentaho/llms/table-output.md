# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/table-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/table-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/table-output.md

# Table Output

The Table Output step loads data into a database table. The Table Output step is equivalent to the SQL operator `INSERT` and is a solution when you only need to insert records. If you just want to update rows, you should use the [Update](https://pentaho-community.atlassian.net/wiki/spaces/EAI/pages/371558127/Update) step. To perform both `INSERT` and `UPDATE` commands, see the [Insert/Update](https://pentaho-community.atlassian.net/wiki/spaces/EAI/pages/371558126/Insert+-+Update) step.

This step provides configuration options for a target table and performance-related options such as **Commit size** and **Use batch update for inserts**. There are performance settings specific to a database type that can be set within the database connection JDBC properties. Refer to your database documentation for specific JDBC performance settings. See also [Special database issues and experiences](https://pentaho-community.atlassian.net/wiki/spaces/EAI/pages/365396524/Special+database+issues+and+experiences).

**Note:** If you insert a record into a database table that has identity columns, the JDBC driver returns the auto-generated key it uses when performing the insert. This is not supported on all database types.
