# Source: https://docs.edgeimpulse.com/tools/clis/edge-impulse-cli/blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Blocks

The blocks CLI tool creates different blocks types that are used in organizational features such as:

* [Transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks) - to transform large sets of data efficiently.
* [Deployment blocks](/studio/organizations/custom-blocks/custom-deployment-blocks) - to build personalized firmware using your own data or to create custom libraries.
* [Custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks) - to create and host your custom signal processing techniques and use them directly in your projects.
* [Custom machine learning models](/studio/organizations/custom-blocks/custom-learning-blocks) - to use your custom neural network architectures and load pre-trained weights, with Keras, PyTorch and scikit-learn.

With the blocks CLI tool, you can create new blocks, run them locally, and push them to Edge Impulse infrastructure so we can host them for you. Edge Impulse blocks can be written in any language, and are based on Docker container for maximum flexibility.

As an example here, we will show how to create a transformation block.

You can create a new block by running:

```
$ edge-impulse-blocks init
? What is your user name or e-mail address (edgeimpulse.com)? jan@edgeimpulse.com
? What is your password? [hidden]
? In which organization do you want to create this block? EdgeImpulse Inc.
Attaching block to organization 'EdgeImpulse Inc.'
? Choose a type of block Transformation block
? Choose an option Create a new block
? Enter the name of your block Extract voice
? Enter the description of your block Extracts voice from video files
Creating block with config: {
  name: 'Extract voice',
  type: 'transform',
  description: 'Extracts voice from video files',
  organizationId: 4
}
? Would you like to download and load the example repository (Python)? yes
Template repository fetched!
Your new block 'Extract voice' has been created in '/Users/janjongboom/repos/custom-transform-block'.
When you have finished building your transformation block, run "edge-impulse-blocks push" to update the block in Edge Impulse.
```

When you're done developing the block you can push it to Edge Impulse via:

```
$ edge-impulse-blocks push
Archiving 'custom-transform-block'...
Archiving 'custom-transform-block' OK (2 KB)

Uploading block 'Extract voice' to organization 'EdgeImpulse Inc.'...
Uploading block 'Extract voice' to organization 'EdgeImpulse Inc.' OK

Building transformation block 'Extract voice'...
INFO[0000] Retrieving image manifest python:3.7.5-stretch
INFO[0000] Retrieving image python:3.7.5-stretch

...

Building transformation block 'Extract voice' OK

Your block has been updated, go to https://studio.edgeimpulse.com/organization/4/data to run a new transformation
```

The metadata about the block (which organization it belongs to, block ID) is saved in `.ei-block-config`, which you should commit. To view this data in a convenient format, run:

```
$ edge-impulse-blocks info
Name: TestDataItemTransform
Description: Data item transformation example
Organization ID: 1
Not pushed
Block type: transform
Operates on: dataitem
Bucket mount points:
    - ID: 1, Mount point: /path/to/bucket
```

### Block runner

Rather than only running custom blocks in the cloud, the `edge-impulse-blocks runner` command lets developers download, configure, and run custom blocks entirely on their local machine, making testing and development much faster. The options depend on the type of block being run, and they can be viewed by using the help menu:

```
$ edge-impulse-blocks runner -h
Usage: edge-impulse-blocks runner [options]
Run the current block locally
Options:
  --data-item <dataItem>          Tranformation block: Name of data item
  --file <filename>               File tranformation block: Name of file in data item
  --epochs <number>               Transfer learning: # of epochs to train
  --learning-rate <learningRate>  Transfer learning: Learning rate while training
  --validation-set-size <size>    Transfer learning: Size of validation set
  --input-shape <shape>           Transfer learning: List of axis dimensions. Example: "(1, 4, 2)"
  --download-data                 Transfer learning or deploy: Only download data and don't run the block
  --extra-args <args>             Pass extra arguments/options to the Docker container
  -h, --help                      display help for command
```

As seen above, the `runner` accepts a list of relevant option flags along with a variable number of extra arguments that get passed to the Docker container at runtime for extra flexibility. As an example, here is what happens when `edge-impulse-blocks runner` is used on a file transformation block:

```
$ edge-impulse-blocks runner --data-item item1 --file sample_1.cbor
Found data item item1 with id=1, metadata={}
Downloading file sample_1.cbor to /path/to/block/data/dataset_1/item1...
File downloaded
...
```

Best of all, the `runner` only downloads data when it isn't present locally, thus saving time and bandwidth.

```
$ edge-impulse-blocks runner --data-item item1 --file sample_1.cbor
Found data item item1 with id=1, metadata={}
File already present; skipping download...
...
```

### Block structure

Transformation blocks use Docker containers, a virtualization technique which lets developers package up an application with all dependencies in a single package. Thus, every block needs at least a `Dockerfile`. This is a file describing how to build the container that powers the block, and it has information about the dependencies for the block - like a list of Python packages your block needs. This `Dockerfile` needs to declare an `ENTRYPOINT`: a command that needs to run when the container starts.

An example of a Python container is:

```
FROM python:3.7.5-stretch

WORKDIR /app

# Python dependencies
COPY requirements.txt ./
RUN pip3 --no-cache-dir install -r requirements.txt

COPY . ./

ENTRYPOINT [ "python3",  "transform.py" ]
```

Which takes a base-image with Python 3.7.5, then installs all dependencies listed in `requirements.txt`, and finally starts a script called `transform.py`.

**Note:** Do not use a WORKDIR under /home! The /home path will be mounted in by Edge Impulse, making your files inaccessible.

**Note**: If you use a different programming language, make sure to use `ENTRYPOINT` to specify the application to execute, rather than `RUN` or `CMD`.

Besides your `Dockerfile` you'll also need the application files, in the example above `transform.py` and `requirements.txt`. You can place these in the same folder.

### Excluding files

When pushing a new block all files in your folder are archived and sent to Edge Impulse, where the container is built. You can exclude files by creating a file called `.ei-ignore` in the root folder of your block. You can either set absolute paths here, or use wildcards to exclude many files. For example:

```
a-large-folder/*
some-path-to-a-text-file.txt
```

#### Clearing configuration

To clear the configuration, run:

```
$ edge-impulse-blocks --clean
```

This resets the CLI configuration and will prompt you to log in again.

#### API Key

You can use an API key to authenticate with:

```
$ edge-impulse-blocks --api-key ei_...
```

Note that this resets the CLI configuration and automatically configures your organization.

#### Other options

* `--dev` - lists development servers, use in conjunction with `--clean`.


Built with [Mintlify](https://mintlify.com).