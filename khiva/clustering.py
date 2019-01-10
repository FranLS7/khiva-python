#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Shapelets.io
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

########################################################################################################################
# IMPORT
########################################################################################################################
import ctypes
from khiva.library import KhivaLibrary
from khiva.array import Array


########################################################################################################################


def k_Shape(arr, k, tolerance=10e-10):

    indexes = ctypes.c_void_p(0)
    centroids = ctypes.c_void_p(0)

    KhivaLibrary().c_khiva_library.kShape(ctypes.pointer(arr.arr_reference),
                                          ctypes.pointer(ctypes.c_int(k)),
                                          ctypes.pointer(ctypes.c_float(tolerance)),
                                          ctypes.pointer(indexes),
                                          ctypes.pointer(centroids))
    return Array(array_reference=indexes), Array(array_reference=centroids)
