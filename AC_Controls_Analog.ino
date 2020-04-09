#define serialPi Serial

String data = "Arduino is up";
int analogPinA0 = A0;
int analogPinA1 = A1;
int analogPinA2 = A2;
int analogPinA3 = A3;
int analogPinA4 = A4;
int var1 = 0;
int var2 = 0;
int var3 = 0;
int var4 = 0;
int var5 = 0;

void setup() {
  // put your setup code here, to run once:
  serialPi.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  var1 = analogRead(analogPinA0);
  var2 = analogRead(analogPinA1);
  var3 = analogRead(analogPinA2);
  var4 = analogRead(analogPinA3);
  var5 = analogRead(analogPinA4);
  serialPi.print(",");
  serialPi.print(var1);
  serialPi.print(",");
  serialPi.print(var2);
  serialPi.print(",");
  serialPi.print(var3);
  serialPi.print(",");
  serialPi.print(var4);
  serialPi.print(",");
  serialPi.print(var5);
  serialPi.println(",");
  delay(200);
}
