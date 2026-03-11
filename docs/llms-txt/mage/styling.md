# Source: https://docs.mage.ai/contributing/styling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Styling

```
eslint_d --fix --ext .js,.jsx,.ts,.tsx
git status --porcelain | grep '^[AM?]' | cut -c4- | grep '\.py$' | xargs black
git diff --name-status master | grep '^[AM?]' | awk '{$1=""; sub("^[ \t]+", ""); print}' | grep '\.\(js\|jsx\|ts\|tsx\)$' | xargs eslint_d --config mage_ai/frontend/.eslintrc.js --fix --ext .js,.jsx,.ts,.tsx
```


Built with [Mintlify](https://mintlify.com).