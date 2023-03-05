# GitHub个人主页
## CSS布局与定位之浮动定位
### 1行1列
#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mysite</title>
    <link rel="stylesheet" href="css/style.css" />
</head>
<body>
    <div id="container">
    </div>
</body>
</html>
```
#### style.css
```css
/*首先对浏览器默认的样式进行清零*/
*{
    padding: 0;
    margin: 0;
}
/*设置页面的基本的一些样式*/
body{
    font-size: 14px;
}
/*定义container的样式最重要*/
#container{
    /*将最外层的这个容器在页面上居中*/
    margin: 0 auto;
    /*定义当前页面的一个宽度|有时页面的内容放在这个容器里，它所占据的宽度*/
    width: 1000px;
    height: 500px;
    /*背景颜色：蓝色*/
    background-color: #6cf;
}
```
### 3行1列
#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mysite</title>
    <link rel="stylesheet" href="css/style.css" />
</head>
<body>
    <div id="container">
        <div id="header"></div>
        <div id="main"></div>
        <div id="footer"></div>
    </div>
</body>
</html>
```
#### style.css
```css
/*首先对浏览器默认的样式进行清零*/
*{
    padding: 0;
    margin: 0;
}
/*设置页面的基本的一些样式*/
body{
    font-size: 14px;
}
/*定义container的样式最重要*/
#container{
    /*将最外层的这个容器在页面上居中*/
    margin: 0 auto;
    /*定义当前页面的一个宽度|有时页面的内容放在这个容器里，它所占据的宽度*/
    width: 1000px;
    height: 500px;
    /*背景颜色：蓝色*/
    /*background-color: #6cf;*/
}
#header{
    height: 100px;
    background-color: #6cf;
    margin-bottom: 5px;
}
#main{
    height: 500px;
    background-color: #cff;
    margin-bottom: 5px;
}
#footer{
    height: 60px;
    /*背景颜色：蓝色*/
    background-color: #6cf;
}
```
### 1行2列
#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mysite</title>
    <link rel="stylesheet" href="css/style.css" />
</head>
<body>
<div id="container">
    <div id="aside"></div>
    <div id="content"></div>
</div>
</body>
</html>
```
#### style.css
```css
/*首先对浏览器默认的样式进行清零*/
*{
    padding: 0;
    margin: 0;
}
/*设置页面的基本的一些样式*/
body{
    font-size: 14px;
}
/*定义container的样式最重要*/
#container{
    /*将最外层的这个容器在页面上居中*/
    margin: 0 auto;
    /*定义当前页面的一个宽度|有时页面的内容放在这个容器里，它所占据的宽度*/
    width: 1000px;
    height: 500px;
    /*背景颜色：蓝色*/
    /*background-color: #6cf;*/
}
#aside{
    float: left;
    width: 300px;
    height: 500px;
    /*蓝色*/
    background-color: #6cf;
}
#content{
    float: left;
    width: 695px;
    height: 500px;
    background-color: #cff;
    margin-left: 5px;
}
```
### 3行2列
#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mysite</title>
    <link rel="stylesheet" href="css/style.css" />
</head>
<body>
<div id="container">
    <div id="header"></div>
    <div id="main">
        <div id="aside"></div>
        <div id="content"></div>
    </div>
    <div id="footer"></div>
</div>
</body>
</html>
```
#### style.css
```css
/*首先对浏览器默认的样式进行清零*/
*{
    padding: 0;
    margin: 0;
}
/*设置页面的基本的一些样式*/
body{
    font-size: 14px;
}
/*定义container的样式最重要*/
#container{
    /*将最外层的这个容器在页面上居中*/
    margin: 0 auto;
    /*定义当前页面的一个宽度|有时页面的内容放在这个容器里，它所占据的宽度*/
    width: 1000px;
    height: 500px;
    /*背景颜色：蓝色*/
    /*background-color: #6cf;*/
}
#header{
    height: 100px;
    background-color: #6cf;
    margin-bottom: 5px;
}
#main{
    height: 500px;
    /*background-color: #cff;*/
    margin-bottom: 5px;
}
#aside{
    float: left;
    width: 300px;
    height: 500px;
    /*蓝色*/
    background-color: #6cf;
}
#content{
    float: left;
    width: 695px;
    height: 500px;
    background-color: #cff;
    margin-left: 5px;
}
#footer{
    height: 60px;
    /*背景颜色：蓝色*/
    background-color: #6cf;
}
```
### 4行3列
#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mysite</title>
    <link rel="stylesheet" href="css/style.css" />
