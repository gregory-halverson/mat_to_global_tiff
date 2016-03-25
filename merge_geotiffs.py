__author__ = 'Gregory Halverson, Trevor McDonald'

# python libraries

import gc

#from subprocess import call

import os

import gdal_merge

path = os.path.dirname(os.path.abspath(__file__))

# gdal_merge command constants
# PYTHON_COMMAND = 'python'
# GDAL_MERGE_SCRIPT = path + '/gdal_merge.py'
GDAL_MERGE_OUTPUT_FLAG = '-o'
GDAL_MERGE_NODATA_FLAG = '-n'

def merge_geotiffs(input_filenames, output_filename, nodata_value=None):
    if type(input_filenames) is str:
        input_filenames = [input_filenames]

    output_filename_option = [GDAL_MERGE_OUTPUT_FLAG, output_filename]

    #gdal_merge_command = [PYTHON_COMMAND, GDAL_MERGE_SCRIPT]

    gdal_merge_args = output_filename_option

    if nodata_value:
        nodata_option = [GDAL_MERGE_NODATA_FLAG, str(nodata_value)]
        gdal_merge_args += nodata_option

    gdal_merge_args += input_filenames

    #gdal_merge_command += gdal_merge_args
    #print("running command: %s" % ' '.join(gdal_merge_command))
    #call(gdal_merge_command)

    gdal_merge_argv = ['gdal_merge'] + gdal_merge_args

    gdal_merge_argv = [str(arg) for arg in gdal_merge_argv]

    print('')
    print('running command: %s' % ' '.join(gdal_merge_argv))
    print('')

    gc.collect()

    try:
        gdal_merge.main(gdal_merge_argv)
    except MemoryError:
        print('')
        print('gdal_merge ran out of memory')
        print('')

    gc.collect()