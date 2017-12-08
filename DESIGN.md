This is the design document for the project.

----Arduino hardware design----
The 12v power supply has one wire connected to one end of the pump, and another end is connected to the relay.
The other end of the pump is connected to the relay as well. The relay acts as a switch to turn on and off the pump. Using the 5V
high voltage from the controller, we can control the switch. A LED indicator on the relay's board indicates when the terminals are closed.
A 9v external battery supply can be connected to the board to power it instead of connecting the board with a USB wire.
See ArduinoPlantWaterer_sketch.jpg for a sketch of the design.

----Arduino code design----
The arduino code is configured for the MKR1000 and uses C. The first functionality was implemented based the WiFiWebServer tutorial
to allow the MKR1000 to connect to the wifi. From another WiFi101 example
(see "https://github.com/arduino-libraries/WiFi101/blob/master/examples/AP_SimpleWebServer/AP_SimpleWebServer.ino"),
another functionality was implemented; the SSID and password are located in a separate library, allowing a user to define these
variables separately. The arduino initiates the connection at setup, and success or failure is relayed to the serial screen.

Then, the soil sensor was added to the arduino code, based on a tutorial from the Sparkfun sensor
(see "https://learn.sparkfun.com/tutorials/soil-moisture-sensor-hookup-guide"). The analog value is translated into a percentage
value and printed to the serial screen. If the percentage drops below 40%, the pump is activated through a digital
output. A delay is set to allow the water to be pumped for 3 seconds. Another delay is set at 15 seconds to allow the soil to
absorb the water before another reading is taken.

Finally, I based myself on a ThingSpeak api tutorial to send the sensor reading
(see "https://www.mathworks.com/help/thingspeak/continuously-collect-data-and-bulk-update-a-thingspeak-channel-using-an-arduino-mkr1000-board-or-an-esp8266-board.html").
A buffer is created to collect the moisture sensor data every 15 seconds. The data is then sent every 2 minutes. This reduces the
power usage of the device. A relative time stamp is used each time the buffer is updated. The POST request's success or failure
is then printed on Serial. The channel is public for this example's purposes, however a private channel can also be used if the
key is provided in the POST request.

The code can be found here: "https://github.com/clammtl/arduinoplantwaterer".

----Website design----
Finally, a website is set up to retrieve the data from the ThingSpeak channel.

ThingSpeak is an IoT analytics platform that allows to store, visualize,
and analyze live data streams. Data is stored on the cloud and is easily accesible with an API. This solution was used as it was
easy to integratevwith the watering system and could easily be accessed remotely on any device. A channel had to be set up with a
humidity level field, recording the percentage of soil humidity being sent to the sensor every 2 minutes.

A webservice call is implemented with the ThingSpeak API to retrieve the latest data. Using the API is fairly easy for a user
with basics in programming. Since one of the goals of this project was to make this fairly accessible, this is a good platform
to use. It can also be manipulated and modified to extract other types of data. There are a number of visualization which can be
easily integrated to a website.

The website is designed using a combination of HTML, javascript, python and jinja. Using python as opposed to only HTML and javascript
allows flexibility in the future to integrate other functions such a a push function from the server to the arduino for remote access.