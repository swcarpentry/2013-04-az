# read a collection of fastq records and print the first 
# 10 sequences
import sys
import screed

filename = sys.argv[1]
print filename

counter = 0
for record in screed.open(filename):
    counter +=1
    sequence = record['sequence']
    print sequence
    if counter >10:
        break

