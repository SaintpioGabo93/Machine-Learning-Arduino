
#include <Wire.h>
#include <MPU6050.h>

// Variables que va a usar el giroscopio

double aceleracionX = 0, aceleracionY = 0, aceleracionZ;
double rotacionX = 0, rotacionY = 0, rotacionZ; 

unsigned long tiempoFinal = 0, tiempoMuestreo = 100;

 
// Creación del objeto giroscopio

MPU6050 acelerometoGiroscopio;

void setup() {
  Serial.begin(9600);
  
  while(!acelerometoGiroscopio.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G)) // Activación del acelerometro con giroscópio
  {
    delay(500);
    }

}

void loop() {

  if (millis() - tiempoFinal >= tiempoMuestreo)
  {
    tiempoFinal = millis();

    Vector moduloAceleracion = acelerometoGiroscopio.readNormalizeAccel(); // Obtiene en forma de vector el módulo de la medición de las tres componentes de la aceleración
    Vector moduloRotacion = acelerometoGiroscopio.readNormalizeGyro(); // Obtiene el módulo de la rotación de las componentes del giroscópio

    aceleracionX = moduloAceleracion.XAxis;
    aceleracionY = moduloAceleracion.YAxis;
    aceleracionZ = moduloAceleracion.ZAxis;

    rotacionX = moduloRotacion.XAxis;
    rotacionY = moduloRotacion.YAxis;
    rotacionZ = moduloRotacion.ZAxis;

    Serial.println(aceleracionX);
    Serial.println(aceleracionY);
    Serial.println(aceleracionZ);
    Serial.println(rotacionX);
    Serial.println(rotacionY);
    Serial.println(rotacionY);
    
    }

}
