birds_file = file('birds.csv','rU')
birds = {}
count = 0
birds_file.readline()
for line in birds_file:
    line_list = line.strip().split(',')
    bird_name = line_list[0]
    data = [int(x) for x in line_list[1:]]
    birds[bird_name]=data
    if count > 20:
        break
    count += 1

for bird,data in birds.items():
    print bird, data

#name = raw_input("Enter a bird: ")
#print name
#print birds[name]

year_str = raw_input("Enter a year: ")
year_int = int(year_str)
year_index = year_int - 2000
#print birds[name][year_index]

for bird,data in birds.items():
    #print "%30s %d"% (bird, data[year_index])    # Python 2
    print "{:30s} {:d}".format(bird, data[year_index]) # Python 3 syntax that works on Python 2
