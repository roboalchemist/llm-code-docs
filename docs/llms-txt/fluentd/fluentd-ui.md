# Source: https://docs.fluentd.org/deployment/fluentd-ui.md

# Source: https://docs.fluentd.org/0.12/deployment/fluentd-ui.md

# Fluentd UI

[fluentd-ui](https://github.com/fluent/fluentd-ui) is a browser-based [fluentd](http://fluentd.org/) and [td-agent](http://docs.treasuredata.com/articles/td-agent) manager that supports following operations.

* Install, uninstall, and upgrade Fluentd plugins
* start/stop/restart fluentd process
* Configure Fluentd settings such as config file content, pid file

  path, etc
* View Fluentd log with simple error viewer

## Getting Started

If you've installed td-agent, you can start it by `td-agent-ui start` as below:

```
$ sudo /usr/sbin/td-agent-ui start
Puma 2.9.2 starting...
* Min threads: 0, max threads: 16
* Environment: production
* Listening on tcp://0.0.0.0:9292
```

Or if you use fluentd gem, install fluentd-ui via `gem` command at first.

```
$ gem install -V fluentd-ui
$ fluentd-ui start
Puma 2.9.2 starting...
* Min threads: 0, max threads: 16
* Environment: production
* Listening on tcp://0.0.0.0:9292
```

Then, open <http://localhost:9292/> by your browser.

The default account is username="admin" and password="changeme"

![fluentd-ui](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75LobUYsnqh1DN83%2Ffluentd-ui.gif?generation=1548740488837671\&alt=media)

## Screenshots

(v0.3.9)

### Dashboard

![dashboard](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75Lqhjda7klOWXLH%2Fdashboard.gif?generation=1548740487994706\&alt=media)

### Setting

![setting](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75Ls4uwG3MIRBti-%2Fsetting.gif?generation=1548740489790657\&alt=media)

### in\_tail setting

![in\_tail](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75Lu8ZFlZsWbyiba%2Fin_tail.gif?generation=1548740489728498\&alt=media)

### Plugin

![plugin](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75LwXtZ-_EUY8A1i%2Fplugin.gif?generation=1548740489553253\&alt=media)

![ss01](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75LySbiYP5pdVZiH%2F01.png?generation=1548740490538533\&alt=media) ![ss02](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75M-jqdAEBlQHqQo%2F02.png?generation=1548740487994588\&alt=media) ![ss03](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75M1tIVYzDBR2vp6%2F03.png?generation=1548740488752147\&alt=media) ![ss04](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75M3IRX-64NbIe3n%2F04.png?generation=1548740488688874\&alt=media) ![ss05](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75M58Do4BvU-trsj%2F05.png?generation=1548740490236453\&alt=media)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
