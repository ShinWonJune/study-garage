
# Asyncio
# 고성능 코루틴 모듈
# 특징 : 하나의 스레드 안에서 코루틴 끼리 제어를 양보하며 작업할 수 있게 함 
#       await(yield from) 을 통해 코루틴 끼리 제어를 가능하게함
#       await 뒤에는 `async` 가 붙은 객체만 올 수 있다. `비동기 함수` 라는 표시.
# await 을 만나면 다른 코루틴으로 제어권이 넘어간다
# 모든 코루틴이 await을 만나면 , await을 만나서 멈췄던 지점 다음 코드가 진행된다.

# Asyncio를 활용하여 웹 페이지 비동기로 가져오기
# urlopen(url) 함수는 결과가 나올 때 까지 코드실행이 중단되는 Blocking I/O 함수 이므로, 쓰레드를 활용해 비동기 작업을 진행함

import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
import asyncio

urls = ['http://naver.com','https://google.com','https://apple.com','https://velog.io','https://github.com','https://gmarket.co.kr']

start = timeit.default_timer()

async  def fetch(url, executor): #동시에 여러 요청이 있을 것이다. async 표시
    print('Thread Name:', threading.current_thread().getName(),'Start',url)
    res = await loop.run_in_executor(executor, urlopen, url) #run_in_executor(executor, func, *args): futures를 멀티스레드에서 실행하게 함. 마찬가지로 asyncio 이므로 await 통해 값 받는다.
    # await 을 만났으므로 다른 코루틴으로 제어권 넘어간다.
    # 모든 코루틴이 await을 만났으면 아래 print문이 실행된다.
    print('Thread Name:', threading.current_thread().getName(),'Done',url)  
    return res.read()[0:5]

async def main():   #여러 함수가 여러 요청을 할 함수이니 비동기 처리 하겠다. 비동기 표시해줌.  async
    # 쓰레드 풀 생성
    executor= ThreadPoolExecutor(max_workers = 10)
    # asyncic.create_task : 하나의 task를 만드는 함수.
    futures = [asyncio.create_task(fetch(url, executor)) for url in urls] # url 만큼의 task 객체(future)가 만들어짐. 아직 실행은 아님
    # await 을 만나면 현 루틴은 멈추고 코루틴 실행됨. futures 가 실행됨. 즉 fetch가 실행됨.
    res = await asyncio.gather(*futures)  #gather: 일이 다 끝난 후 모아주는 역할. 위치 인수(순서대로 여러개를 넣는 인수)로 인수를 받으므로 list를 언패킹 해줘야함. gather([a,b,c]) -> gather(a,b,c)
    print()
    #결과 확인
    print('Result : ', res)
    
# 추가 함수
# asyncio.wait(fts, return_when = ) fts 동시실행하고 return_when에 조건에 따라 함수를 종료시킨다. FIRST_COMPLETE, FRIST_EXCEPTION, ALL_COMPLETE
# asyncio.as_completed(fts, *args, timeout = ) fts의 awaitalb객체를 동시에 실행시킨다. timeout 이 지나고 작업이 완료되지 않으면 timeout error를 발생시킨다.

if __name__ == '__main__':
    # 루프 생성
    loop = asyncio.get_event_loop() #  코루틴 간의 흐름을 관리하는 루프. 제어 양보 관리
    # 루프 대기
    loop.run_until_complete(main()) # 모든 제너레이터가 끝날 때 까지 기다리는 함수
    # 함수 실행
    main()        


    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print('total time cost',duration)  
                                        

