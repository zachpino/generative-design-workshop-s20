# Week 6 · Algorithmic Processes

We'll examine this week how contemporary designers are implementing iterative algorithmic processes to address complex design problems.

In particular, we'll look at the related [Delaunay Triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation) and [Voronoi Tesselation](https://en.wikipedia.org/wiki/Voronoi_diagram) — simple mathematical models for complex natural phenomena. We'll also use [Catmull-Clark Subdivision](https://en.wikipedia.org/wiki/Catmull–Clark_subdivision_surface) algorithm to smooth data-drive, anatomical forms.

-----

### References for the Week

Some examples of pattern algorithm design work.

- [Jerusalem Table](https://www.core77.com/projects/39363/Jerusalem-Tables)
- [Voronoi at Thingiverse](https://www.thingiverse.com/search?q=voronoi)
- [Nervous System](https://n-e-r-v-o-u-s.com/projects/)
- [Marc Newson Voronoi Shelf](http://marc-newson.com/voronoi-shelf/)
- [Go Wheel Chair](http://layerdesign.com/projects/go/)
- [Bespoke 3D Orthopedics Brace](https://www.youtube.com/watch?v=OGRkNexY3N8)
- [Interactive Subdivision](https://www.khanacademy.org/partner-content/pixar/modeling-character/modeling-subdivision/p/interactive-subdivision-in-3d)
- [Pixar in a Box](https://www.khanacademy.org/partner-content/pixar)

- [Unyq](http://unyq.com/en-us/us/)
- [Osteoid Ultrasonic Cast](https://competition.adesignaward.com/design.php?ID=34151)
- [Cortex Cast](http://www.evilldesign.com/cortex)
- [Thermal Comfort Casts](https://3dprint.com/192877/3d-printed-cast-thermal-comfort/)
- [Hand and Wrist Fracture Cast](http://www.machiningnews.com/2017/06/real-world-test-of-3d-printed-cast-for-hand-fracture/)

- [How to Hand Draw Delaunay and Voronoi](http://765.blogspot.com/2009/09/how-to-draw-voronoi-diagram.html)
- [Simple Interactive Voronoi Editor](http://www.sygreer.com/projects/voronoi/)
- [Interactive Javascript Translation](http://paperjs.org/examples/voronoi/)
- [World Capitals Voronoi](https://www.jasondavies.com/maps/voronoi/capitals/)
- [In D3 Data Viz Library](https://github.com/d3/d3-delaunay)
- [Anna Nowak on Application of Voronoi diagrams in contemporary architecture and town planning](https://yadda.icm.edu.pl/baztech/element/bwmeta1.element.baztech-5259df1a-e1f7-442f-a68c-10c0c2b35c96/c/chmot62_06.pdf)

- [All the Maths](http://cgl.uni-jena.de/pub/Workshops/WebHome/cgl12new.pdf)
- [Easier to Understand All the Maths](https://meemoo.org/blog/2014-07-14-noflo-geometry)


-----


### Triangulation, Tesselation, Subdivision

#### Learning about Meshes : Nefertiti

![nef](nef.png)

Take a look at this [fantastically controversial endeavor](http://nefertitihack.alloversky.com) by German artists Nora Al-Badri and Jan Nikolai Nelles to [digitally repatriate](https://ncph.org/history-at-work/repatriation-and-decolonization/) a famous bust of Queen Nefertiti excavated from Egypt and now located in the [Neues Museum in Berlin](https://www.smb.museum/en/museums-institutions/neues-museum/collections-research/about-the-collection.html). Even the [controversy is controversial](https://hyperallergic.com/281739/could-the-nefertiti-scan-be-a-hoax-and-does-that-matter/).

Perhaps we might combine it with some data on the impact of tourism on [Egypt](https://data.worldbank.org/indicator/ST.INT.ARVL?locations=EG&name_desc=false)?

Download a [simplified model](nefertiti-95reduced.obj).

```
International tourist arrivals to Egypt 1995-2017
2871000	
3528000	
3656000	
3213000	
4490000	
5116000	
4357000	
4906000	
5746000	
7795000	
8244000	
8646000	
10610000
12296000
11914000
14051000
9497000	
11196000
9174000	
9628300	
9139000	
5258000	
8157000			
```

#### Delaunay Triangulation

![del](https://i.pinimg.com/originals/76/c1/a2/76c1a2a0222ff50861797b6152db8aa2.jpg)

Developed in the 1930s by Russian geometer [Boris Delaunay](https://en.wikipedia.org/wiki/Boris_Delaunay), the [Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation) is essential to nearly all computer graphics. Whenever you hear or talk about a 'mesh', that's likely based on a Delaunay Triangulation! Videogames, visual effects for cinema, medical scanning, arcGIS geographic data — everything! It is also in heavy use by structural engineers, and unintentionally undergirds nearly all of the truss geometries that define bridges, attics, and other triangular structures as well as communication network routing. More recently, as autonomous vehicles begin to explore unmapped areas where sensors may fail, Delaunay Triangulation logic is used to [allow intelligent agents to navigate dangerous boundaries](https://en.wikipedia.org/wiki/Constrained_Delaunay_triangulation). 

In 3D space, the triangulation creates a *network topography* of triangular cells, based on known points to support, which would use the minimal amount of connective material to maintain, in opposition to a *singular force vector*. Imagine the Delaunay set as the circus net for trapeze artists, which would stretch and deform as the gymnasts fall into it and bounce around in it. That same net would not work very well to catch someone launched into it from the side...

To produce a Delaunay Mesh...

- Sprinkle random points on a 2D plane
- Draw all possible circles defined by any of the 3 points
- If those circles contain *any* of the sprinkled points, that circle should be discarded
- If a circle passes the test, then draw the [circumscribed triangle](https://en.wikipedia.org/wiki/Circumscribed_circle) as an edge

![delaunay supports](delSample.jpg)

#### Voronoi Tesselation

![voronoi](http://datagenetics.com/blog/may12017/anim2.gif)

![del vor](http://meemoo.org/images/delaunay_voronoi_dual.gif)

The geometric [*dual*](https://en.wikipedia.org/wiki/Dual_polyhedron) of the Delaunay Triangulation, [Voronoi Tesselation](https://en.wikipedia.org/wiki/Voronoi_diagram) invented by another amazing Russian mathematician — [Georgy Voronoi](https://en.wikipedia.org/wiki/Georgy_Voronoy) — similarly tiles a plane with shapes — though not not usually triangles. The unusual cells that come out of the Voronoi Tesselation model fairly accurately a multitude of natural formal phenomena as well as behaviors. Bone microstructure, sponge anatomy, soil clumping, termite and bee architecture, neuron network arrangement.... the list is almost endless. This is because the Voronoi Tesselation models an *efficient* set of cells. All of the space within a single Voronoi cell is *closer* to the centroid of a Delaunay triangle, and as a result, Voronoi logic approximates how any agent might make a decision about which of a set of possible choices should be chosen based purely on efficiently traversing or covering a plane or volume. It is increasingly being used by public policymakers to [place trainstops, design road networks](http://datagenetics.com/blog/may12017/index.html), and [predict crime](https://www.tandfonline.com/doi/abs/10.1080/00330124.2017.1288578?scroll=top&needAccess=true&journalCode=rtpg20).

- Generate a Delaunay Triangulation
- Find the midpoint of each edge, and draw a line perpendicular to the edge
- Intersect all these lines, and clip adjacent lines with one another
- Draw the remnant, irregular polygons

![bone](https://afinemesh.files.wordpress.com/2014/04/printed-voronoi.jpg)

#### Catmull Clark Subdivision

![catmull clark](cc.png)

[Catmull Clark Subdivision](https://en.wikipedia.org/wiki/Catmull–Clark_subdivision_surface) is amazing! This algorithm, developed by Pixar engineer-turned-President [Edwin Catmull](https://en.wikipedia.org/wiki/Edwin_Catmull) and author of [Creativity, Inc.](https://www.amazon.com/Creativity-Inc-Overcoming-Unseen-Inspiration-ebook/dp/B00FUZQYBO) and his friend and colleague [Jim Clark](https://en.wikipedia.org/wiki/James_H._Clark), the founder of Netscape and inventor of several critical 3D rendering technologies for animation, cinema, and video games.

The Catmull-Clark subdivision is a simple, iterative process.

- Take each edge of a 3d mesh
- Split each edge and create a new vertex at the center of each face, and connect the new vertex to all the split edges
- Find the average coordinates of the original vertex, the face center vertex, and the split edge vertex
- Move the original vertex to this new, average coordinate and rebuild the mesh

The resulting forms are more *continuous* that the original mesh, with any harsh edges smoothed out. The one flaw is that the new mesh is inherently *heavier*, it has significantly more face and vertices. The characteristic aesthetic of Pixar films, which has directly inspired most other 3D animation companies, is [fundamentally due to the Catmull-Clark algorithm](https://graphics.pixar.com/library/Geri/paper.pdf).

![sulley](subD.jpg)

Play with Pixar in a Box's amazing [interactive tool](https://www.khanacademy.org/partner-content/pixar/modeling-character/modeling-subdivision/p/interactive-subdivision-in-3d)) to get a feel for this simple but surprisingly powerful algorithm.


-----


### Food 4 Rhino Downloads

![grass,right?](rhino.gif)

[Food4Rhino](http://www.food4rhino.com) is a central repository for plugins and add-on software for Rhino 3D, as well as for Grasshopper. Plugins for plugins! 

Create a free account on the website and search around. Anything exciting? Unfortunately, not everything will work on Macs and it's impossible to know unless you see an Apple logo under the *Download* button. But, even if *there is not an Apple logo*, it still might work!

To install a Grasshopper plugin, open Grasshopper, and navigate to File -> Special Folders -> Components Folder.

This will open a Finder/Explorer window, into which you can move the downloaded files. Sometimes, you'll get a single file, and other times, you'll get whole folders. In that latter case, the best practice is usually to drag the entire downloaded folder over. You can find Grasshopper plugins all over the internet, not just at Food4Rhino. If you are running Windows, right click on any .exe, .ghuser, and .gha files and click on *Properties*. Make sure to click *Unblock* if it is an option.

For Grasshopper to load newly installed plugins, we need to restart Rhino and Grasshopper. 

For this and future exercises, let's install a few essential plugins.

- For better Mesh cleanup: [Mesh Edit Tools *2*](https://www.food4rhino.com/app/meshedit)

- For powerful geometric manipulation: [Lunchbox *2017.8.1 ZIP*](https://www.food4rhino.com/app/lunchbox#)


-----


### Grasshopper Algorithmic Forms

#### 'Simple' Delaunay Triangulation

From a field of random points, create a Delaunay triangulation.

[Download](delaunay-definition.gh)

![Grasshopper Definition](delaunay-grasshopper.png)

![Grasshopper Screenshot](delaunay-screenshot.png)

-----

#### Data-Driven Delaunay Cast

Create a Delaunay triangulation in 3D space around a data-driven, anatomical form.

[Download](delaunay-cast-definition.gh)

![Grasshopper Definition](delaunay-cast-grasshopper.png)

![Grasshopper Screenshot](delaunay-cast-screenshot.png)

-----

#### Data-Driven Voronoi Cast

Create a voronoi tesselation in 3D space around a data-driven, anatomical form. Allow for variable cell openness based on attractor curves.

[Download](voronoi-cast-definition.gh)

![Grasshopper Definition](voronoi-cast-grasshopper.png)

![Grasshopper Screenshot](voronoi-cast-screenshot.png)


-----


### Homework

##### Grasshopper (1.5 hours)

TBD after class

##### Listening and Watching I (1 hour)

Read this [short description on this history, opportunities, and limitations of computational narrative](https://medium.com/@mark_riedl/computational-narrative-intelligence-past-present-and-future-99e58cf25ffa) written by [Mark Reidl](https://metamind.io), the director of Salesforce's AI division. 

In so many ways, [contemporary stories are predictable and formulaic](https://theweek.com/articles/797822/disney-ideas), which makes them ideal candidates for generative processes. Disney, like many narrative content producers, is [investing heavily](https://la.disneyresearch.com/?s=computational+narrative) in the opportunities for dynamism, repeatability, predictability, and customization offered by generative narrative processes. In particular, Disney seems to be pushing into [story co-creation with their audiences](https://s3-us-west-1.amazonaws.com/disneyresearch/wp-content/uploads/20170725080728/Computational-Narrative-Paper.pdf) through computational narrative tools.

Other avant-garde storytellers are already *collaborating directly* with experimental, computationally-created narratives. Please watch the 10 minute [*Sunspring*](https://www.youtube.com/watch?v=LY7x2Ihqjmc) from 2016 starring Thomas Middleditch, and written by a generative algorithm named *Benjamin/Jetson*. If interested, read [Ars Technica's interview](https://arstechnica.com/gaming/2016/06/an-ai-wrote-this-movie-and-its-strangely-moving/) with the short's directory Oscar Sharp.

##### Visualization Practice (1 hour, spread out over week)

Take a look at the Dear Data week thirty-six on *Indecision* in preparation for next week. Through the week, construct a dataset for your own visualization purposes on moments when you are stuck in indecision and option-paralysis, and produce 3 visualizations on 5"x7" cards. Explore both 2D and 3D visualization opportunities, and prepare to share these with your peers. Crayons, color pencils, and play-doh are available in the faculty corridor on Zach's desk. Add a legibility key to the backs of all visualizations, and document them in the Google Drive.

##### Submit Work

Please submit homework into the appropriate folders in the class Google Drive.