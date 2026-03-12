# Source: https://developers.make.com/custom-apps-documentation/component-blocks/scope.md

# Scope

## Specification

Different modules require different scopes. This helps you control the permissions of every account. If the service supports OAuth scopes, you should set corresponding scopes for each module you write.

Scope is an array value that is required to complete the request with a list of scopes successfully.

{% tabs %}
{% tab title="Code" %}

<pre class="language-json"><code class="lang-json"><strong>[
</strong>	"identify",
	"users:read"
]
</code></pre>

{% endtab %}
{% endtabs %}

If a module uses RPCs that require particular scopes, the scopes should be listed in the module too.

## Extend scopes

When a module requires a scope that wasn't required elsewhere previously, a dialog for extending permissions will appear.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c423753abd0e93eb25f2f9691fa09894b567bfd2%2Fextend_scopes.png?alt=media" alt="" width="255"><figcaption></figcaption></figure></div>
