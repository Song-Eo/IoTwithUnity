#include <Wire.h>
#include <LiquidCrystal_I2C.h>
 
LiquidCrystal_I2C lcd(0x27,20,4); 
 
 
void setup()
{
  lcd.init();  // LCD초기 설정             
  lcd.backlight(); // LCD초기 설정  
  lcd.setCursor(0,0); //텍스트가 LCD에 나타날 위치
  lcd.print("Hellow, world!"); 
  lcd.setCursor(3,1);
  lcd.print("How are you?"); 
}
