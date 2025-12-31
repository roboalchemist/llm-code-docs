# Source: https://firebase.google.com/docs/data-connect/manage-services-and-databases.md.txt

<br />

YourData Connectprojects consist of two major infrastructure elements:

- One or moreData Connectservice instances
- One or more Cloud SQL for PostgreSQL instances

This guide discusses how to set up and manage yourData Connectservice instances, and introduces how to manage your associated Cloud SQL instances.

## Configure regions forFirebase Data Connect

Projects that useData Connectrequire a location setting.

When you create a newData Connectservice instance, you're prompted to select the location of the service.
| **Note:** The locations of yourData Connectservices don't affect the options for locations needed for other Firebase products you might have in your project, like your defaultCloud Firestorelocation.

### Available locations

Data Connectservices can be created in the following[regions](https://cloud.google.com/docs/geography-and-regions).
| **Note:** Cloud SQL for PostgreSQL instances must be provisioned in the same location as their associatedData Connectinstance.

- asia-east1
- asia-east2
- asia-northeast1
- asia-northeast2
- asia-northeast3
- asia-south1
- asia-southeast1
- asia-southeast2
- australia-southeast1
- australia-southeast2
- europe-central2
- europe-north1
- europe-southwest1
- europe-west1
- europe-west2
- europe-west3
- europe-west4
- europe-west6
- europe-west8
- europe-west9
- me-west1
- northamerica-northeast1
- northamerica-northeast2
- southamerica-east1
- southamerica-west1
- us-central1
- us-east1
- us-east4
- us-south1
- us-west1
- us-west2
- us-west3
- us-west4

| Data Connect's Vertex AI integration is not supported for CloudSQL for PostgreSQL instances deployed in:
|
| - asia-northeast2
| - asia-southeast2
| - australia-southeast2
| - northamerica-northeast2
| - southamerica-west1
| - us-west2
| - us-west3

## ManageData Connectservice instances

### Create services

To create a new service, use theFirebaseconsole or run the local project initialization using theFirebaseCLI. These workflows create a newData Connectservice.

These flows also guide you through:

- Provisioning a new Cloud SQL instance (no-cost tier)
- Linking an existing Cloud SQL instance toData Connect(Blaze plan)

| **Note:** Cloud SQL for PostgreSQL instances must be provisioned in the same location as their associatedData Connectinstance. If your application needs Cloud SQL instances in multiple regions, theFirebaseCLI can help deploy the same schema, queries and mutations to the many data connect services in each region.

### Manage users

Data Connectprovides tools to manage user access that follow the the*principle of least privilege* (grant each user or service account the minimum necessary permissions to support needed functionality) and the notion of*role-based access control (RBAC)*(with predefined roles to manage database permissions, simplifying security management).

To add project members as users who can modifyData Connectinstances in your project, use theFirebaseconsole to select appropriate predefined user roles.
| **Note:** Data Connectservices and Cloud SQL for PostgreSQL are separate components of yourData Connectproject. You administer each component separately. For example, you might addData Connectusers with permissions to delete schemas, but this would not grant them the ability to[perform backups of a PostgreSQL database](https://firebase.google.com/docs/data-connect/manage-services-and-databases#administer-cloud).

These roles grant permissions using Identity and Access Management (IAM). A role is a collection of permissions. When you assign a role to a project member, you grant that project member all the permissions that the role contains. See more information in:

- The[overview of Firebase IAM roles](https://firebase.google.com/docs/projects/iam/overview)
- The detailed list of[Data Connectroles](https://firebase.google.com/docs/data-connect/configuration-reference#iam-configuration)

#### Choose roles to enable specific workflows

IAM roles enableFirebaseCLI workflows to let you manage yourData Connectprojects.

|      CLI command, other workflow      |                                                       Role(s) required                                                        |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `firebase init dataconnect`           | - No permissions (when not linking a Cloud SQL instance) - roles/cloudsql.admin (when creating a Cloud SQL instance)          |
| `firebase deploy ---only dataconnect` | - firebasedataconnect.connectors.\* - firebasedataconnect.services.\* - firebasedataconnect.schemas.\* - roles/cloudsql.admin |
| `firebase dataconnect:sql:diff`       | - firebasedataconnect.services.\* - firebasedataconnect.schemas.\*                                                            |
| `firebase dataconnect:sql:migrate`    | - roles/cloudsql.admin on the target Cloud SQL instance                                                                       |
| `firebase dataconnect:sql:grant`      | - roles/cloudsql.admin on the target Cloud SQL instance                                                                       |

## MonitorData Connectservice performance

### Understand service performance

The performance of both theData Connectservice and the Cloud SQL for PostgreSQL service can affect your experience.

- For the Cloud SQL for PostgreSQL service, refer to general guidance in the[Quotas and limits documentation](https://cloud.google.com/sql/docs/postgres/quotas).
- For theData Connectservice, there is quota for GraphQL requests, affecting the rate at which you can call and execute queries:

  - An overall per-project quota of 6000 requests per minute from client app connectors.
  - An overall per-project quota of 6000 requests per minute from theFirebaseAdmin SDKand from the REST API.
  - A per-user quota of 1200 requests per minute. Here, per-user means the limit applies to requests initiated by one IP address, whether from a client app, from theFirebaseAdmin SDKor from the REST API.

  If you run into those quota limits, please reach out to[Firebase support](https://firebase.google.com/support/troubleshooter/contact)to adjust the relevant quota.

### Monitor service performance, usage and billing

You can monitor requests, errors and operation rates, both globally and per operation in theFirebaseconsole.

## Manage Cloud SQL instances

### Free trial limitations

The following Cloud SQL for PostgreSQL features are not supported in the[3 month free trial](https://firebase.google.com/docs/data-connect/pricing):

- Different machine tier than**db-f1-micro**
- Changing resources of your instance, such as region, storage, memory, CPU
- PostgreSQL versions other than 15.x
- Read replicas
- Private instance IP address
- High-availability (multi-zone); only single-zone instances are supported
- Enterprise Plus edition
- Automatic backups
- Automatic storage increase.

### Limitations of temporary onboarding databases

When you addData Connectto your Firebase project, you can begin to prototype your data model and load data right away, since data will be stored in a temporary database. Note that your permanent Cloud SQL for PostgreSQL instance will take from 5 to 20 minutes to provision. Any initial data you load will be automatically migrated to your permanent PostgreSQL database once it is provisioned.

This temporary database is great for exploring your schema and CRUD operations.

If you don't want to use the temporary database, wait for your Cloud SQL instance to be provisioned.

The temporary database is not a PostgreSQL database and does not provide all PostgreSQL features.

Significant limitations are:

- Database size must be less than 1 MB
- Number of rows per table must be less than 1000
- Less than 1 query per second
- No support for full-text search
- No support for vector embedding generation
- No support for raw SQL features like`@view`,`@col(dataType)`

### Administer Cloud SQL instances

In general, you can manage your Cloud SQL instances using the[Google Cloudconsole](https://console.cloud.google.com/sql/instances)to perform the following workflows.
| **Note:** Data Connectservices and Cloud SQL for PostgreSQL are separate components of yourData Connectproject. You administer each component separately. For example, you might add Cloud SQL users with permissions to handle PostgreSQL administrative tasks, like performance monitoring and backups, but this would not grant them the ability to[modifyData Connectinstances](https://firebase.google.com/docs/data-connect/manage-services-and-databases#manage-data-connect-users).

- Stop and restart Cloud SQL instances
- Create and delete Cloud SQL databases (within instances)
- Start PostgreSQL database instances with flags and use a[variety of extensions](https://cloud.google.com/sql/docs/postgres/extensions)
- Monitor performance with[Cloud SQL observability features](https://cloud.google.com/sql/docs/postgres/observability)in the[Google Cloudconsole](https://console.cloud.google.com/monitoring?project=_)
- Manage Cloud SQL access and security with features like IAM, secret manager, data encryption and auth proxy
- Add, delete and administer Cloud SQL users.

For these and other workflows, refer to the[Cloud SQL for PostgreSQL documentation](https://cloud.google.com/sql/docs/postgres).

### Grant PostgreSQL user roles

Data Connectprovides tools to manage user access that follow the the*principle of least privilege* (grant each user or service account the minimum necessary permissions to support needed functionality) and the notion of*role-based access control (RBAC)*(with predefined roles to manage database permissions, simplifying security management).

In some cases, you might want to connect to theData Connect-managed Cloud SQL database directly via a SQL client of your choice using, for example,Cloud Run,Cloud Functionsor GKE.

To enable such connections, you need to grant SQL permissions by:

- Assigning the`roles/cloudsql.client`IAM role to the user or service account that needs to connect to the instance, either from theGoogle Cloudconsole or using thegcloud CLI
- Granting the necessary PostgreSQL role using theFirebaseCLI

#### Assign the Cloud SQL IAM role

For information on working with Cloud SQL for PostgreSQL to assign IAM role`roles/cloudsql.client`, see[Roles and permissions](https://cloud.google.com/sql/docs/postgres/roles-and-permissions).

#### Grant PostgreSQL roles

Using theFirebaseCLI, you can grant predefined PostgreSQL roles to users or service accounts associated with your project with the`firebase dataconnect:sql:grant`command.

For example, to grant the writer role, run this command at the CLI:  

    firebase dataconnect:sql:grant --role writer

For details, refer to the[CLI reference guide](https://firebase.google.com/docs/data-connect/cli-reference#grant-cloudsql-roles).

### Integrate existing Cloud SQL for PostgreSQL databases

The default database provisioning and management flow assumes your project uses a new (greenfield) databases, and when you invoke`firebase deploy`,Data Connectwill display database schema changes to be made and performs any migrations after you approve.

For existing (brownfield) databases, you may have your own workflow for managing schemas and cannot useData Connecttooling for migrations, yet would like to use your database in aData Connectproject to take advantage of its SDK generation for mobile and web, query-based authorization, client connection management, and more.

This section offers guidance about the latter case: integrating existing databases withData Connect.
| **Note:** This discussion assumes you have a CloudSQL for PostgreSQL database and have set up user roles for database administration. If you have a PostgreSQL database you want to migrate to Cloud SQL, you can use the Database Migration Service following[this Cloud SQL for PostgreSQL guide](https://cloud.google.com/database-migration/docs/postgres/quickstart)

#### Integrate an existing database into aData Connectproject

The workflow for integrating an existing database generally involves these steps:

1. DuringData Connectproject setup in theFirebaseconsole, select the instance and database.
2. Using theFirebaseCLI, run the`firebase dataconnect:sql:setup`command and decline the option to allowData Connectto handle SQL migrations.

   To prevent changes to your database schema not driven by your custom tooling, the`setup`command will assign appropriate reader and writer roles, but not the`owner`role. More information about the`setup`command and PostgreSQL roles is available in the[CLI reference guide](https://firebase.google.com/docs/data-connect/cli-reference#cloudsql-management-commands).
3. Write aData ConnectGraphQL schema that matches your database schema.

   You can only deploy your GraphQL schema, queries and mutations when your GraphQL schema is compatible with your PostgreSQL schema.

   To simplify aligning both schemas, we provide the`firebase dataconnect:sql:diff`command, which will provide you with the required SQL statements to migrate your database. You can use this to iteratively refine your GraphQL schema to match your existing database schema.
4. Moving forward, you can iterate quickly on your GraphQL schema, queries, and mutation in your local development environment. Then, when satisfied, you can use`firebase dataconnect:sql:diff`to obtain the SQL migration statements that you can apply to PostgreSQL using your custom tooling and flows.

5. Alternatively, you might make changes directly to your PostgreSQL database first, then try to port them back into your GraphQL schema. We recommend the GraphQL-first approach, since there might be cases where the schema changes aren't supported. In addition, if you deploy changes that make your PostgreSQL schema incompatible with deployed connector queries or mutation, then those connectors might stop working or misbehave.