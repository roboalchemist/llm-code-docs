# Source: https://docs.kedro.org/en/stable/tutorials/spaceflights_tutorial/index.md

# Next steps: spaceflights tutorial

In this tutorial, we construct nodes and pipelines for a price-prediction model to illustrate the steps of a typical Kedro workflow.

The tutorial takes about **30 minutes** to complete. You will work in the terminal and by inspecting project files in an IDE or text editor. There is no Jupyter notebook for the project.

*It is 2160, and the space tourism industry is booming. Globally, thousands of space shuttle companies take tourists to the Moon and back. You have been able to source data that lists the amenities offered in each space shuttle, customer reviews, and company information.*

***Project***: *You want to construct a model that predicts the price for each trip to the Moon and the corresponding return flight.*

## Tutorial steps

- [Tutorial Template](https://docs.kedro.org/en/stable/tutorials/tutorial_template/index.md)
- [Set Up Data](https://docs.kedro.org/en/stable/tutorials/set_up_data/index.md)
- [Create a Pipeline](https://docs.kedro.org/en/stable/tutorials/create_a_pipeline/index.md)
- [Add Another Pipeline](https://docs.kedro.org/en/stable/tutorials/add_another_pipeline/index.md)
- [Test a Project](https://docs.kedro.org/en/stable/tutorials/test_a_project/index.md)
- [Package a Project](https://docs.kedro.org/en/stable/deploy/package_a_project/index.md)
- [Spaceflights Tutorial FAQs](https://docs.kedro.org/en/stable/tutorials/spaceflights_tutorial_faqs/index.md)

Photo by [Ivan Diaz](https://unsplash.com/@ivvndiaz) on [Unsplash](https://unsplash.com/s/photos/spaceship)

## Watch the video

## Get help

If you encounter an issue with the tutorial:

- Check the [spaceflights tutorial FAQ](https://docs.kedro.org/en/stable/tutorials/spaceflights_tutorial_faqs/index.md) to see if we have answered the question already.
- Use [Kedro-Viz](https://docs.kedro.org/projects/kedro-viz/en/stable/) to visualise your project and better understand how the datasets, nodes, and pipelines fit together.
- Use the [#questions channel](https://slack.kedro.org/) on our Slack channel to ask the community for help.
- Search the [searchable archive of Slack discussions](https://linen-slack.kedro.org/).

## Terminology

We explain any Kedro-specific terminology as we introduce it, and further information can be found in the [glossary](https://docs.kedro.org/en/stable/getting-started/glossary/index.md). Some additional terminology may not be familiar to some readers, such as the concepts below.

### Project root directory

Also known as the "root directory," this is the parent folder for the entire project. It is the top-level folder that contains all other files and directories associated with the project.

### Dependencies

These are Python packages or libraries that an individual project depends upon to complete a task. For example, the Spaceflights tutorial project depends on the [scikit-learn](https://scikit-learn.org/stable/) library.

### Standard development workflow

When you build a Kedro project, you will typically follow a standard development workflow:

1. **Set up the project template**

   - Create a new project and install project dependencies.
   - Configure credentials and any other sensitive/personal content, and logging.

1. **Set up the data**

   - Add data to the `data` folder.
   - Reference all datasets for the project.

1. **Create the pipeline**

   - Construct nodes to make up the pipeline.
   - Choose how to run the pipeline: sequentially or in parallel.

1. **Package the project**

   - Build the project documentation.
   - Package the project for distribution.
