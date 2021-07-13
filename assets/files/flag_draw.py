from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(39.409482,31.1404239, 7)

# line1
line1, line_1 = zip(*[
    (39.4546613,28.5954694),
    (39.4557216,28.4691266),
    (39.3803968,28.4677533),
    (39.3814583,28.5940961),
    (39.3028653,28.5940961),
    (39.3039279,28.4622602)
    ])
gmap.plot(line1, line_1, 'cornflowerblue', edge_width=2)


line2, line_2 = zip(*[
    (39.4557216,28.6243085),
    (39.4536009,28.7753705)
    ])
gmap.plot(line2, line_2, 'cornflowerblue', edge_width=2)


line3, line_3 = zip(*[
    (39.4546613,28.7039594),
    (39.3039279,28.7025861)
    ])
gmap.plot(line3, line_3, 'cornflowerblue', edge_width=2)


line4, line_4 = zip(*[
    (39.3060532,28.7973432),
    (39.4557216,28.7987165),
    (39.4016233,28.8742475),
    (39.4536009,28.9264325),
    (39.2975518,28.9250592) 
    ])
gmap.plot(line4, line_4, 'cornflowerblue', edge_width=2)


line5, line_5 = zip(*[
    (39.4578423,29.1132001),
    (39.4557216,28.9580182),
    (39.3028653,28.9566449),
    (39.3028653,29.1090802),  
    ])
gmap.plot(line5, line_5, 'cornflowerblue', edge_width=2)


line6, line_6 = zip(*[
    (39.4589026,29.1365461),
    (39.4589026,29.2917279)  
    ])
gmap.plot(line6, line_6, 'cornflowerblue', edge_width=2)

line65, line_65 = zip(*[
    (39.4589026,29.214137),
    (39.2999026,29.214137)  
    ])
gmap.plot(line65, line_65, 'cornflowerblue', edge_width=2)


line7, line_7 = zip(*[
    (39.4610231,29.4743757),
    (39.4578423,29.3178205),
    (39.3049906,29.3191938) 
    ])
gmap.plot(line7, line_7, 'cornflowerblue', edge_width=2)


line8, line_8 = zip(*[
    (39.4610231,29.4743757),
    (39.4578423,29.3178205),
    (39.3049906,29.3191938)  
    ])
gmap.plot(line8, line_8, 'cornflowerblue', edge_width=2)


line9, line_9 = zip(*[
    (39.3825197,29.3178205),
    (39.3835812,29.4743757)  
    ])
gmap.plot(line9, line_9, 'cornflowerblue', edge_width=2)


line10, line_10 = zip(*[
    (39.4690394,29.6624871),
    (39.4679793,29.6061822),
    (39.4075243,29.5842096),
    (39.3831153,29.5320245),
    (39.3640067,29.5828363),
    (39.3130248,29.6116754),
    (39.3140873,29.666607) 
    ])
gmap.plot(line10, line_10, 'cornflowerblue', edge_width=2)

line11, line_11 = zip(*[
    (39.4711597,29.689953 ),
    (39.3119623,29.6913262)
    ])
gmap.plot(line11, line_11, 'cornflowerblue', edge_width=2)

line12, line_12 = zip(*[
    (39.4711597,29.817669 ),
    (39.3841768,29.6913262),
    (39.3140873,29.8286554) 
    ])
gmap.plot(line12, line_12, 'cornflowerblue', edge_width=2)

line13, line_13 = zip(*[
    (39.4753999,30.0099298),
    (39.4743399,29.8520013),
    (39.3108998,29.8547479),
    (39.3119623,30.0181695)
    ])
gmap.plot(line13, line_13, 'cornflowerblue', edge_width=2)

line14, line_14 = zip(*[
    (39.3969128,29.8520013),
    (39.4000964,30.0058099)
    ])
gmap.plot(line14, line_14, 'cornflowerblue', edge_width=2)

line15, line_15 = zip(*[
    (39.4796437,30.1931682),
    (39.4796437,30.0393597),
    (39.3140911,30.0421062),
    (39.316216 ,30.1986614) 
    ])
gmap.plot(line15, line_15, 'cornflowerblue', edge_width=2)

line16, line_16 = zip(*[
    (39.4011613,30.0407329),
    (39.4022225,30.1890484)  
    ])
