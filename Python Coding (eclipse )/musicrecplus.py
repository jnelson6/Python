'''
Created on Apr 9, 2018

@author: Julia Nelson and Amy Renne

'I pledge my honor that I have abided by the Stevens Honor System.' 
jnelson6 arenne
'''
PREF_FILE = "musicrecplus.txt"


def menu(username, usermap):
    '''Main menu displaying choices of options to run in the program'''
    Prefs = []
    while True:
        print('Enter a letter to choose an option: \n e - Enter preferences \n r - Get recommendations \n p - Show most popular artists \n h - How popular is the most popular \n m - Which user has the most likes \n q - Save and quit')
        choice = input()
        if choice == 'e':
            Prefs = getPreferences(username, usermap)
            usermap[username] = Prefs
            savePreferences(usermap, PREF_FILE)
        elif choice == 'r':
            recs = getRecommendations(username, usermap)
            if not recs:
                print('No recommendations available at this time')
            else:
                for x in recs:
                    print(x)
        elif choice == 'p':
            bestArtists(usermap)
        elif choice == 'h':
            howPopular(usermap)
        elif choice == 'm':
            bestUser(usermap)
        elif choice == 'q':
            savePreferences(usermap, PREF_FILE)
            return
        
  
def loadUsers(filename):
    '''Looks in file and reads all users and preferences. Returns dictionary
    of users w/ preferences'''
    try:
        file = open(filename, 'r')
        userDict = {}
        for line in file:
            username, Artists = line.strip().split(':')
            ArtistList = Artists.split(',')
            ArtistList.sort()
            userDict[username] = ArtistList
        file.close()
        return userDict
    except:
        return {}


def savePreferences(usermap, filename):
    '''Saves the preferences entered to the text file'''
    file = open(filename, 'w')
    for user in usermap:
        save = str(user) + ':' + ','.join(usermap[user]) + '\n'
        file.write(save)
    file.close()
    
      
def getPreferences(username, usermap):
    '''Gets preferences from users one at a time'''
    newPrefs = ''
    if username in usermap:
        Prefs = []
        for Artist in Prefs:
            print(Artist)
    else:
        Prefs = []
    print('Enter an artist that you like (Enter to finish): ')
    newPrefs = input()
    while newPrefs != '':
        Prefs.append(newPrefs.strip().title())
        print('Enter an artist that you like (Enter to finish): ')
        newPrefs = input()
    Prefs.sort()
    return Prefs

  
def nummatches(list1, list2):
    '''Compares the list of artists with another looking for similarities in order to
    recommend'''
    matches = 0
    for item in list1:
        if item in list2:
            matches += 1     
    return matches

    
def mostSimilar(username, usermap):
    '''Find the most similar other user'''
    targetList = usermap[username]
    mostsimilar = []
    bestScore = 1
    for user in usermap:
        if targetList == usermap[user] or user == username or user[-1] == '$':
            continue                                            
        score = nummatches(targetList, usermap[user])
        if score > bestScore:
            bestScore = score
            mostsimilar = [user]
        elif score == bestScore:
            mostsimilar.append(user)
            
    return mostsimilar

    
def getRecommendations(currentuser, usermap):
    '''Compares current user preferences with other user preferences to find the 
    best recommendations'''
    currentUserArtists = usermap[currentuser]
    bestusers = mostSimilar(currentuser, usermap)
    recommendations = []
    for x in bestusers:
        for artist in usermap[x]:
            if artist not in recommendations and artist not in currentUserArtists: 
                recommendations.append(artist)                                             
    return recommendations


def bestArtists(usermap):
    '''Finds the artist liked most by the users. If there is a tie, print both '''
    likes = {}
    mostpopular = []
    maximum = 0                             
    for user in usermap:                   
        if user[-1] == '$':                 
            continue                        
        for artist in usermap[user]:        
            if artist in likes:
                likes[artist] += 1
            else:
                likes[artist] = 1
    maximum = max(likes.values())  
    for artist in likes:
        if likes[artist] == maximum:
            mostpopular += [artist]
    if len(mostpopular) == 1:
        print(mostpopular[0])
    elif len(mostpopular) == 0:
        print('Sorry no artists found')
    else:
        mostpopular.sort()
        for pop in mostpopular[:-1]:
            print(pop)
        print(mostpopular[-1]) 


def howPopular(usermap):
    '''prints how many likes the most popular artist received '''
    likes = {}
    maximum = 0
    for user in usermap:
        if user[-1] == '$': 
            continue
        for artist in usermap[user]:
            if artist in likes:
                likes[artist] += 1
            else:
                likes[artist] = 1
    maximum = max(likes.values())       
    if not maximum:                    
        print('Sorry, no artists found')
    else:
        print(maximum)


def bestUser(usermap):
    '''find the user with most likes'''
    mostpopular = []
    maximum = 0
    for user, likes in usermap.items():     
        if user[-1] == '$':
            continue
        if len(likes) > maximum:
            maximum = len(likes)
            mostpopular = [user]
        elif len(likes) == maximum:
            mostpopular.append(user)
    if maximum == 0:                        
        print('Sorry, no user found')
    else:
        mostpopular.sort()
        for user in mostpopular:
            print(user)
            
       
def main():
    usermap = loadUsers(PREF_FILE)
    username = input('Enter your name (put a $ symbol after your name if \n you wish your preferences to remain private): ')
    if username not in usermap:
        preferences = getPreferences(username, usermap)
        usermap[username] = preferences
        savePreferences(usermap, PREF_FILE)
    menu(username, usermap)
    

if __name__ == '__main__':
    main()
