# import for webbrowser to work
import webbrowser

# import for csv reader to work
import csv

csvlist = raw_input('Enter csv document - ')

# opens csv file. site-list.csv was the name of the file being opened. This can be change to whatever the file is name
with open(csvlist, 'rb') as csvfile:

    #sites names the list that is in the csv.  this can change but will need to be changed whereever sites is used
    sites = csv.reader(csvfile, delimiter=' ')

    #next skips the first line of the csv as it is usually a header
    next(sites)

    rows = list(sites)

    # x = 0 starts our count a 0 and allows the if statement below to work.
    x = 0

    #defines the total of rows
    total = len(rows)

    for site in rows:

        #pulls the site from each row out of the ['']
        for s in site:

            # when this if statement is no longer true then the function will stop.
            if x != total:

                #prints string number, and link to ensure they are correct add to the end with + '/link'
                print str(x) + 'https://%s' % str(s)
                x += 1

                # opens each link in a browser tab.
                webbrowser.open_new('https://%s' % str(s))
