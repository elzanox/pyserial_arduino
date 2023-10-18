#define led  LED_BUILTIN
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    Serial.println(command);
    if (command == 'H') {
      digitalWrite(led, HIGH);
      Serial.println("ini nyala");
    }
    else if (command == 'L') {
      Serial.println("ini mati");
      digital  Write(led, LOW);
    }
  }
}
