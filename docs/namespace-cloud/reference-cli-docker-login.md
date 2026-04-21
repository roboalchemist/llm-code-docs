<!-- Source: https://namespace.so/docs/reference/cli/docker-login -->

# nsc docker login

Log into the Namespace Container Registry for use with Docker.

`docker login` automatically updates your default Docker `config.json` file with the
Namespace [credential helper](https://docs.docker.com/engine/reference/commandline/login/#credential-helpers)
and prints your Workspace registry endpoint.

The `docker-credential-nsc` credential helper is an executable binary that gets automatically installed alongside `nsc`.
Docker-like tools call the helper binary to retrieve fresh credentials every time they access the specified registry.

Docker-like tools expect the credential helper to be available in your `$PATH`.
You can check that the credential helper is in your path by running `which docker-credential-nsc`.

## Usage

```
nsc docker login
```

### Example

```
$ nsc docker login
 
You are now logged into your workspace container registry:
 
  nscr.io/8enum0hp1l5ii
 
Run your first build with:
 
  $ nsc build . --name test --push
 
Visit our docs for more details on Remote Builds:
 
  https://namespace.so/docs/solutions/docker-builders
```

Where **8enum0hp1l5ii** is your **workspace ID**.

Now you can use the `docker` CLI to push/pull container images to Namespace
Container Registry.
For example:

```
docker push nscr.io/8enum0hp1l5ii/IMAGE_NAME
```

## Options

### --output\_registry\_to <file>

With this option `nsc` will write the Namespace Container Registry endpoint to
the provided file.

Last updated July 4, 2025
