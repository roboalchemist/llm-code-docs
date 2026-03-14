# Crate homebrew

Source

## Structs§

Brew`brew` 命令构造器Cask`Cask` 包的结构体Config`Config` 的结构体EnvFormula`Formula` 包的结构体Package运行 `brew info [name] --json=v2` 命令 `json` 结果反序列的结构体Service`Service` 的结构体ServiceInfo具体服务详情结构体

## Enums§

ServiceStatus

## Functions§

brew执行 `brew` 命令brew_spawn执行 `brew` 命令并实时输出信息cache执行 `brew --cache` 命令caskroom执行 `brew --caskroom` 命令cellar执行 `brew --cellar` 命令config执行 `brew config` 命令并得到结构体env执行 `brew --env --plain` 命令并得到结构体env_shell执行 `brew --env --shell=auto` 命令并得到 shell 文本info执行 `brew info {name} --json=v2` 命令info_all执行 `brew info --eval-all --json=v2` 命令install安装软件 `brew install [name]` 命令install_cask安装 `Cask` 软件 `brew install --cask [name]` 命令install_cask_spawn安装 `Cask` 软件 `brew install --cask [name]` 命令，并实时输出install_spawn安装软件 `brew install [name]` 命令，并实时输出list列举出 `brew` 安装的包列表，包含 `Cask` 和 `Formulae`list_cask列举出 `brew` 安装的包列表，只包含 `Cask`list_formulae列举出 `brew` 安装的包列表，只包含 `Formulae`prefix执行 `brew --prefix` 命令reinstall重新安装软件 `brew reinstall [name]` 命令reinstall_spawn重新安装软件 `brew reinstall [name]` 命令，并实时输出repository执行 `brew --repository` 命令search运行 `brew search [name]` 命令services列出所有服务，就像运行 `brew services`services_cleanup移除所有没用的服务，就像运行 `brew services cleanup`services_info查询服务详情，就像运行 `brew services info [name] --json`services_kill终止服务但保持自启动，就像运行 `brew services kill [name]`services_restart重启服务并注册自启动，就像运行 `brew services restart [name]`services_run启动服务但不注册自启动，就像运行 `brew services run [name]`services_start启动服务并注册自启动，就像运行 `brew services start [name]`services_stop停止服务并注销自启动，就像运行 `brew services stop [name]`uninstall卸载软件 `brew uninstall [name]` 命令update执行更新 `brew update` 命令update_spawn执行更新 `brew update` 命令并实时输出upgrade升级软件 `brew upgrade [name]` 命令upgrade_spawn升级软件 `brew upgrade [name]` 命令，并实时输出version执行 `brew --version` 命令
