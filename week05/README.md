# Week 5 · Data Forms

This week, we'll focus on how contemporary designers are using data — both at an individual and global level — to create uniquely meaningful 3d forms with functional, aesthetic, and public awareness goals.

This particular emerging topic — the creation of a different type of *smart-object* than we often expect — sits at the nexus of data science and visualization, generative design practice, politics and social critique, and speculative communication design.

-----

### References for the Week

Some examples of designed data forms.

- [Dataphys List](http://dataphys.org/list/)
- [Ezri Tarazi](http://www.tarazistudio.com)
- [Adrian Segal](https://www.adriensegal.com)
- [Mischer Traxler](http://mischertraxler.com/projects/)
- [Paul Heinicker](http://paulheinicker.com)
- [Iohanna Pani](http://iohanna.com/filter/DESIGN)
- [Discrete Figures](https://research.rhizomatiks.com/s/works/discrete_figures/en/)


Some data visualization references.

- http://www.dear-data.com 
- www.informationisbeautiful.net
- www.datapointed.com
- www.visualnews.com
- http://nytlabs.com
- http://flowingdata.com
- http://fivethirtyeight.com
- http://infosthetics.com
- http://www.creativeapplications.net
- http://www.datavisualization.ch

-----

### Tactile Data

![form follows data by iohanna pani](https://www.designboom.com/cms/images/-Z84/ff1.jpg)

Data forms, a new term for an even newer aesthetic archetype, is a very young discipline. As data visualization has become more common in 2D and interactive applications — 3-dimensional artists, architects, and designers have begun to experiment with physicalized 3D data — and have questioned how we can effectively communicate more complex information through 3D form. 

Embedding data in physical 3D rather than 2D form allows for many obvious benefits. Materiality, surface finish, color, scale, texture, volume, enclosedness, placement in the world, weight... these all become meaningful choices in 3D form, and provide additional vectors for data-driven intentionality.  More intriguing, perhaps, these same designers have experimented with creating data forms that replace traditional objects — provoking users to engage them in everyday confrontations — constant and unavoidable reminders of the embedded data with the goal of both awareness and behavioral change. 

Would you eat differently if your tableware reminded you of the world's obesity epidemic? Would you use your computer differently if its palmrest was shaped with data of your region's energy usage? Would you spend your days differently if your couch was cushioned with the data of the time you and your friend group spend on Facebook and Netflix?

-----

### Open Data Sources

We often talk about [data as the raw materials](https://designingforanalytics.com/resources/episodes/025-treating-data-science-at-ideo-as-a-discipline-of-design-with-dean-malmgren/) for many new sorts of design. So, to acclimate ourselves to these new opportunities, we need to get our hands on as much of this new resource as possible. 
 
##### Data Search Engines and General Directories
- https://www.data.gov
- https://www.census.gov/developers/
- http://www.zanran.com/q/
- https://www.reddit.com/r/datasets/ (and check out the linked subreddits too!)
- https://github.com/toddmotto/public-apis
- https://www.google.com/publicdata/directory
- https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research
- https://tinyletter.com/data-is-plural

##### Municipal
- https://data.cityofchicago.org
- https://nycopendata.socrata.com/

##### Atmospheric and Geologic
- http://www.ndbc.noaa.gov
- https://www.ncdc.noaa.gov/cdo-web/
- http://weather.rap.ucar.edu
- https://earthquake.usgs.gov/data/
- http://www.ssec.wisc.edu/data/
- https://cfpub.epa.gov/surf/locate/index.cfm
- http://volcano.ssec.wisc.edu

##### Space!
- https://data.nasa.gov
- http://chandra.harvard.edu
- http://sid.stanford.edu/database-browser/

##### Transportation
- https://github.com/graphhopper/open-traffic-collection
- http://opentraffic.io
- https://jblevins.org/notes/airline-data
- https://www.fra.dot.gov/Page/P0365

##### Social
- https://meta.wikimedia.org/wiki/Datasets
- https://developers.facebook.com/docs/graph-api
- https://www.google.com/trends/explore
- https://dev.twitter.com/streaming/overview
- https://www.cia.gov/library/publications/the-world-factbook/

##### Financial
- https://www.quandl.com
- http://data.worldbank.org
- https://www.google.com/finance

##### Animals and Plants
- https://www.gbif.org
- https://beeinformed.org
- https://www.movebank.org
- http://archive.ics.uci.edu/ml/datasets/zoo
- http://whale.wheelock.edu/whalenet-stuff/StopBm2016/
- https://cvml.ist.ac.at/AwA/
- https://ecologicaldata.org/find-data


-----


### Sculpting with Data

Let's manipulate outside data in Grasshopper and connect our parametric forms to meaningful information.

#### Data Plotting

Take a look at many different ways to convert random 3D points into a variety of 3d forms.

[Download](dataplot-definition.gh)

![Grasshopper Definition](dataplot-grasshopper.png)

![Grasshopper Screenshot](dataplot-screenshot.png)

-----

#### Geographic Data Sample

Sculpt real data into form in Grasshopper using this [dataset on the geographic position of capital cities](capitalCities.txt). This Grasshopper file produces a map and globe similar in intent to this [interactive page](https://www.jasondavies.com/maps/voronoi/capitals/) attempting to reveal the mismatch between geopolitical governing structures and geography. 

[Download](voronoi-geographic-definition.gh)

![Grasshopper Definition](voronoi-geographic-grasshopper.png)

![Grasshopper Screenshot](voronoi-geographic-screenshot.png)

-----

#### Motion Data Sample

Sculpt real data into form in Grasshopper using a dataset on 3D motion from the [SFU Mocap Database](http://mocap.cs.sfu.ca). This example is similar to the work of several [futurist artists](https://en.wikipedia.org/wiki/Futurism) that are often called [*dynamisms*](https://en.wikipedia.org/wiki/Dynamism_of_a_Dog_on_a_Leash) and based on the 20th century emergence of [chronophotographic developments](https://en.wikipedia.org/wiki/Chronophotography).

[Download](motion-definition.gh)

![Grasshopper Definition](motion-grasshopper.png)

![Grasshopper Screenshot](motion-screenshot.gif)

This example uses a *ghpython* node and a short script to load files directly downloaded from the [SFU Mocap database](http://mocap.cs.sfu.ca). 

```python
"""
Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable
"""

__author__ = "zap"

import rhinoscriptsyntax as rs

#ask Rhino to open a file
filename = rs.OpenFileName("Open Point File")

#open file for 'r'eading
file = open(filename, "r")

#read all of the lines of the file
contents = file.readlines()

#close the file
file.close()

#output all data
a = contents    
```

Opening and closing the script will allow you to choose a downloaded file to load. Double-click on the *ghpython* node and paste the below code into the pop-up window. When you close the window and "save", another window will pop-up asking you for a file from the database.

![load](load.gif)

-----

#### Data Forms - Gardening Pots

Let's create a set of discursive data objects, drawing attention to several countries' respective deforestation activities and policies.

[Download](data-pots-definition.gh)

![Grasshopper Definition](data-pots-grasshopper.png)

![Grasshopper Screenshot](data-pots-screenshot.png)

Data forms that carry a family similarity to traditional object archetypes are often more effective than the 'data-blobs' (like the examples created above) that are expected of traditional data visualization. By embedding data in everyday objects, we can easily make data more approachable, legible, and confrontational to audiences. Here, we create a set of gardening pots, which demonstrate in 3-dimensions the history of the forested area of 5 large countries: Brazil, China, India, Russia, and the United States. The inside volume of the pot will be shaped by the history of the various countries' forested percentage, and the outside volume will make clear the proportional size of the country and its most recent (2015) forest amount. The smaller the remaining forest, the less room will be available for planting, and the easier the pot will be to topple and shatter — embodying the fragility of the remaining ecosystems. All data is from the [World Bank](https://data.worldbank.org/indicator/AG.LND.FRST.ZS?end=2015&locations=CN-RU-US-BR-IN&start=1990). 

![diagram](diagram.png)

##### Country Areas in Square Kilometers Data (Brazil,China,India,Russia,USA)
```
"Country","Area"
"Brazil",8.516
"China",9.597
"India",3.287
"Russia",17.1
"USA",9.834
```

##### Forested Area as Percentage of Total Area
```
"Country",1990,1995,2000,2005,2010,2015
"Brazil",65.4,63.9,62.4,60.6,59.6,59.0
"China",16.7,17.8,18.9,20.6,21.4,22.2
"India",21.5,21.7,22.0,22.8,23.5,23.8
"Russia",49.4,49.4,49.4,49.4,49.8,49.8
"USA",33.0,33.1,33.1,33.0,33.7,33.0
```

Also browse through these other complementary datasets. Could we find a way to embed some of these other datapoints in our data form?

- [Global Deforestation Rates by Country](https://rainforests.mongabay.com/deforestation_country.html)
- [Environmental Performance Indicators](https://epi.envirocenter.yale.edu/epi-downloads)
- [Global Forest Watch](https://www.globalforestwatch.org)
- [Population Change](https://data.worldbank.org/indicator/SP.POP.TOTL?end=2005&name_desc=false&start=1990)	
- [Country Area](https://simple.wikipedia.org/wiki/List_of_countries_by_area)


-----


### Homework

##### Grasshopper (1.5 hours)

Recreate the "Data Forms - Gardening Pots" and "Geographic Data Sample" examples above. Also, download and play with "Motion Data Sample" and load other datasets into it. It's fun! 

Though you can download the examples, please do recreate them. Grasshopper will only get easier if you patch the nodes yourself!

![patch](patching.gif)

##### Listening and Watching I (1 hour)

Read this [short description on this history, opportunities, and limitations of computational narrative](https://medium.com/@mark_riedl/computational-narrative-intelligence-past-present-and-future-99e58cf25ffa) written by [Mark Reidl](https://metamind.io), the director of Salesforce's AI division. 

In so many ways, [contemporary stories are predictable and formulaic](https://theweek.com/articles/797822/disney-ideas), which makes them ideal candidates for generative processes. Disney, like many narrative content producers, is [investing heavily](https://la.disneyresearch.com/?s=computational+narrative) in the opportunities for dynamism, repeatability, predictability, and customization offered by generative narrative processes. In particular, Disney seems to be pushing into [story co-creation with their audiences](https://s3-us-west-1.amazonaws.com/disneyresearch/wp-content/uploads/20170725080728/Computational-Narrative-Paper.pdf) through computational narrative tools.

Other avant-garde storytellers are already *collaborating directly* with experimental, computationally-created narratives. Please watch the 10 minute [*Sunspring*](https://www.youtube.com/watch?v=LY7x2Ihqjmc) from 2016 starring Thomas Middleditch, and written by a generative algorithm named *Benjamin/Jetson*. If interested, read [Ars Technica's interview](https://arstechnica.com/gaming/2016/06/an-ai-wrote-this-movie-and-its-strangely-moving/) with the short's directory Oscar Sharp.

##### Visualization Practice (1 hour, spread out over week)

Take a look at the Dear Data week thirty-six on *Indecision* in preparation for next week. Through the week, construct a dataset for your own visualization purposes on moments when you are stuck in indecision and option-paralysis, and produce 3 visualizations on 5"x7" cards. Explore both 2D and 3D visualization opportunities, and prepare to share these with your peers. Crayons, color pencils, and play-doh are available in the faculty corridor on Zach's desk. Add a legibility key to the backs of all visualizations, and document them in the Google Drive.

##### Data Research (1 hour, spread out over week)

Take a look through the many data sources linked above and bookmark some personally interesting, unexpected, and meaningful datasets. What might the individual version of some of these global datasets look like? Might some of these datasets find their way into design work in your other courses?

##### Submit Work

Please submit homework into the appropriate folders in the class Google Drive.