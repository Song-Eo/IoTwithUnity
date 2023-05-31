#define RAINDROPMODULE 0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  

  if(analogRead(0)<500)
    Serial.println("Rainy");

  if(analogRead(1)<500)
    Serial.println("Moisture");

  if(!digitalRead(7))
    Serial.println("Detected");
  delay(750);

}
