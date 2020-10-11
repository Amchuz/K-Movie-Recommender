from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP 

def findl(letter):
    if(letter=='A' or letter=='a'):
        a()
    elif(letter=='B' or letter=='b'):
        b()
    elif(letter=='C' or letter=='c'):
        c()
    elif(letter=='D' or letter=='d'):
        d()
    elif(letter=='E' or letter=='e'):
        (e)
    elif(letter=='F' or letter=='f'):
        f()
    elif(letter=='G' or letter=='g'):
        g()
    elif(letter=='H' or letter=='h'):
        a()
    elif(letter=='I' or letter=='i'):
        b()
    elif(letter=='J' or letter=='j'):
        c()
    elif(letter=='K' or letter=='k'):
        d()
    elif(letter=='L' or letter=='l'):
        e()
    elif(letter=='M' or letter=='m'):
        f()
    elif(letter=='N' or letter=='n'):
        g()
    elif(letter=='O' or letter=='o'):
        a()
    elif(letter=='P' or letter=='p'):
        b()
    elif(letter=='Q' or letter=='q'):
        c()
    elif(letter=='R' or letter=='r'):
        d()
    elif(letter=='S' or letter=='s'):
        e()
    elif(letter=='T' or letter=='t'):
        f()
    elif(letter=='U' or letter=='u'):
        g()
    elif(letter=='V' or letter=='v'):
        a()
    elif(letter=='W' or letter=='w'):
        b()
    elif(letter=='X' or letter=='x'):
        c()
    elif(letter=='Y' or letter=='y'):
        d()
    elif(letter=='Z' or letter=='z'):
        e()
    else:
        f()
def a():
    count=0
    print("Which genre do you want ?")
    print("1. Action")
    print("2. Animation")
    print("3. Classical")
    print("4. Comedy")
    print("5. Drama")
    print("6. Fantasy")
    print("7. Historical")
    print("8. Horror")
    print("9. Mystery")
    print("10. Thriller")
    choice=int(input("Enter the number of the genre : "))

    if(choice==1):
        search='https://www.imdb.com/list/ls050944897/?sort=moviemeter,asc&st_dt=&mode=detail'
    elif(choice==2):
        search='https://www.imdb.com/list/ls054358736/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'
    elif(choice==3):
        search='https://www.imdb.com/list/ls063673765/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'
    elif(choice==4):
        search='https://www.imdb.com/list/ls057434105/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'
    elif(choice==5):
        search='https://www.imdb.com/list/ls050926710/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'
    elif(choice==6):
        search='https://www.imdb.com/list/ls068186726/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'
    elif(choice==7):
        search='https://www.imdb.com/list/ls055160226/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'
    elif(choice==8):
        search='https://www.imdb.com/list/ls027399642/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'
    elif(choice==9):
        search='https://www.imdb.com/list/ls045127779/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'
    elif(choice==10):
        search='https://www.imdb.com/list/ls071918022/?sort=moviemeter,asc&st_dt=&mode=detail&page=1'
    else:
        print("Wrong number")
    response = HTTP.get(search) 
    data = response.text 

    soup = SOUP(data, "lxml") 
  
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    for i in title: 
  
            temp = str(i).split('>') 
  
            if(len(temp) == 3): 
                print(temp[1][:-3]) 

            if(count > 13): 
                break
            count += 1

def b():
    count=0
    print("Which genre do you want ?")
    print("1. Action")
    print("2. Animation")
    print("3. Classical")
    print("4. Comedy")
    print("5. Drama")
    print("6. Fantasy")
    print("7. Historical")
    print("8. Horror")
    print("9. Live-Action")
    print("10. Mystery")
    print("11. Thriller")
    choice=int(input("Enter the number of the genre : "))

    if(choice==1):
        search='https://www.imdb.com/list/ls050944897/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    elif(choice==2):
        search='https://www.imdb.com/list/ls054358736/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    elif(choice==3):
        search='https://www.imdb.com/list/ls063673765/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    elif(choice==4):
        search='https://www.imdb.com/list/ls057434105/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    elif(choice==5):
        search='https://www.imdb.com/list/ls050926710/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    elif(choice==6):
        search='https://www.imdb.com/list/ls068186726/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    elif(choice==7):
        search='https://www.imdb.com/list/ls055160226/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    elif(choice==8):
        search='https://www.imdb.com/list/ls027399642/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    elif(choice==9):
        search='https://www.imdb.com/list/ls045127779/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    elif(choice==10):
        search='https://www.imdb.com/list/ls071918022/?sort=alpha,asc&st_dt=&mode=detail&page=1'
    else:
        print("Wrong number")
    response = HTTP.get(search) 
    data = response.text 

    soup = SOUP(data, "lxml") 
  
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    for i in title: 
  
            temp = str(i).split('>') 
  
            if(len(temp) == 3): 
                print(temp[1][:-3]) 

            if(count > 13): 
                break
            count += 1
    
