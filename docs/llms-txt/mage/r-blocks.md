# Source: https://docs.mage.ai/guides/blocks/r-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# R blocks

> You can write R language to transform data in blocks.

## Requirements

<Warning>
  R blocks are only supported when running Mage using [Docker](/getting-started/setup#using-docker).
</Warning>

## Add R block to pipeline

1. Create a new pipeline or open an existing pipeline.
2. Add a data loader, transformer, or data exporter block.
3. Select `R`.

## Example pipeline

1. Data loader
   ```R  theme={"system"}
   load_data <- function() {
       # Specify your data loading logic here
       # Return value: loaded dataframe
       df <- read.csv(url('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'))
       df
   }
   ```
2. Transformer
   ```R  theme={"system"}
   library("pacman")
   p_load(dplyr)

   transform <- function(df_1, ...) {
       # Specify your transformation logic here
       # Return value: transformed dataframe.
       df_1 <- filter(df_1, Pclass < 3)
       df_1
   }
   ```
3. Data exporter
   ```R  theme={"system"}
   export_data <- function(df_1, ...) {
       # Specify your data exporting logic here
       # Return value: exported dataframe
       write.csv(df_1, "titanic_filtered.csv", row.names = FALSE)
   }
   ```

## Install R packages

Add the following at the start of your code in your R block:

```R  theme={"system"}
pacman::p_load(package1, package2, package3)
```

Or

```R  theme={"system"}
library("pacman")
p_load(dplyr)
```

> Note
>
> When you run the R block for the 1st time, the package will be installed.
> The 2nd time you run the R block, the package won’t need to be installed again.

### What is `pacman`?

`pacman` is an R package management tool. You can use `p_library()` to view all the available packages.

Here is the documentation for `pacman` where you can find more useful methods: [https://www.rdocumentation.org/packages/pacman/versions/0.5.1](https://www.rdocumentation.org/packages/pacman/versions/0.5.1)

## Runtime variables

Runtime variables can be accessed via `global_vars` vector, like `global_vars['execution_date']`.

Example code:

```R  theme={"system"}
load_data <- function() {
    df <- read.csv(file='titanic_clean.csv')
    df['date'] <- global_vars['execution_date']
    df
}
```


Built with [Mintlify](https://mintlify.com).