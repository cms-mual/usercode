### ../findQualityFiles.py --startRun 190456 --endRun 208686 --alcaDataset /SingleMu/Run2012C-MuAlCalIsolatedMu-v1/ALCARECO --json Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON_MuonPhys.txt --outputFile Cert_190456-208686__SingleMu__Run2012C-MuAlCalIsolatedMu-v1.py
### list of runs with good B field and quality in the dataset: ###
### [198049, 198050, 198063, 198116, 198207, 198208, 198210, 198212, 198213, 198215, 198230, 198249, 198269, 198271, 198272, 198346, 198372, 198485, 198487, 198522]
### total number of events in those 20 runs = 5671786
fileNames = [
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/487/1621EA45-8BCA-E111-8BAC-5404A640A642.root', # 188634
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/487/FEFD486D-7CCA-E111-9D50-5404A638869B.root', # 186258
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/272/D6EB6C9B-5CC8-E111-84D8-5404A63886CE.root', # 203200
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/372/66B0E829-07C9-E111-AFA7-001D09F29169.root', # 75496
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/249/06DCC37F-D4C7-E111-AACC-0019B9F72CE5.root', # 4640
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/212/0E05C43F-48C7-E111-9C35-001D09F2447F.root', # 203110
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/230/BEE669F3-BBC7-E111-A014-00215AEDFD74.root', # 192371
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/269/FA4D5996-30C8-E111-8E85-0025901D5D9A.root', # 160056
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/522/54D04DC5-1ECB-E111-BF00-BCAEC5329717.root', # 161806
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/230/B8A04F66-36C8-E111-B2A6-003048D373AE.root', # 182705
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/049/94F457A9-F8C6-E111-8465-001D09F2447F.root', # 21406
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/485/72D3F83B-BECA-E111-BCD0-002481E0D83E.root', # 80788
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/116/FEB532DA-94C6-E111-9F75-001D09F2960F.root', # 72264
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/487/C81E6F75-72CA-E111-8BB0-002481E0D83E.root', # 185539
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/269/7481572C-4EC8-E111-ADB6-0025901D625A.root', # 130600
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/230/F6784903-D0C7-E111-B3A8-003048D2BED6.root', # 190053
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/487/DACF42BF-96CA-E111-9A5C-BCAEC518FF40.root', # 186077
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/230/EA125B5F-C5C7-E111-9A8A-001D09F24303.root', # 191643
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/487/4EC71D06-A5CA-E111-86D7-003048D2BD66.root', # 183333
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/522/2CAE3383-8DCB-E111-927A-001D09F2AD84.root', # 26597
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/487/CA98B732-BECA-E111-B8D7-001D09F24DA8.root', # 190318
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/230/9C5BF39A-D3C7-E111-A54D-0030486780EC.root', # 189457
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/050/A0B133FB-25C6-E111-B371-003048D37694.root', # 55393
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/485/66327878-28CA-E111-B006-001D09F28EA3.root', # 163942
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/208/A0CA4DDA-53C7-E111-9C4C-001D09F276CF.root', # 151838
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/063/28285A29-23C6-E111-A007-0025901D627C.root', # 95670
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/215/660C5A20-4AC7-E111-AD1B-001D09F25109.root', # 5195
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/212/DAC42830-7BC7-E111-A8C5-001D09F24682.root', # 92075
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/210/888412F1-4EC7-E111-A05A-003048D2BCA2.root', # 140285
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/271/14B92758-48C8-E111-90F9-0025901D6272.root', # 177153
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/207/D08C02D3-4AC7-E111-823C-001D09F25109.root', # 10045
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/271/5012C2CD-52C8-E111-8F0D-003048F1C58C.root', # 172266
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/213/18EC04AF-56C7-E111-9FD6-5404A63886B4.root', # 46172
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/271/9C3617FA-88C8-E111-A55C-001D09F251FE.root', # 153444
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/487/FA4D114E-B4CA-E111-873C-002481E94050.root', # 180051
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/271/C8E52452-4DC8-E111-9A76-0025901D6272.root', # 182324
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/230/044BE714-AFC7-E111-B9DB-5404A63886B2.root', # 195378
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/207/F60EE22B-47C7-E111-97CB-001D09F25041.root', # 69621
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/272/DE4CB17B-6FC8-E111-9E53-5404A638869C.root', # 202932
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/272/FA13E46E-9DC8-E111-9BF6-0019B9F72CE5.root', # 55618
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/487/2010D511-12CB-E111-9D1A-BCAEC5329727.root', # 131534
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/271/4C094DA1-42C8-E111-AB23-003048F024FA.root', # 179950
    '/store/data/Run2012C/SingleMu/ALCARECO/MuAlCalIsolatedMu-v1/000/198/346/72606D6F-A9C8-E111-B6B3-0025901D629C.root' # 4549
]