def c():
    count=0
    print("Which genre do you want ?")
    print("1. Action")
    print("2. Animation")
    print("3. Classical")
    print("4. Comedy")
    print("5. Drama")
    print("6. Fantasy")
    print("7. Historical")
    print("8. Horror")
    print("9. Live-Action")
    print("10. Mystery")
    print("11. Thriller")
    choice=int(input("Enter the number of the genre : "))

    if(choice==1):
        search='https://www.imdb.com/list/ls050944897/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    elif(choice==2):
        search='https://www.imdb.com/list/ls054358736/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    elif(choice==3):
        search='https://www.imdb.com/list/ls063673765/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    elif(choice==4):
        search='https://www.imdb.com/list/ls057434105/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    elif(choice==5):
        search='https://www.imdb.com/list/ls050926710/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    elif(choice==6):
        search='https://www.imdb.com/list/ls068186726/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    elif(choice==7):
        search='https://www.imdb.com/list/ls055160226/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    elif(choice==8):
        search='https://www.imdb.com/list/ls027399642/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    elif(choice==9):
        search='https://www.imdb.com/list/ls045127779/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    elif(choice==10):
        search='https://www.imdb.com/list/ls071918022/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
    else:
        print("Wrong number")
    response = HTTP.get(search) 
    data = response.text 

    soup = SOUP(data, "lxml") 
  
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    for i in title: 
  
            temp = str(i).split('>') 
  
            if(len(temp) == 3): 
                print(temp[1][:-3]) 

            if(count > 13): 
                break
            count += 1
    
def d():
    count=0
    print("Which genre do you want ?")
    print("1. Action")
    print("2. Animation")
    print("3. Classical")
    print("4. Comedy")
    print("5. Drama")
    print("6. Fantasy")
    print("7. Historical")
    print("8. Horror")
    print("9. Live-Action")
    print("10. Mystery")
    print("11. Thriller")
    choice=int(input("Enter the number of the genre : "))

    if(choice==1):
        search='https://www.imdb.com/list/ls050944897/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    elif(choice==2):
        search='https://www.imdb.com/list/ls054358736/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    elif(choice==3):
        search='https://www.imdb.com/list/ls063673765/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    elif(choice==4):
        search='https://www.imdb.com/list/ls057434105/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    elif(choice==5):
        search='https://www.imdb.com/list/ls050926710/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    elif(choice==6):
        search='https://www.imdb.com/list/ls068186726/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    elif(choice==7):
        search='https://www.imdb.com/list/ls055160226/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    elif(choice==8):
        search='https://www.imdb.com/list/ls027399642/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    elif(choice==9):
        search='https://www.imdb.com/list/ls045127779/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    elif(choice==10):
        search='https://www.imdb.com/list/ls071918022/?sort=num_votes,desc&st_dt=&mode=detail&page=1'
    else:
        print("Wrong number")
    response = HTTP.get(search) 
    data = response.text 

    soup = SOUP(data, "lxml") 
  
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    for i in title: 
  
            temp = str(i).split('>') 
  
            if(len(temp) == 3): 
                print(temp[1][:-3]) 

            if(count > 13): 
                break
            count += 1

def e():
    count=0
    print("Which genre do you want ?")
    print("1. Action")
    print("2. Animation")
    print("3. Classical")
    print("4. Comedy")
    print("5. Drama")
    print("6. Fantasy")
    print("7. Historical")
    print("8. Horror")
    print("9. Live-Action")
    print("10. Mystery")
    print("11. Thriller")
    choice=int(input("Enter the number of the genre : "))

    if(choice==1):
        search='https://www.imdb.com/list/ls050944897/?sort=release_date,desc&st_dt=&mode=detail&page=1'
    elif(choice==2):
        search='https://www.imdb.com/list/ls054358736/?sort=release_date,desc&st_dt=&mode=detail&page=1'
    elif(choice==3):
        search='https://www.imdb.com/list/ls063673765/?sort=release_date,desc&st_dt=&mode=detail&page=1'
    elif(choice==4):
        search='https://www.imdb.com/list/ls057434105/?sort=release_date,desc&st_dt=&mode=detail&page=1'
    elif(choice==5):
        search='https://www.imdb.com/list/ls050926710/?sort=release_date,desc&st_dt=&mode=detail&page=1'
    elif(choice==6):
        search='https://www.imdb.com/list/ls068186726/?sort=release_date,desc&st_dt=&mode=detail&page=1'
    elif(choice==7):
        search='https://www.imdb.com/list/ls055160226/?sort=release_date,desc&st_dt=&mode=detail&page=1'
    elif(choice==8):
        search='https://www.imdb.com/list/ls027399642/?sort=release_date,desc&st_dt=&mode=detail&page=1'
    elif(choice==9):
        search='https://www.imdb.com/list/ls045127779/?sort=release_date,desc&st_dt=&mode=detail&page=1'
    elif(choice==10):
        search='https://www.imdb.com/list/ls071918022/?st_dt=&mode=detail&page=1&sort=release_date,desc'
    else:
        print("Wrong number")
    response = HTTP.get(search) 
    data = response.text 

    soup = SOUP(data, "lxml") 
  
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    for i in title: 
  
            temp = str(i).split('>') 
  
            if(len(temp) == 3): 
                print(temp[1][:-3]) 

            if(count > 13): 
                break
            count += 1
    
