#include <LiquidCrystal.h>
#include <Stepper.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

void setup()
{
  // initialize the LCD
  lcd.begin();

  // Turn on the blacklight and print a message.
  lcd.backlight();
  lcd.print("Hello, world!");
}
 
void loop(){
   lcd.setCursor(0,0);
   lcd.write("Clockwise");
   my28BJY48.step(-STEPS);
   lcd.clear();
   delay(1000);

   lcd.setCursor(0,0);
   lcd.write("CounterClockwise");
   my28BJY48.step(STEPS);
   lcd.clear();
   delay(1000);


}
