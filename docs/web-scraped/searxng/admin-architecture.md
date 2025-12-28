# Source: https://docs.searxng.org/admin/architecture.html

[]

# Architecture[¶](#architecture "Link to this heading")

Further reading

-   Reverse Proxy: [[Apache]](installation-apache.html#apache-searxng-site) & [[nginx]](installation-nginx.html#nginx-searxng-site)

-   uWSGI: [[uWSGI]](installation-uwsgi.html#searxng-uwsgi)

-   SearXNG: [[Step by step installation]](installation-searxng.html#installation-basic)

Herein you will find some hints and suggestions about typical architectures of SearXNG infrastructures.

[]

## uWSGI Setup[¶](#uwsgi-setup "Link to this heading")

We start with a *reference* setup for public SearXNG instances which can be build up and maintained by the scripts from our [[DevOps tooling box]](../utils/index.html#toolboxing).

<figure id="id2" class="align-default">
<div class="highlight-default notranslate">
<div class="highlight">
<pre><code>digraph G ;
      rp -&gt; static  [label=&quot;optional: reverse proxy serves static files&quot;, fillcolor=slategray, fontcolor=slategray];
      rp -&gt; uwsgi [label=&quot;http:// (tcp) or unix:// (socket)&quot;];
      uwsgi -&gt; searxng1 -&gt; valkey;
      uwsgi -&gt; searxng2 -&gt; valkey;
      uwsgi -&gt; searxng3 -&gt; valkey;
      uwsgi -&gt; searxng4 -&gt; valkey;
  }

}</code></pre>
</div>
</div>
<figcaption><p><span class="caption-number">Fig. 2 </span><span class="caption-text">Reference architecture of a public SearXNG setup.</span><a href="#id2" class="headerlink" title="Link to this image">¶</a></p></figcaption>
</figure>

The reference installation activates [`server.limiter`] and [`server.image_proxy`] ([/etc/searxng/settings.yml](https://github.com/searxng/searxng/blob/master/utils/templates/etc/searxng/settings.yml))

    # SearXNG settings

    use_default_settings: true

    general:
      debug: false
      instance_name: "SearXNG"

    search:
      safe_search: 2
      autocomplete: 'duckduckgo'
      formats:
        - html

    server:
      # Is overwritten by $
      secret_key: "ultrasecretkey"
      limiter: true
      image_proxy: true
      # public URL of the instance, to ensure correct inbound links. Is overwritten
      # by $.
      # base_url: http://example.com/location

    valkey:
      # URL to connect valkey database. Is overwritten by $.
      url: valkey://localhost:6379/0