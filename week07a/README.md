# Week 7 · Meshes

Let us spend some time analyzing how 3D meshes are put together, as some of the most exciting approaches in generative design are built on hacking these fundamental 3D representational structures. 


-----


### References for the Week

#### Information on Meshes

#### Mesh Sources

- [Google Poly](poly.google.com)
- [Turbo Squid]()
- [GrabCAD]()


-----


### Meshes

#### Vertices -> Edges -> Faces -> Meshes

![mrdiv](mrdiv.gif) 

##### From the excellent [Mr. Div](https://mrdiv.tumblr.com)

A 3D mesh is file a simple data structure. At its heart are four geometric entitites.

- Vertex (often called 'vees' or 'verts' :rage:) · A point in 3D space
- Edge (sometimes in aggregate called 'loops') · A 2D connection between two vertices. Often, these are left out and can be inferred
- Triangular Face (always 'tris')· A collection of three vertices defining a triangular surface (always planar)
- Quadrangular Face (always 'quads' or 'queues') · A collection of four vertices defining a quadrilateral surface (planar or twisted)

Additionally, faces have additional properties that can sometimes be left out or inferred.

- Normal · A vector perpendicular to a face, defining its *outside*
- Winding · The ordering of the faces, *clockwise* or *counter-clockwise*
- Texture Coordinates · How the vertices of the face should relate to *pixel values* of an image that is designed to cover the 3D mesh.

These data entities are coded explicitly in 3d files. Here are the contents of a simple 'wavefront' .obj file. You would find similar contents in an .stl 'stereolithography' file or many other filetypes, which structure the same data similarly.

```
# Rhino

v 0 1 0
v 1 2 0
v 1 2.220446049250313e-16 0
v 2 1 0
f 4 2 1
f 4 1 3
```

The first line is a comment, which by convention names the program that created the file.

The following lines beginning with "v" are vertex coordinates, and refer to position in 3D space. Note the weird decimal number, due to a tolerance error from Rhino.

The final lines beginning with "f" are triangular faces. The integers that follow are *indices* of vertices, starting confusingly at 1. The indices are wound, by .obj convention, *counter-clockwise*, which means we do not need to notate the normals of these faces to define their directionality.

The file itself defines a singular 3D mesh, which looks like this:

![simple](simple.png)


#### Learning about Meshes : Nefertiti Hack

![nef](nef.png)

Take a look at this [fantastically controversial endeavor](http://nefertitihack.alloversky.com) by German artists Nora Al-Badri and Jan Nikolai Nelles to [digitally repatriate](https://ncph.org/history-at-work/repatriation-and-decolonization/) a famous bust of Queen Nefertiti excavated from Egypt and now located in the [Neues Museum in Berlin](https://www.smb.museum/en/museums-institutions/neues-museum/collections-research/about-the-collection.html). Even the [controversy is controversial](https://hyperallergic.com/281739/could-the-nefertiti-scan-be-a-hoax-and-does-that-matter/). 

Download a [simplified verison of this mesh](nefertiti-95reduced.obj) to peek at as a class.

BTW: [Others are continuing](https://www.myminifactory.com/scantheworld/) this initiative for other museum artefacts!

-----

#### Catmull Clark Subdivision

![catmull clark](cc.png)

[Catmull Clark Subdivision](https://en.wikipedia.org/wiki/Catmull–Clark_subdivision_surface) is amazing! This algorithm, developed by Pixar engineer-turned-President [Edwin Catmull](https://en.wikipedia.org/wiki/Edwin_Catmull) and author of [Creativity, Inc.](https://www.amazon.com/Creativity-Inc-Overcoming-Unseen-Inspiration-ebook/dp/B00FUZQYBO) and his friend and colleague [Jim Clark](https://en.wikipedia.org/wiki/James_H._Clark), the founder of Netscape and inventor of several critical 3D rendering technologies for animation, cinema, and video games.

The Catmull-Clark subdivision is a simple, iterative process.

- Take each edge of a 3d mesh
- Split each edge and create a new vertex at the center of each face, and connect the new vertex to all the split edges
- Find the average coordinates of the original vertex, the face center vertex, and the split edge vertex
- Move the original vertex to this new, average coordinate and rebuild the mesh

The resulting forms are more *continuous* that the original mesh, with any harsh edges smoothed out. The one flaw is that the new mesh is inherently *heavier*: it has significantly more face and vertices. The characteristic aesthetic of Pixar films, which has directly inspired most other 3D animation companies, is [fundamentally due to the Catmull-Clark algorithm](https://graphics.pixar.com/library/Geri/paper.pdf).

![sulley](subD.jpg)

Play with Pixar in a Box's amazing [interactive tool](https://www.khanacademy.org/partner-content/pixar/modeling-character/modeling-subdivision/p/interactive-subdivision-in-3d)) to get a feel for this simple but surprisingly powerful algorithm.

-----

### Grasshopper Mesh Manipulation

Let's take a look at how the Nefertiti mesh is constructed as an exemplar of the mesh data structure, and learn a bit about how the simple structure can be algorithmically manipulated.

[Download](deform-definition.gh)

![Grasshopper Definition](deform-grasshopper.png)

![Grasshopper Screenshot](deform-screenshot.png)

-----

### Homework

##### Grasshopper (1 hour)


##### Listening and Watching I (1 hour)


##### Visualization Practice (1 hour, spread out over week)


##### Submit Work

Please submit homework into the appropriate folders in the class Google Drive.












SUBSTRATE???


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

