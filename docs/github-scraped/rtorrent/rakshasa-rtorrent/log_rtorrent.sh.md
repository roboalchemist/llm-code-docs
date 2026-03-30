# log_rtorrent.sh

```bash
#!/bin/bash
args=($@)
echo "${args[@]:1}" >> $1
```
