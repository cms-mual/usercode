### ./findQualityFiles.py --startRun 190456 --endRun 193621 --alcaDataset /SingleMu/Run2012A-MuAlCalIsolatedMu-13Jul2012-v1/ALCARECO --json Cert_190456-206539_8TeV_PromptReco_Collisions12_JSON_MuonPhys.txt --outputFile Cert_190456-206539__SingleMu__Run2012A-MuAlCalIsolatedMu-13Jul2012-v1.py
### list of runs with good B field and quality in the dataset: ###
### [190645, 190646, 190659, 190679, 190688, 190702, 190703, 190704, 190705, 190706, 190707, 190708, 190710, 190733, 190736, 190738, 191043, 191046, 191056, 191057, 191062, 191090, 191201, 191202, 191226, 191247, 191248, 191264, 191271, 191276, 191277, 191367, 191411, 191691, 191695, 191718, 191720, 191721, 191726, 191800, 191810, 191811, 191830, 191833, 191834, 191837, 191839, 191842, 191845, 191849, 191856, 191857, 191858, 191859, 193093, 193112, 193123, 193124, 193192, 193193, 193207, 193334, 193336, 193541, 193556, 193557, 193575, 193621]
### total number of events in those 68 runs = 8237573
fileNames = [
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/44C067ED-F8D3-E111-B2A7-00266CFFCB80.root', # 48954
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/666E2011-4AD1-E111-9C50-1CC1DE1CED1C.root', # 49819
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/DA1F0127-22D3-E111-BA2A-00266CFFC4C4.root', # 49551
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/84B6E968-11D3-E111-A6C5-00266CFBCC6C.root', # 48865
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/2EF569D9-1ED3-E111-A85E-D8D385FF0B6A.root', # 49810
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/4AA06401-12D3-E111-BF29-00266CFBCC6C.root', # 49943
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/34FE9DFC-F8D3-E111-BD1E-00266CFFC4C4.root', # 49353
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/AA4AE952-1DD3-E111-9852-0017A477040C.root', # 49397
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/F848800F-16D1-E111-9E22-1CC1DE1D1FE6.root', # 49373
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/F63B6219-20D1-E111-9AF9-1CC1DE051028.root', # 18380
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/BE9742FA-E8D2-E111-B667-1CC1DE1CE128.root', # 49969
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/8E36224E-34D1-E111-A15A-0017A4770C34.root', # 49786
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/241BEAF6-00D3-E111-ACFC-1CC1DE041F38.root', # 49981
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/A4ABB204-1CD1-E111-A574-1CC1DE1CDF2A.root', # 49997
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/D0D70D5E-E0D2-E111-99CF-0025B3E0216C.root', # 49994
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/225A2B90-13D1-E111-A8A2-0017A4770420.root', # 49851
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/E85B7FDC-F8D3-E111-9FDB-00266CFEFDEC.root', # 49105
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/98F68AFE-F8D3-E111-8199-0017A477041C.root', # 49867
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/D6615D29-12D3-E111-A120-1CC1DE1CDCAE.root', # 49995
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/3ABD61A7-1DD1-E111-B545-00266CFFBED8.root', # 49994
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/3221E465-15D3-E111-9F44-001E0B5FE542.root', # 49994
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/82749CFD-14D1-E111-AA46-1CC1DE1CE56C.root', # 49985
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/B835FD9C-20D3-E111-873A-00266CFFCCBC.root', # 49899
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/C21CC12F-12D1-E111-B60E-1CC1DE1D1FE6.root', # 41705
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/922D6A1F-D5D0-E111-8A90-0017A4770038.root', # 49999
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/74FD590D-18D1-E111-B40F-0017A4771018.root', # 49995
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/20D9F1DC-F8D3-E111-B0EB-00266CFF0840.root', # 49288
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/4C18FBEF-F8D3-E111-B423-1CC1DE1CE170.root', # 49543
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/B01DF7E9-F8D3-E111-BE2B-00237DA12CEC.root', # 49889
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/76E20452-E0D2-E111-8FCB-1CC1DE056080.root', # 49939
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/243C3EB6-00D1-E111-95FA-1CC1DE046F18.root', # 49866
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/1088112C-14D3-E111-8900-1CC1DE04DF20.root', # 49834
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/F67FCDEC-59D3-E111-BAD8-00266CFFC89C.root', # 49966
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/9AE70CFD-F8D3-E111-839B-00266CFFC80C.root', # 48488
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/DE927907-18D1-E111-A87B-00266CFFBCDC.root', # 49927
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/1645F00D-EBD2-E111-8D8E-1CC1DE1D014A.root', # 49985
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/AC216506-1CD1-E111-80A8-0017A4771028.root', # 49990
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/EE0643F9-05D1-E111-BBAB-00266CFF0234.root', # 49925
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/1AD6DD91-FDD2-E111-956C-0017A4771018.root', # 49995
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/3285E03D-F3D0-E111-A189-0017A4770018.root', # 49935
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/CAC66FF7-00D3-E111-B526-1CC1DE056008.root', # 49999
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/30A12C6B-E7D0-E111-AEF5-0017A4770C10.root', # 49992
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/F0E67293-13D1-E111-AA93-1CC1DE05D2F8.root', # 49926
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/6E0100C2-64D1-E111-BC3F-0017A477040C.root', # 25883
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/982A3106-F9D3-E111-90FE-0017A4770018.root', # 49362
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/F6B4B681-15D3-E111-85F7-0017A4770014.root', # 49577
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/64505743-F9D3-E111-81F7-00266CFF0840.root', # 28367
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/587692DA-F8D3-E111-BE48-00266CFFBCE0.root', # 49663
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/544C5050-0FD1-E111-BAED-0017A477003C.root', # 49932
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/EA7B9FF4-F8D3-E111-8B19-00266CFFBF38.root', # 49420
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/0A0A6DA5-1AD1-E111-8E43-00266CFFC43C.root', # 49999
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/8EE872BD-D6D0-E111-BA1B-00266CFEFDE0.root', # 49999
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/8CF23484-FDD2-E111-9616-0017A4770008.root', # 49640
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/EE8052E8-F8D3-E111-8306-00266CFF0840.root', # 49169
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/206D7761-CCD0-E111-8A9E-00237DA1AC2A.root', # 50000
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/4AD252BC-3DD1-E111-99D7-00266CFFCC54.root', # 49671
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/10EBBBB6-14D1-E111-A8F5-0017A4771020.root', # 49928
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/A6715C3F-F9D3-E111-B4AE-002481A7329C.root', # 49916
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/FC033B14-EBD2-E111-900D-00266CFFC4E0.root', # 49667
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/A8476290-B9D0-E111-8193-00266CFFBF64.root', # 49997
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/A4CF51FD-F8D3-E111-BF7A-00266CFFCC7C.root', # 49960
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/1E8B7D41-F9D3-E111-9C4F-00266CFEFCE8.root', # 49415
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/FA8DEEAC-1DD1-E111-AC6F-1CC1DE1CDCAE.root', # 49826
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/66AF5101-F9D3-E111-8A67-00266CFFC4C4.root', # 48591
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/2856446C-15D3-E111-B8B9-1CC1DE1CE128.root', # 49993
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/046D9900-18D1-E111-8492-00266CFFBF4C.root', # 49988
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/8448B184-39D1-E111-82C3-0017A4770C08.root', # 49874
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/4456C992-D7D0-E111-A6D7-00266CFFBF4C.root', # 49984
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/141C6B3B-F9D3-E111-A935-00266CFFCA1C.root', # 49671
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/F4EB1ADC-F8D3-E111-92EC-D8D3855BBDC4.root', # 49644
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/7A136A24-20D1-E111-BCAE-1CC1DE051060.root', # 49885
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/A6059D82-14D3-E111-B54B-1CC1DE04DF20.root', # 20822
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/C80FEBBC-FBD2-E111-AC95-0017A477082C.root', # 49990
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/78957DF1-F8D3-E111-A643-0017A4770C20.root', # 49917
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/1EE05C61-E7D2-E111-9894-1CC1DE1CF1F6.root', # 49969
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/BA0661AE-FBD2-E111-9615-0017A4770410.root', # 49890
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/669232ED-F8D3-E111-87E3-00266CFFC80C.root', # 49472
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/9E1634E5-0CD3-E111-A225-00266CFFC7E4.root', # 49997
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/646B7E87-52D1-E111-8DB0-00266CFFC4D4.root', # 49848
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/5C79C77E-39D1-E111-81A8-00266CFFCD60.root', # 49856
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/7078C9BD-D6D0-E111-8368-0017A4770C0C.root', # 49690
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/2285F569-F4D0-E111-9BB8-0017A4770C28.root', # 49972
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/5CC239C2-21D1-E111-A149-1CC1DE046F18.root', # 49956
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/BE71D500-3BD1-E111-9E38-1CC1DE1CED1C.root', # 49955
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/BC530418-F9D3-E111-84D2-0017A477100C.root', # 49562
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/78F91E3C-F9D3-E111-9663-1CC1DE04DF20.root', # 49988
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/A8A8A6DA-F8D3-E111-B375-1CC1DE1CDCAE.root', # 49511
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/6AF2968F-13D1-E111-AA39-0017A4770404.root', # 49934
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/82C5AD7E-2CD1-E111-9788-0017A4770C14.root', # 49852
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/7E99D840-F9D3-E111-A0E3-00266CFFCD6C.root', # 49672
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/4CD48709-1CD1-E111-B2C2-0017A4770C38.root', # 49745
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/9AFD1935-FFD6-E111-AE0E-0017A4770408.root', # 669
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/8A43CA61-FFD2-E111-8EAB-1CC1DE1CED22.root', # 49998
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/020AF48B-46D1-E111-8C63-0017A477040C.root', # 49876
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/966761FA-F8D3-E111-843D-00266CFEFDEC.root', # 49717
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/C6AEA2C8-29D1-E111-9FBF-0017A4770024.root', # 49867
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/C26887E3-F8D3-E111-A74C-1CC1DE04DF20.root', # 48614
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/3C0BE906-44D3-E111-A9DA-1CC1DE1D0600.root', # 49777
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/C852A778-18D3-E111-A84E-1CC1DE1D03DE.root', # 49980
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/AE61973D-F3D0-E111-8112-0017A4770434.root', # 50000
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/988511FA-E8D2-E111-987E-1CC1DE052068.root', # 49857
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/D8E81990-0BD3-E111-BF36-1CC1DE1D03DE.root', # 49982
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/8051F057-36D1-E111-905E-0017A4770C20.root', # 49776
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/009487C0-64D1-E111-BABB-0025B3E01806.root', # 49764
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/908741E7-F8D3-E111-87E4-00266CFEFE08.root', # 49052
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/48B5E9F9-F8D3-E111-A9B4-00266CFFBF64.root', # 49607
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/D2310420-EFD2-E111-B226-1CC1DE047FA0.root', # 49989
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/92D38047-16D3-E111-A50F-0017A4770808.root', # 49818
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/621DEB50-DED2-E111-BADB-0017A4771004.root', # 50000
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/447D555A-34D1-E111-A6E8-00266CFFBF84.root', # 49769
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/24D78C61-34D1-E111-A60E-0017A4770810.root', # 49695
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/FA5110D4-29D1-E111-AF92-1CC1DE1CDDBC.root', # 49703
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/982B7922-EFD2-E111-8E4B-00266CFEFC38.root', # 50000
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/6EAD990C-16D1-E111-9C79-0017A4770C3C.root', # 49976
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/B2EEE70C-EBD2-E111-B916-1CC1DE046F18.root', # 49997
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/BEA5297B-18D3-E111-8E29-1CC1DE051080.root', # 49987
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/A8F8D846-DED2-E111-AFB4-00266CFFCAF0.root', # 49996
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/1869D33B-F9D3-E111-B353-00266CFFCC18.root', # 49324
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/04F3FB44-31D1-E111-AA74-1CC1DE055158.root', # 49910
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/68F18704-15D1-E111-A7DB-1CC1DE051028.root', # 49979
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/D6F64808-44D3-E111-8DC5-1CC1DE1D1FE6.root', # 28446
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/4CEA8663-ECD2-E111-B634-0017A4770414.root', # 8479
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/D49E5158-FFD2-E111-955F-1CC1DE1D2004.root', # 49983
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/3A62F795-26D1-E111-87D9-00266CFFBEB4.root', # 8487
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/7EC68EEF-F8D3-E111-895A-0017A4770800.root', # 48720
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/3616D1E7-0CD3-E111-A7E8-002481FFD0CC.root', # 49996
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/865053BB-3DD1-E111-A02A-1CC1DE1D14A0.root', # 49792
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/7E9C772E-12D1-E111-B69A-0017A4770004.root', # 49975
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/24354039-19D1-E111-8442-00237DA1A8CE.root', # 49977
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/3E2C5BD0-D3D0-E111-AD6F-0017A4771008.root', # 49537
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/AC1F2E4D-11D3-E111-B0EA-0026557DB808.root', # 49957
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/4AA0DE4A-0FD1-E111-8A0B-00237DA15C7C.root', # 49963
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/CADA638F-0BD3-E111-9519-1CC1DE1D2004.root', # 49994
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/D86C6A93-26D1-E111-B63F-00266CFFC51C.root', # 49861
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/FC0BF60F-F9D3-E111-B318-00266CFEFC38.root', # 49830
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/022B8064-ECD2-E111-8A47-0017A4771010.root', # 49994
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/E2BE2A53-F8D2-E111-AF0E-00266CFFBC74.root', # 49979
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/50CCCA50-31D1-E111-AE94-1CC1DE1CDDBC.root', # 49989
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/3017BB0F-16D1-E111-BD1B-1CC1DE1D023A.root', # 49942
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/34F73F09-57D3-E111-8B3F-00266CFFBF50.root', # 49979
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/FCAAC4F9-E8D2-E111-BD12-1CC1DE0590E8.root', # 49998
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/9257A75C-F4D0-E111-B9A1-0017A4770824.root', # 49953
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/9454AAD5-D3D0-E111-A9C6-00266CFEFDEC.root', # 50000
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/98BCE6F0-F8D3-E111-9BC7-00266CFFBCFC.root', # 49471
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/5C1498CB-21D1-E111-A3A6-0017A4770018.root', # 40181
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/666F0DEF-F8D3-E111-B5E5-00237DA16692.root', # 49283
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/E401548F-FDD2-E111-AC38-00266CFFBF88.root', # 49747
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/78AED108-3BD1-E111-B8FA-1CC1DE1CDD20.root', # 49754
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/70464D8E-13D1-E111-B018-0017A477080C.root', # 49925
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/DCFCB764-E0D2-E111-8E54-0017A4770434.root', # 49971
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/CEEBEC5C-FFD2-E111-BC90-1CC1DE1D16D4.root', # 49832
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/0E99576F-E7D0-E111-9890-00266CFFC9C4.root', # 49999
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/80D7A8A3-1AD1-E111-9562-00266CFFBE88.root', # 49935
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/8A2BFA36-19D1-E111-A487-1CC1DE050110.root', # 49929
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/8A6B2455-36D1-E111-A3AF-0017A4770404.root', # 49998
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/0EE27952-34D1-E111-BD38-00266CFFC13C.root', # 49902
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/CEC5605C-16D3-E111-AE88-00266CFBCC6C.root', # 49960
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/96E85B23-D5D0-E111-A663-0017A477082C.root', # 49807
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/02723E7B-2CD1-E111-B582-00266CFEFDE0.root', # 49977
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/E0C3F23A-F9D3-E111-BD6F-00266CFFBC64.root', # 49465
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/16845942-F9D3-E111-91A1-0025B3E020D0.root', # 49056
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/C4736C03-F2D2-E111-8F81-00237DA1DDE4.root', # 49971
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/804638FE-00D3-E111-BEF2-0017A4770C1C.root', # 49875
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/A40F4064-E7D2-E111-A318-0017A4770414.root', # 49958
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/D2956C60-14D3-E111-9984-001E0B5FE542.root', # 49941
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/5C4469F5-05D1-E111-9DAD-0017A4771008.root', # 49959
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/02DB77B9-00D1-E111-9BF2-1CC1DE1CED22.root', # 49922
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/5CE2C414-04D3-E111-90B2-0017A4770018.root', # 49966
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/0A7346FA-F9D2-E111-BCAF-1CC1DE0500F0.root', # 49992
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/C21444EE-F8D3-E111-A158-1CC1DE0570A0.root', # 49815
    '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/C03E4F53-F8D2-E111-ADB0-00266CFFCB14.root' # 49805
]