</head>
<body>
<div id="container">
    <div id="header"></div>
    <div id="nav"></div>
    <div id="main">
        <div id="aside1" class="aside"></div>
        <div id="content"></div>
        <div id="aside2" class="aside"></div>
    </div>
    <div id="footer"></div>
</div>
</body>
</html>
```
#### style.css
```css
/*首先对浏览器默认的样式进行清零*/
*{
    margin: 0;
    padding: 0;
}
/*设置页面的基本的一些样式*/
body{
    font-family: "微软雅黑", serif;
    font-size: 14px;
}
/*定义container的样式最重要*/
#container{
    /*将最外层的这个容器在页面上居中*/
    margin: 0 auto;
    /*定义当前页面的一个宽度|有时页面的内容放在这个容器里，它所占据的宽度*/
    width: 900px;
    /*height: 500px;*/
    /*背景颜色：蓝色*/
    /*background-color: #6cf;*/
}
#header{
    height: 100px;
    background-color: #6cf;
    margin-bottom: 5px;
}
#nav{
    height: 30px;
    background: #09c;
    margin-bottom: 5px;
}
#main{
    height: 500px;
    /*background-color: #cff;*/
    margin-bottom: 5px;
}
.aside{
    float: left;
    width: 100px;
    height: 500px;
    /*蓝色*/
    background-color: #6cf;
}
#aside1{

}
#aside2{
    margin-left: 5px;
}
#content{
    float: left;
    margin-left: 5px;
    width: 690px;
    height: 500px;
    background-color: #cff;
}
#footer{
    height: 60px;
    /*背景颜色：蓝色*/
    background-color: #6cf;
}
```
## 案例
### 布局
#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mysite</title>
    <link rel="stylesheet" href="css/style.css" />
</head>
<body>
<div id="container">
    <div id="header"></div>
    <div id="nav"></div>
    <div id="main">
        <div id="aside"></div>
        <div id="content"></div>
    </div>
    <div id="footer"></div>
</div>
</body>
</html>
```
#### style.css
```css
*{
    margin: 0;
    padding: 0;
}
body{
    font-size: 16px;
    color: #673929;
}
#container{
    margin: 0 auto;
    width: 900px;
}
#header{
    height: 220px;
    background-color: #6cf;
    margin-bottom: 5px;
}
#nav{
    height: 30px;
    margin: 5px;
    background-color: #09c;
    font-size: 18px;
    line-height: 30px;
    color: #fff;
    letter-spacing: 2px;
    text-align: center;
}
#main{
    height: 2050px;
    background-color: #000;
}
#aside{
    float: left;
    width: 300px;
    height: 500px;
    /*蓝色*/
    background-color: #6cf;
    text-align: center;
    font-size: 14px;
}
#content{
    float: right;
    width: 595px;
    height: 2050px;
    margin-bottom: 5px;
    background-color: #cff;
}
#footer{
    height: 60px;
    line-height: 60px;
    background-color: #6cf;
    clear: both;
    text-align: center;
}
```
### header + nav
#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mysite</title>
    <link rel="stylesheet" href="css/style.css" />
</head>
<body>
<div id="container">
    <div id="header">
        <img src="css/images/header.jpg" alt="header.jpg">
    </div>
    <div id="nav">
        <a href="#">一</a>
        <a href="#">二</a>
        <a href="#">三</a>
        <a href="#">四</a>
        <a href="#">五</a>
    </div>
    <div id="main">
        <div id="aside"></div>
        <div id="content"></div>
    </div>
    <div id="footer"></div>
</div>
</body>
</html>
```
#### style.css
```css
*{
    margin: 0;
    padding: 0;
}
body{
    font-size: 16px;
    color: #673929;
}
#container{
    margin: 0 auto;
    width: 900px;
}
#header{
    height: 220px;
    background-color: #6cf;
    margin-bottom: 5px;
}
#nav{
    height: 30px;
    line-height: 30px;
    margin: 5px;
    background-color: #09c;
    font-size: 18px;
    color: #fff;
    letter-spacing: 2px;
    text-align: center;
}
a{
    text-decoration: none;
}
a:link{
    color: #fff;
}
a:visited{
    color: #fff;
}
a:hover{
    color: yellow;
}
a:active{
    color: yellow;
}
#main{
    height: 2050px;
    background-color: #000;
}
#aside{
    float: left;
    width: 300px;
    height: 500px;
    /*蓝色*/
    background-color: #6cf;
    text-align: center;
    font-size: 14px;
}
#content{
    float: right;
    width: 595px;
    height: 2050px;
    margin-bottom: 5px;
    background-color: #cff;
}
#footer{
    height: 60px;
    line-height: 60px;
    background-color: #6cf;
    clear: both;
    text-align: center;
}
```
