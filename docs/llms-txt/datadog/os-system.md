# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/os-system.md

---
title: Command execution without sanitization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Command execution without sanitization
---

# Command execution without sanitization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/os-system`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

Detect unsafe shell execution with the `os` module. We should ensure the command is safe before execution. Use `shlex` to sanitize user inputs.

#### Learn More{% #learn-more %}

- [Python `os.system()` documentation](https://docs.python.org/3/library/os.html#os.system)
- [`Python shlex() module`](https://docs.python.org/3/library/shlex.html)
- [CWE 78 - Improper Neutralization of Special Elements used in an OS Command](https://cwe.mitre.org/data/definitions/78.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
os.system(f'mv {saved_file_path} {public_upload_file_path}')
```

```python
command = f'convert "{temp_upload_file_path}" -resize 50% "{resized_image_path}"'
os.system(command)


command2 = f'convert "{temp_upload_file_path}" -resize 50% "{resized_image_path}"'
os.system(command4)
```

```python
import os

directory = "/tmp"

# Use of unsanitized data to execute a process
os.system("/bin/ls")
os.system("/bin/ls " + directory)


os.system(f'mv {saved_file_path} {public_upload_file_path}')


def file_upload_api(request, app):
    file = request.files['file']

    if not _validate_file(file.filename):
        return {
            'message': 'Invalid file extension',
            'allowed_ext': ALLOWED_EXTENSIONS,
            'filename': file.filename
        }, 422

    saved_file_result = _save_temp_file(file, app)
    saved_file_path = saved_file_result['saved_path']

    file_name = Path(saved_file_path).name

    public_upload_file_path = os.path.join(app.config['PUBLIC_UPLOAD_FOLDER'], file_name)

    os.system(f'mv {saved_file_path} {public_upload_file_path}')

    return render_template('file_upload.html', file_url=f'{get_uploads_folder_url()}/{file_name}')
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import os
import shlex

# Use of shlex() to sanitize data
os.system(shlex.escape("/bin/ls"))
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
