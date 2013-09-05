// -*- C++ -*-
//
// Package:    SingleMuonGun
// Class:      SingleMuonGun
// 
/**\class SingleMuonGun SingleMuonGun.cc SingleMuonGun/src/SingleMuonGun.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Yuriy Pakhotin,,,
//         Created:  Wed Sep  4 13:36:33 CDT 2013
// $Id: SingleMuonGun.cc,v 1.1 2013/09/04 18:37:43 pakhotin Exp $
//
//

// system include files
#include <memory>
#include <string>
#include <ostream>
#include <iostream>
#include "boost/shared_ptr.hpp"

// user include files
#include "HepPDT/defs.h"
#include "HepPDT/TableBuilder.hh"
#include "HepPDT/ParticleDataTable.hh"

#include "HepMC/GenEvent.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/one/EDProducer.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"

#include "CLHEP/Random/JamesRandom.h"
#include "CLHEP/Random/RandFlat.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"

using namespace edm;
using namespace std;
using namespace CLHEP;

namespace {
  CLHEP::HepRandomEngine& getEngineReference()
  {

    Service<RandomNumberGenerator> rng;
    if(!rng.isAvailable()) {
      throw cms::Exception("Configuration")
       << "The RandomNumberProducer module requires the RandomNumberGeneratorService\n"
          "which appears to be absent.  Please add that service to your configuration\n"
          "or remove the modules that require it.";
    }
    // The Service has already instantiated an engine.  Make contact with it.
    return (rng->getEngine());
  }
}

//
// class declaration
//

class SingleMuonGun : public edm::EDProducer {
  public:
    explicit SingleMuonGun(const edm::ParameterSet&);
    ~SingleMuonGun();

  private:
    virtual void beginJob();
    virtual void produce(edm::Event&, const edm::EventSetup&);
    virtual void endJob();
    
    virtual void beginRun(edm::Run&, edm::EventSetup const&);
    virtual void endRun(edm::Run&, edm::EventSetup const&);
      
  // ----------member data ---------------------------
  
  int    m_partID;
  double m_minPt;
  double m_maxPt;
  double m_minEta;
  double m_maxEta;
  double m_minPhi;
  double m_maxPhi;
  
  // the event format itself
  HepMC::GenEvent* m_Evt;
  
  ESHandle<HepPDT::ParticleDataTable> m_PDGTable;
            	    	
  int m_Verbosity;

  CLHEP::HepRandomEngine& m_RandomEngine;
  CLHEP::RandFlat*        m_RandomGenerator; 
  
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
SingleMuonGun::SingleMuonGun(const edm::ParameterSet& iConfig)
  : m_Evt(0)
  , m_RandomEngine( getEngineReference() )
  , m_RandomGenerator(0)
  , m_Verbosity( iConfig.getUntrackedParameter<int>( "Verbosity",0 ) )
  , m_partID(    iConfig.getParameter<int>("partID") )
  , m_minPt(     iConfig.getParameter<double>("minPt") )
  , m_maxPt(     iConfig.getParameter<double>("maxPt") )
  , m_minEta(    iConfig.getParameter<double>("minEta") )
  , m_maxEta(    iConfig.getParameter<double>("maxEta") )
  , m_minPhi(    iConfig.getParameter<double>("minPhi") )
  , m_maxPhi(    iConfig.getParameter<double>("maxPhi") )
{
  
  m_RandomGenerator = new CLHEP::RandFlat(m_RandomEngine);
  produces<HepMCProduct>();
  produces<GenEventInfoProduct>();
  produces<GenRunInfoProduct, InRun>();
  
}


SingleMuonGun::~SingleMuonGun()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool SingleMuonGun::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
  if ( m_Verbosity > 0 ) cout << " SingleMuonGunProducer : Begin New Event Generation" << endl;
  
  m_Evt = new HepMC::GenEvent();
  
  HepMC::GenVertex* Vtx = new HepMC::GenVertex( HepMC::FourVector(0.,0.,0.) );
  
  double pt  = fRandomGenerator->fire(m_minPt,  m_maxPt);
  double eta = fRandomGenerator->fire(m_minEta, m_maxEta);
  double phi = fRandomGenerator->fire(m_minPhi, m_maxPhi);
  
  const HepPDT::ParticleData* PData = m_PDGTable->particle( HepPDT::ParticleID(abs(m_partID)) );
  
  double mass    = PData->mass().value();
  double theta   = 2.*atan(exp(-eta));
  double mom     = pt/sin(theta);
  double px      = pt*cos(phi);
  double py      = pt*sin(phi);
  double pz      = mom*cos(theta);
  double energy2 = mom*mom + mass*mass;
  double energy  = sqrt(energy2); 
  HepMC::FourVector p(px,py,pz,energy);
  HepMC::GenParticle* Part = new HepMC::GenParticle(p,m_partID,1);
  Part->suggest_barcode( 1 ) ;
  Vtx->add_particle_out(Part);
  
  m_Evt->add_vertex(Vtx) ;
  m_Evt->set_event_number(iEvent.id().event()) ;
  m_Evt->set_signal_process_id(20) ; 
  
  if ( m_Verbosity > 0 ) m_Evt->print() ;  
  
  auto_ptr<HepMCProduct> BProduct(new HepMCProduct()) ;
  BProduct->addHepMCData( m_Evt );
  iEvent.put(BProduct);

  auto_ptr<GenEventInfoProduct> genEventInfo(new GenEventInfoProduct(m_Evt));
  iEvent.put(genEventInfo);
  
  if ( m_Verbosity > 0 ) cout << " SingleMuonGunProducer : Event Generation Done" << endl;

}

// ------------ method called once each job just before starting event loop  ------------
void 
SingleMuonGun::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SingleMuonGun::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
SingleMuonGun::beginRun(edm::Run& iRun, edm::EventSetup const& iSetup)
{

  iSetup.getData( m_PDGTable ) ;
  return;

}

// ------------ method called when ending the processing of a run  ------------
void 
SingleMuonGun::endRun(edm::Run& iRun, edm::EventSetup const& iSetup)
{

//  auto_ptr<GenRunInfoProduct> genRunInfo( new GenRunInfoProduct() );
//  iRun.put( genRunInfo );

}

//define this as a plug-in
DEFINE_FWK_MODULE(SingleMuonGun);
