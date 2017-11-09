
//set pin numbers
const int RedledPin = 5;
const int buzzerPin = 4;
const int ldrPin = A0;
const int GreenledPin = 16;
const int ButtonPin = 14;

void setup () {
  Serial.begin(115200);
  pinMode(GreenledPin, OUTPUT);
  pinMode(RedledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ldrPin, INPUT);
}

void loop() {
  int ldrStatus = analogRead(ldrPin);  //read the state of the LDR value
  Serial.println(ldrStatus); 
  if (ldrStatus <= 400) {
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
