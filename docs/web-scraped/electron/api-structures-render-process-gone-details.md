# Source: https://www.electronjs.org/docs/latest/api/structures/render-process-gone-details

# RenderProcessGoneDetails Object

- `reason` string - The reason the render process is gone. Possible values:
  - `clean-exit` - Process exited with an exit code of zero
  - `abnormal-exit` - Process exited with a non-zero exit code
  - `killed` - Process was sent a SIGTERM or otherwise killed externally
  - `crashed` - Process crashed
  - `oom` - Process ran out of memory
  - `launch-failed` - Process never successfully launched
  - `integrity-failure` - Windows code integrity checks failed
  - `memory-eviction` - Process proactively terminated to prevent a future out-of-memory (OOM) situation
- `exitCode` Integer - The exit code of the process, unless `reason` is `launch-failed`, in which case `exitCode` will be a platform-specific launch failure error code.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/render-process-gone-details.md)