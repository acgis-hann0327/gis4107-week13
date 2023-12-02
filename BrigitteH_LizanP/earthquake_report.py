import requests
from requests import HTTPError
import os
import feedparser

def get_earthquake_data(out_atom_filename):
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.atom'
    known_file_name = 'data\earthquake_data.atom'
    if os.path.exists(known_file_name) == False:
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            with open(out_atom_filename, 'wb') as out_file:
                # Iterate through the response in 1 MB chunks
                #
                for chunk in response.iter_content(chunk_size=1024*1024):
                    # Write each chunk out to the .csv file ...
                    #
                    out_file.write(chunk)
        except HTTPError as http_err:
            return 'HTTPError: {}'.format(http_err)
        except Exception as err:
            return 'Error:'.format(err.message)
        else:
            return 'OK'

def parse_earthquake_report(atom_file):
    parsed_dict = feedparser.parse(atom_file)
    list_of_earthquakes = []
#    list_of_magnitude = []
    # Extracting the values of lat, long, magnitude, and description from the parsed distionary
    for entry in parsed_dict.entries:
        latitude = entry['where']['coordinates'][1]
        longitude = entry['where']['coordinates'][0]
        title = entry['title']
        list_title = title.split(' - ')
        list_magnitude_earthquake = list_title[0].split()
        magnitude_earthquake = float(list_magnitude_earthquake[1])
        description_of_location = list_title[1]
        tuple_earthquakes_data = (magnitude_earthquake, description_of_location, latitude, longitude)
        # List of tuples with the information of each eartquake!!!
        list_of_earthquakes.append(tuple_earthquakes_data)

    return list_of_earthquakes
    #     # List with the magnitude of each earthquake (this list will be used to calculate the number of earthquakes within each USGS range)
    #     list_of_magnitude.append(magnitude_earthquake)

    # # calculating the count of each classification bin
    # count_magnitude_minor_1 = sum(1 for magnitude in list_of_magnitude if magnitude < 1.0)
    # count_magnitude_between_1_and_2_5 = sum(1 for magnitude in list_of_magnitude if 1.0 <= magnitude < 2.5)
    # count_magnitude_between_2_5_and_4_5 = sum(1 for magnitude in list_of_magnitude if 2.5 <= magnitude < 4.5)
    # count_magnitude_greater_4_5 = sum(1 for magnitude in list_of_magnitude if magnitude >= 4.5)

    # # creating the dictionary with the unique count of the number of earthquakes in each classification bin
    # dict_count_earthquakes = {'<1.0':count_magnitude_minor_1, '>1.0-2.5':count_magnitude_between_1_and_2_5, '>2.5-4.5':count_magnitude_between_2_5_and_4_5, '>4.5+':count_magnitude_greater_4_5}
        



