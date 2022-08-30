import argparse
import os.path
import logging

def main():
    """
    main() - Main function of calc_slcsp.py

    Description: Parse arguments and calculate the SLCSP of the given file.
    """

    # Initialize parser
    parser = argparse.ArgumentParser(description="Determine the second lowest cost silver plan (SLCSP) for a group of ZIP codes. Results printed to stdout.")
    parser.add_argument('-p', '--plans', help="CSV file that contains all the health plans in the U.S. on the marketplace", required=True)
    parser.add_argument('-z', '--zips', help="CSV file that contains a mapping of ZIP code to county/counties & rate area(s)", required=True)
    parser.add_argument('-i', '--input', help="CSV file that contains desired ZIP codes in the first column", required=True)
    parser.add_argument('--log', help="Set log level. Default: ERROR", default="ERROR")
    # Parse arguments
    args = parser.parse_args()
    plans_csv_file = args.plans
    zips_csv_file = args.zips
    input_csv_file = args.input
    log_level = args.log

    # Init logger
    logging.basicConfig(level=log_level)

    # Validate files
    if not os.path.isfile(plans_csv_file) \
        or not os.path.isfile(zips_csv_file) \
        or not os.path.isfile(input_csv_file):

        logging.error(f"File Validation Error\nFile(s) given could not be validated as a file. Please check inputs to script.\nInput given -- Plans CSV: {plans_csv_file}, Zip CSV: {zips_csv_file}, Input CSV: {input_csv_file}\n")
        exit(1)

    logging.info("Files Validated\nInput given -- Plans CSV: {plans_csv_file}, Zip CSV: {zips_csv_file}, Input CSV: {input_csv_file}")

if __name__ == "__main__":
    main()
