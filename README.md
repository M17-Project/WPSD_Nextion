# WPSD Nextion

WPSD Nextion is a set of Nextion HMI and TFT files for use with various TFT screens made by Nextion for WPSD based hotspots and repeaters.

## Installation

* Use a microSD card formatted as FAT32
  * **Recommended:** A microSD card no greater than 32 GB
* Download the TFT file for your model of Nextion screen
* Copy the TFT file to the microSD card
  * The only file on the card should be the TFT file
* Ensure the Nextion screen is powered off before inserting the microSD card
* Insert the microSD card containing TFT file into the Nextion screen
* Power on the Nextion screen with recommended clean power as per its Datasheet
* Allow the Nextion device to upload the TFT file
  * The upload may take several minutes, a progress bar will show while the upload is running
* After the upload succeeds, power off the Nextion screen
* Remove microSD card from the Nextion screen
* Power on the Nextion with recommended clean power as per its Datasheet
* Reattach the Nextion screen to your hotspot/repeater

## Roadmap

- [x] Create initial draft
- [ ] Fill in Info Page
- [ ] Get buttons working on main page

## Credits / Software Used

* FLAGCODE from Rob van Rheenen, PD0DIB

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)