# Source: https://docs.statsig.com/statsig-warehouse-native/geotests/geotests-setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Started with Geotests

This guide walks you through creating a Geotest experiment using Statsig. The steps include:

1. Define your Geo Types
2. Configure your Metric Source
3. Create and Configure
4. Evaluate Design Options
5. Run Analysis

## Define your Geo Types

First decide on one more geo types relevant to your business. Some of the most common are Postal Codes and DMAs (Designated Market Areas), but Statsig allows you to define any arbitrary geo type you'd like.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/geotests/geo_types_settings.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=a6bd10c949185895c6413a0c83f5a4e6" alt="Geo types configuration interface" width="2162" height="1036" data-path="images/geotests/geo_types_settings.png" />
</Frame>

## Configure your Metric Source

Assuming you've already added a [metric source](/statsig-warehouse-native/configuration/metric-sources/) to Statsig, you can next indicate which column(s) represent the geo type(s) you've created.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/geotests/geo_column_mapping.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=715e0c63255849b8b9e994918c3034dc" alt="Geo column mapping configuration screen" width="1714" height="324" data-path="images/geotests/geo_column_mapping.png" />
</Frame>

## Create and Configure

* Navigate to your Experiments page.
* Click the + Create button.
* In the modal, select Analyze to analyze existing experiment data in your warehouse.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/_khyYmU0j-x2L_bX/images/geotests/CreateXP.png?fit=max&auto=format&n=_khyYmU0j-x2L_bX&q=85&s=28c1a4488ad3db8882c54ffe6ccc6012" alt="Experiment creation modal with analyze option" width="1113" height="741" data-path="images/geotests/CreateXP.png" />
</Frame>

* Enter a name and description for your experiment.
* Choose Geotest as the experiment type from the dropdown. Fill in the remaining info as you usually would

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/_khyYmU0j-x2L_bX/images/geotests/SetType.png?fit=max&auto=format&n=_khyYmU0j-x2L_bX&q=85&s=ed590faccf61b8a3ad6ee5d21681fcbc" alt="Geotest experiment type selection dropdown" width="1332" height="782" data-path="images/geotests/SetType.png" />
</Frame>

In the Setup tab:

* Define your hypothesis.
* Set the Geo Type (e.g., country\_id) from one of the types you've defined in your project and metric sources
* Choose your Primary Metrics.

<Note>
  **Important Metric Types**

  GeoTest metrics are currently limited to SUM, COUNT, and COUNT\_DISTINCT types. This limitation is driven by the inference techniques involved in synthetic control methodologies.
</Note>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/geotests/SetupXP.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=ce9d364632faca2d8cbef006fdaff57f" alt="Geotest experiment setup configuration screen" width="1323" height="1086" data-path="images/geotests/SetupXP.png" />
</Frame>

Configure:

