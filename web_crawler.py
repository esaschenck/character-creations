# code for using beautiful soup/ requests
# https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486

# code for getting text on pages from:
# https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
from graphics import *
from random import *


class MyPages:
    '''constructs MyPages object to collect links and analyze pages'''

    

    def __init__(self, base_url):
        '''initalizes the first page (var: baseurl) and calls methods in the class
            to get the other pages and urls in those pages and decode the html '''

        # initializes universal dictionary where key = url and value = decoded html
        # this will store every url visited 
        self.pages = {}
        
        baseurl = 'https://www.nytimes.com/2019/11/20/science/dna-genetics-cancer.html?fallback=false&recId=122371034&locked=0&geoContinent=NA&geoRegion=MA&recAlloc=control&geoCountry=US&blockId=discovery-automated&imp_id=914147840&action=click&module=Science%20%20Technology&pgtype=Homepage'
        baseurl = 'https://www.nytimes.com/2019/12/07/health/sickle-cell-adakveo-oxbryta.html'
        #baseurl = 'https://www.nytimes.com/2019/12/03/health/drug-prices-pelosi-unions.html'
        baseurl = 'https://www.nytimes.com/2019/12/04/us/politics/turley-impeachment.html?action=click&module=Top%20Stories&pgtype=Homepage'
       # baseurl = 'https://www.nytimes.com/2019/12/04/well/move/exercise-aging-inflammation-muscles-age-seniors-elderly-older.html?algo=identity&fellback=false&imp_id=945067857&imp_id=25621643&action=click&module=Science%20%20Technology&pgtype=Homepage'
        baseurl = base_url
        # uses self.get_page_from_url() to get decoded html
        first_page = self.get_page_from_url(baseurl)
        
        # uses self.get_pages() to create a new dictionary for only the first page
        # where key = url and value = decoded html, dictionary will be used to go to the pages
        # these urls link to
        first_pages = self.get_pages(first_page, baseurl)
    
        #print('pages dict', self.pages)

        print('DEPTH = 1')

        counter = 0
        

        # runs through first_pages dictionary 
        for page_url, page in first_pages.items():
            self.pages[page_url] = page
            # finds the base_url for each page_url, assumes it is
            # the page_url before the third slash
            #print("PAGE URL FOR TESTING", page_url)
            base_url = page_url[:page_url.find('/', 8)]
            # uses self.get_pages() to create a new dictionary for each new page
            # key = urls and value = decoded html
            linked_second_pages = self.get_pages(page, base_url)
            

            
                
            for page_url, page in linked_second_pages.items():
                
                # adds each link to universal dictionary self.pages{}
                self.pages[page_url] = page
                
            
            
                
                
                

                

        print()

    def get_pages(self, page, baseurl):
        '''returns a dictionary for each page called linked_pages'''
        # initializes dict for each page, checks for uniqueness 
        linked_pages = {}
        # finds all links through self.get_linked_urls() and stores them in urls as a list
        urls = self.get_linked_urls(page, baseurl)

        #counter = 0 
        # goes through list and gets the decoded html w/ self.get_page_from_url()
        # also adds link to linked_pages{}
        for u in urls:
 
            #counter +=1 
            linked_page = self.get_page_from_url(u)
            linked_pages[u] = linked_page
        
        
                   
        return linked_pages

    def get_linked_urls(self, page, baseurl):
        '''returns a list, LList, that stores all links on each page (checks for uniqueness)'''
        
        # initializes list for page links
        LList = []
        counter = 0 
        # uses BeautifulSoup to find all links on a page
        
        if page != None:
            for link in page.find_all('a'):
                if counter > 20:
                    break
                counter += 1
                href = link.get('href')
                if href is None:
                    continue
                # adds the base url, to relative urls
                if href[:4] != 'http':
                    href = baseurl + '/' + href
                # checks for uniqueness and then adds to LList
                if href not in LList and href not in self.pages:
