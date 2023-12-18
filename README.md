# WPSD Nextion Screens

The WPSD Nextion repo is a set of Nextion HMI (source) and TFT (compiled) files for use with various TFT screens made by Nextion for WPSD-based hotspots and repeaters.

## Currently Available Screens

Model | Size | Notes
---|---|---
[NX4832K035_WPSD_3.5_Nextion](TFT/NX4832K035_WPSD_3.5_Nextion.tft) | 3.5" | 
[NX4827K043_WPSD_4.3_Nextion](TFT/NX4827K043_WPSD_4.3_Nextion.tft) | 4.3" | 
[NX8048K050_WPSD_5.0_Nextion](TFT/NX8048K050_WPSD_5.0_Nextion.tft) | 5.0" | 
[NX8048K050_WPSD_5.0_Nextion_HighSpeed](TFT/NX8048K050_WPSD_5.0_Nextion_HighSpeed.tft) | 5.0" | High Speed


## Installation

1. Use a microSD card no greater than 32 GB formatted as FAT32
2. Download the TFT file for your model of the Nextion screen
3. Copy the TFT file to the microSD card

    :bulb:  The only file on the card should be the TFT file

4. Insert the microSD card containing the TFT file into the Nextion screen
  
    :exclamation:  Ensure you power down the Nextion screen before inserting the microSD card

5. Power on the Nextion screen with recommended clean power as per its Datasheet

6. Allow the Nextion device to upload the TFT file

    :information_source: The upload may take several minutes; a progress bar will show while the upload is running

6. After the upload succeeds, power off the Nextion screen

7. Remove the microSD card from the Nextion screen

8. *Optional*: Power on the Nextion as a test with recommended clean power as per its Datasheet

9. Reattach the Nextion screen to your hotspot/repeater

## Roadmap

- [x] Create initial draft
- [ ] Fill in Info Page
- [ ] Get buttons working on main page

## Credits / Software Used

* FLAGCODE from Rob van Rheenen, PD0DIB

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you want to change.

Please make sure to update tests as appropriate.

## License

[GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
