//Función de Activación de tipo ReLu (Rectified Linear Unit)

double ReLu(double n){
  if ( n < 0)
  return 0.0;
  else if (n >= 0)
  return n;
}
