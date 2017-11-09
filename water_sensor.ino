
//set pin numbers
const int RedledPin = 5;
const int buzzerPin = 4;
const int waterSensorPin = A0;
const int GreenledPin = 16;
const int ButtonPin = 14;

void setup () {
  Serial.begin(115200);
  pinMode(GreenledPin, OUTPUT);
  pinMode(RedledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(waterSensorPin, INPUT);
}

void loop() {
  int waterSensor = analogRead(waterSensorPin);  //read the state of the LDR value
  Serial.println(waterSensor); 
  if (waterSensor < 390) {
    digitalWrite(GreenledPin, LOW);
    tone(buzzerPin, 100);
    digitalWrite(RedledPin, HIGH);
    delay(100);

    noTone(buzzerPin);
    digitalWrite(RedledPin, LOW);
    delay(100);

    Serial.println("----------- ALARM ACTIVATED -----------"); 
  }
  else {  
    noTone(buzzerPin);
    digitalWrite(RedledPin, LOW);
    digitalWrite(GreenledPin, HIGH);
    delay(100);

    Serial.println("ALARM DEACTIVATED");
  }
}
