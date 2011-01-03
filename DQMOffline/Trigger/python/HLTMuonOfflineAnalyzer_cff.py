import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.HLTMuonOfflineAnalyzer_cfi import hltMuonOfflineAnalyzer

globalMuons = cms.PSet(
    requiredTriggers = cms.untracked.vstring(""),
    d0Cut = cms.untracked.double(2.0),
    z0Cut = cms.untracked.double(25.0),
    recoCuts = cms.untracked.string("isGlobalMuon && abs(eta) < 2.4"),
    hltCuts  = cms.untracked.string("abs(eta) < 2.4"),
)

trackerMuons = cms.PSet(
    requiredTriggers = cms.untracked.vstring(""),
    d0Cut = cms.untracked.double(2.0),
    z0Cut = cms.untracked.double(25.0),
    recoCuts = cms.untracked.string("isTrackerMuon && abs(eta) < 2.4"),
    hltCuts  = cms.untracked.string("abs(eta) < 2.4"),
)

vbtfMuons = cms.PSet(
    requiredTriggers = cms.untracked.vstring(""),
    d0Cut = cms.untracked.double(0.2),
    z0Cut = cms.untracked.double(25.0),
    recoCuts = cms.untracked.string(' && '.join([
        "isGlobalMuon && isTrackerMuon",
        "abs(eta) < 2.4",
        "innerTrack.hitPattern.numberOfValidPixelHits > 0",
        "innerTrack.hitPattern.numberOfValidTrackerHits > 10",
        "globalTrack.hitPattern.numberOfValidMuonHits > 0",
        "globalTrack.normalizedChi2 < 10",
        "numberOfMatches > 1",
        ])),
    hltCuts  = cms.untracked.string("abs(eta) < 2.4"),
)

globalAnalyzer = hltMuonOfflineAnalyzer.clone()
globalAnalyzer.destination = "HLT/Muon/Distributions/globalMuons"
globalAnalyzer.targetParams = globalMuons
globalAnalyzer.probeParams = cms.PSet()

trackerAnalyzer = hltMuonOfflineAnalyzer.clone()
trackerAnalyzer.destination = "HLT/Muon/Distributions/trackerMuons"
trackerAnalyzer.targetParams = trackerMuons
trackerAnalyzer.probeParams = cms.PSet()

vbtfAnalyzer = hltMuonOfflineAnalyzer.clone()
vbtfAnalyzer.destination = "HLT/Muon/Distributions/vbtfMuons"
vbtfAnalyzer.targetParams = vbtfMuons
vbtfAnalyzer.probeParams = vbtfMuons

hltMuonOfflineAnalyzers = cms.Sequence(
    globalAnalyzer *
    trackerAnalyzer *
    vbtfAnalyzer
)
