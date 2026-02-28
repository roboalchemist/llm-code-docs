# Harbor docs | Test Harbor with the Demo Server

**Source:** https://goharbor.io/docs/2.14.0/install-config/demo-server/

Test Harbor with the Demo Server

[Harbor version 2.14.0](/docs/2.14.0)

[Harbor Installation and Configuration](/docs/2.14.0/install-config/)

* [Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/)
* [Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/)
* [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/)
* [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
* [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
* [Configure Internal TLS communication between Harbor Component](/docs/2.14.0/install-config/configure-internal-tls/)
* [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
* [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)
* [Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/)
* [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/)
* [Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/)
* [Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/)
* [Harbor Configuration](/docs/2.14.0/install-config/configure-system-settings-cli/)

[Harbor Administration](/docs/2.14.0/administration/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

The Harbor team has made available a demo Harbor instance that you can use to experiment with Harbor and test its functionalities.

When using the demo server, please take note of the conditions of use.

## Conditions of Use of the Demo Server

* The demo server is reserved for experimental use only, to allow you to test Harbor functionality.
* Do not upload sensitive images to the demo server.
* The demo server is not a production environment. The Harbor team is not responsible for any loss of data, functionality, or service that might result from its use.
* The demo server is cleaned and reset every two days.
* The demo server only allows you to test user functionalities. You cannot test administrator functionalities. To test administrator functionalities and advanced features, set up a Harbor instance.
* Do not push images >100MB to the demo server, as it has limited storage capacity.

If you encounter any problems while using the demo server, open an
[issue on Github](https://github.com/goharbor/harbor/issues) or contact the Harbor team on
[Slack](https://github.com/goharbor/harbor#community).

## Access the Demo Server

1. Go to
   <https://demo.goharbor.io>.
2. Click **Sign up for an account**.
3. Create a user account by providing a username, your email address, your name, and a password.
4. Log in to the Harbor interface using the account you created.
5. Explore the default project, `library`.
6. Click **New Project** to create your own project.

   For information about how to create a project, see
   [Create a Project](/docs/2.14.0/working-with-projects/create-projects/).
7. Open a Docker client and log in to Harbor with the credentials that you created above.

   ```
   docker login demo.goharbor.io
   ```
8. Create a very simple `Dockerfile` with the following contents.

   ```
   FROM busybox:latest
   ```
9. Build an image from this Dockerfile and tag it.

   ```
   docker build -t demo.goharbor.io/your-project/test-image .
   ```
10. Push the image to your project in Harbor.

    ```
    docker push demo.goharbor.io/your-project/test-image
    ```
11. In the Harbor interface, go to **Projects** > *your\_project* > **Repositories** to view the image repository that you pushed to your Harbor project.

## What to Do Next

See the
[Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/).

On this page

  
  

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/demo-server.md)
[Create issue](https://github.com/goharbor/harbor/issues)