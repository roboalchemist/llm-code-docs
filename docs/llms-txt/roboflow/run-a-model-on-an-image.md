# Source: https://docs.roboflow.com/developer/command-line-interface/run-a-model-on-an-image.md

# Run a Model on an Image

You can use the roboflow CLI to run a model trained on Roboflow, or with open source models available on [Roboflow Universe](https://universe.roboflow.com).

By running `roboflow infer` in the command line, the Roboflow CLI will be sending images to the Roboflow API and print the results (predictions) in JSON format.

Let's look at an example using an open source model from Roboflow Universe. This is the [poker-cards](https://universe.roboflow.com/roboflow-100/poker-cards-cxcvz/model/1) dataset - an open source Roboflow project that has a trained model capable of identifying poker cards.

From the URL in the browser:

* workspaceId="roboflow-100"
* projectId="poker-cards-cxcvz"
* version=1

Then if you have a local file with a card image you can run a command like

```
roboflow infer -c .70 -w roboflow-100 -m poker-cards-cxcvz/1 ~/Downloads/ace.jpg
```

And it's the same thing if you want to run inference with your own models. Just specify the workspace/project/version for a model that your user has access to.

See all the supported parameters with `roboflow infer --help`
