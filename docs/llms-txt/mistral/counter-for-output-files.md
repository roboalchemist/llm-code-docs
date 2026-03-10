# counter for output files
counter = 0
with open(input_file, "r") as f_in:
    # read the input file line by line
    for line in f_in:
        # parse the line as JSON
        data = json.loads(line)
        # write the data to the current output file
        output_file_objects[counter].write(json.dumps(data) + "\n")
        # increment the counter
        counter = (counter + 1) % 3