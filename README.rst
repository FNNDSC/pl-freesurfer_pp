################################
pl-freesurfer_pp
################################


Abstract
********

A "dummy" app that contains some prior FreeSurfer output and simply copies this to the output directory.
Can selectively copy only the final text data outputs, or all internal generated images and surface meshes.

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







