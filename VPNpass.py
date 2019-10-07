#Testing out Beautiful Soup 4.
#Building a test module for VPN Script

def GetFreeVPNPass ( FreeVPNdomain ):
    #import modules
    import os
    import GetHTML
    from bs4 import BeautifulSoup
    
    #Assign Variables
    d = str(FreeVPNdomain)
    urlcat = "https://freevpn." + d + "/accounts/"
    url = GetHTML.GetSource(urlcat)
    
    #Write files for temp data storage.
    source = open('freevpn.html', 'w')
    source.write(str(url))
    source.close()
    f = open('creds.txt', 'w')

    #Parse the downloaded html source code
    with open("freevpn.html") as fp:
        soup = BeautifulSoup(fp, "lxml")
    
    #Search parsed code for the login credentials
    for tag in soup.find_all('b'):
        f.write(str(tag.text) + "\n") 
        f.write(str(tag.next_sibling) + "\n")

    #Delete html source code
    os.remove('freevpn.html')
    f.close()

    #Pass Credential info into list and extract password field.
    CredList = open('creds.txt', 'r').readlines()
    VPN_Pass = CredList[5]
    
    #Clean up credential list file
    os.remove('creds.txt')
   
    #return password.
    return str(VPN_Pass.strip())

if __name__ == '__main__':
    inputdomain = str(input("enter domain: "))
    testpass = GetFreeVPNPass(inputdomain)
    print(testpass)
