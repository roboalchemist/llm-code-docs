Write the F****** Manual

Topic: $ARGUMENTS

Use the `llm-code-docs-agent` to add documentation for this topic to ~/github/llm-code-docs/

If no topic specified, infer from the current conversation context or the project folder (check package.json, pyproject.toml, go.mod, etc.).


## Steps

1. Check if llms.txt exists:
1.1 Use the find-llms-txt.sh script to probe common locations:
```bash
~/github/llm-code-docs/scripts/find-llms-txt.sh <domain>
```
This checks subdomains (www, docs, developers, api, dev) and paths (/llms.txt, /llms-full.txt, /docs/llms.txt, /.well-known/llms.txt)

1.2 If not found, try Perplexity to search for llms.txt
1.3 If still not found, try Tavily to search for llms.txt

2. If llms.txt exists, add to `scripts/llms-sites.yaml` and run:
```bash
python3 scripts/llms-txt-scraper.py --site <name>
```

3. If no llms.txt, create a scraper in `scripts/<name>-docs.py` based on `scripts/ntfy-docs.py`

4. Update index, commit, and push:
```bash
python3 scripts/update-index.py
git add . && git commit -m "Add <name> documentation"
git push
```

