### museum process
```
semaphore mutex = 1;                       //设置出入口访问的信号量
semaphore empty = 500;                     //博物馆可同时容纳人数

Visitori(){
    while(1){
        P(empty);  //博物馆容纳人数-1
        P(door);   //阻止其他游客出入
        go into the museum;
        V(door);   //允许其他游客出入
        sightseeing;
        P(door);
        leave the museum;
        V(door);
        V(empty);  //博物馆容纳人数+1
    }
}
```

###  factory problem
```
semaphore empty1 = 10;
semaphore empty2 = 10;
semaphore full1 = 0;
semaphore full2 = 0;
semaphore mutex1 = 1;
semaphore mutex2 = 1;

productive_section1(){
    while(1){
        P(empty1);
        P(mutex1);
        put A;
        V(mutex1);
        V(full1);
    }
}

productive_section2(){
    while(1){
        P(empty2);
        P(mutex2);
        put B;
        V(mutex2);
        V(full2);
    }
}

assembly_worker(){
    while(1){
        P(full1)
        P(mutex1);
        take A;
        V(mutex1);
        V(empty1);

        P(full2)
        P(mutex2);
        take B;
        V(mutex2);
        V(empty2);

        assemble the parts;
    }
}
```

### monk drinking

```
semaphore empty = 10;
semaphore full = 0;
semaphore barrel = 3;
semaphore mutex1 = 1;
semaphore mutex2 = 1;

little_monk_i(){
    while(1){
        P(empty);
        P(barrel);
        P(mutex1);
        take water from the well;
        V(mutex1);

        P(mutex2);
        Pour the water into the cylinder;
        V(mutex2);

        V(barrel);
        V(full);
    }
}

old_monk_i(){
    while(1){
        P(full);
        P(barrel);
        P(mutex2);
        take water from the cylinder;
        V(mutex2);
        V(empty);
        drinking;
        V(barrel);
    }

}
```


### car-bridge problem
```
semaphore bridge = 1;

north_to_south(){
    while(1){
        P(bridge);
        pass the bridge;
        V(bridge);
    }
}

south_to_north(){
    while(1){
        P(bridge);
        pass the bridge;
        V(bridge);
    }
}
```

```
semaphore seat = 100;
semaphore mutex = 1;

reader(){
    while(1){
        P(seat);
        P(mutex);
        sign up;
        V(mutex);
        read;
        P(mutex);
        log out;
        V(mutex);x
        V(seat);
    }
}
```