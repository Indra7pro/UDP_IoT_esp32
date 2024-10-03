## UDP_IoT_esp32
It is a server client connection between a pc running python and esp32 to control devices.<br><br>

#### In this example I have used this to make a rc car.<br>
As udp connection is much faster as compared to tcp/ip connection.
The dependencies of the following program
`pynput`,`socket`,`threading`
To install: 
`pip install pynput`

The rest of the modules are already present as the built in modules. 


#### Next is to configure the `arduino ide` for esp32

Add the following link :`https://espressif.github.io/arduino-esp32/package_esp32_index.json` in the `additional boards manager URLs` which could be found in the `preferences` of the auduino library. 

Install the esp32 board from the board manager.<br>
Install `esp32servo` library from the library manager.
