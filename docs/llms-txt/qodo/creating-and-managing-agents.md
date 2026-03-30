# Source: https://docs.qodo.ai/qodo-documentation/qodo-command/features/creating-and-managing-agents.md

# Creating and Managing Agents

Create your own agent for Qodo CLI tool to use, then run Qodo with a customizable command.

## What is an Agent?

An agent is a configurable AI-powered assistant that can perform tasks, automate workflows, and interact with tools (MCPs). Each agent is defined by a set of instructions, optional arguments, and access to tools like version control, the file system, CI pipelines, or cloud environments.

Agents act as **task-specific operators**. You can think of them as highly focused copilots, each with a clear objective and strategy. Rather than manually guiding an AI through each step, you define the desired behavior once and reuse it reliably.

## Why Use Agents?

Using agents has several benefits:

* **Customization**: Define detailed instructions, tool access, and behavior tailored to your workflow.
* **Repeatability**: Agents behave consistently across runs, environments, and users.
* **Automation**: Agents can replace repetitive manual work: code reviews, testing, deployments, and more.
* **Collaboration**: Teams can share, version, and build on each other’s agents for unified engineering workflows.

Creating and running agents is like building a library of specialized assistants that enhance your development process.

***

## Getting Started

### Using an existing agent

You can use an existing agent configuration file with Qodo.

Run Qodo with the flag:

```bash
--agent-file=path/URL
```

Specify either a URL or the local path to the file to use it.

### **1. Create an agent file**

Before starting to use Qodo CLI tool, make sure you've [logged in to Qodo](https://app.qodo.ai/home).

In your project directory, create a new folder called `agents`.

Navigate into the `agents` directory and create a new file with the title of the command that will reference your agent: `<your-command-name-here>.toml`.

### **2. Customize your agent**

Follow the skeleton and customize your agent to your needs.\
You can set instructions, import existing agents configurations for your agent to use, and give it tools to utilize.

Customize your agent by providing attributes in your agent's TOML file, using the table below as a reference.

**Name your agent file after the command you want to use to run it.** This name should also appear in the file itself, under the `commands` section.

The fields of the agent file are:

<table><thead><tr><th width="243.9375">Field name</th><th width="157.63671875">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>description</code></td><td>string</td><td>Description of what your agent does.<br>This field is required when an agent is run with <code>--mcp</code>.</td></tr><tr><td><code>instructions</code></td><td>string</td><td>Required field.<br>Prompt for the AI models explailing the required behavior.</td></tr><tr><td><code>arguments</code></td><td>list of objects.<br><br>Supported types: <code>'string' | 'number' | 'boolean' | 'array' | 'object'</code></td><td><p>List of possible arguments that can be given to the agent.</p><p>The arguments will be translated and forwarded to MCP servers.</p></td></tr><tr><td><code>mcpServers</code></td><td>string</td><td>List of MCP servers used by the agent</td></tr><tr><td><code>tools</code></td><td>list</td><td>List of MCP server names. Allows you to filter specific MCP servers that can be used by your agent</td></tr><tr><td><code>execution_strategy</code></td><td>"act" or "plan"</td><td>Plan lets the agent think through a multi-step strategy, act executes actions immediately</td></tr><tr><td><code>output_schema</code></td><td>string</td><td>Valid json of the wanted agent output</td></tr><tr><td><code>exit_expression</code></td><td>string (<a href="https://jsonpath.com/">JSONPath</a>)</td><td>Only applicable when <code>output_schema</code> is given.<br>For CI runs, a condition used to determine if the agent run succeeded or failed.</td></tr></tbody></table>

### Example custom agent TOML file

