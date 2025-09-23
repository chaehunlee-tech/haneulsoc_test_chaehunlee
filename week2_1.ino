// LED 연결 핀 번호 (GPIO 2)
const int ledPin = 2; 

void setup() 
{ 
	// LED 핀을 출력 모드로 설정 
	pinMode(ledPin, OUTPUT); 
} 
void loop() 
{ 
	// LED를 켬 
	digitalWrite(ledPin, HIGH); 
	delay(1000); // 1초 대기 
  
	// LED를 끔 
	digitalWrite(ledPin, LOW); 
	delay(1000); // 1초 대기  
}
