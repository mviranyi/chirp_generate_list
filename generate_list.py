# to be set by user

frequ = 433075000 # Hz
frequ_step = 25000 # Hz
label = "LPD " # hint: max length is 6
channel = 1 # int
channel_last = 69 # int
filename_output = "output_lpd1_69.txt"

sbatp = 153
sbatp_step = 7

line_number_I = 31 # += 1

# 

prefix = """((ichirp.chirp_common
RadioFeatures
p0
(dp1
S'has_bank_names'
p2
I00
sS'has_implicit_calls'
p3
I00
sS'has_dtcs_polarity'
p4
I01
sS'has_infinite_number'
p5
I00
sS'has_settings'
p6
I01
sS'valid_dtcs_codes'
p7
(lp8
I23
aI25
aI26
aI31
aI32
aI36
aI43
aI47
aI51
aI53
aI54
aI65
aI71
aI72
aI73
aI74
aI114
aI115
aI116
aI122
aI125
aI131
aI132
aI134
aI143
aI145
aI152
aI155
aI156
aI162
aI165
aI172
aI174
aI205
aI212
aI223
aI225
aI226
aI243
aI244
aI245
aI246
aI251
aI252
aI255
aI261
aI263
aI265
aI266
aI271
aI274
aI306
aI311
aI315
aI325
aI331
aI332
aI343
aI346
aI351
aI356
aI364
aI365
aI371
aI411
aI412
aI413
aI423
aI431
aI432
aI445
aI446
aI452
aI454
aI455
aI462
aI464
aI465
aI466
aI503
aI506
aI516
aI523
aI526
aI532
aI546
aI565
aI606
aI612
aI624
aI627
aI631
aI632
aI645
aI654
aI662
aI664
aI703
aI712
aI723
aI731
aI732
aI734
aI743
aI754
asS'requires_call_lists'
p9
I01
sS'has_cross'
p10
I01
sS'valid_tuning_steps'
p11
(lp12
F2.5
aF5.0
aF6.25
aF10.0
aF12.5
aF20.0
aF25.0
aF50.0
asS'_RadioFeatures__docs'
p13
(dp14
g2
S'Indicates that banks may be named'
p15
sg3
S'[D-STAR] Indicates that the radio has an implied callsign at the beginning of the master URCALL list'
p16
sg4
S'Indicates that the DTCS polarity can be changed'
p17
sg5
S'Indicates that the radio is not constrained in the number of memories that it can store'
p18
sg6
S'Indicates that the radio supports general settings'
p19
sg7
S'Supported DTCS codes'
p20
sg9
S'[D-STAR] Indicates that the radio requires all callsigns to be in the master list and cannot be stored arbitrarily in each memory channel'
p21
sg10
S'Indicates that the radios supports different tone modes on transmit and receive'
p22
sg11
S'Supported tuning steps'
p23
sS'has_dtcs'
p24
S'Indicates that DTCS tone mode is available'
p25
sS'has_name'
p26
S'Indicates that an alphanumeric memory name is supported'
p27
sS'valid_cross_modes'
p28
S'Supported tone cross modes'
p29
sS'has_mode'
p30
S'Indicates that multiple emission modes are supported'
p31
sS'has_rx_dtcs'
p32
S'Indicates that radio can use two different DTCS codes for rx and tx'
p33
sS'has_offset'
p34
S'Indicates that the TX offset memory property is supported'
p35
sS'valid_dtcs_pols'
p36
S'Supported DTCS polarities'
p37
sS'has_bank_index'
p38
S'Indicates that memories in a bank can be stored in an order other than in main memory'
p39
sS'has_ctone'
p40
S'Indicates that the radio keeps separate tone frequencies for repeater and CTCSS operation'
p41
sS'has_sub_devices'
p42
S'Indicates that the radio behaves as two semi-independent devices'
p43
sS'valid_bands'
p44
S'Supported frequency ranges'
p45
sS'valid_skips'
p46
S'Supported memory scan skip settings'
p47
sS'can_delete'
p48
S'Indicates that the radio can delete memories'
p49
sS'valid_tmodes'
p50
S'Supported tone squelch modes'
p51
sS'valid_name_length'
p52
S"The maximum number of characters in a memory's alphanumeric tag"
p53
sS'has_nostep_tuning'
p54
S'Indicates that the radio does not require a valid tuning step to store a frequency'
p55
sS'has_comment'
p56
S'Indicates that the radio supports storing a comment with each memory'
p57
sS'has_tuning_step'
p58
S'Indicates that memories store their tuning step'
p59
sS'valid_special_chans'
p60
S'Supported special channel names'
p61
sS'valid_modes'
p62
S'Supported emission (or receive) modes'
p63
sS'memory_bounds'
p64
S'The minimum and maximum channel numbers'
p65
sS'valid_power_levels'
p66
S'Supported power levels'
p67
sS'valid_duplexes'
p68
S'Supported duplex modes'
p69
sS'has_bank'
p70
S'Indicates that memories may be placed into banks'
p71
sS'can_odd_split'
p72
S'Indicates that the radio can store an independent transmit frequency'
p73
sS'valid_characters'
p74
S"Supported characters for a memory's alphanumeric tag"
p75
ssg24
I01
sg26
I01
sg28
(lp76
S'Tone->Tone'
p77
aS'DTCS->'
p78
aS'->DTCS'
p79
aS'Tone->DTCS'
p80
aS'DTCS->Tone'
p81
aS'->Tone'
p82
aS'DTCS->DTCS'
p83
asg30
I01
sg32
I01
sg34
I01
sg36
(lp84
S'NN'
p85
aS'RN'
p86
aS'NR'
p87
aS'RR'
p88
asg38
I00
sg40
I01
sg42
I00
sg44
(lp89
(I130000000
I180000000
tp90
a(I200000000
I260000000
tp91
a(I400000000
I521000000
tp92
asg46
(lp93
S''
p94
aS'S'
p95
asg48
I01
sg50
(lp96
g94
aS'Tone'
p97
aS'TSQL'
p98
aS'DTCS'
p99
aS'Cross'
p100
asg52
I7
sg54
I00
sg56
I00
sg58
I00
sg60
(lp101
sg62
(lp102
S'NFM'
p103
aS'FM'
p104
asg64
(I0
I127
tp105
sg66
(lp106
(ichirp.chirp_common
PowerLevel
p107
(dp108
S'_label'
p109
S'High'
p110
sS'_power'
p111
I36
sba(ichirp.chirp_common
PowerLevel
p112
(dp113
g109
S'Med'
p114
sg111
I34
sba(ichirp.chirp_common
PowerLevel
p115
(dp116
g109
S'Low'
p117
sg111
I30
sbasg68
(lp118
g94
aS'-'
p119
aS'+'
p120
aS'split'
p121
aS'off'
p122
asg70
I00
sg72
I01
sg74
S'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()+-=[]:";\\'<>?,./'
p123
sb(lp124
(ichirp.chirp_common
Memory
p125
(dp126
S'vfo'
p127
I0
sS'tmode'
p128
g94
sS'name'
p129
S'{}'
p130
sS'power'
p131
g115
sS'duplex'
p132
g94
sS'skip'
p133
g94
sS'tuning_step'
p134
F5.0
sS'number'
p135
I30
sS'comment'
p136
g94
sS'immutable'
p137
(lp138
sS'rx_dtcs'
p139
I23
sS'dtcs_polarity'
p140
S'NN'
p141
sS'extd_number'
p142
g94
sS'mode'
p143
S'FM'
p144
sS'dtcs'
p145
I23
sS'offset'
p146
I0
sS'freq'
p147
I{}
sS'cross_mode'
p148
S'Tone->Tone'
p149
sS'ctone'
p150
F88.5
sS'empty'
p151
I00
sS'rtone'
p152
F88.5"""

sba_entry_template = """
sba(ichirp.chirp_common
Memory
p{}
(dp{}
g127
I0
sg128
g94
sg129
S'{}'
p{}
sg131
g115
sg132
g94
sg133
g94
sg134
F5.0
sg135
I{}
sg136
g94
sg137
(lp{}
sg139
I23
sg140
S'NN'
p{}
sg142
g94
sg143
S'FM'
p{}
sg145
I23
sg146
I0
sg147
I{}
sg148
S'Tone->Tone'
p{}
sg150
F88.5
sg151
I00
sg152
F88.5"""

postfix = """
sbatp{}
."""

# generate

output = []
output.append(prefix.format(label + str(channel), str(frequ)))
  # format label and frequ
while channel < channel_last:
  frequ += frequ_step
  channel += 1
  output.append(sba_entry_template.format(str(sbatp), str(sbatp + 1), label + str(channel), str(sbatp + 2), str(line_number_I), str(sbatp + 3),str(sbatp + 4),str(sbatp + 5), str(frequ),str(sbatp + 6)))
  sbatp += sbatp_step
  line_number_I += 1
output.append(postfix.format(sbatp))

# output

f = open(filename_output, "w")
f.writelines(output)
f.close()

#

quit()