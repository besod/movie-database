import json

import sys

class MovieDatabase:
    def __init__(self,language,top_rated):
        # 2
            self.languages = ['ko', 'it', 'cs', 'bn', 'km', 'he', 'tr', 'hi', 'uk', 'fr', 'th', 'bs', 'ru', 'nl', 'id', 'sv', 'zh', 'sh', 'ja',
                          'et', 'ar', 'ml', 'da', 'cn', 'te', 'ro', 'eu', 'es', 'en', 'pl', 'de', 'hu', 'el', 'pt', 'no', 'is', 'fa', 'sr', 'nb', 'fi', 'la', 'af']
            
            self.language = language
            self.top_rated=top_rated
            self.movies=[]
            self.load_movies()
            
    def load_movies(self):
        # 1
        with open('movies.json','r') as f: 
           data =  json.load(f)
        for d in data:
            self.movies.append(d)

    def search_movie(self, title):
        # 4
        #Search movies for the length of nested dictionaries
        #and return title when user prompts.
        for i in range(0, len(self.movies)):
            try:
                movie_title = self.movies[i].get('title').lower()
                if title == movie_title or title in movie_title:
                    matching_movie = self.movies[i]
                    return matching_movie
            except:
                raise KeyError
    
    def top_rated_movies(self,number_of_movies_to_list):
        # 6   
        #Store only 'title' and 'vote_average' in a dictionary unsorted. 
        self.movie_list={}       
        for item in self.movies:
            title=item['title']
            vote_average=item['vote_average']
            self.movie_list[title]=vote_average
        
        #Sorted method returns in tuples.
        # Convert sorted movie list into a dictionary using dict afterwards.        
        sorted_movie_list = sorted(self.movie_list.items(), key=lambda x:x[1],reverse=True)
        converted_top_list=dict(sorted_movie_list)
        top_rated =dict(list(converted_top_list.items())) 
        
        #Limiting the number of top rated movies to Max 50(the first 50 in 'top_rated' dictionary)
        #and store them in a dictionary
        top={}
        for idx,(key,value) in enumerate(top_rated.items()):
            if number_of_movies_to_list > 50 or number_of_movies_to_list < 1:
                raise ValueError
            if number_of_movies_to_list == idx:
                    break
            top[key]=value               
        return top
      
    def list_movies_based_on_language(self,language):
        # 8
        #Store entire dictionaries of movies chosen based on language.
        language_list=[]
        for items in self.movies:                
            if language in items['original_language'] and language in self.languages:
                language_list.append(items)
                continue
            if language not in items['original_language'] and language not in self.languages:
                raise ValueError
        return language_list                  
       
    def compare_movie_ratings(self,first_movie,second_movie):
        # 10       
        for i in range(0, len(self.movies)):
            #Find first move 'title' and 'vote_average' 
            movie_title = self.movies[i].get('title').lower()            
            if first_movie == movie_title:
                matching_movie_1 = self.movies[i]                
                vote_average_first_movie= matching_movie_1.get('vote_average')                
                                                     
                #Find second movie 'title' and 'vote_average'
                for i in range(0, len(self.movies)):                                 
                    movie_title = self.movies[i].get('title').lower()                   
                    if second_movie in movie_title:
                        matching_movie_2 = self.movies[i]
                        vote_average_second_movie=matching_movie_2.get('vote_average')                     
                        if second_movie not in movie_title:
                            raise KeyError
                        #Compare movies based on 'vote_avarage'    
                        if  vote_average_first_movie > vote_average_second_movie   :
                            return True
                        elif vote_average_first_movie == vote_average_second_movie:
                            raise KeyError                                                                             
                        else:
                            return False                   

    def list_latest_movies(self):
        # 12
        """
        __NOT__ REQUIRED FOR G (Godkänt)
        **ONLY START WITH THIS METHOD WHEN YOU HAVE COMPLETED ALL OTHER**
        - VG (Väl godkänt) REQUIREMENT ONLY

        This method should return a list of the latest movies ordered by release_date
        Use the datetime class
        """

        # Remove pass when you've added code
        pass