##                print('Not duplicate', href, self.pages.keys())
                    if href[len(href)-4 : len(href)] != '.jpg' and href[len(href)-4 : \
                                                                    len(href)] != '.mp3' and href[len(href)-4 : len(href)] != '.pdf':
                        LList.append(href)
            

        return LList

    def get_page_from_url(self, url):
        '''returns the decoded html for each page'''

        
        
        # uses requests library to get html content from url
        # creates Response object with requests library
        try:
            res = requests.get(url)
        
        except:
            return None
        # checks the encoding - only proceed if the encoding is utf-8
        if res.encoding == 'utf-8':
            # parses html
            # gets content of the Response object in bytes
            html_page = res.content
            # create BeautifulSoup object 
            page = BeautifulSoup(html_page, 'html.parser')

            # adds url and Beautiful Soup Object to self.pages{}
            self.pages[url] = page

            print('GETTING PAGE:', url)

            return page
        

    def analyze_text(self, query):
        '''For links that contain the given query, builds a dictionary of the
        top 15 most common words overall.'''
        
        # creates list of words not to consider when searching for the most common
        #  words due to lack of significance
        ignore_words = ['the', 'a', 'of', 'an', 'to', 'too', 'in', 'out', \
                        'off', 'can', 'is', 'am','are', 'there', 'from', 'be', \
                        'may', 'some','their', 'they', 'she', 'her', 'him', 'his',\
                        'hers','he', 'how', 'why', 'what', 'them', 'and', 'that', \
                        'dr', 'ms', 'mr', 'or', 'for','our', 'like', 'also', 'as',\
                        'this', 'with', 'miss', 'have', 'these', 'but', 'or', 'however', \
                        'on', 'those', 'more', 'than', 'at', 'has', 'by', 'it', 'your',\
                        'my', '@','said', 'not', 'could', 'would', 'i', 'we', 'you', 'was', \
                        'so', 'about', 'just', "it's", 'who', 'had', 'its']
        
        def get_title(page):
            '''Extracts title from the given page if the page has a title'''
            #if page isn't empty, gets title
            if page != None:
                
                result = page.select('title')
                if len(result) != 0:
                    return result[0].text
                if len(result) == 0:
                    return ''
                    
                
            # if the result is empty, returns empty string
            if page == None:
                return ''
            #print("TITLE", result[0].text)
            
        

        def match_title(page):
            '''checks if query is in the title of the given page (not case sensitive). Returns
            True if the title contains the query, otherwise returns False.'''
            
            # extracts title from page
            title = get_title(page)

            # checks if the lowercase query is in the lowercase title
            if query.lower() in title.lower():
                #print(query, "in:", title)
                return True
            else:
                #print("query not in title")
                return False
            
        def depunc(text):
            '''removes punctuation from the given text string. Returns modified
            text string.'''
            
            punc = ",.;:\'\\\"&%$-_`~[]{}<>?/‘’\“\”"
            for char in text:
                if char in punc:
                    text = text.replace(char, ' ')
            return text

        # initialize titlelist to handle duplicates
        titlelist = []
        # initialize dictionaries to store most common words
        total_dict = {}
        finaldict = {}
        
        # go through the pages in the self.pages dictionary and analyze the
        # text if the query is in the title
        for page_url, page in self.pages.items():
            #print("page_url:", page_url, "page", page)
            title = get_title(page)
            #print(title)
            
            # if page is None, continue looping through    
            if page is None:
                continue
            
            # If the query is in the title and the title is not a repeat, gathers text
                
            if match_title(page) and title not in titlelist:                
                titlelist.append(title)
                #print("TITLE LIST", titlelist)
                text = page.find_all(text = True)
                print("TITLE", title,"\n--------------------")
                # initialize output as empty string so text can be concatenated to it
                output = ''
                # create list of text parent names that do not include the text that
                # needs to be analyzed
                blacklist = [
                    '[document]',
                    'noscript',
                    'header',
                    'html',
                    'meta',
                    'head', 
                    'input',
                    'script',
                    'style'
                    ]

                #extracts only the text from the page
                for t in text:
                    if t.parent.name not in blacklist:
                        output += '{} '.format(t)
                        #print(output[:100])
                        
                # initialize an individual dictionary for each page analyzed
                minidict = {}
                # remove punctuation and convert to lowercase before splitting 
                newoutput = depunc(output)
                
