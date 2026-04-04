# Source: https://northflank.com/docs/v1/application/network/expose-your-application.md

# Expose your application

You will need to expose the relevant port(s) in your application to make it available on private or public networks if this is not configured by default.

If you're using a [Dockerfile](https://northflank.com/docs/v1/application/build/build-with-a-dockerfile) you should use the [EXPOSE](https://docs.docker.com/engine/reference/builder/#expose) command to specify which [ports the container listens on](https://docs.docker.com/engine/reference/builder/#expose). This does not expose the ports in your application, but informs Northflank which ports your deployment should publish.

You may need to specifically bind your application to all available IP addresses by specifying the hostname as `0.0.0.0` in order to accept incoming connections from the container it is running in, while some applications bind to this hostname by default.

Below is a list of commonly-deployed applications and examples of the necessary commands to run them on the desired port. You should refer to the documentation for the language or framework you are using for more detailed information, and use [environment variables](https://northflank.com/docs/v1/application/secure/inject-secrets) rather than hardcoded settings where possible.

## Node

To run a [Node server](https://nodejs.org/en/), the server must be bound to hostname `0.0.0.0` and given a port to listen on. Specify the port in the Dockerfile and call your main file with the `node` command.

#### App example

```js
const http = require('http');

const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname);
```

#### Docker commands example

```Dockerfile
EXPOSE 3000
CMD ["node", "index.js"]
```

## NGINX

Many web applications use [NGINX](https://www.f5.com/products/nginx) to serve a generated site, for example [Angular](https://github.com/northflank-examples/angular-js-example). By default, NGINX listens on port 80, but this can be changed in the [NGINX configuration file](https://docs.nginx.com/nginx/admin-guide/web-server/web-server/) if required.

#### Docker commands example

```Dockerfile
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## Express

To serve an [Express.js application](https://expressjs.com/), ensure the Express application is set to listen on your desired port, then expose that port in the Dockerfile and include the command to run the server.

You can find an example of a [Node Express Server in this repository](https://github.com/northflank-examples/node-express-example).

#### Application example

```javascript
const express = require('express');
const app = express();
const port = 80;

app.listen(port);
```

#### Docker commands example

```Dockerfile
EXPOSE 80
CMD [ "yarn", "run", "start" ]
```

## Next

A [Next.js application](https://nextjs.org/) runs by default on hostname `0.0.0.0` and port `3000`. You can change the port by adding an [environment variable](https://northflank.com/docs/v1/application/run/inject-runtime-variables) called `PORT`, with the value of the port you want to use. You should update your [Dockerfile](https://northflank.com/docs/v1/application/build/build-with-a-dockerfile) and the [network settings](configure-ports) of any deployments to reflect the new port.

You can find an example of a [Next.js application in this repository](https://github.com/northflank-examples/next-js-example).

#### Docker commands example

```Dockerfile
EXPOSE 3000
CMD ["node_modules/.bin/next", "start"]
```

## Flask

To run a Python [Flask application](https://palletsprojects.com/p/flask/) you will need to include a [WSGI server](https://flask.palletsprojects.com/en/2.2.x/deploying/).

You can find an example of a [Python Flask application in this repository](https://github.com/northflank-examples/python-flask-example). This example uses the [Waitress server](https://flask.palletsprojects.com/en/2.2.x/deploying/waitress/).

#### Application example

```python
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
```

#### Docker commands example

```Dockerfile
ENTRYPOINT ["python"]
CMD ["main.py"]

EXPOSE 80
```

## Django

To run a Python [Django application](https://www.djangoproject.com/) you will need to run the server with the command `python manage.py runserver`, binding to `0.0.0.0` with the port specified. The example below uses port `80`.

You can find an example of a [Python Django application in this repository](https://github.com/northflank-examples/python-django-example).

#### Docker commands example

```Dockerfile
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
```

## PHP Laravel

To serve a [Laravel application](https://laravel.com/) you must run the PHP [artisan](https://laravel.com/docs/9.x/artisan) command to serve the site, binding to hostname `0.0.0.0` with the option `--host=`. You can use the option `--port=` to specify the port to listen on.

You can find an example of a [Laravel application in this repository](https://github.com/northflank-examples/php-laravel-example).

#### Docker commands example

```Dockerfile
CMD [ "php", "artisan", "serve", "--host=0.0.0.0", "--port=80" ]
EXPOSE 80
```

## Ruby on Rails

To serve a [Ruby on Rails application](https://rubyonrails.org/), you must expose the port (default `3000`) and run the Rails server, bound to `0.0.0.0`.

You can find an example of a [Ruby on Rails application in this repository](https://github.com/northflank-examples/ruby-on-rails-example).

#### Configuration example

While developing on your local machine, your Rails server will be available on `localhost`, however you will need to authorize hosts to make it accessible when deployed.

You can configure your application to accept connections on Northflank by adding the following to the relevant environment configuration file in `config/environments`. The `NF_HOSTS` environment variable is injected to all runtime containers on Northflank and contains all the configured [domain names](configure-ports#public-ports) for the server.

```rb
if ENV["NF_HOSTS"].present?
     config.hosts = ENV["NF_HOSTS"]
end
```

#### Docker commands example

```Dockerfile
EXPOSE 3000
CMD ["bin/rails", "server", "-b", "0.0.0.0"]
```

## Rust

To serve a [Rust application](https://rust-lang.org/) you can use a web application framework, in our example we use [nickel](https://nickel-org.github.io/) to listen on port `6767`, and bound to `0.0.0.0`.

You can find an example of a [Rust application in this repository](https://github.com/northflank-examples/rust-example).

#### Rust application example

```rust
#[macro_use] extern crate nickel;

use nickel::{Nickel, StaticFilesHandler};

fn main() {
    let mut server = Nickel::new();
    server.utilize(StaticFilesHandler::new("static/"));
    server.listen("0.0.0.0:6767").unwrap();
}
```

#### Docker commands example

```Dockerfile
EXPOSE 6767
CMD ["./rust-docker-web"]
```

## Next steps

- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
