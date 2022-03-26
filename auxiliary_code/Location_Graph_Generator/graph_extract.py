import pandas as pd
import requests
# from bs4 import BeautifulSoup

import os
import subprocess
import sys

import xml.etree.ElementTree as ET
from parse_osm import build_node_list

from extract_hospitals import extract_hospitals
from extract_offices import extract_offices
from extract_schools import extract_schools
from extract_parks import extract_parks
from extract_supermarkets import extract_supermarkets
from extract_houses import extract_houses

# ## Location Map Functions

def extract_region_map(region=None, search_path=None):
    if region != None:
        if region + '.osm' not in os.listdir(search_path):
            command = 'osmconvert ' + search_path + 'england.osm.pbf -B=' + search_path + region + '.poly -o=' + search_path + region +'.osm'
            print(command)
            subprocess.call(command, shell=True)


def get_population(region=None, pop_data=None):
    if region != None:
        return int(pop_data.Population[pop_data.Borough == region])
    else:
        return 0


def extract_all_data(current_region, region_population, verbose=False, path=None):

    if current_region != None:

        if current_region + '_data_combined.csv' not in os.listdir():

            current_region = current_region.replace(' ', '_')
            map_filename = current_region + '.osm'
            data_file_path = current_region + '_data'
            data_file_prefix = current_region + '_data'

            tree = ET.parse(map_filename)
            root = tree.getroot()
            node_list = build_node_list(root)

            if verbose:
                print('Extracting Houses...')
            extract_houses(data_file_prefix, root, node_list, region_population)
            if verbose:
                print('Extracting Offices...')
            extract_offices(data_file_prefix, root, node_list)
            if verbose:
                print('Extracting Parks...')
            extract_parks(data_file_prefix, root, node_list)
            if verbose:
                print('Extracting Supermarkets...')
            extract_supermarkets(data_file_prefix, root, node_list)
            if verbose:
                print('Extracting Schools...')
            extract_schools(data_file_prefix, root, node_list)
            if verbose:
                print('Extracting Hospitals...')
            extract_hospitals(data_file_prefix, root, node_list)

            command = 'cat ' + data_file_path + '* > ' + data_file_path + '_combined.csv'
            subprocess.call(command, shell=True)


def get_idx(region=None, osm_id_data=None):

    if region == None:
        return 1713458
    elif region in list(osm_id_data.Borough):
        return int(osm_id_data.OSM_id[osm_id_data.Borough==region])
    else:
        return 0

def get_poly(idx=175342, region='greater_london', path=None):

        url = 'https://polygons.openstreetmap.fr/get_poly.py?id=' + str(idx) + '&params=0'
        if region + '.poly' not in os.listdir(path):
            dd = requests.get(url)
            fname = path + region + '.poly'
            with open(fname, 'wb') as ff:
                ff.write(dd.content)

def extract_boundary(region='greater_london', osm_id_data=None, pop_data=None, path=None):

    if region != 'greater_london':
        get_poly(get_idx(region, osm_id_data), region, path)
        extract_region_map(region, search_path=path)
        extract_all_data(region, get_population(region, pop_data), path=path)

    fname = path + region + '.poly'

    with open(fname) as ff:
        s = ff.readlines()[2:-2]

    dd = [x.strip().split('\t') for x in s]

    df = pd.DataFrame(dd, dtype=float, columns=['Longitude', 'Latitude'])

    return df

if __name__ == '__main__':

    region = str(sys.argv[1])
    population = int(sys.argv[2])
    extract_all_data(region, population, path='Data')
