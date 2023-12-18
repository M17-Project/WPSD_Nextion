# Nextion Field Use with NextionDriver and WPSD

This document explains the basic status and text fields supplied by MMDVMHost from G4KLX, and NextionDriver from ON7LDS. Using this information, you can build your own Nextion HMI files for use with WPSD.

Thank you to Jason KE7FNS who originally compiled this information and to Rob PD0DIB for providing the information.

## Page names

* 0 page MMDVM
* 1 page DStar
* 2 page DMR
* 3 page YSF
* 4 page P25 
* 5 page NXDN
* 6 page POCSAG
* 7 page M17

## MMDVM Status values

```
0   : bkcmd  (Nextion command to stop all success/failure messages over the serial port)
11  : IDLE
12  : CW Ident
13  : ERROR text
14  : ERROR
15  : LOCKOUT
16  : IP Address
17  : ID/Call (t0 and if layout >2 t4,and t5 are sent also)
19  : END
20  : RX Frequency
21  : TX Frequency
22  : Temperature
23  : Location
24  : Nextion Driver extra info update (t3, t20, t21, t22, t23, cpuload)

41  : D-Star listening
42  : Type MY1 MY2
45  : UR
46  : Reflector
47  : RSSI
48  : BER

61  : Timeslot 1 DMR listening
62  : Timeslot 1 DMR ID
63  : Timeslot 1 TalkerAlias
64  : Timeslot 1 Call end
65  : Timeslot 1 TG
66  : Timeslot 1 RSSI
67  : Timeslot 1 BER
68  : Timeslot 1 User data (t18,19,20,21,22)
69  : Timeslot 2 DMR listening
70  : Timeslot 2 DMR ID
71  : Timeslot 2 TalkerAlias
72  : Timeslot 2 Call end
73  : Timeslot 2 TG
74  : Timeslot 2 RSSI
75  : Timeslot 2 BER
76  : Not used?
77  : Not used?
78  : Timeslot 2 User data (t13,14,15,16,17)

81  : YSF listening
82  : Source
83  : Destination
84  : Origin
85  : RSSI
86  : BER

101 : P25 listening
102 : Source
103 : Destination
104 : RSSI
105 : BER

121 : NXDN listening
122 : Source
123 : Destination
124 : RSSI
125 : BER

132 : RIC
133 : Message text
134 : Waiting / Idle
```

## Fields

```
MMDVM
t0 : Owner call sign & DMR ID || errortext LOCKOUT
t1 : status || ERROR
t2 : Local date & time

  screenLayout >2 :
    t3  : ip address
    t4  : owner call
    t5  : owner ID
    t30 : RX Frequency
    t32 : TX Frequency
    t20 : CPU Temperature
    t31 : location

  Nextion Driver only:
    t21     : CPU frequency
    t22     : CPU load average 1 min
    t23     : Disk free (in percent)
    cpuload : CPU load average 1 min



DStar
t0 : Type MY1 MY2
t1 : UR
t2 : Reflector
t3 : RSSI
t4 : BER


DMR
t0 : Timeslot 1 source DMR ID / Call sign / TalkerAlias
t1 : Timeslot 1 Destination
t2 : Timeslot 2 source DMR ID / Call sign / TalkerAlias
t3 : Timeslot 2 Destination
t4 : Timeslot 1 RSSI
t5 : Timeslot 2 RSSI
t6 : Timeslot 1 BER
t7 : Timeslot 2 BER

  screenLayout >2 :
    t8  : Timeslot 2 type, talkerAlias
    t9  : Timeslot 1 type, talkerAlias

      Nextion Driver only:
        t10 : Timeslot 1 TG name
        t11 : Timeslot 2 TG name

    t12 : Not used?
    t13 : CSV lookup data TS2
    t14 : CSV lookup data TS2
    t15 : CSV lookup data TS2
    t16 : CSV lookup data TS2
    t17 : CSV lookup data TS2
    t18 : CSV lookup data TS1
    t19 : CSV lookup data TS1
    t20 : CSV lookup data TS1
    t21 : CSV lookup data TS1
    t22 : CSV lookup data TS1


YSF
t0 : Type, Source
t1 : Destination
t2 : Source
t3 : RSSI
t4 : BER


P25
t0 : Type, Source
t1 : Destination
t2 : RSSI
t3 : BER


NXDN
t0 : Type, Source
t1 : Destination
t2 : RSSI
t3 : BER

POCSAG
t0 : Waiting || RIC
t1 : Message

M17
t0 : Type, Source
t1 : Destination
t2 : RSSI
t3 : BER
```