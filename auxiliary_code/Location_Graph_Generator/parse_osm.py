import sys
import xml.etree.ElementTree as ET
import pyproj
from shapely import ops
from functools import partial
from shapely.geometry import Polygon, Point
import random

def build_node_list(root, verbose=False):
  node_list = {}
  for c1 in root:
    if c1.tag == "node":
      x = float(c1.attrib["lon"])
      y = float(c1.attrib["lat"])
      i = int(c1.attrib["id"])
      node_list[i] = [x,y]

  if verbose:
    for k in node_list:
      print(k,node_list[k])
  return node_list
              

def get_nodes(way, verbose=False):
  nodes = []
  for c2 in way:
    if c2.tag == "nd":
      nodes.append(int(c2.attrib["ref"]))
      if verbose:
        print(c2.attrib["ref"])
  return nodes

def get_polygon_from_way(way, node_list, verbose=False):
  nodes = get_nodes(way, verbose)
  poly_nodes = []
  for i in nodes:
    try:
      poly_nodes.append(node_list[i])
    except KeyError:
      print("Warning: node with key {} is not found, ignoring it...".format(i), file=sys.stderr)
  if len(poly_nodes) > 3:
    return Polygon(poly_nodes)
  else:
    print("Warning: location has fewer than 3 valid nodes. Omitting it.", file=sys.stderr)
    return None


# Credit to https://gis.stackexchange.com/questions/127607/area-in-km-from-polygon-of-coordinates
# User jczaplew
def calc_geom_area(poly):
  """
  Calcs area in square meters (polygon.area returns it in degrees, not so useful).
  """
  bounds = poly.bounds
  p = ops.transform(
  partial(
      pyproj.transform,
      pyproj.Proj('EPSG:4326'),
      pyproj.Proj(
          proj='aea',
          lat_1=bounds[1],
          lat_2=bounds[3])),
  poly)
  # Print the area in m^2
  return p.area

def random_points_within(poly, num_points):
  min_x, min_y, max_x, max_y = poly.bounds
  points = []
  while len(points) < num_points:
    random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
    if (random_point.within(poly)):
      points.append(random_point)

  return points


def get_tag(c2, tag_type):
  if c2.tag == "tag":
    if c2.attrib["k"] == tag_type:
      return c2.attrib["v"]
  return None
