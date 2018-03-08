"""
Copyright (c) 2018 Grumpy Cat Software S.L.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

########################################################################################################################
# IMPORT
########################################################################################################################
import ctypes
import numpy as np
import time
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

########################################################################################################################

def find_best_n_discords(profile_list, index_list, n, c_tsa_library):
    """

    :param profile_list:
    :param index_list:
    :param n:
    :param c_tsa_library:
    :return:
    """

    start= time.time()

    profile_c_double_array = (ctypes.c_double * len(profile_list))(*profile_list)
    index_c_double_array = (ctypes.c_uint32 * len(index_list))(*index_list)

    initialized_discord_distance_array = np.zeros(n).astype(np.double)
    initialized_discord_index_array = np.zeros(n).astype(np.int)
    initialized_subsequence_index_array = np.zeros(n).astype(np.int)


    c_discord_distance = (ctypes.c_double * n)(*initialized_discord_distance_array)
    c_discord_index = (ctypes.c_int * n)(*initialized_discord_index_array)
    c_subsequence_index = (ctypes.c_int * n)(*initialized_subsequence_index_array)


    logging.info("Time conversioning to C types:" + str(time.time() - start))

    c_tsa_library.find_best_n_discords(ctypes.pointer(profile_c_double_array),
                                     ctypes.pointer(index_c_double_array),
                                     ctypes.pointer(ctypes.c_long(len(profile_list))),
                                     ctypes.pointer(ctypes.c_long(n)),
                                     ctypes.pointer(c_discord_distance),
                                     ctypes.pointer(c_discord_index),
                                     ctypes.pointer(c_subsequence_index))

    np_discord_distance = np.array(c_discord_distance)
    np_discord_index = np.array(c_discord_index).astype(int)
    np_subsequence_index = np.array(c_subsequence_index).astype(int)

    return {'discord_distance': np_discord_distance, 'discord_index': np_discord_index, 'subsequence_index': np_subsequence_index}