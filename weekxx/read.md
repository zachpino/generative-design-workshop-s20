#### Catmull Clark Subdivision

Catmull Clark Subdivision is amazing! We'll talk about it in class, it's very difficult to describe in words.

But, play with Pixar in a Box's amazing [interactive tool](https://www.khanacademy.org/partner-content/pixar/modeling-character/modeling-subdivision/p/interactive-subdivision-in-3d)) to get a sense of it.






#### After Vera Molnar / Jared Tarbell

Let's experiment with randomness to produce geometric patterns inspired by the works of [Molnár](http://www.veramolnar.com) and [Tarbell](http://www.complexification.net/gallery/), two extraordinary generative artists who work with controlled randomness towards new definitions of aesthetics.

[Download](random-pattern-definition.gh)

![Grasshopper Definition](random-pattern-grasshopper.png)

![Grasshopper Cubic Disarray Recreation](random-pattern-screenshot.png)

-----



### Food 4 Rhino

![grass,right?](rhino.gif)

[Food4Rhino](http://www.food4rhino.com) is a central repository for plugins and add-on software for Rhino 3D, as well as for Grasshopper. Plugins for plugins! 

Create a free account on the website and search around. Anything exciting? Unfortunately, not everything will work on Macs and it's impossible to know unless you see an Apple logo under the *Download* button. But, even if *there is not an Apple logo*, it still might work!

To install a Grasshopper plugin, open Grasshopper, and navigate to File -> Special Folders -> Components Folder.

This will open a Finder/Explorer window, into which you can move the downloaded folder. The best practice is usually to drag the entire folder over, not the individual .gha or .ghuser files. You can find Grasshopper plugins all over the internet, not just at Food4Rhino. If you are running Windows, right click on any .exe, .ghuser, and .gha files and click on *Properties*. Make sure to click *Unblock* if it is an option.

For Grasshopper to load newly installed plugins, we just need to restart Grasshopper. Either quit and restart Rhino, or alternatively, in *Rhino* type `Grasshopper unload plugin` and then relaunch Grasshopper.

For this and future exercises, let's install a few specific and essential plugins.

- For better Mesh cleanup: [Mesh Edit Tools *1.9* from Oct 1, 2016](https://www.food4rhino.com/app/meshedit)
- For better Mesh smoothing: [Weaverbird for Mac](http://www.giuliopiacentino.com/get-wb-no-admin/) or [Weaverbird for Windows](http://www.giuliopiacentino.com/get-wb/)

-----

### Grasshopper Definition


#### Image Sampler

Extract brightness data from an image and create a heightmap.

![imagesampler](imagesampler.png)

[imagesampler](imagesampler.gh)

![imagesampler](imagesampler_gh.png)

-----

#### 'Simple' Delaunay Triangulation

From a field of random points, create Delaunay triangulation

![delaunay](delaunay.png)

[delaunay](delaunay.gh)

![delaunay](delaunay_gh.png)

-----

#### Data-Driven Voronoi Cast

Create a voronoi tesselation in 3D space around a data-driven, anatomical form. Allow for variable cell openness based on attractor curve.

![voronoi_cast.png](voronoi_cast.png)

[voronoi_cast](voronoi_cast.gh)

![voronoi_cast_gh.png](voronoi_cast_gh.png)

-----

#### Data-Driven Delaunay Cast

Create a Delaunay triangulation in 3D space around a data-driven, anatomical form.

![delaunay_cast.png](delaunay_cast.png)

[delaunay_cast](delaunay_cast.gh)

![delaunay_cast_gh.png](delaunay_cast_gh.png)

-----

### Homework

Week off!





##### Image Sampler

Extract brightness data from an image and create 3D [heightmaps](https://en.wikipedia.org/wiki/Heightmap).

[Download](image-sampler-definition.gh)

![Grasshopper Definition](image-sampler-grasshopper.png)

![Grasshopper Walkthrough](image-sampler-screenshot.png)

##### After Molnár and Tarbell

Let's experiment with randomness to produce geometric patterns inspired by the works of [Molnár](http://www.veramolnar.com) and [Tarbell](http://www.complexification.net/gallery/), two extraordinary generative artists who work with controlled randomness and grids towards new aesthetic definitions. Take a regular grid, place polygons at every node, and distort every aspect of the resulting composition including polygon vertex count, rotation, placement, overall distortion, stroke color, fill color, stroke thickness...

[Download](random-pattern-definition.gh)

![Grasshopper Definition](random-pattern-grasshopper.png)

![Grasshopper Walkthrough](random-pattern-screenshot.png)

