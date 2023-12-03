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
    actual = er.parse_earthquake_report(atom_file)[41][1]
    expected = '68 km NE of Barcelona, Philippines'
    assert expected == actual

def test_write_kml():
    expected = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
  <Placemark>
    <name>Magnitude: 1.7</name>
    <description>Location: Central Alaska
Latitude: 63.2737
Longitude: -149.3227</description>
    <Point>
      <coordinates>-149.3227,63.2737,0</coordinates>
    </Point>
  </Placemark>"""
    in_atom_filename = 'data\earthquake_data.atom'
    out_kml_filename = 'data\earthquake_data.kml'
    er.write_kml(in_atom_filename, out_kml_filename)
    with open(out_kml_filename) as infile:
        kml = infile.read()
        actual = kml[:kml.find('/Placemark') + 11]
    assert expected == actual
    
    script_folder = os.path.dirname(os.path.abspath(__file__))
    earthquake_data_kml = os.path.join(script_folder, out_kml_filename)
    os.startfile(earthquake_data_kml)
    