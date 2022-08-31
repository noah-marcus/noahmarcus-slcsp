# SLCSP
Repository for the AdHoc 'SLCSP' homework assignment. Contains python script that determines the second lowest cost silver plan (SLCSP) for a group of ZIP codes.

## Background
The SLCSP is the so-called "benchmark" health plan in a particular area. It's used to compute the tax credit that qualifying individuals and families receive on the marketplace. It's the second lowest rate for a silver plan in the rate area.

For example, if a rate area had silver plans with rates of [197.3, 197.3, 201.1, 305.4, 306.7, 411.24], the SLCSP for that rate area would be 201.1, since it's the second lowest rate in that rate area.

The script in this repository will determine the second lowest cost plan on a given set of ZIP codes.

## Environment Set-Up
First, clone the repository:

```
# Clone noahmarcus-slcsp repository
git clone git@github.com:noah-marcus/noahmarcus-slcsp.git
```

The script does not require any third-pary Python packges. It was built and tested with `Python 3.8.7`. If you do not have Python3 installed, please run the following command:

```
# Install Python3.8
sudo apt-get install python3.8
```

While not necessary, you may want to create a virtual enviroment for this project to enusre there is no accidental conflict with other Python projects on your machine. Instructions are provided below for this optional step:

```
# Navigate to project directory
cd /path/to/noahmarcus-slcsp

# Create a Python3 virtual environment
python3 -m venv slcsp-env

# Enter virtual environment
source slcsp-env/bin/activate
```

## Running the Script
The python script `calc_slcsp.py` will calculate the second lowest cost silver plan on a set of given input files. The following three CSV formatted files are passed in via command line arguments and are required:
  1. Input File (Ex: `inputs/slcsp.csv`) - CSV file that contains ZIP codes of interest in the first column
  2. Plans File (Ex: `inputs/plans.csv`) - CSV file that contains all the health plans in the U.S. on the marketplace
  3. Zips File  (Ex: `inputs/zips.csv`) - CSV file that contains a mapping of ZIP code to county/counties & rate area(s)

Example files are provided under the `noahmarcus-slcsp/inputs` directory.

Supply these three files to the script via the command:

```
# Run calc_slcsp with provided input files
python3 calc_slcsp.py -p inputs/plans.csv -z inputs/zips.csv -i inputs/slcsp.csv
```

The script's usage message is printed below for reference.

```
usage: calc_slcsp.py [-h] -p PLANS -z ZIPS -i INPUT [--log LOG]

Determine the second lowest cost silver plan (SLCSP) for a group of ZIP codes. Results printed to stdout.

optional arguments:
  -h, --help                show this help message and exit
  -p PLANS, --plans PLANS   CSV file that contains all the health plans in the U.S. on the marketplace
  -z ZIPS, --zips ZIPS      CSV file that contains a mapping of ZIP code to county/counties & rate area(s)
  -i INPUT, --input INPUT   CSV file that contains desired ZIP codes in the first column
  --log LOG                 Set log level. Default: ERROR
```
