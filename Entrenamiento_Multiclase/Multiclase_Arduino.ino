#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

double accelX = 0, accelY =0, accelZ;

unsigned long lastTime = 0, sampleTime = 100;
//--------------------------------------------- Variables Red Neuronal ---------------------------------------------------//

double a0[3];
double W1[3][3] = {{0.033,2.64,-0.151},{-0.938,0.427,-1.31},{0.08,-3.276,-0.773}};
double a1[3];
double W2[5][3] = {{-3.803,-11.737,-4.267},{-3.057,1.563,-2.106},{-0.019,0.015,0.539},{1.226,-0.263,0.932},{1.741,-0.355,0.957}};
double a2[5]; 
double b1[3]= {-0.571,-0.567,1.225};
double b2[5]= {0.088,-0.059,0.144,0.049,-0.071};
double aux = 0.0;
//////////////////////////////////////////////////////////////////



//---------- Preprocesamiento Red Neuronal -----------------------///
double mean[3]={0.306,-1.245,4.879};
double dstd[3]={5.639,4.382,3.352};

///////////////////////////////////////


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
                                
                                
                                    //-------------------------------Normalización de Datos -------------------------//
                                  
                                                          a0[0] = dataNormalized(accelX,mean[0],dstd[0]);
                                                          a0[1] = dataNormalized(accelY,mean[1],dstd[1]);
                                                          a0[2] = dataNormalized(accelZ,mean[2],dstd[2]);
                                
                                                         //////////////////////////////////////////////////
                                    

    //---------------------------------------------------- Estructura Red Neuronal --------------------------------------------------------------//

                           
                        for(int i = 0 ; i<3; i++ ) {aux=0.0;for(int j = 0 ; j <3 ; j++ ) { aux=aux+W1[i][j]*a0[j];} a1[i]=relu(aux+b1[i]);}
                        double aux1 = 0;
                        for(int i = 0 ; i<5; i++ ) {aux=0.0;for(int j = 0 ; j <3 ; j++ ){ aux=aux+W2[i][j]*a1[j];} a2[i]=(aux+b2[i]);aux1=aux1+exp(a2[i]);}
                        double minimo = 0.0;
                        int classes = 0;
                        for(int i = 0;  i<5; i++){a2[i] = exp(a2[i])/aux1;if(a2[i]>minimo){minimo=a2[i];classes=i;}}

                          //////////////////////////////////////////////////////////////////////////////////////////

         Serial.println(classes);
  }
}


// Funciones de Activación para la Red Neuronal


double relu(double n)
{
  if(n>=0) return n; else if (n<0) return 0;
}

double dataNormalized(double inputData,double mean,double desvStandar) 
{
  double valueNorm;
  valueNorm = (inputData-mean)/desvStandar;
  return valueNorm;
}
