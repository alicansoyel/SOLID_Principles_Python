# SOLID Pensipleri

1. Single Responsibility Principle(Tekil Sorumluluk İlkesi): Bir sınıfın veya bir metodun tek bir görevi olmalıdır. Bir sınıf veya bir metot birden fazla görevi yerine getirmemelidir.

2. Open/Closed Principle(Açık/Kapalılık İlkesi): Yazılan bir sınıf veya metot gelişime/genişlemeye açık, değişime kapalı olmalıdır. Yazılan kod için bir geliştirme geldiğinde yazdığınız mevcut kodda yapıyı değiştirmemeniz gerekir.

3. Liskov's Substitution Principle(Liskov İkame İlkesi): Eğer aynı işlemleri gerçekleştiren birden fazla sınıfınız varsa bunlar kendi aralarında yer değiştirilebilir olacağından Liskov İkame İlkesine uygundur. Bu durumda ortak işlemler için bir base class yapılabilir.

4. Interface Segregation Principle(Arayüz Ayırma İlkesi): Ortak işlemlere sahip birden fazla sınıfınız var ve bu ortak sınıftan türeyen başka bir sınıfıza ait başka bir özellik kazandırmak istiyorsanız bunu da ayrı bir soyut sınıfta ilgili özelliği tanımlayıp bu özelliği almak isteyen sınıf için miras almasını sağlayabilirsiniz. Böylece arayüz ayırma ilkesini sağlamış olursunuz.

5. Dependecy Inversion Principle (Bağımlığı Tersine Çevirme İlkesi): Yüksek seviyeli modüllerin düşük seviyeli modüllere bağlı olmamalıdır. İki seviye, soyutlamalar üzerinden birbirine bağlı olmalıdır. Bu ilke, genellikle bir bağımlılıkların enjekte edildiği ve bu sayede daha az bağımlılık içeren kodun elde edildiği bir tasarım deseni olarak ifade edilir. Kısaca kodlama yazarken bağımlılık kaçınılmazdır. Bir sınıfın bir sınıfa bağımlı olması yerine bu bağımlılığın soyut sınıflar veya arayüzler üzerinden sağlanması daha doğru bir çözüm olacaktır.

****************************************************************************************************************************************************************************************************************************************************************************

# SOLID Principles

1. Single Responsibility Principle (SRP): A class or method should have only one responsibility. A class or method should not perform multiple tasks.

2. Open/Closed Principle (OCP): A class or method should be open for extension but closed for modification. When making changes or enhancements, you should not alter the existing code.

3. Liskov's Substitution Principle (LSP): If you have multiple classes that perform the same operations, they should be substitutable for each other. This principle suggests creating a base class for common operations.

4. Interface Segregation Principle (ISP): If you have multiple classes with common operations and want to add additional features to a class derived from this common class, you can define this feature in a separate abstract class. This way, the class that needs the additional feature can inherit it without being burdened by unnecessary functionalities.

5. Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules; both should depend on abstractions. This principle often involves injecting dependencies, resulting in code with fewer dependencies. In short, when writing code, dependency is inevitable, but it's better to provide dependencies through abstract classes or interfaces rather than a class depending directly on another class.
