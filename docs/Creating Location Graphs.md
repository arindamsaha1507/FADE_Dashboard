# Creating Location Graphs

The overall procedure is to extract the map of the region of interest from a larger map and then extract the locations and sizes of the buildings of interest from there. The `osmconvert` software is used to obtain smaller region from a larger Open Street Map (OSM). It can be installed on Linux using the following command.

```shell
sudo apt install osmctools
```

We illustrate the next steps using the English county of Cumbria as an example. The OSM map of **England**, in which **Cumbria** is located, was downloaded from [GeoFabrik](http://download.geofabrik.de/europe/great-britain/england-latest.osm.pbf) and stored as `england.osm.pbf`. Thereafter, the OSM id of the relation corresponding to Cumbria was identified as `88065` from [Open Street Maps](https://www.openstreetmap.org/relation/88065). The population of the county was taken to be `498083` in accordance with [Data Commons](https://datacommons.org/tools/timeline#&place=nuts/UKD1&statsVar=Count_Person). With these pre-requisites, the end-user must take the following steps to prepare the location graph for **Cumbria**.

1. Clone the graph extractor code into the directory where the country map is located.
2. Run the following commands in the terminal from within the directory.

    ```shell
    wget http://polygons.openstreetmap.fr/get_poly.py?id=88065&params=0
    osmconvert england.osm.pbf -B=cumbria.poly -o=cumbria.osm
    python graph_extract.py cumbria 498083
    ```

This results in the creation of the location graph file named `cumbria_buildings.csv` which is the configuration file which can be used as an input for FACS. In order to create the location graph file for any other region in England, step 2 can be followed using the properties of the desired region. For regions in a different country, step 1 also needs to be followed and the map of the corresponding country must be downloaded before following step 2.
