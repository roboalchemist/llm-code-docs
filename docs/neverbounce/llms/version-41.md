# Source: https://developers.neverbounce.com/changelog/version-41.md

# Version 4.1

## Hybrid

Several months ago we began rolling out Hybrid, the unification of our industry leading real-time verification with historical-driven intelligence. By utilizing billions of third-party data points, Hybrid allows NeverBounce to respond with verification results at unprecedented levels of speed and accuracy. It’s our latest step in our ongoing mission to eradicate accept-all and unknown emails.

To get the benefits of Hybrid, no changes are needed to use it today. Hybrid is currently being used for all verifications being sent to NeverBounce. However, we recognize some users will want more transparency and control over the Hybrid algorithm, which is why we've launched Version 4.1 of our API.

## New Verification Flags

We've added new verification flags to indicate when the verification result is generated using historical data. These are present in the `v4.1/single/check` and `v4.1/jobs/results` endpoints.

* historical\_response

## Hybrid Control Endpoints

We've introduced a new parameter for the `v4.1/single/check` and `v4.1/jobs/create`  endpoints to disable historical-driven results. This will force the algorithm to use the classic real-time verification we've always had.

This is done with our new `request_meta_data` request parameter.

```shell Single w/o Historical
curl --request POST\
  --url https://api.neverbounce.com/v4/single/check?key={api_key}&email={email}&request_meta_data[leverage_historical_data]=0
```

```shell Job Create w/o Historical
curl --request POST\
  --url https://api.neverbounce.com/v4/jobs/create\
  --data key={api_key}\
  --data input_location='remote_url'\
  --data filename='SampleNeverBounceAPI.csv'\
  --data auto_parse=1\
  --data auto_start=1\
  --data input='https://mydomain.com/my_file.csv'\
  --data request_meta_data[leverage_historical_data]=0
```