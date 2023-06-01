#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 rfid(SS_PIN, RST_PIN);

LiquidCrystal_I2C lcd(0x27, 20, 4);
String printing = "------GasLevel------";
String gas_level;

bool flag1, flag2, flag3;
int rf;

byte nuidPICC[4];

void setup()
{
  rf = 0;
  flag1 = false;
  flag2 = false;
  flag3 = false;
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print(printing);
  lcd.setCursor(9,2);
  lcd.print("00");

  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522 

}

void loop()
{
  delay(500);
  if (Serial.available() > 0){
    lcd.setCursor(9, 2);
    char s = Serial.read();
    if(s=='1')
      gas_level = "01";
    else if(s=='2')
      gas_level = "02";
    else if(s=='3')
      gas_level = "03";
    else if(s=='4')
      gas_level = "04";
    else if(s=='5')
      gas_level = "05";
    lcd.print(gas_level);
  }
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
  
  // 카드가 인식되었다면 다음으로 넘어가고 아니면 더이상 
  // 실행 안하고 리턴
  if ( ! rfid.PICC_IsNewCardPresent())
    return;

  // ID가 읽혀졌다면 다음으로 넘어가고 아니면 더이상 
  // 실행 안하고 리턴
  if ( ! rfid.PICC_ReadCardSerial())
    return;

   if (rfid.uid.uidByte[0] != nuidPICC[0] || 
   rfid.uid.uidByte[1] != nuidPICC[1] || 
   rfid.uid.uidByte[2] != nuidPICC[2] || 
   rfid.uid.uidByte[3] != nuidPICC[3] ) {
    // Store NUID into nuidPICC array
    for (byte i = 0; i < 4; i++) {
      nuidPICC[i] = rfid.uid.uidByte[i];
    }
    if(rf == 0){
      Serial.print("rfid_first");
      rf++;
  }
    else if (rf == 1){
      Serial.print("rfid_second");
     rf++;
  }
  }



    // Halt PICC
  rfid.PICC_HaltA();

  // Stop encryption on PCD
  rfid.PCD_StopCrypto1();
}
