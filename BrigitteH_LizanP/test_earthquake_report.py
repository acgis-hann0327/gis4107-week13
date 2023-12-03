import earthquake_report as er
import os

def test_get_earthquake_data():
    er.get_earthquake_data('data\earthquake_data.atom')
    expected = True
    known_file_name = 'data\earthquake_data.atom'
    actual = os.path.exists(known_file_name)
    assert expected == actual

def test_parse_earthquake_report():
    atom_file = 'data\earthquake_data.atom'
    actual = er.parse_earthquake_report(atom_file)[0][1]
    expected = '68 km NE of Barcelona, Philippines'
    assert expected == actual

def test_write_kml():
    expected = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document><Placemark>
        <name>Saint John River at Fort Kent</name>
        <description>
            https://wateroffice.ec.gc.ca/report/real_time_e.html?stn=01AD002
        </description>
        <Point>
            <coordinates>-68.59583,47.25806,0</coordinates>
        </Point></Placemark>"""
    in_atom_filename = 'data\earthquake_data.atom'
    out_kml_filename = 'data\earthquake_data.kml'
    er.write_kml(in_atom_filename, out_kml_filename)
    with open(out_kml_filename) as infile:
        kml = infile.read()
        actual = kml[:kml.find('/Placemark') + 11]
    assert expected == actual
    # os.startfile(wsc.out_kml_filename)