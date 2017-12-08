This is the README.md file for the implementation of the project.

First, the hardware must be assembled together. The circuit details are outlined in the Hardware Design page. The project uses an MKR1000 board, although
other boards with an ethernet shield can be subsituted. Note that an external 9V external power supply can be provided instead of a USB connection, although
for the initial setup a USB connection is required to upload the code. The code is located in the arduino_code folder or on github https://github.com/clammtl/arduinoplantwaterer)

After setting up the hardware, a ThingSpeak channel must be initiated. An account can be created for free. Then, the fields must be initiated.
For this project, only Field1 (humidity) was selected for the channel. The channel is public, although a private channel can also be used (see details in Arduino code).
Then, the arduino can be connected via USB to a Mac or PC to upload the arduino code with the Arduino application. The libraries for the MKR1000 were updated
in the application to ensure that the code could be uploaded.

Finally, a website is set up to retrieve the data from the ThingSpeak channel. A webservice call is implemented with the ThingSpeak API to retrieve the latest data.
The website is designed using a combination of HTML, javascript, python and jinja. The implementation is located in application.py.