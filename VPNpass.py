#Testing out Beautiful Soup 4.
#Building a test module for VPN Script

def GetFreeVPNPass ():
    #import modules
    import os
    import wget
    from bs4 import BeautifulSoup
    
    #Assign Variables
    url = "https://freevpn.me/accounts/"
    filename = wget.download(url, 'freevpn.html')
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

