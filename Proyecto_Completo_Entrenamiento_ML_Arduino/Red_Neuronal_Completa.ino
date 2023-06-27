#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

double accelX = 0, accelY =0, accelZ;

unsigned long lastTime = 0, sampleTime = 100;
///////////////////////////////// Variables Red Neuronal /////////////////////////////////
/*

En esta parte copiar y pegar los datos obtenidos del análisis para las variables de la Red Neuronal



*/
//////////////////////////////////////////////////////////////////



///////////////////////////////// Preprocesamiento Red Neuronal /////////////////////////////////

/*


En esta parte copiar y pegar los valores dados de preprocesamiento de la red neuronal


*/


///////////////////////////////////////////////////////////////////////////////////////////////////////


void setup() {

  Serial.begin(9600);

  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    delay(500);
  }
}

void loop() {

  if(millis()-lastTime>=sampleTime)
  {
    lastTime = millis();

    Vector normAccel = mpu.readNormalizeAccel();
    accelX = normAccel.XAxis;
    accelY = normAccel.YAxis;
    accelZ = normAccel.ZAxis;

    a0[0] = dataNormalized(accelX,mean[0],dstd[0]);
    a0[1] = dataNormalized(accelY,mean[1],dstd[1]);
    a0[2] = dataNormalized(accelZ,mean[2],dstd[2]);

    ///////////////////////////////// Estructura Red Neuronal /////////////////////////////////

            /*

            Aquí copiar y pegar la estructura de la red neuronal obtenida de Python

            */


    //////////////////////////////////////////////////////////////////////////////////////////

          if (round(a2[0]==1)) Serial.println("Izquierda");else Serial.println("No izquierda");
  }
}


// Funciones de Activación para la Red Neuronal


double relu(double n)
{
  if(n>=0) return n; else if (n<0) return 0;
}
double sigmoid(double n)
{
  return 1.0/(1.0 + exp(-n));
}

double dataNormalized(double inputData,double mean,double desvStandar)
{
  double valueNorm;
  valueNorm = (inputData-mean)/desvStandar;
  return valueNorm;
}