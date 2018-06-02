<div dir="rtl" alighn="right">
این برنامه زمان زیرنویس ورودی رو از زمانی که بهش می‌گیم و به مقدار دلخواه به جلو و یا عقب می‌بره\

چطور ازش استفاده کنیم؟\
توی ترمینال به شکل زیر برنامه رو فرا می‌خونیم:
 </div>

```sh
 python3 subshifter.py -i '[input file]' -o '[output file]'

```
<div dir="rtl" alighn="right">
به عنوان مثال:
 </div>

```sh
 python3 subshifter.py -i 'test/Steins.Gate.01.[720BD].ass' -o 'test/test.ass'

```




<div dir="rtl" alighn="right">


بعد که برنامه رو اجرا کردیم به ترتب موارد زیر رو وارد می‌کنیم:

زمانی که می‌خوایم از اون به بعد زیرنویس جلو/عقب بره، [می‌تونیم ۰:۰:۰ رو وارد کنیم تا کل زیرنویس جا به جا بشه.]
 </div>

```sh
 Specify start point of shift in HH:MM:SS format: 0:0:0
 00:00:00
```

<div dir="rtl" alighn="right">
مقدار جا به جا شدن
 </div>

```sh
 Specify shift time in HH:MM:SS format: 0:1:0
 00:01:00
```
<div dir="rtl" alighn="right">
جهت جا به جایی رو به جلو یا عقب
 </div>

```sh
 Delay - or + ? defult is - [-/+]: +
 delay: + -->
```
<div dir="rtl" alighn="right">
در انتها کاش یک جوانمرد پیدا بشه GUI براش بسازه و برنامه رو همه‌گانی/کابرپسند کنه.
 </div>
