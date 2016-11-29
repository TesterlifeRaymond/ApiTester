#	这是一个读取excel 和csv 之后 做对比的脚本

### 使用python库包含

* xlrd
* csv
// 如果使用多线程及队列

* queue
* threading


// files  放置需要对比的两个文件

// service/controller  单步操作 --- 读取、对比

// util/my_queue   在加入多线程服务的时候， 可以将controller文件的Excel类继承 执行多线程对比操作



