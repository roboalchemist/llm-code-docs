# Example – Top Artists

This is a very simplified case of something we do at Spotify a lot.
All user actions are logged to Google Cloud Storage (previously HDFS) where
we run a bunch of processing jobs to transform the data. The processing code itself is implemented
in a scalable data processing framework, such as Scio, Scalding, or Spark, but the jobs
are orchestrated with Luigi.
At some point we might end up with
a smaller data set that we can bulk ingest into Cassandra, Postgres, or
other storage suitable for serving or exploration.

For the purpose of this exercise, we want to aggregate all streams,
find the top 10 artists and then put the results into Postgres.

This example is also available in
examples/top_artists.py [https://github.com/spotify/luigi/blob/master/examples/top_artists.py].

## Step 1 - Aggregate Artist Streams

```
class AggregateArtists(luigi.Task):
    date_interval = luigi.DateIntervalParameter()

    def output(self):
        return luigi.LocalTarget("data/artist_streams_%s.tsv" % self.date_interval)

    def requires(self):
        return [Streams(date) for date in self.date_interval]

    def run(self):
        artist_count = defaultdict(int)

        for input in self.input():
            with input.open('r') as in_file:
                for line in in_file:
                    timestamp, artist, track = line.strip().split()
                    artist_count[artist] += 1

        with self.output().open('w') as out_file:
            for artist, count in artist_count.iteritems():
                print(artist, count, file=out_file)

```