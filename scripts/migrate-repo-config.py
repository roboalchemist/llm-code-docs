import yaml
import re

with open('scripts/repo_config.yaml') as f:
    content = f.read()

# Transform: docs/github-scraped/X -> docs/X/github/
new_content = re.sub(
    r'target_folder: docs/github-scraped/(\S+)',
    lambda m: f'target_folder: docs/{m.group(1)}/github/',
    content
)

with open('scripts/repo_config.yaml', 'w') as f:
    f.write(new_content)

# Verify YAML is still valid
yaml.safe_load(open('scripts/repo_config.yaml'))
print('OK')
