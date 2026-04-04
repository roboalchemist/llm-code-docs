# Fauxton Documentation
# Source: https://docs.couchdb.org/en/stable/fauxton/install.html
# Path: install.html

[ Apache CouchDB® ![Logo](../_static/logo.png) ](../index.html)

## Table of Contents

User Guides

  * [1\. Introduction](../intro/index.html)
  * [2\. Replication](../replication/index.html)
  * [3\. Querying CouchDB](../ddocs/index.html)
  * [4\. Best Practices](../best-practices/index.html)

Administration Guides

  * [1\. Installation](../install/index.html)
  * [2\. Setup](../setup/index.html)
  * [3\. Configuration](../config/index.html)
  * [4\. Cluster Management](../cluster/index.html)
  * [5\. Maintenance](../maintenance/index.html)
  * [6\. Fauxton](index.html)
    * 6.1. Fauxton Setup
      * 6.1.1. Fauxton Visual Guide
      * 6.1.2. Development Server
      * 6.1.3. Understanding Fauxton Code layout
        * 6.1.3.1. ToDo items
  * [7\. Experimental Features](../experimental.html)

Reference Guides

  * [1\. API Reference](../api/index.html)
  * [2\. JSON Structure Reference](../json-structure.html)
  * [3\. Query Server](../query-server/index.html)
  * [4\. Partitioned Databases](../partitioned-dbs/index.html)

Other

  * [1\. Release Notes](../whatsnew/index.html)
  * [2\. Security Issues / CVEs](../cve/index.html)
  * [3\. Reporting New Security Problems with Apache CouchDB](../cve/index.html#reporting-new-security-problems-with-apache-couchdb)
  * [4\. License](../about.html)
  * [5\. Contributing to this Documentation](../contributing.html)

## Quick Reference Guides

  * [API Quick Reference](../http-routingtable.html)
  * [Configuration Quick Reference](../config-ref.html)

## More Help

  * [CouchDB Homepage](https://couchdb.apache.org/)
  * [Mailing Lists](https://couchdb.apache.org/#mailing-list)
  * [Realtime Chat](https://couchdb.apache.org/#chat)
  * [Issue Tracker](https://github.com/apache/couchdb/issues)
  * [Download Docs](../download.html)

__[Apache CouchDB®](../index.html)

  * [](../index.html)
  * [6\. Fauxton](index.html)
  * 6.1. Fauxton Setup
  * [ View page source](../_sources/fauxton/install.rst.txt)

* * *

# 6.1. Fauxton Setup

Fauxton is included with CouchDB 2.0, so make sure CouchDB is running, then go
to:

    
    
    http://127.0.0.1:5984/_utils/
    

You can also upgrade to the latest version of Fauxton by using npm:

    
    
    $ npm install -g fauxton
    $ fauxton
    

(Recent versions of [node.js](http://nodejs.org/) and
[npm](https://npmjs.org/doc/README.html) are required.)

## 6.1.1. Fauxton Visual Guide

You can find the Visual Guide here:

    

<http://couchdb.apache.org/fauxton-visual-guide>

## 6.1.2. Development Server

Recent versions of [node.js](http://nodejs.org/) and
[npm](https://npmjs.org/doc/README.html) are required.

Using the dev server is the easiest way to use Fauxton, specially when
developing for it:

    
    
    $ git clone https://github.com/apache/couchdb-fauxton.git
    $ npm install && npm run dev
    

## 6.1.3. Understanding Fauxton Code layout

Each bit of functionality is its own separate module or addon.

All core modules are stored under app/module and any addons that are optional
are under app/addons.

We use [backbone.js](http://backbonejs.org/) and
[Backbone.layoutmanager](https://github.com/tbranyen/backbone.layoutmanager)
quite heavily, so best to get an idea how they work. Its best at this point to
read through a couple of the modules and addons to get an idea of how they
work.

Two good starting points are app/addon/config and app/modules/databases.

Each module must have a base.js file, this is read and compile when Fauxton is
deployed.

The resource.js file is usually for your `Backbone.Models` and
`Backbone.Collections`, view.js for your `Backbone.Views`.

The routes.js is used to register a url path for your view along with what
layout, data, breadcrumbs and api point is required for the view.

### 6.1.3.1. ToDo items

Checkout JIRA or [GitHub Issues](https://github.com/apache/couchdb-
fauxton/issues) for a list of items to do.

[ Previous](index.html "6. Fauxton") [Next ](../experimental.html "7.
Experimental Features")

* * *

(C) Copyright 2025, Apache Software Foundation. CouchDB® is a registered
trademark of the Apache Software Foundation.

Built with [Sphinx](https://www.sphinx-doc.org/) using a
[theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the
Docs](https://readthedocs.org).

