# Source: https://docs-v3.activeloop.ai/v3.4.1/enterprise-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/enterprise-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/enterprise-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/enterprise-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/enterprise-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/enterprise-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/enterprise-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/enterprise-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/performance-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/performance-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/performance-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/performance-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/performance-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/performance-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/performance-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/performance-features/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/examples/rag/managed-database/migrating-datasets-to-the-tensor-database.md

# Source: https://docs-v3.activeloop.ai/examples/rag/managed-database/migrating-datasets-to-the-tensor-database.md

# Migrating Datasets to the Tensor Database

## How to migrate existing Deep Lake datasets to the Tensor Database

Datasets are created in the Tensor Database by specifying the `dest = "hub://<org_id>/<dataset_name>"` and `runtime = {"tensor_db": True})` during dataset creation. If datasets are currently stored locally, in your cloud, or in non-database Activeloop storage, they can be migrated to the Tensor Database using:

<pre class="language-python"><code class="lang-python"><strong>import deeplake
</strong>
<strong>ds_tensor_db = deeplake.deepcopy(src = &#x3C;current_path>, 
</strong>                                 dest = "hub://&#x3C;org_id>/&#x3C;dataset_name>", 
                                 runtime = {"tensor_db": True}, 
                                 src_creds = {&#x3C;creds_dict>}, # Only necessary if src is in your cloud
                                 )
</code></pre>
