Diagram class Sphere
====================


.. graphviz::

   digraph hierarchy {
      size="5,5"
      node[shape=record,style=filled,fillcolor=gray95]
      edge[dir=back, arrowtail=empty]


      1[label = "{SphereBase|_dimension = None|+getDimension()\n+checkPointInSphere()\n+createRandomPointInSphere()\n+createConretePoint()}"]
      2[label = "{Sphere1D|_dimension = 1|+getDimension()\n+checkPointInSphere()\n+createRandomPointInSphere()\n+createConretePoint()}"]
      3[label = "{Sphere2D|_dimension = 2|+getDimension()\n+checkPointInSphere()\n+createRandomPointInSphere()\n+createConretePoint()}"]
      4[label = "{Sphere3D|_dimension = 3|+getDimension()\n+checkPointInSphere()\n+createRandomPointInSphere()\n+createConretePoint()}"]

      1->2
      2->3
      3->4
   }

