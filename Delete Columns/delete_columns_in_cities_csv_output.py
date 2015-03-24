import csv
import codecs

filename = "AD.txt"

with codecs.open(filename, 'rb', 'utf-8') as infile, codecs.open("out.csv", 'wb', 'utf-8') as outfile:
  writer = csv.writer(outfile, delimiter='\t')

  for line in infile:
    #print line
    line = line.split("\t")
    line = [line[1], line[2], line[4], line[5], line[8], line[10]]
    #line = [line[2], line[4], line[5], line[8], line[10]]
    #print line
    #break
    #line = "\t".join(line)
    #line = line + "\n"
    #print line
    #outfile.write(line)
    writer.writerow(unicode(line).encode("utf-8"))
    #writer.writerow(line)