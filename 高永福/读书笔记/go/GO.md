## Golang 

## 接口

声明的struct类型，将定义的Interface实现，就是接口

只要实现接口的结构体都可以接受

```
//接口的存在可以直接相等，不用相同类型
//接口实现的时候需要把下面的都实现
```

实现了泛型，因为interface没有类型，可以传任何东西

```
func Myfun(a interface{}){
   
}
```





```
package main

import "fmt"

type Animal interface{
   Eat()
   Run()

}

type Cat struct{
   Name string
   Sex bool
}

type Dog struct {
   Name string
}

func (c Cat)Run(){
   fmt.Print(c.Name,"Run")
}

func (c Cat)Eat(){
   fmt.Print(c.Name,"Eat")
}

func (d Dog)Run(){
   fmt.Print(d.Name,"Run")
}


var l Animal
func main(){
   var a Animal
   a = Cat{
      Name: "mao",
      Sex: false,
   }
   //接口的存在可以直接相等，不用相同类型
   //接口实现的时候需要把下面的都实现
   Myfun(a)
   l.Run()
   l.Eat()
   //Myfun(a)
}

func Myfun(a Animal){
   l = a
}
```

## goroutine和channel

协程

goroutine把程序单独跑到某个程序

channel不同协程之间进行通讯

在调用一个方法前前面+ go 就是协程

go提供协程管理器



### go语言等待组

记得传参的时候要传入地址，可以让这个程序在这个阶段执行

```
func main()  {

   //i:=0
   //go Run()
   var wg sync.WaitGroup
   wg.Add(1)
   go Run(&wg)
   wg.Wait()
   //for i<100{
   // i++
   // fmt.Print(i)
   //}

}

func Run(wg *sync.WaitGroup){
   fmt.Print("woshi")
   wg.Done()
}
```

### channel

有缓冲区1，可以存到一个东西



```
func main(){
   c1 := make(chan int,1)
   //1个缓冲区
   //c2 :=make(chan int)

   c1 <- 1
// 往里存
   fmt.Print(<- c1)
}
```



```
func main(){
   c1 := make(chan int)
   //1个缓冲区
   //c2 :=make(chan int)

   c1 <- 1
// 往里存
   fmt.Print(<- c1)
}
//如果没有缓冲区，
程序会在想要取出c1中的内容的时候死锁等待，并且创建一个缓冲区
因此可以写一个协程程序在旁边将内容存进去
```

channel的缓冲区

当缓冲区满了提交去取，缓冲区有一个空闲就会开始填充

channel chan是默认有一个缓冲区的，
