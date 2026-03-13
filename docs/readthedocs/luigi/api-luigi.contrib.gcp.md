# luigi.contrib.gcp

Common code for GCP (google cloud services) integration

Functions

`get_authenticate_kwargs`([oauth_credentials, ...])

Returns a dictionary with keyword arguments for use with discovery

luigi.contrib.gcp.get_authenticate_kwargs(*oauth_credentials=None*, *http_=None*)

Returns a dictionary with keyword arguments for use with discovery

Prioritizes oauth_credentials or a http client provided by the user
If none provided, falls back to default credentials provided by google’s command line
utilities. If that also fails, tries using httplib2.Http()

Used by gcs.GCSClient and bigquery.BigQueryClient to initiate the API Client