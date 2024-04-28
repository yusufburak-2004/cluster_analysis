# Penguins Dataset Analysis

Bu proje, `penguins` veri seti üzerinde bir dizi veri analizi işlemi gerçekleştirmeyi amaçlamaktadır. Veri seti, Antarktika'daki Palmer Archipelago'da bulunan 3 pengu türünün (Adelie, Chinstrap ve Gentoo) özelliklerini içerir.

## Proje Adımları

1. **Veri Yükleme ve Temizleme**: İlk olarak, veri seti yüklendi ve eksik değerler kaldırıldı. Ayrıca, flipper uzunluğu değişkeni üzerinde outlier'lar belirlenip temizlendi.

2. **Veri Ön İşleme**: Veri seti, kategorik değişkenlerin işlenmesi için dummy değişkenlere dönüştürüldü ve ardından standartlaştırıldı.

3. **Boyut Azaltma (PCA)**: PCA (Principal Component Analysis) yöntemi kullanılarak veri setinin boyutu azaltıldı. Böylece, veri setindeki varyansın büyük bir kısmını korurken, boyut azaltılarak analiz süresi ve işlem karmaşıklığı azaltıldı.

4. **Kümeleme (K-Means)**: Kümeleme algoritması olan K-Means kullanılarak veri seti kümelere ayrıldı. Bu adım, benzer özelliklere sahip veri noktalarını gruplamak için yapıldı.

5. **Sonuçların Görselleştirilmesi**: Kümeleme sonuçları, küme sayısı ve PCA tarafından azaltılan boyuta göre görselleştirildi.

6. **Küme İstatistikleri**: Kümeleme sonuçlarına dayanarak, her küme için ortalama özellik değerleri hesaplandı ve bu istatistikler görselleştirildi.

## Sonuçlar

Elde edilen sonuçlar, veri setindeki penguin türlerinin belirli özellikler açısından nasıl gruplandığını göstermektedir. Kümeleme sonuçları, farklı penguin türlerinin belirli özelliklere sahip olduğunu ve bu özellikler açısından birbirinden nasıl farklılaştığını göstermektedir.
