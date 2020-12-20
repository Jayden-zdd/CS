# HTML
## 1. 基础知识

### 1.1 元素
\<br> 换行,\<p>等  
>***块元素：header, section, footer, aside, nav, main, article, figure，根据语义猜页面布局，以下是新加功能：***
>>* \<canvas> 标签只是图形容器（画布），必须使用脚本来绘制图形。
>>* \<SVG>可以加入可伸缩的矢量型图片
>>* \<math>加入可以编辑显示数学工公式
>>* 加入drop和drag的function可以拖放对象到另一个位置
>>* getCurrentPosition() 方法来获得用户的位置
>>* video, audio
>>* web存储与数据库交互
>>* 页面执行脚本时页面状态是不可以响应的，直到脚本完成。web worker是运行在后台的js不影响页面性能
### 1.2 属性
class: 为html元素定义一个或多个类名（classname）(类名从样式文件引入)
id: 定义元素的唯一id
style: 规定元素的行内样式（inline style）
title: 描述了元素的额外信息 (作为工具条使用)
### 1.3 字体
\<b>和\<i>对应粗体和斜体，如今被\<strong>和\<em>代替，但含义并不相同。\<strong>和\<em>意味呈现文本是重要的
特殊字符：大于（&gt;）小于号（&lt;），
### 1.4 链接href
\<a id="tips">有用的提示部分\</a>
\<a href="#tips">访问有用的提示部分\</a>
\<a href="https://www.runoob.com/html/html-links.html#tips">访问有用的提示部分\</a>
### 1.5 图像img
src图片路径，alt图片资源未加载出来时显示文字内容
### 1.6 表格table
\<table>开始，\<th>表头，\<tr>每一行，\<td>每一列，从左上到右下排列
### 1.7 列表
1.7.1 \<ul>无序列表，\<ol>有序，都需要\<li>表示每一项
    \<ul>
    \<li>Coffee</li>
    \<li>Milk</li>
    \</ul>
1.7.2 自定义列表
自定义列表以 \<dl> 标签开始。每个自定义列表项以 \<dt> 开始。每个自定义列表项的定义以 \<dd> 开始。
    \<dl>
    \<dt>Coffee</dt>
    \<dd>- black hot drink</dd>
    \<dt>Milk</dt>
    \<dd>- white cold drink</dd>
    \</dl>
### 1.8 区块div和span
\<div>：用于组合其他html元素，并无特殊意义
\<span>: 用于文本的容器，也无特殊意义
### 1.9 表单form
表单元素有文本框，下拉框，单选框和多选框等等，通过type类型（password,raido,checkbox,submit）来选择
\<form>
name: \<input type="text" name="tname"><br>\</form>
>***新的表单元素：***
* \<datalist>规定输入域的选项列表，比如下拉框的所有项
* \<keygen>密钥生成，提交表单会生成两个键，私钥存储在客户端，公钥发送到服务器
* \<output>不同类型的输出
>***新的表单属性：***
>>\<form>新加了autocomplete（文本框显示历史输入）和novalidate（不验证输入数据值）
>>\<input>新加了 autofocus等属性


### 1.10 框架iframe
\<iframe src="demo_iframe.htm" width="200" height="200"></iframe>
### 脚本script
\<script> 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件,脚本用于图片操作、表单验证和内容动态更新
### 1.11 H5
\<!DOCTYPE html>必须第一行声明，新加特性**粗斜体**标出
>***引入应用程序缓存***
    \<!DOCTYPE HTML>
    \<html manifest="demo.appcache">
### 1.12 注释
\<!-- comment -->

