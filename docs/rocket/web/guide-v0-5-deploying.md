# Source: https://rocket.rs/guide/v0.5/deploying/

Title: Deploying - Rocket Web Framework

URL Source: https://rocket.rs/guide/v0.5/deploying/

Markdown Content:
![Image 1: cloud](https://rocket.rs/images/cloud-0.png)![Image 2: cloud](https://rocket.rs/images/cloud-1.png)![Image 3: cloud](https://rocket.rs/images/cloud-2.png)![Image 4: cloud](https://rocket.rs/images/cloud-0.png)![Image 5: cloud](https://rocket.rs/images/cloud-0.png)![Image 6: cloud](https://rocket.rs/images/cloud-0.png)

This section describes deploying Rocket applications to production. It provides a general overview as well as concrete, reusable examples for common deployment scenarios including [self-managed deployments](https://rocket.rs/guide/v0.5/deploying/#self-managed), [containerization](https://rocket.rs/guide/v0.5/deploying/#containerization), and [fully-managed deployments](https://rocket.rs/guide/v0.5/deploying/#fully-managed).

Rocket does not endorse or prefer any particular tools or services.

Rocket does not endorse or prefer any specific tools or services mentioned in this guide. They are mentioned in exposition only. Rocket is agnostic to its deployment environment.

[](https://rocket.rs/guide/v0.5/deploying/#overview "anchor")Overview
---------------------------------------------------------------------

For any deployment, it's important to keep in mind:

1. **Configuration**

Minimally, Rocket will need to be configured to listen on the correct **port** and **address**, typically port `80` or `8080` and address `0.0.0.0`. Your deployment environment may have different requirements. Recall that by default, you can set the address and port via the environment variables `ROCKET_ADDRESS` and `ROCKET_PORT` as well as through [many other means](https://rocket.rs/guide/v0.5/configuration).

1. **Asset Bundling**

If your application serves assets or leverages templates, you may need to bundle those assets with your application binary. For example, if you serve static assets from the `./static` directory and enable templates, you'll need to ensure that those directories are present and **in the current working directory** that your application binary starts in.

1
2
3
4
5
6
7
8
9 use rocket::fs::FileServer;use rocket_dyn_templates::Template;#[launch]fn rocket() -> _ { rocket::build() .mount("/", FileServer::from("./static")) .attach(Template::fairing())}
For the application above, assuming the `template_dir` configuration parameter hasn't been changed, you'll need to ensure that the `static` and `templates` directories are placed in the current working directory that the application will start in. Otherwise, Rocket will refuse to launch.

1. **Load Balancing**

Rocket does not yet have robust support for [DDoS mitigation](https://github.com/rwf2/Rocket/issues/1405), so a production deployment will require placing Rocket behind a load balancer or reverse proxy that does. If you are deploying your Rocket application to managed environments such as Kubernetes, Heroku, or Google Cloud Run, this will be handled for you automatically. However, if you're deploying to a self-managed environment such as a VPS, we recommend placing Rocket behind a mature reverse proxy such as HAProxy or NGINX.

1. **Service Management**

As your application matures, you'll need to deploy updated versions to your production environment, stopping the existing application and starting the new one in its place. In a managed environment, you can likely rely on the environment to provide these mechanisms. In a self-managed environment, using a service manager like `systemd`, _in addition_ to a reverse proxy, is recommended.

In either case, it's important to know that once a Rocket application has started, it will run until [graceful shutdown](https://api.rocket.rs/v0.5/rocket/shutdown/struct.ShutdownConfig.html) is initiated. Your application should leverage Rocket's graceful shutdown mechanisms such as the [`Shutdown`](https://api.rocket.rs/v0.5/rocket/struct.Shutdown.html) future and [shutdown fairings](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html#shutdown) to clean-up resources before terminating. You should also ensure that the graceful shutdown configuration is aligned with your environment. For example, Kubernetes issues a `SIGTERM` signal to initiate termination which Rocket listens for by default, but other environments may send other signals which you might need to enable as [triggers](https://api.rocket.rs/v0.5/rocket/shutdown/struct.ShutdownConfig.html#triggers).

The following section addresses these concerns and more for common deployment scenarios.

[](https://rocket.rs/guide/v0.5/deploying/#common-scenarios "anchor")Common Scenarios
-------------------------------------------------------------------------------------

### [](https://rocket.rs/guide/v0.5/deploying/#self-managed "anchor")Self-Managed

In a _self-managed_ environment, you are typically responsible for all facets of deployment and service management. In exchange, a self-managed environment typically incurs the lowest financial cost.

You must decide whether you manage your Rocket application _directly_, by installing, configuring, and running a service manager, load balancer, and Rocket application, or _indirectly_ by installing and configuring an application management service like [kubernetes](https://kubernetes.io/), [k3s](https://k3s.io/), or [dokku](https://dokku.com/). Because indirect self-management typically revolves around [containerization](https://rocket.rs/guide/v0.5/deploying/#containerization), covered in the next section, we focus on _direct_ self-management here.

Our recommendation for a direct self-managed deployment is to:

* **Compile for the remote target (i.e, the VPS), bundle, and copy.**

Compile your application for the remote target and bundle the binary with its assets. You may need to cross-compile for the remote target: we recommend using [`cargo-zigbuild`](https://github.com/rust-cross/cargo-zigbuild). Before cross-compiling, you'll also need to install the Rust toolchain for the target.

The script below performs these steps, producing a gzipped archive ready to be copied to a remote server.

1
2
3
4
5
6
7
8
9
10
11
12
13
14 PKG="app" TARGET="x86_64-unknown-linux-gnu" ASSETS=("Rocket.toml" "static" "templates") BUILD_DIR="target/${TARGET}/release" rustup target add $TARGET cargo zigbuild --target $TARGET --release tar -cvzf "${PKG}.tar.gz" "${ASSETS[@]}" -C "${BUILD_DIR}" "${PKG}"

* **Run the application as a managed service.**

Once the bundle is at the remote server, use a service manager to start, monitor, and stop the application. As an example, assuming the bundle produced by the script above was extracted to `/www/pkg`, the following `systemd` service file defines a service for the application:

1
2
3
4
5
6
7
8
9
10
11
12
13
14[Unit] Description=Rocket Application After=network.target [Service] Type=simple WorkingDirectory=/www/pkg ExecStart=/www/pkg/pkg User=pkg Group=pkg Restart=always [Install] WantedBy=multi-user.target  
You'll want to modify the service file as needed. Consider particularly the `User` and `Group`: that user/group will need to be authorized to access the `WorkingDirectory`.

Write the service file to the `systemd` services directory (for example, `/etc/systemd/system/pkg.service`). You can now interact with the service as usual:

1 systemctl [status,enable,start,stop,restart,disable] pkg
If the service is running but the server doesn't appear to be responding, ensure that you've set the address and port you expect in the `[default]`, `[global]`, and/or `[production]` sections of `Rocket.toml` or via another configuration source. For example, you may wish to set systemd `Service` environment variables:

1
2
3[Service] + Environment=ROCKET_ADDRESS=127.0.0.1 + Environment=ROCKET_PORT=8000  

* **Configure a reverse proxy for the application.**

Finally, configure a reverse proxy to serve requests to the running application server. As an example, a simple NGINX reverse proxy configuration file for the application above might look like:

1
2
3
4
5
6
7
8
9 server {  listen 80;  location / {  proxy_pass http://127.0.0.1:8000;  proxy_set_header X-Real-IP $remote_addr;  proxy_set_header X-Forwarded-Proto $scheme; } }  
Note that we configure NGINX to forward the actual remote IP via the `X-Real-IP` header, which Rocket uses by default via [`ip_header`](https://api.rocket.rs/v0.5/rocket/config/struct.Config.html#structfield.ip_header). Additionally, the scheme is forwarded via `X-Forwarded-Proto`, but it must be explicitly configured via [`proxy_proto_header`](https://api.rocket.rs/v0.5/rocket/config/struct.Config.html#structfield.proxy_proto_header) for Rocket to consider.

### [](https://rocket.rs/guide/v0.5/deploying/#containerization "anchor")Containerization

In a _containerization_ environment, you are responsible for writing a `Dockerfile` or `Containerfile` which you provide to an application platform. The platform may be self-managed, as with [k3s](https://k3s.io/) or [dokku](https://dokku.com/), or fully-managed, as with Google Cloud Run or Heroku.

Below you'll find an example of a `Dockerfile` that:

* Builds the application with the latest stable Rust compiler.
* Uses `--mount=type=cache` to avoid recompiling dependencies.
* Uses a second stage to create a slim (~100MiB), ready-to-deploy image with only what's needed.
* Bundles all of an application's assets in the container.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35 FROM docker.io/rust:1-slim-bookworm AS build ARG pkg=rocket-app WORKDIR /build COPY . . RUN --mount=type=cache,target=/build/target \ --mount=type=cache,target=/usr/local/cargo/registry \ --mount=type=cache,target=/usr/local/cargo/git \ set -eux; \ cargo build --release; \ objcopy --compress-debug-sections target/release/$pkg ./main FROM docker.io/debian:bookworm-slim WORKDIR /app COPY --from=build /build/main ./ COPY --from=build /build/Rocket.tom[l] ./static COPY --from=build /build/stati[c] ./static COPY --from=build /build/template[s] ./templates ENV ROCKET_ADDRESS=0.0.0.0 ENV ROCKET_PORT=8080 CMD ./main

You will need to modify the `pkg``ARG` or provide it via the command-line:

1 docker build --build-arg pkg=cargo_package_name -t app .

You may also need to make the following changes:

* Add/remove/modify `ENV` variables as needed.
* Modify the expected `target/release/$pkg` directory.
* Add more assets to `COPY` to the final image.

Finally, we recommend the following `.dockerignore` file to avoid copying unnecessary artifacts:

1
2
3
4 target .cargo **/_.sh **/_.tar.gz

### [](https://rocket.rs/guide/v0.5/deploying/#fully-managed "anchor")Fully-Managed

In a _fully-managed_ environment, you provide a service with your source code and instructions on how to build and run your application. The `Dockerfile` in the [containerization](https://rocket.rs/guide/v0.5/deploying/#containerization) section, coupled with a configuration file that instructs the service to build it, may be one such example.

Because the specifics on deploying to a fully-managed environment depend on the environment, we provide only the following general guidelines:

* **Ensure the address and port are set as required.**

Most environments require your application to listen on `0.0.0.0`. Ensure `ROCKET_ADDRESS=0.0.0.0`.

Some environments require your application to listen on specific ports. Remember to set the port as required. For example, if the service requires your application to listen on a port provided by a `$PORT` environment variable, set `ROCKET_PORT=$PORT` before starting your application.

* **Compile or run with `--release`.**

Ensure that you run `cargo` commands with `--release`. Besides compiling with optimizations, compiling with `--release` sets the default [configuration profile](https://rocket.rs/guide/v0.5/configuration/#profiles) to `release`.

* **Enable debug logging if the application misbehaves.**

The default log level in `--release` (the release profile) is `critical`. This level may omit messages helpful in understanding application misbehavior. To reenable those messages, set `ROCKET_LOG_LEVEL=debug`.

* * *

![Image 7: cloud](https://rocket.rs/images/cloud-0.png)![Image 8: cloud](https://rocket.rs/images/cloud-1.png)![Image 9: cloud](https://rocket.rs/images/cloud-2.png)
