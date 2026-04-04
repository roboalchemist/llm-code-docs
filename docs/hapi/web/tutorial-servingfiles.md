# hapi Documentation
# Source: https://hapi.dev/tutorials/servingfiles/?lang=en_US

Tutorials

Languages:

en-US pt-BR ko-KR tr-TR zh-CN

  * [Getting Started](/tutorials/gettingstarted/?lang=en_US)

* * *

  * [Express Migration](/tutorials/expresstohapi/?lang=en_US)

* * *

  * [Authentication](/tutorials/auth/?lang=en_US)

* * *

  * [Caching](/tutorials/caching/?lang=en_US)

* * *

  * [Cookies](/tutorials/cookies/?lang=en_US)

* * *

  * [Logging](/tutorials/logging/?lang=en_US)

* * *

  * [Plugins](/tutorials/plugins/?lang=en_US)

* * *

  * [Routing](/tutorials/routing/?lang=en_US)

* * *

  * [Server Methods](/tutorials/servermethods/?lang=en_US)

* * *

  * [Serving Static Files](/tutorials/servingfiles/?lang=en_US)

* * *

  * [Testing](/tutorials/testing/?lang=en_US)

* * *

  * [Validation](/tutorials/validation/?lang=en_US)

* * *

  * [Views](/tutorials/views/?lang=en_US)

* * *

  * [Community Tutorials](/tutorials/community/?lang=en_US)



# Serving Static Content

_This tutorial is compatible with hapi v17 and newer_

##  Overview

Inevitably while building any web application, the need arises to serve a simple file from disk. There is a hapi plugin called [inert](/module/inert) that adds this functionality to hapi through the use of additional handlers.

First you need to install and add `inert` as a dependency to your project:

`npm install @hapi/inert`

##  Inert

The `inert` plugin provides new handler methods for serving static files and directories, as well as adding a `h.file()` method to the toolkit, which can respond with file based resources.

##  Relative paths

To simplify things, especially if you have multiple routes that respond with files, you can configure a base path in your server and only pass relative paths to `h.file()`:
    
    
    'use strict';
    
    const Hapi = require('@hapi/hapi');
    const Path = require('path');
    
    const start = async () => {
    
        const server = Hapi.server({
            routes: {
                files: {
                    relativeTo: Path.join(__dirname, 'public')
                }
            }
        });
    
        await server.register(require('@hapi/inert'));
    
        server.route({
            method: 'GET',
            path: '/picture.jpg',
            handler: function (request, h) {
    
                return h.file('picture.jpg');
            }
        });
    
        await server.start();
    
        console.log('Server running at:', server.info.uri);
    };
    
    start();
    

When you set an option under `server.options.routes`, such as above, it will apply to _all_ routes. You can also set these options, including the `relativeTo` option on a per-route level.

##  `h.file(path, [options])`

Now, let's see how to use the [`h.file()`](/module/inert/api#hfilepath-options) method:
    
    
    const start = async () => {
    
        const server = Hapi.server();
    
        await server.register(require('@hapi/inert'));
    
        server.route({
            method: 'GET',
            path: '/picture.jpg',
            handler: function (request, h) {
    
                return h.file('/path/to/picture.jpg');
            }
        });
    
        await server.start();
    
        console.log('Server running at:', server.info.uri);
    };
    
    start();
    

By requiring the `inert` plugin, you get access `h.file()` method. Here, you tell `h.file()` the path of the image you want to return. In this case, `'/path/to/picture.jpg'`.

##  File handler

An alternative to using the `h.file()` method would be to use the `file` handler:
    
    
    server.route({
        method: 'GET',
        path: '/picture.jpg',
        handler: {
            file: 'picture.jpg'
        }
    });
    

###  File handler options

You can also specify the parameter as a function that accepts the `request` object and returns a string representing the file's path (absolute or relative):
    
    
    server.route({
        method: 'GET',
        path: '/{filename}',
        handler: {
            file: function (request) {
                return request.params.filename;
            }
        }
    });
    

It can also be an object with a `path` property. When using the object form of the handler, you can do a few additional things, like setting the `Content-Disposition` header and allowing compressed files like so:
    
    
    server.route({
        method: 'GET',
        path: '/script.js',
        handler: {
            file: {
                path: 'script.js',
                filename: 'client.js', // override the filename in the Content-Disposition header
                mode: 'attachment', // specify the Content-Disposition is an attachment
                lookupCompressed: true // allow looking for script.js.gz if the request allows it
            }
        }
    });
    

##  Directory handler

In addition to the `file` handler, inert also adds a `directory` handler that allows you to specify one route to serve multiple files. In order to use it, you must specify a route path with a parameter. The name of the parameter does not matter, however. You can use the asterisk extension on the parameter to restrict file depth as well. The most basic usage of the directory handler looks like:
    
    
    server.route({
        method: 'GET',
        path: '/{param*}',
        handler: {
            directory: {
                path: 'directory-path-here'
            }
        }
    });
    

###  Directory handler options

The above route will respond to any request by looking for a matching filename in the `directory-path-here` directory. Note that a request to `/` in this configuration will reply with an HTTP `403` response. You can fix this by adding an index file. By default hapi will search in the directory for a file called `index.html`. You can disable serving an index file by setting the index option to `false`, or alternatively you can specify an array of files that inert should look for as index files:
    
    
    server.route({
        method: 'GET',
        path: '/{param*}',
        handler: {
            directory: {
                path: 'directory-path-here',
                index: ['index.html', 'default.html']
            }
        }
    });
    

A request to `/` will now first try to load `/index.html`, then `/default.html`. When there is no index file available, inert can display the contents of the directory as a listing page. You can enable that by setting the `listing` property to `true` like so:
    
    
    server.route({
        method: 'GET',
        path: '/{param*}',
        handler: {
            directory: {
                path: 'directory-path-here',
                listing: true
            }
        }
    });
    

Now a request to `/` will reply with HTML showing the contents of the directory. When using the directory handler with listing enabled, by default hidden files will not be shown in the listing. That can be changed by setting the `showHidden` option to `true`. Like the file handler, the directory handler also has a `lookupCompressed` option to serve precompressed files when possible. You can also set a `defaultExtension` that will be appended to requests if the original path is not found. This means that a request for `/bacon` will also try the file `/bacon.html`.

##  Static file server

One common case for serving static content is setting up a file server. The following example shows how to setup a basic file serve in hapi:
    
    
    const Path = require('path');
    const Hapi = require('@hapi/hapi');
    const Inert = require('@hapi/inert');
    
    const init = async () => {
    
        const server = new Hapi.Server({
            port: 3000,
            routes: {
                files: {
                    relativeTo: Path.join(__dirname, 'public')
                }
            }
        });
    
        await server.register(Inert);
    
        server.route({
            method: 'GET',
            path: '/{param*}',
            handler: {
                directory: {
                    path: '.',
                    redirectToSlash: true
                }
            }
        });
    
        await server.start();
    
        console.log('Server running at:', server.info.uri);
    };
    
    init();
    

The first thing you do is require both `inert` and `path`. As you will see, you will need both of these to get our file server up and running.

Next, you configure `server.options.routes`. You set the location the server will look for the static files by setting the `relativeTo` option.

After your server is configured, you then register the `inert` plugin. This will allow you to have access to the `directory` handler, which will enable you to server your files. In the `directory` handler, you configure `path`, which is required, to look in the entire `public` directory which you specified in the `relativeTo` option. The second option is the `redirectToSlash` option. By setting this to `true`, you tell the server to redirect requests without trailing slashes to the same path with those with the trailing slash.

![clipboard](/img/clipboardCheck.png)
