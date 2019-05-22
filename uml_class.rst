Diagram UML
===========


.. graphviz::

   digraph hierarchy {
      size="5,5"
      node[shape=record,style=filled,fillcolor=gray95]
      edge[dir=back, arrowtail=empty]


      2[label = "{AbstractSuffixTree|+ text\n+ root|...}"]
      3[label = "{SimpleSuffixTree|...| + constructTree()\l...}"]
      4[label = "{CompactSuffixTree|...| + compactNodes()\l...}"]
      5[label = "{SuffixTreeNode|...|+ addSuffix(...)\l...}"]
      6[label = "{SuffixTreeEdge|...|+ compactLabel(...)\l...}"]


      2->3
      2->4
      5->5[constraint=false, arrowtail=odiamond]
      4->3[constraint=false, arrowtail=odiamond]
      2->5[constraint=false, arrowtail=odiamond]
      5->6[arrowtail=odiamond]
   }



.. graphviz::

    digraph ele{

      rankdir=BT // Graph direction : Bottom-Top

      node [shape=record] // all nodes are in Box shape

      edge [dir=normal labeldistance=1] // "labeldistance=1" is default value



      // Multiplicity types by Crow's Foot Notation

      Member1 -> Group1 [dir=both arrowtail=crowodot arrowhead=teetee label="0or* to 1"]

      Member2 -> Group2 [dir=both arrowtail=teeodot arrowhead=teetee label="0or1 to 1"]

      Member3 -> Group3 [dir=both arrowtail=crowtee arrowhead=crowodot label="1or* to 0or*"]

    }