```toml
# agent.toml
version = "1.0"
[commands.my_agent]
description = "Detailed description for users"
instructions = """
Your agent's behavior instructions here.
Be specific about the task and expected outcomes.
"""

# Optional: Define arguments
arguments = [
    { name = "input_file", type = "string", required = true, description = "Input file path" },
    { name = "threshold", type = "number", required = false, default = 0.8, description = "Quality threshold" }
]

# Optional: MCP servers your agent uses
mcpServers = """
{
    "shell": {
      "command": "uvx",
      "args": [
        "mcp-shell-server"
      ],
      "env": {
        "ALLOW_COMMANDS": "..."
      }
    },
    "github": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ]
    }
}
"""

# Optional: Define tools you'd like your agent to be able to use
tools = ["filesystem", "git", "shell", "github"]

# Optional: Define execution strategy: "plan" for multi-step, "act" for direct execution
execution_strategy = "act"

# Optional: Define expected output structure
output_schema = """
{
    "properties": {
        "success": {"type": "boolean"},
        "results": {"type": "array", "items": {"type": "string"}},
        "score": {"type": "number"}
    }
}
"""

# Optional: Success condition for CI/CD
exit_expression = "success"
```

### **3. Set output type**

You can give your agent a `json` schema to follow as its output.

If there’s no output schema given, your agent will output a textual summary as a reply for a query.

### **4. Create an `agent.toml` file**

At your project's root directory level, create a file called `agent.toml`. This file will hold all agent files that Qodo will know and be able to call.\
Example `agent.toml` file:

```toml
# Version of the agent configuration standard
version = "1.0"

model = "model-name"

imports = [
    "agents/explain.toml",
    "agents/review.toml",
    "agents/test_codebase.toml",
    ... # more agents
]
```

{% hint style="success" %}
You can add an `instructions` field to your `agent.toml` file to specify how the Qodo CLI tool should behave when it's not using a custom command, e.g. when it's running default commands like `chat`.

For example, adding an instruction like *“Reply in Japanese”* will make `qodo chat` respond in Japanese.
{% endhint %}

### 5. Add your agent to `agent.toml`

Add your newly created agent to the `agent.toml` file, under the `imports` section.

### 5. Use your agent

You can now run your agent by calling:

```bash
qodo <command_name>
```

***

## Use MCP Servers with your agents with the `mcp.json` file

You can define MCP servers to be used by your agents. This will make the MCP servers available to all agents you're configuring.

At your project's root directory level, create a file called `mcp.json`.

Once configured in the `mcp.json` file, the MCP servers can be mentioned under the `tools` section in your agent file to be used by your agent.

If you want a specific MCP server for your agent that doesn't need to be reused for other agents, you can define it in the specific agent configuration TOML file.

For example:

