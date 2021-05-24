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
  float angle = mpu.getAngleZ();
  float accel[2] = {mpu.getAccX(), mpu.getAccZ()};
  String output = "";
  output.concat(angle);
  output.concat(" ");
  output.concat(accel[0]);
  output.concat(" ");
  output.concat(accel[1]);
  Serial.println(output);
  delay(100);
}
