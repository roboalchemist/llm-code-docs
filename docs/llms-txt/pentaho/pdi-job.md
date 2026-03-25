# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/pentaho-mapreduce-workflow/pdi-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/pentaho-mapreduce-workflow/pdi-job.md

# PDI Job

Once you have created the Mapper transformation, you are ready to include it in a Pentaho MapReduce job entry and build a MapReduce job.

Open a PDI job and drag the specifically-designed Pentaho MapReduce job entry onto the canvas. In addition to ordinary transformation work, this entry is designed to execute mapper/reducer functions within PDI. Again, no need to provide a Java class to achieve this.

Configure the Pentaho MapReduce entry to use the transformation as a mapper. Drag and drop a Start job entry, other job entries as needed, and result job entries to handle the output onto the canvas. Add hops to sequence the entries into a job that you execute in PDI.

The workflow for the job should look something like this.

![Transformation Job Workflow Word Count Example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-0acc47785235b1e402e3559b431a52728ba14a2d%2FJob_Workflow_word_count_example.png?alt=media)

The Pentaho MapReduce dialog box enables you to configure the Pentaho MapReduceentry.

![Pentaho MapReduce dialog Mapper tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-887280b1d66dded97ed9f216544738ae4a88ae85%2FssPDIMapReduceEntry-MapperTab.png?alt=media)
