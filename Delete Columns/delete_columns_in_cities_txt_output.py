import codecs

filename = "AD.txt"

with codecs.open(filename, 'rb', 'utf-8') as infile, codecs.open("out.txt", 'wb', 'utf-8') as outfile:

  for line in infile:
    line = line.split("\t")
    line = [line[1], line[2], line[4], line[5], line[8], line[10]]
    separator = "\t"
    line = separator.join(line) + "\n"
    outfile.write(line)