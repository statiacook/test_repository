from astropy.io import fits
import numpy as np
import copy
import pylab
import math

class Star(object):
	def __init__(self):
		self.fields = {}
	
#class DataFile(object,requiredfields=None):
class DataFile(object):
	def __init__(self, path):
		self.path = path
		datafile = fits.open(path)
		column_names = datafile[1].columns.names
		self.stars = [] #list of star objects, each with a dict of fields
		#for row in xrange(0,len(datafile[1].data.field('TEFF_ADOP')+1):
		x = True
		row=0
		print x
		#while x is True:
		#    try:
		#        stardata=datafile[1].data[row]
		#        if goodStar(stardata):
		        #    s=Star()
		        #    s.fields[column]=stardata.field(column)
		        #    self.stars.append(s)
		        #    row=row+1
		#    except IndexError:
		#        x=False
		        
def goodStar(stardata, badValue=-9999):
    goodvalues=True
    if (stardata["LOGG_ADOP"] == badValue) or (stardata["FEH_ADOP"] == badValue) or (stardata["TEFF_ADOP"]==badvalue):
        goodvalues=False
    return goodvalues
    
    
#### Good to here    
    
if __name__ == "__main__":
	df = DataFile("../data/ssppOut-dr9.fits")