gmap.plot(line16, line_16, 'cornflowerblue', edge_width=2)

line17, line_17 = zip(*[
    (39.3194033,30.2247539),
    (39.4817636,30.2220074),
    (39.4838835,30.362083 ),
    (39.4054058,30.362083 ),
    (39.4054058,30.2316204) 
    ])
gmap.plot(line17, line_17, 'cornflowerblue', edge_width=2)

line18, line_18 = zip(*[
    (39.4896654,30.5388784),
    (39.4875457,30.3919362),
    (39.3220119,30.3905629),
    (39.3241366,30.5375051)
    ])
gmap.plot(line18, line_18, 'cornflowerblue', edge_width=2)

line19, line_19 = zip(*[          
    (39.3251989,30.5649709),
    (39.4939046,30.6405019),
    (39.3273235,30.7256459)
    ])
gmap.plot(line19, line_19, 'cornflowerblue', edge_width=2)

line20, line_20 = zip(*[          
    (39.4005833,30.5965566),
    (39.4005833,30.6885671)
    ])
gmap.plot(line20, line_20, 'cornflowerblue', edge_width=2)

line21, line_21 = zip(*[          
    (39.4981435,30.7590567),
    (39.3283858,30.7549368),
    (39.3283858,30.8936392)  
    ])
gmap.plot(line21, line_21, 'cornflowerblue', edge_width=2)

line22, line_22 = zip(*[          
    (39.3294481,30.9224783),
    (39.5076801,30.9224783),
    (39.4536221,31.0089956),
    (39.5097991,31.08178),
    (39.3262612,31.0831533)
    ])
gmap.plot(line22, line_22, 'cornflowerblue', edge_width=2)

line23, line_23 = zip(*[          
    (39.328796 ,31.1060917),
    (39.5155056,31.1912357),
    (39.3319828,31.2832462)
    ])
gmap.plot(line23, line_23, 'cornflowerblue', edge_width=2)

line24, line_24 = zip(*[          
    (39.409482,31.1404239),
    (39.410543,31.2420475)  
    ])
gmap.plot(line24, line_24, 'cornflowerblue', edge_width=2)

line25, line_25 = zip(*[          
    (39.3372937,31.3052189),
    (39.5250398,31.3024723),
    (39.3372937,31.4452946),
    (39.5335136,31.4411747)
    ])
gmap.plot(line25, line_25, 'cornflowerblue', edge_width=2)

line26, line_26 = zip(*[          
    (39.3405817,31.4639944),
    (39.5357332,31.4626212),
    (39.5018331,31.5642447),
    (39.4265581,31.5766043),
    (39.3448299,31.5628714),
    (39.3405817,31.4818472)
    ])
gmap.plot(line26, line_26, 'cornflowerblue', edge_width=2)

line27, line_27 = zip(*[          
    (39.5357332,31.7441458),
    (39.5336149,31.598577),
    (39.4456496,31.5999503),
    (39.448831 ,31.7455191),
    (39.3575731,31.7482657),
    (39.3543875,31.5958304) 
    ])
gmap.plot(line27, line_27, 'cornflowerblue', edge_width=2)

line28, line_28 = zip(*[          
    (39.362882 ,31.9130606),
    (39.3607585,31.7812247),
    (39.5378514,31.7757315),
    (39.5378514,31.910314) 
    ])
gmap.plot(line28, line_28, 'cornflowerblue', edge_width=2)

line29, line_29 = zip(*[          
    (39.454133 ,31.7771048),
    (39.4551934,31.9075674)
    ])
gmap.plot(line29, line_29, 'cornflowerblue', edge_width=2)

line30, line_30 = zip(*[          
    (39.3650055,31.9350333),
    (39.5442056,31.9364066),
    (39.3639438,32.0586295),
    (39.5463236,32.0586295)
    ])
gmap.plot(line30, line_30, 'cornflowerblue', edge_width=2)

line31, line_31 = zip(*[          
    (39.5463236,32.0860953),
    (39.3650055,32.0833487),
    (39.381991 ,32.1629996),
    (39.4626154,32.1959586),
    (39.5325558,32.1588797),
    (39.5484415,32.0984549)
    ])
gmap.plot(line31, line_31, 'cornflowerblue', edge_width=2)

