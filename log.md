### 3일차
## if의 여러개 써진 코드를 3줄코드로 고치다.
    if 0 <= box_y <= Line_distant/2:
        distant = box_y
    elif Line_distant/2 <= box_y <= Line_distant*(3/2):
        distant = abs(Line_distant-box_y)    
    elif Line_distant*(3/2) <= box_y <= Line_distant*(5/2):
        distant = abs(Line_distant*2-box_y)
    elif Line_distant*(5/2) <= box_y <= Line_distant*(7/2):
        distant = abs(Line_distant*3-box_y)
    elif Line_distant*(7/2) <= box_y <= Line_distant*(9/2):
        distant = abs(Line_distant*4-box_y)
    elif Line_distant*(9/2) <= box_y <= Line_distant*(11/2):
        distant = abs(Line_distant*5-box_y)
    elif Line_distant*(11/2) <= box_y <= Line_distant*(13/2):
        distant = abs(Line_distant*6-box_y)
    elif Line_distant*(13/2) <= box_y <= Line_distant*(15/2):
        distant = abs(Line_distant*7-box_y)
    elif Line_distant*(15/2) <= box_y <= Line_distant*(17/2):
        distant = abs(Line_distant*8-box_y)
    elif Line_distant*(17/2) <= box_y <= Line_distant*(19/2):
        distant = abs(Line_distant*9-box_y)
distant의 값(바늘과 선의 거리)를 구해주는 코드를 
이러한 if의 여러개가 붙어있는 부분을 for 문으로 고쳐

    for q in range(10):
        if Line_distant*(-1 + 2*q /2) <= box_y <= Line_distant*(1 + 2*q/2):
                  distant = abs(Line_distant*q - box_y)
            로 3줄로 줄였다.
            
## counter_total의 값을 0 으로 변화시켜 숫자의 잘못세지는 오류를 해결하다.
  counter_total을 10에서 0 으로 고쳐 숫자가 잘못 세지는 오류를 해결했다.  
## 박스의 크기를 조정하다.

### 4일차
## 사칙연산 실수를 줄이다.
if Line_distant*(-1 + 2*q /2) <= box_y <= Line_distant*(1 + 2*q/2)
부분에 우선 사칙연산 실수를 줄이기 위해 괄호를 써서
if Line_distant*((-1 + 2*q)/2) <= box_y <= Line_distant*((1 + 2*q)/2):
로 고쳤다.
### 5일차
오류가 있었는데 여러번 바꾸면서 실행해 오류를 바로잡았다.
