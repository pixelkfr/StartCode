#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt, sys, os, re

"""
Cleaner file base.
"""

def cleaner( input_file, output_file, log_file=None ):

    # Files - Initialization
    try:
        input_file_obj = open( os.path.abspath( input_file ), 'r' )
    except Exception, err:
        msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( input_file, err )
        sys.exit( msg.encode( 'UTF-8' ) )	
    try:
        output_file_obj = open( os.path.abspath( output_file ), 'a' )
    except Exception, err:
        msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( output_file, err )
        sys.exit( msg.encode( 'UTF-8' ) )
    if log_file:
        try:
            log_file_obj = open( os.path.abspath( log_file ), 'a' )
        except Exception, err:
            msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( log_file, err )
            sys.exit( msg.encode( 'UTF-8' ) )
    else:
        log_file_obj = sys.stdout

    # Cleaning
    for line in input_file_obj:
        output_file_obj.write("line")

		
if __name__ == "__main__":

    def usage():
        msg = """Usage: cleaner.py [-L LOG_FILE] INPUT_FILE OUTPUT_FILE
               -l --log=FILE		write log and errors in a FILE """
        sys.stderr.write( msg.encode( 'UTF-8' ) )
    try:
		opts, args = getopt.getopt( sys.argv[1:], "l:", ["log="] )
    except getopt.GetoptError, err:
        sys.stderr.write( str( err ) )
        usage()
        sys.exit(2)

    log_file = None
    for o, a in opts:
        if o in ( "-l", "--log" ):
            log_file = a.strip()
        else:
            assert False, "unhandled option"

    if len( args ) != 2:
        usage()
        sys.exit(2)
    else:
        input_file = args[0]
        output_file = args[1]

    cleaner( input_file, output_file, log_file )
