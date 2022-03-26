import sys
import xml.etree.ElementTree as ET
from parse_osm import *
import numpy as np
import csv

def extract_houses(outfilenameprefix, root, node_list, Region_Population, household_size=2.6):
    
    outfilename = outfilenameprefix + '_houses.csv'
    outfile = open(outfilename, 'w')
    
    Total_Num_of_Houses = Region_Population/household_size

    poly_list = []

    for c1 in root:
      if c1.tag == "way":
        for c2 in c1:
          if c2.tag == "tag":
            #if c2.attrib["k"] == "building":
            #  if c2.attrib["v"] in ["house","apartments","residential"]:
            if c2.attrib["k"] == "landuse":
              if c2.attrib["v"] == "residential":
                p = get_polygon_from_way(c1, node_list)
                if p:
                  poly_list.append((p, p.centroid.x, p.centroid.y, int(calc_geom_area(p))))

                
    Total_Area = sum(p[3] for p in poly_list)

    #with open('house.csv', "w") as outfile:
    for p in poly_list:
      areaPercent = p[3]/Total_Area
      Num_of_Houses = int(Total_Num_of_Houses * areaPercent)
      houseArea = int(areaPercent * Num_of_Houses/Total_Num_of_Houses)
      points = random_points_within(p[0], Num_of_Houses)
      for h in points:
        print("house,{},{},{}".format(h.x, h.y, houseArea), file=outfile)
        #  outfile.write("house,{},{},{}".format(h.x, h.y, houseArea))
        #  outfile.write("\n")
        
    outfile.close()


    # print("Debug: list of leisure types in osm file:", building_types, file=sys.stderr)

