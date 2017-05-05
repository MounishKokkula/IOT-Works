#include <ESP8266WiFi.h>
#include <PubSubClient.h>
/* Flame Sensor analog example.
Code by Reichenstein7 (thejamerson.com)

Flame Sensor Ordered from DX ( http://www.dx.com/p/arduino-flame-sensor-for-temperature-
detection-blue-dc-3-3-5v-118075?tc=USD&gclid=CPX6sYCRrMACFZJr7AodewsA-Q#.U_n5jWOrjfU )

To test view the output, point a serial monitor such as Putty at your arduino. 
*/


const char* ssid = //Your SSID
const char* password = // Your password
const char* mqtt_server = //Your MQTT Server ip


//// lowest and highest sensor readings:
//const int sensorMin = 0;     // sensor minimum
//const int sensorMax = 1024;  // sensor maximum
//int Water = 0;

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
     // client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


void setup() {
  // initialize serial communication @ 9600 baud:
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // read the sensor on analog A0:
	int sensorReading = digitalRead(5);
  // map the sensor range (four options):
  // ex: 'long int map(long int, long int, long int, long int, long int)'
//	int range = map(sensorReading, sensorMin, sensorMax, 0, 3);
        
  
//  // range value:
//  switch (range) {
//  case 0:    // A fire closer than 1.5 feet away.
//    Serial.println("** Close Fire **");
//    FireValue = 0;
//    
//    break;
//  case 1:    // A fire between 1-3 feet away.
//    Serial.println("** Distant Fire **");
//    FireValue = 1;
//    break;
//  case 2:    // No fire detected.
//    Serial.println("No Fire");
//    FireValue = 2;
//    break;
//  }
//  delay(1);  // delay between reads
//      
  long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    ++value;
    //snprintf (msg, 75, "hello world #%ld", value);
    Serial.print("Publish message: ");
    
    String pubString = String(sensorReading); 
    pubString.toCharArray(msg, pubString.length()+1); 
    Serial.println(msg);
    client.publish("Flood", msg);
  }
}
