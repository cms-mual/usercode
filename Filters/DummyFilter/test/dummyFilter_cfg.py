import FWCore.ParameterSet.Config as cms

import os
#inputfiles = os.environ["ALIGNMENT_INPUTFILES"].split(" ")
#jobnumber = int(os.environ["ALIGNMENT_JOBNUMBER"])



process = cms.Process("CHAMBERFILTER")

process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
        '/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4/e72a66c48f67453e57ae7abb7c7b6a5b/singleMuonGun_RECO_3064_1_yCu.root',
       '/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4/e72a66c48f67453e57ae7abb7c7b6a5b/singleMuonGun_RECO_3065_1_jqT.root'
    )
)


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring("cout"),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string("INFO")))

#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = "GR_R_53_V16A::All"

#process.load("Configuration.StandardSequences.Reconstruction_cff")
#process.load("Configuration.StandardSequences.GeometryDB_cff")
#process.load("Configuration.StandardSequences.MagneticField_38T_cff")

process.DummyFilter = cms.EDFilter("DummyFilter",
  filterAll      = cms.bool(True)
)

process.Path = cms.Path(process.DummyFilter)

process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("singleMuonGun_RECO_v4_Consolidated_v1.root"),
  SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("Path"))
)

process.EndPath = cms.EndPath(process.output)

