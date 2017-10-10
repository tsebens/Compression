# File compression class. Useful if you need to manage large numbers of files that are or need to be compressed

import gzip
import shutil
from subprocess import call

def getCmpCmd( i_fp, o_fp ):
	template = "zpaq/zpaq.exe a %s %s -m5" % ( o_fp, i_fp )
	return template
	
def getDcmpCmd( i_fp, o_fp ):
	template

# Accepts a file and compresses that file. Defaults to the same name in the same location with '.gz' appended. 
# Ouput location can be specified via o_fp
# Compression level can be specified via cmp_lvl
def compressFile( i_fp, o_fp='default' ):
	if o_fp == 'default':
		o_fp = i_fp + '.gz' # If output location has been specified, compress file into the same directory as the original.
	command = getCmpCmd( i_fp, o_fp )
	call( command ) # Execute the command
	

	
def main():
	fp = r"H:\CompressionTest\orig.mb58"
	compressFile( fp )
	
if __name__ == '__main__':
	main()