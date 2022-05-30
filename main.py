PPow: = 10;

PHp: = 100;

Plovk: = 2;

MPow: = 5;

MHp: = 50;

Mlovk: = 3;

Randomize; // запуск
случайного
генератора
чисел

if random(100) + 1 <= Mlovk then

form1.caption := 'Монстр уклонился от удара';



if random(100) + 1 >= Mlovk then

MHp := MHp - Ppow;

Randomize; // запуск
случайного
генератора
чисел

if random(100) + 1 <= Plovk then

form1.caption := 'Персонаж уклонился от удара';



if random(100) + 1 >= Plovk then

PHp := PHp - Mpow;

MToch := 40;

PToch := 60;
Randomize; // запуск
случайного
генератора
чисел

if random(100) + 1 <= Ptoch then

// если
персонаж
попал
точно
в
цель
тогда
и
проверяем

// уклонится
ли
враг
от
удара
или
нет

begin

if random(100) + 1 <= Mlovk then

form1.caption := 'Монстр уклонился от удара';



if random(100) + 1 >= Mlovk then

MHp := MHp - Ppow;

end;
Randomize; // запуск
случайного
генератора
чисел

if random(100) + 1 <= Mtoch then

begin

if random(100) + 1 <= Plovk then

form1.caption := 'Персонаж уклонился от удара';



if random(100) + 1 >= Plovk then

PHp := PHp - Mpow;

end;