class Menu:    
    def __init__(self):
        
        self.movie_db_en=MovieDatabase(language="en",top_rated=50)       
        self.start_main_menu()      
        
    def start_main_menu(self):
        # 3        
        while True:    
            print('\nWhat would you like to do?\n')
            print('[1] - Movie summary')
            print('[2] - Compare movies')
            print('[3] - List top rated movies')
            print('[4] - Export movies from a language of choice')
            print('[5] - (VG) List latest movies')
            print('[6] - (VG) Export image from a movie')
            print('[q] - Quit (no dedicated method required)')       
        
            user=input('Enter your choice:  ').lower()
            if user == 'q':
                    sys.exit()                
            elif user == '1':
                self.movie_summary()
                continue            
            elif user == '2':
                self.compare_ratings()
                continue                       
            elif user == '3':
                self.list_top_movies()
                continue           
            elif user == '4':
                self.export_movies()
                continue                
            else:
                print(f'\nSomething went wrong...Try again!')
                continue

    def movie_summary(self):
        # 5
        while True:
            #Prompt user to enter movie title
            title = input('Enter title of a movie: ').lower()
            if title == 'b':
                break
            try:
                matching_movie = self.movie_db_en.search_movie(title)
                movie_title = matching_movie.get('title')
                genre_ids = matching_movie.get('genre_ids')
                release_date = matching_movie.get('release_date')
                original_language = matching_movie.get('original_language')
                overview = matching_movie.get('overview')
                vote_average=matching_movie.get('vote_average')
                vote_count=matching_movie.get('vote_count')
                popularity=matching_movie.get('popularity')
                id=matching_movie.get('id')
                adult=matching_movie.get('adult')
                print(f'\nTitle:{movie_title}\nRelease date: {release_date}\nGenre ids: {genre_ids}\nID: {id}')
                print(f'Vote_average: {vote_average}\nVote_count: {vote_count}\nPopularity: {popularity}\nAdult: {adult}')
                print(f'Language: {original_language}\nOverview: {overview}')
            except:
                print('\nUnable to find movie!')
                print("Try again or press 'b' to go back to main menu")
            else:
                break
    def list_top_movies(self):
        # 7
        while True:
            try:
                #Prompt user to input valid figure. Raises valueError if input is incorrect
                number_of_movies_to_list=int(input('\nHow many movies do you want to display(Max 50): '))
                
                top=self.movie_db_en.top_rated_movies(number_of_movies_to_list)
                print(f'\nIndex   Rating   Movie title')
                print(f'-----   ------   -----------')
                for idx,(key,value) in enumerate(top.items()):
                    print(f'{[idx]}      {value}     {key}')
                print("-" * 45)
            except ValueError:
                print('Type Error...Enter correct figure.')
                continue
            else:
                break    
        
    def export_movies(self):
        # 9
        while True:
            try:
                print(f'\n{self.movie_db_en.languages}')
                #Prompt user to enter language of choice.
                language=input('\nChoose a language to export:  ')
                matching_language=self.movie_db_en.list_movies_based_on_language(language.lower())
                
            except ValueError:    
                print('\nSomething went wrong. Try again!')      
                             
            else:                
                with open('movie_export.json','w') as f:
                    json.dump(matching_language,f)
                print(f'\nMovie of your language choice \'{language}\' exported as json data')                
                break        

    def compare_ratings(self):
        # 11        
        while True:          
            try:
                #Prompt user to enter movie titles.                                
                first_movie = input('\nEnter title of first movie: ').lower()                
                second_movie= input('Enter title of second movie: ').lower()                     
                movie_rate=self.movie_db_en.compare_movie_ratings(first_movie,second_movie)
                print(movie_rate)          
            except KeyError:
                print('Type correct title of movie and try again!')
                
            else:
                break

    def export_poster_image(self):
        # 13 - Last one (VG)
        """
        - THIS METHOD IS NOT REQUIRED FOR G (Godkänt)
        **ONLY START WITH THIS METHOD WHEN YOU HAVE COMPLETED ALL OTHER**

        - VG (Väl godkänt) REQUIREMENT ONLY

        You should use the "poster_path" string to access the poster image of the movie

        1. Ask the user for a movie that they want to export the image for.
        2. Download the image with requests.
        3. Using the package "pillow" (https://pillow.readthedocs.io/en/stable/index.html) 
        you need to resize the image to 300x200 pixels
        4. Save the image locally
        5. You should create a requirements.txt with pillow as a dependency to the project

        Use this base URL to request an image: https://image.tmdb.org/t/p/w300/
        A full url might look like this with the poster_path added to the end: https://image.tmdb.org/t/p/w300/kqcbwRrUmkcUe6TcFWHMnobVDon.jpg
        """

        # Remove pass when you've added code
        pass


if __name__ == "__main__":
    menu = Menu()
