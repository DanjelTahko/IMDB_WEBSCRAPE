from imdb import IMDB

def run():

    imdb = IMDB()
    
    while(True):

        cin = str(input("> "))
        if cin == 'q':
            break
        elif cin == 'filter':
            print(imdb.filter)
        elif cin == 'b':
            imdb.filter = ['actor', 'actress']
            print("Changed to basic filter")
        else:
            try:
                imdb.scrape_person(cin)
            except:
                print('no url found')


if __name__ == "__main__":
    run()