```json
{
  "mcpServers": {
    "shell": {
      "command": "uvx",
      "args": [
        "mcp-shell-server"
      ],
      "env": {
        "ALLOW_COMMANDS": "ls,cat,pwd,rg,wc,touch,find,mkdir,rm,cp,mv,chmod,head,tail,sort,uniq,cut,tr,sed,awk,grep,diff,which,whereis,file,stat,du,df,ps,kill,env,export,echo,printf,test,true,false,sleep,timeout,xargs,tee,yes,seq,date,basename,dirname,realpath,readlink,ln,tar,gzip,gunzip,zip,unzip,curl,wget,jq,yq,xmllint,git,npm,npx,yarn,pnpm,node,ts-node,tsc,deno,bun,python,python3,pip,pip3,poetry,pipenv,pytest,unittest,nose2,java,javac,junit,mvn,gradle,go,gofmt,gotest,cargo,rustc,rustfmt,ruby,gem,bundle,rake,rspec,php,composer,phpunit,dotnet,msbuild,nuget,make,cmake,ninja,gcc,g++,clang,clang++,ld,ar,objdump,nm,strip,gdb,lldb,valgrind,strace,ltrace,ldd,pkg-config,autoconf,automake,libtool,m4,flex,bison,perl,cpan,swift,swiftc,kotlin,kotlinc,scala,scalac,sbt,clojure,lein,elixir,mix,erlang,erl,escript,ghc,cabal,stack,runhaskell,ocaml,opam,dune,r,rscript,julia,lua,luac,tcl,tclsh,bash,sh,zsh,fish,csh,tcsh,dash,ksh,bc,dc,sqlite3,mysql,psql,redis-cli,mongo,elasticsearch,jest,mocha,jasmine,karma,cypress,playwright,selenium,webdriver,chromedriver,geckodriver,rspec,minitest,cucumber,behave,pytest,unittest,nose2,testng,junit,spock,scalatest,quickcheck,hspec,tasty,criterion,bench,ab,siege,wrk,hey,nmap,netstat,ss,lsof,iftop,htop,top,iostat,vmstat,free,uptime,uname,whoami,id,groups,sudo,su,chown,chgrp,umask,ulimit,nohup,screen,tmux,vim,nano,emacs,less,more,watch,tree,rsync,scp,ssh,telnet,ftp,sftp,ping,traceroute,dig,nslookup,host,whois,arp,route,ip,ifconfig,systemctl,service,crontab,at,batch,jobs,fg,bg,disown,history,alias,unalias,type,command,builtin,hash,help,man,info,apropos,whatis,locale,iconv,od,hexdump,xxd,strings,objcopy,readelf,size,strip,addr2line,c++filt,nm,ar,ranlib,ld,as,gprof,gcov,lcov,genhtml,cppcheck,clang-tidy,clang-format,astyle,indent,splint,lint,shellcheck,yamllint,eslint,tslint,pylint,flake8,black,isort,rubocop,gofmt,rustfmt,prettier,autopep8,yapf,standardjs,jshint,csslint,htmlhint,stylelint,commitizen,commitlint,husky,lint-staged,pre-commit,tox,nox,pipx,pyenv,rbenv,nvm,sdkman,kiex,kerl,rustup,gvm,tfenv,kubectl,helm,docker,docker-compose,podman,vagrant,terraform,ansible,packer,consul,vault,nomad,prometheus,grafana,jaeger,zipkin,opentelemetry,datadog,newrelic,sentry,rollbar,bugsnag,honeybadger,airbrake,raygun,loggly,splunk,elk,logstash,kibana,elasticsearch,fluentd,fluent-bit,rsyslog,syslog-ng,journalctl,dmesg,logrotate,cron,anacron,systemd,init,rc,service,chkconfig,update-rc.d,systemctl,launchctl,brew,apt,apt-get,yum,dnf,zypper,pacman,emerge,portage,pkg,pkgng,snap,flatpak,appimage,rpm,dpkg,alien,checkinstall,fpm,nfpm,goreleaser,electron-builder,pkg,nexe,vercel,netlify,heroku,aws,gcloud,az,kubectl,helm,istio,linkerd,envoy,nginx,apache,haproxy,traefik,caddy,lighttpd,tomcat,jetty,undertow,wildfly,glassfish,websphere,weblogic,iis,gunicorn,uwsgi,unicorn,puma,passenger,pm2,forever,nodemon,supervisor,circus,celery,rq,sidekiq,delayed_job,active_job,spring,hibernate,django,flask,fastapi,express,koa,hapi,restify,meteor,next,nuxt,gatsby,create-react-app,vue-cli,angular-cli,ember-cli,ionic,cordova,phonegap,react-native,flutter,xamarin,unity,unreal,godot,blender,gimp,imagemagick,ffmpeg,vlc,mplayer,sox,lame,flac,ogg,mp3,wav,avi,mp4,mkv,webm,gif,png,jpg,jpeg,svg,pdf,latex,pdflatex,xelatex,lualatex,bibtex,biber,makeindex,pandoc,markdown,rst,asciidoc,textile,creole,mediawiki,confluence,notion,obsidian,roam,logseq,zettlr,typora,mark,remarkable,ghostwriter,writemonkey,focuswriter,manuskript,scrivener,artoftext,ulysses,bear,day-one,journey,momento,diaro,grid-diary,five-minute-journal,stoic,calm,headspace,insight-timer,ten-percent-happier"
      }
    },
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
      "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

{% hint style="success" %}
For MCP Servers that require environment variables or tokens, add the `Authorization` field to their section in the `mcp.json` file.\
This allows you to keep your tokens hidden and secure while still utilizing these MCP Servers.
{% endhint %}

***

## Agent Modes

### MCP Server Mode: the `--mcp` flag

You can also run an agent as a tool server:

```bash
qodo <command_name> --mcp
```

This launches the agent as a service listening on port `3000`.

The service can be integrated with other AI tools or exposed via URL.

You can exit at any time by pressing `Escape`.

***

## Qodo and Community Agent Examples

Check out [Qodo's agent repository in GitHub](https://github.com/qodo-ai/agents) to see examples of working agents.
