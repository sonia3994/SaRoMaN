import os

class print_config:

	def __init__(self,GenerationMode):
		self.GenerationMode = GenerationMode

	def print_file(self,filename,data):
	    '''
	    Print data to file filename.
	    '''
	    outfile = open(filename,'w+')
	    outfile.write(data)
	    outfile.close()

	def print_digi_config(self,dictionary,filename):

		filedata = self.print_general('CON',dictionary)
		self.print_file(filename,filedata)

	def print_mindG4_config(self,dictionary,filename):

		filedata = self.print_general('GEOMETRY',dictionary)

		if(self.GenerationMode == 'SINGLE_PARTICLE'):
			filedata += '''

### Three generators, SINGLE_PARTICLE, NUANCE and GENIE, with different
### configuration parameters, are available. The first is chosen
### as default. Comment out the following lines if you want to
### use the latter.
GENERATION generator S SINGLE_PARTICLE


GENERATION particle_name S %(part)s

### Particle energy will be sample between these two values (in GeV)
GENERATION energy_min    D 0.300
GENERATION energy_max    D 3.000

'''% dict(dictionary, **vars(self))
		elif(self.GenerationMode == 'GENIE'):
			filedata += '''
GENERATION generator S GENIE
'''% dict(dictionary, **vars(self))			

		

		filedata += '''
### JOB options ###########################################
JOB output_dst    S %(out_base)s/G4_out/nd_%(part)s%(inttype)s/nd_%(part)s%(inttype)s_%(seed)d.dst.root
JOB number_events I %(Nevts)s

JOB random_seed I 13243%(seed)d

### GEOMETRY configuration parameters #####################

### Uncomment if you want to simulate TASD.
## Sets all volumes as sensitive detectors.
## Remember to use G4_POLYSTYRENE as passive_material as well!!.
# GEOMETRY TASD I 0

### Air gaps between layers (in mm)
GEOMETRY gap1 D 2.5
GEOMETRY gap2 D 2.5
GEOMETRY gap3 D 2.5
GEOMETRY gap4 D 2.5

### MAgnetic field. Still uniform vector.(T)
## A single bit to turn the uniform field off in favour of a toroidal field
GEOMETRY isUniform I 0

# if uniform then [bx,by,bz]. if toroidal then [br,btheta,bphi]
GEOMETRY field DV 3
0.
1.
0.

# If we wish to use a field map then the identity of the field map
# must be entered here.
GEOMETRY FieldMap S %(field_map_full_name)s

GEOMETRY FieldScaling D %(Bfield)d

### GENERATION configuration parameters ################### 

### NUANCE/GENIE data files for passive and active materials!! Set the filenames here!!

GENERATION active_material_data S %(out_base)s/genie_samples/nd_%(part)s%(inttype)s/ev0_%(ASeed)s_%(pid)d_1000060120[0.922582],1000010010[0.077418]_%(Nevts)s.root
GENERATION passive_material_data S %(out_base)s/genie_samples/nd_%(part)s%(inttype)s/ev0_%(seed)d_%(pid)d_1000260560_%(Nevts)s.root
#
### Vertex location (RANDOM, ACTIVE, PASSIVE, FIXED, GAUSS).
GENERATION vertex_location S GAUSS


### Special simulation for training purpose
### Use the muon but not the hadronization from GENIE
# GENERATION FSL_Select I 0

# Vertex if FIXED requested.
GENERATION fvert DV 3
0.
0.
-1000
 
GENERATION bspot DV 2
100.
100.

### PHYSICS configuration parameters ######################

### Production cut (in mm) for secondaries
PHYSICS production_cut D 30.
#
### Minimum Kinetic energy for a particle to be tracked (MeV).
PHYSICS minimum_kinEng D 100.
'''% dict(dictionary, **vars(self))

		self.print_file(filename,filedata)

	def print_rec_config(self,dictionary,filename):
		filedata = self.print_general('RUN',dictionary)

		filedata += '''

#############################################
#  parameters for the setup
#############################################

# relative density, Sc/Fe, AIR/Sc.
RUN rel_denSI D 0.135
RUN rel_denAS D 0.001

# Attenuation in Wavelength shifting fibre
RUN WLSatten D 5000.

# measurement type.
RUN meas_type S xyz

# magnetic field.
RUN mag_field DV 3
0.
1.
0.

RUN mag_field_map S %(field_map_full_name)s

RUN fieldScale D %(seed)d
########

# energy loss (MeV/cm)
# 1.5 cm Fe, 2 cm Sc, 1.0 cm Air
# RUN de_dx_min D 0.5323 
# 2 cm Fe, 2 cm Sc
# RUN de_dx_min D 0.637  
# 1.5 cm Fe, 1.5 cm Sc, 0.5 cm Air
# RUN de_dx_min D 0.6484
# 1.5 cm Fe, 1.5 cm Sc, 0.5 cm Air, 0.1 cm Aluminum
RUN de_dx_min D 0.575
# 3 cm Fe, 2 cm Sc
# RUN de_dx_min D 0.757
RUN de_dx_scint D 0.205

# Position resolution for detector (cm).
RUN pos_res D 0.75

# Step size for track fitting (cm).
RUN StepSize D 1.

# name of detector for hit getter.
RUN detect S tracking

########
# For hit clustering.(edge in cm)
RUN do_clust I 1
RUN rec_boxX D 2.0

# min energy at plane for detection (MeV) ***must be same as in digi!!***
RUN min_eng D 0.000016

# Seed for smear on cluster position.NOT USED!! NEEDS TIDIED!
RUN Gen_seed D 373940592

# sigma (cm)
RUN pos_sig D 0.577
RUN zpos_sig D 0.433

#############################################
#  parameters for the analysis
#############################################

# monitor ntuple file
RUN out_file S %(out_base)s/rec_out/nd_%(part)s%(inttype)s/nd_%(part)s%(inttype)s_%(seed)d.root

#liklihood file.
RUN like_file S %(out_base)s/likelihoods/like_%(part)s_%(inttype)s_%(seed)d.root

# type of fit
RUN kfitter S kalman

# fitter model
RUN model S particle/helix

# verbosities for recpack services
ANA vfit I 0
ANA vmat I 0
ANA vnav I 0
ANA vmod I 0
ANA vsim I 0

# maximum chi2 for tracks
RUN chi2fit_max D 50

# maximum local chi2 for nodes (muon fit)
RUN chi2node_max D 20
RUN max_outliers I 5

# maximum local chi2 for nodes (pattern rec.)
RUN pat_rec_max_chi D 20
RUN pat_rec_max_outliers I 10
RUN max_consec_missed_planes I 3
# minimum proportion of planes used to not reject
# event failing consec planes cut
RUN min_use_prop D 0.7

# Stuff for skipper etc.
RUN maxBlobSkip D 0.2
RUN minBlobOcc D 2

# cuts on cellular automaton trajectories. separation in cm.
RUN max_sep D 7
RUN max_traj I 40
RUN accept_chi D 20
RUN max_coincidence D 0.5

# cut on the maximum number of reconstructed trajectories
RUN max_N_trajectories I 4

# lowest and highest number of hits required for fit.
RUN low_Pass_hits I 8
RUN high_Pass_hits I 500

# proportion of nodes which must be fir not to trigger backwards fit.
RUN low_fit_cut0 D 0.8

# proportion of nodes which must be fit to accept type 2 (free mu) interaction.
RUN low_fit_cut2 D 0.6

# Fiducial cuts. (reduction in z and reduction at both sides in x,y. cm)
RUN z_cut D 300
RUN x_cut D 50
RUN y_cut D 50

# fit data twice (0=false, 1=true)
ANA refit I 1

# multiplication factor for covariance in refit seed
ANA facRef D 10000.

# Relevant parameters for pattern recognition.
# Do Pattern recognition (0=false, 1=true)
ANA patRec I 1

# Min./Max. isolated hits for patRec seed.
ANA min_seed_hits I 7
ANA max_seed_hits I 20
ANA min_check_nodes I 3

# Minumum proportion of isolated hits for central p seed.
ANA min_iso_prop D 0.8

# additional variables for mutliple track analysis
ANA plane_occupancy I 10
ANA max_multOcc_plane I 10

# Bit to tell if require output of likelihood info.
RUN likeli I 1

###  data to read ###
DATA idst_files SV 1
%(out_base)s/digi_out/nd_%(part)s%(inttype)s/nd_%(part)s%(inttype)s_%(seed)d_digi.dst.root

###  data to write ###
#
# DATA odst_files SV 1
# /home/alaing/ntupElec/tnd_e.FITTED.gz
'''% dictionary

		self.print_file(filename,filedata)

