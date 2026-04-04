# Source: https://ansible-book.gitbook.io/ansible-first-book/ansible-jin-jie/host-inventory-zhu-ji-qing-dan/an-mu-lu-jie-gou-cun-chu-bian-liang.md

# 按目录结构存储变量

假设inventory文件为/etc/ansible/hosts，那么相关的hosts和group变量可以放在下面的目录结构下

```
/etc/ansible/group_vars/raleigh # can optionally end in '.yml', '.yaml', or '.json'
/etc/ansible/group_vars/webservers
/etc/ansible/host_vars/foosball
```

/etc/ansible/group\_vars/raleigh 文件内容可以为

```
---
ntp_server: acme.example.org
database_server: storage.example.org
```

如果对应的名字为目录名，ansible会读取这个目录下面所有文件的内容

```
/etc/ansible/group_vars/raleigh/db_settings
/etc/ansible/group_vars/raleigh/cluster_settings
```

group\_vars/ 和 host\_vars/ 目录可放在 inventory 目录下,或是 playbook 目录下. 如果两个目录下都存在,那么 **playbook 目录下的配置**会**覆盖** inventory 目录的配置.
