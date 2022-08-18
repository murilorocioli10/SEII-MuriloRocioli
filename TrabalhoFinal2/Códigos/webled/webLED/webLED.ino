//#include <SoftwareSerial.h>

String inByt;
int Led = 4; 

void setup() {

  Serial.begin(9600);
  // Inicializando a saída
  pinMode(Led, OUTPUT);
  // Configurando a saída como desligado
  digitalWrite(Led, LOW);
  //Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  //

}

void serialEvent() {
    inByt = Serial.readStringUntil('\n');
    //Serial.print(inByt);
   
    if (inByt == "on") {
        digitalWrite(Led, HIGH);
    } else if (inByt == "off") {
        digitalWrite(Led, LOW);
    } //else {
       //continue;
    //}
}
