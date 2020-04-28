import csv


# In this folder we have a CSV representing all Hugo award winners (except for that bad year when the award got taken over)
# I pull in the CSV and find all the books that have relatively short titles
# Brevity is the soul of wit (plus it's saves time)

# open the file and save to a variable
# the 'r' means "read"
file = open('hugo_winners.csv', 'r')


# Create a DictReader object based on the CSV file
# This object is really just something to loop over, it doesn't do much else
# On looping, each book is represented as a dictionary
# You can see the docs here but docs can be hard to read as a beginner:
# https://docs.python.org/3/library/csv.html
books = csv.DictReader(file)



# loop over the reader object. each "iteration" (round through the loop)
# represents a book with title, first sentence, etc.


for book in books:
    
    # Show the books with short titles
    if len(book['title']) < 14:
        print(book['title'])



# There's a lot more to do with CSVs, including writing them
# Look in the docs for the writer objects and try to figure out how to use them
# or do soemthing else with CSVs :)

# Email with questions
