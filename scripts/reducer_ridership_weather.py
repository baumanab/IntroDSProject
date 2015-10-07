def mapper():
    def format_key(fog, rain):
        return '{}fog-{}rain'.format(
            '' if fog else 'no',
            '' if rain else 'no'
        )

    for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) == 22 and data[6] == 'ENTRIESn_hourly':
            continue
        print "{0}\t{1}".format(format_key(float(data[14]), float(data[15])), data[6])

mapper()

def reducer():
    riders = 0      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        this_key, count = data


        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, float(riders/num_hours))
            riders = 0
            num_hours = 0
        old_key = this_key
        riders += float(count)
        num_hours += 1

    if old_key != None:
        print "{0}\t{1}".format(old_key, float(riders/num_hours))

reducer()