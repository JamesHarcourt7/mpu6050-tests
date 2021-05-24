#include <MPU6050_light.h>
#include <Wire.h>

MPU6050 mpu(Wire);

void setup() {
  Serial.begin(115200);
  Wire.begin();
  mpu.begin();
  mpu.calcGyroOffsets();
}

void loop() {
  mpu.update();
  float angle[3] = {mpu.getAngleX(), mpu.getAngleY(), mpu.getAngleZ()};
  String output = "";
  output.concat("{");
  output.concat(angle[0]);
  output.concat(", ");
  output.concat(angle[1]);
  output.concat(", ");
  output.concat(angle[2]);
  output.concat("}");
  Serial.println(output);
  delay(100);
}
