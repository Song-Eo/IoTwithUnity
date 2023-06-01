#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 rfid(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key; 

LiquidCrystal_I2C lcd(0x27, 20, 4);
String printing = "------GasLevel------";
String gas_level;

byte nuidPICC[4];

void setup()
{
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print(printing);
  lcd.setCursor(9,2);
  lcd.print("00");

  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522 

    for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;
  }
  pinMode(3, OUTPUT);
}

void loop()
{
  if (Serial.available() > 0){
    gas_level = "0";
    lcd.setCursor(9, 2);
    char s = Serial.read();
    gas_level.concat(s);
    lcd.print(gas_level);
  }
  if ( ! rfid.PICC_IsNewCardPresent())
    return;

  if ( ! rfid.PICC_ReadCardSerial())
    return;

  digitalWrite(3, HIGH);
  delay(2000);
  digitalWrite(3, LOW);
}
