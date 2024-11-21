# Cripto Projesi

Bu proje, kriptografik işlevler ve dijital imza işlemleri ile ilgili çeşitli Python dosyalarını içermektedir. Proje, verileri şifreleme, dijital imza oluşturma, hash doğrulama, GUI (grafiksel kullanıcı arabirimi) ile etkileşimli işlem yapma gibi özellikler sunmaktadır. Aşağıda projenin içerdiği dosyalar ve bunların ne yaptığı açıklanmıştır.

## Dosya Yapısı

### 1. `data.png`
Bu dosya, proje kapsamında kullanılan örnek bir görsel dosyadır. Dijital imza ve şifreleme testlerinde görsel olarak kullanılabilir.

### 2. `Dsa_Fun.py`
Bu dosya, Dijital İmza Algoritması (DSA) işlemlerini gerçekleştiren fonksiyonları içerir. Bu dosyada, imza oluşturma ve imza doğrulama işlemleri gerçekleştirilir.

### 3. `Dsa_Signature.py`
Bu dosya, DSA algoritmasını kullanarak dijital imza oluşturur. Verilen mesaj üzerinde bir imza oluşturur ve imzayı metin dosyasına kaydeder.

### 4. `Gui.py`
Bu dosya, kullanıcı ile etkileşime girebilmek için bir GUI (grafiksel kullanıcı arabirimi) sağlar. Kullanıcı, bu arabirim aracılığıyla şifreleme ve imza oluşturma işlemleri yapabilir.

### 5. `Gui2.py`
Bu dosya, `Gui.py` dosyasının başka bir versiyonudur veya ek fonksiyonlar içeren bir GUI uygulamasıdır. Kullanıcı etkileşimini genişletmek amacıyla oluşturulmuş olabilir.

### 6. `Hash_Check.py`
Bu dosya, bir veri parçasının hash değerini hesaplar ve bu hash değeri ile doğrulama yapar. Bu, veri bütünlüğünü kontrol etmek için kullanılır.

### 7. `imza.txt`
Bu dosya, dijital imza ile şifrelenmiş veriyi saklamak için kullanılır. `Dsa_Signature.py` tarafından üretilen dijital imzalar burada kaydedilir.

### 8. `Key_Create.py`
Bu dosya, şifreleme işlemleri için gerekli olan anahtarları oluşturur. Genellikle RSA veya benzeri algoritmalar için anahtar çifti oluşturulmasına yardımcı olur.

### 9. `Main.py`
Bu dosya, projenin ana yürütme dosyasını temsil eder. Projenin temel işlevleri burada başlatılır. Kullanıcı etkileşimi ve diğer modüllerle entegrasyon bu dosyada yönetilir.
