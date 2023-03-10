# patterns

№1
Фабричный метод
Также известен как: Виртуальный конструктор, Factory Method

Фабричный метод — это порождающий паттерн проектирования, который определяет общий интерфейс для создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.

Представьте, что вы создаёте программу управления грузовыми перевозками. Сперва вы рассчитываете перевозить товары только на автомобилях. Поэтому весь ваш код работает с объектами класса Грузовик. В какой-то момент ваша программа становится настолько известной, что морские перевозчики выстраиваются в очередь и просят добавить поддержку морской логистики в программу. Проблема с добавлением нового класса в программу
Добавить новый класс не так-то просто, если весь код уже завязан на конкретные классы.

Отличные новости, правда?! Но как насчёт кода? Большая часть существующего кода жёстко привязана к классам Грузовиков. Чтобы добавить в программу классы морских Судов, понадобится перелопатить всю программу. Более того, если вы потом решите добавить в программу ещё один вид транспорта, то всю эту работу придётся повторить.

В итоге вы получите ужасающий код, наполненный условными операторами, которые выполняют то или иное действие, в зависимости от класса транспорта.

Решение
Паттерн Фабричный метод предлагает создавать объекты не напрямую, используя оператор new, а через вызов особого фабричного метода. Не пугайтесь, объекты всё равно будут создаваться при помощи new, но делать это будет фабричный метод.

Структура классов-создателей
Подклассы могут изменять класс создаваемых объектов.

На первый взгляд, это может показаться бессмысленным: мы просто переместили вызов конструктора из одного конца программы в другой. Но теперь вы сможете переопределить фабричный метод в подклассе, чтобы изменить тип создаваемого продукта.

Чтобы эта система заработала, все возвращаемые объекты должны иметь общий интерфейс. Подклассы смогут производить объекты различных классов, следующих одному и тому же интерфейсу.

Структура иерархии продуктов
Все объекты-продукты должны иметь общий интерфейс.

Например, классы Грузовик и Судно реализуют интерфейс Транспорт с методом доставить. Каждый из этих классов реализует метод по-своему: грузовики везут грузы по земле, а суда — по морю. Фабричный метод в классе ДорожнойЛогистики вернёт объект-грузовик, а класс МорскойЛогистики — объект-судно.

Программа после применения фабричного метода
Пока все продукты реализуют общий интерфейс, их объекты можно взаимозаменять в клиентском коде.

Для клиента фабричного метода нет разницы между этими объектами, так как он будет трактовать их как некий абстрактный Транспорт. Для него будет важно, чтобы объект имел метод доставить, а как конкретно он работает — не важно.


№2
Паттерн Приспособленец (Flyweight) - структурный шаблон проектирования, который позволяет использовать разделяемые объекты сразу в нескольких контекстах. Данный паттерн используется преимущественно для оптимизации работы с памятью.

В качестве стандартного применения данного паттерна можно привести следующий пример. Текст состоит из отдельных символов. Каждый символ может встречаться на одной странице текста много раз. Однако в компьютерной программе было бы слишком накладно выделять память для каждого отдельного символа в тексте. Гораздо проще было бы определить полный набор символов, например, в виде таблицы из 128 знаков (алфавитно-цифровые символы в разных регистрах, знаки препинания и т.д.). А в тексте применить этот набор общих разделяемых символов, вместо сотен и тысяч объектов, которые могли бы использоваться в тексте. И как следствие подобного подхода будет уменьшение количества используемых объектов и уменьшение используемой памяти.

Паттерн Приспособленец следует применять при соблюдении всех следующих условий:

Когда приложение использует большое количество однообразных объектов, из-за чего происходит выделение большого количества памяти

Когда часть состояния объекта, которое является изменяемым, можно вынести во вне. Вынесение внешнего состояния позволяет заменить множество объектов небольшой группой общих разделяемых объектов.

Ключевым моментом здесь является разделение состояния на внутренне и внешнее. Внутреннее состояние не зависит от контекста. В примере с символами внутреннее состояние описывается кодом символа из таблицы кодировки. Так как внутреннее состояние не зависит от контекста, то оно может быть разделяемым и поэтому выносится в разделяемые объекты.

Внешнее состояние зависит от контекста, является изменчивым. В применении к символам внешнее состояние может представлять положение символа на странице. То есть код символа может быть использован многими символами, тогда как положение на странице будет для каждого символа индивидуально.

При создании приспособленца внешнее состояние выносится. В приспособленце остается только внутреннее состояние. То есть в примере с символами приспособленец будет хранить код символа.

№3
Наблюдатель — поведенческий шаблон проектирования. Также известен как «подчинённые». Реализует у класса механизм, который позволяет объекту этого класса получать оповещения об изменении состояния других объектов и тем самым наблюдать за ними.

№4
Одиночка
Шаблон Одиночка используется, если нужны гарантии, что существует единственный экземпляр данного класса. Во время выполнения программы не должны появляться другие. На самом деле, в Python проще намеренно создать один экземпляр, а затем использовать его.

Python позволяет вносить изменения в процесс создания экземпляра класса. Для этого существует метод __new__. Им и нужно воспользоваться для реализации паттерна Одиночка.



#5 
Паттерн «Декоратор» позволяет динамически добавлять объекту новые обязанности, не прибегая при этом к порождению классов. При этом, работа с подобной структурой является более удобной и гибкой, нежели со множеством классов. Для этого, ссылка на декорируемый объект помещается в другой класс, называемый «Декоратором». Причем, и декоратор и декорируемый объект реализуют один и тот-же интерфейс, что позволяет вкладывать несколько декораторов друг в друга, добавляя тем самым декорируемому объекту любое число новых обязанностей. Декоратор переадресует внешние вызовы декорируему объекту сопровождая их наложением дополнительных обязанностей.
