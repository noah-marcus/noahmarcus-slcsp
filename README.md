# SLCSP
Repository for the AdHoc 'SLCSP' homework assignment. Contains python script that determines the second lowest cost silver plan (SLCSP) for a group of ZIP codes.

## Environment Set-Up
Before we can run the script to calculate the SLCSP, we must first create a python virtual environment to ensure all necessary packages are installed.

First, let's clone the repository:

```
# Clone noahmarcus-slcsp repository
git clone git@github.com:noah-marcus/noahmarcus-slcsp.git
```

Now let us create the virtual environment and install the required packages:

```
# Navigate to project directory
cd /path/to/noahmarcus-slcsp

# Create a Python3 virtual environment
python3 -m venv slcsp-env

# Enter virtual environment
source slcsp-env/bin/activate

# Install required packages (TBD)
# python3 -m pip install -r requirements.txt
```

## Running the Script

TBD

The script's usage message is printed below for reference.

```
usage: calc_slcsp.py [-h] -p PLANS -z ZIPS -i INPUT [--log LOG]

Determine the second lowest cost silver plan (SLCSP) for a group of ZIP codes. Results printed to stdout.

optional arguments:
  -h, --help            show this help message and exit
  -p PLANS, --plans PLANS
                        CSV file that contains all the health plans in the U.S. on the marketplace
  -z ZIPS, --zips ZIPS  CSV file that contains a mapping of ZIP code to county/counties & rate area(s)
  -i INPUT, --input INPUT
                        CSV file that contains desired ZIP codes in the first column
  --log LOG             Set log level. Default: ERROR
  ```
