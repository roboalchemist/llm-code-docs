# Source: https://buildkite.com/docs/agent/self-hosted/install/ubuntu.md

# Installing Buildkite agent on Ubuntu

The Buildkite agent is supported on Ubuntu versions 18.04 and above using our signed apt repository.

## Installation

First, add our signed apt repository. Buildkite agent versions come in three release channels:

- **Stable**: Thoroughly tested, production-ready releases recommended for most users.
- **Unstable/Beta**: Newer features that are still being tested, may contain bugs that affect stability.
- **Experimental**: Built directly from the `main` branch, may be incomplete or have unresolved issues.

The default version of the agent is `stable`. You can get the beta version by using `unstable` instead of `stable` or the experimental version by using `experimental` instead of `stable` in the installation commands that follow.

Start by downloading the Buildkite PGP key to a directory that is only writable by `root` (create the directory before running the following command if it doesn't already exist):

```shell
curl -fsSL https://keys.openpgp.org/vks/v1/by-fingerprint/32A37959C2FA5C3C99EFBC32A79206696452D198 | sudo gpg --dearmor -o /usr/share/keyrings/buildkite-agent-archive-keyring.gpg
```

> 📘 Is [keys.openpgp.org](https://keys.openpgp.org) down?
> If you get a 404 or other error from `curl` in the previous command, see the [Alternative keyservers](#alternative-keyservers) section.

Then add the signed source to your list of apt sources:

```shell
echo "deb [signed-by=/usr/share/keyrings/buildkite-agent-archive-keyring.gpg] https://apt.buildkite.com/buildkite-agent stable main" | sudo tee /etc/apt/sources.list.d/buildkite-agent.list
```

And install the Buildkite agent:

```shell
sudo apt-get update && sudo apt-get install -y buildkite-agent
```

Configure your [agent token](/docs/agent/self-hosted/tokens):

```shell
sudo sed -i "s/xxx/INSERT-YOUR-AGENT-TOKEN-HERE/g" /etc/buildkite-agent/buildkite-agent.cfg
```

And then start the agent:

```shell
sudo systemctl enable buildkite-agent && sudo systemctl start buildkite-agent
```

You can view the logs at:

```shell
sudo journalctl -f -u buildkite-agent
```

## Updating keys installed using apt-key

If you've previously installed keys using `apt-key`, move the Buildkite agent key from `/etc/apt/trusted.gpg` or `/etc/apt/trusted.gpg.d/` to `/usr/share/keyrings/buildkite-agent-archive-keyring.gpg`, making sure that both that file and directory are only writable by `root`.

Update your Buildkite agent entries in `/etc/apt/sources.list.d/buildkite-agent.list` to:

```shell
deb [signed-by=/usr/share/keyrings/buildkite-agent-archive-keyring.gpg] https://apt.buildkite.com/buildkite-agent stable main
```

## SSH key configuration

<p>SSH keys should be copied to (or generated into) <code>/var/lib/buildkite-agent/.ssh/</code>. For example, to generate a new private key which you can add to your source code host:</p>
<div class="highlight"><pre class="highlight shell"><code><span class="nv">$ </span><span class="nb">sudo </span>su buildkite-agent
<span class="nv">$ </span><span class="nb">mkdir</span> <span class="nt">-p</span> ~/.ssh <span class="o">&amp;&amp;</span> <span class="nb">cd</span> ~/.ssh
<span class="nv">$ </span>ssh-keygen <span class="nt">-t</span> rsa <span class="nt">-b</span> 4096 <span class="nt">-C</span> <span class="s2">"build@myorg.com"</span>
</code></pre></div>

See the [Buildkite agent code access](/docs/agent/self-hosted/code-access) documentation for more details.

## File locations

<ul>
<li>Configuration: <code>/etc/buildkite-agent/buildkite-agent.cfg</code>
</li>
<li>Agent Hooks: <code>/etc/buildkite-agent/hooks/</code>
</li>
<li>Builds: <code>/var/lib/buildkite-agent/builds/</code>
</li>
<li>Logs, depending on your system:

<ul>
<li>
<code>journalctl -f -u buildkite-agent</code> (systemd)</li>
<li>
<code>/var/log/upstart/buildkite-agent.log</code> (upstart)</li>
<li>
<code>/var/log/buildkite-agent.log</code> (older systems)</li>
</ul>
</li>
<li>Agent user home: <code>/var/lib/buildkite-agent/</code>
</li>
<li>SSH keys: <code>/var/lib/buildkite-agent/.ssh/</code>
</li>
</ul>

## Configuration

<p>The configuration file is located at <code>/etc/buildkite-agent/buildkite-agent.cfg</code>. See the <a href="/docs/agent/self-hosted/configure">configuration documentation</a> for an explanation of each configuration setting.</p>

## Default operating system user running the agent

On Ubuntu, the Buildkite agent runs as the `buildkite-agent` operating system user account.

You can override this default user through a [systemd modification](#systemd-modifications).

## Running multiple agents

<p>You can run as many parallel agent workers on the one machine as you wish with
the <code>spawn</code> configuration setting, or by passing the <code>--spawn</code> flag.</p>
<div class="highlight"><pre class="highlight ini"><code><span class="c"># Start 5 workers. Each one independently fetches and executes jobs.
</span><span class="py">spawn</span><span class="p">=</span><span class="s">5</span>
</code></pre></div>

## Upgrading

<p>The Buildkite agent can be upgraded like any other system package:</p>
<div class="highlight"><pre class="highlight shell"><code><span class="nb">sudo </span>apt-get update <span class="o">&amp;&amp;</span> apt-get upgrade
</code></pre></div>

## Alternative keyservers

<p>The PGP key used to sign the Buildkite agent package is also hosted on the following keyservers. Use these keyservers if the one in the installation instructions is down.</p>

<ul>
<li>
<p><a href="https://keyserver.ubuntu.com" class="external-link" target="_blank">keyserver.ubuntu.com</a></p>
<div class="highlight"><pre class="highlight shell"><code>curl <span class="nt">-fsSL</span> <span class="s1">'https://keyserver.ubuntu.com/pks/lookup?op=get&amp;search=0x32A37959C2FA5C3C99EFBC32A79206696452D198&amp;exact=on&amp;options=mr'</span> | <span class="nb">sudo </span>gpg <span class="nt">--dearmor</span> <span class="nt">-o</span> /usr/share/keyrings/buildkite-agent-archive-keyring.gpg
</code></pre></div>
</li>
<li>
<p><a href="https://pgp.mit.edu" class="external-link" target="_blank">pgp.mit.edu</a></p>
<div class="highlight"><pre class="highlight shell"><code>curl <span class="nt">-fsSL</span> <span class="s1">'https://pgp.mit.edu/pks/lookup?op=get&amp;search=0x32A37959C2FA5C3C99EFBC32A79206696452D198&amp;exact=on&amp;options=mr'</span> | <span class="nb">sudo </span>gpg <span class="nt">--dearmor</span> <span class="nt">-o</span> /usr/share/keyrings/buildkite-agent-archive-keyring.gpg
</code></pre></div>
</li>
</ul>

## Systemd modifications

<p>To override specific directives from the <code>buildkite-agent.service</code> systemd unit file, implement these configurations using the <em>drop-in</em> directory <code>/etc/systemd/system/buildkite-agent.service.d</code>. Within this directory, any files ending with <code>.conf</code> are merged in alphanumeric order and parsed after the main <code>buildkite-agent.service</code> unit file. Therefore, these <code>*.conf</code> files can be used to override or extend the directives of the <code>buildkite-agent.service</code> systemd unit file.</p>

<p>The following <code>.conf</code> file example overrides the operating system user account running the <code>buildkite-agent</code> service, and the environment variable for <code>HOME</code>:</p>
<figure class="highlight-figure"><figcaption>/etc/systemd/system/buildkite-agent.service.d/change-service-user.conf</figcaption><div class="highlight"><pre class="highlight conf"><code>[<span class="n">Service</span>]
<span class="c"># Run the buildite-agent service as a different user:
</span><span class="n">User</span>=<span class="n">my</span>-<span class="n">service</span>-<span class="n">account</span>
<span class="c"># Change the environment variable for HOME:
</span><span class="n">Environment</span>=<span class="n">HOME</span>=/<span class="n">opt</span>/<span class="n">my</span>-<span class="n">service</span>-<span class="n">account</span>
</code></pre></div></figure>
