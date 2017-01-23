import webbrowser #import webbrowser functionality

importantUrls = ["www.reddit.com", "www.youtube.com", "www.macrumors.com"] #collection of sites you'd like to open later on


def open_tabs(url_listers):  #function that iterates through elements of an array 
	for element in url_listers: #for loop that iterates through any given array passed through as an argument
		webbrowser.open_new_tab(element) #use the webbrowser function to open each url in a new tab


def main(): #main method where we call our functions
	webbrowser.open("www.google.ca", new=2, autoraise=False) #first tab that will open with the web browser
	open_tabs(importantUrls) #calling the open_tabs function we created earlier and using it to iterate through each element in the array 

main() #calling the main method so the program will start :)