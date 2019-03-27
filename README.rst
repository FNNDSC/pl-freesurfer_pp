pl-freesurfer_pp
================

.. image:: https://badge.fury.io/py/freesurfer_pp.svg
    :target: https://badge.fury.io/py/freesurfer_pp

.. image:: https://travis-ci.org/FNNDSC/freesurfer_pp.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/freesurfer_pp

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-freesurfer_pp

.. contents:: Table of Contents


Abstract
--------

``freesurfer_pp.py`` is a *dummy* FreeSurfer plugin that is prepopulated with the results of several FreeSurfer runs. For a given run, this script will copy, for a given internal target, the already created ``stats`` directory as well as two directories of png files -- one containing colored parcellations, and one with some 3D views.

Synopsis
--------

.. code::

    python z2labelmap.py                                            \
        [-v <level>] [--verbosity <level>]                          \
        [--random]                                                  \
        [-p <f_posRange>] [--posRange <f_posRange>]                 \
        [-n <f_negRange>] [--negRange <f_negRange>]                 \
        [-P <'RGB'>] [--posColor <'RGB'>]                           \
        [-N  <'RGB'> [--negColor <'RGB'>]                           \
        [-s <f_scaleRange>] [--scaleRange <f_scaleRange>]           \
        [-l <f_lowerFilter>] [--lowerFilter <f_lowerFilter>]        \
        [-u <f_upperFilter>] [--upperFilter <f_upperFilter>]        \
        [-z <zFile>] [--zFile <zFile>]                              \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>                                                  \
        <outputDir> 

Run
----



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