## 2. CSS
CSS在Html4中开始使用，通入以下方式引入：
* 内联样式：在HTML元素中使用“style”
* 内部样式表：在HTML的HEAD部分使用\<style>元素来包含CSS,适用于**单个文档需要特殊样式**
* 外部样式表：外部CSS文件（最佳方式）\<link rel="stylesheet" type="text/css"href="mystyle.css">，适用于**应用在多个页面**
### 2.1 背景
body {background-color:#b0c4de;},  
body {background-image:url('paper.gif');}
### 2.2 文本
    body {color:red;},  
    h1 {text-align:center;},  
    h3 {text-decoration:underline;}主要设置链接的下划线,  
    p.uppercase {text-transform:uppercase;},  
    p {text-indent:50px;}缩进,
    p{font-family:"Times New Roman", Times, serif;},  
    p.italic {font-style:italic;},  
    p {font-size:14px;},  
    p {font-size:0.875em;} /* 14px/16=0.875em */,  
    body {font-size:100%;}
### 2.3 链接
    a:link {color:#000000;}      /* 未访问链接*/  
    a:visited {color:#00FF00;}  /* 已访问链接 */  
    a:hover {color:#FF00FF;}  /* 鼠标移动到链接上 */  
    a:active {color:#0000FF;}  /* 鼠标点击时 */ 
### 2.4 列表
ul.a {list-style-type: circle;}  
ol.c {list-style-type: upper-roman;}
### 2.5 表格
    table, th, td  
    {  
        border: 1px solid black;   
        width:100%;  
        height:50px;  
        text-align:right;   
    }
### 2.6 盒子
    从里到外：  
    div {  
        width: 300px;实际显示内容  
        padding: 25px;内边距，内边距是透明的  
        border: 25px solid green;边框  
        margin: 25px;外边距，外边距是透明的  
    }
### 2.7 Display和Visibility
display属性设置一个元素应如何显示，visibility属性指定一个元素应可见还是隐藏,但是visibility仍然占用空间  
h1.hidden {display:none;}  
h1.hidden {visibility:hidden;}
### 2.8 定位Position和布局Overflow
static,relative,fixed,absolute,sticky  
overflow 属性用于控制内容溢出元素框时显示的方式
### 2.9 下拉框
    <style>
    .dropdown {
        position: relative;
        display: inline-block;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        padding: 12px 16px;
        z-index: 1;
    }

    .dropdown:hover .dropdown-content {
        display: block;
    }
    </style>
### 2.10 表单
    input[type=text], select {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
### 2.11 注释
/* comment */
## 3 JavaScript
### 3.1 js显示数据
js没有打印或者输出的函数，但是可以使用 一下方式输出信息：
* window.alert()弹出警告框
* document.write()方法将内容写到 HTML 文档中
* innerHTML 写入到 HTML 元素
* console.log() 写入到浏览器的控制台。
### 3.2 数据类型    
#### 基本类型：字符串（String）、数字(Number)、布尔(Boolean)、对空（Null）、未定义（Undefined）、Symbol
    var length = 16;// Number 通过数字字面量赋值
    var points = x * 10;// Number 通过表达式字面量赋值
    var lastName = "Johnson";// String 通过字符串字面量赋值，字符串长度lastname.length
    Undefined 表示变量不含有值,可以将变量值设为 null 来清空变量
    Symbol 是 ES6 引入了一种新的原始数据类型，表示独一无二的值。
#### 引用数据类型：对象(Object)、数组(Array)、函数(Function)
    var cars = ["Saab", "Volvo", "BMW"];// Array  通过数组字面量赋值;var cars=new Array();
    var person = {firstName:"John", lastName:"Doe"};// Object 通过对象字面量赋值
    三种对象类型：Object,Date,Array
#### typeof查看变量类型
    typeof 3.14     // 返回 number     
#### 类型强转
    String(123) 和（123).toString()
    Number("3.14"),parseFloat(),parseInt()
**注意：js区分大小写,语句间需要分号隔开**
### 3.3 正则表达式RE
#### /正则表达式主体/修饰符(可选)
    i	执行对大小写不敏感的匹配。
    g	执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。
    m	执行多行匹配。
    var str = "Visit Runoob!"; 
    var n = str.search(/Runoob/i);
> test()方法：  
    var patt = /e/;  
    patt.test("The best things in life are free!");
    返回true  
> exec()方法： 
    /e/.exec("The best things in life are free!");  
    返回一个数组，其中存放匹配的结果。如果未找到匹配，则返回值为 null。
### 3.4 Json: JavaScript Object Notation
> JSON.parse()用于将一个 JSON 字符串转换为 JavaScript 对象
> JSON.stringify()用于将 JavaScript 值转换为 JSON 字符串
### 3.5 异步编程
> 回调函数
    function print() {
    document.getElementById("demo").innerHTML="RUNOOB!";
}
setTimeout(print, 3000);
> ajax:所有现代浏览器均支持 XMLHttpRequest 对象,XMLHttpRequest 用于在后台与服务器交换数据。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。
### 3.6 闭包
#### 作用：一个是前面提到的可以读取函数内部的变量，另一个就是让这些变量的值始终保持在内存中。
    function f1(){
        var n=999;
    　　function f2(){
        　　alert(n);　
        }
        return f2;
    }
    var result=f1();
    result(); // 999 


### 3.7 注释
> 单行：// coment  
> 多行：/* coment */




