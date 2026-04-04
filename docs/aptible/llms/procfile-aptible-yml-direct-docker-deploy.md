# Source: https://www.aptible.com/docs/core-concepts/apps/deploying-apps/image/deploying-with-docker-image/procfile-aptible-yml-direct-docker-deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Procfiles and  `.aptible.yml`

To provide a [Procfile](/how-to-guides/app-guides/define-services) or a [`.aptible.yml`](/core-concepts/apps/deploying-apps/releases/aptible-yml) when using [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy), you need to include these files in your Docker image at a pre-defined location:

* The `Procfile` must be located at `/.aptible/Procfile`.
* The `.aptible.yml` must be located at `/.aptible/.aptible.yml`.

Both of these files are optional: when you deploy directly from a Docker image, Aptible uses your image's `CMD` to know which service command to run.

# Creating a suitable Docker Image

Here is how you can create those files in your Dockerfile, assuming you have files named `Procfile` and `.aptible.yml` at the root of your Docker build context:

```dockerfile  theme={null}
RUN mkdir /.aptible/
ADD Procfile /.aptible/Procfile
ADD .aptible.yml /.aptible/.aptible.yml
```

Note that if you are using `docker build .` to build your image, then the build context is the current directory.
