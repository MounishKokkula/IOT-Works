
//set pin numbers

const int buzzerPin = 16;//d2
const int ldrPin = A0;
const int GreenledPin = 4;//d0
const int BlueledPin = 2;//d4
const int RedledPin = 5; //d1

void setup () {
  Serial.begin(115200);
  pinMode(GreenledPin, OUTPUT);
  pinMode(RedledPin, OUTPUT);
  pinMode(BlueledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ldrPin, INPUT);
  }

void loop() {
  int ldrStatus = analogRead(ldrPin);  //read the state of the LDR value
  Serial.println(ldrStatus); 
  if (ldrStatus <= 400) {
    tone(buzzerPin, 100);
    analogWrite(RedledPin, 0);
    analogWrite(GreenledPin, 255);
    analogWrite(BlueledPin, 0);
    delay(100);

    analogWrite(RedledPin, 0);
    analogWrite(GreenledPin, 0);
    analogWrite(BlueledPin, 0);
    delay(100);    
    
 //   noTone(buzzerPin);
 //   delay(100);

    Serial.println("----------- ALARM ACTIVATED -----------"); 
  }
  else {  
//    noTone(buzzerPin);

    analogWrite(RedledPin, 255);
    analogWrite(GreenledPin, 0);
    analogWrite(BlueledPin, 0);
    delay(100);

    Serial.println("ALARM DEACTIVATED");
  }
}


