void setup() {
  flag1 = false;
  flag2 = false;
  flag3 = false;
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  

  if(analogRead(0)<500 && !flag1){
    Serial.print("rain");
    flag1 = true;
  }

  if(analogRead(1)<500 && !flag2){
    Serial.print("mois");
    flag2 = true;
  }

  if(digitalRead(7) && !flag3){
    Serial.print("undetect");
    flag3 = true;
  }
    
  delay(750);

}
