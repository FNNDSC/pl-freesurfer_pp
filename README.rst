################################
pl-freesurfer_pp
################################


Abstract
********

A "dummy" app containing the output of some prior FreeSurfer output which simply copies this to thput directory

Run
***

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-freesurfer_pp freesurfer_pp.py            \
            /incoming /outgoing

This will ...

Make sure that the host ``$(pwd)/out`` directory is world writable!