* Expected Treatment Start/End Dates
* Pre-treatment duration (days)
* Desired Effect Size % (this is the MDE you're hoping to measure; smaller MDEs will make finding a valid design harder)
* Type of Test: 1-sided or 2-sided
* Alpha level (desired type I error rate, inverse of Significance)
* Optionally enable Budgeting
* Additional advanced modeling parameters for users familiar with [Geolift's Advanced API](https://github.com/facebookincubator/GeoLift/blob/main/R/pre_test_power.R)

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/UuyObWFVsFwVo6-M/images/geotests/XPAdvancedConfigs.png?fit=max&auto=format&n=UuyObWFVsFwVo6-M&q=85&s=4d42cb842caa1f769f3205ac3ca632f6" alt="Experiment configuration settings interface" width="1610" height="675" data-path="images/geotests/XPAdvancedConfigs.png" />
</Frame>

## Generate Design Options

When you're happy with your initial settings, click "Use Experiment Designer" to begin to design process.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/geotests/StartDesigner.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=262f305d90166239f7ede5fa7a0ced16" alt="Experiment designer launch button" width="1317" height="269" data-path="images/geotests/StartDesigner.png" />
</Frame>

The Experiment Designer automates the process of evaluating potential splits of geos. Creating a new design set involves 3 steps:

1. **Define your targeting**
2. **Set any Inclusion or Exclusion overrides**
3. **Define your date range**

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/_khyYmU0j-x2L_bX/images/geotests/CreateDesign.png?fit=max&auto=format&n=_khyYmU0j-x2L_bX&q=85&s=3034f988955ec013031dcefb70a5dd80" alt="Geographic limitations configuration interface" width="1399" height="1055" data-path="images/geotests/CreateDesign.png" />
</Frame>

### Define Targeting

Targeting allows you to define the set of geos potentially eligible to be included in your experiment. By default it pulls the unique set of geo types from your metric source from the last 90 days. You can add additional custom filters that help you filter your geos down, based on columns in your metric source. For example, you can filter geos to those in a certain region or by transactions that occurred in a certain language.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/geotests/targeting.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=8dee0fa42a183cf282e3e5dab21b37dd" alt="Geotest targeting filters for eligible regions" width="744" height="547" data-path="images/geotests/targeting.png" />
</Frame>

You can also manually specify a set of geos yourself. The geo id types must match those in your metric source exactly.

### Set Inclusion or Exclusion Overrides

After defining your targeting set, you can manually overwrite any of these geos into treatment or control groups as desired.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/geotests/targetingoverwrites.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=361ba66ce375ddad824bd94ebe6cd57e" alt="Override interface assigning specific geos to treatment or control" width="1405" height="447" data-path="images/geotests/targetingoverwrites.png" />
</Frame>

For example, when testing if a new marketing campaign is effective, you might know that you want include the city of Austin because a contract has already been signed. And you might know that you do not want to launch in New York, Los Angeles, or Washington D.C. because of local regulations. You can specify these constraints on the designer and it will ensure that all design options considered will conform to these rules.

### Define Date Range

Lastly, you must define the data range of your design dataset. This date range defines what data gets pulled as historical baseline to train a synthetic control model. In general, a good rule of thump is that you design data duration should be at least 4x the expected duration of your treatment period in order to achieve good fits and maximize sensitivity and power of your experiments.

### Advanced Options

* **Rolling Lookback Windows:** Control how many iterative simulations should be done to evaluate power. For instance, a value equal to 5 would simulate power for the last five possible tests in the date range. Corresponds to `lookback_window` in the GeoLift API.

* **Dynamic Time Warping:** Control how much the synthetic control model depends on auto-correlations in the metric vs. correlations between different geos on the same days. A value of 1 focuses exclusively on the metric while a value of 0 (default) relies on correlations only. Corresponds to `dtw` in the GeoLift API.

* **Control Cell Size Requirements:** Sets limits on the share of primary metric value from geos in any considered control group. If not set, all design options will be analyzed regardless of their size. For example, if designing on a Revenue metric, a control size range of \[50%, 90%] would mean that only design options where 50% to 90% of revenue was in the designated control geos. Corresponds to `holdout` in the GeoLift API.

## Evaluate Design Options

Once a Design Option Set has been created (usually takes a few minutes), it will be shown in your Experiment Designs tab. All design option sets generated are shown here, enabling you to look through prior design iterations as needed.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/_khyYmU0j-x2L_bX/images/geotests/DesignerOptions.png?fit=max&auto=format&n=_khyYmU0j-x2L_bX&q=85&s=e214347b774ba8d33f5c0677f088e394" alt="Experiment designer options display" width="1404" height="508" data-path="images/geotests/DesignerOptions.png" />
</Frame>

Click into a completed design set (e.g. “Design Set 3”).

* Review the ranked recommendations for your best design options
* Compare MDE, Power, Cost and Control/Test Allocation
* Click View Cell Details to expand and see specific geo assignments
* See additional model performance details
* Select your desired design using the radio button, and clicking **Save Design to Experiment**.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/_khyYmU0j-x2L_bX/images/geotests/DesignOption.png?fit=max&auto=format&n=_khyYmU0j-x2L_bX&q=85&s=27f825e5ae665c3fe8201f0e07874e62" alt="Design option selection interface" width="1390" height="1169" data-path="images/geotests/DesignOption.png" />
</Frame>

## Run Analysis

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/_khyYmU0j-x2L_bX/images/geotests/AnalysisResults.png?fit=max&auto=format&n=_khyYmU0j-x2L_bX&q=85&s=ac5aef1bf45010fca855f6c5a7b252a3" alt="Geotest analysis results dashboard" width="1405" height="774" data-path="images/geotests/AnalysisResults.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).