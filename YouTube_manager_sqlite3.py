import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               ) 
''')

counter = 0

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)",(name, time))
    con.commit()
    counter += 1

def update_video(vide0_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name, new_time, vide0_id))
    con.commit()

def delete_video(vide0_id):
    cursor.execute("DELETE FROM videos where id = ?", (vide0_id,))
    con.commit()
    counter -= 1
    
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
                if counter == 0:
                    print("Nothing to see in List")
                else:
                    list_all_videos()
                print("*" * 70)
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the video ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the video ID to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice!")
    con.close()
if __name__ == "__main__":
    main()
