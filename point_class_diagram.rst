Diagram class Point
====================


.. graphviz::

   digraph hierarchy {
      size="5,5"
      node[shape=record,style=filled,fillcolor=gray95]
      edge[dir=back, arrowtail=empty]


      1[label = "{PointBase|- _dimension = None|+ getDimension()\n+getDistanceFromCenter()\n+createRandomPointInSphere()\n+createConretePoint()}"]
      2[label = "{Point1D|- _dimension = 1|+ getDimension()\n+getDistanceFromCenter()\n+createRandomPointInSphere()\n+createConretePoint()}"]
      3[label = "{Point2D|- _dimension = 2|+ getDimension()\n+getDistanceFromCenter()\n+createRandomPointInSphere()\n+createConretePoint()}"]
      4[label = "{Point2D|- _dimension = 3|+ getDimension()\n+getDistanceFromCenter()\n+createRandomPointInSphere()\n+createConretePoint()}"]

      1->2
      2->3
      3->4
   }

