
def parsed_html(filename_for_link, filename_for_data, number_of_titles_to_add):
    import csv
    total_website_data ='<h3>Chelsea News from Weaintgotnohistory.sbnation.com</h3><br>'
    data = []
    link= []
    with open(filename_for_link) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            row = str(row)
            link.append(row[2:-2])
            
    with open(filename_for_data,"r") as f2:
        for lines in f2:
            data.append(lines)

    starting_tags='<a href="'
    middle_tags= '">'
    ending_tags = "</a><br><br>"
    i =1
    while i<=number_of_titles_to_add:
        line = starting_tags + link[i] + middle_tags + data[i] + ending_tags
        i+=1
        total_website_data+=line
    return total_website_data