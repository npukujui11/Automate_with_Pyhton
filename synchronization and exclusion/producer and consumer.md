### analysis
* 生产者-消费者问题
* 生产者和消费者之间对buffer的访问是互斥（exclusion）关系；
* 生产者生产之后，消费者才能消费，二者是同步（synchronization）关系；

### graph
```mermaid
graph TD;
    生产者-->buffer;
    buffer-->消费者;
```

### code
```
semaphore mutex = 1;  //临界区互斥信号量
semaphore empty = n;  //空闲缓冲区个数
semaphore full = 0;   //缓冲区初始化
```

#### producer process

```
producer(){
    while(1){
        produce an item in nextp; //生产数据
        P(empty);                 //空buffer个数-1
        P(mutex);                 //互斥夹紧
        add a nextp to buffer;
        V(mutex);                 //互斥加紧
        V(full);                  //满buffer个数+1
    }
}
```

#### consumer process

```
consumer(){
    while(1){
        P(full);                     //满buffer个数-1
        P(mutex);                    //互斥夹紧
        remove an item from buffer;  //从缓冲区中取的数据
        V(mutex);                    //互斥夹紧
        V(empty);                    //空buffer个数+1
        consume the item;            //消费数据
    }
}