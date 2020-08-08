# Image Processing Create And Dublicate Dataset
Yeni resim dataları üretme ya da çoğaltma programıdır.

## Proje Test Videosu
<video width="320" height="240" controls>
  <source src="info_video.mp4" type="images/mp4">
</video>

## Projede Kullanılan IDE'ler ve İndirme Linki

<ul>
  <li>Proje Python 3 ile yazılmıştır.</li>
  <li>Python3 
   <ul>
    <li> İndirme Linki: https://www.python.org/downloads/ </li>
   </ul>
  </li>
  <li>Anaconda & Spyder
    <ul>
      <li>İndirme Linki: https://www.anaconda.com/distribution/ </li>
    </ul>  
  </li>
  <li>PyCharm
   <ul>
    <li>İndirme Linki: https://www.jetbrains.com/pycharm/download/#section=windows </li>
   </ul>  
  </li>
 <li>Visual Studio Code
  <ul> 
    <li> İndirme Linki: https://code.visualstudio.com/ </li>
  </ul>
 </li>
</ul>
 
## Projenin Çalışması İçin Gerekli Kütüphaler ve İndirme Linkleri
<ul>
  <li>OpenCV
    <ul>
          <li><code>pip install opencv-python</code></li>
        </ul>  
  </li>
  <li>PyQt5</li>
    <ul>
          <li><code>pip install PyQt5</code></li>
   </ul>  
  </li>
  </li>
  <li>Scipy</li>
    <ul>
          <li><code>pip install scipy</code></li>
   </ul>  
  </li>
  <li>Skimage</li>
    <ul>
          <li><code>pip install skimage</code></li>
   </ul>  
  </li>
</ul>

## Proje Çalıştığında Açılan Sayfalar
<ul>
  <li>mainWindows.py dosyasını çalıştırdığınızda anasayfa açılıyor.</li>
</ul>
<img src= "https://github.com/celalakcelikk/Image_processing_create_and_dublicate_dataset/blob/master/images/mainwindows.PNG">
<p> Yukarıdaki resimde görüldüğü gibi gerekli parametreleri halledince "CONTROL" butonuna basınca, parametreleri kontrol sayfası açılmaktadır.

#### Parametrelerin Açıklaması
<p>Sırayla:</p>
<ul>
  <li>İlk satır dataların kaydedileceği klasörü seçmeniz gerekiyor.</li>
  <li>İkinci satır dataların sınıf adları olan .txt uzantılı dosyayı seçmemize yarıyor.</li>
  <li>Üçüncü satır kaç tane aynı sınıftan resim üreteceğimizi yazmamıza yarıyor.Not: Data çoğaltmada işe yaramıyor. Ama boş bırakmayınız.</li>
  <li>Dördüncü satır birinci sütun data işlemini seçmemize yarıyor.</li>
  <li>Dördüncü satır ikinci sütun datanın kayıt edilecek uzantısını seçmemize yarıyor.</li>
  <li>Beşinci satır kamerada yapılacak işlemi göstermede yardımcı datayı seçmemize yarıyor.</li>
</ul>
  
## Yeni Resim Üretme

<img src="https://github.com/celalakcelikk/Image_processing_create_and_dublicate_dataset/blob/master/images/createimagewindows.png" >

## Var olan Resimleri Çoğaltma
### Çoğaltama Parametreleri Ekleme Sayfası
<img src="https://github.com/celalakcelikk/Image_processing_create_and_dublicate_dataset/blob/master/images/augmentedwindows.png" >
<ul><li>Çoğaltma paramtrelerini test etmek için "Augmented Image Control" butonuna tıklayıp kontrol yapılabilir.</li></ul>
<ul><li>Çoğaltma işlemini başlatmak için "Augmented Image" butonuna tıklayıp kontrol yapılabilir.</li></ul>

#### Çoğaltma Parametreleri Kontrol Etme Sayfası
<img src="https://github.com/celalakcelikk/Image_processing_create_and_dublicate_dataset/blob/master/images/augmentedTestWindows.png" >

#### Resimleri Çoğaltma Sayfası
<img src="https://github.com/celalakcelikk/Image_processing_create_and_dublicate_dataset/blob/master/images/createaugmentedwindows.png" >
