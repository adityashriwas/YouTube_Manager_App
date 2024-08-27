from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("mongodb+srv://youtubepy:youtubepy@youtubepy.1xkcp97.mongodb.net/",
                     tlsAllowInvalidCertificates = True)
# not a good idea to include id and passwords in code files

db = client["ytmanager"]

video_collections = db["videos"]

# print(video_collections)


def list_all_videos():
    for video in video_collections.find():
        print(f"ID:{video['_id']} | Name: {video['name']} | Time: {video['time']}")

def add_video(name, time):
    video_collections.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    video_collections.update_one(
        {'_id': ObjectId(video_id)},
        {'$set': {'name': name, 'time': time}}
        )

def delete_video(video_id):
    video_collections.delete_one({'_id': ObjectId(video_id)})


def main():
    while True:
        print("\n YouTube Manager App | Choose an option ")
        print("1. List all YouTube video ")
        print("2. Add a YouTube video ")
        print("3. Update a YouTube video ")
        print("4. Delete a YouTube video ")
        print("5. Exit the App")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                print("*" * 70)
                list_all_videos()
                print("*" * 70)
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the video ID to update: ")
                name = input("Enter the updated video name: ")
                time = input("Enter the updated video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the video ID to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice!")
if __name__ == "__main__":
    main()