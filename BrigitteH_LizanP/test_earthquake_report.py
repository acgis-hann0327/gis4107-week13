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