##                print("OUTPUT", newoutput[:500])

                
                text_words = newoutput.lower().split()
            
                

                
                # go through list of text words and, if the word is not in
                # ignore_words and doesn't have length 1, add to the individual dictionary.
                #If the word is already in the dictionary, add one to its count. 
                for item in text_words:
                    if item in ignore_words or len(item) == 1:
                        continue
                    if item not in minidict:
                        minidict[item] = 1
                    else:
                        minidict[item] += 1

                # go through key value pairs in each individual dictionary and add them to
                # the total dictionary.
                
                counter = 0
                for key, value in sorted(minidict.items(), reverse=True, \
                                         key=lambda item: item[1]):
                    counter += 1
                    if counter >= 10:
                        break
                    if key not in total_dict:
                        total_dict[key] = value
                    else:
                        total_dict[key] += value
                        
        # add the top 15 most common words in the total dictionary to the final dictionary.
        counter2 = 0
        for key, value in sorted(total_dict.items(), reverse=True, \
                                         key=lambda item: item[1]):
            
            counter2 += 1
            if counter2 >= 50:
                break
            
            finaldict[key] = value
            
            
        #print("TOTAL DICT", total_dict)
        print("FINAL DICT", finaldict)
        
        if len(finaldict) == 0:
            print("No titles with matches were found.")
        
        return finaldict

def barGraph(top_wordsdict):
    '''Given a dictionary of words, creates a bar graph with the frequency of the words
    on the y axis and the identity of the words on the x axis'''

    # initialize lists of words and frequencies to be set on the axis
    words = []
    frequencies = []
    
    # add all the words and their frequencies into parallel lists
    for word,number in top_wordsdict.items():
        words.append(word)
        frequencies.append(number)
    y_pos = np.arange(len(words))

    # create bar graph to visualize the words and their frequencies
    plt.bar(y_pos, frequencies, align='center', alpha=.5)
    plt.xticks(y_pos, words, rotation = 45)
    plt.ylabel('Frequency')
    plt.xlabel('Words')
    plt.title('Top Word Frequencies')

    #adjusts the graph so that the lower portion is not cut off
    plt.subplots_adjust(left=0.1, bottom=0.3, right=0.9)
    
    #plots the graph
    plt.show()

