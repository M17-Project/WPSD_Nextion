# Nextion Field Use with NextionDriver and WPSD

This document explains the basic status and text fields supplied by [MMDVMHost from G4KLX](https://github.com/g4klx/MMDVMHost) (in the [`Nextion.cpp`](https://github.com/g4klx/MMDVMHost/blob/master/Nextion.cpp) file), and [NextionDriver from ON7LDS](https://github.com/on7lds/NextionDriver). Using this information, you can build your own Nextion HMI files for use with WPSD.

Thank you to Jason KE7FNS who originally compiled this information and to Rob PD0DIB for providing the information.

## Page names

0. MMDVM
0. DStar
0. DMR
0. YSF
0. P25 
0. NXDN
0. POCSAG
0. M17

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

## Nextion Display Fields

### MMDVM

```
t0 : Owner call sign & DMR ID || errortext LOCKOUT
t1 : status || ERROR
t2 : Local date & time

  screenLayout >2 :
    t3  : IP Address
    t4  : Owner call sign
    t5  : Owner DMR ID
    t30 : RX Frequency
    t32 : TX Frequency
    t20 : CPU Temperature
    t31 : Location

  Nextion Driver only:
    t21     : CPU frequency
    t22     : CPU load average 1 min
    t23     : Disk free (in percent)
    cpuload : CPU load average 1 min
```

### DStar

```
t0 : Type MY1 MY2 // char text[50U]; ::sprintf(text, "t0.txt=\"%s %.8s/%4.4s\"", type, my1, my2);
t1 : UR           // char text[50U]; ::sprintf(text, "t1.txt=\"%.8s\"", your);
t2 : Reflector    // char text[50U]; ::sprintf(text, "t2.txt=\"via %.8s\"", reflector);
t3 : RSSI         // char text[25U]; ::sprintf(text, "t3.txt=\"-%udBm\"", m_rssiAccum1 / DSTAR_RSSI_COUNT);
t4 : BER          // char text[25U]; ::sprintf(text, "t4.txt=\"%.1f%%\"", m_berAccum1 / float(DSTAR_BER_COUNT))
```

### DMR

```
t0 : Timeslot 1 source DMR ID / Call sign / talkerAlias // char text[50U]; ::sprintf(text, "t0.txt=\"1 %s %s\"", type, src.c_str());
t1 : Timeslot 1 Destination                             // char text[50U]; ::sprintf(text, "t1.txt=\"%s%s\"", group ? "TG" : "", dst.c_str());
t2 : Timeslot 2 source DMR ID / Call sign / talkerAlias // char text[50U]; ::sprintf(text, "t2.txt=\"2 %s %s\"", type, src.c_str());
t3 : Timeslot 2 Destination                             // char text[50U]; ::sprintf(text, "t3.txt=\"%s%s\"", group ? "TG" : "", dst.c_str());
t4 : Timeslot 1 RSSI                                    // char text[25U]; ::sprintf(text, "t4.txt=\"-%udBm\"", m_rssiAccum1 / DMR_RSSI_COUNT);
t5 : Timeslot 2 RSSI                                    // char text[25U]; ::sprintf(text, "t4.txt=\"-%udBm\"", m_rssiAccum1 / DMR_RSSI_COUNT);
t6 : Timeslot 1 BER                                     // char text[25U]; ::sprintf(text, "t6.txt=\"%.1f%%\"", m_berAccum1 / DMR_BER_COUNT);
t7 : Timeslot 2 BER                                     // char text[25U]; ::sprintf(text, "t7.txt=\"%.1f%%\"", m_berAccum2 / DMR_BER_COUNT);

  screenLayout > 2 :
    t8  : Timeslot 2 type, talkerAlias  // char text[50U]; ::sprintf(text, "t8.txt=\"%s %s\"", type, talkerAlias);
    t9  : Timeslot 1 type, talkerAlias  // char text[50U]; ::sprintf(text, "t9.txt=\"%s %s\"", type, talkerAlias);

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
```

### YSF

```
t0 : Type, Source // char text[30U]; ::sprintf(text, "t0.txt=\"%s %.10s\"", type, source);
t1 : Destination  // char text[30U]; ::sprintf(text, "t1.txt=\"DG-ID %u\"", dgid);
t2 : Source       // char text[30U]; ::sprintf(text, "t2.txt=\"at %.10s\"", origin);
t3 : RSSI         // char text[25U]; ::sprintf(text, "t3.txt=\"-%udBm\"", m_rssiAccum1 / YSF_RSSI_COUNT);
t4 : BER          // char text[25U]; ::sprintf(text, "t4.txt=\"%.1f%%\"", m_berAccum1 / float(YSF_BER_COUNT));
```

### P25

```
t0 : Type, Source // char text[30U]; ::sprintf(text, "t0.txt=\"%s %.10s\"", type, source);
t1 : Destination  // char text[30U]; ::sprintf(text, "t1.txt=\"%s%u\"", group ? "TG" : "", dest);
t2 : RSSI         // char text[25U]; ::sprintf(text, "t2.txt=\"-%udBm\"", m_rssiAccum1 / P25_RSSI_COUNT);
t3 : BER          // char text[25U]; ::sprintf(text, "t3.txt=\"%.1f%%\"", m_berAccum1 / float(P25_BER_COUNT));
```

### NXDN

```
t0 : Type, Source // char text[30U]; ::sprintf(text, "t0.txt=\"%s %.10s\"", type, source);
t1 : Destination  // char text[30U]; ::sprintf(text, "t1.txt=\"%s%u\"", group ? "TG" : "", dest);
t2 : RSSI         // char text[25U]; ::sprintf(text, "t2.txt=\"-%udBm\"", m_rssiAccum1 / NXDN_RSSI_COUNT);
t3 : BER          // char text[25U]; ::sprintf(text, "t3.txt=\"%.1f%%\"", m_berAccum1 / float(NXDN_BER_COUNT));
```

### POCSAG

```
t0 : Waiting || RIC // char text[200U]; ::sprintf(text, "t0.txt=\"RIC: %u\"", ric);
t1 : Message        // char text[200U]; ::sprintf(text, "t1.txt=\"%s\"", message.c_str());
```

### M17

```
t0 : Type, Source // char text[30U]; ::sprintf(text, "t0.txt=\"%s %.10s\"", type, source);
t1 : Destination  // char text[30U]; ::sprintf(text, "t1.txt=\"%s\"", dest);
t2 : RSSI         // char text[25U]; ::sprintf(text, "t2.txt=\"-%udBm\"", m_rssiAccum1 / M17_RSSI_COUNT);
t3 : BER          // char text[25U]; ::sprintf(text, "t3.txt=\"%.1f%%\"", m_berAccum1 / float(M17_BER_COUNT));
```
