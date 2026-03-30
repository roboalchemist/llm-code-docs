# Source: https://docs.fluentd.org/0.12/articles/recipe-syslog-to-treasure-data.md

# Recipe Syslog To Treasure Data

Looking to get data out of syslog into treasure data? You can do that with [fluentd](https://github.com/fluent/fluentd-docs-gitbook/tree/507e377b7e8e78a312dc49e76bd9a302c33fd058/fluentd.org) in **10 minutes**!

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-Lk7cBlK-Nhj6kCsg9Nq%2F-Lk7c_SPEcOx4IcrSa_O%2Fsyslog.png?generation=1563512977910548\&alt=media)

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-Lk7cBlK-Nhj6kCsg9Nq%2F-Lk7cY6WyV-VIE3H67AD%2Ftreasure_data.png?generation=1563512954980863\&alt=media)

Here is how:

```
$ gem install fluentd
$ gem install fluent-plugin-td
$ touch fluentd.conf
```

`fluentd.conf` should look like this (just copy and paste this into fluentd.conf):

```
<source>
  @type syslog
  port 5140
  bind 0.0.0.0
  tag system.local
</source>

<match **>
  @type tdlog
  apikey <Treasure Data API key> # You get your API key by signing up for Treasure Data
  auto_create_table
  buffer_type file
  buffer_path /var/log/td-agent/buffer/td
</match>
```

After that, you can start fluentd and everything should work:

```
$ fluentd -c fluentd.conf
```

Of course, this is just a quick example. If you are thinking of running fluentd in production, consider using [td-agent](https://github.com/fluent/fluentd-docs-gitbook/tree/507e377b7e8e78a312dc49e76bd9a302c33fd058/articles/td-agent.md), the enterprise version of Fluentd packaged and maintained by [Treasure Data, Inc.](https://www.treasure-data.com).

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
