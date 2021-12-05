# 数据类型

## 值类型

- bool 

- int

- int8 to int 256

- fixed/unfixed 定长浮点型
- fixedMxN





## 地址类型

表示以太坊地址，长度为20个字节，地址可以

使用 .balance方法获取余额

使用.transfer方法将余额转到另一个地址

## 引用类型/复合数据类型

- struct 结构体
- map 映射

# 变量

- 状态变量：永久保存在合约存储空间中的变量
- 局部变量：仅仅在函数执行过程中有效的变量
- 全局变量：保存在全局命名空间，用于获取  **区块链相关信息**   的特殊变量



状态变量，合约构造之下的变量

局部变量，在函数体内创建的变量







# 映射 (mapping)类型

可以理解为字典

```javascript
mapping(_KeyType => _ValueType)
```

- `_KeyType` – 可以是任何内置类型，或者bytes和字符串。不允许使用引用类型或复杂对象。
- `_ValueType` – 可以是任何类型。

```solidity
  mapping(address => Voter) public voters;
```

后面为变量名