line32, line_32 = zip(*[          
    (39.3727298,32.2153733),
    (39.5540278,32.214),
    (39.4989462,32.289531),
    (39.5550866,32.3554489),
    (39.3716682,32.3581955)
    ])
gmap.plot(line32, line_32, 'cornflowerblue', edge_width=2)

line33, line_33 = zip(*[          
    (39.5550866,32.5037644),
    (39.5529689,32.3787949),
    (39.3716682,32.3801682),
    (39.3727298,32.5037644)
    ])
gmap.plot(line33, line_33, 'cornflowerblue', edge_width=2)

line34, line_34 = zip(*[          
    (39.4682086,32.3801682),
    (39.4682086,32.5051377)
    ])
gmap.plot(line34, line_34, 'cornflowerblue', edge_width=2)

line35, line_35 = zip(*[          
    (39.5561454,32.5271103),
    (39.5561454,32.6850388)
    ])
gmap.plot(line35, line_35, 'cornflowerblue', edge_width=2)

line36, line_36 = zip(*[          
    (39.5572309,32.6081345),
    (39.3738181,32.6081345)
    ])
gmap.plot(line36, line_36, 'cornflowerblue', edge_width=2)

line37, line_37 = zip(*[          
    (39.5561744,32.7085394),
    (39.3759436,32.7112859)
    ])
gmap.plot(line37, line_37, 'cornflowerblue', edge_width=2)

line38, line_38 = zip(*[          
    (39.4820182,32.7112859),
    (39.4820182,32.8197759)
    ])
gmap.plot(line38, line_38, 'cornflowerblue', edge_width=2)

line39, line_39 = zip(*[          
    (39.3716972,32.8156561),
    (39.5551156,32.8142828)
    ])
gmap.plot(line39, line_39, 'cornflowerblue', edge_width=2)

line40, line_40 = zip(*[          
    (39.3741626,32.967138 ),
    (39.3720394,32.8449151),
    (39.5607508,32.8435418),
    (39.5607508,32.9657647)
    ])
gmap.plot(line40, line_40, 'cornflowerblue', edge_width=2)

line41, line_41 = zip(*[          
    (39.4812999,32.8449151),
    (39.48024  ,32.9602716)
    ])
gmap.plot(line41, line_41, 'cornflowerblue', edge_width=2)

line42, line_42 = zip(*[          
    (39.5652946,33.1309605),
    (39.5631772,32.996378 ),
    (39.3755341,32.9950047)
    ])
gmap.plot(line42, line_42, 'cornflowerblue', edge_width=2)

line43, line_43 = zip(*[          
    (39.4763094,32.996378 ),
    (39.4763094,33.1268406)
    ])
gmap.plot(line43, line_43, 'cornflowerblue', edge_width=2)

line44, line_44 = zip(*[          
    (39.5664711,33.1529345),
    (39.3767138,33.1529345),
    (39.3767138,33.2792773)
    ])
gmap.plot(line44, line_44, 'cornflowerblue', edge_width=2)

line45, line_45 = zip(*[          
    (39.3767138,33.2998766),
    (39.5685884,33.3603014),
    (39.3788368,33.4509386)
    ])
gmap.plot(line45, line_45, 'cornflowerblue', edge_width=2)

line46, line_46 = zip(*[          
    (39.4584047,33.3245959),
    (39.459465 ,33.4097399)
    ])
gmap.plot(line46, line_46, 'cornflowerblue', edge_width=2)

line47, line_47 = zip(*[          
    (39.5770568,33.6280932),
    (39.5749398,33.4660448),
    (39.3809598,33.4729113),
    (39.3820213,33.6226),
    (39.4902064,33.6239733),
    (39.4849071,33.471538)
    ])
gmap.plot(line47, line_47, 'cornflowerblue', edge_width=2)

line48, line_48 = zip(*[          
    (39.5795526,33.6540717),
    (39.5795526,33.740589),
    (39.4958845,33.7721747),
    (39.4905857,33.825733),
    (39.4715065,33.773548),
    (39.389831 ,33.740589),
    (39.3887696,33.6499518)
    ])
gmap.plot(line48, line_48, 'cornflowerblue', edge_width=2)


# Draw
gmap.draw("my_map.html")
