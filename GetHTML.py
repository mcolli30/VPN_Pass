"""
Code to pull html source using requests
Import GetHTML
Then call 
"""

def GetSource( site ):
    import requests
    source = site
    webpage = requests.get(source)
    htmlsource = webpage.text
    
    return htmlsource

if __name__ == '__main__':

    testurl = print(input("Enter URL"))

    testsource = GetSource(testurl)
    
    print(testsource)