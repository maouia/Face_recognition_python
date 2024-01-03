import os
import inquirer

import file_path
import face_detect


questions = [
    inquirer.List(
        "choice",
        message="Whats Your Choice?",
        choices=["ChangePath", "FaceDetect","Exit"],
    ),
]
os.system('clear')
while True :
    answers = inquirer.prompt(questions)
    match answers["choice"]:
        case "Exit" :
            exit()
        case "ChangePath":
            os.system('clear')
            path = input('Enter The Path To Change : ')
            file_path.update_path(path)
        case "FaceDetect":
            face_detect.main()
        case _ :
            print("error choice")



