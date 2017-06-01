import csv

# Files
meta_information_file   = 'Indicator_meta_template_GCAM_v2.csv'
input_files             = ['GCAM_No_Paris.csv', 'GCAM_Paris.csv', 'GCAM_Paris_Plus.csv', 'GCAM_Ref.csv']
output_file             = 'Time_series_GCAM.csv'

# Read in meta file, make dictionary of model name to ESP name
ESP_col = 0
GCAM_col = 1
indicator_dict = {}
with open(meta_information_file, 'rt') as f:
    csvreader   = csv.reader(f)
    headers     = next(csvreader)
    for row in csvreader:
        # read in rows only if there is an indicator for GCAM
        if row[GCAM_col]:
            indicator_dict[row[GCAM_col]] = row[ESP_col]

# define set of known countries
country_set = {'Argentina', 'Australia_NZ', 'Brazil', 'Canada', 'China',
                'Colombia', 'EU-12', 'EU-15', 'India', 'Indonesia', 'Japan',
                'Mexico', 'Pakistan', 'Russia', 'South Africa', 'South Korea',
                'Taiwan', 'USA', 'World'}

# set headers for output file
output_headers = ['Model', 'Scenario', 'Region', 'ESP Slug', 'Unit of entry',
                  '2005', '2010', '2020', '2030', '2040', '2050', '2060',
                  '2070', '2080', '2090', '2100']
# open output file for writing
with open(output_file, 'w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow(output_headers)
    # read in input files
    for file in input_files:
        with open(file, 'r') as f:
            csvreader = csv.reader(f)
            # scan through rows for headers
            while True:
                headers = next(csvreader)
                # if the first entry of the row is called 'model' this row is the header
                # (this is specific to the GCAM input files)
                if headers[0].lower() == 'model':
                    break
            # find the column with indicators
            indicator_col = headers.index('Variable')
            # find the column with country names
            country_col = headers.index('region')
            # read through all rows and write to output file on-the-fly
            for row in csvreader:
                country = row[country_col]
                if country in country_set:
                    if row[indicator_col] in indicator_dict.keys():
                        # # replace GCAM name with ESP name TO BE DECIDED
                        # row[indicator_col] = indicator_dict[row[indicator_col]]
                        # write output row
                        writer.writerow(row)

print("Finished.")
