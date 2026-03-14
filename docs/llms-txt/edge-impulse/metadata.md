# Source: https://docs.edgeimpulse.com/studio/projects/data-acquisition/metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metadata

You can add arbitrary metadata to data items. You can use this for example to track on which site data was collected, where data was imported from, or where the machine that generated the data was placed. Some key use cases for metadata are:

1. Prevent leaking data between your train and validation set. See: [Using metadata to control your train/validation split](/studio/projects/data-acquisition/metadata#using-metadata-to-control-your-train-validation-split) below.
2. Synchronisation actions in [data pipelines](/studio/organizations/data-pipelines), for example to remove data in a project if the source data was deleted in the cloud.
3. Get a better understanding of real-world accuracy by seeing how well your model performs when grouped by a metadata key. E.g. whether data on site A performs better than site B.

### Viewing and editing metadata in the Studio

Metadata is shown on **Data acquisition** when you click on a data item. From here you can add, edit and remove metadata keys.

<Frame caption="Metadata shown on Data acquisition">
  <img src="https://mintcdn.com/edgeimpulse/ZGbvQAs-QNgkltKA/.assets/images/viewing-editing-metadata.png?fit=max&auto=format&n=ZGbvQAs-QNgkltKA&q=85&s=64dd57e57e07af6c28b7b3866ed15096" width="1587" height="1000" data-path=".assets/images/viewing-editing-metadata.png" />
</Frame>

### Adding metadata when adding data

It's pretty unpractical to manually add metadata to each data item, so the easiest way is to add metadata when you upload data. You can do this either by:

1. Providing an [info file](/tools/clis/edge-impulse-cli/uploader#custom-labeling-and-metadata) file when uploading data (this works both in the CLI and in the Studio).
2. Setting the `x-metadata` header to a JSON string when calling the ingestion service:

```
curl -X POST \
     -H "x-api-key: ei_238fae..." \
     -H "x-label: car" \
     -H "x-metadata: '{\"site\":\"Paris\"}' \
     -H "Content-Type: multipart/form-data" \
     -F "data=@one.png" \
     https://ingestion.edgeimpulse.com/api/training/files
```

### Reading and writing metadata through the API

You can read samples, including their metadata via the [List samples](/apis/studio/raw-data/list-samples) API call, and then use the [Set sample metadata](/apis/studio/raw-data/set-sample-metadata) API to update the metadata. For example, this is how you add a metadata field to the first data sample in your project using the [Python API Bindings](/tutorials/tools/api-bindings/studio/python/use-python-api-bindings):

```python  theme={"system"}
import edgeimpulse_api as ei

# update project ID / API Key
EI_PROJECT_ID = 1
EI_API_KEY = "ei_8b8..."

# instantiate the API client
configuration = ei.Configuration()
configuration.api_key["ApiKeyAuthentication"] = EI_API_KEY

api = ei.ApiClient(configuration)
raw_data = ei.RawDataApi(api)

# fetch the first page of data
samples = raw_data.list_samples(project_id=EI_PROJECT_ID, category='training', offset=0, limit=20)

# grab the current metadata
metadata = samples.samples[0].metadata
print('first sample metadata is', metadata)

# add an extra key
metadata = metadata if metadata else {}
metadata['hello'] = 'world'

# update metadata
raw_data.set_sample_metadata(project_id=EI_PROJECT_ID,
                             sample_id=samples.samples[0].id,
                             set_sample_metadata_request=ei.SetSampleMetadataRequest(metadata=metadata))
print('updated metadata!')

```

### Using metadata to control your train validation split

When training an ML model we split your data into a train and a validation set. This is done so that during training you can evaluate whether your model works on data that it has seen before (train set) and on data that it has never seen before (validation set) - ideally your model performs similarly well on both data sets: a sign that your model will perform well in the field on completely novel data.

However, this can give a false sense of security if data that is very similar ends up in both your train and validation set ("data leakage"). For example:

* You split a video into individual frames. These images don't differ much from frame to frame; and you don't want some frames in the train, and some in the validation set.
* You're building a sleep staging algorithm, and look at 30 second windows. From window to window the data for one person will look similar, so you don't want one window in the train, another in the validation set for the same person in the same night.

By default we split your training data randomly in a train and validation set (80/20 split) - which does not prevent data leakage, but if you tag your data items with metadata you can avoid this. To do so:

1. Tag all your data items with metadata.
2. Go to any ML block and under *Advanced training settings* set 'Split train/validation set on metadata key' to a metadata key (f.e. `video_file`).

   <Frame caption="Controlling the train/validation split with a metadata key">
     <img src="https://mintcdn.com/edgeimpulse/ydYuX7QIsmo2tzb8/.assets/images/using-metadata-to-control-train-val-split.png?fit=max&auto=format&n=ydYuX7QIsmo2tzb8&q=85&s=50ca3fbae0decb06998baa98b35f6898" width="1260" height="488" data-path=".assets/images/using-metadata-to-control-train-val-split.png" />
   </Frame>

Now every data item with the same *metadata value* for `video_file` will always be grouped together in either the train or the validation set; so no more data leakage.


Built with [Mintlify](https://mintlify.com).