# Source: https://unsloth.ai/docs/fr/commencer/install/updating.md

# Source: https://unsloth.ai/docs/de/loslegen/install/updating.md

# Source: https://unsloth.ai/docs/jp/hajimeni/install/updating.md

# Source: https://unsloth.ai/docs/zh/kai-shi-shi-yong/install/updating.md

# Source: https://unsloth.ai/docs/get-started/install/updating.md

# Updating Unsloth

## Standard Updating (recommended):

```bash
pip install --upgrade unsloth unsloth_zoo
```

### Updating without dependency updates:

<pre class="language-bash" data-overflow="wrap"><code class="lang-bash">pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth
<strong>pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth_zoo
</strong></code></pre>

## To use an old version of Unsloth:

{% code overflow="wrap" %}

```bash
pip install --force-reinstall --no-cache-dir --no-deps unsloth==2025.1.5
```

{% endcode %}

'2025.1.5' is one of the previous old versions of Unsloth. Change it to a specific release listed on our [Github here](https://github.com/unslothai/unsloth/releases).
