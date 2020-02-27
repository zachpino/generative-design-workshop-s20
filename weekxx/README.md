# Week 5 · Grids as Data Scaffolds

This week, we will take a look at how generative designers can use the regularity and structures of grids and related data scaffolds to seed their design work.

-----

### References for the Week

- [Red Blob Games on Grids](http://www-cs-students.stanford.edu/~amitp/game-programming/grids/)
- [Red Blob Games on Hex Grids](https://www.redblobgames.com/grids/hexagons/)
- [Quasicrystals](https://en.wikipedia.org/wiki/Quasicrystal)
- [Penrose Tiling](https://en.wikipedia.org/wiki/Penrose_tiling)
- [Geometric Honeycomb](https://en.wikipedia.org/wiki/Honeycomb_(geometry))
- [Beta-Skeletons](https://en.wikipedia.org/wiki/Beta_skeleton)
- [Islamic Patterns](https://patterninislamicart.com/drawings-diagrams-analyses)
- [Convex Hulls](https://en.wikipedia.org/wiki/Convex_hull)
- [*Rule of Six*](http://arandalasch.com/works/rules-of-six/) by Aranda Lasch
- [Algorithmic Patterns for Façade Design](apfd.pdf) by Inês Caetano
- [Paneling methods on complex surfaces](http://www.gasathj.com/tiki-read_article.php?articleId=31) by Matteo Codignola & Vito Sirago
- [Process(ing): Generative Irregular Grid](https://medium.com/@mishaheesakkers/process-ing-generative-irregular-grid-8f0d712dfaa4) by Misha Heesakkers
- [Sand Glyphs](https://inconvergent.net/generative/sand-glyphs/) by Inconvergent (Anders Hoff)
- [Seed Cathedral](http://www.heatherwick.com/project/uk-pavilion/) by Thomas Heatherwick
- [Geometricism](http://geometricism.com) by David Wade
- [Esther Stocker](https://www.sightunseen.com/2010/02/esther-stocker-artist/)

-----

#### Delaunay Triangulation

![del](https://i.pinimg.com/originals/76/c1/a2/76c1a2a0222ff50861797b6152db8aa2.jpg)

Developed in the 1930s by Russian geometer [Boris Delaunay](https://en.wikipedia.org/wiki/Boris_Delaunay), the [Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation) is essential to nearly all computer graphics. Whenever you hear or talk about a 'mesh', that's likely based on a Delaunay Triangulation! Videogames, visual effects for cinema, medical scanning, arcGIS geographic data — everything! It is also in heavy use by structural engineers, and unintentionally undergirds nearly all of the truss geometries that define bridges, attics, and other triangular structures as well as communication network routing. More recently, as autonomous vehicles begin to explore unmapped areas where sensors may fail, Delaunay Triangulation logic is used to [allow intelligent agents to navigate dangerous boundaries](https://en.wikipedia.org/wiki/Constrained_Delaunay_triangulation). 

In 3D space, the triangulation creates a *network topography* of triangular cells, based on known points to support, which would use the minimal amount of connective material to maintain, in opposition to a *singular force vector*. Imagine the Delaunay set as the circus net for trapeze artists, which would stretch and deform as the gymnasts fall into it and bounce around in it. That same net would not work very well to catch someone launched into it from the side...

- Sprinkle random points on a 2D plane
- Draw all possible circles defined by any set of 3 proximal points
- If those circles contain *any* of the other sprinkled points, that circle should be discarded
- If a circle passes the test, then draw the [circumscribed triangle](https://en.wikipedia.org/wiki/Circumscribed_circle) as an edge

![delaunay supports](http://codingcity.org/wp-content/uploads/2015/07/renderingplaza2.jpg)


#### Voronoi Tesselation

![voronoi](http://datagenetics.com/blog/may12017/anim2.gif)

![del vor](http://meemoo.org/images/delaunay_voronoi_dual.gif)

The geometric [*dual*](https://en.wikipedia.org/wiki/Dual_polyhedron) of the Delaunay Triangulation, [Voronoi Tesselation](https://en.wikipedia.org/wiki/Voronoi_diagram) invented by another amazing Russian mathematician — [Georgy Voronoi](https://en.wikipedia.org/wiki/Georgy_Voronoy) — similarly tiles a plane with shapes — though not not usually triangles. The unusual cells that come out of the Voronoi Tesselation model fairly accurately a multitude of natural formal phenomena as well as behaviors. Bone microstructure, sponge anatomy, soil clumping, termite and bee architecture, neuron network arrangement.... the list is almost endless. This is because the Voronoi Tesselation models an *efficient* set of cells. All of the space within a single Voronoi cell is *closer* to the centroid of a Delaunay triangle, and as a result, Voronoi logic approximates how any agent might make a decision about which of a set of possible choices should be chosen based purely on efficiently traversing or covering a plane or volume. It is increasingly being used by public policymakers to [place train stops, design road networks](http://datagenetics.com/blog/may12017/index.html), and [predict crime](https://www.tandfonline.com/doi/abs/10.1080/00330124.2017.1288578?scroll=top&needAccess=true&journalCode=rtpg20).

- Generate a Delaunay Triangulation
- Find the midpoint of each edge, and draw a line perpendicular to the edge
- Intersect all these lines, and clip adjacent lines with one another
- Draw the remnant, irregular polygons

![bone](https://afinemesh.files.wordpress.com/2014/04/printed-voronoi.jpg)


-----


-----

### Homework

##### Grasshopper (1.5 hours)

Please recreate the *Distance-Based Circles* example above. It is very similar to the *Deformable Mesh* variant we completed in class, and you might be able to build it already with the skills you have! 

Then, consider the *Attractor/Repulsor* and *Patterns through Random Projection* examples above. Feel free to start by downloading the examples, though there will certainly be better learning outcomes if you *start from scratch* and try to build the parts that seem familiar first before adding the new methods necessary to make these examples function as animated above (vector and domain construction, respectively).


##### Listening and Watching I (.5 hours)

Read a short case-study by Sidewalk Lab describing their neighborhood design tool: [*A first step toward the future of neighborhood design*](https://www.sidewalklabs.com/blog/a-first-step-toward-the-future-of-neighborhood-design/) as well as this [short interview](https://www.youtube.com/watch?v=-SoqN4GBpTM) with Chicago-native architect Jeanne Gang. If interested, you can read more about *Solar Carve* on [Studio Gang's website](https://studiogang.com/project/40-tenth-ave). All these pieces discuss how generative design tools allow creators to embed a non-human intelligence about environmental phenomena into their designed outcomes.

We will soon be exploring combinatorial design and more data-oriented generative approaches, so hopefully these teasers will be inspirational despite their location in urban planning and architecture rather than traditional design.


##### Listening and Watching II (1 hour)

Moving laterally a bit, but relating to our dive into generative music last week, let us investigate works in *generative literature* and *poetry*. **First**, visit [curated.ai](http://curatedai.com) and read through some of the poems hosted there. Please do not visit the "about" page until later.

Then, read through this recent New Yorker article on generative literature: [What Happens When Machines Learn To Write Poetry](https://www.newyorker.com/culture/annals-of-inquiry/the-mechanical-muse). Following that, read this short introduction to *curated.ai* at Popular Science [Artificial Intelligences Are Writing Poetry For A New Online Literary Magazine](https://www.popsci.com/ai-poetry-literary-magazine/). 

I hope we can have a robust argument about whether this is amazing, or terrible, next week. :confused:


##### Visualization Practice (1 hour, spread out over week)

Take a look at the Dear Data week forty-six on *Books We Own* in preparation for next week. Through the week, construct a dataset for your own visualization purposes on a set of related content items that you own (not necessarily books -- consider real and digital possessions such as videogames, movies, collectibles, tableware...), and produce 3 visualizations on 5"x7" carts. Explore both 2D and 3D visualization opportunities, and prepare to share these with your peers. Crayons, color pencils, and play-doh are available in the faculty corridor on Zach's desk. Add a legibility key to the backs of all visualizations, and bring these in to share next week.


##### Catching Up

Please continue to submit homework from the last several weeks, if you have not already, into the appropriate folders in the class Google Drive.