class wordCloud:
    '''class for wordCloud object, containing method setWordFeatures and
    RandDarkColor'''
    
    #constructor for wordCloud class
    def __init__(self, win, top_wordsdict, WordList, FrequencyList):
        '''formal parameters are win, top_wordsdict, WordList, FrequencyList,
        constructs wordCloud object'''
        
        self.words = WordList
        self.frequencies = FrequencyList
        for word,number in top_wordsdict.items():
            self.words.append(word)
            self.frequencies.append(number)

    def setWordFeatures(self, win, WordList, FrequencyList):
        '''win, WordList, FrequencyList; 
        a method of wordCloud class that
        sets the position and text size for each word in the WordList
        according to its frequency, and sets a random (dark) color to
        each word'''
        
        for i in range(len(WordList)):
            
            CurrentWord = WordList[i]
            
            #if CurrentWord is the first one in WordList(i.e.if it is the most frenquent word)
            if i == 0:
                #then makes its position at the center of the window
                word = Text(Point(0, 0), CurrentWord)
                #and sets its size to the largest possible
                word.setSize(36)
            else:
                #initialize x and y to make sure go into while loop
                x = 0
                y = 0
                if FrequencyList[i] >= int(0.9*FrequencyList[0]):
                    while -18<=x<=18 and -10<=y<=10:
                        x = randint(-25, 25)
                        y = randint(-20, 20)
                    position = Point(x, y)
                    word = Text(position, CurrentWord)
                    word.setSize(33)
                elif int(0.8*FrequencyList[0]) <= FrequencyList[i] < int(0.9*FrequencyList[0]):
                    while -25<=x<=25 and -20<=y<=20:
                        x = randint(-40, 40)
                        y = randint(-30, 30)
                    position = Point(x, y)
                    word = Text(position, CurrentWord)
                    word.setSize(30)
                elif int(0.7*FrequencyList[0]) <= FrequencyList[i] < int(0.8*FrequencyList[0]):
                    while -40<=x<=40 and -30<=y<=30:
                        x = randint(-54, 54)
                        y = randint(-40, 40)
                    position = Point(x, y)
                    word = Text(position, CurrentWord)
                    word.setSize(27)
                elif int(0.6*FrequencyList[0]) <= FrequencyList[i] < int(0.7*FrequencyList[0]):
                    while -54<=x<=54 and -40<=y<=40:
                        x = randint(-66, 66)
                        y = randint(-50, 50)
                    position = Point(x, y)
                    word = Text(position, CurrentWord)
                    word.setSize(24)
                elif int(0.5*FrequencyList[0]) <= FrequencyList[i] < int(0.6*FrequencyList[0]):
                    while -66<=x<=66 and -50<=y<=50:
                        x = randint(-77, 77)
                        y = randint(-60, 60)
                    position = Point(x, y)
                    word = Text(position, CurrentWord)
                    word.setSize(21)
                elif int(0.4*FrequencyList[0]) <= FrequencyList[i] < int(0.5*FrequencyList[0]):
                    while -77<=x<=77 and -60<=y<=60:
                        x = randint(-86, 86)
                        y = randint(-80, 80)
                    position = Point(x, y)
                    word = Text(position, CurrentWord)
                    word.setSize(18)
                elif int(0.3*FrequencyList[0]) <= FrequencyList[i] < int(0.4*FrequencyList[0]):
                    while -80<=x<=80 and -70<=y<=70:
                        x = randint(-88, 88)
                        y = randint(-80, 80)
                    position = Point(x, y)
                    word = Text(position, CurrentWord)
                    word.setSize(15)
                elif int(0.2*FrequencyList[0]) <= FrequencyList[i] < int(0.3*FrequencyList[0]):
                    while -82<=x<=82 and -80<=y<=80:
                        x = randint(-90, 90)
                        y = randint(-80, 80)
                    position = Point(x, y)
                    word = Text(position, CurrentWord)
                    word.setSize(12)
                else:
                    while -84<=x<=84 and -90<=y<=90:
                        x = randint(-95, 95)
                        y = randint(-95, 95)
                    position = Point(x, y)
                    word = Text(position, CurrentWord)
                    word.setSize(9)
            word.setTextColor(self.RandDarkColor())
            word.draw(win)

    def RandDarkColor(self):
        '''Generate a random dark color and return it'''
        #words are in darker colors so that they are easily seen with a contrast to the light-colored background
        r = randint( 0, 200 )
        g = randint( 0, 180 )
        b = randint( 0, 200 )
        color = color_rgb( r, g, b )
        return color 

def main():
    '''Test web crawling and webpage analysis code'''
    
    # construct mypages object
    baseurl = input('Paste base url: ')
    mypages = MyPages(baseurl)

    # prompt user for desired query
    query = input("Search articles with titles containing: ")

    # hold the dictionary of highest frenquency words in variable top_words
    top_words = mypages.analyze_text(query)
    
    # construct the graphics window by calling functions in graphics.py
    if len(top_words) != 0:
        win = GraphWin('WordCloud', 500, 500)
        win.setBackground('light blue')
        w = 100
        win.setCoords(-w, -w, w, w)
    # initialize WordList and FrequencyList to be two empty lists
        WordList = []
        FrequencyList = []
    
    #call the class wordCloud and its method, and draw the words onto graphics window
        WC=wordCloud(win, top_words, WordList, FrequencyList)
        WC.setWordFeatures(win, WordList, FrequencyList)
    
        barGraph(top_words)

    

main()
    

