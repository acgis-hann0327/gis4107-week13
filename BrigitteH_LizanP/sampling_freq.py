import water_stn_converter as wsc



def create_sampling_report(in_json_filename, out_csv_filename):
    wsc.in_json_filename = in_json_filename
    wsc.out_csv_filename = out_csv_filename 
    wsc.get_sampling_frequencies()
    with open(in_json_filename) as infile:
        header = infile.readline()
        with open(out_csv_filename, 'w') as outfile:
            outfile.write(header)
            for line in infile:
                outfile.write(line)