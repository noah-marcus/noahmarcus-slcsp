import argparse
import os.path
import logging

def parse_plans_csv(plans_csv_file):
    """
    Parse plans csv file and generate silver_plans_rates dictionary.

    Parameters:
    plans_csv_file : str
        Filename given by user for csv file that contains all health plans in the U.S.

    Returns:
    silver_plans_rates_dict : dict
        Dictionary of all silver rate plans found in csv file
        key: tuple ('State', 'Rate Area')
        values: { plan_id : str, lowest_rate : float, second_lowest_rate : float }
    """
    # Init return variable
    silver_plans_rates_dict = {}

    # Open file
    with open(plans_csv_file) as plans_csv:
        # Skip first line in csv file
        next(plans_csv)

        # Compile silver plans and rates into dictionary
        for plan in plans_csv:
            # Split plan line by comma
            plan_params = plan.strip().split(',')

            # Parse plan values
            plan_id = plan_params[0]
            state = plan_params[1]
            metal_level = plan_params[2]
            rate = float(plan_params[3])
            rate_area = int(plan_params[4])

            # If data is incomplete, skip entry
            if not plan_id or not state or not metal_level or not rate or not rate_area:
                continue

            # Create rate area tuple from parameters
            rate_area_tuple = (state, rate_area)

            # Save data if silver plan
            if metal_level.lower() == "silver":

                # Add plan rate to dictionary
                if rate_area_tuple in silver_plans_rates_dict:
                    # Check if new rate is lowest or second lowest
                    if rate < silver_plans_rates_dict[rate_area_tuple]['lowest_rate']:
                        # If new rate is lowest, move previous lowest to second_lowest_rate
                        silver_plans_rates_dict[rate_area_tuple]['second_lowest_rate'] = silver_plans_rates_dict[rate_area_tuple]['lowest_rate']
                        # Set new lowest rate
                        silver_plans_rates_dict[rate_area_tuple]['lowest_rate'] = rate

                    elif silver_plans_rates_dict[rate_area_tuple]['second_lowest_rate'] == None \
                        or rate < silver_plans_rates_dict[rate_area_tuple]['second_lowest_rate']:
                        # If new rate is lower than the current second lowest rate, but higher than the current lowest rate
                        # replace the current second lowest rate
                        silver_plans_rates_dict[rate_area_tuple]['lowest_rate'] = rate


                # Create entry in dictionary if it does not exist yet
                else:
                   silver_plans_rates_dict[rate_area_tuple] = {
                        'lowest_rate': rate,
                        'second_lowest_rate': None,
                        'plan_id': plan_id
                   }


        return silver_plans_rates_dict

def parse_zips_csv(zips_csv_file):
    """
    Parse zips csv file and generate zip_code_to_rate_area dictionary.

    Parameters:
    zips_csv_file : str
        Filename given by user for csv file that contains a mapping of ZIP code to county/counties & rate area(s)

    Returns:
    zip_code_to_rate_area_dict : dict
        key: zipcode : str
        values: { tuple ('State', 'Rate Area') }
    """
    # Init return variable
    zip_code_to_rate_area_dict = {}

    # Open file
    with open(zips_csv_file) as zips_csv:
        # Skip first line in csv file
        next(zips_csv)

        # Compile zip codes and rate areas into dictionary
        for zip in zips_csv:
            # Split zip line by comma
            zip_params = zip.strip().split(',')

            # Parse zip values
            zipcode = zip_params[0]
            state = zip_params[1]
            county_code = zip_params[2]
            name = zip_params[3]
            rate_area = int(zip_params[4])

            # If data is incomplete, skip entry
            if not zipcode or not state or not county_code or not name or not rate_area:
                continue

            # Create rate area tuple from parameters
            rate_area_tuple = (state, rate_area)

            if zipcode not in zip_code_to_rate_area_dict:
                # If zipcode does not exist, add to dictionary
                zip_code_to_rate_area_dict[zipcode] = rate_area_tuple
            else:
                # If zipcode is already in dictionary, we have a duplicate and the answer is ambigious
                zip_code_to_rate_area_dict[zipcode] = None

    return zip_code_to_rate_area_dict

def generate_slcsp(input_csv_file, silver_plans_rates_dict, zip_code_to_rate_area_dict):
    """
    Parse zips csv file and generate zip_code_to_rate_area dictionary.

    Parameters:
    input_csv_file : str
        Filename given by user for csv file that contains ZIP codes of interest
    silver_plans_rates_dict : dict
        Dictionary linking silver plans to their second lowest rates
    zip_code_to_rate_area_dict : dict
        Dictionary linking zip codes to rate areas

    Returns:
    slcsp_result : str
        CSV formatted string of input (ZIP codes of interest) with the slcsp in the second column
    """

def main():
    """
    Main function of calc_slcsp.py.

    Parse arguments and calculate the SLCSP of the given file.
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

    # Generate silver plan rates
    silver_plans_rates_dict = parse_plans_csv(plans_csv_file)

    # Generate zip code dictionary
    zip_code_to_rate_area_dict = parse_zips_csv(zips_csv_file)

    # Find SLCSP for inputs
    slcsp_result = generate_slcsp(input_csv_file, silver_plans_rates_dict, zip_code_to_rate_area_dict)

if __name__ == "__main__":
    main()
