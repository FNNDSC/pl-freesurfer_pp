pl-freesurfer_pp
=============

Abstract
********

This container houses some previously generated FreeSurfer output files (essentially the `stats` directory of a typical FreeSurfer run) and simply copies a given `stats` directory from inside the container to the plugin output directory.

Run
***

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. Note that the "input" directory is effectively ignored by this plugin, but is required.

In the simplest sense, the plugin can be run with

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-freesurfer_pp freesurfer_pp.py \
            /incoming /outgoing

which will copy the internal `stats` directory from a `05-yr/02-mo/04-da` subject to the output. Other choices are available. To get a listing of the internal tree of already processed and available FreeSurfer choices:

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-freesurfer_pp freesurfer_pp.py \
            -T ../preprocessed \
            /incoming /outgoing

This will print a tree of the available choices of `preprocessed` data in a directory tree. Select one, say the `08-yr/07-mo/16-da` and specify that to copy:

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-freesurfer_pp freesurfer_pp.py \
            -a 08-07-16 \
            /incoming /outgoing

To simulate a processing delay, specify some time in seconds:

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-freesurfer_pp freesurfer_pp.py \
            -a 08-07-16 \
            -P 20 \
            /incoming /outgoing

Make sure that the host ``$(pwd)/out`` directory is world writable!
