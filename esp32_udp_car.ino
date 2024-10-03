#include <WiFi.h>
#include <WiFiUdp.h>
#include <ESP32Servo.h>

// Wi-Fi credentials
const char* ssid = "Your wifi ssid";
const char* password = "Your wifi password";

// Define pins
const int servoPin = 12;
const int ledPin = 2;
const int m1Pin = 32;
const int m2Pin = 33;

// Create objects for Servo and UDP
Servo myServo;
WiFiUDP udp;
unsigned int localPort = 8080;

void setup() {
  // Initialize Serial Monitor
  Serial.begin(115200);

  // Initialize GPIOs
  pinMode(ledPin, OUTPUT);
  pinMode(m1Pin, OUTPUT);
  pinMode(m2Pin, OUTPUT);
  
  // Attach servo to pin
  myServo.attach(servoPin);
  myServo.write(90); // Set initial servo position to 90 degrees (neutral)

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());

  // Start UDP
  udp.begin(localPort);
  Serial.println("UDP server started");
}

void loop() {
  char incomingPacket[255]; // Buffer for incoming packets
  int packetSize = udp.parsePacket();

  if (packetSize) {
    // Read the packet into incomingPacket
    int len = udp.read(incomingPacket, 255);
    if (len > 0) {
      incomingPacket[len] = 0;
    }

    Serial.printf("Received packet from %s: %s\n", udp.remoteIP().toString().c_str(), incomingPacket);

    String request = String(incomingPacket);

    // On Commands --------------------------------
    if (request == "FL_on") {
      digitalWrite(m1Pin, HIGH);
      digitalWrite(m2Pin, LOW);
      myServo.write(180);
    } 
    else if (request == "FR_on") {
      digitalWrite(m1Pin, HIGH);
      digitalWrite(m2Pin, LOW);
      myServo.write(0);
    } 
    else if (request == "BL_on") {
      digitalWrite(m1Pin, LOW);
      digitalWrite(m2Pin, HIGH);
      myServo.write(180);
    } 
    else if (request == "BR_on") {
      digitalWrite(m1Pin, LOW);
      digitalWrite(m2Pin, HIGH);
      myServo.write(0);
    } 
    else if (request == "F_on") {
      digitalWrite(m1Pin, HIGH);
      digitalWrite(m2Pin, LOW);
    } 
    else if (request == "B_on") {
      digitalWrite(m1Pin, LOW);
      digitalWrite(m2Pin, HIGH);
    } 
    else if (request == "L_on") {
      myServo.write(180);
    } 
    else if (request == "R_on") {
      myServo.write(0);
    } 
    else if (request == "break") {
      digitalWrite(m1Pin, HIGH);
      digitalWrite(m2Pin, HIGH);
    }

    // Off Commands --------------------------------
    else if (request == "FL_off" || request == "FR_off" || request == "BL_off" || request == "BR_off") {
      digitalWrite(m1Pin, LOW);
      digitalWrite(m2Pin, LOW);
      myServo.write(90);  // Neutral position
    } 
    else if (request == "F_off" || request == "B_off") {
      digitalWrite(m1Pin, LOW);
      digitalWrite(m2Pin, LOW);
    } 
    else if (request == "L_off" || request == "R_off") {
      myServo.write(90);  // Neutral position
    } 
    else if (request == "all_off") {
      digitalWrite(m1Pin, LOW);
      digitalWrite(m2Pin, LOW);
      myServo.write(90);  // Neutral position
    }

    // Send response back to client
    udp.beginPacket(udp.remoteIP(), udp.remotePort());
    udp.print("ok");
    udp.endPacket();
  }
}
