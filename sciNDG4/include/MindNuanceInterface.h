// ----------------------------------------------------------------------------
///  \file   MindNuanceInterface.h
///  \brief
///  
///  \author  A Laing <a.laing@physics.gla.ac.uk>
///  \author  J Martin-Albo <jmalbos@ific.uv.es>
///  \date    17 March 2009
///  \version $Id: MindNuanceInterface.h 543 2014-11-01 23:03:10Z  $
///
///  Copyright (c) 2009 - IFIC Neutrino Group
// ----------------------------------------------------------------------------

#ifndef __NUANCE_INTERFACE__
#define __NUANCE_INTERFACE__

#include <G4VPrimaryGenerator.hh>
#include <globals.hh>
#include <fstream>


#include "MindConfigService.h"
#include "MindParamStore.h"
#include "MindDetectorConstruction.h"
#include "SciNearDetectorGeometry.h"
#include "MindLookupTable.h"

#include <G4RunManager.hh>
#include <G4VUserDetectorConstruction.hh>
#include <Randomize.hh>
#include <G4Material.hh>
#include <G4PrimaryParticle.hh>

#include <bhep/bhep_svc.h>

class G4ParticleDefinition;
class G4PrimaryParticle;
class G4Event;

using namespace CLHEP;

class MindNuanceInterface: public G4VPrimaryGenerator
{
public:
  /// Constructor
  MindNuanceInterface();
  /// Destructor
  ~MindNuanceInterface() {}
  
  void GeneratePrimaryVertex(G4Event*);

private:
  void Initialize();

  
  G4PrimaryParticle*
    CreatePrimaryParticle(G4int PDG, G4double eng, G4ThreeVector dir, bool pLep=false);
  G4String InteractionType(G4int code);

  G4int SelectVertexRegion();
  G4ThreeVector GetRandomVertex();
  G4double GetTargetProb();    

private:
  std::ifstream _nuanceFiles[2]; ///< Nuance input data files
  
  G4ParticleDefinition* _particle_definition;
  G4double _mass; ///< Particle mass
  G4double _charge; ///< Particle charge
  G4int _vert_mat;
  G4double _FeTargetProp;
  G4String _vtx_location;

  bool _tasd; //< a tasd detector?

  //Vertex in the case a fixed point is requested.
  G4int _fvecReg;
  G4ThreeVector _fvec;

  bool _runStart; //<Used if fixed vertex required.

  bhep::vdouble _had4P;

};

#endif
