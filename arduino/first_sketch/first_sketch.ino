// #include <DHT.h>


// const int AnalogPin = A1;
int movVar = 2;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(movVar, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int movVal = digitalRead(movVar);
  //Serial.println("Hello world!!");

  if (movVal == HIGH){
      Serial.println("Movement detected");
      delay(500);
      Serial.println(movVal);
    }
  // Serial.println(movVal);

}
