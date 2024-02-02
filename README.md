# Flight Search App

Bu proje, uçuş arama uygulaması için bir Python tabanlı test otomasyonu içerir. Projede, hem API üzerinden gelen verileri kontrol eden bir test sınıfı (Test_Amadeus), hem de bir web uygulaması üzerindeki kullanıcı deneyimini test eden iki ayrı test sınıfı (Test_Listing ve Test_Search) bulunmaktadır.

## Kullanılan Teknolojiler

- Python 3
- Selenium WebDriver
- pytest
- requests
- openpyxl

## Kurulum

1. Python 3 yükleyin: [Python.org](https://www.python.org/downloads/)
2. Proje klasöründe terminali açın ve gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:

# Proje Fonksiyonları

Bu proje, uçuş arama uygulaması için bir Python tabanlı test otomasyonu içerir. Aşağıda projede yer alan önemli fonksiyonlar ve sınıflar bulunmaktadır:

## Test_Api Sınıfı

`Test_Amadeus` sınıfı, uçuş arama API'sini test etmek için kullanılır. Bu sınıf, belirli bir backend URL'sine istek gönderir ve gelen yanıtı kontrol eder. Aşağıdaki testleri içerir:

- `test_statusCode`: HTTP yanıt kodunu kontrol eder (200 olmalıdır).
- `test_contentType`: Yanıtın içerik türünü kontrol eder (JSON olmalıdır).
- `test_response_content_format`: Yanıtın içeriğinin doğru formatlara sahip olduğunu kontrol eder.

## Test_Listing Sınıfı

`Test_Listing` sınıfı, web uygulamasındaki liste işlevselliğini test etmek için kullanılır. Şu testi içerir:

- `test_found_items`: Belirli iki şehir arasında uçuşların listelendiğini doğrular. 

## Test_Search Sınıfı

`Test_Search` sınıfı, web uygulamasındaki arama işlevselliğini test etmek için kullanılır. Şu testi içerir:

- `test_from_to_same_place`: Aynı şehir hem 'From' hem de 'To' olarak seçilemez kuralını doğrular.

Her bir test sınıfı, belirli bir işlevselliği test etmek için tasarlanmıştır ve bu işlevselliklerin doğru çalıştığına emin olmak için kullanılır.


