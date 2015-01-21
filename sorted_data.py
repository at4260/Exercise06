def restaurant_rev():

    # open and read the file
    rest_scores = {}
    f = open('scores.txt')

    # create a dictionary with the scores.txt data to have restaurant: rating
    for line in f:
        # print line
        line = line.strip()
        # print line
        restaurant = line.split(':')
        rest_scores[restaurant[0]] = restaurant[1]

    f.close()
    # get the keys and sorts the keys
    # creates a list of the keys that it sorts
    alpha = sorted(rest_scores)
    print alpha
    # loop through each key=value pair and print the statement

    for key in alpha:
    print "Restaurant %s is rated at a %s." % (key, rest_scores[key])
