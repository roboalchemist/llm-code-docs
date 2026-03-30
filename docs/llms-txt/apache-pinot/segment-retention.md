# Source: https://docs.pinot.apache.org/release-1.2.0/basics/concepts/components/table/segment/segment-retention.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/concepts/components/table/segment/segment-retention.md

# Source: https://docs.pinot.apache.org/release-1.4.0/basics/concepts/components/table/segment/segment-retention.md

# Source: https://docs.pinot.apache.org/basics/concepts/components/table/segment/segment-retention.md

# Segment retention

Segments in Pinot tables have a retention time, after which the segments are deleted. Typically, offline tables retain segments for a longer period of time than real-time tables.

The removal of segments is done by the retention manager. By default, the retention manager runs once every 6 hours.

The retention manager purges two types of segments:

* Expired segments: Segments whose end time has exceeded the retention period.
* Replaced segments: Segments that have been replaced as part of the [merge rollup task.](https://docs.pinot.apache.org/operators/operating-pinot/minion-merge-rollup-task)

There are a couple of scenarios where segments in offline tables won't be purged:

* If the segment doesn't have an end time. This would happen if the segment doesn't contain a time column.
* If the segment's table has a `segmentIngestionType` of `REFRESH`.

If the retention period isn't specified, segments aren't purged from tables.

The retention manager initially moves these segments into a *Deleted Segments* area, from where they will eventually be permanently removed.
