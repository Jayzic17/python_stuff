import sys, fileinput, os, csv

# Read from finalized .txt report
txt_file = open(sys.argv[1], 'r')
file_content = txt_file.read()
tag_list = file_content.split('\n')
txt_file.close()

# Write to .csv
with open(sys.argv[2], mode='w') as file:
    writer = csv.writer(file, delimiter=',')
    for line in tag_list:
        writer.writerow([line])