#For rec and digi so far
	def print_general(self, inPreParam, dictionary):
		self.preParam = inPreParam


		filedata = '''
'''

		if(self.preParam == 'CON'):
			filedata+= '''
# number of events to be processed.
RUN nEvents I %(Nevts)d

# gausian sigma for smear (cm)
RUN Gaus_Sigma D 1.0

# energy smear (%%)
RUN Eng_Res D 0.11

# seed value for random generator
CON Gen_seed D 107311191

CON rec_boxX D 2.0
CON rec_boxY D 2.0

# minimum energy at plane to be detected.(MeV)
CON min_eng D 0.000016

DATA idst_files SV 1
%(out_base)s/G4_out/nd_%(part)s%(inttype)s/nd_%(part)s%(inttype)s_%(seed)d.dst.root

DATA odst_file S %(out_base)s/digi_out/nd_%(part)s%(inttype)s/nd_%(part)s%(inttype)s_%(seed)d_digi.dst.root
'''% dict(dictionary, **vars(self))

		filedata += '''

%(preParam)s IsOctagonal I %(MIND_type)s

# MIND dimensions (m)
%(preParam)s MIND_x D %(MIND_xdim)s
%(preParam)s MIND_y D %(MIND_ydim)s
%(preParam)s MIND_z D %(MIND_zdim)s
%(preParam)s vertex_x D %(MIND_vertex_xdim)s
%(preParam)s vertex_y D %(MIND_vertex_ydim)s
%(preParam)s vertex_z D %(MIND_vertex_zdim)s //vertexDepth
%(preParam)s ear_height D %(MIND_ear_ydim)s
%(preParam)s ear_width  D %(MIND_ear_xdim)s
%(preParam)s bore_diameter D %(MIND_bore_diameter)s

#Mind internal dimensions
%(preParam)s active_material S %(MIND_active_mat)s
%(preParam)s active_thickness D %(MIND_width_active)s //widthSc
%(preParam)s x0Sc D %(MIND_rad_length_active)s
%(preParam)s active_layers I %(MIND_active_layers)s //nlayers
%(preParam)s passive_material S %(MIND_passive_mat)s
%(preParam)s passive_thickness D %(MIND_width_passive)s //widthI
%(preParam)s x0Fe D %(MIND_rad_length_passive)s

%(preParam)s bracing_material S %(MIND_bracing_mat)s 
%(preParam)s bracing_thickness D %(MIND_width_bracing)s // widthAl

%(preParam)s air_gap D %(MIND_width_air)s //withA
%(preParam)s x0AIR D %(MIND_rad_length_air)s

'''% dict(dictionary, **vars(self))

		return filedata




