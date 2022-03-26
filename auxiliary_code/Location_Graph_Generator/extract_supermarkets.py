import sys
import xml.etree.ElementTree as ET
from parse_osm import *

def extract_supermarkets(outfilenameprefix, root, node_list, flag=False):
    
  outfilename = outfilenameprefix + '_supermarkets.csv'
  outfile = open(outfilename, 'w')
    
  leisure_types = {}

  for c1 in root:
    if c1.tag == "way":
      for c2 in c1:
        if flag==True:
          if get_tag(c2, "shop") or get_tag(c2, "landuse") == "retail"  or get_tag(c2, "building") == "retail":
            if get_tag(c2, "amenity") == "supermarket" or get_tag(c2, "other_tags") == "supermarket":
              p = get_polygon_from_way(c1, node_list)
              if p:
                #print(get_nodes(c1))
                #print(c2.tag, c2.attrib, p.centroid, calc_geom_area(p))
                print("supermarket,{},{},{}".format(p.centroid.x, p.centroid.y, int(calc_geom_area(p))), file=outfile)
                break
            else:
              p = get_polygon_from_way(c1, node_list)
              if p:
                #print(get_nodes(c1))
                #print(c2.tag, c2.attrib, p.centroid, calc_geom_area(p))
                print("shopping,{},{},{}".format(p.centroid.x, p.centroid.y, int(calc_geom_area(p))), file=outfile)
                break
        else:
          if get_tag(c2, "shop"):
            if get_tag(c2, "shop") == "supermarket" or get_tag(c2, "amenity") == "supermarket" or get_tag(c2, "other_tags") == "supermarket":
              p = get_polygon_from_way(c1, node_list)
              if p:
                #print(get_nodes(c1))
                #print(c2.tag, c2.attrib, p.centroid, calc_geom_area(p))
                print("supermarket,{},{},{}".format(p.centroid.x, p.centroid.y, int(calc_geom_area(p))), file=outfile)
                break
            else:
              p = get_polygon_from_way(c1, node_list)
              if p:
                #print(get_nodes(c1))
                #print(c2.tag, c2.attrib, p.centroid, calc_geom_area(p))
                print("shopping,{},{},{}".format(p.centroid.x, p.centroid.y, int(calc_geom_area(p))), file=outfile)
                break

  print("Debug: list of leisure types in osm file:", leisure_types, file=sys.stderr)

  outfile.close()


if __name__ == "__main__":
  tree = ET.parse(sys.argv[1])

  root = tree.getroot()
  leisure_types = {}
  node_list = build_node_list(root)

  # use flag = true to execute special code block for landuse and buildings = retail
  flag = True
  extract_supermarkets(tree, flag)
