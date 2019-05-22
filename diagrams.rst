In sphinx you can include inline math :math:`x\leftarrow y\ x\forall
y\ x-y` or display math

.. math::

  W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]



Inheritance diagrams
--------------------

Inheritance diagrams can be inserted directly into the document by
providing a list of class or module names to the
``inheritance-diagram`` directive.

For example::

  .. inheritance-diagram:: codecs


produces:

.. inheritance-diagram:: codecs



.. _sphinx_literal:

This file
---------

.. literalinclude:: doc.rst


Bob->Alice : hello



.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }


.. graphviz::


   graph ER {
       node [shape=box]; course; institute; student;
       node [shape=ellipse]; {node [label="name"] name0; name1; name2;}
           code; grade; number;
       node [shape=diamond,style=filled,color=lightgrey]; "C-I"; "S-C"; "S-I";

       name0 -- course;
       code -- course;
       course -- "C-I" [label="n",len=1.00];
       "C-I" -- institute [label="1",len=1.00];
       institute -- name1;
       institute -- "S-I" [label="1",len=1.00];
       "S-I" -- student [label="n",len=1.00];
       student -- grade;
       student -- name2;
       student -- number;
       student -- "S-C" [label="m",len=1.00];
       "S-C" -- course [label="n",len=1.00];

       label = "\n\nEntity Relation Diagram\ndrawn by NEATO";
       fontsize=20;
   }

.. graphviz::

     digraph example {
         a [label="sphinx", href="http://sphinx-doc.org", target="_top"];
         b [label="other"];
         a -> b;
     }

.. graphviz::

   digraph foo {
     node [style=rounded]
     node1 [shape=box]
     node2 [fillcolor=yellow, style="rounded,filled", shape=diamond]
     node3 [shape=record, label="{ a | b | c }"]

     node1 -> node2 -> node3
   }


.. graphviz::

   digraph foo {
    PlantUML -> Dot [label=use];
   }

.. graphviz::

   digraph G {
           fontname = "Bitstream Vera Sans"
           fontsize = 8

           node [
                   fontname = "Bitstream Vera Sans"
                   fontsize = 8
                   shape = "record"
           ]

           edge [
                   fontname = "Bitstream Vera Sans"
                   fontsize = 8
           ]

           Animal [
                   label = "{Animal|+ name : string\l+ age : int\l|+ die() : void\l}"
           ]

           Dog [
                   label = "{Dog||+ bark() : void\l}"
           ]

           Cat [
                   label = "{Cat||+ meow() : void\l}"
           ]

           edge [
                   arrowhead = "empty"
           ]

           Dog -> Animal
           Cat -> Animal
   }


I am trying to have a diagram here...

.. inheritance-diagram:: BaseClass DerivedClass
   :parts:2

.. graphviz::

   digraph {
      "From here" -> "To" -> "Somewhere";
      "From here" -> "To" -> "Somewhere else";
   }

.. graphviz::

   digraph g {
         graph [
         rankdir = "LR"
         ];
         node [
         fontsize = "16"
         shape = "ellipse"
         ];
         edge [
         ];
         "node0" [
         label = "<f0> 0x10ba8| <f1>"
         shape = "record"
         ];
         "node1" [
         label = "<f0> 0xf7fc4380| <f1> | <f2> |-1"
         shape = "record"
         ];
         "node2" [
         label = "<f0> 0xf7fc44b8| | |2"
         shape = "record"
         ];
         "node3" [
         label = "<f0> 3.43322790286038071e-06|44.79998779296875|0"
         shape = "record"
         ];
         "node4" [
         label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
         shape = "record"
         ];
         "node5" [
         label = "<f0> (nil)| | |-1"
         shape = "record"
         ];
         "node6" [
         label = "<f0> 0xf7fc4380| <f1> | <f2> |1"
         shape = "record"
         ];
         "node7" [
         label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
         shape = "record"
         ];
         "node8" [
         label = "<f0> (nil)| | |-1"
         shape = "record"
         ];
         "node9" [
         label = "<f0> (nil)| | |-1"
         shape = "record"
         ];
         "node10" [
         label = "<f0> (nil)| <f1> | <f2> |-1"
         shape = "record"
         ];
         "node11" [
         label = "<f0> (nil)| <f1> | <f2> |-1"
         shape = "record"
         ];
         "node12" [
         label = "<f0> 0xf7fc43e0| | |1"
         shape = "record"
         ];
         "node0":f0 -> "node1":f0 [
         id = 0
         ];
         "node0":f1 -> "node2":f0 [
         id = 1
         ];
         "node1":f0 -> "node3":f0 [
         id = 2
         ];
         "node1":f1 -> "node4":f0 [
         id = 3
         ];
         "node1":f2 -> "node5":f0 [
         id = 4
         ];
         "node4":f0 -> "node3":f0 [
         id = 5
         ];
         "node4":f1 -> "node6":f0 [
         id = 6
         ];
         "node4":f2 -> "node10":f0 [
         id = 7
         ];
         "node6":f0 -> "node3":f0 [
         id = 8
         ];
         "node6":f1 -> "node7":f0 [
         id = 9
         ];
         "node6":f2 -> "node9":f0 [
         id = 10
         ];
         "node7":f0 -> "node3":f0 [
         id = 11
         ];
         "node7":f1 -> "node1":f0 [
         id = 12
         ];
         "node7":f2 -> "node8":f0 [
         id = 13
         ];
         "node10":f1 -> "node11":f0 [
         id = 14
         ];
         "node10":f2 -> "node12":f0 [
         id = 15
         ];
         "node11":f2 -> "node1":f0 [
         id = 16
         ];
   }