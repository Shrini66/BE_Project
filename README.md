Speech to Sign Language Converter
Overview
The Speech to Sign Language Converter is a web application that takes live audio speech recordings as input, converts them into text, and displays relevant Indian Sign Language animations. This project combines various technologies to provide a seamless experience for users.

Features
Front-end: The user interface is built using HTML, CSS, and JavaScript to provide an intuitive and user-friendly experience.

Speech Recognition: Utilizes the JavaScript Web Speech API to transcribe live audio speech into text.

Text Preprocessing: The application uses the Natural Language Toolkit (NLTK) in Python to preprocess the transcribed text.

Sign Language Animations: It displays 3D animations of a character created using the Blender 3D tool to convey Indian Sign Language.

Prerequisites
Python >= 3.7
A web browser that supports the Web Speech API
Usage
Clone the repository to your local machine.

Open the terminal in the project directory.

Run the application with the command:

python manage.py runserver [optional port number]
Once the server is running, open your web browser and go to the provided localhost address (usually looks like "http://127.0.0.1:8000/").

Sign up and start exploring the application.

Click on the microphone button to start recording speech.

The speech is processed and relevant sign language animations are displayed accordingly. You can also manually enter text for conversion.

Contribution
Contributions to this project are welcome. If you have any suggestions or improvements, feel free to create a pull request.

License
This project is licensed under the MIT License.
