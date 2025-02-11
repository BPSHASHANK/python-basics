# create a youtube project like user can add time and video update delete like crud operation
import json
def load_data():
    try:
        with open('youtube.txt','w') as file:
            json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(videos):
        with open('youtube.txt','w') as file:
         json.dump(file)       
def list_all_videos(videos):
       for index,videos in    enumerate(videos,start=1):  
           print(f'{index}')
       
       
def add_video(videos):
    name=input("enter the video name:")
    time=input("enter the video time:")
    videos.append()

def update_video(videos):
    pass

def  delete_video(videos):
    pass
def main():

 videos=load_data
while(True):
                print("youtube Manageer || choose your option :\n")
                print("1.list all the youtube videos:")
                print("2.Add  a video to the list :" )
                print("3.Update to the list")
                print("4.Delete to the list")
                print("5.exit")
                choice=int(input("enter yor choice\n"))
                match choice:
                    case '1':
                        list_all_videos(videos) 
                    case '2':
                            add_video(videos)
                    case '3':
                        update_video(videos)
                    case '4':
                        delete_video(videos)
                    case '5':
                        break
                    # if we press other then 1 /5 t shuld show invalid or some thing
                    case _:
                        print("invalid")
if __name__=="__main__":
    main()
    
            
                    
            
    