import earthquake_report as er
import os

def test_get_earthquake_data():
    er.get_earthquake_data('data\earthquake_data.atom')
    expected = True
    known_file_name = 'data\earthquake_data.atom'
    actual = os.path.exists(known_file_name)
    assert expected == actual

def test_parse_earthquake_report():
    atom_file = 'data\earthquake_data_copy.atom'
    actual = er.parse_earthquake_report(atom_file)
    expected = 0
    assert expected == actual