def f():
    count=0
    print("Which genre do you want ?")
    print("1. Action")
    print("2. Animation")
    print("3. Classical")
    print("4. Comedy")
    print("5. Drama")
    print("6. Fantasy")
    print("7. Historical")
    print("8. Horror")
    print("9. Live-Action")
    print("10. Mystery")
    print("11. Thriller")
    choice=int(input("Enter the number of the genre : "))

    if(choice==1):
        search='https://www.imdb.com/list/ls050944897/?sort=runtime,desc&st_dt=&mode=detail&page=1'
    elif(choice==2):
        search='https://www.imdb.com/list/ls054358736/?sort=runtime,desc&st_dt=&mode=detail&page=1'
    elif(choice==3):
        search='https://www.imdb.com/list/ls063673765/?sort=runtime,desc&st_dt=&mode=detail&page=1'
    elif(choice==4):
        search='https://www.imdb.com/list/ls057434105/?sort=runtime,desc&st_dt=&mode=detail&page=1'
    elif(choice==5):
        search='https://www.imdb.com/list/ls050926710/?sort=runtime,desc&st_dt=&mode=detail&page=1'
    elif(choice==6):
        search='https://www.imdb.com/list/ls068186726/?sort=runtime,desc&st_dt=&mode=detail&page=1'
    elif(choice==7):
        search='https://www.imdb.com/list/ls055160226/?sort=runtime,desc&st_dt=&mode=detail&page=1'
    elif(choice==8):
        search='https://www.imdb.com/list/ls027399642/?sort=runtime,desc&st_dt=&mode=detail&page=1'
    elif(choice==9):
        search='https://www.imdb.com/list/ls045127779/?sort=runtime,desc&st_dt=&mode=detail&page=1'
    elif(choice==10):
        search='https://www.imdb.com/list/ls071918022/?st_dt=&mode=detail&page=1&sort=runtime,desc'
    else:
        print("Wrong number")
    response = HTTP.get(search) 
    data = response.text 

    soup = SOUP(data, "lxml") 
  
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    for i in title: 
  
            temp = str(i).split('>') 
  
            if(len(temp) == 3): 
                print(temp[1][:-3]) 

            if(count > 13): 
                break
            count += 1

def g():
    count=0
    print("Which genre do you want ?")
    print("1. Action")
    print("2. Animation")
    print("3. Classical")
    print("4. Comedy")
    print("5. Drama")
    print("6. Fantasy")
    print("7. Historical")
    print("8. Horror")
    print("9. Live-Action")
    print("10. Mystery")
    print("11. Thriller")
    choice=int(input("Enter the number of the genre : "))

    if(choice==1):
        search='https://www.imdb.com/list/ls050944897/?sort=date_added,desc&st_dt=&mode=detail&page=1'
    elif(choice==2):
        search='https://www.imdb.com/search/title/?genres=animation&countries=KR&sort=release_date,asc'
    elif(choice==3):
        search='https://www.imdb.com/list/ls063673765/?sort=date_added,desc&st_dt=&mode=detail&page=1'
    elif(choice==4):
        search='https://www.imdb.com/list/ls057434105/?sort=date_added,desc&st_dt=&mode=detail&page=1'
    elif(choice==5):
        search='https://www.imdb.com/list/ls050926710/?sort=date_added,desc&st_dt=&mode=detail&page=1'
    elif(choice==6):
        search='https://www.imdb.com/list/ls068186726/?sort=date_added,desc&st_dt=&mode=detail&page=1'
    elif(choice==7):
        search='https://www.imdb.com/list/ls055160226/?sort=date_added,desc&st_dt=&mode=detail&page=1'
    elif(choice==8):
        search='https://www.imdb.com/list/ls027399642/?sort=date_added,desc&st_dt=&mode=detail&page=1'
    elif(choice==9):
        search='https://www.imdb.com/list/ls045127779/?sort=date_added,desc&st_dt=&mode=detail&page=1'
    elif(choice==10):
        search='https://www.imdb.com/list/ls071918022/?st_dt=&mode=detail&page=1&sort=date_added,desc'
    else:
        print("Wrong number")
    response = HTTP.get(search) 
    data = response.text 

    soup = SOUP(data, "lxml") 
  
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    for i in title: 
  
            temp = str(i).split('>') 
  
            if(len(temp) == 3): 
                if('See full summary' in temp[1]):
                    break
                else:
                    print(temp[1][:-3]) 

            if(count > 13): 
                break
            count += 1



if __name__ == '__main__': 

    print("Hello there")
    print("Type something randomly, it doesn't have to be a word")
    r=input("Type here : ")
    l=list(r)
    letter=l[-1]
    findl(letter)