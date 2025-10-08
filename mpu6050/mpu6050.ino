#include "Wire.h"       
#include "I2Cdev.h"     
#include "MPU6050.h"
long time=30000; // time range of the sample   

MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;

struct MyData {
  byte X;
  byte Y;
  byte Z;
    byte AX;
  byte AY;
  byte AZ;

};

MyData data;

void setup()
{
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  //pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
if(millis()<=time){
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  data.X = map(ax, -17000, 17000, 0, 255 ); // X axis data
  data.Y = map(ay, -17000, 17000, 0, 255); 
  data.Z = map(az, -17000, 17000, 0, 255);
    data.AX = map(gx, -17000, 17000, 0, 255 ); // X axis data
  data.AY = map(gy, -17000, 17000, 0, 255); 
  data.AZ = map(gz, -17000, 17000, 0, 255);  // Y axis data
  delay(100);
  //Serial.print("Axis X = ");
  Serial.print("[");
  Serial.print(data.X);
  Serial.print(",");
  //Serial.print("Axis Y = ");
  Serial.print(data.Y);
  Serial.print(",");
  //Serial.print("Axis Z  = ");
  Serial.print(data.Z);
  Serial.println("],");

/*Serial.print("  ");
    Serial.print("Axis AX = ");
  Serial.print(data.AX);
  Serial.print("  ");
  Serial.print("Axis AY = ");
  Serial.print(data.AY);
  Serial.print("  ");
  Serial.print("Axis AZ  = ");
  Serial.println(data.AZ);
*/
}
}
