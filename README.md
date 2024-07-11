# Solar Active Region Classification using SVM

## Links

* Reference paper https://iopscience.iop.org/article/10.1088/0004-637X/798/2/135
* For data download https://github.com/alciomarhollanda/DATA-SET-FOR-SOLAR-FLARE-PREDICTION

## Data
The data consists of physical parameters derived from the SHARP data products.
* Active Region observations from 2010 - 2014
* Limited to five parameters
* Labelled into flaring or non-flaring based on the GOES event list

## Quick Setup Guide

* Install dependencies
```
pip install -r requirements.txt
```

* Download the data
```
gdown --fuzzy "https://drive.google.com/file/d/11qNpY_boQ0Y4m10xSoZBrVoaQ0xMIo6l/view?usp=sharing"
```
* Check data integrity
```
md5sum -c data/combined_sharp_lorentz_labeled.csv.md5
```
