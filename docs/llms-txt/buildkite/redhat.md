# Source: https://buildkite.com/docs/agent/self-hosted/install/redhat.md

# Installing Buildkite agent on Red Hat Enterprise Linux, CentOS, and Amazon Linux

The Buildkite agent is supported on the following operating systems, using the yum repository:

- Red Hat Enterprise Linux
  - Red Hat Enterprise Linux 7 (RHEL7)
  - Red Hat Enterprise Linux 8 (RHEL8)
  - Red Hat Enterprise Linux 9 (RHEL9)
  - Red Hat Enterprise Linux 10 (RHEL10)
- CentOS
  - CentOS 7
  - CentOS 8
- Amazon Linux
  - Amazon Linux 2 (AL2)
  - Amazon Linux 2023 (AL2023)

## Installation

Start by adding the yum repository for your architecture (if unsure, run `uname -m` to find your system's architecture).

Buildkite agent versions come in three release channels:

- **Stable**: Thoroughly tested, production-ready releases recommended for most users.
- **Unstable/Beta**: Newer features that are still being tested, may contain bugs that affect stability.
- **Experimental**: Built directly from the `main` branch, may be incomplete or have unresolved issues.

The default version of the agent is `stable`. You can get the beta version by using `unstable` instead of `stable` or the experimental version by using `experimental` instead of `stable` in the installation commands that follow.

> 📘
> The `repo_gpgcheck=0` parameter is required when additional OS hardening has been enabled to verify the GPG signature of the repository's metadata. Without this extra parameter for disabling metadata signature checking, the package installation will not succeed.

For 64-bit (x86_64):

```shell
sudo sh -c 'echo -e "[buildkite-agent]\nname = Buildkite Pty Ltd\nbaseurl = https://yum.buildkite.com/buildkite-agent/stable/x86_64/\nenabled=1\ngpgcheck=0\nrepo_gpgcheck=0\npriority=1" > /etc/yum.repos.d/buildkite-agent.repo'
```

For 32-bit (i386):

```shell
sudo sh -c 'echo -e "[buildkite-agent]\nname = Buildkite Pty Ltd\nbaseurl = https://yum.buildkite.com/buildkite-agent/stable/i386/\nenabled=1\ngpgcheck=0\nrepo_gpgcheck=0\npriority=1" > /etc/yum.repos.d/buildkite-agent.repo'
```

For ARM 64-bit (aarch64):

```shell
sudo sh -c 'echo -e "[buildkite-agent]\nname = Buildkite Pty Ltd\nbaseurl = https://yum.buildkite.com/buildkite-agent/stable/aarch64/\nenabled=1\ngpgcheck=0\nrepo_gpgcheck=0\npriority=1" > /etc/yum.repos.d/buildkite-agent.repo'
```

Then install the agent:

```shell
sudo yum -y install buildkite-agent
```

Configure your [agent token](/docs/agent/self-hosted/tokens):

```shell
sudo sed -i "s/xxx/INSERT-YOUR-AGENT-TOKEN-HERE/g" /etc/buildkite-agent/buildkite-agent.cfg
```

After the installation, you can start the agent and tail the logs by using the following command:

```shell
sudo systemctl enable buildkite-agent && sudo systemctl start buildkite-agent
sudo tail -f /var/log/messages
```

## SSH key configuration

<p>SSH keys should be copied to (or generated into) <code>/var/lib/buildkite-agent/.ssh/</code>. For example, to generate a new private key which you can add to your source code host:</p>
<div class="highlight"><pre class="highlight shell"><code><span class="nv">$ </span><span class="nb">sudo </span>su buildkite-agent
<span class="nv">$ </span><span class="nb">mkdir</span> <span class="nt">-p</span> ~/.ssh <span class="o">&amp;&amp;</span> <span class="nb">cd</span> ~/.ssh
<span class="nv">$ </span>ssh-keygen <span class="nt">-t</span> rsa <span class="nt">-b</span> 4096 <span class="nt">-C</span> <span class="s2">"build@myorg.com"</span>
</code></pre></div>

See the [Buildkite agent code access](/docs/agent/self-hosted/code-access) documentation for more details.

## File locations

- Configuration: `/etc/buildkite-agent/buildkite-agent.cfg`
- Agent Hooks: `/etc/buildkite-agent/hooks/`
- Builds: `/var/buildkite-agent/builds/`
- Logs, depending on your system:
  - `journalctl -f -u buildkite-agent` (systemd)
  - `/var/log/buildkite-agent.log` (older systems)
- Agent user home: `/var/lib/buildkite-agent/`
- SSH keys: `/var/lib/buildkite-agent/.ssh/`

## Configuration

The configuration file is located at `/etc/buildkite-agent/buildkite-agent.cfg`. See the [configuration documentation](/docs/agent/self-hosted/configure) for an explanation of each configuration setting.

## Which user the agent runs as

On Red Hat, the Buildkite agent runs as user `buildkite-agent`.

## Running multiple agents

<p>You can run as many parallel agent workers on the one machine as you wish with
the <code>spawn</code> configuration setting, or by passing the <code>--spawn</code> flag.</p>
<div class="highlight"><pre class="highlight ini"><code><span class="c"># Start 5 workers. Each one independently fetches and executes jobs.
</span><span class="py">spawn</span><span class="p">=</span><span class="s">5</span>
</code></pre></div>

## Upgrading

```shell
sudo yum clean expire-cache && sudo yum update buildkite-agent
```

## Systemd modifications

<p>To override specific directives from the <code>buildkite-agent.service</code> systemd unit file, implement these configurations using the <em>drop-in</em> directory <code>/etc/systemd/system/buildkite-agent.service.d</code>. Within this directory, any files ending with <code>.conf</code> are merged in alphanumeric order and parsed after the main <code>buildkite-agent.service</code> unit file. Therefore, these <code>*.conf</code> files can be used to override or extend the directives of the <code>buildkite-agent.service</code> systemd unit file.</p>

<p>The following <code>.conf</code> file example overrides the operating system user account running the <code>buildkite-agent</code> service, and the environment variable for <code>HOME</code>:</p>
<figure class="highlight-figure"><figcaption>/etc/systemd/system/buildkite-agent.service.d/change-service-user.conf</figcaption><div class="highlight"><pre class="highlight conf"><code>[<span class="n">Service</span>]
<span class="c"># Run the buildite-agent service as a different user:
</span><span class="n">User</span>=<span class="n">my</span>-<span class="n">service</span>-<span class="n">account</span>
<span class="c"># Change the environment variable for HOME:
</span><span class="n">Environment</span>=<span class="n">HOME</span>=/<span class="n">opt</span>/<span class="n">my</span>-<span class="n">service</span>-<span class="n">account</span>
</code></pre></div></figure>
