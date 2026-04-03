# RPC Plugin

## Description

The plugin is designed as a replacement of the web server module `mod_scgi` and performs functions of the last. I.e. carries out link between a web server and rtorrent. On one hand, it simplifies setup (and protection) of the chain ruTorrent->web-server->rtorrent (no need to care about any `/RPC2`). On the other hand - implementation of this functionality in php leads to additional (in comparison with "the native" module of a web server) server processor loading. Therefore usage of the given plugin is not recommended for routers and various embedded systems.
