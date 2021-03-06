// ----------------------------------------------------------------------------
///  \file     MindPrimaryGeneration.h
///  \brief  
/// 
///  \author   J Martin-Albo <jmalbos@ific.uv.es>
///  \date     10 Feb 2009 
///  \version  $Id: MindPrimaryGeneration.h 543 2014-11-01 23:03:10Z  $
///
///  Copyright (c) 2009 -- IFIC Neutrino Group
// ----------------------------------------------------------------------------

#ifndef __PRIMARY_GENERATION__
#define __PRIMARY_GENERATION__

#include <G4VUserPrimaryGeneratorAction.hh>
#include "MindSingleParticle.h"
#include "MindNuanceInterface.h"
#include "MindGenieInterface.h"
#include "MindGenieEventInterface.h"
#include "MindCryInterface.h"
#include "MindConfigService.h"
#include "MindParamStore.h"

#include <G4Event.hh>


class G4VPrimaryGenerator;
class G4Event;

// using namespace CLHEP; 

class MindPrimaryGeneration: public G4VUserPrimaryGeneratorAction
{
public:
  /// Constructor
  MindPrimaryGeneration();
  /// Destructor
  ~MindPrimaryGeneration() {}

  /// Geant4 mandatory method for primary vertex/particle creation. 
  /// It is invoked by G4RunManager during the event loop.
  void GeneratePrimaries(G4Event*);

private:
  void Initialize();
  
private:
  G4VPrimaryGenerator* _generator; 
};

#endif
