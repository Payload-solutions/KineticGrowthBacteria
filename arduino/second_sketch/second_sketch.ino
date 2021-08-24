#include <DHT.h>


const int analogPin = A1; // for the pH sensor
int buf[10], temp;
bool digitalValue;
int dataTemp = 5;
unsigned long int avgValue;


DHT dht(dataTemp,DHT11);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();

}

void loop() {
  // put your main code here, to run repeatedly:
  int counter = 0;

  while (counter < 6){
      Serial.println("Initializing...");
      Serial.println(analogPin);

      if (analogPin >= 15){
          Serial.println("pH sensor disconnected!!");
        }
      else{
          for (int i = 0; i < 10; i++){
              buf[i] = analogRead(analogPin);
              delay(1000);
            }
          for (int i = 0; i < 9; i++){
            
              for (int j = i+1; j < 10; j++){
                    if (buf[i] > buf[j]){

                      temp = buf[i];
                      buf[i], buf[j] = buf[j], temp;
                    }
                }
            }
        
        }

        avgValue = 0;

        for (int i=2; i < 8; i++){
            avgValue += buf[i];
        }

        float pHVol = (float)avgValue*5.0/1024/6;
        float pHValue = -5.70*pHVol + 21.34;

        Serial.print("phValue => ");
        Serial.println(pHValue);
         
    }

}
