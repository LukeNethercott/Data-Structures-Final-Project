pages_visited=['churchofjesuschrist.org', 'byui.edu', 'familysearch.org', 'github.com', 'byui.instructure.com']

#Adds every URL that a user visits to the top of the stack
def new_page(stack, url):
    pass

#Removes a URL from the stack when the back button is pressed
def go_back(stack):
    pass




#Everything below this line is for testing purposes only ------------------------------------------

#The user then visits steam.com
new_page(pages_visited, 'steam.com')

#The user then visits gmail.com
new_page(pages_visited, 'gmail.com')

#The user then clicks the back button three times
go_back(pages_visited)
go_back(pages_visited)
go_back(pages_visited)

#The user then visits comeuntochrist.org
new_page(pages_visited, 'comeuntochrist.org')

#If you completed the practice correctly, it should print ['churchofjesuschrist.org', 'byui.edu', 'familysearch.org', 'github.com', 'comeuntochrist.org']
print(pages_visited)