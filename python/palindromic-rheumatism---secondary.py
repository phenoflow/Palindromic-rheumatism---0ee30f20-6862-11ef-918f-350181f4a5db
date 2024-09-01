# phekb, 2024.

import sys, csv, re

codes = [{"code":"1570266","system":"ICD10CM"},{"code":"1570267","system":"ICD10CM"},{"code":"1570268","system":"ICD10CM"},{"code":"45543472","system":"ICD10CM"},{"code":"45557796","system":"ICD10CM"},{"code":"45567454","system":"ICD10CM"},{"code":"1570266","system":"ICD10CM"},{"code":"45543472","system":"ICD10CM"},{"code":"1570267","system":"ICD10CM"},{"code":"45557796","system":"ICD10CM"},{"code":"1570268","system":"ICD10CM"},{"code":"45567454","system":"ICD10CM"},{"code":"44819966","system":"ICD10CM"},{"code":"44819966","system":"ICD10CM"},{"code":"1570266","system":"ICD10CM"},{"code":"1570267","system":"ICD10CM"},{"code":"1570268","system":"ICD10CM"},{"code":"45543472","system":"ICD10CM"},{"code":"45557796","system":"ICD10CM"},{"code":"45567454","system":"ICD10CM"},{"code":"1570266","system":"ICD10CM"},{"code":"45543472","system":"ICD10CM"},{"code":"1570267","system":"ICD10CM"},{"code":"45557796","system":"ICD10CM"},{"code":"1570268","system":"ICD10CM"},{"code":"45567454","system":"ICD10CM"},{"code":"44819966","system":"ICD10CM"},{"code":"44819966","system":"ICD10CM"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('palindromic-rheumatism-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["palindromic-rheumatism---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["palindromic-rheumatism---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["palindromic-rheumatism---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
