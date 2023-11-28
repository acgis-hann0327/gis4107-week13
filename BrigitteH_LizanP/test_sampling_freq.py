import sampling_freq as sf

def test_create_sampling_report():
    in_json_filename = r'data\water_stn.json'
    out_csv_filename = r'data\water_stn.csv'
    sf.create_sampling_report(in_json_filename,out_csv_filename)
    # with open (out_csv_filename) as infile:

    expected = '682'
    actual = 0
    assert actual == expected
