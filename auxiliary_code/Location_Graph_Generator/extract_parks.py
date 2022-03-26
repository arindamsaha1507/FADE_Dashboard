import sys
import xml.etree.ElementTree as ET
from parse_osm import *

def extract_parks(outfilenameprefix, root, node_list):
  outfilename = outfilenameprefix + '_parks.csv'
  outfile = open(outfilename, 'w')
  leisure_types = {}
  for c1 in root:
    if c1.tag == "way":
      for c2 in c1:
        #<tag k="leisure" v="park"/>
        if c2.tag == "tag":
          if c2.attrib["k"] == "leisure":
            if c2.attrib["v"] in leisure_types:
              leisure_types[c2.attrib["v"]] += 1
            else:
              leisure_types[c2.attrib["v"]] = 1

            if c2.attrib["v"] in ["park","garden","nature_reserve"]:
              p = get_polygon_from_way(c1, node_list)
              if p:
                #print(get_nodes(c1))
                #print(c2.tag, c2.attrib, p.centroid, calc_geom_area(p))
                print("park,{},{},{}".format(p.centroid.x, p.centroid.y, int(calc_geom_area(p))), file=outfile)
            else:
              p = get_polygon_from_way(c1, node_list)
              if p:
                #print(get_nodes(c1))
                #print(c2.tag, c2.attrib, p.centroid, calc_geom_area(p))
                print("leisure,{},{},{}".format(p.centroid.x, p.centroid.y, int(calc_geom_area(p))), file=outfile)

  print("Debug: list of leisure types in osm file:", leisure_types, file=sys.stderr)
  outfile.close()

if __name__ == "__main__":
  tree = ET.parse(sys.argv[1])
  root = tree.getroot()

  leisure_types = {}
  node_list = build_node_list(root)

  extract_parks(tree)
