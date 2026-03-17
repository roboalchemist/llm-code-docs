# Source: https://docs.roboflow.com/developer/python-sdk/train-a-model.md

# Train a Model

You can start a training job either in the Roboflow platform or using the Python SDK, using the instructions below.

{% tabs %}
{% tab title="Python SDK" %}
To schedule a training job via the Python SDK, use the `train()` method on the version of your dataset for which you would like to train your model. **Note:** this code initiates training on the Roboflow platform asynchronously, and the code will finish executing before training completes.

<pre class="language-python"><code class="lang-python"><strong>import roboflow
</strong>
rf = roboflow.Roboflow(api_key=YOUR_API_KEY_HERE)

# List all projects for your workspace
workspace = rf.workspace()

# get a project
project = rf.workspace().project("PROJECT_ID")

# Create a new version with custom preprocessing and augmentation
new_version = project.generate_version({
    "preprocessing": {
        "auto-orient": True,
        "resize": {"width": 640, "height": 640, "format": "Stretch to"},
        "grayscale": False
    },
    "augmentation": {
    }
})
version = project.version(new_version)

# Train on the version with specific training parameters
model = version.train(
    model_type="rfdetr-nano", # Choose a model to train on. To see full list pass a invalid value like 'invalid'
    checkpoint=None,       # Use a specific checkpoint to continue training
    plot_in_notebook=False # Visualize training progress (for notebooks)
)
</code></pre>

{% endtab %}
{% endtabs %}
