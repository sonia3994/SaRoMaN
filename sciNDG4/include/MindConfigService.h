/// ---------------------------------------------------------------------------
///  \file   MindConfigService.h
///  \brief  Run-time configuration management.
///
///  \author   J Martin-Albo <jmalbos@ific.uv.es>
///  \date     16 March 2009
///  \version  $Id: MindConfigService.h 543 2014-11-01 23:03:10Z  $
///  
///  Copyright (c) 2009 -- IFIC Neutrino Group
/// ---------------------------------------------------------------------------

#ifndef __INPUT_SERVICE__
#define __INPUT_SERVICE__

#include <iostream>
#include <globals.hh>

class MindParamStore;


/// Singleton class for run-time configuration management.
///
class MindConfigService
{
public:
  /// Returns the singleton class instance
  static MindConfigService& Instance();
  
  /// Initialize service with a configuration file
  void SetConfigFile(const G4String& config_file);

  /// Get the store with the geometry config parameters
  const MindParamStore& Geometry() const { return *_geometry; }
  /// Get the store with the generation config parameters
  const MindParamStore& Generation() const { return *_generation; }
  /// Get the store with the physics config parameters
  const MindParamStore& Physics() const { return *_physics; }
  /// Get the store with the actions config parameters
  const MindParamStore& Actions() const { return *_actions; }
  /// Get the store with the geometry config parameters
  const MindParamStore& Job() const { return *_job; }
  
  /// Method to access the configfile name
  const std::string FileName() const { return _config_file; }

private:
  /// constructor (hidden)
  MindConfigService();
  /// destructor (hidden)
  ~MindConfigService() {}
  /// copy-constructor (hidden)
  MindConfigService(MindConfigService const&);
  /// assignement operator (hidden)
  MindConfigService& operator=(MindConfigService const&);

private:
  MindParamStore* _geometry;
  MindParamStore* _generation;
  MindParamStore* _physics;
  MindParamStore* _actions;
  MindParamStore* _job;

  bool _init;

  std::string _config_file;
};

#endif
