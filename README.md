# PIR Motion Sensor Build Instructions for the LumiMonitor

## Table of Contents
[Introduction](https://github.com/KyleV1999/LumiMonitor#Introduction)

[Budget](https://github.com/KyleV1999/LumiMonitor#Budget)


## Introduction

This is the build instructions for building the PIR Motion sensor as part of the LumiMonitor project. The PIR (Passive Infared) Motion Sensor will detect motion within 3 meters of the sensor. These instuction will show you how to design and build the breadboard and PCB circuits to intigrate the sensor with a Broadcom Development Platform (Raspberry Pi 3B+). I will also provide a list of materials and links to where you can buy them, as well as a Corel Draw file so that you can laser cut a case out of clear acrylic. These instutions take into account that you will have access to equipment such as a soldering iron, laser cutter, wire strippers, etc. The PIR Motion Sensor will be used in the final Lumi Monitor project to intiate hands-free data collection. The photo below depicts the final product:

![Final Product](Images/box_sensormount.jpg)

Before you begin some skills you will need duing the build of this project include:
* Basic electrical and circuit knowledge
* Basic programming knowledge
  * This project specifically was programmed in Python
* Basic understanding of the Raspberry Pi and Linux based operating systems
* Soldering

## Budget
Thse are the parts needed to complete the project. Displayed below are links and price breakdown for each component.

**Parts for Lumi Monitor**

| Part   | Source  | Part Number | # of Units | Price Per Unit (CAD)  | Taxes & Shipping (CAD) | Subtotal  | Link |
| ------ | ------- | ----------- | --------------- | --------------- | ---------------------- | --------- | ---- |
| Raspberry Pi 3 B+ Motherboard | Amazon | 3BPLUS-R | 1 | $55.97 | $7.28 | $63.25 | https://amzn.to/2kMYDtb |
| Grove ‐ PIR Motion Sensor | Digikey | 101020020 | 1 | $11.56 | $8.35 | $19.91 | https://bit.ly/2kKx8QV | 
| Seeedstudio Grove 4-pin Connector (10) | robotshop.com | RB-See-204 | 1 | $1.33 | $9.01 | $11.67 | https://bit.ly/32it9vh |
| Breakaway PCB Board Header Connector | Amazon | ODYF162934WAZR85384 | 1 | $12.80 | $4.18 | $16.98 | https://amzn.to/37IDlAd |
| Elegoo 120pcs Multicolored Dupont Wire | Amazon | EL-CP-004 | 1 | $11.95 | $4.36 | $16.31 | https://amzn.to/2qHYRop |
| Kingston 32 GB Micro SD Card | Walmart | SDCS/32GBCR | 1 | $11.98 | $2.98 | $14.96 | https://bit.ly/2souG61 / In Store |
| AmazonBasics USB 3.0 to Ethernet Adapter | Amazon | AE3101X1 | 1 | $20.05 | $4.53 | $24.58 | https://amzn.to/2Nwrq0A |
| 3ft Ethernet Cable| PrimeCables.ca | | 1 | $1.24 | $6.88 | $8.12 | https://bit.ly/2QYcxGe |
| Raspberry Pi Micro USB Power Supply | Amazon |DCAR-RSP-2A5 | 1 | $11.99 | $6.36 | $18.35 | https://amzn.to/2skohZp |
| Clear Acrylic Glass 3mm | Amazon | | 1 | $17.09 | $0.00 | $17.09 | https://amzn.to/2XWM1OX |
| M2.5 Screws | Digikey | | 4 | $0.15 | $0.00 | $0.60 | https://bit.ly/2Oy8TS9 |
| Lead Free Solder | Amazon | 2-CA-X | 1 | $15.99 | $4.32 | $20.31 | https://amzn.to/37JXLJj |
| Total Cost | $232.13 |
| Total Tax & Shipping | $58.25 | 

**Below are images for major components used:**

Grove PIR Motion Sensor - Sensor

![Motion Sensor](Images/grovesensor.jpg)

Broadcom Development Platform / Raspberry Pi 3B+

![Raspberry Pi 3B+](Images/raspberrypi3b+.jpg)

Grove Headers - Used to connect sensor to PCB

![Headers](https://www.robotshop.com/media/catalog/product/cache/image/1350x/9df78eab33525d08d6e5fb8d27136e95/s/e/seeedstudio-grove-4-pin-connector-1_1.jpg)

AmazonBasics USB 3.0 to Ethernet Adapter - Used for SSH and remote desktop connection with development platform

![USB To Ethernet](https://images-na.ssl-images-amazon.com/images/I/71NMeVTevGL._SX425_.jpg)

## Time Commitment






























