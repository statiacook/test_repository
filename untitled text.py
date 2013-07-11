from astropy.io import fits
import numpy as np
import copy
import pylab
import math


path="../data/ssppOut-dr9.fits"
hdulist=fits.open(path)
img_data = hdulist[1].data
img_header = hdulist[1].header
data=img_data
args=["LOGG_ADOP", "FEH_ADOP", "TEFF_ADOP", "SPECTYPE_HAMMER"]
for arg in args:
	data.arg=np.array(img_data.field(arg))
