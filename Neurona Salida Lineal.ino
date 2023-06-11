double p[] = {0.51,0.59,-0.15};
double w[] = {0.57,-0.79,0.75};
double b = 0.8;

void setup() {
  Serial.begin(9600);
  double n = p[0]*w[0]+p[1]*w[1]+p[2]*w[2]+b;
  double a = lineal(n);
  Serial.print("La neurona es: ");
  Serial.println(n,4);
  Serial.print("La Salida Lineal es: ");
  Serial.println(a,4);  
 /* Para que esta neurona funcione se tiene que ingresar a una función de activación */
}

void loop() {
  // put your main code here, to run repeatedly:

}

double lineal(double n){
  return n;
}
